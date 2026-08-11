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

---

## 2026-08-09 — SCD (almajhudbd@gmail.com) — C1/C2/C3 W6 blocks: import → audit → repair → promotion

- **Task.** Three W6 masters built in chat (C1 Block 6 Pronoun, C2 Block 6b Have/Has+Match, C3 Block 7 Adjective)
  imported to `_wip/`, audited for the first time, repaired to the Principal's minimum-change standard, and promoted.
- **Promoted:** `blocks/C1/C1_ENG_Block06_Pronoun_v1.md` · `blocks/C2/C2_ENG_Block06b_HaveHas_Match_v1.md` ·
  `blocks/C3/C3_ENG_Block07_Adjective_v1.md`. `_wip/` retains each manifest + STATE as the audit trail.
- **Working method, set by the Principal early and applied throughout:** report each gate failure's **assessment
  impact** first; fix only what has one; rule the rest. Content changes were minimised because the files were already
  delivered. Net: **C1 nil content changes**, **C2 48**, **C3 15**.
- **First audit runs.** None of the three had ever been through `run_all.py`; their in-file "audited" claims came from
  the chat build. Manifests were built (C1 88 items, C2 269, C3 295) and the suite run repeatedly.
- **Substantive defects found and fixed.** C2: 15 answer sets in strict has/have alternation (**108 of 275 marks
  winnable by alternating**), a key error marking a correct answer wrong, 32 match-pair repeats, a §H.9 attribution
  breach (*"the sun gives us light"*). C3: PT computing 34.5 against a stated 34, 9 over-repeated match pairs, a
  strict-alternation PT part fixed by **reordering with no sentence rewritten**, two conflicting answer keys, an
  off-roster name, and a **within-paper answer leak** (Part B #7 handed the pupil Part C #4).
- **Blind spots the gates could not see.** C3's 40 match placements and the PT's entire 16-item Article half were
  invisible to every gate — both found by hand extraction, both now itemised/declared. C1's 29 house-name items remain
  outside the held-word gate. Three occurrences → **CR-032 flagged PATTERN**; **no rule created** (Principal's call).
- **PDs logged: PD-039 … PD-050** (12). Included **PD-041** reversing an earlier ruling, **PD-042** reclassifying a
  house character, **PD-047** closing BC-1, and **PD-050** in which the agent's own argument was **withdrawn as
  overstated** after the Principal challenged it. **Corrections CR-020 … CR-032** (13) logged to the ledger — overdue,
  since §5A requires them in-session.
- **Also delivered:** 24 canonical extracts generated from the promoted C2 and C3 masters; C3's `extracts/TN/` copy
  regenerated (91 stale pre-repair lines gone, now byte-identical); dependency pointers on the C2 6a and C1 B5 masters;
  forward-only Drive Plan notes for C1 (§2/§7/§9b), C2 (§4/§7) and C3 (§4/§7).
- **Two agent errors caught and corrected in-session:** a replacement item proposed for C3 PT Part C #4 would have
  recreated the very leak it was fixing (withdrawn before writing); and two Block 6 overlap sources were misattributed
  to one sheet. Both recorded in STATE rather than quietly fixed.
- **Outstanding, tracked separately:** C1's 12 canonical extracts · the CR-028/CR-032 PATTERN governance decision ·
  PD-042 §H.5 drive-wide re-screen · C3 File 2 size-adjective gap · C2 W6 assignment (blocked on the stale Coverage
  Log) · `Rani` ×6 in the promoted C3 Block 6 master (observation only, not reopened).


## 10.08.26 — SCD · C4 session: PD-054 ruled + PD-036/PD-055 collision resolved

- **Task:** open the next C4 block (B7 Verb & SVA, W7). Two governance items cleared first.
- **PD-036 was NOT pending.** `blocks/C4/_wip/STATE.md` open item #1 said "PD-036 is the next free
  number"; it was written mid-sweep on 08.08.26 and stale the same day. PD-036 was already ruled and
  live (gate + constant + self-test + CR-009 + PD-038). No new number assigned; STATE item #1 closed.
- **PD-054 — student-facing text visibility (Principal, 10.08.26).** Optional `clue` / `instructions` /
  `boxes` manifest fields routed into the **existing** values-lexicon, sacred-word and held-word screens.
  No new gate. Held-word binds on `clue` only (English content words must be held/exemplar/block-local);
  instructions and boxes exempt. Sacred split on Charter §H.3: clue/boxes FAIL, instructions FLAG.
  **CR-011 promoted PATTERN → PROMOTED** — Bangla glosses binding. Closes the `(together)` failure mode.
- **Evidence the defect was real:** C4B06 re-run reports **0 English clue words checked** — it declares no
  `clue` field at all; its `(সঙ্গে)` glosses were visible only because the extractor left the parenthetical
  inside `text`. Coverage was accidental, not designed.
- **Validation:** `selftest_clue_text.py` 12/12 · all five pre-existing self-tests pass · **C4B06 regression
  ALL GATES PASS, per-gate results identical to 08.08.26** (`audits/reports/C4B06_audit_2026-08-10.txt`).
- **Numbering incident.** The entry was drafted as PD-051 against a log topping out at PD-050; the parallel
  **C3B08** session committed `cc7446c` mid-session taking **PD-051/052/053**. Renumbered to **PD-054** across
  Decision Log, `run_all.py`, `selftest_clue_text.py`, `README_manifest.md`, `CORRECTIONS.md`, `STATE.md`.
- **Concurrency defect, recorded not rewritten.** The PD-054 Decision Log edit was uncommitted on disk when the
  C3B08 session ran `git add -A`; it was absorbed into **that** session's commit while `git status` showed the
  log clean. Left in the audit trail at the Principal's instruction. Stale `.git/index.lock` blocked the commit
  until folder delete permission was granted.
- **PD-036 double-assignment resolved (Principal, 10.08.26).** Two unrelated rulings held PD-036 since 08.08.26.
  **PD-036 stays with the cross-sheet repetition gate** (live dependencies: `run_all.py`,
  `CROSS_SHEET_MAX_REPEATS`, `selftest_cross_sheet.py`, CR-009, PD-038). The **C5 Annual-2025 binding-set ruling
  is reissued as PD-055**, forward-only, substance untouched, with an explicit provenance banner. Decision Log
  headings now unique.
- **Legacy PD-036 citations deliberately NOT edited:** `C5_ENG_DrivePlan_v1_7.md` (§K.3 — correct at v1_8) ·
  `blocks/C5/_wip/C5_ENG_Block07_AdjectivePronoun_v1.md` + `blocks/C5/_wip/STATE.md` (**open in a parallel
  session**) · `SESSION_LOG.md` (historical). Listed in the PD-055 banner so they cannot be lost.
- **Standing process change:** derive the next PD number from **current HEAD immediately before each append**;
  avoid `git add -A` when a parallel session has governance changes in its working tree.
- **Carried forward:** Bangla `VALUES_LEXICON` widening (4/22 entries Bangla, English-only inflection matching)
  — stated follow-on, **not** part of PD-054 · File 2 label re-map · C4B07 = Verb & SVA, W7, first of the three
  protected tense weeks.
- **Next:** C4B07 Phase 1 orientation, read-only. No master write.

---

## 10.08.26 — C3 Block 8 (Pronoun): Phases 1–3 + Day 1 built
**User:** SCD · **Task:** "start C3 next block" → C3B08 Pronoun, W7.

- **Phase 1.** All three binding C3 papers read from source: **Annual 2025 Q3 is the sole pronoun anchor**
  (connected-passage cloze, no word box, 5×1); HY2025 and HY2026 confirmed not to test pronoun. Held scope at W7 =
  the whole 195-word pool. Flags raised: File 2 batch sizes disagree with batch content (W6 40 not 35, W7 34 not 39,
  pool 195 not 194); the block's graded surface is 100% function words (the CR-032 PATTERN at full scale); the
  twelve pronouns are absent from File 2; Charter §H.5 and CLAUDE.md §5 disagreed on the name roster; textbook/TG/
  C3 BlockBuildSpec absent from the repo.
- **Phase 2.** Eight questions, all ruled by the Principal in session. **PD-051** pronouns block-local ·
  **PD-052** *you* taught **and graded**, widening §2 row 8 (cross-class replication to C1/C2/C4/C5 flagged, NOT
  executed — C1 Block 6 already promoted) · **PD-053** Charter §H.5 roster gains Maryam and Fatima, which makes
  CR-029's C3B07 fix retroactively correct without reopening the block. Charter reissued **v1.5→v1.6**, C3 Drive
  Plan **v1.8→v1.9**, both forward-only per §K.3; neither original edited in place. Also repaired: the Drive Plan
  version-log separator sat below the v1.8 row, so the log did not render as a table. Roll 17 confirmed; B7
  delivered/locked; *this/that* kept off all student sheets; CR-032 handled by hand this block.
- **Phase 3.** Blueprint written to `_wip/C3B08_blueprint.md`, **approved** with all six §D decisions as
  recommended (PT at 30 marks, terms taught-not-graded on the PD-014 precedent, volume held).
- **Phase 4, Day 1.** Master v1.1 built: header, Clue Card, checklist, Sunday script, 17-prompt Exit Check,
  `C3B08-CW1` (28) and `C3B08-HW1` (26). First audit run returned one genuine **FAIL** — cross-sheet repetition,
  `Yusuf` on both Part Bs; the pre-audit estimate had wrongly scored it against a ≤2 threshold when the operative
  gate is **zero**. Fixed to `Abdullah`, no key moved. **PD-054 landed mid-build** from the parallel C4 session;
  `boxes` and `instructions` declared on both sheets in response. Re-run: **ALL GATES PASS**.
- **⚑ Raised, unresolved:** house-roster names are graded content with no declared vocabulary status — the same
  blind spot as C1 Block 6's 29 untriggered name items, one of CR-032's three occurrences. Proposed as a standing
  instrument (exemplar-like, not counted toward load); needs a ruling and is drive-wide.
- **PD numbering:** the ceiling moved 050 → 053 (here) → 056 (parallel session) during the session. STATE.md now
  records no next-free number, only the re-derivation command.
- **Paused for review before Day 2.**

---

## 11.08.26 — SCD · repo/status check (read-only) + push connectivity test

- **Task:** confirm `E:\EnglishDrive` is a clone; report Class 5 status. No build work.
- **Verified clone** of `github.com/enayetsyl/EnglishDrive.git`, branch `main`. ⚑ **Security:** the
  origin URL in `.git/config` embeds a GitHub PAT in plaintext — rotate and move to a credential
  helper or SSH remote.
- **C5 status reported:** B01–B06 promoted; `C5B07` (Adjective + Pronoun, W6) drafted complete in
  `_wip/` with 8 worksheets, `C5B0607-PT` and AK, extracts at `extracts/C5/_wip_B07/`, **not promoted.**
  Blocking: **no `run_all.py` run has ever been recorded for C5B07** (no `audits/reports/C5B07_*`), the
  manifest predates PD-036/PD-037/PD-054, the Assignment is outstanding against an existing
  `assignments/C5/C5_Eng_Assignment_W6.md`, the master header/TD extract disagree, and the master +
  STATE still cite **PD-036** for the Annual ruling now reissued as **PD-055**.
- **Tooling failure, recorded:** the agent's Linux shell would not boot for the whole session, so **no
  git command could be executed by the agent** — the `git pull` was run by the Principal manually, and
  this entry was written with the file tools and committed/pushed by the Principal.
