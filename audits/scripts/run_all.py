#!/usr/bin/env python3
"""
English Skill-Building Drive — programmatic audit suite (Run Book §6.5 / §6.8 / §6.11).

Usage:
    python3 run_all.py <manifest.json> [--file2 <path.xlsx>] [--report-dir <dir>]

The manifest is a machine-readable extraction of every graded answer set, item text,
stated mark total, and dictation list from the draft sheets. Schema:
audits/scripts/README_manifest.md

Exit code 0 = all gates PASS (human-review flags may still be present).
Exit code 1 = one or more gates FAIL.

All string comparisons are punctuation- and case-normalised on BOTH sides
(Starter Template §B: a comma once defeated an audit).
"""

import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path

# ----------------------------------------------------------------------------- helpers

def norm(s: str) -> str:
    """Normalise for comparison: NFC, lowercase, strip all punctuation, collapse ws."""
    s = unicodedata.normalize("NFC", str(s))
    s = s.lower()
    s = re.sub(r"[^\w\s\u0980-\u09FF]", " ", s)   # keep word chars + Bangla range
    s = re.sub(r"\s+", " ", s).strip()
    return s


def graded_sheets(m):
    """Sheets that belong to THIS block's graded surface.

    A sheet may carry "audit_scope": "pt_overlap_only" to be visible ONLY to
    gate_pt_zero_overlap() — used to bring another block-half's already-validated
    worksheets into the PT overlap comparison (PD-032) without re-running the
    de-patterning / marks / held-word gates over them.

    Additive: a sheet with no "audit_scope" key is graded, so a manifest that
    declares none behaves exactly as before.
    """
    return [s for s in m["sheets"] if s.get("audit_scope") != "pt_overlap_only"]


def all_items(sheet):
    for part in sheet.get("parts", []):
        for it in part.get("items", []):
            yield part.get("name", "?"), it


def sheet_answer_sets(sheet):
    """Yield (part_name, [answers]) for every part that has an answer sequence."""
    for part in sheet.get("parts", []):
        answers = part.get("answers")
        if answers is None:
            answers = [it.get("answer") for it in part.get("items", [])
                       if it.get("answer") is not None]
        if answers:
            yield part.get("name", "?"), [str(a) for a in answers]


# ----------------------------------------------------------------------------- gates

def gate_depattern(m):
    """Max run ≤2 and no strict alternation, per graded answer set."""
    fails, checked = [], 0
    for sheet in graded_sheets(m):
        for pname, answers in sheet_answer_sets(sheet):
            checked += 1
            a = [norm(x) for x in answers]
            # max run
            run, best = 1, 1
            for i in range(1, len(a)):
                run = run + 1 if a[i] == a[i - 1] else 1
                best = max(best, run)
            if best > 2:
                fails.append(f"{sheet['name']} Part {pname}: run of {best}")
            # strict alternation: whole set flips between exactly two values, len ≥ 4
            if len(a) >= 4 and len(set(a)) == 2:
                if all(a[i] != a[i - 1] for i in range(1, len(a))):
                    fails.append(f"{sheet['name']} Part {pname}: strict alternation")
    return ("De-patterning", not fails, f"{checked} answer sets checked", fails)


def gate_pair_overlap(m):
    """CW↔HW positional answer overlap ≤35%; identical item texts ≤2 per day."""
    fails, notes = [], []
    by_name = {s["name"]: s for s in graded_sheets(m)}
    for sheet in graded_sheets(m):
        pair = sheet.get("pair")
        if not pair or pair not in by_name:
            continue
        other = by_name[pair]
        # positional answer overlap, part-aligned by order
        sa = [x for _, xs in sheet_answer_sets(sheet) for x in xs]
        oa = [x for _, xs in sheet_answer_sets(other) for x in xs]
        n = min(len(sa), len(oa))
        if n:
            same = sum(1 for i in range(n) if norm(sa[i]) == norm(oa[i]))
            pct = 100.0 * same / n
            notes.append(f"{sheet['name']}↔{pair}: positional {pct:.0f}%")
            if pct > 35.0:
                fails.append(f"{sheet['name']}↔{pair}: positional overlap {pct:.0f}% (> 35%)")
        # identical item texts
        st = {norm(it.get("text", "")) for _, it in all_items(sheet) if it.get("text")}
        ot = [norm(it.get("text", "")) for _, it in all_items(other) if it.get("text")]
        ident = sum(1 for t in ot if t in st)
        if ident > 2:
            fails.append(f"{sheet['name']}↔{pair}: {ident} identical item texts (> 2)")
    return ("CW↔HW overlap", not fails, "; ".join(notes) or "no pairs declared", fails)


def gate_pt_zero_overlap(m):
    """Zero PT item texts identical (normalised) to any worksheet item."""
    fails = []
    pts = [s for s in m["sheets"] if s.get("type") == "pt"]
    wss = [s for s in m["sheets"] if s.get("type") != "pt"]
    ws_texts = {norm(it.get("text", "")): s["name"]
                for s in wss for _, it in all_items(s) if it.get("text")}
    for pt in pts:
        for pname, it in all_items(pt):
            t = norm(it.get("text", ""))
            if t and t in ws_texts:
                fails.append(f"{pt['name']} Part {pname}: item duplicates {ws_texts[t]}: "
                             f"\"{it.get('text','')[:60]}\"")
    return ("PT zero-overlap", not fails,
            f"{sum(1 for s in pts for _ in all_items(s))} PT items vs "
            f"{len(ws_texts)} worksheet items", fails)


def gate_within_sheet_dupes(m):
    fails = []
    for sheet in graded_sheets(m):
        texts = [norm(it.get("text", "")) for _, it in all_items(sheet) if it.get("text")]
        for t, c in Counter(texts).items():
            if c > 1:
                fails.append(f"{sheet['name']}: duplicate item ×{c}: \"{t[:60]}\"")
    return ("Within-sheet duplicates", not fails, "all sheets scanned", fails)


def gate_rehearsal_disjoint(m):
    st = {norm(w) for w in m.get("pt_self_try_words", [])}
    demo = {norm(w) for w in m.get("demo_box_words", [])}
    shared = sorted(st & demo)
    if not st and not demo:
        return ("Rehearsal/graded disjoint", True, "not applicable (no boxes declared)", [])
    return ("Rehearsal/graded disjoint", not shared,
            f"{len(st)} self-try vs {len(demo)} demo words",
            [f"shared word: {w}" for w in shared])


def gate_marks(m):
    fails, notes = [], []
    for sheet in graded_sheets(m):
        stated = sheet.get("stated_total")
        per = []
        for part in sheet.get("parts", []):
            pm = part.get("marks")
            if pm is not None:
                per.append(float(pm))
            else:
                per.extend(float(it.get("marks", 1)) for it in part.get("items", []))
        comp = sum(per)
        if stated is None:
            notes.append(f"{sheet['name']}: no stated total (computed {comp:g})")
            continue
        notes.append(f"{sheet['name']}: {comp:g}/{stated:g}")
        if abs(comp - float(stated)) > 1e-9:
            fails.append(f"{sheet['name']}: computed {comp:g} ≠ stated {stated:g}")
    return ("Mark totals", not fails, "; ".join(notes), fails)


SACRED = {"allah", "আল্লাহ", "quran", "qur an", "কুরআন", "কোরআন"}

def gate_sacred(m):
    fails = []
    for sheet in graded_sheets(m):
        for pname, it in all_items(sheet):
            for field in ("answer", "trigger"):
                v = it.get(field)
                if v and norm(v) in SACRED:
                    fails.append(f"{sheet['name']} Part {pname}: sacred word as graded "
                                 f"{field}: {v}")
    for w in m.get("dictation", []):
        if norm(w) in SACRED:
            fails.append(f"dictation: sacred word graded: {w}")
    return ("Sacred-word guard", not fails, "graded targets + dictation scanned", fails)


VALUES_LEXICON = {
    "music", "song", "sing", "dance", "guitar", "drum", "piano", "flute", "violin",
    "band", "concert", "christmas", "halloween", "easter", "diwali", "puja", "holi",
    "valentine", "গান", "নাচ", "পূজা", "বড়দিন",
}

def gate_values_lexicon(m):
    flags = []
    for sheet in graded_sheets(m):
        for pname, it in all_items(sheet):
            words = set(norm(it.get("text", "")).split())
            hit = words & VALUES_LEXICON
            if hit:
                flags.append(f"{sheet['name']} Part {pname}: {sorted(hit)} in "
                             f"\"{it.get('text','')[:60]}\"")
    # This gate FLAGS for human review; lexicon hits are treated as failures until ruled.
    return ("Values lexicon screen", not flags, "student-facing item texts scanned", flags)


def load_file2_words(path):
    """Heuristic loader: find a word column and (if present) a release-week column.

    Sheets with an EXACT 'word' header are preferred; fuzzy matches ("words this
    week") are used only if no sheet in the workbook has an exact word column.
    """
    from openpyxl import load_workbook
    wb = load_workbook(path, data_only=True)
    sheets = []
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue
        header = [str(h).strip().lower() if h else "" for h in rows[0]]
        exact = next((i for i, h in enumerate(header)
                      if h in ("word", "words", "english", "english word")), None)
        fuzzy = next((i for i, h in enumerate(header) if "word" in h), None)
        kcol = next((i for i, h in enumerate(header)
                     if any(k in h for k in ("week", "release", "batch"))), None)
        if exact is not None or fuzzy is not None:
            sheets.append((exact, fuzzy, kcol, rows))
    use_exact = any(e is not None for e, _, _, _ in sheets)
    words = {}
    for exact, fuzzy, kcol, rows in sheets:
        wcol = exact if use_exact else fuzzy
        if wcol is None:
            continue
        for r in rows[1:]:
            if r[wcol] is None:
                continue
            w = norm(r[wcol])
            wk = None
            if kcol is not None and r[kcol] is not None:
                mnum = re.search(r"\d+", str(r[kcol]))
                wk = int(mnum.group()) if mnum else None
            if w and (w not in words or (wk is not None and
                       (words[w] is None or wk < words[w]))):
                words[w] = wk
    return words


def gate_heldword(m, file2_path):
    if not file2_path:
        return ("Held-word / exemplar", False,
                "SKIPPED — no --file2 given (gate cannot pass without it)",
                ["provide --file2 <pool.xlsx>"])
    try:
        pool = load_file2_words(file2_path)
    except Exception as e:  # noqa: BLE001
        return ("Held-word / exemplar", False, f"File 2 load error: {e}", [str(e)])
    if not pool:
        return ("Held-word / exemplar", False,
                "File 2 loaded but no word column recognised — check README_manifest.md",
                ["unrecognised File 2 layout"])
    exemplars = {norm(w) for w in m.get("exemplars", [])}
    build_week = m.get("build_week")
    fails, checked = [], 0
    targets = []
    for sheet in graded_sheets(m):
        for pname, it in all_items(sheet):
            trig = it.get("trigger")
            if trig:
                targets.append((f"{sheet['name']} {pname}", trig))
    for w in m.get("dictation", []):
        targets.append(("dictation", w))
    for where, w in targets:
        checked += 1
        nw = norm(w)
        if nw in exemplars:
            continue
        if nw not in pool:
            fails.append(f"{where}: '{w}' not in File 2 pool and not a declared exemplar")
        elif build_week is not None and pool[nw] is not None and pool[nw] > build_week:
            fails.append(f"{where}: '{w}' released week {pool[nw]} > build week {build_week}")
    note = f"{checked} graded targets checked against {len(pool)} pool words"
    if not targets:
        note += " — WARNING: manifest declares no 'trigger' fields; gate is vacuous"
    return ("Held-word / exemplar", not fails, note, fails)


def gate_one_defensible(m):
    """Cannot be fully automated — surface candidates where one item text maps to
    multiple distinct answers across the block, for HUMAN review."""
    seen = {}
    flags = []
    for sheet in graded_sheets(m):
        for pname, it in all_items(sheet):
            t, a = norm(it.get("text", "")), norm(it.get("answer", "") or "")
            if not t or not a:
                continue
            if t in seen and seen[t][0] != a:
                flags.append(f"same item, different answers: \"{t[:50]}\" → "
                             f"{seen[t][0]} ({seen[t][1]}) vs {a} ({sheet['name']} {pname})")
            seen.setdefault(t, (a, f"{sheet['name']} {pname}"))
    # informational: never blocks on its own, but is printed for the human pass
    return ("One-defensible-answer (human)", True,
            f"{len(flags)} candidates for human review" if flags else
            "no conflicting-answer candidates; full check remains a human read", flags)


# ----------------------------------------------------------------------------- main

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    manifest_path = Path(sys.argv[1])
    file2 = None
    report_dir = Path(__file__).resolve().parent.parent / "reports"
    args = sys.argv[2:]
    for i, a in enumerate(args):
        if a == "--file2" and i + 1 < len(args):
            file2 = args[i + 1]
        if a == "--report-dir" and i + 1 < len(args):
            report_dir = Path(args[i + 1])

    m = json.loads(manifest_path.read_text(encoding="utf-8"))
    block = m.get("block_id", manifest_path.stem)

    gates = [
        gate_depattern(m),
        gate_pair_overlap(m),
        gate_pt_zero_overlap(m),
        gate_within_sheet_dupes(m),
        gate_rehearsal_disjoint(m),
        gate_marks(m),
        gate_sacred(m),
        gate_values_lexicon(m),
        gate_heldword(m, file2),
        gate_one_defensible(m),
    ]

    lines = [f"AUDIT REPORT — {block} — {date.today().isoformat()}",
             f"manifest: {manifest_path}", f"file2: {file2 or 'NOT PROVIDED'}", "-" * 72]
    ok = True
    for name, passed, note, detail in gates:
        status = "PASS" if passed else "FAIL"
        if not passed:
            ok = False
        lines.append(f"[{status}] {name:32s} {note}")
        for d in detail:
            lines.append(f"        - {d}")
    lines.append("-" * 72)
    lines.append("RESULT: ALL GATES PASS" if ok else "RESULT: FAILURES PRESENT — do not finalize")
    lines.append("Reminder: the naturalness gate and full one-defensible-answer check are HUMAN.")
    out = "\n".join(lines)
    print(out)

    report_dir.mkdir(parents=True, exist_ok=True)
    rp = report_dir / f"{block}_audit_{date.today().isoformat()}.txt"
    rp.write_text(out, encoding="utf-8")
    print(f"\nreport saved: {rp}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
