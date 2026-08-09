#!/usr/bin/env python3
"""Self-test for the cross-sheet repetition gate (CR-009 / PD-036).

Run:  python3 audits/scripts/selftest_cross_sheet.py

Asserts:
  X.1  seeded error — the same sentence on two sheets FAILS at threshold 0
  X.2  all-distinct sentences PASS
  X.3  matching is punctuation/case-normalised ("The boys run fast." ≡ "the boys run fast")
  X.4  within-sheet duplicates are NOT this gate's business (covered elsewhere)
  X.5  pt_overlap_only reference sheets are excluded (audit_scope respected)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_all import gate_cross_sheet_repetition, CROSS_SHEET_MAX_REPEATS  # noqa: E402

assert CROSS_SHEET_MAX_REPEATS == 0, "self-test written for the PD-036 threshold of 0"


def sheet(name, texts, scope=None):
    s = {"name": name, "type": "worksheet", "stated_total": len(texts),
         "parts": [{"name": "A", "items": [
             {"text": t, "answer": "x", "marks": 1} for t in texts]}]}
    if scope:
        s["audit_scope"] = scope
    return s


def mk(*sheets):
    return {"block_id": "SELFTEST", "sheets": list(sheets)}


def check(label, cond, detail=""):
    print(f"[{'ok' if cond else 'XX'}] {label}")
    if detail:
        print(f"       {detail}")
    return cond


ok = True

_, passed, note, fails = gate_cross_sheet_repetition(
    mk(sheet("CW4", ["The boys run fast.", "A kind man helps."]),
       sheet("HW4", ["The boys run fast.", "The girl reads loudly."])))
ok &= check("X.1 seeded error: same sentence on two sheets FAILS", not passed,
            fails[0] if fails else "")

_, passed, note, _ = gate_cross_sheet_repetition(
    mk(sheet("CW4", ["The boys walk home.", "A kind man helps."]),
       sheet("HW4", ["The boys run fast.", "The girl reads loudly."])))
ok &= check("X.2 all-distinct sentences PASS", passed, note)

_, passed, _, fails = gate_cross_sheet_repetition(
    mk(sheet("CW4", ["The boys run fast."]),
       sheet("HW4", ["the boys run fast"])))
ok &= check("X.3 normalised matching across sheets", not passed,
            fails[0] if fails else "")

_, passed, _, _ = gate_cross_sheet_repetition(
    mk(sheet("CW4", ["Twice on one sheet.", "Twice on one sheet."])))
ok &= check("X.4 within-sheet duplicate alone does not fire this gate", passed)

_, passed, _, _ = gate_cross_sheet_repetition(
    mk(sheet("CW4", ["The boys run fast."]),
       sheet("B5-CW1", ["The boys run fast."], scope="pt_overlap_only")))
ok &= check("X.5 pt_overlap_only reference sheets excluded", passed)

print("=" * 72)
print("SELF-TEST RESULT:", "ALL ASSERTIONS HOLD" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)
