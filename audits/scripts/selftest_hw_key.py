#!/usr/bin/env python3
"""Self-test for the HW key transcribability gate (CR-006 / PD-037).

Run:  python3 audits/scripts/selftest_hw_key.py

Asserts:
  K.1  seeded error — HW Part B key identical to CW Part B key FAILS
       (the C4B06 F1 defect, reproduced with the actual HW-1 B key)
  K.2  the reordered key (the F1 fix) PASSES
  K.3  sequences shorter than 3 are ignored (no false fire on 2-item parts)
  K.4  unpaired sheets are ignored; a manifest with no pairs passes
  K.5  the pair is checked once, not twice (declared on the CW side only)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_all import gate_hw_key  # noqa: E402

CW_KEY = ["in", "on", "under", "near", "into", "at"]     # C4B06 CW-1 Part B
FIXED = ["at", "under", "in", "into", "on", "near"]      # the F1 reorder


def mk(hw_key, cw_key=None, pair=True):
    cw_key = cw_key or CW_KEY
    def sheet(name, key, pairname=None):
        s = {"name": name, "type": "worksheet", "stated_total": len(key),
             "parts": [{"name": "B", "items": [
                 {"text": f"item {name} {i}", "answer": a, "marks": 1}
                 for i, a in enumerate(key)]}]}
        if pairname:
            s["pair"] = pairname
        return s
    return {"block_id": "SELFTEST",
            "sheets": [sheet("CW1", cw_key, "HW1" if pair else None),
                       sheet("HW1", hw_key)]}


def check(label, cond, detail=""):
    print(f"[{'ok' if cond else 'XX'}] {label}")
    if detail:
        print(f"       {detail}")
    return cond


ok = True

_, passed, note, fails = gate_hw_key(mk(CW_KEY))
ok &= check("K.1 seeded error: HW key identical to CW key FAILS", not passed,
            fails[0] if fails else "")

_, passed, note, fails = gate_hw_key(mk(FIXED))
ok &= check("K.2 reordered key (F1 fix) PASSES", passed, note)

_, passed, _, _ = gate_hw_key(mk(["in", "on"], cw_key=["in", "on"]))
ok &= check("K.3 2-item identical sequences ignored (len < 3)", passed)

_, passed, _, _ = gate_hw_key(mk(CW_KEY, pair=False))
ok &= check("K.4 no declared pair → gate passes", passed)

_, _, note, fails = gate_hw_key(mk(CW_KEY))
ok &= check("K.5 pair checked once (one failure, not two)", len(fails) == 1, note)

print("=" * 72)
print("SELF-TEST RESULT:", "ALL ASSERTIONS HOLD" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)
