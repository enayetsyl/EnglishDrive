# Session Log

Append-only. Newest entry last. Never overwrite past entries.

---

## 2026-08-08 — SCD (almajhudbd@gmail.com)

- Task: repo setup and housekeeping (no block build).
- Files touched: blocks/C1/C1_ENG_GrammarBlock05_Demonstrative_v1.md (copied from
  extracts/C1/TN per Principal instruction), audits/reports/setup_check.txt,
  CLAUDE.md (§1: file-deletion rule, session-log rule), .gitattributes (new),
  SESSION_LOG.md (new).
- Decisions/approvals: Principal approved sandbox file-delete permission; approved
  PAT-based push access; instructed the Block 5 copy and both CLAUDE.md rules.
- Flags raised: missing Block 5 master (fixed); stale .git lock files blocking
  commits (fixed via delete permission); sandbox lacked push credentials (fixed);
  CRLF noise in .gitignore (fixed via .gitattributes renormalize).
- Open: inconsistent master filenames in blocks/C1 ("_v1 (1).md" copies) — flagged,
  no action taken.

---

## 2026-08-08 — SCD (almajhudbd@gmail.com)

- Task: **C4B06 (Preposition, W6)** — recovered the existing master from `_wip/inbox/`,
  reconciled it against PD-029, ran the block's **first programmatic audit**, and applied
  the Principal's rulings F1–F12 + T1/T2. Teacher Script / Teaching Days 1–4 left untouched
  (already checked) apart from one PD-028→PD-012 citation fix.
- Files touched: `blocks/C4/_wip/C4_ENG_Block06_Preposition_v1_4.md` (new working master, v1.4),
  `blocks/C4/_wip/C4B06_manifest.json` (new), `blocks/C4/_wip/STATE.md`,
  `_wip/C4B06_review_dispositions.md`, `_wip/C4B06_F5_detail.md`, `_wip/C4B06_F7_draft_items.md`,
  `audits/scripts/run_all.py`, `audits/scripts/README_manifest.md`,
  `audits/scripts/selftest_block_local.py` (new), `audits/reports/C4B06_audit_2026-08-08.txt`,
  `governance/driveplans/C4_ENG_DrivePlan_v1_11.md` (new),
  `governance/Curriculum_Design_Decision_Log_Working.md`.
- Decisions/approvals: BC-1 "recover what exists"; BC-2 author Drive Plan v1.11; F1–F12 and
  T1/T2 all approved; F10 widened to all eight sheets; F7 = choose-between-two (18 items,
  HW-1 #28 distractor `into`→`in`); `(together)`→`(সঙ্গে)`; F5 time nouns declared block-local,
  block-scoped, **not** added to File 2. Later CW-1/HW-1 edits: A3 shelf, A7 recast, A8 man,
  HW-1 A14 red, Part B clues→Bangla, Vocabulary Writing→W6 batch.
- PD numbers assigned: **PD-034** (audit_scope extended to the §6.7 paired-week recovery),
  **PD-035** (PD-012 trigger extended to Drive-Plan-cap-required concepts). PD-033 was taken
  by the parallel C5 session.
- Flags raised: PT overlapped Block 5 (**PD-029 breach** — two verbatim duplicates; the master's
  v1 log had claimed this was verified); `quickly` W7 and `run` absent from File 2, both graded;
  every CW↔HW pair shared an identical secondary key; Part C match tasks were unmarkable.
  All resolved. **Outstanding: `shelf` (CW-1 A3) and `red` (HW-1 A14) are not in File 2** —
  awaiting ruling; audit is 9/10 until then.
- Infrastructure: the mount refused `unlink` all session and **re-materialised renamed files**
  (locks and `SESSION_LOG.md`), so the merge with the C5 session's work was done in a sandbox
  clone and pushed from there. Delete permission was requested once and declined.
  Leftover untracked duplicates in the mount: `SESSION_LOG.md.aside2`,
  `SESSION_LOG.md.local-untracked` — safe to delete, identical to `SESSION_LOG.md`.
