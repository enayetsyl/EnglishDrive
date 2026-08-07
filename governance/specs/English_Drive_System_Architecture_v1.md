# English Skill-Building Drive — System Architecture (Reconstructed)

**Document type:** Technical reference — reconstructed system architecture.
**This document is NOT the Project Charter and NOT the Run Book.** It is the evidence base both will be built from.
**Basis:** cross-referenced analysis of every surviving Drive Plan (File 1), vocabulary artefact (File 2), the Block-Build Spec, all completed Build Blocks (File 3) for Class 3 plus Block 1 for Classes 1/2/4/5, ten Half-Yearly/Annual exam papers across five classes, and the Skeleton / TG-Reconciliation / Stability Report build-input files.
**Method:** every claim below is tagged **Observed** (stated or directly demonstrable in a surviving file), **Inferred** (not stated, but strongly implied by consistent evidence), or **Unknown** (cannot be determined from what survives). Where a claim rests on a single data point rather than a cross-checked pattern, that is noted explicitly.

---

## 0. What this document is for

This is the map of the machine, not the machine's rulebook. The Charter will state *what the rules are*; the Run Book will state *how to operate the machine*; this document states *what the machine's parts are, how they connect, and how they've actually behaved* — so that both later documents are built on a shared, evidenced understanding rather than on assumption.

---

## 1. Artefact hierarchy

**Observed**, assembled from the "built against" citation chain that every surviving File 1/2/3 document carries in its header.

```
English_Drive_Project_Charter (vX)                    ← project-wide policy, ROOT
        │
        │  binds every class
        ▼
Class N Drive Plan (File 1)                            ← per-class application of the charter
        │
        ├──► Class N Vocabulary Pool + Batch Order      ← File 2, "build input" for File 3
        │        (per-class; POS-tagged, lead-time-solved)
        │
        └──► Class N Block-Build Spec                   ← File 3 format constitution
                 (C3 only, formally; other classes mirror C3's Spec directly)
                        │
                        ▼
                 Class N Grammar Block 1…M (File 3)      ← the teaching artefact
                        │
                        ├─ Block-at-a-glance / checklist / Clue Card
                        ├─ Class 1–4 (or Session 1–5) teacher script
                        │     └─ Classwork + Homework worksheets (each with an answer key)
                        ├─ Thursday take-home test
                        ├─ Bloom-ladder reference
                        └─ Free-thinking (self-try) rubric


BINDING, EXTERNAL TO THE HIERARCHY (not authored by the Drive, but govern it):
  • NCTB textbook + Teacher's Guide (per class)
  • Half-Yearly + Annual exam papers (per class) — school-authored, binding on §7

BUILD INPUTS (authored by a separate, earlier initiative; consumed, not owned, by the Drive):
  • Class N Skeleton (REF-05) — 10-year stability-tagged curriculum map
  • Class N TG-Reconciliation — book↔TG↔exam coverage audit
  • Class N Stability Report — the underlying 10-year corpus analysis
  • LOCKED_REF-18 Bloom's Daily-Use Pocket — shared cross-project Bloom reference

INFORMATIONAL ONLY, NOT REQUIRED IN THIS PROJECT (per standing operating rule):
  • Cross-class progression maps (REF-19, REF-03)
```

**A second, separate hierarchy exists and must not be confused with the above (Observed, Section 4 of the prior evidence pass):** the Skeleton / TG-Reconciliation / Stability Report files are themselves outputs of a **different, formally-numbered initiative** — "Project 00 / 01 / 02 / 03" — governed by a document called `Instructions`, with its own dependency-ID system (`D-PROJ00-0XX`), its own REF-numbered artefacts (REF-01 Curation Policy, REF-02 Session Map, REF-03 English Spine, REF-05 Skeleton, REF-06, REF-19), and its own propagation infrastructure (`PROJECT00_README.md`, `PROJECT00_CROSS_PROJECT_INDEX.md`). The English Drive **consumes three of that project's outputs as build inputs** and nothing more. `Instructions` is not a prior name for the Charter, and the Project 00–03 apparatus is not part of what the Run Book needs to describe. This boundary is drawn explicitly in the Drive's own operating rules ("cross-class progression maps are informational only and need not be in the project") and is corroborated independently from the Project-01 side (the TG-Reconciliation files route curation findings *outward* to "Project 02 / REF-01," never inward).

---

## 2. Purpose of each artefact

**Observed**, drawn from each artefact's own stated self-description.

| Artefact | Carries | Purpose |
|---|---|---|
| **Charter** | Project-wide policy: spine order, book-boundedness, vocabulary-first reuse, Bloom bands, values alignment, retention gate, rubric definition, calendar cap | The non-negotiable rulebook every class's Drive Plan applies. Wins on any conflict with any other document. |
| **Drive Plan (File 1)** | The charter's rules *applied* to one class's actual book/TG/papers: depth caps per grammar rung (§2), drive parameters (§3), week-by-week schedule (§4), vocabulary reuse base (§5), Bloom application (§6), exam-format map (§7), New Word Routine staging (§8), self-try rubric (§9), house-style notes (§10) | States *how far* and *in what order* this class's grammar teaching may go, and *what format* each block's practice must take to mirror the school's own exam. |
| **Vocabulary Pool + Batch Order (File 2)** | POS-tagged word inventory (Pool) + weekly release schedule (Batch Order) | Guarantees every graded grammar item in File 3 uses a word the student has already been taught and tested on — the mechanism that makes "vocabulary-first, grammar-reuse" enforceable rather than aspirational. |
| **Block-Build Spec** | The document skeleton, scripting conventions, worksheet/answer-key conventions, hard constraints, and a consistency checklist, extracted from the validated pilot block | The *format constitution* for File 3 — not policy, a description of how a compliant block is shaped. "Sits under the charter." |
| **Build Block (File 3)** | One teaching week: 4 scripted classes + homework + Thursday test + answer keys + rubric | The actual classroom-facing teaching artefact. The unit teachers run from directly. |
| **Worksheets (Classwork/Homework, embedded in each Block)** | Graded practice items in the school's exam format, using only held vocabulary | The practice vehicle; homework (not class time) is the primary practice channel per the locked schedule. |
| **Thursday test** | Four parts: spelling/dictation (parent-assisted) · exam-format item · classify-by-role · self-try | The weekly retention checkpoint that feeds the pacing decision for the following week. |
| **Exam papers (HY, Annual)** | School-authored, external | **Binding** on Drive Plan §7 — the format the school actually tests in, which all graded practice must mirror. |
| **Skeleton / TG-Reconciliation / Stability Report** | 10-year curriculum stability tagging, book↔TG audit, and the underlying corpus analysis | **Build inputs** — context and traceability (e.g. "book anchor: Unit 5, p.72") for block builders; not binding, not authored by this project. |

---

## 3. Dependencies between artefacts

**Observed.** Every File 1/2/3 header states an explicit build-against chain, and the chain is always the same shape:

> `Charter (version) → Drive Plan (version) → Spec (version, where cited) → format-mirror block (the most recently validated sibling)`

Two structural rules emerge from tracing this chain across every block:

1. **Format-mirror always points to the newest validated sibling, not just to Block 1.** Block 9 mirrors Block 1 *and* Block 8; Block 10 mirrors Block 1 *and* Block 9. Conventions accumulate transitively rather than being re-derived from a single root each time.
2. **Cross-class dependency runs through Class 3, not through each class's own (often-absent) Spec.** Because only C3 has a maintained Block-Build Spec, C4 and C5's Block 1 headers cite `C3_ENG_BlockBuildSpec_v6.md` and the validated `C3_ENG_Block01_Word_v9.md` directly, skipping their own class's incomplete Spec chain. **C3 is the load-bearing reference for the entire project, not just for its own class.** (Inferred consequence, Observed citation pattern.)

**File 2 is a hard dependency of File 3, not a soft one (Observed).** C5's own Drive Plan log states plainly that without File 2, "§3 ramp / §4 fresh-batch / §5 reuse base are provisional" — meaning no File 3 block can be honestly finalised until its class's Pool + Batch Order exists. Correct build order is therefore: **build inputs → Drive Plan → File 2 → Spec (if absent, borrow C3's) → Block.**

**The Spec is a *described* dependency that is not always a *live* one (Observed, and worth flagging as a system property rather than a defect).** Blocks 6 through 14 explicitly self-report that the Spec was never updated to reflect their conventions ("Spec stale... Blocks 3–9 conventions remain unfolded"). The actual mechanism holding block-to-block consistency together in practice is **direct imitation of the previous block file**, not consultation of the Spec document. The Spec is best understood as a *snapshot description* of the convention as of Block 5, not a live-governing document past that point.

---

## 4. Information flow — planning to classroom delivery

**Observed**, reconstructed as a pipeline from the version-log forensics across all completed blocks:

1. **Book + TG + binding exam papers** establish what a class's students are actually taught and tested on.
2. **Drive Plan §2** converts this into a depth-capped grammar spine (never past what the book/papers actually use), and **§7** maps each rung to the exact exam-question format it must mirror.
3. **File 2** is built once per class: extract candidate words from the book's units → deduplicate (word held once, at first-taught unit) → POS-tag → curation-screen at source (excluded rhymes/festivals never enter the batch) → assign a `Home Grammar Block` + lead-time-solve the release schedule so every word is held at least one week before its block needs it → validate pool-count = batch-count exactly.
4. **The Block-Build Spec** (or, absent that, the most recent validated block) supplies the document shape a new block must take.
5. **A Build Block is authored** to satisfy: its Drive Plan §2 cap, its §7 exam-format anchor, only File 2's already-held words for graded items, the charter's values/guardrail constraints, and the Spec's worksheet/scripting conventions — then it goes through the versioning lifecycle in Section 6 before being considered final.
6. **The teacher delivers the block** in the classroom using the scripted করণীয় / শিক্ষক বলবেন–প্রত্যাশিত উত্তর format across four (or five) classes, assigning homework nightly.
7. **Students sit the Thursday take-home test**, parent-assisted for dictation.
8. **The teacher marks it the following Sunday** and applies the retention gate — which sets File 2's *next* batch size. This closes the loop back into step 3 for the following week.

---

## 5. The feedback loop — exams back into the Drive

This is where the system is most alive, and where the clearest evidence of deliberate engineering exists.

**5.1 The weekly retention loop (Observed, stated identically in at least three independent files).** Thursday class average ≥80% → ramp the next batch up; 65–79% → hold; <65% → shrink and re-teach. This is the shortest feedback loop in the system — week to week, entirely internal to File 2, requiring no document changes.

**5.2 The "map-then-decide" loop — a built block forcing a plan correction (Observed, repeated pattern, named explicitly in Block 5's log).** When a binding paper tests something the book doesn't teach, the resolution path is: build evidence surfaces during a block build → flagged in that block's own version log, attributed to a Principal ruling → the Drive Plan is version-bumped to match (e.g. Gender's four-category cap, Preposition's added `to`) → a propagation note names which other classes' equivalent blocks need the same treatment. **The artefact built downstream is allowed to correct the plan upstream of it** — a genuine, repeated inversion of the nominal Charter→Plan→Spec→Block hierarchy, and one the system tolerates by design rather than by accident (every instance is logged, reasoned, and attributed).

**5.3 The reverse channel — recommending the *exam* change, not the curriculum (Observed, C2 precedent).** Where a paper tests materially beyond a class's book/TG readiness, the Drive Plan can log an **"exam-revision recommendation to the school"** rather than teaching upward to meet it (C2 §7: noun gender, irregular-plural lists, pronoun-cloze density, common/proper sorting). This is a real, evidenced third option alongside "teach more" and "accept the gap" — the system pushes back on the exam when appropriate rather than always deferring to it.

**5.4 The combined-binding-papers policy (Recommended in this session, now Observed as already-standard practice elsewhere in the project).** A new exam year does not retire the previous one; all binding papers (HY prior year, HY current year, Annual) remain simultaneously binding, and §7 is a **union**, not a replacement. Re-checking the evidence base: C1, C2, and C4's Drive Plans were *already* built this way before this session's clarification — C3's plan was the outlier, built against only two papers. The clarification therefore corrected the pilot to match a policy the rest of the project already followed, rather than introducing a new one.

**5.5 The delivered-content lock (established this session; Observed as a real constraint going forward, not yet reflected in any file).** Once a block has been taught, it is treated as **frozen** — new evidence from exam mapping must be absorbed downstream (in a later block, or in File 2's batch scheduling), never by rewriting delivered content. This is a genuinely new operating constraint not evidenced anywhere in the surviving files prior to this project — it reflects the practical reality of a live classroom deployment that the original, possibly pre-launch, build artefacts didn't yet have to account for. **This is the one place in this document where the described system behaviour is prescriptive going forward rather than reconstructed from the past.**

---

## 6. Versioning and review process

**Observed**, reconstructed from version-log forensics across eleven independently-built block files. A consistent five-stage lifecycle recurs:

1. **Initial build (`v1`)** — cites its Drive Plan version + format-mirror block; declares topic, §2 cap, exam anchor(s), book anchor (unit/page), dual-job word, held-word scope, values guards, worksheet-size formula, and states answer keys were "verified programmatically."
2. **Volume pass** — worksheet item counts increased to a fixed formula (`30/15/15 = 60` per sheet in the standard case), keys regenerated and re-verified.
3. **Register/consistency pass** — project-wide wording standardised across files (e.g. "পাকা নিয়ম" → "নিশ্চিত নিয়ম" swept across every block that used it; a Dhaka→Sylhet localisation swept the same way), evidence of a cross-file sweep rather than a local fix.
4. **Named content-audit pass** — a scan for one specific violation class, logged by exact worksheet-cell coordinate (a "past-tense audit," a "do-not-repeat audit" against prior blocks' names/scenarios).
5. **Principal ruling entries** — scope or cap decisions explicitly attributed to the Principal by name, distinct from editorial passes, each logged with its reasoning and a propagation note.

**The version log is a universal, non-optional element** — present, in the same four-column shape (`Version · Date · Change · By`, or a three-column variant), in every Drive Plan, every Spec, and every Block without exception.

**A supersede convention governs document retirement (Observed, stated explicitly in the Stability Report and independently in the TG-Reconciliation files):** a superseded version moves to `/archive/`; the successor states what changed and why, but nothing is silently deleted or overwritten.

**One naming caution (Inferred):** filenames ending `v1__1_` or similar (seen in C1 and C5's Block 1 files) do not correspond to any version number stated inside the file — these read as upload/download filename-collision artefacts, not authored version signals, and should not be treated as evidence of a real `v1.1`.

---

## 7. Propagation workflow for curriculum changes

**Observed, assembled from repeated identical language across the TG-Reconciliation files and independently corroborated by the block-level propagation notes:** when new evidence requires a change, the system's default is **stage, don't auto-apply**.

The recurring ordered pattern:

1. **The triggering evidence is identified** — a new paper, a built block surfacing a book/paper mismatch, or (as of this session) a Principal ruling.
2. **The directly affected artefact is flagged first**, in its own version log, with the specific change named.
3. **The next artefact up the dependency chain is version-bumped to match** — a Block forces a Drive Plan §2/§7 edit; a Drive Plan edit is checked against the Spec (though the Spec update is, in practice, the step most often deferred — see Section 3).
4. **A propagation note is written naming every other class's equivalent block/file** that will need the same treatment, without applying it there yet.
5. **Timing is an explicit, separate decision, reserved for the Principal**: apply now, or batch this change together with other pending ones for one all-class fold-in later. This staging language — *"apply-now-vs-TODO is the Principal's call per item"* — recurs verbatim across at least five independent files (both inside the Drive's own blocks and inside the separate Project 01 TG-Reconciliation files), which is strong convergent evidence this is a genuine, deliberately-held house convention rather than a coincidence of phrasing.
6. **The delivered-content lock (Section 5.5) now adds a hard constraint at step 3–4** for any class whose relevant block has already been taught: the propagation target for that class shifts from "the block itself" to "the next block downstream, or File 2's batch schedule" — the change still propagates, but its landing point moves.

**What this workflow does *not* guarantee (Observed as a real gap, not assumed):** flags raised at step 2 are not reliably swept up. C3 Block 10's "charter §E edit pending" flag was still open, unresolved, three block-builds later. The propagation workflow's weak point is not the logging — the logging is thorough and consistent — it is the **absence of a forcing function that guarantees a flagged edit is eventually applied.**

---

## 8. Project-wide rules vs. class-specific implementation

**Observed**, separated by checking which rules are stated identically across every class's documents versus which vary by class.

| Rule / mechanism | Scope | Evidence |
|---|---|---|
| Retention gate thresholds (≥80 / 65–79 / <65) | **Project-wide, verbatim-identical** | Stated in the same numbers in C1's pool, C3's pool, and C3's batch order independently. |
| Book-bounded teaching (never past what book/papers use) | **Project-wide** | Stated as a charter-level rule in every Drive Plan's pre-flight checklist. |
| Cumulative spine order (Word→Sentence→...→Composition) | **Project-wide concept** | Present in all five classes' block sequencing. |
| **Which rungs exist, and in what count** (C1: 10 blocks; C2: 11; C3: 14; C4: 16) | **Class-specific** | Each Drive Plan §2 derives its own spine length from that class's actual book content — C2's is deliberately shorter because the C2 book is "pre-grammatical." |
| Bloom band definitions and per-class dominant levels | **Project-wide reference (REF-18), class-specific application** | The REF-18 pocket's §4 table gives one fixed band per class; each Drive Plan cites its own row and climbs within it. |
| Salafi/athari values + house style guardrails (sacred-word guard, non-mahram pairing screen, no music/festivals) | **Project-wide** | Identical language recurs in the charter-derived hard-constraints section of every Spec/Drive Plan; the sacred-word and mahram guards appear consistently once any block starts authoring narrative content, in any class. |
| Self-try rubric point value (12-mark) | **Mostly project-wide, one documented exception** | 12-mark in C3/C4/C5; **C2 uses an 8-mark rubric** — an explicit, stated class-specific delta on an otherwise shared mechanism. |
| Dual-job staging *mechanism* (one tracked value-positive noun↔verb pair, advancing block to block) | **Project-wide mechanism** | Same rule, same constraints (base/imperative form, no verb-s collision) in every class that has reached a block needing it. |
| The specific dual-job *word sequence itself* (help → rain → place/hand → exercise …) | **Class-specific** | Each class's word sequence is drawn from its own File 2 pool and schedule. |
| Worksheet-size formula (30/15/15 = 60) | **Observed as C3-wide from Block 3 onward; Inferred, not confirmed, as project-wide** | Not yet independently verified in a completed C1/C2/C4/C5 block beyond Block 1 (which predates the formula's introduction). |
| W1–W7 fresh-vocabulary window, then consolidation | **Observed as invariant across all five classes' File 2 artefacts** | Could plausibly be coincidence of book size rather than a stated rule — flagged as **Inferred**, not confirmed as a named charter clause. |
| Delivery register (Bangla-medium, bilingual) | **Project-wide**, with one class-specific structural variant | All five classes deliver bilingually; **C1 alone uses a distinct "Session" unit + fixed Track-A oral drill + five-step New Word Routine**, appropriate to its younger age band, versus C3's four-class/three-step pattern. |
| "First-teach" vs. "cumulative re-walk" framing of Block 1 | **Class-specific, but for a structural reason, not a stylistic one** | C3 re-walks because it assumes prior Drive exposure; **C4 and C5 explicitly declare "first-teach"** because this is the Drive's first year running in every class simultaneously — there is no prior Drive-taught cohort for them to re-walk. |

---

## 9. Remaining unknowns

Organised by what they block.

**Blocking a faithful Charter reconstruction:**
- The charter's literal wording for any section. Section *content* is now well-evidenced for §C (duration/3-month cap), §E (grammar inventory + the map-then-decide exception path), §F (book-bounded vocabulary + retention gate), §G (Bloom bands), §H (curation-adjacent exclusions), §I (self-try rubric) — but no verbatim text survives for any of them.
- **Which charter version is authoritative.** The corpus cites v1.0 (your original instruction), v1.1 (C3 Spec), v1.2 (C2/C4), and a staged v1.2→v1.3 patch (C5), with no way to determine which section-level rulings belong to which version. A reconstruction is necessarily a **composite of the latest known ruling per section**, not a snapshot of any one real version.
- Whether "map-then-decide" and the "exam-revision recommendation" mechanism are literally named charter clauses, or informal project vocabulary that happens to recur.
- The still-open charter §E / Block 10 conflict (Drive Plan v1.2 widened verb scope; no confirmation charter §E was ever edited to match).

**Blocking a faithful Run Book reconstruction:**
- Whether a Run Book ever existed as a distinct document, or whether everything attributed to it (build workflow, kickoff line, checklist) lived entirely inside the Block-Build Spec and the builders' working memory.
- The exact mechanism behind the "do-not-repeat" cross-block audit (referenced once, in Block 7's log, as something that was run — never itself surviving as a file).
- Whether the per-block five-stage lifecycle (Section 6) was an explicit template someone filled in each time, or an emergent habit from imitating the previous block.

**Open curriculum decisions, not resolvable from evidence alone (need a Principal ruling, already flagged in this session):**
- C3 Block 4: whether `advice`/`news` become a graded exception set or a documented accepted gap.
- Spine placement for the new affirmative↔negative transformation content (Block 2 companion vs. Block 10 companion).
- C1's Annual Q2 vocabulary gap — fix path agreed (File 2 batch, delivered from Block 2 onward) but not yet built.

**Structurally unresolvable from what survives:**
- **C5 has no Annual paper and no File 3 build yet.** Its exam map cannot be completed, and nothing in this document should be read as covering C5 beyond File 1/File 2.
- **C1's internal three-way block-numbering contradiction** (pool sheet 2's 13-block fossil spine vs. the 10-block spine in the current Batch Order and Drive Plan). The Drive Plan's 10-block spine is being treated as authoritative in this document because it's corroborated by the standalone Batch Order file and because the Drive Plan explicitly narrates *why* Article was dropped and Preposition demoted — but no file confirms this resolution was ever formally recorded as a decision, only that later files behave as if it were.
- The full content of `Instructions` and the Project 00–03 apparatus — confirmed out of scope for this Drive's Charter/Run Book, but its exact boundary rules (what exactly Project 03 is permitted to do with Drive outputs, for instance) remain genuinely unknown and, per the project's own stated scope, likely don't need to be known.

---

## Appendix — glossary of recurring terms (Observed)

| Term | Meaning |
|---|---|
| File 1 / File 2 / File 3 | Drive Plan / Vocabulary Pool+Batch Order / Grammar Blocks — the three-file structure repeated per class |
| ধাপ | "Step" — the numbered sub-unit of a class's teacher script |
| করণীয় | "To-do" — the teacher's physical action, scripted line by line |
| শিক্ষক বলবেন / প্রত্যাশিত উত্তর | "Teacher will say / expected answer" — the two-column discovery-dialogue table format |
| ভূমিকা / পদ | "Role" — the umbrella term for a word's part of speech; কাজ/ক্রিয়া reserved for Verb specifically |
| CW / HW | Classwork / Homework worksheet, followed by class number and ক/খ/গ (part a/b/c) |
| Dual-job | A word introduced in one grammatical role that is shown (or later practiced) in a second role — tracked as a single, staged resource across blocks |
| Held word | A vocabulary item already released in File 2's batch schedule as of the current week — the only kind of word permitted in a graded item |
| Map-then-decide | The resolution path used when a binding exam tests content the book doesn't teach: surface it, flag it, get a Principal ruling, widen the cap if approved |
| Retention gate | The ≥80/65–79/<65 Thursday-test threshold that sets the following week's new-vocabulary batch size |

---

*This document synthesises the full evidence trail assembled across the reconstruction project's prior phases: initial system understanding, File 2 and exam-paper integration, Build Block reverse-engineering, and the Annual-paper/combined-binding-policy/Block-1-freeze revisions. It supersedes no prior analysis in this conversation — it consolidates them.*
