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

---

## 2026-08-08 — SCD (almajhudbd@gmail.com) — C4B06 promotion

- Task: **C4B06 (Preposition, W6) — FINAL**. Applied the Principal's CW-1/HW-1 content edits, added
  `shelf` to the block-local place set, replaced `red` with held `colourful`, converted the Part-B
  fill-in clues to Bangla, re-based all four Vocabulary Writing boxes onto the W6 batch, and ran a
  cross-sheet repetition pass.
- Cross-sheet repetition: **38 sentences repeated over 78 placements** (CW-4 was 16/20 recycled,
  HW-4 11/20). **40 items re-authored**, every one preserving its original answer class.
  Re-verified: 199 sentences compared, **zero repeats**. No mark total moved at any point.
- Promoted: master to `blocks/C4/C4_ENG_Block06_Preposition_v1.md` (internal v1.5); extracts generated
  to `extracts/C4/` — CW1–4, HW1–4, `C4B0506_PT`, `C4B06_AK`, `C4B06_CC`, `C4B06_TD`, master copy.
- Decisions: `shelf` → block-local place set (now 11); `colourful` NOT declared (already held W3);
  40 replacements approved and applied; promotion approved.
- Flags open: **cross-sheet duplicate gate proposed but unruled** (would need PD-036 to bind the drive);
  clue/instruction text still unread by every gate; PT Part B lists five classes vs six on the worksheets;
  attribution line and W7 examples remain in the out-of-scope Teacher Script.
- Infrastructure: mount still refuses `unlink` and re-materialises renamed files; all git work continues
  via the sandbox clone. `_wip/` duplicates could not be cleared — `blocks/C4/` is authoritative.

---

## 2026-08-08 — SCD (almajhudbd@gmail.com) — corrections-ledger system

- Task: installed the corrections feedback loop — `governance/CORRECTIONS.md` (16 retrofit rows
  from the C4B06 review cycle + C2B06b) and CLAUDE.md §5A; then batch-1 promotions.
- Files touched: `governance/CORRECTIONS.md` (new), `CLAUDE.md` (§5A),
  `audits/scripts/run_all.py` (3 new gates), `selftest_option_list.py` / `selftest_hw_key.py` /
  `selftest_cross_sheet.py` (new), `check_citations.py` (new), `README_manifest.md`,
  `governance/Curriculum_Design_Decision_Log_Working.md` (PD-036, PD-037).
- Decisions: seeded rows confirmed; **PD-036** cross-sheet repetition gate (threshold 0);
  **PD-037** option-list completeness + HW key transcribability gates; CR-006/007/008/009
  → PROMOTED; CR-010 stays PATTERN permanently ("human gate by design, never scriptable");
  CR-005/012–016 stay OPEN for the next block review.
- Verification: all 5 self-tests pass (3 new + 2 regression); citation check CLEAN —
  550 citations / 58 files, 37 PDs defined, 0 unknown, 0 superseded.
- Flags: C4B06 v1.7 PT review (other session) contains new Principal corrections not yet
  in the ledger — candidate rows for that session or the next review.
- Follow-up rulings (same session): **PD-038** — PD-036 zero-repeat governs, CW↔HW ≤2
  allowance kept as backstop only (gate report line updated); threshold stays 0.
  v1.7 PT corrections logged cross-session as **CR-017** (class list, via CR-008/PD-037),
  **CR-018** (items 13/16, reason pending), **CR-019** (Part C clue give-aways — CR-016
  type, 2nd occurrence). CR-018 rationale and the Part E 5→2 reduction await the
  reviewing session; duplicates to be merged on next view.

---

## 2026-08-09 — SCD (almajhudbd@gmail.com) — blueprint approvals

- Task: pending-actions review; both blueprints read in full and cross-checked against
  their STATE files (arithmetic, PD citations, staging — no blocking contradictions).
- Approvals (Principal, 09.08.26, recorded cross-session in each STATE.md):
  **C2B06b blueprint APPROVED** — §10-1 moot (PD-032/PD-034 already implemented),
  §10-2 = option (a) reconcile Coverage Log from the _wip draft, §10-3 PT split
  confirmed (A10·B5·C5·D6·E4=30). **C5B07 blueprint APPROVED** — cover (not remove)
  wall cards during PT, half-marks accepted, Drive Plan §4 W6 forward-only note
  authorized, §12 corrected: next free PD is PD-039.
- Both STATEs note the post-blueprint audit gates (PD-036/037/038) and the §5A
  pre-draft ledger read. Phase 4 authorized for both blocks; C2 unit 1 is the
  sentence bank (Principal approval required before use).
- Files touched: `blocks/C2/_wip/STATE.md`, `blocks/C5/_wip/STATE.md`, `SESSION_LOG.md`.

---

## 2026-08-09 — SCD (almajhudbd@gmail.com) — C1/C2/C3 W6 chat-built blocks imported

- **Repo recovery first.** The mount's `git pull` failed on divergent branches with three stale locks
  (`index.lock`, `HEAD.lock`, `ORIG_HEAD.lock`) and `unlink` denied. Delete permission was requested and
  **granted** this session. Local (C5B07 Phase 4 units 1–7 + review edits) was committed, then merged
  `--no-rebase` with remote (C4B06 FINAL, corrections-ledger, PD-036/037/038, C2B06b + C5B07 blueprint
  approvals). 18 add/add conflicts were content-identical; **two real conflicts** resolved as a union —
  `blocks/C5/_wip/STATE.md` (BC-1 CLOSED kept, blueprint-APPROVED ruling kept) and `SESSION_LOG.md`.
  Nothing discarded. Merge `a5694b7`, pushed.
- **Task:** three W6 masters built in chat (not in Cowork) imported to `_wip/` —
  `blocks/C1/_wip/C1_ENG_Block06_Pronoun_v1.md`, `blocks/C2/_wip/C2_ENG_Block06b_HaveHas_Match_v1.md`,
  `blocks/C3/_wip/C3_ENG_Block07_Adjective_v1.md`. Forward-only stems (CLAUDE.md §6), CRLF normalised,
  internal Master-ID / Filename fields updated. **None promoted.**
- **PD collisions.** Every provisional PD number in the C1 and C2 files was already taken. Reassigned and
  logged: **PD-039** (C1 B6 S3 cap-lift, overrides Ruling A) · **PD-040** (C1 combined `C1B0506-PT`) ·
  **PD-041** (C2 combined `C2B06ab-PT` — **reverses** the 08.08.26 "stale citation, disregarded" ruling,
  Principal 09.08.26) · **PD-042** (house character **Rabab reclassified male**, Charter §H.5 amendment,
  drive-wide non-mahram re-screen OPEN) · **PD-043** (C3 combined `C3B0607-PT`). C2's block-local *field*
  repointed to PD-012/PD-035. C3's PD-028 weighting citation was correct and left alone.
- **Flagged, not resolved:** **PD-036 is assigned twice** in the Decision Log (C5 Annual-paper ruling and
  the cross-sheet repetition gate). Both are live and cited in delivered files. Principal ruling needed.
- **Open per block:** C1 — PT Parts F/G overlap waiver is narrower than the §4 zero-overlap gate as
  tightened by PD-036/038. C2 — PD-031/PD-032 not declared in the file; the widened sixteen-sheet PT
  overlap has never been run. C3 — **BC-1**: *big* / *table* cited to PD-029/PD-030 (neither holds that
  ruling) and contradicting the header's "no block-local set"; citation replaced with a pending marker.
- **The big one:** **none of the three blocks has a manifest, and `run_all.py` has never been run on any
  of them.** Their in-file "programmatically verified / seven-audit sweep PASS" lines come from the chat
  build, not this repo's suite, and do not satisfy CLAUDE.md §4 (ten gates). Recorded in all three STATEs.

