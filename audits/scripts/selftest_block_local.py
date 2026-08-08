#!/usr/bin/env python3
"""Self-test for the PD-012 `block_local` manifest field (T1) and the T2 values
lexicon inflection matching.

Run:  python3 audits/scripts/selftest_block_local.py

Asserts:
  T1.1  a block-local word used as a graded trigger PASSES the held-word gate
  T1.2  an undeclared non-held word still FAILS (the field does not blanket-pass)
  T1.3  a block-local word in the dictation list FAILS (PD-012 bars it)
  T1.4  a word declared as BOTH exemplar and block_local FAILS
  T1.5  additive: a manifest with no `block_local` key behaves exactly as before
  T2.1  inflected values-lexicon forms are caught (sang / sings / singing / songs)
  T2.2  prefix matching does not over-fire (bandage is not `band`)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_all import gate_heldword, gate_values_lexicon, _values_hits  # noqa: E402

POOL = str(Path(__file__).parents[2] / "file2" / "C4_ENG_VocabBatchOrder_v2.xlsx")


def mk(trigger, *, block_local=None, exemplars=None, dictation=None):
    m = {"block_id": "SELFTEST", "build_week": 6,
         "sheets": [{"name": "CW1", "type": "worksheet", "stated_total": 1,
                     "parts": [{"name": "A", "items": [
                         {"text": "x", "answer": "Noun", "trigger": trigger, "marks": 1}]}]}],
         "dictation": dictation or []}
    if block_local is not None:
        m["block_local"] = block_local
    if exemplars is not None:
        m["exemplars"] = exemplars
    return m


def check(label, cond, detail=""):
    print(f"[{'ok' if cond else 'XX'}] {label}")
    if detail:
        print(f"       {detail}")
    return cond


ok = True

# --- T1 -----------------------------------------------------------------------
name, passed, note, fails = gate_heldword(mk("gate", block_local=["gate", "box"]), POOL)
ok &= check("T1.1 block-local trigger passes", passed, note)

name, passed, note, fails = gate_heldword(mk("bench", block_local=["gate", "box"]), POOL)
ok &= check("T1.2 undeclared non-held word still fails", not passed,
            fails[0] if fails else "")

name, passed, note, fails = gate_heldword(
    mk("gate", block_local=["gate"], dictation=["gate"]), POOL)
ok &= check("T1.3 block-local word in dictation fails (PD-012)", not passed,
            next((f for f in fails if "dictation" in f), ""))

name, passed, note, fails = gate_heldword(
    mk("gate", block_local=["gate"], exemplars=["gate"]), POOL)
ok &= check("T1.4 word declared exemplar AND block-local fails", not passed,
            next((f for f in fails if "BOTH" in f), ""))

# additive: no block_local key at all -> a held word must still pass, and an
# unheld one must still fail, exactly as before the field existed.
_, p_held, _, _ = gate_heldword(mk("teacher"), POOL)
_, p_unheld, _, _ = gate_heldword(mk("bench"), POOL)
ok &= check("T1.5 additive — no block_local key behaves as before",
            p_held and not p_unheld,
            f"held passes={p_held}, unheld passes={p_unheld}")

# --- T2 -----------------------------------------------------------------------
caught = all(_values_hits(t) for t in
             ["A small bird sang.", "The girl sings loudly.",
              "The child was singing.", "They played songs."])
ok &= check("T2.1 inflected forms caught (sang/sings/singing/songs)", caught)

ok &= check("T2.2 no over-match on 'bandage'", not _values_hits("He had a bandage."))

print("=" * 72)
print("SELF-TEST RESULT:", "ALL ASSERTIONS HOLD" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)
