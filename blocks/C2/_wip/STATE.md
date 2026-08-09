# C2 Block 6b — build state

**Block ID:** `C2B06b` · **Week:** W6 (Sun–Wed teaching, Thu PT) · **Master (planned):** `C2_ENG_Block06b_HaveHas_Match_v1.md`
**Topic:** have / has + match-to-make-a-sentence — second half of the W5–W6 two-week split block.

---

## Phase reached

**Phase 4 — BUILT IN CHAT, IMPORTED TO `_wip/` 09.08.26. NOT AUDITED. NOT PROMOTED.**
Phase 1 complete. Phase 2 complete — all 7 questions ruled. Phase 3 blueprint **APPROVED** (Principal, 09.08.26).
Phase 4 was authored **outside the repo, in chat**, not unit-by-unit in-repo; the master (internal v1.1, including a
Principal inline-review pass) was imported on 09.08.26 as `_wip/C2_ENG_Block06b_HaveHas_Match_v1.md`.

**Consequence:** no `_wip/C2B06b_manifest.json` exists and `audits/scripts/run_all.py` has **never been run** on this
block. The file's own claims of "programmatically verified" gates come from the chat build, not from this repo's audit
suite, and do not satisfy CLAUDE.md §4. **The block may not be presented as final until the manifest is built and every
gate returns PASS.**

## Decisions confirmed

| # | Decision | Who / when |
|---|---|---|
| 1 | ~~**PT shape: `C2B06b-PT` is its own W6 Performance Test**, per PD-025. The "combined 6a+6b PT / PD-028" line in the kickoff message was a **stale citation** and is disregarded.~~ **REVERSED 09.08.26 — see decision 7.** | Principal, 08.08.26 |
| 2 | Filename normalisation: 14 `" (1)"` suffixes stripped across `blocks/`; no collisions, no content change. | Principal, 08.08.26 · commit `e2a188a` |
| 3 | Stem convention **not** retro-renamed; forward-only rule added to CLAUDE.md §6. | Principal, 08.08.26 |
| 4 | `C4B04-AK` consolidated to `extracts/`; HW-2 #28 = *an*; `blocks/` duplicate removed. Logged **PD-030**. | Principal, 08.08.26 · commit `a8e329a` |
| 5 | PD numbering: agent assigns the next free number automatically (CLAUDE.md §3). Applied — **PD-028** (C3 B07 weighting), **PD-029** (C4 renumbering + `C4B0506-PT`), **PD-030**. | Principal, 08.08.26 · commit `a6e9347` |
| 6 | Lock-file workaround (rename aside; request delete permission first) approved as standing practice; noted in CLAUDE.md §1. | Principal, 08.08.26 |

| 7 | **REVERSAL of decision 1 — the combined PT stands.** The chat-built master's **`C2B06ab-PT`** (30 marks, covering 6a doing-words/am-is-are **and** 6b have-has/match) is what is wanted. Logged **PD-041**, which overrides PD-025 for this cycle only. The 08.08.26 disregard is superseded, retained struck through. Blueprint annotated, not rewritten. | Principal, 09.08.26 |
| 8 | **Stale PD numbers corrected on import.** Combined-PT **PD-028 → PD-041**; block-local *field* **PD-029 → PD-012 (as extended by PD-035)**; Rabab-is-male **PD-030 → PD-042**. All three provisional numbers had already been taken in the Decision Log. | Agent, 09.08.26 |
| 9 | Master imported to `_wip/` under the blueprint's planned stem `C2_ENG_Block06b_HaveHas_Match_v1.md`; CRLF normalised to LF. **Not promoted** — promotion waits on the audit run and an explicit "done". | Agent, 09.08.26 |

---

## Pending — must close before promotion

1. **Manifest + full audit run.** Build `_wip/C2B06b_manifest.json` (schema `audits/scripts/README_manifest.md`) covering all 8 worksheets + `C2B06ab-PT`, then run `run_all.py` and save the verbatim report. **Nothing in this block has been checked by a script in this repo.**
2. **PD-032 widened PT zero-overlap — never run.** The gate must compare `C2B06ab-PT` against **all sixteen** sheets (6a's 8 + 6b's 8). The `audit_scope: pt_overlap_only` mechanism this needs now exists (PD-034). The imported master declares neither PD-031 nor PD-032; both declarations are owed in the file.
3. **PD-042 §H.5 re-screen.** Rabab is now male drive-wide. Only C2B06b has been swept; **every other delivered block still needs a non-mahram re-screen**, and the Charter §H.5 roster plus CLAUDE.md §5 house-character line still list Rabab as a girl's name.
4. **Pointers owed:** dependency pointer on `C2_ENG_GrammarBlock06a_Verbs_v1.md` ("W5 PT postponed; assessed in combined `C2B06ab-PT`, PD-041"); C2 Drive Plan §4/§7 forward-only note.
5. **Assignment (Phase-2 ruling 7) not built.** The Coverage Log is still stale (`last run = C5 W3 · 2026-07-21`, no C2 W4/W5 rows) — the generator halts per spec §2. Options (a) reconcile / (b) Special Instruction / (c) defer. Unruled.
6. **Blueprint blocker still open:** the `run_all.py` `audit_scope` change was requested in the blueprint; PD-034 has since ruled it, so this is now closed for scope but the run itself is outstanding.

## Next step

Build `_wip/C2B06b_manifest.json` from the imported master, run `python3 audits/scripts/run_all.py _wip/C2B06b_manifest.json --file2 file2/<C2 pool>`, paste the verbatim output, and bring any FAIL to the Principal before promotion.

---

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

~~Principal reviews `_wip/C2B06b_blueprint.md` and rules the three open items in its §10.~~
**RULED — see Principal ruling below (09.08.26).** Phase 4 may begin.
**Unit 1 = the hand-authored sentence bank**, which comes to the Principal for approval
**before any worksheet uses it**.

---

## Principal ruling — 09.08.26 (recorded cross-session)

**Blueprint APPROVED.** §10 rulings:

1. **§10-1 (audit_scope script change): already implemented and ruled** — PD-032/PD-034;
   the flag exists in `run_all.py` with self-test `selftest_audit_scope.py`. Nothing to write.
2. **§10-2 (Coverage Log): option (a) — reconcile first**, starting from
   `_wip/CoverageLog_reconciliation_draft.md`, then generate `C2B06b-AS`.
3. **§10-3 (PT split): confirmed** — A 10 · B 5 · C 5 · D 6 · E 4 = 30.

**Note for the build:** the audit suite has grown since the blueprint was written —
**PD-036** cross-sheet repetition gate (zero repeats across all the block's sheets;
the "≤2 identical/day" allowance is backstop only per **PD-038**), **PD-037**
option-list completeness (declare `options` on identify parts in the manifest) and
HW-key transcribability (no HW part's key positionally identical to its CW part).
See `governance/CORRECTIONS.md` and CLAUDE.md §5A — state applicable PATTERN/PROMOTED
rules before drafting each sheet. Next free PD number: **PD-039**.

---

## Audit run 1 — 09.08.26 · `audits/reports/C2B06b_audit_2026-08-09.txt`

Manifest `_wip/C2B06b_manifest.json` built from the master (9 sheets, 269 items; match items stored as the **formed**
sentence). **First script run in this repo.** **8 gates PASS · 5 FAIL.**

**FAIL 1 — de-patterning: 15 answer sets in strict has/have alternation.** CW1 C · HW1 A, B, C · CW2 A, B, D ·
HW2 A, B, D · CW3 D · HW3 D · CW4 D · HW4 D · **PT Part D**. A pupil can score the whole part by alternating.
The master states de-patterning was "programmatically verified (run ≤2, no strict alternation)" — the run-length rule
holds; the alternation rule does not. This is the single largest defect in the block.

**FAIL 2 — CW↔HW positional overlap over cap.** CW1↔HW1 **65%** · CW2↔HW2 **52%** (cap 35%).
Plus identical item texts over the ≤2/day backstop: CW3↔HW3 **6**, CW4↔HW4 **3**.

**FAIL 3 — PT zero-overlap: 4 Part D items** duplicate `CW2`, `CW4`, `CW4`, `HW4`.
These are the reuses **PD-041(c) already waives** (binary-target held-scope exhaustion). Gate cannot see the waiver —
record the ruling here and the FAIL is accounted for.

**FAIL 4 — HW key transcribability.** CW3↔HW3 Part D keys are positionally identical (`have · has · have · has · have`).

**FAIL 5 — cross-sheet repetition (PD-036): 29 sentences on more than one sheet**, several on three
(`Fatima has a story book`, `Aisha draws a triangle`, `Fatima and Jesmin have two books`, `My brother draws a car`,
`Aisha and Maryam ____ two jars`). Same defect class as C4B06's pre-promotion state.

**Passed:** within-sheet duplicates · option lists (26 parts) · rehearsal disjointness · **mark totals (all nine sheets
exact, PT 30/30)** · sacred-word · values lexicon · held-word · one-defensible-answer.

### Two findings no gate catches — human screens

1. **⛔ §H.9 attribution breach.** `The sun → gives us light` is a **graded match answer** in **CW3 Set 2** and
   **HW4 Set 1**, and a sample answer in the Tuesday script (line 260). CLAUDE.md §5 names this exact pattern:
   *"the sun gives…" → recast*. Natural phenomena may not act autonomously. **Three occurrences to recast.**
2. **Part-label mismatch between sheet and key.** CW1 and HW1 print Parts **A / B / C**; the answer key labels them
   `A_circle · B_fill · **D_underline**`. A teacher marking CW1 finds no Part C key. Cosmetic to fix, real in the classroom.

**Manifest limitation:** the held-word gate checked only 10 targets (the dictation list). *have/has* needs no trace
(PD-026) and match objects were not given triggers — declare them before the next run if the gate is to be meaningful.

---

## Triage ruling on Audit run 1 — 09.08.26 · **PD-045**

Each of the five failures was assessed for **assessment impact** before any content was drafted.

| Failure | Disposition |
|---|---|
| CW↔HW positional 65% / 52% | **Ruled acceptable — gate artefact.** The metric flattens all parts into one sequence; C2's HW sheets are shorter than their CW by design, so the comparison misaligns past the first part. CW3↔HW3 reads 0% while its Part D key is identical — the correctly-aligned `gate_hw_key()` is the governing test. `run_all.py` unchanged. |
| PT Part D, 4 reuses | **Ruled — already covered by PD-041(c).** |
| 38 have/has cross-sheet repeats | **Ruled acceptable** — rule-derived, no recall advantage (PD-044 principle). |
| **Strict alternation, 15 answer sets** | **DEFECT — 108 of 275 marks winnable by alternating.** CW3↔HW3 Part D's identical key closes with it. |
| **28 match-task cross-sheet repeats** | **DEFECT** — pupil recalls the pairing instead of working it out. 5 appear on three sheets. |

**Corrected this pass (no content touched):** CW1 and HW1 answer keys relabelled `D_underline` → `C_underline`
to match the Part C printed on those sheets.

**Held separately:** `The sun → gives us light` (CW3 Set 2, HW4 Set 1, Tuesday script) is a **§H.9 attribution
breach**, not an overlap question, and no ruling above covers it.

**Status:** the two defects are **OPEN**. Edit plan reported to the Principal 09.08.26; **no replacement content
drafted or applied** pending review of the scale.

---

## Audit run 2 — 09.08.26 · minimum-change repair applied · `audits/reports/C2B06b_audit_2026-08-09.txt`

**48 changes applied** to the master, answer keys and manifest together, exactly as approved. Nothing else touched.

- **#1 — 15 subject-number flips** (CW1 C1 · HW1 A1/B1/C1 · CW2 A8/B8/D8 · HW2 A1/B7/D1 · CW3 D1 · HW3 D5 · CW4 D1 · HW4 D6 · PT D8), each keeping the item's object, task, marks and part answer-class.
- **HW1 Part C #2 key correction** — *"We have a home."* was keyed `has` after the v1.1 sentence change and is now keyed `have`. A pupil underlining *have* was being marked wrong.
- **#5b — 32 of 33 match replacements** (CW3 6 · HW3 5 · CW4 14 · HW4 7). 26 are one-word subject swaps; 6 change an object noun where no other subject makes sense. The 33rd, `The sun → gives us light`, is **deliberately not changed** — held for the §H.9 decision.
- **Printed match columns re-deranged** on 5 of the 12 changed sets (HW3 Set1/Set3, CW4 Set1/Set3, HW4 Set1); the other 7 retained their existing shuffle, which was still a valid derangement.

**Result: 11 PASS · 3 FAIL — every failure already ruled.**

| Gate | Before | After |
|---|---|---|
| De-patterning | FAIL — 15 alternating sets | **PASS** |
| HW key transcribability | FAIL — CW3↔HW3 Part D | **PASS** |
| Cross-sheet repetition | FAIL — 66 repeats | FAIL — **32** (31 have/has, ruled PD-045(5a); +1 the held sun item) |
| CW↔HW positional overlap | FAIL — 65% / 52% | FAIL — 54% / 40% (gate artefact, ruled PD-045) |
| PT zero-overlap | FAIL — 4 items | FAIL — same 4 (**PD-041(c) waiver intact**) |
| Mark totals | PASS | **PASS — all nine sheets unchanged** (32/26/34/25/34/28/38/28, PT 30) |

Within-sheet duplicates, option lists, rehearsal disjointness, sacred-word, values lexicon, held-word and
one-defensible-answer all PASS.

**Not touched, as instructed:** the two pre-existing same-verb sets (CW3 Set 4 *brush/brushes*, HW3 Set 3 *goes/go*) —
noted only; the pairs stay unambiguous on number and gender.

## §H.9 attribution — CLOSED 09.08.26 (Option A, predicate only)

`The sun → gives us light` is recast in all three places, one cell each:
**CW3 Set 2 → *comes in the morning*** · **HW4 Set 1 → *goes in the evening*** · **Tuesday script sample** matched to
the CW3 form. *come · go · morning · evening* are all held. The two graded forms differ, so no new repeat is created.
**PD-031 ruled out** the attribute-by-naming alternative — no sacred word may sit in a match strip — so a secular
non-giving predicate was the only compliant route. Logged **CR-023**; this is the **2nd occurrence of the CR-004
attribution type**, one short of PATTERN.

## Audit run 3 — 09.08.26 (final for this pass)

**11 PASS · 3 FAIL, and every failure is already ruled.** Cross-sheet repetition is down to **31 — all of them
have/has items** ruled acceptable under PD-045(5a); no match repeat and no attribution item remains.
CW↔HW positional (54% / 40%) is the ruled gate artefact; PT zero-overlap is the four PD-041(c) waived reuses.
**Mark totals unchanged on all nine sheets.** Corrections logged: **CR-020 … CR-024**.

---

## PD-032 widened PT zero-overlap — RUN 09.08.26 · ⚑ 2 NEW findings, no content changed

6a's **eight worksheets (256 items)** were loaded into `_wip/C2B06b_manifest.json` as reference sheets carrying
`"audit_scope": "pt_overlap_only"` (the PD-034 mechanism), so they are visible **only** to the PT overlap gate and are
not re-audited. `C2B06ab-PT` is now compared against **all sixteen sheets**, 442 worksheet items in total. 6a's own
unadministered PT was **not** loaded: PD-032 scopes the widening to the eight worksheets, and PD-041(a) carries 6a's
PT items into the combined paper by design, so comparing against it would flag the carry itself.

**Result — the 6a side of the PT is NOT disjoint, contrary to the master's claim.**

| PT item | Duplicates |
|---|---|
| Part C #1 — `I ___ in the classroom.` | `6a-CW4` |
| Part C #5 — `The birds ___ in the tree.` | `6a-CW3` |

**Why this matters more than the four Part D hits.** PD-041(c) waived verbatim reuse **for the have/has section only**,
and states in terms that *"dictation, doing-word, am/is/are and match remain fully disjoint"*. These two are **am/is/are**
items, so they sit **outside** the waiver and contradict a recorded consequence of PD-041. The master's answer-key note
— *"PT: match/dictation/6a-side fully disjoint from worksheets"* — is disproved by this run.

**RULED 09.08.26 — PD-046. Both items stand; neither is re-authored.** Each answer is derived from the subject by the
taught rule (*I* → **am**, plural → **are**), so a pupil who met the sentence in W5 holds no advantage over one applying
the rule — the PD-044 reasoning, applied per-item. Valid delivered PT content is not rewritten to resolve a
governance/scope mismatch that carries no marks consequence.

**PD-046 is deliberately narrow.** It is scoped to `C2B06b` and to these two item texts only. It **does not amend
PD-041(c)** or alter a word of it — that waiver still reads, as written, that only the have/has section is waived and
am/is/are stays disjoint. It creates **no drive-wide waiver**, and **no change to the zero-overlap standard for future
blocks** (`gate_pt_zero_overlap()` unchanged, `CROSS_SHEET_MAX_REPEATS` still 0, PD-036/PD-038 unamended).

**One thing the ruling does not cover:** the master's answer-key line *"PT: match/dictation/6a-side fully disjoint from
worksheets"* is **false** and this run proves it. It stays in the delivered file only because correcting it is a content
edit declined at this stage. Recorded here so no future build cites it as verified.

**All other gate results are unchanged by the widened run** — the manifest addition is additive and invisible to every
gate except PT overlap.

## CR-023 — one occurrence from PATTERN

The `The sun → gives us light` recast is the **2nd** occurrence of the CR-004 attribution type (autonomous natural
giver). Under CLAUDE.md §5A a **3rd** makes it PATTERN and obliges a proposal for a script check or standing rule.
Flagged only — no rule introduced, nothing edited.

## Owed pointers — DONE 09.08.26

- `blocks/C2/C2_ENG_GrammarBlock06a_Verbs_v1.md` — forward-only dependency pointer above its PT section
  (*W5 PT postponed; assessed in combined `C2B06ab-PT`, PD-041*) plus a **v1.5 version-log row**. Pointer only:
  no teaching content, item, key or mark total in 6a was touched.
- `governance/driveplans/C2_ENG_DrivePlan_v1_9.md` — forward-only notes at **§4** (combined PT this cycle) and
  **§7** (both AN25 anchors examined in the combined paper, per-anchor split preserved). No row amended.

## Still outstanding (parked by Principal instruction)

1. **PD-042 §H.5 re-screen** — drive-level; Rabab now male, only this block swept. Not expanded.
2. **W6 assignment** — blocked on the stale Coverage Log (`last run = C5 W3 · 2026-07-21`); the generator halts per
   spec §2 and the reconcile/Special-Instruction/defer choice is unruled. Not built.
3. **The two 6a-side PT items above** — awaiting ruling.

---

## C2B06b — CLOSED, content-complete · 09.08.26

**Final suite run (widened manifest, all sixteen sheets): 11 PASS · 3 FAIL — every failure ruled, none unruled.**

| Failure | Ruling |
|---|---|
| CW↔HW positional 54% / 40% | **PD-045** — gate artefact (flattened, misaligned comparison across unequal part lengths) |
| PT zero-overlap — 4 Part D items | **PD-041(c)** — have/has held-scope exhaustion, waiver intact and unamended |
| PT zero-overlap — 2 Part C items vs 6a | **PD-046** — rule-derived answers, no assessment advantage; block-scoped |
| Cross-sheet repetition — 31 texts | **PD-045(5a)** — all have/has, rule-derived |

Mark totals exact on all nine sheets (32 · 26 · 34 · 25 · 34 · 28 · 38 · 28 · PT 30). De-patterning, HW-key
transcribability, within-sheet duplicates, option lists, rehearsal disjointness, sacred-word, values lexicon,
held-word and one-defensible-answer all PASS. The master has not been touched since the §H.9 recast — verified by diff.

**Parked, not blocking closure:** PD-042 §H.5 drive-wide re-screen · W6 assignment (blocked on the stale Coverage Log)
· CR-023 one occurrence from PATTERN. **PROMOTED 09.08.26** on the Principal's "done" — master now at `blocks/C2/C2_ENG_Block06b_HaveHas_Match_v1.md`.

---

## PROMOTION — 09.08.26

Principal: *"C2B06b is done. You may promote it from `_wip`."*

Master moved `blocks/C2/_wip/` → **`blocks/C2/C2_ENG_Block06b_HaveHas_Match_v1.md`**. `_wip/` retains the blueprint,
this STATE file and `C2B06b_manifest.json` (the manifest stays with the audit trail, as C4B06's did) — no `_wip/`
history cleared.

**Not yet generated: the student extracts.** The master's own *Extract manifest* section lists them as
regenerate-only from this file — CW1–4, HW1–4, `C2B06ab-PT`, `C2B06b-AK`, `C2B06b-CC`, `C2B06b-TD`. C4B06 shipped 13
extracts to `extracts/C4/` at promotion; C2B06b has none in `extracts/C2/` beyond the 6a set. Flagged as the next
deliverable, not assumed.

