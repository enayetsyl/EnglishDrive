#!/usr/bin/env python3
"""PD citation check (CR-007).

Every "PD-###" string cited in any governance or block file (plus CLAUDE.md and
SESSION_LOG.md) must exist as a "### PD-###" heading in the Decision Log.
Unknown numbers and citations of superseded entries are flagged.

A Decision Log entry is superseded when its own heading is struck through
(~~...~~) or its **Status:** line contains "superseded".

Usage:  python3 audits/scripts/check_citations.py [repo_root]
Exit 0 = clean · 1 = findings present.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else \
    Path(__file__).resolve().parents[2]
LOG = ROOT / "governance" / "Curriculum_Design_Decision_Log_Working.md"

CITE = re.compile(r"PD-(\d{1,3})")
HEADING = re.compile(r"^#{1,6}\s*(~~)?\s*PD-(\d{1,3})\b")
STATUS_SUPERSEDED = re.compile(r"\*\*status:?\*\*.*supersed", re.IGNORECASE)


def parse_log(log_path):
    """Return (defined, superseded) sets of PD numbers (ints)."""
    defined, superseded = set(), set()
    current = None
    for line in log_path.read_text(encoding="utf-8").splitlines():
        h = HEADING.match(line.strip())
        if h:
            current = int(h.group(2))
            defined.add(current)
            if h.group(1):  # struck-through heading
                superseded.add(current)
            continue
        if current is not None and STATUS_SUPERSEDED.search(line):
            superseded.add(current)
    return defined, superseded


def scan_targets():
    files = [ROOT / "CLAUDE.md", ROOT / "SESSION_LOG.md"]
    for base in ("governance", "blocks"):
        files.extend(sorted((ROOT / base).rglob("*.md")))
    return [f for f in files if f.is_file()]


def main():
    if not LOG.is_file():
        print(f"FATAL: Decision Log not found at {LOG}")
        sys.exit(2)
    defined, superseded = parse_log(LOG)
    unknown_hits, superseded_hits = [], []
    files = scan_targets()
    cited = 0
    for f in files:
        rel = f.relative_to(ROOT)
        for ln, line in enumerate(f.read_text(encoding="utf-8",
                                              errors="replace").splitlines(), 1):
            # Decision Log headings are definitions, not citations.
            if f == LOG and HEADING.match(line.strip()):
                continue
            for mnum in CITE.finditer(line):
                cited += 1
                n = int(mnum.group(1))
                where = f"{rel}:{ln}  PD-{n:03d}  | {line.strip()[:70]}"
                if n not in defined:
                    unknown_hits.append(where)
                elif n in superseded:
                    superseded_hits.append(where)

    print(f"CITATION CHECK — {len(files)} files scanned, {cited} PD citations, "
          f"{len(defined)} PDs defined (PD-{min(defined):03d}…PD-{max(defined):03d}), "
          f"{len(superseded)} superseded")
    print("-" * 72)
    if unknown_hits:
        print(f"UNKNOWN PD NUMBERS ({len(unknown_hits)}):")
        for h in unknown_hits:
            print(f"  {h}")
    if superseded_hits:
        print(f"CITATIONS OF SUPERSEDED PDs ({len(superseded_hits)}):")
        for h in superseded_hits:
            print(f"  {h}")
    if not unknown_hits and not superseded_hits:
        print("CLEAN — every citation resolves to a live Decision Log entry.")
    sys.exit(1 if (unknown_hits or superseded_hits) else 0)


if __name__ == "__main__":
    main()
