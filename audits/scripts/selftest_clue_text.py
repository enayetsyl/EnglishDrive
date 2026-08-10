#!/usr/bin/env python3
"""Self-test for PD-054 — student-facing text visibility.

Seeded-error tests proving that clue glosses, part instruction lines and sheet
boxes are now visible to the values-lexicon, sacred-word and held-word screens,
and that the deliberately NARROWER clue rule behaves as ruled:

    clue glosses      English content words must be held / exemplar / block-local
    instructions      exempt from held-word (teacher register, not vocabulary)
    boxes             exempt from held-word; values + sacred screened
    Bangla glosses    exempt from held-word by nature (CR-011); still screened

The headline case is `(together)`: a W7 word that printed on a W6 sheet, carried
the answer on five graded items, and left every gate green because the held-word
gate reads `trigger` alone.

Run: python3 audits/scripts/selftest_clue_text.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_all import (  # noqa: E402
    gate_heldword, gate_sacred, gate_values_lexicon, student_facing_surfaces,
)

FAILURES = []


def check(label, condition, detail=""):
    if condition:
        print(f"[ok] {label}")
        if detail:
            print(f"       {detail}")
    else:
        print(f"[FAIL] {label}")
        if detail:
            print(f"       {detail}")
        FAILURES.append(label)


# A tiny stand-in pool. build_week 6: 'friend' is held by W6, 'together' is W7.
POOL = {"friend": 5, "father": 4, "school": 3, "together": 7, "sing": 2}


class FakeFile2:
    """gate_heldword() takes a path and calls load_file2_words(); patch that out."""


def heldword_with_pool(m, pool=POOL):
    import run_all
    original = run_all.load_file2_words
    run_all.load_file2_words = lambda _path: dict(pool)
    try:
        return run_all.gate_heldword(m, "fake.xlsx")
    finally:
        run_all.load_file2_words = original


def manifest(sheets, **kw):
    base = {"block_id": "SELFTEST", "build_week": 6, "sheets": sheets}
    base.update(kw)
    return base


def sheet(name="CW1", parts=None, boxes=None, **kw):
    s = {"name": name, "type": "CW", "parts": parts or [], "stated_total": 0}
    if boxes is not None:
        s["boxes"] = boxes
    s.update(kw)
    return s


def part(name="A", items=None, instructions=None):
    p = {"name": name, "items": items or []}
    if instructions is not None:
        p["instructions"] = instructions
    return p


# --------------------------------------------------------------------------- Y.1
m = manifest([sheet(parts=[part(items=[
    {"text": "I go to school ___ my friend.", "answer": "with",
     "trigger": "friend", "clue": "(together)"}])])])
name, passed, note, detail = heldword_with_pool(m)
check("Y.1 seeded error: out-of-pool-week English clue word FAILS",
      not passed and any("together" in d for d in detail),
      detail[0] if detail else "no detail")

# --------------------------------------------------------------------------- Y.2
m = manifest([sheet(parts=[part(items=[
    {"text": "I go to school ___ my friend.", "answer": "with",
     "trigger": "friend", "clue": "(friend)"}])])])
name, passed, note, detail = heldword_with_pool(m)
check("Y.2 held English clue word PASSES", passed, note)

# --------------------------------------------------------------------------- Y.3
m = manifest([sheet(parts=[part(items=[
    {"text": "I go to school ___ my friend.", "answer": "with",
     "trigger": "friend", "clue": "(সঙ্গে)"}])])])
name, passed, note, detail = heldword_with_pool(m)
check("Y.3 Bangla clue gloss exempt from held-word (CR-011)", passed, note)

# --------------------------------------------------------------------------- Y.4
m = manifest([sheet(parts=[part(
    instructions="Fill in the blanks with the correct preposition.",
    items=[{"text": "I walk ___ my father.", "answer": "with",
            "trigger": "father"}])])])
name, passed, note, detail = heldword_with_pool(m)
check("Y.4 instruction line exempt from held-word (teacher register)",
      passed, note)

# --------------------------------------------------------------------------- Y.5
m = manifest([sheet(parts=[part(items=[
    {"text": "I walk ___ my father.", "answer": "with", "trigger": "father",
     "clue": "(to the school)"}])])])
name, passed, note, detail = heldword_with_pool(m)
check("Y.5 function words in a clue are never held-word targets "
      "(only 'school' is checked here, not 'to'/'the')",
      passed and "1 English clue word" in note, note)

# --------------------------------------------------------------------------- Y.6
m = manifest([sheet(parts=[part(
    instructions="Sing the song, then fill in the blanks.",
    items=[{"text": "I walk ___ my father.", "answer": "with"}])])])
name, passed, note, detail = gate_values_lexicon(m)
check("Y.6 values lexicon now reads instruction lines",
      not passed and any("sing" in d for d in detail),
      detail[0] if detail else "no detail")

# --------------------------------------------------------------------------- Y.7
m = manifest([sheet(boxes=[{"name": "Word Bank", "words": ["drum", "desk"]}],
                    parts=[part(items=[
                        {"text": "The bag is ___ the desk.", "answer": "on"}])])])
name, passed, note, detail = gate_values_lexicon(m)
check("Y.7 values lexicon now reads sheet boxes",
      not passed and any("drum" in d for d in detail),
      detail[0] if detail else "no detail")

# --------------------------------------------------------------------------- Y.8
m = manifest([sheet(boxes=[{"name": "Word Bank", "words": ["Allah", "desk"]}],
                    parts=[part(items=[
                        {"text": "The bag is ___ the desk.", "answer": "on"}])])])
name, passed, note, detail = gate_sacred(m)
check("Y.8 sacred word in a word bank FAILS (selectable = graded target)",
      not passed and any("allah" in d.lower() for d in detail),
      detail[0] if detail else "no detail")

# --------------------------------------------------------------------------- Y.9
m = manifest([sheet(parts=[part(
    instructions="Remember that Allah made everything. Now fill in the blanks.",
    items=[{"text": "The bag is ___ the desk.", "answer": "on"}])])])
name, passed, note, detail = gate_sacred(m)
check("Y.9 sacred word in an instruction line FLAGS but does not fail "
      "(Charter §H.3 permits teacher prose)",
      passed and any("allah" in d.lower() for d in detail),
      note)

# -------------------------------------------------------------------------- Y.10
m = manifest([sheet(name="REF", audit_scope="pt_overlap_only",
                    parts=[part(items=[
                        {"text": "x", "clue": "(together)"}])])])
name, passed, note, detail = heldword_with_pool(m)
check("Y.10 pt_overlap_only reference sheets excluded, as everywhere",
      passed, note)

# -------------------------------------------------------------------------- Y.11
m = manifest([sheet(parts=[part(items=[
    {"text": "I go to school ___ my friend.", "answer": "with",
     "trigger": "friend"}])])])
name, passed, note, detail = heldword_with_pool(m)
surfaces = list(student_facing_surfaces(m["sheets"][0]))
check("Y.11 manifest declaring none of the three fields behaves exactly as before",
      passed and surfaces == [], f"{len(surfaces)} surfaces found")

# -------------------------------------------------------------------------- Y.12
m = manifest([sheet(parts=[part(items=[
    {"text": "I go to school ___ my friend.", "answer": "with",
     "trigger": "friend", "clue": "(together)"}])])],
    block_local=["together"])
name, passed, note, detail = heldword_with_pool(m)
check("Y.12 an explicitly block-local clue word PASSES (PD-012/PD-035 route)",
      passed, note)

print("=" * 72)
if FAILURES:
    print(f"SELF-TEST RESULT: {len(FAILURES)} ASSERTION(S) FAILED")
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
print("SELF-TEST RESULT: ALL ASSERTIONS HOLD")
