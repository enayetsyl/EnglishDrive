#!/usr/bin/env python3
"""Self-test for the option-list completeness gate (CR-008 / PD-037).

Run:  python3 audits/scripts/selftest_option_list.py

Asserts:
  O.1  seeded error — a part keyed 'Adverb' whose printed options omit it FAILS
       (the C4B06 F10 defect, reproduced)
  O.2  the same part with 'Adverb' in the options PASSES
  O.3  matching is punctuation/case-normalised ('adverb.' ≡ 'Adverb')
  O.4  additive — a manifest with no 'options' fields reports vacuous, not FAIL
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_all import gate_option_list  # noqa: E402

FIVE = ["Noun", "Verb", "Adjective", "Pronoun", "Preposition"]
SIX = FIVE + ["Adverb"]


def mk(options, answer="Adverb"):
    part = {"name": "A", "items": [
        {"text": "The doctor writes slowly.", "answer": answer, "marks": 1}]}
    if options is not None:
        part["options"] = options
    return {"block_id": "SELFTEST", "sheets": [
        {"name": "CW1", "type": "worksheet", "stated_total": 1, "parts": [part]}]}


def check(label, cond, detail=""):
    print(f"[{'ok' if cond else 'XX'}] {label}")
    if detail:
        print(f"       {detail}")
    return cond


ok = True

_, passed, note, fails = gate_option_list(mk(FIVE))
ok &= check("O.1 seeded error: keyed Adverb missing from options FAILS", not passed,
            fails[0] if fails else "")

_, passed, note, fails = gate_option_list(mk(SIX))
ok &= check("O.2 keyed Adverb present in options PASSES", passed, note)

_, passed, _, _ = gate_option_list(mk(["noun", "ADVERB."], answer="Adverb"))
ok &= check("O.3 normalised matching ('ADVERB.' ≡ 'Adverb')", passed)

_, passed, note, _ = gate_option_list(mk(None))
ok &= check("O.4 additive: no 'options' fields → vacuous pass", passed and "vacuous" in note,
            note)

print("=" * 72)
print("SELF-TEST RESULT:", "ALL ASSERTIONS HOLD" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)
