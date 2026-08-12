# English Drive — Assignment Generator Specification

**File:** `English_Drive_AssignmentGenerator_Spec_v1_4.md`
**Version:** v1.4 · 2026-08-12
**Status:** Active specification — **FROZEN** (Principal ruling 2026-07-21). Future Drive Plan revisions are handled as integration updates (new declarations consumed via §2.1, §3.9, and the input files), not as changes to this algorithm.
**Authority:** Sits under the Project Charter (v1.2) and Run Book (v1.3). Where this specification conflicts with the Charter, the Charter wins. This specification governs weekly Assignment generation only; it does not alter block-build, Performance Test, or extract-generation procedure.

---

## 1. Purpose & Scope

The weekly **Assignment** is a completion-based revision sheet, given at school on Thursday after the Performance Test, completed Thursday–Saturday, submitted Sunday (Run Book §9.1–9.2).

Its primary purpose is **systematic rotational revision** of all blocks completed to date, so that every previously taught topic returns on a predictable cycle. Fresh practice of the week's current set (§2.1) is a secondary purpose — current-set blocks already receive their practice through CW, HW, and the Performance Test.

This specification defines:

- the inputs a generation run requires (§2),
- the composition rules for the assignment itself (§3),
- the automatic block-rotation system (§4),
- the optional Special Instruction input (§5),
- the outputs of each run, including the teacher Answer Key and designer briefs (§6),
- the **Coverage Log**, its structure, update procedure, and use (§7),
- the verification checklist run before delivery (§8).

A weekly generation prompt simply invokes this specification; no rules live in the prompt itself.

---

## 2. Inputs per Generation Run

| # | Input | Source | Required |
|---|---|---|---|
| 1 | Class + week number | Stated in the prompt | Yes |
| 2 | Current-set block file(s) — every block in C(N) (§2.1); none for a consolidation-only week | Upload or project file | Yes, when C(N) ≠ ∅ |
| 3 | Class Drive Plan (current version) | Project file | Yes |
| 4 | **Coverage Log** (current version) | Project file | Yes, from the first logged week onward |
| 5 | Vocabulary Pool + Batch Order | Project files | Yes |
| 6 | Special Instruction | Stated in the prompt | Optional (§5) |

### 2.1 Week model — Current Set and Completed Set

For any assignment week N:

- **Current Set C(N)** — the block(s) under teaching in week N, as declared by the class Drive Plan §4 for that week and restated in the weekly prompt. The set may contain one block, several blocks, or be empty (a consolidation-only week).
- **Completed Set** — the block(s) whose teaching **finishes** in week N. A single-week block completes in its teaching week; a multi-week block completes only in its final week and belongs to the Current Set of every week it spans.

**Bridge content** is not a rotation unit: bridges never appear in a Current Set, never receive a Coverage Log ledger row, and are delivered — when scheduled — inside their host block's part.

**Declaration vs. behaviour.** The Drive Plan §4 declares each week's Current Set, including declaring a week consolidation-only (C(N) = ∅). This specification owns the behaviour on whatever is declared. The weekly prompt restates the declaration; the generator verifies **membership** against Drive Plan §4 and halts on mismatch. The **order** of current-set members is taken from the weekly prompt, not from the Drive Plan table's physical layout; if the prompt states no discernible order, members are ordered by block ID ascending.

**Consolidation-only weeks (C(N) = ∅):** the current-set share (§3.1) transfers to the revision component — the paper becomes ~90% rotation-selected revision + ~10% Challenge. Rotation, weighting, deferral, logging, and the weekly sequence run unchanged; one-week variations are made via Special Instruction (§5), never by ad-hoc departure from this rule.

Previous assignments are **not** uploaded. The Coverage Log replaces them (§7). If the Coverage Log is missing or stale, the generator halts and flags it rather than reconstructing history by assumption.

---

## 3. Assignment Composition Rules

### 3.0 Definition — "item"

An **item** is one written or marked student response: one blank, one classification, one rewrite line, one end-mark, one table cell, one picture judged. A compound prompt counts each response separately (e.g., "Noun: ___ Reason: ___" = 2 items; a rearrange-and-name-the-type line = 2 items). A Challenge counts each required sentence or labelled step as one item. All ratio, weighting, and checklist computations in this specification use this count.

### 3.1 Content ratios

| Component | Share of items | Notes |
|---|---|---|
| **Revision** (previously completed blocks) | **≈ 70%** | Split across the rotation-selected blocks (§4) |
| **Current set** (all blocks in C(N)) | **≈ 10–20% in total** | Split equally among current-set members; a member's share may not be reallocated to another member. If C(N) = ∅, this share transfers to the revision component (§2.1) |
| **Challenge / Self-Try** | **≈ 10%** | Create-level, closes the paper |

Ratios are targets, not exact counts; the verification checklist (§8) confirms the paper lands inside these bands.

> **⚑ Class 5 exception (PD-058, 12.08.26).** These ratios are **superseded for Class 5** from the assignment of W8. C5 order and weight follow the Scholarship 2026 question map — see **§3.12(f)**. Classes 1–4 are unaffected.

### 3.2 Skeleton and ordering

1. **Revision parts** open the paper — one part per selected revision block, ordered oldest block first, so cognitive demand can climb naturally down the page.
2. **Current-set part(s)** follow the revision parts — one part per current-set member, in the order declared by the weekly prompt (§2.1). Omitted entirely when C(N) = ∅.
3. **Challenge (⚡)** always closes the paper.

Parts are lettered A, B, C… continuously. There is no fixed part count; the paper carries as many parts as the rotation requires.

> **⛑ Class 5 exception (PD-058, 12.08.26).** This skeleton is **superseded for Class 5** from the assignment of W8: C5 questions are **numbered at their Scholarship 2026 question numbers**, in the paper's order, not lettered revision-first. See **§3.12(a), (f)**. Classes 1–4 are unaffected.

### 3.3 Vocabulary integration — no standalone vocabulary section

Vocabulary is **not** given its own part. Held-pool words are woven into the sentences, passages, tables, and word boxes of the block-revision parts themselves. Rules:

- Every graded item uses **held vocabulary only** (all batches released up to and including the current week).
- The current week's fresh batch should appear naturally somewhere in the paper.
- Word boxes remain permitted as *scaffolds inside a block part* (e.g., a fill-in part revising Nouns draws its box from held nouns); each box word is used exactly once.
- Rotate earlier batches so no batch is entirely absent for long stretches; avoid featuring the same word two consecutive weeks.
- Class 1 fixed drills (months sequence, letter-words) follow the Drive Plan §5 rotation and count as revision content, independent of block rotation.

### 3.4 Marks and assessment

- Assignments carry **no marks and no marking scheme**. They are completion-based.
- No mark tags (e.g., `[12]`) appear anywhere on the student sheet.
- The Challenge is reviewable against the Charter §I rubric at the teacher's discretion, but is not scored on the sheet.

> **⛑ Class 5 exception (PD-058, 12.08.26).** Class 5 assignments **do** print Scholarship mark tags from W8 — see **§3.12(c)**. They remain completion-based; the tags teach the paper's weighting and are not a marking scheme. Classes 1–4 keep this section in full.

### 3.5 Length

- Baseline: ~3 pages (Classes 1–2), ~4 pages (Classes 3–5).
- As completed blocks accumulate, the paper **may lengthen** to honour the rotation guarantee (§4.4) — length yields to coverage, within reason. If a paper would exceed baseline by more than 50%, the generator automatically defers the lowest-fill-priority **fill** block (never a mandatory block; §4.2.4), records the deferral in the log `Note` column, and grants the deferred block top fill-priority the following week. If no fill block remains to defer, the paper lengthens (§4.2.4) and the overrun is noted in the log.

> **⛑ Class 5 exception (PD-058, 12.08.26).** The baseline-plus-50% deferral trigger is **replaced for Class 5** by the growth ramp at **§3.12(e)**. No C5 fill block is deferred on length. Classes 1–4 are unaffected.

### 3.10 Reading component — Class 5 only (from 13.08.26)

Effective with the assignment of **13 August 2026** (Principal ruling C-9, immediate), every **Class 5** assignment carries a **reading passage with passage-based items**. Classes 1–4 are unaffected.

1. **One passage per assignment.** 4–8 sentences at Phase A, lengthening with the class's demonstrated level.
2. **Sourcing.** Passages are taken **verbatim** from *English for Today* Class 5 — never paraphrased or re-authored, since "seen text" is the examined property. The §H curation screen is applied at **selection**; sacred matters are never graded test targets. Prioritise the units the papers draw on (U2, U4, U7, U14, U19) and the narrative units; rotate units, tracked in the Coverage Log `Passage` column.
3. **Phase A formats** (default): answer in a full sentence at the 3-mark shape · lift-and-reshape · match word to meaning · True/False · fill from a box.
4. **Phase B formats** (introduced by performance, not by date): inferential and "what would you do" items · obedience to a length instruction ("answer in three sentences").
5. **Progression is diagnostic-driven** (ruling C-5): the ungraded diagnostic of 13.08.26 sets the entry level; difficulty rises with demonstrated performance. Do not assume a single class level.
6. **Marking guidance** on the answer key must state that reading answers are expected **in complete sentences**.
7. The passage part sits with the revision parts in the §3.2 skeleton, before the Challenge.

### 3.11 Fast-teach drips — Class 5 only

| Drip | Starts | Volume |
|---|---|---|
| **FT-1 rearrangement** | assignment of R5 (20–24.09.26) | **2 items** in every assignment, to the examinations |
| **FT-2 form-fill · cardinal/ordinal numbers** | assignment of R7 (4–8.10.26) | revision items as the rotation allows |

Drip items count against the **revision** share (§3.1) and are recorded in the Coverage Log `Drip` column.

> **Cap discipline (unchanged).** §3.5's length rules and the 40-minute working cap are **not** relaxed by §3.10 or §3.11. Where space is tight, **grammar drip volume yields to the passage**, never the reverse; the deferral machinery of §3.5/§4.2.4 operates exactly as before.

### 3.6 Picture-based parts (Classes 1–2 only)

- Picture activities are permitted **only** in Class 1 and Class 2, and only where they serve the learning objective (e.g., singular/plural discrimination, sorting).
- The generator does **not** produce images. It produces a **Designer Brief** (§6.3) for each picture part, written to be pasted directly into an image-generation tool.
- Imagery constraints: inanimate objects only, no humans or animals, no facial features or personification, age-appropriate, Islamic-aligned, and directly matched to the item's answer key. Plants (trees, flowers) have appeared in delivered practice; their continued use is permitted unless the Principal rules otherwise under REF-01 / Charter §H.8.

### 3.7 Language, names, and values

- Instruction language follows the established gradient: Bengali gloss mandatory in Classes 1–2, selective in Class 3, minimal in Classes 4–5. Student-facing instructions lead in English per the drive-wide convention.
- Names draw from the established set (Yusuf, Aisha, Hamza, Maryam, Nusair, Raima, Rabab, Abdullah, Porshi…); settings stay within home / school / masjid / village / market contexts.
- Full Charter §H curation applies. **Sacred-word guard (§H.3):** du'ā sentences may appear as sentence-type or structure *examples* where the classification target is the sentence, never the sacred word; Allah / Qur'an are never a fill-blank answer or classification target.

### 3.8 Bloom's discipline

- The paper climbs within the class's Charter §G.2 band: recall/identify items early, apply mid-paper, the class's upper-band work late, Challenge at (guided) Create. It never opens at the band's top.
- Reasoning items ("write the reason") appear from Class 3 up; verify-and-correct (Evaluate-lite) items from Class 4 up.
- One modelled example ("The first one is done for you") whenever a format is new to assignments or has not appeared for 2+ weeks.

### 3.9 Formats

- All items use exam-mirror formats from the class Drive Plan §7.
- A revision part defaults to the format the block was originally practised/tested in; a second permitted format may substitute for variety, but not two weeks running for the same block (tracked via the Coverage Log, §7).

---

## 4. Block-Rotation System

### 4.1 Eligible set

All blocks with a Coverage Log ledger row (i.e., **completed**) up to and including week N−1. Blocks currently in progress — members of a Current Set that have not yet completed — are **not** eligible for rotation; a half-taught block is never revised. Members of C(N) are handled by §3.1 and are not part of rotation.

### 4.2 Selection algorithm

Applied in order:

1. **Mandatory — previously completed.** Every block in the **Completed Set of week N−1** is selected. This may be zero, one, or several blocks. If it is zero (the prior week completed nothing — e.g., a non-final week of a multi-week block, or a consolidation-only week), no mandatory slot arises from this rule and rule 3's fill obligation absorbs the capacity.
2. **Mandatory — overdue blocks.** Any completed block absent from the **two most recent assignments** is selected (the "no block skips more than two consecutive assignments" guarantee).
3. **Fill — mandatory to cap.** After rules 1–2, the generator **must** continue selecting until the cap (rule 4) is reached or the eligible set is exhausted — it may not stop short. Selection order: longest-absent-first; ties break toward the block with the fewest lifetime assignment appearances; remaining ties break toward the older block.
4. **Cap.** Default cap: **5 revision blocks** per assignment. If mandatory selections (rules 1–2) alone exceed the cap, the cap yields and all mandatory blocks are included — mandatory blocks are never deferred. Only fill blocks (rule 3) may be deferred, and only by the automatic §3.5 length rule.

### 4.3 Weighting

Selected revision blocks receive **equal item weight by default**. Unequal weighting occurs only via a Special Instruction (§5), and the log records it.

### 4.4 Guarantee

Under the default cap of 5, the rotation guarantees every completed block appears at least once in every three consecutive assignments, for drives of up to ~15 completed blocks — comfortably above any class's block count. §3.5 deferral cannot break this guarantee: any block absent from the two most recent assignments becomes mandatory under rule 2, and mandatory blocks are never deferred (rule 4).

> **⛑ Class 5 exception (PD-058, 12.08.26).** The §4.2 rule-4 cap of 5 is **lifted for Class 5** from W8 — every completed block is eligible every week (**§3.12(d)**). The guarantee is therefore met trivially for C5. Classes 1–4 keep the cap.

---

## 5. Special Instruction (optional input)

A one-run override supplied in the weekly prompt. Typical uses:

- **Weak-topic boost:** "Performance Test showed weakness in plural −es; give the Plural block double weight this week." The named block is force-selected and over-weighted; another fill-slot block is displaced.
- **Force-include / force-exclude** a specific block for one week.
- **Format request** for a particular part.

Rules:

1. A Special Instruction affects **one assignment only**; it never permanently modifies this specification.
2. It may not breach Charter constraints (held-word discipline, sacred-word guard, Bloom band, curation).
3. Any block displaced by a Special Instruction inherits top fill-priority the following week, so rotation fairness self-corrects.
4. The instruction and its effect are recorded in the Coverage Log (§7.2, `SI` column).

---

## 6. Outputs per Generation Run

Each run delivers, in this order:

### 6.1 Assignment (student sheet)

- File name: `C{class}_Eng_Assignment_W{week}` (matching delivered practice, e.g., `C3_Eng_Assignment_W2`).
- School header block, Class line ("Class X – English Grammar Campaign"), "Assignment – Week N", Name/Date lines.
- No answer content, no marks, no dictation lists.

### 6.2 Answer Key (teacher sheet, separate file)

- File name: `C{class}_Eng_Assignment_W{week}_AnswerKey`.
- Teacher-facing only; never merged into the student sheet (consistent with the drive-wide master-only key convention).
- One answer per item; Challenge entries state acceptance criteria ("any grammatical sentence using a held noun, correct type named") rather than a single model answer, plus one model answer for teacher reference.
- Standard de-patterning verification applies to any choice/classification parts (max column-run ≤ 2), checked programmatically before delivery.

### 6.3 Designer Brief (Classes 1–2, only when a picture part is included)

- Delivered as a clearly separated section after the Answer Key (not a separate file unless requested).
- Contains, per image set: exact object list and counts, layout (grid, boxes), style ("simple black-line colouring-book style, white background, no text, no humans or animals, no faces"), and the intended answer each image encodes.
- Written to be pasted verbatim into an image-generation tool.

### 6.4 Updated Coverage Log

- The full replacement Coverage Log file (§7.3), reflecting this week's assignment. Delivered every run, saved back to the project by the Principal.

---

## 7. Coverage Log Specification

### 7.1 File identity

- **One shared file for all five classes:** `English_Drive_AssignmentCoverageLog_v{n}.md`, containing five class sections (C1–C5).
- Markdown tables only; no prose narratives. Target size: under two pages even at drive end.
- The log stores **only what future generation needs** — never item text, sentences, or answer content.

### 7.2 Structure

The file opens with a single **state line**: `Log state: last run = C{class} W{week} · {date}`. Every run rewrites this line.

Each class section contains exactly two tables.

**Table 1 — Block Ledger** (one row per completed block; the rotation engine reads this)

| Column | Content |
|---|---|
| Block | Block ID and short name (e.g., `B02 Sentence Types`) |
| Taught | Week the block **completed** (e.g., `W2`); multi-week blocks record the span (e.g., `W9–W10`) with the completion week governing all computations |
| Appearances | Total assignments the block has appeared in (integer) |
| Last seen | Most recent assignment week (e.g., `W2`) |
| Last format | Format code/short label used at last appearance (e.g., `type-ID`, `end-marks`, `fill-table`) |

**Table 2 — Assignment History** (one row per generated assignment; audit trail and SI tracking)

| Column | Content |
|---|---|
| Week | Assignment week (e.g., `W2`) |
| Current | Current Set for the week, comma-separated (e.g., `B08, B09`), or `—` for a consolidation-only week |
| Revision | Blocks revised, comma-separated (e.g., `B01`) |
| SI | Special Instruction applied, one short phrase, or `—` |
| Note | At most one short flag (e.g., `length over baseline`, `B03 displaced → priority W5`), or `—` |

**Class 5 only — two additional Assignment History columns (v1.3):**

| Column | Content |
|---|---|
| Passage | *EfT* unit used and phase, e.g. `U7 / A` — so units rotate and phase progression is visible |
| Drip | Fast-teach items carried, e.g. `FT-1×2`, `FT-1×2, FT-2×1`, or `—` |

Nothing else is stored. Vocabulary batch release is already tracked by the Batch Order files and is not duplicated here; the generator reads batch state from those files directly.

> **Individual student tracking is NOT stored in the Coverage Log** (Principal ruling C-6, 10.08.26). Per-student progress sheets — weaknesses, improvement, recurring mistakes, progress over time, areas needing practice — are a **separate artefact** whose owner and template remain open implementation items. The Coverage Log remains a class-level generation-state file and must not become a student record.

### 7.3 Update procedure

1. The generator updates the log **at the end of every generation run**, as the final output (§6.4), never before the assignment is finalised.
2. Update = full file replacement: increment Appearances / set Last seen / set Last format for every block used; add one Assignment History row; add a Block Ledger row for **each block in the week's Completed Set** (each becomes rotation-eligible from the next week). In-progress blocks receive **no** ledger row; the in-progress state is inferred, without any additional column, from a block appearing in a recent Assignment History `Current` cell while having no ledger row.
3. The Principal saves the delivered log back into the project, replacing the previous version. The file version number increments only on **structural** changes to the log format (governed by this spec), not on routine weekly updates.
4. If a delivered assignment is later revised in a way that changes block coverage, the log is corrected in the next run and the correction noted in the `Note` column.
5. **Sequential runs only.** Generation runs — across all classes — form a single sequence. Every run must take as input the log produced by the immediately preceding run of *any* class, as identified by the state line. Two runs must never be generated from the same log version in parallel; if this occurs, the second output log is invalid and that run is repeated from the surviving log. The Principal saves each delivered log back to the project before starting the next run.

### 7.4 How the generator uses the log

1. **Eligibility & rotation (§4):** the Block Ledger's `Taught`, `Last seen`, and `Appearances` columns drive the entire selection algorithm. "Absent from the two most recent assignments" is computed from `Last seen` against the two most recent Assignment History rows.
2. **Format variety (§3.9):** `Last format` prevents the same block appearing in the same format two assignments running.
3. **SI fairness (§5.3):** a `Note` recording a displaced block grants that block top fill-priority in the next run.
4. **Halt condition:** if the log's latest Assignment History week is not W(N−1) for a week-N run, the generator flags the gap and asks before proceeding — it never invents missing history. The generator also echoes the input log's state line at the start of every run; if the state line is missing, or the log does not contain the Assignment History row the state line implies, the generator halts and flags a possible parallel-run overwrite.

### 7.5 Seeding

The log must be seeded once with the already-delivered W1 (B01 assignments) and W2 assignments for all five classes before the first automated run. Seeding is a one-time build task performed from the delivered files, not from memory.

---

## 8. Verification Checklist (run before delivery, every run)

- ☐ Ratios within §3.1 bands (item counts computed per §3.0, not estimated)
- ☐ Rotation rules §4.2 satisfied; no block absent three consecutive assignments
- ☐ All graded content uses held vocabulary only (checked against Pool + Batch Order)
- ☐ No standalone vocabulary section; fresh batch words present in-context
- ☐ Sacred-word guard §H.3 and full §H curation pass
- ☐ Bloom climb within class band; no over-band item
- ☐ De-patterning on choice/classification parts (max run ≤ 2, programmatic)
- ☐ No marks on student sheet (**C1–C4**; C5 from W8 prints Scholarship tags per §3.12(c)); no answer content on any student sheet
- ☐ Picture parts: C1–2 only, Designer Brief present, imagery constraints met
- ☐ File names per §6; header block correct
- ☐ Coverage Log: input state line echoed and verified (§7.4.4), log updated with new state line, and delivered
- ☐ **C5 only:** reading passage present, sourced **verbatim** from *EfT* C5, §H-screened at selection, unit not repeated from the previous run; phase appropriate to demonstrated level; answer key states the full-sentence expectation
- ☐ **C5 only:** FT drips present at the correct volume once their start week has passed (FT-1 from R5; FT-2 from R7)
- ☐ **C5 only (from W8):** length inside the §3.12(e) ramp for the current week band; where tight, item counts were reduced and **no question was dropped**
- ☐ **C5 only (from W8):** questions carry their **Scholarship numbers** in paper order; unlocked questions per §3.12(b) all present; no question dropped once unlocked
- ☐ **C5 only (from W8):** Scholarship mark tags printed per §3.12(c); still no marking scheme, model answer or score box on the sheet
- ☐ **C5 only (from W8):** §3.12(g) growth discipline — every item added since the previous run traces to a newly unlocked question or to raising an existing question toward its Scholarship item count
- ☐ **C5 only (to R7):** Revision section carries only blocks with no Scholarship mapping (B3, B5); it closes at R7 per §3.12(h)
- ☐ **C5 only, pre-W8 runs:** length still inside §3.5 baseline rules — the passage has not been used to justify an overrun
- ☐ **No reading component or Part R has been retrofitted into Blocks 1–7 material** (delivered blocks are frozen)

---

## 9. Governance Notes

1. **Run Book alignment.** Run Book v1.3 §9.4 states assignments are generated "as part of the standard block-build process." This specification formalises assignment generation as a distinct weekly workflow. A one-line Run Book amendment pointing §9.4 to this specification is **pending** and should be batched with the next Run Book update. Until then, this specification governs assignment generation and the Run Book governs everything else.
2. **Change control.** Changes to ratios, rotation rules, or log structure require a Principal ruling and a version increment of this file, logged in the Decision Log.
3. **Decision Log.** Adoption of this specification (revision-first ratios, no-marks policy, separate answer key, shared Coverage Log, Special Instruction mechanism, C1–2 designer-brief policy) constitutes a Project Decision and should be logged.
4. **Consolidation-week ownership.** Drive Plan §4 owns the *declaration* of consolidation-only weeks; this specification owns the *behaviour* (§2.1: current-set share transfers to revision). The pending Drive Plan review should ensure each class's §4 marks its consolidation weeks explicitly.
5. **Bridge ruling.** Principal ruling 2026-07-21: bridge content folds into its host block and is not an independent rotation unit (§2.1).

---

*Version log*

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-07-21 | Initial specification. Ratios, rotation system, Special Instruction input, output set (assignment + answer key + designer brief + log), and Coverage Log structure defined per Principal rulings of 2026-07-21. |
| v1.1 | 2026-07-21 | Blocker amendments per specification review: item definition added (§3.0); fill-to-cap made mandatory (§4.2.3); overload resolution unified under §4.2.4 with automatic fill-only deferral in §3.5 (no routine Principal confirmation) and §4.4 guarantee note; shared-log sequential-run procedure with state line (§7.2, §7.3.5, §7.4.4); §8 checklist aligned. AMD-5 (multi-block/consolidation weeks) and AMD-6 (format-code registry) held pending Drive Plan review — spec text unchanged for those areas. |
| v1.4 | 2026-08-12 | **Class 5 Scholarship-style progression ruled (PD-058; C5 only, C1–C4 behaviour wholly unchanged).** New **§3.12** makes the Primary Scholarship Examination 2026 pattern the **primary format target** for the C5 assignment from **W8**: questions authored at their **Scholarship numbers** in the paper's order, wording and scaffolding, carrying only taught content, with a **week-by-week unlock map** (Q12 at R1 · Q8 at R3 · Q9 as taught content at R5 · Q7 affix alternative at R6 · Q10 and Q11 at R7 · Q13 at R8 · Q14 at R9; Q4/Q5 at R1 on a second, unseen passage). **Four C5 exemptions granted, each annotated at source: §3.4** — Scholarship **mark tags now print** on the C5 sheet (`[1x5=5]`) while assignments stay completion-based, no marking scheme or score box; **§4.2 r.4** — the 5-block **rotation cap is lifted**, every completed block eligible every week; **§3.5** — the baseline-plus-50% **deferral trigger is replaced** by a four-band growth ramp (~5pp/45min at W8–R1 rising to the full 14-question shape/90min at R8–R10), with item counts inside questions reducing before any question is dropped; **§3.1/§3.2** — ratios and revision-first skeleton **superseded**, order and weight following the Scholarship map, with two guarantees preserved (the current-set block carries at least one item; the paper still climbs within its Charter §G.2 band). **Endpoint boundary recorded:** the ramp stops at **90 minutes, not the paper's 150** — the assignment is homework completed alone Thursday–Saturday, and the full-length timed paper remains the **post-drive mock strand** (C5 Drive Plan §11.11 / direction D2); §3.12 does not authorise a mock. **§3.12(g) growth discipline:** added length must come from a newly unlocked question or from raising an existing question toward its Scholarship item count — repeating a covered skill in a fresh wrapper to fill pages is **barred**. **§3.12(h):** B3 Transformation and B5 Countability map to no 2026 question and sit in a separated **Revision** section that **closes at R7**; both remain live for the Performance Test and Mohammadpur-format practice. **§8 checklist** gains five C5 ticks and the no-marks tick is qualified to C1–C4. **Deliberately unchanged:** §3.3 held-vocabulary rule, §3.10 reading component, §3.11 FT drips until their unlock weeks, §5, §6 answer-key separation, §7 Coverage Log, the Charter §H guards, the delivered-block freeze, and every C1–C4 behaviour. |
| v1.3 | 2026-08-10 | **Class 5 Scholarship-style architecture (C5 only; C1–C4 behaviour unchanged).** New **§3.10 Reading component (C5)** — from the assignment of **13.08.26** every C5 assignment carries **one graded reading passage** with passage-based items: Phase A formats first (literal full-sentence answers at the 3-mark shape, lift-and-reshape, meaning-match, True/False, box-fill), progressing to Phase B (inferential/opinion, length-instruction obedience) as the 13.08.26 diagnostic and subsequent performance allow. Passages are **verbatim** from *English for Today* Class 5, §H-screened at selection, prioritising U2/U4/U7/U14/U19. New **§3.11 Fast-teach drips (C5)** — FT-1: two rearrangement items in every assignment from R5 (20–24.09.26) to the examinations; FT-2: form-fill/number revision items from R7 (4–8.10.26). **§3.1 ratio note (C5)**: the reading passage and FT drips are drawn from the **revision share**; grammar drip volume yields to the passage, never the reverse. **§3.5 length cap UNCHANGED** — the 40-minute working cap and baseline/deferral rules stand exactly as at v1.2; the passage does not license a longer paper. **§7.2 Coverage Log** gains two Block-Ledger-adjacent columns in the **C5 section only** — `Passage` (EfT unit + Phase A/B) and `Drip` (FT-1/FT-2 item counts) — so passage rotation and drip continuity survive across runs. **Individual student tracking is deliberately NOT added to the Coverage Log** (Principal ruling C-6, 10.08.26): per-student progress sheets are a separate artefact whose owner and template remain open. **One-off note:** the 13.08.26 assignment is accompanied by a short **ungraded reading diagnostic** (ruling C-5), delivered alongside but not part of the assignment and not logged as an assignment part. Source rulings: Principal 09–10.08.26; C5 Drive Plan v1.12 §7A. **Unchanged:** all ratios, the rotation engine, marks policy, answer-key separation, Special Instruction mechanism, C1–C4 behaviour, and the delivered-block rule — **no Part R or reading component is retrofitted into Blocks 1–7 material**. |
| v1.2 | 2026-07-21 | **Generalization + freeze.** Single-current-block model replaced by Current Set / Completed Set (§2.1 new; §1, §2 inputs, §3.1, §3.2, §4.1, §4.2.1, §7.2, §7.3.2 reworded). Algorithm now independent of block ordering, multi-block weeks, and multi-week blocks; single-block weeks reproduce v1.1 behaviour exactly (|C(N)| = 1 case). Ownership boundary set: Drive Plan §4 declares each week's Current Set (including consolidation-only); this spec owns behaviour, with consolidation weeks transferring the current-set share to revision. Current-set part order taken from the weekly prompt (block-ID-ascending fallback), not table layout. Bridges ruled non-rotation units folded into host blocks. Specification frozen; format-code registry (§3.9) remains the sole open integration item, pending Drive Plan review. |
