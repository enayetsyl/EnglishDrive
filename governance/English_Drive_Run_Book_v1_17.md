# English Skill-Building Drive — Run Book

**Canonical filename:** `English_Drive_Run_Book_v1_16.md`
**Document type:** Operating procedure manual (reconstructed).
**Companion documents:** `English_Drive_Project_Charter_v1_4` (policy — governing) · `English_Drive_System_Architecture_v1` (structure — read before using this Run Book).
**Status:** v1.17 — baseline, in active use.
**Date:** 2026-08-01

---

## 1. Purpose, Scope & How to Use This Document

The Run Book is the procedural layer of the project:
- the **Charter** states what is and isn't allowed (policy),
- the **System Architecture** document states what artefacts exist and how they connect (structure),
- this **Run Book** states the concrete steps for doing the next thing (procedure).

Where this Run Book states a procedure that conflicts with the Charter, the Charter wins. This Run Book only sequences and operationalises what the Charter permits.

**Audience.** Whoever builds the next file, with no assumed memory of prior sessions. Assume the reader has read nothing except this document, the Charter, the Architecture document, and whatever specific artefact they're about to work on.

**Scope.** This Run Book governs the English Skill-Building Drive only — File 1 (Drive Plans), File 2 (Vocabulary), File 3 (Grammar Blocks), and the Block-Build Specification. It does not govern the separate Project 00–03 ecosystem that the Skeleton, TG-Reconciliation, and Stability Report files belong to. Those are read-only build inputs.

---

## 2. Roles & Decision Authority

Four roles appear in the project: Principal, Content Developer, Teacher, Student.

### 2.1 The Principal — final decision authority

Rules on:
- Cap or scope widening beyond a Drive Plan's stated depth (Section 10.4).
- Timing of a flagged propagation — apply now or batch for later (Section 12.3–12.4).
- Worksheet-volume and structural revisions affecting delivered teacher workload.
- Exam-revision recommendations raised to the school (Section 10.6).
- Project-level operating-constraint changes.

### 2.2 The Content Developer — plans, builds, reviews, maintains

The surviving version logs identify the Content Developer as Claude. In this Run Book, however, the role is described generically as Content Developer, since the procedures are intended to be tool-independent.

Responsibilities:
- Authors and maintains Drive Plans, File 2, the Block-Build Specification, and Grammar Blocks (Sections 5–6).
- Runs the full build lifecycle — draft, volume pass, register pass, audits, answer-key verification (Section 6).
- Surfaces map-then-decide situations; does not resolve them (Sections 6.6, 10.4).
- Self-checks every quality gate (Section 8).
- Writes and closes propagation notes (Section 12).

### 2.3 The Teacher — classroom delivery

Runs the scripted classroom dialogue, distributes worksheets, gives daily Homework — the HW worksheet, introduced with a one-line task statement and one modelled item — checks Homework out of class with a khata comment, administers the weekly Performance Test, gives the Assignment, collects it the following Sunday, applies the retention gate, and keeps the Clue Card current on the wall (Section 9). Marks self-construction / free-thinking responses per Section 13.

No evidence a Teacher edits, requests changes to, or overrides any Drive artefact.

### 2.4 Student — retention-gate data source

Performance Test results, aggregated to a class average, set the following week's File 2 batch size through the retention gate (Section 9.8). Students are not decision-makers within the project, but their performance data directly influences weekly vocabulary pacing through this mechanism.

Parents have no formal role in the current assessment workflow (Section 9.6).

### 2.5 Decision-authority summary

| Decision type | Who decides |
|---|---|
| Cap/scope widening beyond a stated depth | Principal |
| Timing of a flagged propagation (now vs. batch) | Principal |
| Worksheet volume / structural revisions | Principal approves; Content Developer executes |
| Drafting, register sweeps, content audits | Content Developer |
| Weekly batch-size pacing | Mechanical — retention gate, no human decision |
| Project-level operating-constraint changes | Principal |
| Communicating an exam-revision recommendation to the school | Principal is the addressee; the delivery channel to the school itself is not defined here — confirm with the Principal case by case |

---

## 3. Project File Map & Naming Conventions

### 3.1 Core naming grammar

```
C{class}_ENG_{FileType}[TopicSuffix]_v{version}[_final].{md|xlsx|docx}
```

- `{class}` — `1`–`5`
- `{FileType}` — `DrivePlan`, `VocabPool`, `VocabBatchOrder`, `BlockBuildSpec`, `GrammarBlock`/`Block`, `Assignment`, `Skeleton`, `StabilityReport`, `TGReconciliation`
- `Assignment` files follow the accepted pattern `C{class}_ENG_Block{NN}_Assignment_v{version}.docx` (block number carried in the name; supersedes the earlier `Class_{n}_B{NN}_Assignment` pattern, which is retired for new files)
- Student-facing extract files follow their own compact pattern — see 3.12; they are the only artefacts exempt from this grammar
- `[TopicSuffix]` — File 3 only, e.g. `05_NounGender`; encodes both spine position and topic
- `{version}` — plain integer for File 3 (`v9`); dotted or underscore-dotted for File 1/Spec (`v1.4` / `v1_4`)
- `[_final]` — seen once in the corpus; treat as a one-off label, not a confirmed status convention

### 3.2 `GrammarBlock` vs. `Block`

Both forms exist in the surviving files with no documented rule distinguishing them. Use a single naming convention consistently going forward. Unless the Principal specifies otherwise, continue using the convention already adopted within the project to avoid introducing further inconsistency.

The per-class continuity observed in the corpus (C1–C3 `GrammarBlock`, C4–C5 `Block`) stands as the working convention. Unifying to a single form drive-wide remains an **open Principal ruling** — it was noted, not decided, at v1.3.

### 3.3 Filename version suffixes are not authoritative

Read the version from the file's own header line, never from the filename. Filenames occasionally carry suffixes (e.g. `v1__1_`) that do not match the version stated inside the file — these are filename artefacts, not authored version numbers.

### 3.4 File 2's two-artefact structure

Standard shape: a Pool workbook (`Master Pool` + `How to use` sheets) and a separate Batch Order workbook (`Weekly Plan`, `Word → Week`, `How it works` sheets).

If a class's Pool workbook also contains an internal Batch Order sheet, and it disagrees with the standalone Batch Order file, **the standalone file wins.** Correct or remove the internal sheet rather than leaving the two in contradiction.

### 3.5 Worksheet naming inside a block

Current convention: `CW-{class-number} | ক/খ/গ` and `HW-{class-number} | ক/খ/গ`, tied to the class-day the worksheet is given in. Mark notation follows the exam paper's own convention: `[n×m=total]`.

New blocks use this convention. These day-scoped labels are unique only *inside* one block file; the globally unique form of the same worksheet is its canonical artefact ID (3.11) — e.g. this block's `CW-2` is, project-wide, `C4B03-CW2`.

### 3.6 Build-input file naming

Build inputs (Skeleton, Stability Report, TG-Reconciliation) carry a `completed_` prefix, signalling they are finished deliverables from the separate Project 01 initiative — read-only, never edited here.

### 3.7 Self-declared canonical names

Recommended: state the file's own canonical filename in its header, as Project 01 artefacts already do. This gives an in-file collision check and is cheap to add. Not yet a required convention in File 1/2/3.

### 3.8 File location

All surviving files sit in a single flat project root. This reflects the platform the project was authored in and should not be interpreted as an architectural requirement.

### 3.9 Naming checklist before creating any new file

- ☐ Filename matches `C{class}_ENG_{FileType}[TopicSuffix]_v{version}.{ext}` exactly.
- ☐ `{FileType}` matches the convention already in use for this artefact type (3.2).
- ☐ Version in the filename matches the version stated in the file's own header (3.3).
- ☐ For a new File 2, build both the Pool workbook and the standalone Batch Order file (3.4).
- ☐ New worksheets use the `CW-N | ক/খ/গ` / `HW-N | ক/খ/গ` convention (3.5).
- ☐ Consider adding a self-declared canonical filename to the header (3.7).
- ☐ Confirm that the file's build-against references (Drive Plan version, Build Block Specification version, format mirror, exam anchors, and other dependencies) are correct before beginning work.
- ☐ New worksheets, Performance Tests, and Assignments carry their canonical artefact ID (3.11); extracts print it as the footer line (3.12).

### 3.10 Canonical terminology & retired aliases

*(Principal ruling, 2026-07-19 — supersedes the earlier "interchangeable terms" ruling for written use.)*

Fixed terminology for the recurring weekly artefacts. **Written project artefacts use only the canonical term.** Retired aliases remain acceptable in speech and in discussion, but must not appear in new or revised files. Existing files are corrected forward-only, each on its own next revision (Charter K.3) — do not open a file solely to rename.

| Canonical term | Code | Retired written aliases | Notes |
|---|---|---|---|
| Classwork worksheet | CW | "Worksheet CW" (unnumbered) | Always day-numbered: CW-1 … CW-4 |
| Homework worksheet | HW | — | Daily; see 9.2 |
| Performance Test | PT | Thursday test · weekly test · take-home test | "Take-home test" is also model-stale (Charter v1.2 §M.3) |
| Weekly Assignment | AS | — | Weekly, post-PT; see 9.2 |
| Self-try | ST | — | Short/student-facing form; "self-construction" remains the formal long form in governance text (Section 13) and is not retired |
| Clue Card | CC | — | — |
| Teacher Delivery Sheet | TD | — | Teacher-facing block projection; strip/keep per §3.13 |
| Teacher Answer Key | AK | "answer key" (per-worksheet form) | One consolidated key per block; assembled last, per §3.15 |

### 3.11 Canonical artefact IDs

Every recurring weekly artefact has a compact, globally unique, block-anchored ID:

```
C{class}B{block}[{half}]-{CODE}[{day}][-W{week}]
```

- `C{class}` — class 1–5. `B{block}` — two-digit block number (`B03`).
- `{CODE}` — from the 3.10 table: `CW`, `HW`, `PT`, `AS`, `ST`, `CC`, `TD`, `AK`.
- `AK` is block-scoped — no day or week suffix: `C4B04-AK`.
- `[{day}]` — class-day number, for day-scoped artefacts only (CW/HW): `C3B03-CW1`.
- `TD` is block-scoped — no day or week suffix: `C5B04-TD`.
- `[-W{week}]` — only for 2-week blocks with one PT per week: `C2B05-PT-W1`, `C2B05-PT-W2`.
- `[{half}]` — optional lowercase `a`/`b` on the **block token**, for a **two-week split-block authored as two master files** (§6.7): `C2B06a-CW1`, `C2B06b-PT`. The half-letter qualifies the block; it does **not** create a new block — `C2B06a` and `C2B06b` both anchor to **block 06**. Use **either** the half-qualifier (two-master build) **or** the `-W{week}` PT suffix (single-master build), never both for the same block. Block-scoped extracts (TD, CC, AK) take the half-letter only if authored per-half (`C2B06a-TD`); a block with one shared TD/CC/AK omits it.
- Item level, when a single item must be referenced: append section letter + item number — `C4B03-CW2-B7` (in extracts, sections are lettered A/B/C; masters using ক/খ/গ map ক=A, খ=B, গ=C).

**Anchor is the block, not the week** (Principal ruling, 2026-07-19): block numbers survive schedule shifts — inserted blocks, early partial entry, and 2-week stretches all move week numbers but not block identity. A two-week block's `a`/`b` half-qualifier likewise does not change block identity: both halves are the same spine block.

IDs appear: in the master block file wherever the artefact is defined, as the footer line of every extract (3.12), and in propagation notes and cross-file references.

### 3.12 Student-facing extract files

Extracts are print-ready student sheets **derived from a master block file** — one `.md` per CW day, per HW day, and per PT. Filenames use the compact ID form, not the 3.1 grammar:

```
C3B03_CW1.md · C3B03_HW1.md · C5B02_PT.md · C2B05_PT_W1.md
```

Governing rules (full generation procedure: 6.9):

1. **The block file is the single master.** Extracts carry no version log and are never edited directly. To change a worksheet or test: edit the master, bump its version, regenerate the extract. A direct edit to an extract is invalid and is overwritten at the next regeneration.
2. **Answer keys and PT dictation word lists never appear in extracts** — they stay in the master (teacher copy) only. A PT extract is the *student-facing half* of the test: dictation prints as numbered blank lines with a listen-and-write instruction.
3. **Template (locked 2026-07-19):** school header (`SCHOOL FOR COMMUNITY DEVELOPMENT` / `Class {n} - English Grammar Campaign` / `Block {NN}: {Topic} ({Classwork|Homework} — Day {d})` or `({Performance Test})`); `Name-` and `Date-` on one line, date left blank; all instructions and section labels in **English** (`Part A/B/C`, Arabic numerals, marks as `[n]`); item content copied verbatim from the master — English instructions do not license editing items; **pure markdown, no HTML tags** (the viewer renders them literally); the canonical ID as an italic footer line.
4. **Marks are printed on PT extracts** (exam-mirroring). The assignment-era "no marks on student paper" style applies to Assignments, not PTs.
5. **Answer space:** short answers are written on the sheet (inline blanks); extended responses (e.g. self-try sentences beyond the printed lines) go on supplementary paper — extracts do not carry large blank blocks.
6. **Print path is `.md` → `.docx`.** The `.md` extract is the clean intermediate; centering and final layout are applied at the docx stage. Left-aligned headers in the raw `.md` are expected, not a defect.

### 3.13 Teacher Delivery Sheet (extract)

| Strip (Developer/Principal-only) | Keep (teacher needs in class) |
|---|---|
| Provenance / build header block | Block title + week/days it runs |
| Dependency flags, consistency-check notes, blast-radius / version-drift notes | Learning outcomes, plain form |
| Version log | The teaching script (English — §3.14) |
| Held-word source citations & batch traceability | Board work / worked examples |
| **Answer keys** (already master-only, §3.12 r.2) | Grammar explanation as taught |
| Bloom / rubric **traceability mapping** (the audit trail) | Clue Card content |
| Charter / Drive Plan §-references | Self-try / free-thinking **task prompt** |
| CW/HW/PT **item content** (lives in its own extract) | Self-try / free-thinking **rubric** (teacher administers it) |
| | **PT instructions** — the student-facing test procedure, *not* the key or dictation list |
| | Pointers to sibling extracts (e.g. "CW1 is on its own sheet"), as pointers only |

Two boundary rulings (Principal, 2026-07-21): the teacher **does** receive the free-thinking **rubric** (they mark it) but not its charter-traceability; and the teacher **does** see **PT instructions** (they run the oral test) but never the key or dictation word list.

---

### 3.14 Language of delivery (implementation standard)

**Default instructional language is English**, across every artefact the drive produces.

1. **Teacher scripts are written in English**, and classroom delivery is in English.
2. **All instructions are in English** — classroom instructions, CW, HW, Performance Test, Assignment, worksheet directions, Clue Card directions, dictation instructions, and teacher notes.
3. **Bangla appears only where it is the learning content itself**, not as the medium of instruction. Legitimate uses:
   - Bangla meanings of vocabulary
   - English↔Bangla translation activities
   - Matching English words with Bangla meanings
   - Items where Bangla is intentionally part of the task or the required answer
4. **Optional Bangla support.** Where Bangla genuinely aids comprehension of a difficult concept, the **main teacher script stays in English** and the Bangla explanation is **explicitly marked as an optional teacher note** — never woven into default delivery.

This standard is **project-wide**. Drive Plans inherit it and do not restate it (§B.1 build-against chain); a Drive Plan that carries its own delivery-language convention is superseded by this section.

**Retrofit is forward-only (Charter §K.3).** Blocks already finalized under the previous Bangla-led convention are not reopened for language alone; they convert at their own next revision. A block being revised for any reason converts its script and instructions as part of that revision.

The block master file serves two audiences with conflicting needs. The **Content Developer and Principal** need the full provenance header, dependency flags, consistency checks, version log, held-word sourcing, answer keys, and Bloom/rubric traceability — build-integrity metadata. The **classroom teacher** needs only the teaching script, board work, delivery sequence, and target examples. Printing the master hands the teacher a document where a large share of the content is invisible to their job and risks answer keys or governance notes being misread as classroom instructions.

The **Teacher Delivery Sheet (TD)** is the teacher-facing projection of a master block — one `.md` per block. Like all extracts, it is **derived, unversioned, and regenerate-only**: the master is the single editable source (§3.12 rule 1 applies in full). Filename uses the compact ID form:

```
C5B04_TD.md
```

**Strip / keep manifest (locked):**

---

### 3.15 Teacher Answer Key (extract)

The **Teacher Answer Key (AK)** is a single consolidated key covering every graded artefact in a block. Answer keys are **not** printed after each worksheet in the master; they are assembled into one document once all worksheets are final.

**Rationale.** A teacher marking a week's work needs one document, not ten scattered key sections. Consolidation also makes the numbering audit possible: every item in every worksheet is checked against exactly one answer in one pass.

Like all extracts, the AK is **derived, unversioned and regenerate-only** — the master block file remains the single editable source (§3.12 r.1). Filename uses the compact ID form:

```
C4B04_AK.md
```

**Contents and order (fixed):**

```
CW1 · HW1 · CW2 · HW2 · CW3 · HW3 · CW4 · HW4 · PT · Assignment
```

1. **Original numbering is preserved exactly.** Item 29 in the key is item 29 on the worksheet. Numbering never restarts or re-flows inside the key.
2. **Answers only.** The key carries the correct answer per item, not the question text. Brief marking notes appear only where an item genuinely needs one — model answers for open production, accept-either rulings, or a mark split. Reproducing questions would make the key a second copy of the worksheets and defeat its purpose.
3. **Dictation word lists live here**, with the PT, since they are teacher-only (§3.12 r.2) and never appear on the student sheet.
4. **Never issued to students**, and never merged into a student extract or the Teacher Delivery Sheet.

**Ordering constraint.** The AK is assembled **after** every worksheet is final, never alongside them. A key written next to a worksheet still under revision goes stale silently.


---

### 3.16 Vocabulary Writing (HW worksheets)

Every HW worksheet ends with a **Vocabulary Writing** section (ruled **PD-015**; forward-only).

1. **Words.** 5–6 words drawn from the class's own File 2 (Vocabulary Pool + Batch Order), from the block's **released-week batch** under the cumulative-release model. Distinct sets across the HWs of a multi-HW block (no word repeated between them). Each class uses its own pool/batch; no cross-class sharing.
2. **Format.** A boxed English **Word Bank** listing the words once, then a **blank two-column table** — *English Word* | *বাংলা অর্থ* — one row per word, no prefilled cells. The student copies the English word into column 1 and writes its Bangla meaning in column 2; **both columns are student-written**.
3. **Marking.** Unmarked practice, teacher-checked for spelling and meaning; **excluded from the HW mark total**.
4. **Placement.** The final section of the HW, after all marked parts.
5. **Scope.** Classes 1–5 uniformly. The student-produced Bangla is **learning content**, consistent with §3.14 (Bangla as learning content, not worksheet instruction); worksheet instructions remain English-only. **Forward-only** (Charter §K.3): delivered/frozen HWs are not retrofitted.

---

### 3.17 Worksheet reference blocks (the rule box)

A **reference block** is the boxed panel a worksheet may carry above its items — headed *"The rule"*, *"Remember"*, or similar — restating what the sheet practises. It is optional; where present it is governed by **PD-018**.

1. **What it may contain.** A **rule**, stated as a method the student applies. An **arbitrary learned list** — a closed set the student can only memorise because no taught rule derives it (river names, country names taking *the*, irregular plurals, fixed collocations).
2. **What it may not contain.** A **worked example of a derivable word the sheet grades**. If the taught method produces the answer, printing that answer removes the thinking the item tests.
3. **The distinction is derivability, not word class.** *An hour* is derivable — say the word, hear the vowel, apply the rule — so printing it above an item grading *hour* is an answer key. *The Padma* is not derivable from anything taught; withholding it tests days-old recall rather than reasoning, which is a different assessment from the one the block is running.
4. **Audit (see §6.5).** Compare every reference block against its own sheet's answer key, **normalising punctuation on both sides** — box text and item targets. A comma, emphasis marker, or trailing full stop between an article and its noun is enough to defeat a naive string match; a first audit pass on the block that produced this rule reported a sheet clean that was in fact leaking seven answers.
5. **Scope.** Student-facing worksheets of every type — CW, HW, Performance Test, Assignment — across Classes 1–5. **Clue Cards and other wall references are exempt**: they are not sat with the paper, and their function is precisely to hold the taught rule in front of the class.
6. **A block may vary the convention across its own sheets**, provided each sheet complies — for example, a method line on the single-rule days and no block at all on the integration days, where a reminder would be either useless or a crib. State the pattern in the block file so it reads as design rather than drift.

**Forward-only** (Charter §K.3): delivered worksheets are not retrofitted.

---

## 4. Build Order & Dependencies

### 4.1 Mandatory build sequence

1. **Build inputs** (Skeleton, TG-Reconciliation, Stability Report) — read-only.
2. **Drive Plan (File 1)** — depends on build inputs + binding exam papers.
3. **Vocabulary Pool + Batch Order (File 2)** — depends on the Drive Plan's §2 spine and §5 reuse-base logic. Do not begin File 3 without a completed File 2.
4. **Block-Build Specification** — depends on a validated first block. If the class has none, use Section 4.3.
5. **Grammar Blocks (File 3)** — depends on all of the above, plus the previous block in sequence (Section 4.2).

### 4.2 Format-mirror rule

Every new block cites the most recently validated block. Identify:
- the newest validated block in this class, and
- if this class's sequence is short or just starting, the newest validated block in Class 3 (the reference class).

Cite both in the new block's header if both apply.

### 4.3 Missing or outdated Block-Build Specification

If a class-specific Block-Build Specification is unavailable or outdated, continue using the following references instead:
- this class's own Drive Plan (§2/§4/§5/§7/§8/§9),
- Class 3's Block-Build Specification for document shape and scripting conventions,
- the most recently validated block in Class 3 as the worked example.

### 4.4 Dependency quick-reference

| Building… | Hard dependencies | Soft references |
|---|---|---|
| Drive Plan | Build inputs, binding exam papers | — |
| File 2 (Pool + Batch Order) | Drive Plan §2, §5 | — |
| Block-Build Specification | One validated block in this class | — |
| Grammar Block | Drive Plan, File 2, binding exam papers, format-mirror block | This class's Specification (else Class 3's) |

### 4.5 Pre-build checklist

- ☐ All required dependencies exist and are the current version (re-check, don't rely on memory).
- ☐ Confirm that all required dependencies are available and that no unresolved Principal decision is still pending (for example, scope changes, curriculum placement, or exam-mapping rulings). If a required decision is still pending, pause the build until it is resolved.

---

## 5. File 2 Build Procedure (Vocabulary Pool + Batch Order)

### 5.1 Purpose

File 2 guarantees every graded item in File 3 uses a word the student has already been taught.

### 5.2 Build the Pool workbook

1. Extract candidate words from the class's NCTB book, unit by unit, in book order.
2. Deduplicate — hold a recurring word once, under the unit that teaches it first.
3. Identify every grammar role the word can legitimately take within the project's teaching scope, and record both the primary role and any additional roles where required.
4. Curation-screen at source. Exclude anything the Curation Policy rules out before it enters the pool. Log what was excluded and why in the Pool's "How to use" sheet.
5. Assign each word a `Home Grammar Block`, and an `Also Feeds` note where it's reused downstream.
6. Build the Pool once. Weekly batches are drawn from this fixed pool, not rebuilt alongside it.
7. Write the "How to use" sheet: total word count, POS breakdown, source edition, exclusions and rationale, POS→block mapping rule.

### 5.3 Build the Batch Order workbook

1. Solve the lead-time constraint — every word is released at least one full week before its `Home Grammar Block` is taught, with more margin for word-heavy blocks (e.g. Verb).
2. Front-load by POS — nouns first, then adjectives, then verbs and adverbs, so vocabulary is no longer new by the time grammar gets heavy.
3. Set batch sizes as a planned progression. The Batch Order defines the intended sequence; any week-to-week adjustments are made according to the retention-gate procedure described in Section 9.8, not by editing the underlying planning logic.
4. Stop releasing new words once the pool clears. Remaining weeks are consolidation and spaced revision only.
5. Write the "How it works" sheet: pool size and source file, ramp logic, fresh-window cutoff week, POS lead-time rule.

### 5.4 Special word categories

For words a binding exam tests that the book doesn't supply, use one of:
- an exam-back-mapped column (traces a word to the specific exam item it answers), or
- a tagged import set (words added directly, tagged by source rather than unit).

Either way, the word still gets a `Home Grammar Block`, still passes curation screening, and still respects the lead-time rule.

### 5.5 Validation before finalizing

- ☐ Every word in the Batch Order exists in the Pool, and vice versa.
- ☐ POS counts in the Pool's "How to use" sheet match an actual count of the Pool sheet.
- ☐ Every POS group's last-batched word lands at least one week before that POS's grammar block.
- ☐ Batch sizes across all weeks sum to the stated pool total.
- ☐ If a standalone Batch Order file and an internal Batch Order sheet both exist, confirm they agree — if not, the standalone file wins (Section 3.4).

### 5.6 After finalizing

Treat the Pool as a stable planning artefact. Changes should only be made through a documented versioned revision following a Principal decision or an approved exam-mapping update. Do not re-tag or resequence the Pool for routine use. Where a fix could apply to another class's Pool, log a propagation note (Section 12).

### 5.7 Grammar Exemplars (not vocabulary)

*(Governance source: **PD-009**, Curriculum Design Decision Log — project-wide.)*

Some grammar rules can only be demonstrated with specific words. The Article block's sound exceptions are the clearest case: *an hour* cannot be taught without *hour*. These words are **Grammar Exemplars** — they exist to demonstrate a rule, not to build lexical knowledge — and they are **exempt from the held-vocabulary rule** (Rule 1 / §5.1).

**What qualifies.** A word qualifies only if all three hold:
1. Its presence is required by the block's Drive Plan §2 cap or by a binding exam anchor (§10.1).
2. The graded skill is the grammar rule, not the word's meaning.
3. It belongs to a **closed, fixed set** — not an open class the builder can extend at need.

If a word is merely convenient, or makes a nicer sentence, it is **not** an exemplar. Use a held word instead. Where an item shape from a binding paper uses an ordinary word that happens to be unheld, rebuild the shape on a held word rather than admitting the word as an exemplar — the exemplar list covers the *exceptions*, not everything the paper happens to print.

**How to implement.**
- **Teach them explicitly.** Exemplars are never assumed known. They appear in the Lesson Plan, in teacher modelling, on the Clue Card, and in guided practice before any graded use.
- **Use them freely where required.** They may appear in CW, HW, PT and Assignment, including as the graded answer.
- **Never treat them as vocabulary.** Not added to the Pool or Batch Order; not counted in any fresh or held batch size; not vocabulary-learning targets; **never dictation or spelling items** (§9.6). A student is never graded on their meaning or spelling.
- **Keep the list fixed and minimal**, and keep it stable across the project — the same rule draws on the same exemplars in every class that teaches it, at that class's cap.
- **Curation still applies in full** — Charter §H.9 screening and the §H.3 sacred-word guard bind exemplars exactly as they bind pool words.

**Record them.** The block file's header states its exemplar list, each item traced to its cap or exam anchor. The list is part of the block's build record, not an inline aside.

**This does not amend File 2.** Pools and Batch Orders are untouched by an exemplar decision (§5.6 still governs Pool changes). The exemption is a carve-out in the *audit*, not a change to what the Pool holds — consistent with the Pool already excluding function words at source as grammar targets.

### 5.8 Block-local teaching words (taught-but-not-pooled)

*(Governance source: **PD-012**, Curriculum Design Decision Log — project-wide.)*

Some binding papers test a concept the held pool cannot establish at all — not a single exception word, but a whole category. The clearest cases: the **-es** plural rule when no held noun ends in s/sh/ch/x, and the four gender categories when the pool holds only a fragment of the counterpart pairs. Here a class may teach the required items **in-block without entering them in File 2**. These are **Block-local teaching words**, a word-status distinct from both held vocabulary and Grammar Exemplars.

**What qualifies.** A word qualifies only if all three hold:
1. Its presence is required to complete a concept the block's Drive Plan §2 cap or a binding exam anchor (§10.1) tests, and the held pool cannot supply that concept.
2. It is sourced from the binding papers, not reached for as a convenience.
3. It is genuinely a taught item that week — meaning, reading, and use are taught before any graded use.

**Status of a block-local word.**
- **Gradeable within its own block only** — it may appear in that block's CW, HW and PT, including as a graded answer. Fairness holds locally: nothing is graded that was not taught this week.
- **Never a dictation or spelling item** (§9.6) — it is not a File 2 pool word, so the PT dictation draws on the held pool only.
- **Not held downstream** — later blocks do not treat it as held vocabulary.
- **Not in the spaced-revision cycle** (e.g. the W8–W12 window).

**How this differs from the two neighbouring statuses:**
- *vs Grammar Exemplars (§5.7):* an exemplar demonstrates a *rule* and is never a vocabulary-learning target; a block-local word **is** a taught noun/word for the week (the child learns its meaning), but its "held" status is confined to the block. Both stay out of File 2.
- *vs Override words (§5.9):* an override word is counted toward the week's taught-vocabulary load and **is** spelling/dictation-eligible that week; a block-local word is neither — it is gradeable only inside its own block and never a spelling/dictation item.

**Record them.** The block header states its block-local set, each item traced to the concept and paper it completes, with the four status lines above stated explicitly.

**Audit treatment.** The held-word audit (§6.5) passes a graded answer that traces to a held word, a declared Grammar Exemplar, **or a declared block-local word** — anything outside all three sets fails. The §6.8 checklist verifies the block-local set is declared and traced, every block-local word is taught before graded use, none appears as a dictation or spelling item, and none is reused as held in a later block.

**This does not amend File 2.** Pools and Batch Orders are untouched; forward-only File 2 reconciliation (if any) is flagged, not applied from the block.

> **Choosing between §5.7, §5.8 and §5.9 (PD-020).** The instrument follows **what the word is for**, not convenience. Sole purpose is to demonstrate a rule, and the child never needs to own the word → **Grammar Exemplar (§5.7)**, *not counted* toward the week's load. A genuine taught word for the week whose held status is confined to the block → **block-local (§5.8)**, *counted*. Real taught vocabulary, spelling- and dictation-eligible → **override (§5.9)**, *counted*. **Load is a decision input, not an afterthought:** where a candidate passes the exemplar test, §5.8 must not be used in its place, because block-local status adds the word to the week's taught load and can trip the retention gate (§9.8) on a vocabulary count rather than on mastery of the block's actual skill. **Rebuild before widening:** where a binding paper's item is built on an ordinary unheld word, rebuild the item shape on held words rather than admitting the word or widening the §2 cap — the operative reading of §5.7's anti-drift line.

### 5.9 Override words (exam-anchored common vocabulary)

*(Governance source: **PD-011**, Curriculum Design Decision Log — project-wide.)*

Where a binding paper anchors **common, age-appropriate vocabulary** that the held pool cannot supply, and those words are ordinary lexical items a child should genuinely learn (not rule-demonstration exemplars), they may be admitted to a block as **Override words**. Unlike block-local words, override words **are counted toward the week's taught-vocabulary load** and **are spelling/dictation-eligible from the day they are taught** — they behave as real taught vocabulary for the week.

**What qualifies.** Common, age-appropriate, exam-anchored vocabulary that the held pool cannot supply. This is **not** a licence for unrestricted vocabulary expansion; it is confined to words a binding paper anchors and the pool lacks.

**How to implement.** Taught explicitly (meaning, pronunciation, reading, spelling); staged across the week; counted toward that week's taught-vocabulary load; used in graded items only after teaching. Curation (§H.9) and the sacred-word guard (§H.3) apply in full.

**File 2.** The override is a build-time admission; File 2 is not amended from the block. Reconciliation to File 2 (reflecting the override words as that week's taught vocabulary) is flagged forward-only.

---

## 6. File 3 Build Procedure — the Per-Block Lifecycle

### 6.1 Before starting

Confirm the Section 4.5 checklist is complete. Identify this block's Drive Plan §2 cap, its §7 exam anchor(s) across all binding papers (Section 10), its File 2 held-word scope, its book anchor, and its format-mirror block.

### 6.2 Stage 1 — Initial build

Draft the block against the standard skeleton (Section 3, Spec §2): Block-at-a-glance → checklist → Clue Card → Class-by-class script → Performance Test → Assignment → Bloom ladder → answer keys → self-try rubric → version log. Answer keys are held in the master but are **not** printed after each individual worksheet; they are consolidated into the block's Teacher Answer Key once every worksheet is final (§3.15, §6.11).

Build outputs for the week include the Classwork and Homework worksheets (Section 6.3), the Performance Test, and the Assignment (Section 9.7), plus their student-facing extracts (Section 6.9). Each teaching day's script carries its Exit Check prompt set (Section 9.4).

In the header, state explicitly: topic and §2 cap · exam anchor(s) and their source papers · book anchor · Drive Plan version · Build Block Specification version (or reference specification) · format-mirror reference · held-word scope · relevant values guards · worksheet-size target.

Every graded item must use only File 2 words already held by this block's week. Anything outside that scope is gloss-marked as unheld and excluded from grading.

Self-construction / free-thinking questions follow the question-design guidance in Section 13.2.

Write the version log's `v1` entry summarizing all of the above.

### 6.3 Stage 2 — Volume pass

Bring worksheets to full size (target: two worksheets per class — Classwork and Homework — sized to the project's standard formula, or the appropriate variant for a paired/2-day block). Regenerate and verify every answer key against the expanded item set. Log the change.

### 6.4 Stage 3 — Register and consistency pass

Check wording against established project register. Where a register choice has already been fixed in an earlier block, match it. Log any changes made.

### 6.5 Stage 4 — Named content audits

Run and name each of the following before treating a block as finished:
- **Tense audit** — no ungraded tense forms leak ahead of where the spine introduces them.
- **Held-word audit** — every graded answer traces to a word this week's batch holds, **or to a declared Grammar Exemplar** (§5.7, PD-009). Exemplars are listed and justified in the block header; anything outside both sets fails the audit.
- **Reference-block audit** — for every worksheet carrying a rule box (§3.17, PD-018), compare the box text against that sheet's own answer key and confirm it prints no worked example of a **derivable** word the sheet grades. **Normalise punctuation on both sides before matching** — box text and item targets — or comma- and emphasis-separated pairs pass a naive comparison undetected. An arbitrary learned list is permitted and does not fail the audit.
- **Values audit** — sacred-word guard, non-mahram pairing screen, no music/festival content, house-style names/greetings. *Festival contexts are admissible where the referent is Islamic (Eid, Ramadan) and excluded for other-faith festivals — the exclusion attaches to the referent, not the word (PD-021).*
- **Attribution audit** — no authored sentence presents a natural phenomenon as acting on its own. Where agency appears it is **attributed in place** — *"the sun gives us light by Allah's Will"* — rather than restructured to move Allah into the subject position (**PD-019**); plain description without agency is equally acceptable. Attribution is a values matter in student work: corrected, never marked down as a language error (§13.1).
- **Do-not-repeat audit** — scan prior blocks in this class for reused names, sentences, or scenarios.
- **Paired-sheet duplication audit** — for each teaching day, compare the answer sequence of that day's **CW against its HW** position by position. Positional overlap must be **≤35%**. A CW and HW that share an answer order let a student complete the homework by copying the classwork column without reading a single item, which defeats the independent-practice purpose of HW (§9.2 r.1) and is the same exploitable pattern PD-008 bars *within* an exercise. The failure mode is a build habit, not an accident: an HW assembled by trimming or lightly editing its CW bank inherits that bank's order. Shuffle the HW independently and re-verify — item content may legitimately overlap between CW and HW (the week's practice is deliberately repetitive); the **answer order** may not. Run the same comparison against the PT where a PT part reuses a worksheet's item shape.
- **Rehearsal/graded disjointness audit** — where a graded task rehearses an ungraded one — a demo Self-try and its Performance Test counterpart, a practice set and its test version, a modelled example and the item that assesses the same skill — the **prompt sets must be disjoint**. A student who drafted an answer in rehearsal must not be able to reproduce it verbatim under assessment; that converts independent production into recall of yesterday's sentence and defeats the reason the rehearsal and the graded task were separated. **Item-type coverage should match** — the graded set must still reach every category the rehearsal covered, so the assessment is no harder or narrower — but the specific words, pairs, names, or prompts must not repeat. Check word boxes, prompt lists, and self-try stimulus sets in particular; these are the artefacts most often produced by lightly editing their rehearsal counterpart. Precedent: the C3/C4 Block 3 Performance Test already required redistributing self-try pairs so no student received their own earlier pair back.
- **Item-text duplication audit** — compare graded items by **sentence text**, not only by answer: each day's **HW against its CW**, and the **Performance Test against every worksheet in the block**. Verbatim repetition is not practice — a student who meets the same sentence twice transcribes an answer they have already produced instead of applying the rule again, and a PT built from worksheet sentences measures recall of those sentences rather than independent production (§9.2 r.3). **The rule is: re-test the same rule on different sentences.** Content overlap is expected and welcome — the same trigger word, the same article, the same reason may recur freely — but the sentence frame must change. Thresholds: **HW ≤2 items** identical to its CW; **PT: zero** items identical to any worksheet. This audit is distinct from the paired-sheet audit above: a sheet can pass answer-order overlap while being half a literal copy, because reordering copied items changes the sequence without changing the text.

### 6.6 Stage 5 — Principal ruling entries and finalization

If Stages 1–4 surfaced a cap, scope, or conflict question — a map-then-decide situation (Section 10.4) — do not resolve it. State the conflict and options in the version log, flag it for the Principal, and pause that item. Once ruled on, log the ruling, its reasoning, and any propagation note for other classes (Section 12).

Only once all Stage 1–4 items are resolved and any Stage 5 rulings are logged is the block finalized.

### 6.7 Shape variants

- **Paired-week block:** each half runs 2 classes instead of 4; the two share one Thursday-slot assessment, assembled in the second block's file; the first block's file notes the join.
- **Two-week block (8-day, PT per week):** a single spine block allotted two weeks runs **4+4 class-days across two teaching weeks**, each week a self-contained half with **its own Thursday Performance Test** and its own fresh vocabulary batch, and a marked **seam** between halves. Author it **either** as one master with `-W1`/`-W2` PT extracts, **or** — where the two weeks carry distinct grammar and benefit from separate audit surfaces — as **two master files with an `a`/`b` block-half qualifier** (§7): `C{class}B{NN}a_…`, `C{class}B{NN}b_…`. Both halves anchor to the same block number. The first-half master notes the seam and the forward carry of held vocabulary into the second half. Distinct from the *paired-week block* above, which runs 2+2 and shares **one** assessment.
- **2-day block:** worksheets numbered by class-day (`CW-1`, `CW-2`...).
- **Composition / open-production block:** the worksheet-size formula doesn't apply — state this as a declared deviation; substitute model answers for programmatic answer keys.
- **First-teach vs. re-walk framing:** if this class has no prior Drive-taught cohort, Block 1 teaches word-classes from zero rather than re-walking prior exposure. State which framing applies in the header.

All variants still pass through Stages 1–5.

### 6.8 Pre-finalization checklist

- ☐ Section order matches the standard skeleton (or a stated variant).
- ☐ Depth taught only to the Drive Plan §2 cap; lower rungs re-walked first.
- ☐ Graded items use only held words **or declared Grammar Exemplars** (§5.7, PD-009); other unheld items gloss-marked, never graded.
- ☐ If the block uses Grammar Exemplars: the list is stated in the header with each item traced to its §2 cap or exam anchor, every exemplar is explicitly taught before graded use, and none appears as a dictation or spelling item.
- ☐ Practice format mirrors the exam anchor(s) from Section 10's combined-paper map.
- ☐ Bloom ladder climbs within the block, within this class's band.
- ☐ Dual-job (if applicable) follows the value-positive, base/imperative-verb rule.
- ☐ Every worksheet's answer key is verified against its actual item set.
- ☐ Any worksheet reference block complies with §3.17 — rule and arbitrary learned list permitted; **no worked example of a derivable word the sheet grades**; audit run with punctuation normalised on both sides.
- ☐ Attribution form follows PD-019 wherever a natural phenomenon acts.
- ☐ Self-try / free-thinking task present, on the class's standard rubric.
- ☐ Every teaching day carries an Exit Check set aligned to that day's objective, with one prompt per student at this class's size (§9.4).
- ☐ The Performance Test and weekly Assignment are included, and the Assignment aligns with this week's grammar objective(s), held vocabulary, and exam-style practice (Section 9.7).
- ☐ All seven named audits (6.5) completed and logged, including the paired-sheet duplication audit (CW↔HW positional overlap ≤35%), the rehearsal/graded disjointness audit (no shared prompts between a demo task and its graded counterpart), and the item-text duplication audit (HW ≤2 items identical to its CW; **zero** PT items identical to any worksheet).
- ☐ Version log is complete, with every stage's changes recorded and any Principal rulings attributed.
- ☐ Confirm that any required updates to downstream artefacts (other blocks, Drive Plans, File 2, Build Block Specification, or documentation) have been identified and recorded as propagation notes before finalizing (Section 12).
- ☐ Student-facing extracts generated (or regenerated, if a revision touched any worksheet or the PT) and machine-checked against the master (Section 6.9).
- ☐ Teacher Answer Key assembled after all worksheets were final, in the §3.15 order, and its consistency check passed (Section 6.11).
- ☐ Teacher Delivery Sheet generated/regenerated per Section 6.10 if taught content, the Clue Card, the free-thinking task/rubric, or PT instructions changed.

### 6.9 Stage 6 — Extract generation

Run after finalization, and again after any later revision that touches a worksheet or the PT.

1. **Generate** one extract per CW day, per HW day, and per PT, per the 3.12 template and filename pattern.
2. **PT precondition:** a PT extract may only be generated from a master already on the in-school Performance Test model (Charter v1.2 §M.3). If the master's test section still describes the take-home / parent-assisted model, or contributes only part of a joint test, **stop** — the master must be converted (its own version bump) before its PT extract exists. Generating from a stale section would carry the retired model into print.
3. **Machine consistency check** — required, not eyeballed. Because an extract may reword instruction lines (and, for pre-§3.14 masters, translate them to English), the check compares **items and structure, not raw text**: item counts per section, item content strings, section order, and mark totals must match the master exactly. Instruction lines are excluded from the diff.
4. **Retrofit is forward-only** (Charter K.3): new blocks ship with extracts; existing finalized blocks gain theirs on their own next revision, or on demand when the Teacher needs a specific sheet.
5. **In-item Bangla hints — resolved by §3.14.** Scaffolding inside item text (e.g. HW fill-in hints) is **instructional support, not learning content**, so it is written in English like every other instruction. Bangla remains only where the item's *task* is Bangla — a required Bangla meaning, a translation item, or an English↔Bangla match. Where a Class 1–2 item genuinely needs Bangla to be attemptable, the Bangla is an **explicitly marked optional teacher note** (§3.14 r.4), not default item text.

Extract generation completes the finalization gate for the block; the Content Developer owns it end-to-end (Section 8.4).

### 6.10 Stage 7 — Teacher Delivery Sheet generation

Run after §6.9, and again after any revision that touches taught content, the Clue Card, the free-thinking task/rubric, or PT instructions.

1. **Generate** one TD per block, applying the §3.13 strip/keep manifest against the finalized master.
2. **Derived, not edited:** the TD carries no version log and is never edited directly (§3.12 r.1). A change to teaching content is made in the master, then the TD regenerates. A direct edit to a TD is invalid and is overwritten at the next regeneration.
3. **No graded-content leak:** the TD carries no answer keys, no dictation word lists, and no CW/HW/PT item content — only pointers to those sibling extracts.
4. **Consistency check:** confirm every kept section reproduces the master verbatim and every stripped category is absent. The TD reproduces the master's script as written; under §3.14 that script is in English, so no translation step arises (for pre-§3.14 masters not yet converted, the TD still reproduces verbatim — it is not the place to convert language).
5. **Retrofit is forward-only** (Charter K.3): new blocks ship with a TD; existing finalized blocks gain theirs on their next revision or on teacher demand.


### 6.11 Stage 8 — Teacher Answer Key generation

Run after §6.9, once **every** worksheet, the Performance Test and the Assignment are final. Re-run after any revision that changes an item, an answer, or a mark value.

1. **Assemble one AK per block** in the fixed §3.15 order, preserving each artefact's original item numbering.
2. **Answers only** — no question text, brief marking notes only where an item requires one.
3. **Consistency check — required, and programmatic, not eyeballed.** Before delivery, verify that:
   - every graded item in every worksheet has **exactly one** corresponding answer in the AK;
   - no answer in the AK refers to an item number that does not exist;
   - item numbering is continuous and non-duplicated within each artefact;
   - per-artefact mark totals computed from the AK match the totals printed on the worksheets.
   A mismatch blocks delivery (§8.2) — fix the master, regenerate, re-run.
4. **Never merged into a student extract or the TD** (§3.12 r.2, §3.13).


---

## 7. Project Handover & New Build Session

### 7.1 Assume a cold start

Treat every session as if no prior context survives. Continuity lives in the files, not in memory of a previous session.

### 7.2 Identify the session type

- **Continuing session** — relevant Drive Plan, Spec, and prior block already confirmed current in this session. Skip to 7.4.
- **New task, known project** — do the orientation pass (7.3) before drafting.
- **Full cold start** — do the full orientation pass (7.3); treat every version citation as unverified until re-read.

### 7.3 Orientation checklist

Read, in order:

1. The Charter — current version, in full.
2. This Run Book and the System Architecture reference.
3. The class's Drive Plan — current version, in full.
4. The class's File 2 (Pool + Batch Order) — confirm current.
5. All binding exam papers for this class (Section 10) — not just the most recent one.
6. The Block-Build Specification this build will follow (this class's, or Class 3's per Section 4.3).
7. The format-mirror block(s) this build will cite.

Do not rely on a prior session's citations of these versions — re-open and re-check each one.

### 7.4 Confirm scope before drafting

State and get confirmation on:
- What is being built (which file, which block/section).
- Output format (standing default: a single `.md` file; confirm if this differs).
- Confirm the expected review workflow (draft for review first, or prepare the final deliverable directly).

### 7.5 Session discipline

- One unit of work at a time. Finish and pause for review before starting the next block, file, or major section.
- Keep the wrapper minimal — deliver the artefact; don't restate the prompt or narrate every step. Surface flags only where they matter: conflicts with a locked decision, a pending Principal decision (Sections 4.5, 6.6), cross-class propagation notes, or a genuine quality risk.
- Stop at a pending decision — flag rather than resolve (Sections 4.5, 6.6).

### 7.6 Full project-recovery scenario

If the surviving files exist but the Charter, Run Book, or both are missing, the standard orientation checklist (7.3) can't be completed as written. Instead:

1. Treat every surviving file as evidence — read broadly before drafting anything.
2. Reconstruct in this order: system structure first, then procedure, then policy.
3. Tag every reconstructed claim Observed / Inferred / Reconstructed, and surface open questions to the Principal rather than resolving them silently.

---

## 8. Build & Quality Gates

### 8.1 Gate sequence

| Gate | When | Checklist |
|---|---|---|
| Pre-build | Before drafting | Section 4.5 |
| Orientation | Start of any session | Section 7.3 |
| In-build stage gates | During drafting | Sections 6.2–6.6 |
| Pre-finalization | Before marking a file complete | Section 6.8 |
| Propagation | Immediately after finalization | Section 12 |

A file may proceed to the next gate only after the current gate has been completed successfully or any required Principal ruling has been recorded.

### 8.2 What blocks a gate

- A required dependency is missing or unconfirmed current (Sections 4.4, 4.5).
- A pending Principal decision is outstanding (Sections 4.5, 6.6).
- A checklist item fails and cannot be corrected without a scope decision.
- An answer key does not verify against its item set.
- A worksheet uses an unheld word in a graded item.
- A values or continuity guard is violated (sacred-word, non-mahram, delivered-content lock — Section 11).

### 8.3 On gate failure

1. Stop work on that item.
2. Log the specific failure in the file's version log (or, pre-build, note it before drafting begins).
3. If it requires a Principal decision, flag it and pause — do not draft a workaround.
4. If it's correctable without a scope decision, correct it and re-run the gate.

### 8.4 Gate Responsibilities

- The Content Developer is responsible for completing every quality gate.
- The Principal becomes involved only when a gate surfaces a policy, scope, or timing decision.
- Once the ruling is recorded, the Content Developer resumes the workflow.

---

## 9. Weekly Teaching & Assessment Cycle

### 9.1 Weekly sequence

| Day | Action | Who |
|---|---|---|
| Sun–Wed | Teach scheduled classes; begin Classwork in class under guidance (9.3); assign daily Homework, plus any unfinished CW; close each day with the Exit Check (9.4) | Teacher / Student |
| Thu | Conduct the weekly Performance Test at school | Teacher / Student |
| Thu | Give the weekly Assignment after the Performance Test | Teacher |
| Sun | Collect Assignments, review Performance Test and Assignment outcomes as needed, then begin the next week's block | Teacher |

### 9.2 Writing load (implementation standard)

English classes are **writing-intensive**. Students should spend most of the lesson actively writing, not only listening or answering orally.

1. **Every teaching week normally carries both** a **Classwork (CW)** worksheet used during the lesson and a **Homework (HW)** worksheet for independent practice. (Worksheet sizing is set at the volume pass, 6.3.)
2. **Performance Tests emphasise sustained writing** — the target is approximately **30 minutes of continuous writing** appropriate to the class level, rather than many short, disconnected objective items.
3. **Assessment primarily measures independent production.** Recognition and oral practice are preparation *for* production, not substitutes for it. Where a block's cap is recognition-only, that caps the *grammar depth*, not the amount of writing the week demands.
4. **Writing volume rises with class level**, gradually and age-appropriately: lower classes write less and with more scaffolding, higher classes sustain longer independent production.

### 9.3 Classwork and Homework workflow (implementation standard)

1. In class, students **begin the CW worksheet under the teacher's guidance**.
2. The teacher explains the lesson, demonstrates representative questions, and solves selected examples together with the class.
3. Students complete **as much of the CW as time allows** during the lesson.
4. **Unfinished CW becomes part of the home task**, completed alongside the HW worksheet.
5. Teachers therefore **plan CW expecting it may not finish in class**, while ensuring enough guided practice is given before students continue independently.

This workflow applies **unless a lesson or special instruction explicitly states otherwise**.

### 9.4 Exit Check (implementation standard)

Every teaching day (Sun–Wed) ends with a short **Exit Check** before dismissal. It is a whole-class formative check confirming that the day's learning objective was actually reached — not a graded assessment, and not a preview of tomorrow.

1. **One prompt per student.** Prepare as many prompts as there are students in the class, so every student answers exactly once. The count follows the **delivering branch's** current roll for that class — at the time of writing, Class 4 at the Sylhet branch has 12 students, so its Exit Check carries 12 prompts. Where class size differs between branches, or changes during the year, the teacher adds or removes prompts while keeping the same format. Roll numbers are not governance data: a block file records the count it was built for, and a teacher adjusts on the day without a file revision.
2. **The day's learning target only.** Prompts test what was taught that day (and, where the day builds on it, earlier days of the same block). An Exit Check never introduces new content, and never reaches ahead to a later day's target.
3. **Two to five minutes, no worksheet.** Oral, whole-class, one student per prompt. Nothing is printed, distributed, or collected. It runs after the CW/HW instructions, immediately before dismissal.
4. **Prepared in advance.** Prompts are written into the Lesson Plan as part of the block build, not improvised at the end of a lesson. Each day's script carries its own Exit Check set.
5. **Answer plus reason, where the objective supports it.** If the day's target involves a rule with a statable justification, the student gives the answer *and* names the reason in a few words. Where the target is recall or recognition only, the answer alone is enough.
6. **What the teacher does with it.** A student who answers wrongly is corrected on the spot and the prompt moves on — this is a temperature check, not a test. If several students miss the same prompt type, that is a signal to re-open the point at the start of the next day, and (where the pattern is severe) to note it for the block's retention record.

**Block-build requirement.** Every block includes an Exit Check set for each teaching day, aligned to that day's stated objective. This is checked at finalization (§6.8).

### 9.5 Homework vs. Assignment

- **Homework** — daily, given after each Sun–Wed class: the **HW worksheet** for that class-day (9.2 r.1), introduced with a one-line task statement and one modelled item so students can start unaided; completed at home that night, together with any unfinished CW (9.3); checked out of class with a khata comment.
- **Assignment** — weekly, given at school on Thursday after the Performance Test; completed over Thu–Sat; submitted Sunday.

Do not conflate the two — they are separate artefacts with separate timing and separate purposes.

### 9.6 Performance Test

The weekly Performance Test is conducted at school under teacher supervision. Parent participation is not part of the assessment workflow. Mark the same day or as soon as practical; results feed the retention gate (9.8).

### 9.7 Assignment generation

Assignments are generated as part of the standard block-build process and are delivered alongside the weekly block materials (Section 6.2). The Assignment consolidates the week's learning and should align with the week's grammar objective(s), held vocabulary, and exam-style practice. Apply the same held-word and exam-format constraints as to any other graded worksheet.

### 9.8 Marking and retention gate

Mark the Performance Test against its answer key, then apply:

| Average | Action |
|---|---|
| ≥ 80% | Increase next week's fresh batch size per the planned ramp (Section 5.3) |
| 65–79% | Hold batch size at current level |
| < 65% | Shrink next batch and re-teach the weakest items |

Pacing logic is unchanged from Section 5.3 — only the assessment source has changed.

### 9.9 Wall reference

Keep the Clue Card current on the classroom wall. Update it only when a block adds a new role to it.

---

## 10. Exam-Mapping Update Procedure

### 10.1 Binding papers

All Half-Yearly and Annual papers for a class remain binding simultaneously. A new paper adds to the binding set; it does not retire an earlier one. Never remove exam-format coverage from a Drive Plan or block solely because a newer paper no longer tests it, if an earlier binding paper still does.

### 10.2 When new assessment evidence becomes available

When new assessment evidence becomes available (e.g. a Half-Yearly or Annual paper):

1. Extract every question, its format, its instruction wording, and its mark split.
2. Compare against the class's current §7 map, question by question.
3. Classify each question as:
   - **Already covered** — matches an existing block's anchor; no action.
   - **Format or weight change on an existing anchor** — same skill, different item count/marks/mix; update §7's citation, no scope change.
   - **New content** — tests a skill no current block teaches.
4. After comparing against §7, also confirm whether the change affects File 2, File 3 (existing or future blocks), or the Block-Build Specification — this identifies impact; it does not mean updating them yet.
5. Log the comparison in the Drive Plan's version log, even where no change results.

### 10.3 Updating the §7 map

- Add the new paper's citations alongside existing ones for the same block — do not overwrite.
- Where formats differ across binding papers for the same block, retain practice for both formats.
- Where item counts or mark splits differ across binding papers, state each explicitly rather than picking one.

### 10.4 New content — map-then-decide

1. Do not draft teaching material for it yet.
2. State what the new content is, which paper introduced it, and candidate placements in the spine.
3. Flag it as a pending Principal decision (Sections 4.5, 6.6) and pause that item.
4. Once ruled on, update the affected planning artefacts first, then build or revise the affected block(s) in accordance with Section 11 where applicable.

### 10.5 Triage classification

| Category | Criteria | Action |
|---|---|---|
| Definitely required | New content is now binding, or a currently-graded item conflicts with a stated teaching cap | Build/resolve per 10.4; schedule per Section 11 if the target block is delivered |
| Optional | Format harmonization, item-count/mark-weight alignment, cosmetic consistency | Apply opportunistically; not gating |
| Wait for future evidence | A single paper's isolated item, no clear pattern, no immediate exam-readiness risk | Log and monitor; act only if a subsequent binding paper confirms the pattern |

Record the triage decision and its rationale in the relevant version log, even if no immediate action is taken. Items classified as "Wait for future evidence" are included in the periodic outstanding-flag review (Section 12.7).

### 10.6 Reverse channel — recommending exam revision

If a binding paper tests materially beyond this class's book/TG readiness or the Charter's depth caps, do not assume the curriculum must automatically expand to match the paper. Log an exam-revision recommendation to the Principal instead.

### 10.7 Interaction with the delivered-content lock

If 10.4's placement decision would land in an already-delivered block, do not revise that block. Proceed to Section 11.

---

## 11. Delivered-Content Lock Procedure

### 11.1 Scope of the lock

A block is delivered once its class has taught it to students. Delivered blocks are frozen: no curriculum or content changes, regardless of what later evidence (Section 10) surfaces about them.

The lock applies to the block's teaching script, worksheets, Performance Test, Assignment, and answer keys. It does not apply to:
- File 2 (words may still be added/rescheduled for later weeks),
- later blocks (may still be built or revised),
- the Drive Plan (may still be version-bumped; the cap statement is documentation, not a re-delivery of taught content).

### 11.2 The implementation record

The implementation record is the log of which blocks have actually been taught to students, by class. The Teacher maintains it, updating it as each block is delivered. It records, at minimum: class, block number/topic, and the date teaching was completed.

Confirm delivery status against the implementation record before making any curriculum change to a block. Where the record is unavailable or unclear, confirm with the Principal directly.

### 11.3 On identifying a delivered block affected by new evidence

1. Confirm delivery status against the implementation record (Section 11.2).
2. Do not edit the delivered block file.
3. Identify candidate downstream locations: a later block in the same class, a new companion strand inside an existing later block, or File 2's batch schedule if the fix is vocabulary-only (Section 5.4).
4. If more than one candidate is plausible, or none is clear, flag it as a pending Principal decision (spine placement) rather than choosing unilaterally.

### 11.4 Building the downstream fix

- Open the receiving block's normal re-walk step with a one-line bridge naming the new content — do not assume prior exposure just because the topic conceptually "belongs" earlier.
- Deliver new vocabulary through the routine and format the class already knows (Section 6).
- Apply the standard per-block lifecycle (Section 6) to the downstream fix.

### 11.5 Recording the redirect

Record the redirect in the receiving block's version log and, where appropriate, in the Drive Plan's version history or project change log. Do not modify the delivered block solely to document the redirect.

### 11.6 Continuity check before finalizing a downstream fix

- ☐ No assumption that students already met this content, unless it was genuinely covered elsewhere.
- ☐ New content uses a routine/format already familiar to students who completed the delivered block.
- ☐ The delivered block itself remains unmodified.
- ☐ The fix is traceable from both the source gap and the receiving block's own build record.

Once the receiving location has been identified, continue the update using the standard propagation workflow (Section 12).

---

## 12. Versioning, Propagation & Escalation Protocol

### 12.1 Version log — required on every file

Every Drive Plan, File 2 workbook, Specification, and Block carries a version log: version, date, change description, and who ruled on it where a decision was involved. Update it at every stage of the file's lifecycle (Section 6.2–6.6), not only at final release.

### 12.2 Superseding a file

A new version replaces the old one; the old version is archived, not deleted. The new version states what changed and why. Every supersession is a logged event.

### 12.3 Propagation sequence

1. Log the change in its file of origin.
2. Update the next artefact up the dependency chain to match (Section 4.1).
3. Check whether the Block-Build Specification needs a matching update; if not applied immediately, log that it's pending.
4. Write a propagation note listing every other class's equivalent artefact that will need the same treatment. Do not apply it there yet unless directed.
5. Route the timing decision (apply now vs. batch) to the Principal.

### 12.4 Cross-class batching

Default to logging a propagation note and waiting for a batching decision, rather than applying a change across all classes immediately. When the Principal approves a batch, apply it to all flagged classes in the same pass, and close out every propagation note it addresses.

### 12.5 Escalation — when to flag the Principal

Flag and pause, rather than proceeding, whenever:
- A cap or scope decision is required (Sections 4.5, 6.6, 10.4).
- A delivered block is affected and needs a downstream placement decision (Section 11.3).
- A propagation note's timing needs to be set (12.3 step 5).
- An exam-revision recommendation is being raised (Section 10.6).
- Two binding documents conflict and neither resolves the other.

Do not resolve any of the above unilaterally. State the issue, the options, and a recommendation if one is clear — then wait.

### 12.6 Closing a propagation note

Close a propagation note only when the flagged class's equivalent artefact has been updated to match, that update's own version log records the change, and the originating note is marked closed with a pointer to the closing update. Do not close a note by declaring an intention to apply it later.

### 12.7 Outstanding-flag review

Periodically review all open propagation notes, pending-decision flags, and items classified as "Wait for future evidence" (Section 10.5) across every class's artefacts. An open flag with no forcing function to resolve it is a known failure mode of this workflow — review prevents flags from remaining open indefinitely without a decision ever being made.

---

## 13. Self-Construction & Value-Alignment Marking Guidance

### 13.1 Marking student self-construction responses — value alignment

*(Governance source: **PD-010** — Islamic/value alignment is **not a scored rubric criterion**, project-wide. Charter §I.3.)*

Charter §H applies in full to every teacher-authored and Content-Developer-authored artefact — questions, prompts, model answers, worksheets, the Assignment, the Performance Test. This is unchanged and non-negotiable (Section 6.5 values audit).

**No rubric awards marks for value alignment.** The self-construction rubric is 4 marks — Content accuracy · Reasoning · Organisation · Correct word-class placement (Charter §I.3) — and value alignment is not among them, nor available as a substitute criterion (§I.5). The guidance below governs how a values issue in a student response is handled instead.

It does not extend to student responses beyond what the question itself asks for:

- A student's response may be religiously neutral. Do not deduct marks for a neutral, non-Islamic, non-value-explicit answer, provided it does not conflict with Charter §H.
- Require explicit Islamic or value content in a student's response only when the question itself explicitly asks for it.
- If a student's response actively conflicts with Charter §H, correct it as a values matter, not as a grammar or content-quality deduction — flag it rather than silently marking it down as if it were a language error.

| Question asks for… | Student writes a religiously neutral, on-topic answer | Marking |
|---|---|---|
| Open topic, no value instruction (e.g. "Write two sentences about your school day.") | Yes | Full marks if otherwise correct — do not deduct for absence of value content |
| Explicit value instruction (e.g. "Write two sentences using Islamic greetings.") | Yes, but omits the instructed value content | Mark down — the question's own instruction was not met |
| Any question | Response conflicts with Charter §H | Do not grade as a language error — flag as a values matter |

### 13.2 Self-construction question design — expected depth

State the expected depth of response directly in the question's own wording — sentence count, word count, or an explicit instruction to explain or justify. Do not leave depth implicit and infer it later at marking time.

Do not deduct marks for a correct, on-topic answer being "too simple" unless the question's own wording explicitly required more detail, explanation, or complexity. If the question didn't ask for it, its absence isn't an error.

Apply this convention whenever authoring a self-construction question (Content Developer, Section 6.2) or adapting one in the moment (Teacher).

| Expected depth | Example question | Marking note |
|---|---|---|
| Single word/phrase | "Write one word that means the opposite of 'kind.'" | One correct word earns full marks. |
| One sentence | "Write one full sentence using the word 'patience' correctly." | A single correct sentence earns full marks — do not require a second sentence or an explanation. |
| Multiple sentences with explanation | "Write two sentences describing a time you helped someone, and explain in one more sentence why it was a good deed." | Full marks require all three stated parts — a two-sentence answer without the explanation is incomplete because the question asked for it, not because two sentences is inherently insufficient. |
| Extended/open | "Write a short paragraph (at least four sentences) describing your daily routine, using at least three of this week's new words." | Mark against exactly what's stated — length and word-count requirements, not additional unstated criteria. |

---

## Version log

| Version | Date | Change | By |
|---|---|---|---|
| v1 | 2026-07-10 | Initial compiled Run Book, drafted section by section with the Principal from surviving-evidence analysis and the English Drive System Architecture document. | Content Developer / Principal |
| v1.1 | 2026-07-10 | Consistency pass: standardised Assignment/Performance Test/Homework terminology across all sections; fixed dangling and mismatched cross-references; defined the implementation record (Section 11.2) and linked it to every delivery-status check; cross-linked "Wait for future evidence" triage items (Section 10.5) to the periodic outstanding-flag review (Section 12.7). | Content Developer / Principal |
| v1.2 | 2026-07-10 | Added Section 13 (Self-Construction & Value-Alignment Marking Guidance), operationalizing two Principal decisions: (1) student responses may be religiously neutral unless the question explicitly requires value content, while all teacher/Content-Developer-authored material remains fully bound by Charter §H; (2) self-construction questions must state expected response depth in their own wording, and marking may not penalize correct answers for being "too simple" beyond what was asked. No Charter changes. | Content Developer / Principal |
| v1.4 | 2026-07-21 | **Teacher Delivery Sheet extract type (Principal ruling, 2026-07-21).** New teacher-facing extract that projects a master block down to only what the classroom teacher needs, stripping producer/Content-Developer governance metadata that creates print-time information overload. (1) New **3.13** — defines the Teacher Delivery Sheet (TD): derived, unversioned, regenerate-only (per 3.12 r.1), one `.md` per block, filename `C{class}B{block}_TD.md`; includes the locked strip/keep manifest. Two boundary rulings: teacher receives the free-thinking **rubric** (not its charter-traceability) and **PT instructions** (never the key or dictation list). (2) New **6.10 Stage 7** — TD generation procedure: apply the manifest, no graded-content leak, kept sections reproduced verbatim (teaching script Bangla-led, not translated), forward-only retrofit. (3) **3.10** — `TD` row added to the canonical terminology table. (4) **3.11** — `TD` added to the `{CODE}` list; block-scoped, no day/week suffix (`C5B04-TD`). (5) **6.8** — pre-finalization checklist line added. No Charter changes. All changes forward-only per Charter K.3. | Content Developer / Principal |
| v1.3 | 2026-07-19 | **Terminology reconciliation & extract model (Principal rulings, 2026-07-19).** (1) New **3.10 Canonical terminology** — PT-only in written artefacts; "Thursday test" / "weekly test" / "take-home test" retired as written aliases (narrows the earlier interchangeability ruling: interchangeable orally, PT in files); "Worksheet CW" unnumbered form retired; "self-construction" retained as the formal long form of Self-try, not retired (avoids a §13 rewrite). (2) New **3.11 Canonical artefact IDs** — `C{class}B{block}-{CODE}[{day}][-W{week}]`, block-anchored (not week-anchored) by ruling; item-level suffix defined. (3) New **3.12 + 6.9 master/extract model** — block file is the single master; per-day CW/HW and per-week PT extracts are derived, unversioned, regenerate-only; keys and dictation lists master-only; locked student-sheet template (school header, one-line Name/Date, English instructions and A/B/C sections, marks printed on PT, pure markdown, italic footer ID); PT extracts only from masters on the Charter v1.2 §M.3 in-school model; machine consistency check compares items/structure, not raw text (instructions are translated); print path `.md` → docx; short answers on the sheet, extended responses on supplementary paper. (4) **3.1** — `Assignment` added to the FileType list with pattern `C{class}_ENG_Block{NN}_Assignment_v{n}.docx`; the `Class_{n}_B{NN}_Assignment` pattern retired for new files. (5) **3.2** — GrammarBlock-vs-Block unification recorded as a still-open Principal ruling; per-class continuity stands. (6) Checklists 3.9 and 6.8 extended; 6.2 build outputs now include extracts. **Open items:** in-item Bangla hint language in extracts (6.9.5); GrammarBlock/Block unification (3.2). All changes forward-only per Charter K.3 — no delivered block reopened for renaming alone. | Content Developer / Principal |
| v1.5 | 2026-07-23 | **Language of delivery — implementation standard (Principal ruling, project-wide).** New **§3.14**: the default instructional language is **English** across teacher scripts, classroom delivery, and all instructions (CW, HW, Performance Test, Assignment, worksheet directions, Clue Card directions, dictation, teacher notes). **Bangla is retained only where it is the learning content itself** — Bangla meanings, English↔Bangla translation, English–Bangla matching, and items where Bangla is intentionally the task or the required answer. Where Bangla genuinely aids a difficult concept, the main script stays English and the Bangla is an **explicitly marked optional teacher note**. Drive Plans **inherit** this and do not restate it (§B.1); any class-level delivery-language convention is superseded. Retrofit is **forward-only** (Charter §K.3) — finalized blocks convert at their next revision, not reopened for language alone. **Consequential edits:** (1) **§3.13** strip/keep table — "The teaching script (Bangla-led)" → "(English — §3.14)". (2) **§6.10 r.4** — removed the assertion that the teaching script is Bangla-led and untranslated; the TD reproduces the master verbatim and is not a language-conversion step. (3) **§6.9 r.3** — machine-check rationale generalised (an extract may reword instruction lines; for pre-§3.14 masters it may translate them). (4) **§6.9 r.5** — the flagged-but-unruled question on in-item Bangla hints is now **resolved by §3.14**: in-item scaffolding is instructional support and is written in English; Bangla stays only where the item's task is Bangla, with optional-note treatment where a Class 1–2 item genuinely needs it. **No Charter change required** — the Charter carries no language-of-delivery provision. | Principal / Claude |
| v1.6 | 2026-07-23 | **Two implementation standards added (Principal, project-wide).** New **§9.2 Writing load** — English classes are writing-intensive; students spend most of the lesson actively writing; every teaching week normally carries both a **CW** worksheet (in-lesson) and an **HW** worksheet (independent practice); Performance Tests target **~30 minutes of sustained writing** appropriate to class level rather than many short objective items; assessment primarily measures **independent production**, with recognition and oral work as preparation for it; writing volume rises gradually from lower to higher classes. A recognition-only block cap limits **grammar depth**, not the week's writing demand. New **§9.3 Classwork and Homework workflow** — students begin CW in class under teacher guidance; the teacher explains, demonstrates representative questions and solves selected examples with the class; students complete as much CW as time allows; **unfinished CW carries home and is completed with the HW worksheet**; teachers plan CW expecting it may not finish in class, while ensuring sufficient guided practice first; applies unless a lesson explicitly states otherwise. **Consequential edits:** old §9.2–§9.6 renumbered to **§9.4–§9.8** with internal cross-references updated (retention gate 9.5→9.7; Assignment generation 9.4→9.6). **Conflict resolved:** §9.4 and §2.3 described daily Homework as *"a one-line task and one modelled item"*, which read as an oral-instruction task rather than a worksheet and contradicted §9.2 r.1; both now describe the **HW worksheet**, with the one-line task statement and modelled item retained as how it is *introduced*. §9.1 weekly sequence updated to show CW beginning in class under guidance and unfinished CW going home. **No Charter change required** — the Charter carries no worksheet-load or CW/HW workflow provision. | Principal / Claude |
| v1.7 | 2026-07-23 | **Grammar Exemplars — operational rule for PD-009 (Principal, project-wide).** New **§5.7 Grammar Exemplars (not vocabulary)**: a small, fixed, closed set of words whose sole purpose is to demonstrate a grammar rule is classified as a Grammar Exemplar and is **exempt from the held-vocabulary rule** (Rule 1 / §5.1). Three-part qualifying test (required by the Drive Plan §2 cap or a binding exam anchor · the graded skill is the rule, not the word's meaning · belongs to a closed fixed set), with an explicit anti-drift line: a word that is merely convenient is not an exemplar, and a binding paper's item shape built on an ordinary unheld word is rebuilt on a held word rather than admitting that word. Implementation: exemplars are **taught explicitly** (Lesson Plan, teacher modelling, Clue Card, guided practice) before any graded use; may appear in **CW, HW, PT and Assignment including as graded answers**; are **never** added to the Pool or Batch Order, never counted as fresh or held vocabulary, never vocabulary-learning targets, and **never dictation or spelling items**; the list stays fixed, minimal and stable across classes; Charter §H.9 curation and the §H.3 sacred-word guard apply in full. Each block using exemplars states its list in the header, traced per item to its cap or exam anchor. **File 2 is not amended** — the exemption is a carve-out in the audit, not a change to Pool contents, consistent with the Pool already excluding function words at source as grammar targets. **Consequential edits:** (1) **§6.5** held-word audit — graded answers now trace to a held word *or* a declared exemplar, with anything outside both sets failing. (2) **§6.8** pre-finalization checklist — held-word line extended, plus a new line verifying the exemplar list is declared and traced, every exemplar taught before graded use, and none used as a dictation or spelling item. **Governance source: PD-009** (Curriculum Design Decision Log), raised during the C4 Block 4 (Article) build, where the §2 cap and all three binding papers (HY25 Q2, HY26 Q7, Annual Q3) required sound-exception and proper-noun items that no W4 held word could supply. **No Charter change made** — Charter §E Rule 1 should carry a pointer to this carve-out at its next revision (flagged for the batched update). Forward-only per Charter §K.3. | Principal / Claude |
| v1.8 | 2026-07-23 | **Exit Check — delivery standard (Principal, project-wide).** New **§9.4 Exit Check**: every teaching day (Sun–Wed) closes with a short whole-class formative check confirming the day's learning objective was reached. **One prompt per student** so every student answers exactly once — the count follows the delivering branch's roll (Class 4 at the **Sylhet** branch is currently 12 students, so 12 prompts); teachers add or remove prompts as class size changes while keeping the format, without a file revision. Note the branch distinction: the drive is **delivered at Sylhet**, while the binding exam papers (§10.1) are **Mohammadpur** papers — roll sizes come from the former, exam anchors from the latter. Prompts cover **the day's target only** (never new content, never a later day's target), run **2–5 minutes orally with no worksheet**, are **prepared in advance in the Lesson Plan** rather than improvised, and require **answer plus a brief stated reason** where the objective supports one. Wrong answers are corrected on the spot; a repeated miss pattern signals a re-open at the start of the next day. Every block build must supply an Exit Check set per teaching day. **Consequential edits:** (1) old **§9.4–§9.8** renumbered to **§9.5–§9.9** (Homework vs. Assignment · Performance Test · Assignment generation · Marking and retention gate · Wall reference). (2) **§9.1** weekly-sequence Sun–Wed row now closes with the Exit Check. (3) **§6.2** build outputs include the per-day Exit Check set. (4) **§6.8** pre-finalization checklist line added. **Stale cross-references repaired** — §2.4, §2.5 and §5.3 still pointed at pre-v1.6 numbering (retention gate cited as 9.5, assessment workflow as 9.3, Assignment generation as 9.4); all now resolve correctly, along with refs shifted by this insert (§5.7 dictation → 9.6; §6.2 Assignment → 9.7; §9.6 retention gate → 9.8). **No Charter change required** — the Charter carries no lesson-close provision. | Principal / Claude |
| v1.9 | 2026-07-23 | **Teacher Answer Key — consolidated key extract (Principal, project-wide).** New **§3.15**: the **Teacher Answer Key (AK)** is a single consolidated key per block covering every graded artefact, replacing per-worksheet key sections. Derived, unversioned, regenerate-only (§3.12 r.1); filename `C{class}B{block}_AK.md`. **Fixed order:** CW1 · HW1 · CW2 · HW2 · CW3 · HW3 · CW4 · HW4 · PT · Assignment. **Original item numbering preserved exactly** (no restarting or re-flowing); **answers only**, no question text, with brief marking notes only where an item needs one (model answers, accept-either rulings, mark splits); **PT dictation word lists live in the AK**, never on the student sheet; never issued to students and never merged into a student extract or the TD. **Ordering constraint:** the AK is assembled only after every worksheet, the PT and the Assignment are final — a key written alongside a worksheet still under revision goes stale silently. New **§6.11 Stage 8** — AK generation with a **required programmatic consistency check**: every graded item has exactly one corresponding answer, no answer references a non-existent item, numbering is continuous and non-duplicated per artefact, and per-artefact mark totals computed from the AK match the totals printed on the worksheets; a mismatch blocks delivery (§8.2). **Consequential edits:** (1) **§3.10** terminology table — `AK` row added, per-worksheet "answer key" form retired. (2) **§3.11** — `AK` added to the `{CODE}` list, block-scoped with no day/week suffix (`C4B04-AK`). (3) **§6.2** — answer keys remain in the master but are no longer printed after each worksheet. (4) **§6.8** — pre-finalization checklist line added. **No conflict with §3.12 r.2 or §3.13:** those bar keys from *student* extracts and the Teacher Delivery Sheet; the AK is a teacher-facing artefact and both prohibitions stand unchanged. Forward-only per Charter §K.3 — finalized blocks gain an AK at their next revision or on teacher demand. | Principal / Claude |
| v1.10 | 2026-07-23 | **Paired-sheet duplication audit (Principal, project-wide).** New fifth named audit in **§6.5**: for each teaching day, the day's **CW and HW answer sequences are compared position by position**, with positional overlap capped at **≤35%**. Rationale: a CW and HW sharing an answer order let a student complete the homework by copying the classwork column without reading any item — defeating the independent-practice purpose of HW (§9.2 r.1) and reproducing, across paired sheets, exactly the exploitable pattern **PD-008** bars within a single exercise. The audit names the build habit that causes it: an HW assembled by trimming or lightly editing its CW bank inherits that bank's answer order. **Item content may legitimately overlap** between CW and HW — the week's practice is deliberately repetitive — but the **answer order may not**; the HW is shuffled independently and re-verified. The same comparison runs against the PT wherever a PT part reuses a worksheet's item shape. **Consequential edit:** §6.8 checklist now reads "all five named audits," naming the overlap threshold. **Discovered during the C4 Block 4 (Article) build**, where HW-2 Part A was found to be a 100% positional match to CW-2's first twelve answers and three further parts exceeded 60%; per-sheet de-patterning had passed in every case, because the existing checks tested each worksheet in isolation. Forward-only per Charter §K.3 — existing finalized blocks are audited at their next revision, not reopened for this alone. | Principal / Claude |
| v1.11 | 2026-07-23 | **Rehearsal/graded disjointness audit (Principal, project-wide).** New sixth named audit in **§6.5**: where a graded task rehearses an ungraded one — a demo Self-try and its PT counterpart, a practice set and its test version, a modelled example and the item assessing the same skill — the **prompt sets must be disjoint**. A student who drafted an answer during rehearsal must not be able to reproduce it verbatim under assessment, which would convert independent production (§9.2 r.3) into recall of the previous day's sentence. **Item-type coverage must still match** so the graded task is neither harder nor narrower than the rehearsal; only the specific words, pairs, names or prompts change. Word boxes, prompt lists and self-try stimulus sets are called out as the highest-risk artefacts, being the ones most often produced by lightly editing their rehearsal counterpart. Cites the existing C3/C4 Block 3 PT precedent requiring self-try pairs to be redistributed so no student received their own earlier pair. **Consequential edit:** §6.8 checklist now reads "all six named audits," naming both this and the paired-sheet audit. **Discovered during the C4 Block 4 (Article) build**, where the PT self-try word box shared four of six words with the Wednesday demo box it had been adapted from; the box was rebuilt disjoint (`M.P. · honest · Bangladesh · sun · money · ticket` against the demo's `hour · university · Dhaka · moon · water · envelope`) with all four article types still reachable. This is the same build habit behind the v1.10 audit — a derived artefact inheriting its source's structure — surfacing one layer up, between rehearsal and assessment rather than between paired worksheets. Forward-only per Charter §K.3. | Principal / Claude |
| v1.12 | 2026-07-24 | **Item-text duplication audit (Principal, project-wide).** New seventh named audit in **§6.5**: graded items are compared by **sentence text**, not only by answer — each day's HW against its CW, and the **PT against every worksheet in the block**. Rationale: verbatim repetition is transcription, not practice; a student meeting the same sentence twice reproduces an answer already produced rather than applying the rule, and a PT assembled from worksheet sentences measures recall of those sentences instead of independent production (§9.2 r.3). **Rule: re-test the same rule on different sentences** — the same trigger word, article and reason may recur freely, but the sentence frame must change. **Thresholds:** HW **≤2** items identical to its CW; PT **zero** items identical to any worksheet. Explicitly distinguished from the v1.10 paired-sheet audit, which compares answer *order*: a sheet can pass order-overlap while being half a literal copy, because reordering copied items changes the sequence without changing the text. **Consequential edit:** §6.8 checklist now reads "all seven named audits." **Discovered during the C4 Block 4 (Article) build** when the Principal queried HW-3 Part A: six of twelve items were word-for-word identical to CW-3, rising to nine of twenty across Parts A and C, while the sheet passed answer-order overlap at 33%. A full sweep then found the **PT repeated nine of its twenty-one written items verbatim from worksheets** — the most serious instance, since it silently converted the graded test into a recall exercise. Day 4 scored zero duplicates, having been built from an independent bank rather than by trimming its CW; this confirms the cause is the derive-by-trimming habit already named at v1.10 and v1.11. Forward-only per Charter §K.3. | Principal / Claude |
| v1.13 | 2026-07-24 | **Self-construction rubric — 4 marks, value alignment unscored (Principal, project-wide; Charter v1.3 §I).** **§13.1** now opens with the governing rule: no rubric awards marks for value alignment, the self-construction rubric is **4 marks** (Content accuracy · Reasoning · Organisation · Correct word-class placement, 1 each, uniform across all five classes), and value alignment is neither a criterion nor an available substitute (Charter §I.5). The existing §13.1 guidance is unchanged in substance and now reads as the procedure for handling a values issue in a student response — flag and correct as a values matter, never as a language or content deduction. **This resolves a standing contradiction:** §13.1 already directed that value content be required only where the question asks for it, while the rubric simultaneously awarded 2 marks for it on open production tasks. Governance source: **PD-010**. Charter §I rewritten at v1.3 in the same pass; all five Drive Plans §9 updated. Existing blocks convert forward-only (Charter §K.3). | Principal / Claude |
| v1.14 | 2026-07-26 | **Two new non-held word-statuses — operational rules (Principal, project-wide).** New **§5.8 Block-local teaching words (taught-but-not-pooled)** and **§5.9 Override words (exam-anchored common vocabulary)**, placed alongside §5.7 Grammar Exemplars as the third and fourth carve-outs from the held-vocabulary rule. **§5.8 (PD-012):** a word required to complete a concept the held pool cannot supply, sourced from the binding papers, is **gradeable within its own block only**, never a dictation/spelling item, not held downstream, and not in spaced revision — the previously-undefined \"taught in-block, gradeable in-block, not in File 2\" status the Run Book had no word for. **§5.9 (PD-011):** common, age-appropriate, exam-anchored vocabulary the held pool cannot supply may be admitted as an **Override word**, counted toward the week's taught-vocabulary load and **spelling/dictation-eligible** from its taught day — behaving as real taught vocabulary, the point that distinguishes it from both exemplars (§5.7, never spelling targets) and block-local words (§5.8, gradeable in-block only). Both sections spell out how each status differs from the neighbouring two, so the three carve-outs are not conflated. **Consequential edits:** §6.5 held-word audit now passes a graded answer tracing to a held word, a declared exemplar, **or a declared block-local word**; §6.8 checklist extended to verify the block-local set is declared/traced, taught before graded use, never a dictation/spelling item, and never reused as held downstream. **File 2 is not amended** by either status — both are build-time admissions, forward-only for any Pool reconciliation. **Governance source: PD-011, PD-012** (Curriculum Design Decision Log). Raised across the C1 Block 4 (Adjective, override) and C2/C3 Block 5 (Plural/Gender, block-local) builds, where the held pool could not supply the adjectives, the -es plural set, or the full gender categories the binding papers test. Forward-only per Charter §K.3. | Principal / Claude |
| v1.16 | 2026-08-01 | **Worksheet reference blocks — new governance where there was none (Principal, project-wide).** New **§3.17 Worksheet reference blocks (the rule box)**: the boxed panel a worksheet may carry above its items **may print a rule** and **may print an arbitrary learned list** (a closed set no taught rule derives — river names, country names taking *the*, irregulars, fixed collocations), and **may not print a worked example of a derivable word the sheet grades**. The operative distinction is **derivability**, not word class: *an hour* is derivable by applying the taught method, so printing it above an item grading *hour* is an answer key; *the Padma* is derivable from nothing, and withholding it tests days-old recall rather than reasoning. Clue Cards and other wall references are **exempt** — they are not sat with the paper. A block may vary the convention across its own sheets provided each complies, stating the pattern so it reads as design rather than drift. **Consequential edits:** (1) **§6.5** gains a **Reference-block audit** requiring the box to be compared against its own sheet's key **with punctuation normalised on both sides**. (2) **§6.8** checklist line added. **Governance source: PD-018**, raised on the C5 Block 6 (Article) build, where HW-1's rule box printed seven article+word pairs directly above the parts grading them — **12 of 38 marks copyable off the top of the sheet** — a defect that survived four block versions and the block's own §6.5 audit; a first re-audit then reported a second sheet clean that was leaking a further seven, because commas between article and noun defeated the match. The Run Book previously carried **no provision at all** governing reference blocks, which is why this shipped. **Two further project-wide rulings applied in the same pass.** **PD-019 — attribution form:** §6.5 gains an **Attribution audit** — where a natural phenomenon acts, the agency is **attributed in place** (*"the sun gives us light by Allah's Will"*) rather than restructured to move Allah into the subject position; plain description remains equally acceptable. Same theology, materially lower cost to the student, since a three-word addition is a habit that travels where a structural correction is forgotten under exam pressure. §6.8 line added; §13.1 marking guidance unchanged — attribution is corrected as a values matter, never marked down as a language error. **PD-021 — festival:** the §6.5 values-audit line now records that festival contexts are admissible where the referent is Islamic (Eid, Ramadan) and excluded for other-faith festivals; the exclusion attaches to the referent, not the word. **PD-020 — instrument selection:** a pointer note added ahead of **§5.9** setting out how §5.7, §5.8 and §5.9 are chosen between, with **load as a decision input** (a candidate passing the exemplar test must not be admitted under §5.8, which would add it to the week's taught load and can trip the §9.8 retention gate on a vocabulary count rather than on the block's actual skill) and the **rebuild-before-widening** companion rule. §5.7–§5.9 themselves are **unamended**. All forward-only per Charter §K.3 — delivered worksheets and blocks are not retrofitted. | Principal / Claude |
| v1.15 | 2026-07-29 | **Vocabulary Writing section standard on all HW worksheets (Principal, project-wide).** New **§3.16**: every HW worksheet across all five classes ends with a **Vocabulary Writing** section — 5–6 words drawn from the class's own File 2 released-week batch (cumulative-release model), distinct across a block's HWs, presented as a boxed English **Word Bank** above a **blank two-column table** (*English Word* | *বাংলা অর্থ*), one row per word, no prefilled cells. The student copies each English word and writes its Bangla meaning; both columns are student-written, practising spelling and meaning together. **Unmarked practice**, teacher-checked, excluded from the HW mark total; placed after all marked parts. Bangla here is student-produced learning content (§3.14), so worksheet instructions remain English-only; File 2 is not amended. **Governance source: PD-015** (Curriculum Design Decision Log). Directed during the C4 Block 5 (Adjective + Pronoun) build, after the section was added to that block's HWs and the Principal made it a drive-wide standard; C4 Block 5 is the first compliant block. Forward-only per Charter §K.3 — delivered/frozen HWs are not retrofitted. | Principal / Claude |
| v1.17 | 2026-08-02 | **Two-week block shape + `a`/`b` block-half qualifier (Principal, project-wide).** **§7 (3.11) ID grammar** extended to `C{class}B{block}[{half}]-{CODE}[{day}][-W{week}]`: a new optional lowercase **`a`/`b` half-qualifier on the block token** supports a **two-week split-block authored as two master files** (`C2B06a-CW1`, `C2B06b-PT`). The half-letter qualifies the block, it does **not** create a new block — both halves anchor to the same spine block number, preserving the 2026-07-19 "anchor is the block" ruling (that note extended with an explicit half-qualifier clause). A block uses **either** the half-qualifier (two-master build) **or** the `-W{week}` PT suffix (single-master build), never both. **§6.7 Shape variants** gains a **two-week block (8-day, PT per week)** entry: 4+4 class-days across two teaching weeks, each week a self-contained half with its own Thursday PT and fresh vocabulary batch and a marked seam; authored as one master (`-W1`/`-W2` PTs) or two masters (`a`/`b`) where the halves carry distinct grammar and warrant separate audit surfaces — distinct from the *paired-week block* (2+2 sharing one assessment). **Governance source: PD-025**, raised on the C2 Block 6 build (verbs + be / have-has), the drive's first two-week block, built as two masters `C2B06a` (W5) and `C2B06b` (W6) with one PT per week. Forward-only per Charter §K.3. | Principal / Claude |
