# C2 Block 6b — build state

**Block ID:** `C2B06b` · **Week:** W6 (Sun–Wed teaching, Thu PT) · **Master (planned):** `C2_ENG_Block06b_HaveHas_Match_v1.md`
**Topic:** have / has + match-to-make-a-sentence — second half of the W5–W6 two-week split block.

---

## Phase reached

**Phase 3 — Pre-build blueprint: DRAFTED (08.08.26), awaiting Principal approval.**
Phase 1 complete. Phase 2 complete — all 7 questions ruled. Blueprint at `_wip/C2B06b_blueprint.md`.
No build content drafted. No sentence bank drafted.

## Decisions confirmed

| # | Decision | Who / when |
|---|---|---|
| 1 | **PT shape: `C2B06b-PT` is its own W6 Performance Test**, per PD-025. The "combined 6a+6b PT / PD-028" line in the kickoff message was a **stale citation** and is disregarded — the Decision Log is authoritative. | Principal, 08.08.26 |
| 2 | Filename normalisation: 14 `" (1)"` suffixes stripped across `blocks/`; no collisions, no content change. | Principal, 08.08.26 · commit `e2a188a` |
| 3 | Stem convention **not** retro-renamed; forward-only rule added to CLAUDE.md §6. | Principal, 08.08.26 |
| 4 | `C4B04-AK` consolidated to `extracts/`; HW-2 #28 = *an*; `blocks/` duplicate removed. Logged **PD-030**. | Principal, 08.08.26 · commit `a8e329a` |
| 5 | PD numbering: agent assigns the next free number automatically (CLAUDE.md §3). Applied — **PD-028** (C3 B07 weighting), **PD-029** (C4 renumbering + `C4B0506-PT`), **PD-030**. | Principal, 08.08.26 · commit `a6e9347` |
| 6 | Lock-file workaround (rename aside; request delete permission first) approved as standing practice; noted in CLAUDE.md §1. | Principal, 08.08.26 |

## Orientation findings (Phase 1, verified at source)

- **Governing versions read:** Charter v1.5 · Run Book v1.17 · C2 Drive Plan v1.9 · Block-Build Starter Template v2 · Decision Log (working, through PD-030).
- **Format mirror:** `blocks/C2/C2_ENG_GrammarBlock06a_Verbs_v1.md` (v1.9) — the W5 half. Structure: Block-at-a-glance → verb staging table → Clue Card → teacher checklist → 4 day scripts (6 steps each, Exit Check per day, roll **14**) → 8 worksheets → Thursday PT → answer key → version log.
- **06a volumes:** CW 32–36 / HW 26–30 marks per sheet; **PT total 30** = Part A dictation 10 · Parts B–D 16 · Part E self-try 4.
- **Exam anchors for 6b (verified in the paper itself, not cited):** `Class 2 English Mohammadpur Final Question 2025.pdf` (AN25), magic bytes `25504446` — genuine PDF, not a mislabelled ZIP.
  - **AN25 Q12 [5]** — *"Fill in the blanks with 'have' or 'has'"*: Maryam __ / The child __ / The flowers __ / The giraffe __ / They __ . Mixed singular + plural subjects; bare blanks, no word box.
  - **AN25 Q11 [5]** — *"Match the words from the table to make five meaningful sentences"*: printed as **five mis-paired sentences to be re-formed**, not a two-column ruled table. Source rows: *He are dirty · The moon is the Quran everyday · His clothes reads at night · My father shines Muslims · We are a kind boy.*
- **Vocabulary (File 2):** W6 fresh batch **20 verbs** — come, get, put, give, help, show, point, use, know, brush, go, grow, wait, love, ride, eat, drink, fly, throw, sit. **Held scope at W6 = 121** (101 through W5 + 20). W5's 20 verbs are held and reusable.
- **Governing PDs in force:** PD-025 (two-week shape, one PT/week) · PD-026 (have/has is a function-word grammar target — no held-word trace needed, no §5.7 exemplar) · PD-027 (worksheet word box permitted where answers repeat; **PT boxless**) · PD-008 (de-patterning) · PD-010 (4-mark self-try) · PD-015 (Vocabulary Writing on every HW).
- **Assignment:** `assignments/C2/C2_Eng_Assignment_W6.docx` **already exists** and is a cumulative Blocks 1–5 revision sheet (naming/doing words, common-proper + capitals, a/an/the …). Whether 6b builds a new assignment is Phase 2 question 7.

## Phase 2 — all 7 ruled (Principal, 08.08.26)

1. **Sacred words excluded** from all 6b match strips, worksheets and PT; format mirrored on secular content. → **PD-031**
2. **Mirror the printed form** — numbered mis-paired sentences, pupil re-forms five, 1 mark each.
3. **Teach *I/we/you have* orally, grade 3rd person only**; bar *have got*, negatives, questions.
4. **W5+W6 held pool**; every W6 verb staged to its teaching day.
5. **Cross-half grading allowed**; PT zero-overlap gate widened to **all sixteen** sheets (6a's 8 + 6b's 8). Both declared explicitly in the master. → **PD-032**
6. **Held animals only**, 06a's forest/tree/pond restriction carried. **No giraffe.**
7. **6b builds its own assignment** per `AssignmentGenerator_Spec_v1_2` + Coverage Log — coverage check, novelty check, draft questions for review before finalizing. Timing per Charter §M.3 (after the PT). Existing W6 cumulative sheet stays as-is; blueprint flags coexistence.

## Blockers raised in the blueprint (need ruling before Phase 4)

- **`run_all.py` change required** for PD-032: `gate_pt_zero_overlap()` only compares within one manifest. Proposed additive `"audit_scope": "pt_overlap_only"` flag. Touches `audits/` — needs explicit approval.
- **Coverage Log is stale** — reads `last run = C5 W3 · 2026-07-21`; C2 ledger has no W4/W5 rows though those assignments exist. Spec §2 says the generator **halts**. Options (a) reconcile / (b) Special Instruction / (c) defer the assignment.
- **Confirm PT part split** — A 10 · B 5 · C 5 · D 6 · E 4 = 30.

## Exact next step

Principal reviews `_wip/C2B06b_blueprint.md` and rules the three open items in its §10.
On approval → **Phase 4 unit 1 = the hand-authored sentence bank**, which comes to the Principal
for approval **before any worksheet uses it**. **No build content before blueprint approval.**
