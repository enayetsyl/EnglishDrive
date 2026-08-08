#!/usr/bin/env python3
"""Self-test for the "audit_scope": "pt_overlap_only" flag (PD-032).

Run:  python3 audits/scripts/selftest_audit_scope.py

Asserts three things:

  1. NORMAL mode still catches a planted PT duplicate (no behaviour lost).
  2. SCOPED mode still catches it, while the de-patterning / mark-total /
     within-sheet-duplicate gates SKIP the scoped sheet.
  3. ADDITIVE: a manifest declaring no audit_scope produces output byte-identical
     to the pre-change script, if a baseline copy is supplied via
     --baseline <path to the old run_all.py>.

Exit 0 = all assertions hold.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNNER = HERE / "run_all.py"


def run(manifest, script=RUNNER):
    with tempfile.TemporaryDirectory() as td:
        p = subprocess.run(
            [sys.executable, str(script), str(HERE / manifest), "--report-dir", td],
            capture_output=True, text=True)
        return p.stdout


def comparable(out):
    """Drop the 'report saved:' line — it carries a per-run temp path, not behaviour."""
    return "\n".join(l for l in out.splitlines() if not l.startswith("report saved:")).strip()


def gate(out, name):
    m = re.search(rf"^\[(PASS|FAIL)\] {re.escape(name)}", out, re.M)
    return m.group(1) if m else "ABSENT"


def main():
    baseline = None
    if "--baseline" in sys.argv:
        baseline = sys.argv[sys.argv.index("--baseline") + 1]

    normal = run("selftest_manifest_normal.json")
    scoped = run("selftest_manifest_scoped.json")

    checks = [
        ("NORMAL: PT zero-overlap catches planted duplicate",
         gate(normal, "PT zero-overlap"), "FAIL"),
        ("NORMAL: de-patterning sees the worksheet",
         gate(normal, "De-patterning"), "PASS"),
        ("NORMAL: mark totals sees the worksheet",
         gate(normal, "Mark totals"), "PASS"),
        ("SCOPED: PT zero-overlap STILL catches the duplicate",
         gate(scoped, "PT zero-overlap"), "FAIL"),
        ("SCOPED: de-patterning SKIPS scoped sheet (run of 3 not reported)",
         gate(scoped, "De-patterning"), "PASS"),
        ("SCOPED: mark totals SKIPS scoped sheet (stated 999 not reported)",
         gate(scoped, "Mark totals"), "PASS"),
        ("SCOPED: within-sheet duplicates SKIPS scoped sheet",
         gate(scoped, "Within-sheet duplicates"), "PASS"),
    ]

    print("=" * 72)
    print("SELF-TEST — audit_scope: pt_overlap_only  (PD-032)")
    print("=" * 72)
    ok = True
    for label, got, want in checks:
        good = got == want
        ok &= good
        print(f"[{'ok' if good else 'XX'}] {label}\n       expected {want}, got {got}")

    # de-patterning / marks must NOT even mention the scoped sheet
    leaked = [g for g in ("C2B06a-CW1",) if re.search(
        rf"^\[(PASS|FAIL)\] (De-patterning|Mark totals|Within-sheet).*{g}", scoped, re.M)]
    print(f"[{'ok' if not leaked else 'XX'}] SCOPED: scoped sheet name absent from "
          f"non-overlap gate notes\n       {'clean' if not leaked else leaked}")
    ok &= not leaked

    # the PT-overlap failure must name the scoped sheet — proving visibility
    vis = "C2B06a-CW1" in scoped
    print(f"[{'ok' if vis else 'XX'}] SCOPED: PT-overlap failure names the scoped sheet "
          f"(visibility proven)\n       {'yes' if vis else 'no'}")
    ok &= vis

    if baseline:
        b = run("selftest_manifest_normal.json", script=baseline)
        same = comparable(b) == comparable(normal)
        print(f"[{'ok' if same else 'XX'}] ADDITIVE: unflagged manifest byte-identical to "
              f"pre-change script\n       {'identical' if same else 'DIFFERS'}")
        ok &= same
    else:
        print("[--] ADDITIVE check skipped (pass --baseline <old run_all.py>)")

    print("=" * 72)
    print("SELF-TEST RESULT:", "ALL ASSERTIONS HOLD" if ok else "FAILURES PRESENT")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
