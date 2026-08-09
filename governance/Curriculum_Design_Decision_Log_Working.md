# English Skill-Building Drive — Curriculum Design Decision Log (Working)

*This is the working log, not the final official version. It reflects decisions confirmed and approved in the working-notebook chat as of 01.08.26. Items still under discussion, unconfirmed, or explicitly parked are noted at the end but not treated as decisions.*

---

## Project Decisions (PD)

Decisions already adopted and applied across the English Drive.

### PD-001 — Add reteaching to the Drive Plans
**Decision:** Add structured reteaching of previous topics instead of relying mainly on revision.
**Why:** Students need guided practice before learning new grammar.
**What led to this:** While rebuilding the Drive Plans, it became clear the previous plans mainly revised old topics instead of reteaching them. Classroom experience also showed many students needed guided reteaching before learning new grammar.
**Affected files:** All class Drive Plans, Block Specifications, Lesson Plans, Teacher Runbooks.
**Status:** Applied

### PD-002 — Thursday Assessment (Home Test → Performance Test)
**Decision:** Change Thursday from a Home Test to an in-school Performance Test. Students also receive a separate weekend take-home assignment sheet, as part of the same assessment workflow — not a separate decision.
**Why:** This matches the school's current assessment system.
**What led to this:** The school changed its weekly assessment system from a Home Test to an in-school Performance Test; the weekend assignment sheet was added as part of the same workflow change.
**Affected files:** All Drive Plans, Weekly Routine, Block Specifications, Worksheets, Teacher Runbooks, plus a new assignment-sheet artifact per block (format still being designed).
**Status:** Applied (Thursday test format); assignment-sheet format still in progress.

### PD-003 — Improve the curriculum using classroom evidence
**Decision:** Make curriculum changes based on classroom experience, teacher feedback, student performance, and assessment results.
**Why:** Many curriculum improvements only became clear after teaching the lessons.
**What led to this:** This is a standing project policy, not tied to one event. During reconstruction, many improvements came from classroom teaching, teacher feedback, and observing student performance rather than from planning alone.
**Affected files:** Project-wide — guides future curriculum development rather than one specific file.
**Status:** Applied

### PD-004 — Use Mohammadpur question analysis
**Decision:** Use lessons from the Mohammadpur question papers to improve teaching, worksheets, and assessments.
**Why:** The papers highlighted areas where the curriculum could be improved.
**What led to this:** Reviewing the Mohammadpur question papers as a whole (not one single question) showed opportunities to improve question quality, curriculum sequencing, and assessment design.
**Affected files:** Drive Plans, Worksheets, Performance Tests, Block Specifications.
**Status:** Applied

### PD-005 — Flexible block pacing
**Decision:** Not every block needs one week. Some blocks may take a full week, while lighter blocks can share a week.
**Why:** Different topics need different amounts of teaching and practice.
**What led to this:** While rebuilding the Drive Plans, some blocks became heavier because of reteaching, self-construction activities, and better progression. Other blocks were lighter. Giving every block exactly one week was no longer practical.
**Affected files:** All Drive Plans.
**Status:** Applied

### PD-006 — Keep vocabulary in sync with the curriculum
**Decision:** Whenever block order changes, update the Vocabulary Pool and Weekly Vocabulary Batches.
**Why:** Vocabulary should always match the grammar progression.
**What led to this:** Whenever the block sequence changed during reconstruction, the Vocabulary Pool and Weekly Vocabulary Batches had to be updated to stay aligned with the grammar progression.
**Affected files:** Vocabulary Pool, Weekly Vocabulary Batch Order, Drive Plans for all classes where block sequencing changes.
**Status:** Applied

### PD-007 — Better assessment questions
**Decision:** Design questions that test real understanding instead of predictable or memorised answers.
**Why:** Students should learn to think and use English, not only remember answer patterns.
**What led to this:** Reviewing earlier worksheets, assessments, and the Mohammadpur papers showed that some questions encouraged predictable or memorised answers instead of checking real understanding.
**Affected files:** Worksheets, Performance Tests, Block Specifications.
**Status:** Applied

### PD-008 — Anti-pattern answer ordering
**Decision:** All exercises in every grammar block must be ordered so correct answers don't follow a predictable pattern. Refined specification: no adjacent same-answer repeats, no repeating cycle, and run-length capped at ≤2 with no strict alternation (e.g., no clean ABAB… cycle for 2-label sets). Enforced mechanically; type/category balance preserved; answer keys regenerated and cross-checked against the shuffled order.
**Why:** Students could pattern-match answers instead of reading and understanding each question. Strict alternation was found to be its own kind of guessable pattern.
**What led to this:** Surfaced during the Class 5 Block 2 build, where exercises originally followed a predictable cycle and had to be reordered. Refined during the Class 5 Block 3 build after a hand-count slip (6/5/7) was caught programmatically.
**Affected files:** All grammar block worksheets and answer keys, all classes.
**Status:** Applied

### PD-009 — Grammar Exemplars are not vocabulary
**Decision:** A small, fixed set of words whose only purpose is to demonstrate a grammar rule is classified as **Grammar Exemplars**, not vocabulary. Grammar Exemplars are exempt from held-vocabulary restrictions. They must be taught explicitly during instruction and may appear in Clue Cards, teacher modelling, guided practice, CW, HW, Performance Tests and Assignments — including as graded answers — but they are never added to the Vocabulary Pool, never counted as fresh or held vocabulary, and are never vocabulary-learning targets (no dictation or spelling items). The exemplar list stays fixed and minimal, and is used only where the Drive Plan cap or a binding exam anchor requires it. Curation screening and the sacred-word guard continue to apply in full. The first application is the Article block's sound-exception words (*university, one-taka/one-eyed, hour, honest, M.P., excellent, eagle, historic*) and the minimal proper-noun examples used for the zero article (*Cox's Bazar, Dhaka, Sylhet, Bangladesh*).
**Why:** These words exist to demonstrate a rule, not to build lexical knowledge. A student answering *an hour* is being graded on hearing the opening sound, not on knowing what an hour is. Holding them to the held-vocabulary rule would make the rule itself untestable while protecting nothing.
**What led to this:** Surfaced during the Class 4 Block 4 (Article) build. The Drive Plan §2 cap requires teaching a fixed sound-exception list plus zero article for proper nouns, and all three binding papers (HY25 Q2, HY26 Q7, Annual Q3) test exactly those cases. None of the exception words were held by W4, and the Pool excludes proper nouns at source — so the whole graded surface of the block was unbuildable under the held-word rule. Three options were weighed: expanding the Pool, grading below the exam, or exempting the exemplars. The exemption was ruled in as the only route that preserves both curriculum fidelity and exam fidelity without inflating a fresh batch that already carried a 33-word spike at W3. Alignment note: the Pool already excludes function words at source because they are grammar targets; this decision applies the same logic one step further.
**Affected files:** Run Book §5.7 (operational rule), §6.5 and §6.8 (held-word audit carve-out). Project-wide rule — applies to all Article blocks (C2 Block 3, C5, and C1 if Article enters that spine) and to future grammar topics with the same structure. Vocabulary Pools and Batch Orders are **not** modified. Existing finalized blocks convert forward-only (Charter §K.3).
**Status:** Applied

### PD-010 — Self-construction rubric: 4 marks, value alignment not scored
**Decision:** The self-construction (self-try) rubric is **4 marks — four criteria at 1 mark each: Content accuracy, Reasoning, Organisation, Correct word-class placement — uniform across all five classes**, replacing the previous 10/10/12 ladder. **Islamic/value alignment is removed as a scored criterion, project-wide, for the time being.** Charter §H continues to bind every authored artefact in full without exception. It does not extend to scoring student responses: a religiously neutral, on-topic answer earns full marks; value content is required only where the question itself asks for it; and a response conflicting with §H is flagged and corrected as a values matter, never marked down as a language or content error. Criteria score 1 or 0 — no partial credit at this total. Criterion substitution remains available within the fixed 4-mark total (Charter §I.5), but value alignment is not available as a substitute.
**Why:** Scoring value alignment on open student production directly contradicted Run Book §13.1, which already directed that value content be required only where the question asks for it — the block-level rubric was awarding 2 marks for something the marking guidance said not to score. The ruling resolves a standing contradiction rather than introducing a new position. The 12-mark total also overweighted a short production task within a Performance Test: in C4 Block 4 it was 12 of 55 marks for a four-line task.
**What led to this:** Surfaced during the C4 Block 4 (Article) build, when the Principal specified a four-criteria, 1-mark-each rubric with value alignment removed. Flagged as a Charter conflict before application (Charter §I set 10/10/12); the Principal ruled the change project-wide rather than block-scoped, and confirmed uniform criteria across all five classes rather than each class retaining its own set.
**Affected files:** Charter §I.3, §I.4, §I.5 and §G.5 (v1.2 → v1.3). Run Book §13.1 (v1.12 → v1.13). All five Drive Plans §9 — C1 v1.13 (both §6 and §9c statements), C2 v1.7, C3 v1.6, C4 v1.9, C5 v1.4. **Class 1 gains** a word-class-placement criterion it did not previously carry, judged by correct use rather than by naming the class. **Class 2 loses** its Neatness & sentence-mechanics criterion, and with it the open-items question about that criterion's relationship to Organisation. Every Performance Test carrying a self-try falls by 6 or 8 marks. Delivered blocks convert forward-only (Charter §K.3).
**Status:** Applied

### PD-011 — Vocabulary override for exam-anchored words
**Decision:** Common, age-appropriate, exam-anchored vocabulary may be introduced in a block though absent from the Vocabulary Pool (File 2), provided it is taught explicitly (meaning, pronunciation, reading, spelling), staged across the week, counted toward the week's taught-vocabulary load, and used in graded items only after teaching. This is limited to common, age-appropriate, exam-anchored vocabulary; it is **not** a licence for unrestricted vocabulary expansion. **Distinct from Grammar Exemplars (PD-009 / Run Book §5.7):** override words **are** spelling-eligible and are counted as taught vocabulary; exemplars are neither. **Distinct from Block-local teaching words (PD-012):** override words are counted toward the week's taught-vocabulary load as real taught vocabulary and are spelling/dictation-eligible within the week; block-local words are gradeable only inside their own block and are never dictation/spelling items.
**Why:** These words exist because a binding paper tests them and the held pool cannot supply them, but — unlike rule-demonstration exemplars — they are ordinary lexical items a child should genuinely learn (meaning included), so they belong in the taught-vocabulary load and in spelling. Holding them to the held-only rule would make the exam-anchored skill unbuildable while protecting nothing.
**What led to this:** Surfaced during the Class 1 Block 4 (Adjective) build. The Drive Plan §2 cap requires choosing between two adjectives and underlining adjectives in sentences, and Annual-2025 Q4 tests five specific adjective pairs (tall/long, soft/hard, clean/dirty, sweet/sour, weak/strong). The held W1–W4 pool carried exactly one adjective (*good*), not enough for a single two-option item, and the five Annual pairs were unheld. The override was ruled in as the route that preserves exam fidelity without inflating the fresh batch, with the words taught read-and-spell and staged Sun→Tue across the week.
**Affected files:** Run Book (operational rule alongside §5.7). Vocabulary Pools and Batch Orders are **not** modified — the override is a build-time admission, flagged forward-only for File 2 reconciliation. Applies to all classes where a binding paper anchors common vocabulary the held pool cannot supply.
**Status:** Applied

### PD-012 — Block-local teaching set (taught-but-not-pooled)
**Decision:** A class may teach exam-required items in-block without entering them in the Vocabulary Pool (File 2). Block-local words are **gradeable within their own block's CW / HW / PT only** (fairness holds locally — nothing graded that was not taught that week); they are **not** dictation or spelling-test items; they are **not** available to later blocks as held vocabulary; and they are **not** in the spaced-revision cycle. This is a word-status the held-vocabulary rule and PD-009 exemplars do not cover: taught in-block, gradeable in-block, not in File 2, not held downstream.
**Why:** Some binding papers test a concept that cannot be established from the held pool at all — e.g. the -es plural rule when no held noun ends in s/sh/ch/x, or the full gender categories when the pool holds only a fragment of the counterpart pairs. The concept (not the individual word's frequency) requires the words; grading them only inside the block that teaches them keeps the fairness guarantee architectural while satisfying exam fidelity, without permanently inflating File 2 or the downstream revision load.
**What led to this:** Surfaced on the C3 Block 5 precedent and applied again at C2 Block 5. C3 Block 5 (Gender) adopted 20 block-local words to complete the four gender categories from the binding papers; C2 Block 5 (Plural) adopted five (*class, watch, box, dress, glass*) to complete the -es rule, the held pool carrying only *grass* (a mass noun). Both were sourced from the binding papers, not the NCTB pool.
**Affected files:** Run Book (needs the operational word-status definition and its audit treatment — see this session's Run Book update). Vocabulary Pools and Batch Orders **not** modified. Applies project-wide wherever a binding paper's concept cannot be built from held vocabulary.
**Status:** Applied

### PD-013 — No cross-year vocabulary carry
**Decision:** Each class is designed independently. Vocabulary and grammar taught in class *C-minus-1* are **not** automatically held or gradeable in class *C*; a concept receives its first explicit instruction at its first spine appearance **within its own class**, regardless of whether an earlier class taught it. A later class does not shift to "revise + extend" merely because an earlier class now teaches a topic — it teaches fresh unless a Principal ruling for that specific block says otherwise.
**Why:** The Drive builds one class at a time against that class's own book, Teacher's Guide, and binding papers. Treating a lower class's coverage as a held baseline would couple every class's build to the others' delivery state and undermine the fairness guarantee (a student who joined at class *C* cannot be assumed to hold *C-minus-1* content). Independence keeps each class's graded scope derivable from its own evidence.
**What led to this:** Ruled during the C3 Block 5 (Gender) build, where the question arose of whether C2's newly-added gender teaching (C2 Blocks 4–5) should make C3 shift from first-formal-teaching to revise-and-extend. The Principal ruled C3 Block 5 remains first formal gender instruction, built on no cross-year carry; C2's gender teaching is not assumed as a C3 held baseline. This resolves the cross-class dependency both the C2 and C3 Drive Plans had flagged.
**Affected files:** Project-wide build principle. C3 Drive Plan §2 row 5 and the C2/C3 cross-class dependency flags (resolved this session). No Vocabulary Pool or Batch Order change.
**Status:** Applied

### PD-014 — Gender category terms are taught, not graded
**Decision:** The gender category terms (*masculine / feminine / common / neuter*) are **taught** across a gender block — students recognise, pronounce, and become familiar with them through an in-class term-practice segment (choral reading, syllable-breaking, board-writing, oral recall) run every teaching day — but they are **not a graded element** on any worksheet or Performance Test. The terms are metalanguage (category names), sitting outside both File 2 (they are grammar terminology, not naming/doing/describing words) and any block-local example set (which are example *nouns*, not category names). **This supersedes an earlier session ruling that made the terms graded spelling objectives.**
**Why:** The graded skill is naming a noun's gender in the paper's find-and-classify format, not spelling the category label. Grading the terms themselves would test spelling of metalanguage rather than the classification skill the binding paper actually assesses, and would add a spelling burden the exam does not carry.
**What led to this:** Ruled during the C3 Block 5 (Gender) build, superseding an earlier same-session ruling that had made the four terms graded spelling objectives. The Principal ruled the terms taught-not-graded; the block runs a named in-class term-practice segment each day but carries no term as a graded item.
**Affected files:** Gender blocks project-wide (C3 Block 5 delivered on this ruling). No Charter, Run Book, or File 2 change required; recorded here as the governing decision.
**Status:** Applied

---

### PD-015 — Vocabulary Writing section standard on all HW worksheets
**Decision:** Every Home Worksheet (HW) across all five classes ends with a **Vocabulary Writing** section. Standing convention, **forward-only**. Specification: (a) **Source** — 5–6 words drawn from the class's own Vocabulary Pool / Batch Order (File 2), from the block's **released-week batch** under the cumulative-release model (words available up to and including the teaching week); each class uses its own pool/batch, no cross-class sharing. (b) **Distinctness** — where a block spans multiple HWs, the word sets are distinct across those HWs (no word repeated between them). (c) **Layout** — a boxed English **Word Bank** listing the words once, above a **blank two-column table** (*English Word* | *বাংলা অর্থ*), one row per word, no prefilled entries. (d) **Task** — the student copies each English word into column 1 and writes its **Bangla meaning** in column 2; both columns are student-written, practising English spelling and Bangla meaning together. (e) **Marking** — **unmarked practice**, teacher-checked for spelling and meaning; excluded from the HW mark total. (f) **Placement** — the final section of the HW, after all marked parts. Applies uniformly to Classes 1-5.
**Why:** Builds retention of released vocabulary through active writing of both form (English spelling) and meaning (Bangla), rather than passive meaning-recall; complements the Thursday PT dictation without adding graded load. Bangla here is student-produced learning content (Run Book §3.14), so worksheet instructions remain English-only.
**What led to this:** Ruled during the C4 Block 5 (Adjective + Pronoun) build, after the Vocabulary Writing section was added to that block's HWs and the Principal directed it be made a drive-wide standard for all future blocks across all classes.
**Affected files:** Run Book gains §3.16 (Vocabulary Writing). Forward-only per Charter §K.3 — delivered/frozen HWs (Block 1 of every class, and any block already built) are **not** retrofitted; new HWs from this ruling onward include the section. C4 Block 5 is the first compliant block. No File 2 or mark-scheme change.
**Status:** Applied

---

### PD-016 — §H.8 living-being imagery override (C1 Block 5 picture-cued worksheets)
**Decision:** For **Class 1, Block 5 (Demonstrative)**, living-being images **rendered without facial features** (no eyes, nose, mouth, or beak; smooth blank heads) are admitted as pointed-object picture cues on the block's picture-cued worksheets, to widen the pointed-object pool and reduce noun/configuration repetition across the block's picture sheets. Principal ruling.
**Conflict recorded (not silently absorbed):** This **contradicts Charter §H.8** as written. §H.8 states "no living-being depictions, per the Curation Policy's **faceless / no-living-being** rule" — facelessness is part of the standard in §H.8, alongside no-living-being, **not** an exemption from it. Admitting faceless living-beings is therefore an **override of the clause**, not an interpretation of it.
**Escalation flag (UNRESOLVED dependency):** Charter **§H.9** names **REF-01** (LOCKED Islamic Curation Policy, owned/revised in **Project 02**) as the canonical values authority, with §H as its Drive-local subset; §H.8's living-being rule traces to REF-01's faceless/no-living-being rule. A Drive-level PD governs how *this* project builds worksheets but **cannot amend REF-01**. If the faceless/no-living-being rule is REF-01-sourced, this override may require **REF-01-owner / Project-02 sign-off** before it is REF-01-compliant. REF-01 is **not present in this project's files**, so its exact wording and scope could not be verified at ruling time. Flagged as an open dependency; **not** resolved by this PD.
**Standing recommendation on record (advisory, does not alter the ruling):** the binding Muhammadpur papers use **no living-being imagery** — the Annual-2025 Q6 pointed objects verified directly are house, trees, eggs, umbrella, bananas (all non-living). The block's noun supply is coverable without living-beings (6 held non-living nouns + PD-012 carriers). The override was adopted at Principal direction to reduce repetition; it is not required for exam fidelity.
**Scope & boundary:** **C1 Block 5 only** unless explicitly extended by a later ruling. Faceless rendering is mandatory for any admitted living-being. Does not license facial features, and does not extend to other classes or blocks.
**Affected files:** C1 Block 5 master + its picture-cued CW/HW worksheets and image specifications. Charter §H.8 carries a **forward-only note** pointing to PD-016 (added this pass). Forward-only per Charter §K.3.
**Status:** Applied (C1 Block 5); **REF-01 escalation OPEN.**
**Status update (2026-08-02, forward-only per §K.3):** **Not exercised in C1 Block 5 as built.** During the C1 B5 build the Word Box was removed (PD-023), which restricted all graded pictures to taught, spellable nouns; as a consequence **all faceless living-being imagery was dropped and no living-being appears on any C1 B5 sheet.** The block therefore does **not** rely on this override, §H.8 is **fully observed** in C1 B5 as delivered, and the REF-01 escalation **no longer gates C1 B5**. This ruling and its REF-01 flag remain on record for any **future** block that elects to use faceless imagery; the escalation stays **OPEN** for that contingency. The original ruling text above is preserved unchanged (§K.3).

---

### PD-017 — Block-local carrier objects for C1 Block 5 picture cues (PD-012 pattern)
**Decision:** For **Class 1, Block 5 (Demonstrative)**, a **block-local carrier set** of pointed-object picture cues is declared under the **PD-012 pattern (taught-but-not-pooled)**: **umbrella, eggs, bananas, door**. These are used **only as picture cues** in the demonstrative naming-frame items (the graded target is the demonstrative *this/that/these/those*, not the noun). They are counted toward the week's teaching load, introduced/named before appearing on a graded sheet, and are **never** graded vocabulary, dictation, or spelling items.
**Rationale:** umbrella, eggs, bananas are exam-attested (Annual-2025 Q6 pointed objects) but absent from File 2; door is a File 2 **W6** word (not yet held at W5) borrowed early strictly as a picture carrier. Declaring them block-local keeps the demonstrative items exam-faithful without breaching held-vocabulary discipline (they are carrier objects, and per the established pattern, carrier words in word-role tasks are not subject to held-vocabulary discipline).
**Boundary:** carrier status is picture-cue only; none enters the Thursday vocabulary PT, the HW Vocabulary Writing section (which draws from the W5 *released batch* per PD-015), or any dictation/spelling list. Held W1–W4 non-living nouns (book, pen, pencil, bag, tree, house) remain the primary graded-item objects.
**Affected files:** C1 Block 5 master + picture-cued worksheets. Forward-only per Charter §K.3.
**Status:** Applied (C1 Block 5).
**Status update (2026-08-02, forward-only per §K.3):** Carrier set **narrowed to {umbrella, egg(s)}**. When the Word Box was removed (PD-023), graded pictures were restricted to taught spellable nouns; **bananas and door were dropped** from the carrier set. Umbrella and egg were retained specifically to carry the "a/an" article items the exam tests (*an umbrella*, *an egg*), introduced orally, with carrier noun spelling not graded — only the demonstrative is. The original ruling text above is preserved unchanged (§K.3).

---

### PD-018 — Worksheet reference blocks must not print worked answers
**Decision:** A **reference block on a student-facing worksheet** (the boxed "The rule" / "Remember" panel above the items) **may print a rule** and **may print an arbitrary learned list** — a closed set the student can only memorise, never derive. It **may not print a worked example of a derivable word the sheet grades**. Applies to all classes and all worksheet types (CW, HW, Assignment); Clue Cards and other wall references are unaffected, as they are not sat with the paper.
**The audit that accompanies it:** every reference block is checked against its own sheet's answer key, with punctuation normalised **on both sides** — box text and item targets. A comma or emphasis marker between an article and its noun is enough to defeat a naive match.
**Why:** A rule box that prints *an hour · a hero · a university* above items grading exactly those words is an answer key, not a reference. The distinction that makes the rule workable is **derivability**: *an hour* is derivable by applying the taught method, so printing it removes the thinking being tested; *the Padma* is not derivable from any taught rule — it is a learned list, and withholding it tests days-old recall rather than reasoning.
**What led to this:** Found on the C5 Block 6 (Article) build by Principal review. HW-1's rule box printed **seven** article+word pairs directly above the parts grading them — **12 of 38 marks were copyable off the top of the sheet**. A first audit pass reported HW-2 clean; re-run with punctuation normalised, HW-2 leaked a further seven. The defect had survived four block versions and the block's own §6.5 audit.
**Affected files:** Run Book gains a §3 subsection stating the rule, with matching lines in **§6.5** (audits) and **§6.8** (pre-finalization checklist), alongside the existing held-word and exemplar lines — the Run Book currently has **no** provision governing reference blocks, which is why this shipped. Forward-only per Charter §K.3: delivered worksheets are not retrofitted.
**Status:** Ruled; applied in C5 Block 6. Run Book edit pending.

---

### PD-019 — Attribution form: attribute the agency, do not restructure the sentence
**Decision:** Where authored material describes a natural phenomenon acting, the required form is **attribution appended to the natural sentence** — *"The sun gives us light **by Allah's Will**"* — **not** a restructuring that moves Allah into the subject position (*"Allah gives us light through the sun"*). Plain description without agency (*"The sun is very far from us"*) remains equally acceptable. Applies to all classes.
**Why:** Same theology, materially lower cost to the student. A child composing freely writes *the sun gives us light* because that is the word order English hands them; a structural correction is forgotten under exam pressure, whereas a three-word addition is a habit that travels. The rule is easier to teach, easier to mark, and easier to apply to sentences the teacher did not anticipate.
**Marking:** unchanged — attribution is a values matter, corrected and never marked down as a language error (Charter §I.3, Run Book §13.1). Value alignment remains unscored (PD-010).
**Interaction with §H.3:** unchanged and unaffected. Allah remains absent from all worksheet, Performance Test and answer-key items; the attributed form lives in teacher script and board work.
**What led to this:** Principal ruling during the C5 Block 6 (Article) build, where the unique-noun set (*the sun · the moon · the earth*) makes the autonomous-giver construction almost unavoidable in student production.
**Affected files:** Charter §H carries no attribution clause — one is needed, or the rule lives only in individual block files. Block teacher-checklists and §6.5 attribution-screen rows adopt the new form as they are next revised. Forward-only per Charter §K.3.
**Status:** Ruled; applied in C5 Block 6. Charter edit pending.

---

### PD-020 — Choosing between the three non-held word statuses
**Decision:** When a block needs a word the held pool cannot supply, the instrument is chosen by **what the word is for**, not by convenience:
- **Grammar Exemplar (§5.7 / PD-009)** — sole purpose is to demonstrate a rule; the child never needs to own the word. **Not counted** toward the week's vocabulary load.
- **Block-local word (§5.8 / PD-012)** — a genuine taught word for the week whose held status is confined to the block. **Counted** toward the week's load.
- **Override word (§5.9 / PD-011)** — real taught vocabulary, spelling- and dictation-eligible from its taught day. **Counted**.

**Load is a decision input, not an afterthought.** Where a candidate word passes the exemplar test, PD-012 must not be used in its place: block-local status adds the word to the week's taught load and can trip the retention gate (≥80% ramp / 65–79% hold / <65% shrink) on a vocabulary count rather than on mastery of the block's actual skill.
**Companion rule — rebuild before widening.** Where a binding paper's item is built on an ordinary unheld word, the **item shape is rebuilt on held words** rather than admitting the word or widening the §2 cap. This is the operative reading of PD-009's anti-drift line, and it preserves both the exam-format drill and the cap.
**What led to this:** C5 Block 6 (Article). PD-012 was proposed and confirmed, then **corrected to PD-009 before drafting**: the ~15 candidate words were rule-demonstrators (*the sun*, *university*, *Headmaster*), and PD-012 would have added them to a week already carrying the ramp's largest fresh batch — 40 words — under a live retention gate. Separately, three HY-25 Morning item shapes (*the west side · the truth · the college road*) were rebuilt on held nouns rather than widening the cap.
**Affected files:** Clarifies PD-009, PD-011 and PD-012; amends none of them. Run Book §5.7–§5.9 may carry a pointer at next revision.
**Status:** Applied.

---

### PD-021 — "Festival" is admissible in Islamic-calendar contexts
**Decision:** The word *festival* and festival contexts are **admissible where the referent is Islamic** — Eid, Ramadan — and remain **excluded** for other-faith festivals. The word is not itself barred; the exclusion attaches to the referent.
**Why:** Charter §H excludes other-faith festival content. Read as a ban on the word, it removes an ordinary held vocabulary item from every class's usable set and forces awkward circumlocution around Eid, which the drive's register otherwise encourages.
**What led to this:** Principal ruling during the C5 Block 6 (Article) build, where `festival` sits in the W3 held batch and its status was ambiguous.
**Affected files:** Charter §H (clarifying note at next revision). Block-level exclusion lists (`team`, `temple`) are unaffected. Forward-only.
**Status:** Applied.

---

### PD-022 — Generic *the* taught-and-produced; the *Quran* article item prepared by secular transfer, never blanked (C3 Block 6 Article)
**Decision (two parts).** **(a) Generic *the* widened into the C3 Article cap.** The binding **HY2026 Q6** tests generic (whole-kind) *the* — *"The cow is a useful animal"*, *"The Quran is a holy book"* — a use the Drive Plan §2 row 6 originally excluded ("specific/unique" only). Since a student cannot answer these items without producing generic *the*, C3 Block 6 **teaches whole-kind *the* as a named third *the* use and grades its production**, restricted to **secular subjects** (*the cow / the ox / the ostrich / the owl*). It is taught at Understand/Apply, not as abstract definiteness theory; the "no abstract definiteness theory" guardrail is preserved by naming three concrete *the* uses (already-named · the-one-we-mean/only-one · whole-kind) rather than teaching a general rule. **(b) The sacred-word *Quran* item is prepared by secular transfer, never blanked.** The HY2026 paper blanks an article on *Quran* (*"___ Quran is ___ holy book"*). Charter **§H.3** forbids the drive to author *Quran* as a fill-in/classification target. These are reconciled by **teaching the transferable pattern on secular subjects** — a student who can do *the cow / the ostrich* can answer the *Quran* item — plus a **marked teacher-script note** allowing the teacher to read the exam sentence reverently in oral preparation. *Quran* appears in no worksheet or Performance Test blank.
**Conflict recorded (not silently absorbed):** This is a **binding-paper vs Charter §H.3 tension** — the exam does something (blank an article on a sacred word) that the charter forbids the drive to reproduce. The exam-first principle governs *scope* (which grammar is taught, how heavily) but does **not** override an explicit §H.3 values guard; the guard is a floor. Resolution is teach-to-transfer, not relaxing the guard. Generic *the* itself is admitted on the same **paper-fidelity / map-then-decide** path already used for Block 5 gender (four categories, Drive Plan v1.4/v1.7) and Block 10 verb (present continuous, v1.2).
**Why:** Preparing students for a real graded exam item without authoring content that breaches the sacred-word guard; and closing the cap-vs-paper gap the original §2 row 6 carried.
**What led to this:** C3 Block 6 (Article) build, 2026-07-26. Principal ruled generic *the* taught-and-produced (secular only) and confirmed the *Quran* secular-transfer + teacher-note method after the tension was surfaced rather than absorbed.
**Affected files:** Drive Plan §2 row 6 and §7 Article note (updated, C3 Plan v1.8). Replicates to Classes 1/2/4/5 wherever the Article block meets the same paper items (generic *the*, sacred-word article items). No File 2 change; the block-local *an*-onset set is governed by **PD-012 / PD-009 / Run Book §5.7–5.8**. Charter §H.3 unchanged (reaffirmed). Forward-only (Charter §K.3); frozen blocks not retrofitted.
**Status:** Applied (C3 Block 6 is the first block delivered on this ruling).

---

### PD-023 — Word Box removed from C1 Block 5 worksheets (divergence from DP §2 "noun from word box")
**Decision:** For **Class 1, Block 5 (Demonstrative)**, **no Word Box is printed on any worksheet** (CW-1…HW-4, PT Part F). Principal ruling. The graded target is the demonstrative (*this/that/these/those*); the pointed **picture** supplies the noun. To keep every item fair without the word-box scaffold, all pictured objects are restricted to nouns the child has been taught to read and spell — the held W1–W4 set **book, pen, pencil, bag, tree, house** — plus the two PD-017 carriers **umbrella, egg(s)** (for "a/an" practice; carrier noun spelling not graded).
**Conflict recorded (not silently absorbed):** DP §2 row 5 and the §-skeleton row for B5 both specify *"picture-cued; noun from word box"* / *"fill-in-blank … word box."* Printing no word box is a **divergence from the current Drive Plan cap text**. It narrows nothing in the taught skill (the demonstrative), and raises the noun demand from copy-from-box to read-from-picture + spell-from-memory, which is why the object pool is held to taught spellable nouns.
**Rationale:** reviewer/Principal direction; also brings the sheet closer to the raw Annual Q6 (which prints no word box). Fairness preserved by the taught-spellable-noun restriction.
**Affected files:** C1 Block 5 master + all its worksheets. **Drive Plan §2 row 5 and the §-skeleton B5 row** carry a forward-only note recording that the word-box scaffold is not printed for this block (added this pass, C1 Plan). Forward-only per Charter §K.3; frozen blocks not retrofitted.
**Status:** Applied (C1 Block 5).

---

### PD-024 — C1 Block 5 Performance Test carries a graded Part F (demonstrative picture question); divergence from DP §4 vocabulary-only PT
**Decision:** For **Class 1, Block 5 (Demonstrative)**, the Thursday Performance Test additionally carries **Part F — a 6-item, 6-mark picture-cued demonstrative question mirroring Annual Q6** ("Make appropriate sentences about the pointed objects using This, That, These, Those"). Principal-directed. **PT total = 25** (Parts A–D vocabulary 15 + Part E self-try 4 + Part F 6).
**Conflict recorded (not silently absorbed):** DP §4 / §3d set the Thursday PT as **vocabulary (15 marks)** with **"no new grammar content in S4"**; the block's grammar was to be assessed via CW/HW and the self-try. Adding a graded grammar Part F is a **divergence from the §4 vocabulary-only model.**
**Rationale:** follows the **Block 4 precedent** — its PT gained a graded recognition part (Part E, mirroring Annual Q4). Provides a direct exam-mirror graded check of the block's taught skill. Disjointness from CW/HW is **waived for Part F** (graded skill test, per the Block 4 ruling); §6.5 disjointness continues to bind the Part E self-try only.
**Affected files:** C1 Block 5 master + PT extracts (`C1B05-PT`, `C1B05-PT-F`). **Drive Plan §4** carries a forward-only note recording that B5's PT carries a graded Part F (added this pass, C1 Plan). Forward-only per Charter §K.3.
**Status:** Applied (C1 Block 5).

---

### PD-025 — Two-week block internal shape (8-day, one PT per week); two-master `a`/`b` option — C2 Block 6
**Decision:** A spine block allotted **two weeks** ("load peak") builds as an **8-day, two-half block**: each week is a self-contained teaching half (4 class-days) with **its own Thursday Performance Test**, its own fresh vocabulary batch (§4), and a marked **seam**. It may be authored as **one master** (PT extracts `-W1`/`-W2`) **or as two masters** with an **`a`/`b` block-half qualifier** (`C2B06a`, `C2B06b`) where the halves carry distinct grammar and warrant separate audit surfaces. The half-qualifier does **not** create a new block — both halves anchor to the same spine block number (preserves the 2026-07-19 "anchor is the block" ruling). Distinct from the §6.7 **paired-week block** (2+2 sharing one assessment).
**For C2 Block 6 specifically:** built as **two masters** — **06a** (W5: verbs + simple-present agreement + am/is/are) and **06b** (W6: have/has + match-to-make-a-sentence) — one PT per week (06a PT mirrors HY25 Q12 + HY26 Q11; 06b PT mirrors AN25 Q12 + Q11), per-anchor exam mark splits preserved.
**Conflict recorded (not silently absorbed):** Drive Plan §4 lists W5–W6 with a **singular** "Performance Test" and §2 row 6 describes the block as one undivided unit. This ruling reads §4's singular as non-binding on internal shape and sets **two PTs** (one per week), consistent with Run Book §9.1/§9.5.
**Rationale:** a single end-of-fortnight PT would leave the first week with no retention signal before the second week's fresh batch lands, at the heaviest load point. Two masters give each week a clean, independent audit surface (held-scope, de-pattern, CW↔HW and PT-vs-worksheet disjointness) without cross-week bleed.
**Affected files:** Run Book §6.7 (two-week variant) and §7 (`a`/`b` half-qualifier) — amended v1.16 → v1.17. C2 Drive Plan §4/§7 carry a forward-only note recording the two-PT, two-master shape (v1.7 → v1.8). C2 Block 6 masters (`…06a`, `…06b`) + extracts. Forward-only per Charter §K.3.
**Status:** Applied (C2 Block 6).

---

### PD-026 — Function-word grammar targets (am/is/are, have/has) are not non-held vocabulary
**Decision:** When the **grammar target itself is a function word** — am/is/are, have/has, and comparable closed-class items — it is **not** vocabulary and takes **none** of the three non-held statuses (§5.7 exemplar, §5.8 block-local, §5.9 override). It is the rule being taught, delivered in teacher script, clue card, and graded blanks directly; it is correctly **absent from File 2** (function words are excluded at pool source) and needs no exemplar carve-out. The §6.5 held-word audit passes a graded be/have blank on the grounds that the answer **is the block's taught grammar target**, not a lexical item requiring a held trace.
**Boundary:** this covers closed-class words that *are* the grammar objective. It does **not** license ordinary open-class words (nouns/verbs/adjectives) being used unheld — those still require a held trace or a declared §5.7/§5.8/§5.9 status per PD-020.
**Rationale:** PD-020 selects an instrument by "what the word is for." A be/have form is not "for" the child to own as vocabulary; it is the structure under instruction. Forcing it through §5.7 (exemplar) would misclassify a grammar target as a lexical demonstrator; through §5.8/§5.9 it would add function words to the taught-vocabulary load and the retention-gate count — a category error.
**What led to this:** C2 Block 6 (Verbs + am/is/are; have/has in W2). The 20 held W5 verbs supply every graded doing-word answer; am/is/are and have/has are taught as grammar, so the block declares **no PD-009 exemplar**.
**Affected files:** Clarifies PD-009/PD-020; amends neither. Run Book §5.7 may carry a one-line pointer at next revision. Forward-only.
**Status:** Applied (C2 Block 6).

---

### PD-027 — Worksheet fill word-boxes are permitted as scaffolding though the papers use bare blanks
**Decision:** A **word box on a fill-in worksheet part** (the list of answer options above a "fill in the correct word" task) is permitted as **teaching scaffolding**, even where the binding papers present the equivalent item as a **bare blank**. It is distinct from a §3.17 **reference block**: a word box is an inline **answer-set for a fill task**, not a boxed panel restating a rule above the sheet. The **Performance Test carries no word box** (mirrors the exam's bare-blank format), so the unaided exam skill is still rehearsed at test. A word box is admissible only where **answers repeat across blanks** (so no item is derivable by elimination); a one-to-one box on a single-answer set is an answer key and is barred.
**Conflict recorded:** verified against HY25/HY26/AN25 — Muhammadpur/Mohammadpur fill items use **no word box**. Worksheet boxes therefore diverge from strict exam-format mirroring; permitted as a scaffold, not a fidelity claim.
**Rationale:** early-week worksheets legitimately scaffold more than the test; the box supports the first week a set is graded while the boxless PT preserves exam fidelity. Interacts cleanly with §3.17/PD-018 (word box ≠ rule box) and its repeat-answer guard prevents the box becoming a key.
**What led to this:** C2 Block 6 W1 — Part C "fill the doing word" carries a 5-verb box on CW/HW; the PT is boxless.
**Affected files:** Clarifies §3.17/PD-018 boundary. C2 Block 6 W1 worksheets. Forward-only.
**Status:** Applied (C2 Block 6).

---

### PD-028 — C3 Block 7 (Adjective): graded-item weighting 55/25/20 across the three strands
**Decision:** In **C3 Block 7 (Adjective)**, graded items are weighted **55 / 25 / 20** across **descriptive : possessive-demonstrative : number**. The *how many* (number) strand is admitted to the taught cap alongside Drive Plan v1.8 §2 row 7. The **possessive, demonstrative and number strands are taught in full but are not exam-tested**; only the descriptive strand carries an exam anchor.
**Rationale:** the sole adjective anchor in the binding C3 set is **Annual 2025 Q8** ("Identify adjectives from the following passage", 5×1=5), identify-from-passage and descriptive-only — **HY2025 and HY2026 do not test adjectives at all** (verified against all three papers). The other strands are curriculum-necessary (they carry the Block 7/8 adjective-vs-pronoun boundary) but must not displace exam-weighted practice, so they are taught fully and graded lightly rather than dropped or given equal weight.
**What led to this:** the C3 Block 7 build session, which set the weighting and admitted *how many* to the cap.
**Affected files:** `C3_ENG_GrammarBlock07_Adjective_v1.md` (Provenance table, Topic/cap and Weighting rows); C3 Drive Plan §2 row 7.
**Numbering note:** this ruling was **cited as PD-028** in `extracts/C3/TN/C3_ENG_GrammarBlock07_Adjective_v1.md` but was never appended to this log; the number is now formally assigned to it here, so that in-file citation resolves correctly. That in-file citation is historical and **stays unedited per Charter §K.3**.
**Status:** Applied (C3 Block 7); logged retrospectively 08.08.26.

---

### PD-029 — C4 spine renumbering (Adjective + Pronoun → Block 5; Preposition → Block 6) and the combined `C4B0506-PT` holiday carry-forward
**Decision:** Two linked rulings on the Class 4 spine. **(i) Renumbering:** the C4 spine folds **Adjective + Pronoun into a single Block 5** (sub-rows **5a Adjective / 5b Pronoun**) and **Preposition becomes Block 6** (Drive Plan v1.11). Existing `C4B05-*` extract IDs are **unchanged**. **(ii) Assessment carry-forward:** the Week-5 Thursday `C4B05-PT` was **built but never administered** — the slot was lost to a holiday. Its assessment is **carried into the combined `C4B0506-PT`** (in `C4_ENG_Block06_Preposition_v1.md`), which grades Block 5 (Adjective + Pronoun) **and** Block 6 (Preposition) together in the Week-6 slot. `C4B05-PT` is retained as the built-but-unused Block-5 record and is **not to be administered separately** absent a Principal ruling; the combined PT's Adjective/Pronoun items are **freshly authored**, zero-overlap against `C4B05-PT` and all Block-5 worksheets (§6.5 verified during the Block 6 build).
**Boundary — not a precedent for split blocks.** The combined PT here is a **§6.7 paired-week recovery measure** caused by a lost teaching day, merging two **different block numbers**. It is **not** a design pattern, and it does **not** license a combined PT across the two halves of a **two-week `a`/`b` split block**, which **PD-025** governs (one PT per week, per-anchor mark splits preserved, separate audit surfaces). Run Book v1.17 §6.7 keeps the paired-week block explicitly *distinct from* the two-week block.
**Rationale:** the renumbering reflects the taught reality that adjective and pronoun are one boundary-sharing unit at C4 level; the carry-forward preserves the assessment rather than discarding a built PT or double-testing pupils on a spent item set.
**What led to this:** the C4 Block 5/Block 6 build sessions (06.08.26).
**Affected files:** `C4_ENG_Block05_AdjectivePronoun_v1.md` (numbering note, `C4B05-PT` banner, version log v1.15); `C4_ENG_Block06_Preposition_v1.md` (`C4B0506-PT`); C4 Drive Plan v1.11.
**Numbering note:** this ruling was **cited as PD-028** in `extracts/C4/TN/C4_ENG_Block05_AdjectivePronoun_v1.md` but was never appended to this log. **PD-028 has been assigned to the C3 Block 7 weighting ruling above**, so this ruling takes **PD-029**. The `PD-028` citation inside the C4 file is therefore **stale and now resolves to a different entry**; it is historical and **stays unedited per Charter §K.3**. Cite **PD-029** for this ruling going forward.
**Status:** Applied (C4 Blocks 5–6); logged retrospectively 08.08.26.

---

### PD-030 — `C4B04-AK` consolidated to `extracts/`; HW-2 item 28 resolved to *an*
**Decision:** `extracts/C4/C4B04_AK.md` is the **authoritative** Class 4 Block 4 answer key. **HW-2 item 28** — master item *"She is ______ honest teacher."* — is **`an`** (silent *h*). A second copy at `blocks/C4/C4B04_AK.md` carried **`The`** for that item and has been **removed**: `blocks/` holds **block masters only**, and an answer key is not a master. Three sections that existed only in the removed copy — **Marking notes**, **PT Part A dictation word list** (with its teacher-only caveat and the PD-009 exemplar rule), and the **§6.11 Consistency check table** — were ported into the `extracts/` copy **verbatim, unreworded**.
**Rationale:** two divergent renderings of one answer key is a marking hazard — a teacher handed the `blocks/` copy would have mismarked HW-2 #28 against the master. Consolidating to one authoritative file removes the divergence; porting the unique sections first means the cleanup costs no content.
**Evidence / Observation:** verified programmatically, not by eye. Both copies were parsed into item-number → answer maps: **285 numbered answers compared**; the merged `extracts/` file is **identical to the pre-merge `extracts/` copy (0 differences)** and differs from the removed `blocks/` copy at **exactly one item — HW-2 #28** — resolved against the master. All nine stated mark totals unchanged (CW1 54 · HW1 46 · CW2 54 · HW2 46 · CW3 57 · HW3 45 · CW4 38 · HW4 46 · PT 47). The three ported sections were confirmed byte-identical substrings of the source.
**Note:** the C4 Block 4 v1.1 review log already records an earlier transcription defect in HW-2 (Part B had contained HW-3's Part B verbatim), so this sheet has prior history of copy drift. **No student-facing worksheet and no block master was changed** — the defect existed only in the duplicate key.
**Affected files:** `extracts/C4/C4B04_AK.md` (consolidated); `blocks/C4/C4B04_AK.md` (removed). Commit `a8e329a`.
**Status:** Applied (08.08.26).

---

### PD-031 — Sacred words are excluded from match-to-make-a-sentence tasks; the exam format is mirrored on secular content
**Decision:** In a **match-to-make-a-sentence** task (and any task whose graded act is **assembling or re-forming a sentence**), **no strip, fragment or complement may contain a sacred word** — *Allah, আল্লাহ, Quran, কুরআন*. This holds on worksheets **and** the Performance Test. The exam format is mirrored faithfully on **secular content**; the reverence guard is not traded for format fidelity.
**Rationale:** Charter §H.3 bars a sacred word as a **graded classification target**. In a match/assembly task the graded act *is* the assembly of the strip, so a sacred-word strip is a graded target — squarely inside §H.3, not a borderline case. A child can also produce a *wrong* pairing of a sacred strip while working, which is precisely what the guard exists to prevent. The format (re-form five mis-paired sentences) transfers completely to secular subject matter, so nothing pedagogical is lost.
**Boundary vs PD-022:** PD-022 permitted a *Quran* item in C3 Article by **secular transfer, never blanked** — the sacred word was printed intact and the graded blank sat elsewhere in the sentence. That carve-out does **not** extend here, because a match task cannot hold the sacred strip fixed and still be a match task. Teacher script and clue-card prose may continue to reference sacred content normally (§H.3 permits teacher prose).
**What led to this:** C2 Block 6b, whose binding anchor **AN25 Q11** itself contains the strip *"My father reads the Quran everyday."* The drive mirrors the question's **form**, not that content.
**Affected files:** `C2_ENG_Block06b_*` master + extracts. Clarifies Charter §H.3 for assembly-type items; amends nothing. Forward-only.
**Status:** Ruled (Principal, 08.08.26); applies from C2 Block 6b.

---

### PD-032 — Cross-half grading in a two-week split block, and the widened PT zero-overlap audit scope
**Decision:** In a two-week `a`/`b` split block, the **b-half Performance Test may grade grammar taught in the a-half** where the binding exam format requires it. Where it does, **the PT zero-overlap gate must run against the worksheets of *both* halves**, not just the half under build. For C2 Block 6b this means the `C2B06b-PT` is audited against **sixteen** worksheets (6a's eight + 6b's eight), not eight. **Both the cross-half grading and the widened audit scope are declared explicitly in the b-half master.**
**Rationale:** AN25 Q11 ("match the words to make five meaningful sentences") is built on **be-forms** — *is/are* — which are 6a's grammar. Mirroring the exam therefore puts 6a content on 6b's graded surface; be-forms are held by W6, so this is pedagogically sound. But PD-025 justified the two-master split partly on **separate audit surfaces**, and a PT that grades both halves has an item-overlap surface spanning both. Auditing it against only its own half would leave a real leak path — a 6b PT item could silently duplicate a 6a worksheet item.
**Implementation note:** `audits/scripts/run_all.py` `gate_pt_zero_overlap()` compares the PT against worksheets **within the same manifest**. Satisfying this ruling requires the a-half worksheets to be visible to that gate **without** re-running the other gates over an already-validated block. The mechanism (a reference-scope flag on those sheets) is a **minimal additive change to the audit script**, to be approved before use.
**What led to this:** C2 Block 6b Phase 2 review.
**Affected files:** `C2_ENG_Block06b_*` master; `audits/scripts/run_all.py`. Extends PD-025; amends nothing. Forward-only.
**Status:** Ruled (Principal, 08.08.26); applies from C2 Block 6b.

---

### PD-033 — C5 block renumbering: Drive Plan §2 realigned to the build sequence (18 blocks; 4a/4b and 7a/7b sub-rows)
**Decision:** The **C5 Drive Plan §2 Block column is now the authoritative block number and matches the actual build sequence**, giving **18 blocks**. Two rung-pairs that are taught as one block each are carried as lettered sub-rows: **4a** (noun — common & proper + collective) / **4b** (noun — gender), delivered together at W3; and **7a** (Adjective) / **7b** (Pronoun). **Correspondence and Composition remain separate Blocks 17 and 18** — distinct rungs, not sub-rows (Principal ruling). A permanent **§2A concordance** carries the former §2 row numbers so that citations inside already-delivered block files resolve.

**Mapping (old §2 row → new Block):** 1→1 · 2→2 · 3→3 · **4→4a** · 5→5 · **6→4b** · **7→6** · **8→7a** · **9→7b** · 10→8 · 11→9 · 12→10 · 13→11 · 14→12 · 15→13 · 16→14 · 17→15 · 18→16 · **19a→17** · **19b→18**. Offset pattern: rows 1–3 unchanged, row 7 runs −1, rows 10–18 run −2.

**Why:** two numbering systems had been running in parallel and had begun to corrupt citations. §2 numbered **rungs** (1–18 + 19a/19b = 20); the build numbered **blocks** as shipped. They diverged at the noun cluster — §2 rows 4 and 6 shipped **merged** as build-Block 4, and row 5 as build-Block 5 — so from row 7 the offset was −1, and would become −2 once Adjective + Pronoun merged. The drift was already live and load-bearing: `C5_ENG_Block06_Article_v1_5.md` cites "§2 row 7" six times for what is build-Block 6; §4's map named "Block 11" and "Block 13" for blocks that will build as 9 and 11; and §2 row 8's "the locked Block 7/8 boundary" was an **unmarked C3 cross-reference**, not a C5 one. Left unresolved, every subsequent block file would have compounded the offset.

**Reconciliation with the 2026-07-02 first-teach reframe.** That ruling stated the **block/week count grows — nothing compressed**, and 20 rungs → 18 blocks reads at first glance as the opposite. It is not: **no rung is dropped** (the two merges preserve every rung as a sub-row), and the growth the ruling directed is delivered — **Preposition (Block 8) and Conjunction (Block 13) are now teaching blocks in their own right** rather than clue-card rows inside Block 1, which is what the reframe re-homed them out of.

**Precedent:** **PD-029**, which folded the C4 spine's Adjective + Pronoun into a single Block 5 with sub-rows **5a/5b** and moved Preposition to Block 6, leaving existing `C4B05-*` extract IDs unchanged. This ruling applies the same instrument to C5.

**Scope limit — numbering only.** This ruling takes **no position on the calendar**. The week→block mapping, per-week load, week count, and any pairing/compression decision remain **superseded and pending a separate Principal decision** (Principal instruction, 08.08.26). §4's table has had its block numbers corrected and W1–W5 recorded as delivered fact; **every row from W6 onward is explicitly marked "not ratified."**

**What the renumbering exposed (recorded, not resolved):** with the numbers corrected, the calendar arithmetic is explicit for the first time — **18 blocks**, six delivered (W1–W5) and one in build, against the Charter **§C.1** three-month ceiling measured from the 1 July start. The remaining blocks do not fit one-per-week. Resolving it requires a ruling on pairing/compression or a **§C.5** cap widening, together with the calendar lock that **§C.3/§M.1** required *before* Week 1 and which was never closed.

**Delivered content untouched (Charter §K.2/§K.3).** No delivered C5 block master or extract is edited, and **no block file is renamed** — Blocks 1–6 already carry the corrected numbers, so the correction moves §2's rows onto the build, not the reverse. Historical "§2 row N" citations inside frozen files stay as written and resolve through §2A.

**What led to this:** raised at the opening of the C5 Block 7 (Adjective + Pronoun) build, 08.08.26, when the block's §2 citation could not be stated unambiguously — it is build-Block 7 but §2 rows 8–9. The Principal directed the renumbering be settled before the build continued.

**Affected files:** `C5_ENG_DrivePlan_v1_6.md` (new version; v1_5 retained, forward-only per §K.3) — §2 table, §2 exam-bridge ledger, new §2A concordance, §2 governance note, pre-flight checklist, §3, §4 table + notes, §7 map + new note, §8. `blocks/C5/_wip/STATE.md` (C5B07 citations). **Not modified:** all C5 block masters and extracts, File 2 (its stale week→block labels remain a separate forward-only reconciliation), the Assignment Coverage Log (its C5 entries cite B03/B04, which do not change), and the week-named assignment files.
**Status:** Applied (Principal, 08.08.26).

---

### PD-036 — The genuine C5 Annual-2025 paper is in the project; the binding set is four
**Decision:** `exam-papers/Class 5 English Mohammadpur Final Question 2025.pdf` (md5 `1265996d9f26052e76334a2f3a0d2ba4`) **is** the genuine **Class 5 Annual Examination 2025** paper. The **C5 binding set is four** — HY-2025 Morning, HY-2025 Day, HY-2026, Annual-2025 — all simultaneously binding by union (Charter §J.2–J.3). **The bar on citing an Annual anchor in any C5 artefact is lifted**, and Block 3's standing "Annual Q8 unverifiable" dependency is **closed**.
**The 31.07.26 duplicate ruling is not overturned.** That ruling concerned `Class_5_English_Muhammdpur_Annual2025.docx`, a **different file**, byte-identical to HY-2026, which is **not present in this repo**. A cross-check of the four C5 papers now present returns **four distinct md5s**; no duplication remains.
**Evidence:** the Principal supplied the paper on 08.08.26; it proved **byte-identical to a file already in `exam-papers/`**, flagged during the C5 Block 7 Phase-1 orientation as BC-1 and ruled "missing" earlier the same day on the then-available information. The file's own header reads *School for Community Development · Mohammadpur Branch · **Annual Examination 2025** · Class: Five · Subject: English · Time 2 hours 30 minutes · Full Marks 80*.
**Verification run on arrival (Run Book §10.2), question by question.** All twelve questions extracted and compared against Drive Plan §7. **All five existing Annual citations hold; no §7 row required correction:** Q1 / Q5 fill-from-box → Block 1 · Q7 correct form of verbs → Blocks 10–11 · **Q8 transformation → Block 3** · Q9 WH-questions (2×5=10) → Block 15 · Q4 composition + Q11 letter → Blocks 17–18. Q2/Q3/Q6 are reading formats (not a grammar block, §7). **Block 3 specifically:** Q8 reads *"Change the Sentences according to the direction"* with **Interrogative and Negative directions only** — matching the §2 Block 3 two-direction cap exactly, with no voice or narration item. The cap needs no change.
**No cap or ledger change.** The Annual introduces no new *taught* structure: its Q7 tense range (*always wash · bought · has been raining · died before came · by 10 a.m. … finished*) is already governed by the §2 exam-bridge ledger, and **future perfect remains exam-revision-pack only**.
**One coverage gap surfaced — flagged, not resolved (Principal instruction).** **Annual Q10** *"Rearrange the words in the appropriate order to make meaningful sentences"* **[1×5=5]** and **HY-2026 Q5** *"Rearrange the words in the correct order…"* **[5×1=5]** both test sentence rearrangement, which **no §7 row and no C5 block covers**. Two independent binding papers with a consistent format at 5 marks each make this **"definitely required"** under Run Book §10.5, not "wait for future evidence"; **C1 already carries a Rearrangement block**, so it is a C5 spine gap rather than a rejected category. Per Charter §E.6 / Run Book §10.4 r.1–r.2 **no teaching material has been drafted and no placement proposed.** Resolution requires a Principal decision on spine placement and is **coupled to the open calendar decision** — the spine has no spare week. Recorded in Drive Plan §7 so it cannot be lost; it gates no current block build.
**Affected files:** `C5_ENG_DrivePlan_v1_7.md` (new version; v1_6 retained, forward-only per §K.3) — header derivation line, §7 preamble, status line, new §7 gap flag. `blocks/C5/_wip/STATE.md` (BC-1 closed). **Not modified:** the §2 caps and ledger, the PD-033 numbering, the calendar/week map, and every delivered C5 block master — **none cited an Annual anchor**, so nothing is retro-corrected. `English_Drive_BlockBuild_StarterTemplate_v2.md` carries a stale "C5 binds on three papers" note, flagged for its own next revision (§K.3).
**Status:** Applied (Principal, 08.08.26).

---

### Open item — C3 Exit Check roll size (17) not file-verified
Recorded for tracking, not a Principal decision. The C3 Block 6 Exit Check tables use a **17-prompt roll** on the Principal's in-session statement; no class roster in the current project files confirms 17. Verify against an authoritative roster, or log a Principal confirmation, before treating the roll as governance-grade. Affects only the per-day Exit Check length (one prompt per student), not any graded item.

---

## Project Proposals (PR)

Ideas or workflow improvements still under discussion, not yet official decisions.

### PR-001 — Generate weekly assignments with Claude
**Proposal:** Use Claude to generate weekly school assignments from the approved curriculum instead of preparing them mostly manually.
**Reason:** This can save time and improve consistency.
**Affected files:** Future Weekly Assignment files, Assignment prompts, Teacher workflow.
**Status:** Under Review — Week 1 assignments were prepared mostly manually and are already uploaded to the Project Knowledge.

### PR-002 — Weekly Curriculum Design Log
**Proposal:** Keep this working chat during the week and update the official Curriculum Design Decision Log in the Project Knowledge once every week.
**Reason:** This will preserve important curriculum decisions and the reasons behind them without interrupting development work.
**Affected files:** This Working Log chat and the official Curriculum Design Decision Log in the Project Knowledge.
**Status:** Under Review

---

## Pending Class Decisions

Decisions made in principle but not yet implemented. Not official until converted.

### Class 4 — Move Block 03 earlier in the sequence
**Date:** 11.07.26
**Status:** Planned (Not Yet Implemented)
**Proposed Change:** Move Block 03 earlier in the sequence.
**Reason:** While rebuilding the curriculum, concluded that students would benefit from learning this topic earlier, since later blocks depend on it.
**Evidence / Observation:** Surfaced during the Class 4 Block 03 discussion.
**Affected Documents (once implemented):** Class 4 Drive Plan, Block 03 file, Vocabulary Batch Order (if needed).
**Next Action:** Update Drive Plan → Rebuild Block 03 → Update Vocabulary Batch Order if needed.
**Notes:** Not yet implemented. Convert to an official Class 4 Decision once the Drive Plan and Block 03 rebuild are done. **Not yet confirmed whether this is the same item as the later-detailed "insert a Sentence & Sentence Types block after Noun" cluster raised in the Class 4 Block 02 discussion — pending your confirmation.**

---

## Class 3 Decisions

### Oral plain-label fade tier
**Date:** 10.07.26
**Category:** Curriculum design decision
**Decision:** Class 3 may use plain labels orally as a beginning scaffold when introducing sentence types. Previously, Class 3 was formal-terms-only with no plain-label naming. Students still write formal terms in exams. This mirrors the existing Class 4 oral-reminder allowance.
**Reason:** Reconciles classroom practice (teachers wanting to introduce with plain labels) with the formal-terms-in-exam policy.
**Evidence / Observation:** A Principal ruling relayed during the Class 5 Block 2 conversation, overriding the Block-Build Spec's previously locked "Class 3 = formal only" tier.
**Affected Documents:** Block-Build Spec (Locked Decision section), all Class 3 sentence-type files (next revision), Class 5 teacher-reference note.
**Status:** Ruled, not yet propagated to files. **Note (11.07.26): a Class 3 Block 2 build session applied fading-box mechanics (support box shown Day 1, narrows Day 2, removed Day 3) consistent with this ruling — pending your confirmation on whether to fold this detail into this entry.**

---

## Class 5 Decisions

### Block 2 (Sentence Types) — First-teach reframe
**Date:** 10.07.26
**Category:** Curriculum design decision
**Decision:** Block 2's tier changed from Revision to First-teach (discovery pace), with no prior retention assumed. Bloom ladder opens at Remember/Understand.
**Reason:** Students shouldn't be assumed to already know the five sentence types.
**Evidence / Observation:** Reviewer argued the point; Block 1 (Word) had already been reframed to first-teach by an earlier Principal ruling; Principal approved extending that stance to Block 2.
**Affected Documents:** C5 Drive Plan §2 (tier), §4 (week map), §5 (exam-bridge) — flagged, not yet edited. Later C5 blocks that assume a revision baseline.
**Status:** Ruled, not yet applied to Drive Plan.

### Block 2/3 — Solo-week expansion and W2/W3 split
**Date:** 10.07.26
**Category:** Curriculum design decision
**Decision:** Block 2 expanded to a near-solo 3-day week (Sun–Tue). Block 3 (Transformation) splits across weeks: class 1 in W2 (Wednesday), class 2 in W3 with the noun re-walk. W2 Thursday test = Sentence Types only; W3 Thursday test = Block 3 + Block 4. Overall calendar stays ~15 weeks.
**Reason:** First-teach of five sentence types needs more than 2 days; Transformation is a light bridge that doesn't need its own solo week.
**Evidence / Observation:** Follows directly from the first-teach reframe above — original 2-day plan was too compressed.
**Affected Documents:** C5 Drive Plan §4 (week map, Thursday-test pairing), Block 3 file, Block 4/noun blocks (shared W3 test).
**Status:** Ruled, not yet applied to Drive Plan. **Implementation note (11.07.26): Drive Plan §4 and the 14-week Batch Order map are confirmed stale and still need updating to reflect this split.**

### Sorrow-register exclamatory — strict "never in construction"
**Date:** 10.07.26
**Category:** Curriculum design decision
**Decision:** Sorrow-register exclamatory content appears only in identify/passage sections with a teacher-scenario note — never in any make-a-sentence, self-try, or construction task. No student-produced exclamatory exists anywhere in the block.
**Reason:** Child-safety/appropriateness — students shouldn't be prompted to compose sad or grief-related sentences themselves.
**Evidence / Observation:** Tightened during the Block 2 build; the underlying principle already exists in Class 3/5 policy, but this is the strict "never in construction" application.
**Affected Documents:** Block 2 worksheets, answer keys, day-scripts.
**Status:** Applied

### Negative imperative representation
**Date:** 10.07.26
**Category:** Curriculum design decision
**Decision:** Every identify worksheet in Block 2 must include negative/prohibitive imperatives (e.g., "Never tell a lie," "Do not..."), shown in teaching cards and examples too.
**Reason:** Binding exam evidence (HY-25 Day and Morning papers) both include a negative imperative that the block hadn't represented.
**Evidence / Observation:** Gap found by comparing the block against binding exam papers.
**Affected Documents:** Block 2 files. Flagged as worth checking in other classes' sentence-type blocks too.
**Status:** Applied

### Day-staged worksheet architecture (Class 5-local)
**Date:** 10.07.26
**Category:** Curriculum design decision (workflow-adjacent)
**Decision:** Worksheets built as day-staged sheets (CW-1/HW-1 Day 1, CW-2/HW-2 Day 2, CW-3 Day 3), with a type-name hint box above section ক that fades across days. Each class's worksheet sits under its own day-script for print-per-class; answer keys pooled separately and marked "don't print with students."
**Reason:** Scaffolded fade so help depends less on cueing over time; clean per-class printing (previously Class 2/3 shared a sheet, causing confusion).
**Evidence / Observation:** Built this way during the Block 2 build.
**Affected Documents:** Block 2 files. Not yet a project-wide standard — left as Class 5-local. Reused in the Block 3 build (11.07.26) without change.
**Status:** Applied

### Day-1 recognition-only construction
**Date:** 10.07.26
**Category:** Curriculum design decision
**Decision:** Independent sentence construction removed from Day-1 homework (HW-1 = identify + find-the-error only). Construction moved to HW-2 and the Day-3 guided self-try. HW-2 construction reduced to 3 items, Assertive/Interrogative/Optative only — no Imperative or Exclamatory construction.
**Reason:** Day-1 homework was asking students to construct sentences before construction had been guided at all (self-try isn't until Day 3) — backwards and too heavy.
**Evidence / Observation:** Identified during the Block 2 build review.
**Affected Documents:** Block 2 files. Flagged as a possible project-wide sequencing principle ("no independent construction before a skill is taught") — left as an open candidate, not yet promoted.
**Status:** Applied

### Block 3 — Re-walk scope correction
**Date:** 11.07.26
**Category:** Curriculum design decision
**Decision:** Block 3 class 2's warm-up re-walks Word → Sentence → sentence types only. It must not re-walk common/proper noun, since noun is first-taught the same week (Block 4) and students may not hold it yet.
**Reason:** Removes a prerequisite-assumption error in the draft.
**Evidence / Observation:** Reviewer caught it — "we haven't gone to nouns yet."
**Affected Documents:** Block 3 file only.
**Status:** Decided, not yet applied (inline-staged, not written to file).

### Block 3 — Pattern Card reminder-script + time rebudget
**Date:** 11.07.26
**Category:** Curriculum design decision
**Decision:** Keep the four helper rows (be/can/do/does) but add a 4-point teacher reminder-script explaining them, and rebudget Class 1 timing to give the teacher ~3 minutes to teach it.
**Reason:** The card assumed four sub-concepts students may not yet hold, on a light Bridge block.
**Evidence / Observation:** Reviewer concern about helper-pattern and -s-drop recall.
**Affected Documents:** Block 3 file. (Flagged as a possible reusable convention for other helper-pattern blocks — not decided.)
**Status:** Decided, not yet applied.

---


### Block 6 (Article) — solo FULL week at W5
**Date:** 31.07.26
**Category:** Curriculum design decision
**Decision:** Class 5 Block 6 (Article, §2 row 7) runs as a **solo FULL week** — 4 teaching days (Sun–Wed) + its own Thursday Performance Test, not shared or paired with any adjacent block. Release week 5.
**Reason:** Article is anchored in **all three** distinct binding C5 papers, and HY-25 Morning Q6 carries **10 marks** — the single heaviest grammar question in any C5 paper (every other grammar anchor sits at 5–8). The answer set is four-way (a/an/the/x), needing more practice reps than any two-way re-walk block. No retention is assumed at C5 under the 2026-07-02 first-teach reframe, and this cohort never received the C4 Article block (delivered to this year's Class 4 on 24.07.26), so the "re-walk" tier runs at near-first-teach pace. C4 gave Article a solo full week on a *lighter* cap and lighter anchors. Zero article (x), retained in the cap by the v1.1 ruling, is **not tested in any C5 paper** — teaching load with no exam relief.
**Scope limit:** Governs **Block 6's load only.** It does **not** revive, ratify or reconstruct §4's week map or §2's block numbering, both superseded by the 2026-07-02 ruling with no recorded successor. The wider C5 schedule remains an open governance item.
**Numbering note:** build-block numbers have diverged from §2 row numbers — this is build-**Block 6** but §2 **row 7**, the noun cluster (rows 4–6) having shipped as build-Blocks 4–5. All block-file citations use "§2 row 7". Any Drive Plan reconstruction must reconcile the two systems explicitly.
**Affected Documents:** C5 Block 6 master (applied). C5 Drive Plan §4 — W5 row currently reads "TBD" for load; carry this ruling forward at schedule reconstruction.
**Status:** Applied to the block; Drive Plan edit pending.

### Block 6 (Article) — §2 row-7 cap widened: one article for two coordinated titles
**Date:** 31.07.26
**Category:** Curriculum design decision
**Decision:** §2 row 7 is widened to admit **one article before two coordinated nouns naming one person**, taught as a fixed contrast pair — *The Headmaster and Secretary **is** coming.* (one person) / *The Headmaster and the Secretary **are** coming.* (two people). Recognition and fill-in depth only; the **verb** (*is / are*) is taught as the reading clue, matching how the paper disambiguates. No further coordination or determiner theory, and no rule-naming beyond the contrast pair.
**Reason:** HY-25 Morning Q6(e) tests exactly this, inside the 10-mark article question, with "(one person)" supplied as the disambiguator. Nothing in the existing cap reached it, so the block would otherwise have shipped a known blind spot on the heaviest grammar item in the binding set.
**Scope limit:** The only addition. Q6(d) (*the more… the more…*) remains **recognition only** per the standing guardrail; the "no abstract zero-article rule-naming" guardrail is unchanged.
**Evidence / Observation:** Verified by direct read of the HY-25 Morning paper during the Block 6 pre-build check.
**Affected Documents:** C5 Drive Plan §2 row 7 (cap text — this is the authorising ruling; edit pending). C5 Block 6 master (applied). **C4 Block 4 (Article) is delivered and not retrofitted** (Charter §K.3) — no C4 paper tests this, so no downstream absorption is required.
**Status:** Applied to the block; Drive Plan edit pending.

### Binding paper set — the C5 "Annual-2025" file is a duplicate of HY-2026
**Date:** 31.07.26
**Category:** Data integrity / governance
**Decision:** `Class_5_English_Muhammdpur_Annual2025.docx` is **byte-identical** to `Class_5_English_Muhammadpur_HY2026.docx` (identical md5; the file's own header reads *Half-Yearly Exam – 2026*). It is a mis-saved copy, not an Annual paper. The **C5 binding set is three distinct papers**: HY-2025 Morning, HY-2025 Day, HY-2026. The genuine Class 5 Annual-2025 paper is **missing from the project** and is to be sourced; until it lands, no C5 artefact may cite an "Annual-2025" anchor.
**Reason:** Union binding (Run Book §10.1) makes an absent paper a real coverage gap — but a duplicate masquerading as a fourth paper is worse, since it inflates apparent evidence and lets a single HY-2026 item be cited twice as if independently confirmed.
**Evidence / Observation:** Found during the Block 6 pre-build check while verifying article anchors directly against the papers. A cross-class md5 comparison found **no other duplication** — this is C5-only. This ruling promotes and resolves the standing data-integrity flag previously held under *Open Items Tracked Outside This Log*.
**Affected Documents:** C5 Drive Plan §7 — header states "Confirmed from the four Class 5 papers"; correct to three (edit pending). The §7 Article row already cites only HY-26 Q7, HY-25 Morning Q6 and HY-25 Day Q5, independently confirming the duplicate never fed a real anchor. Block-Build Starter Template's C5 binding-paper list. Version-log entries citing "the four Class 5 papers" are historical and stay untouched (Charter §K.3). **Block 3's Annual Q8 evidence remains unverifiable** until the genuine paper is located.
**Status:** Ruled. ⚑ **Open dependency:** source the genuine C5 Annual-2025 paper; re-run §7 mapping when it arrives.

---

## Open Items Tracked Outside This Log

*Not decisions — listed here only for continuity, per earlier working-session discussion. None of these are logged as PD/PR/CX entries.*

- **Programmatic verification as a build standard** — parked for a future Build Standards/QA document, not a curriculum decision.
- **Print-per-class worksheets + pooled answer keys** — left as Class 5-local; not elevated to project-wide.
- **"No construction before a skill is taught"** — open candidate; watching whether it holds consistently across classes before promoting to PD.
- **"First-teach tier shifts earlier when a block moves earlier in the spine"** — not recorded yet; revisit after more classes are rebuilt.
- ~~**Data-integrity flag:** Class 5's "Annual-2025" exam file is byte-identical to HY-2026…~~ **RESOLVED 31.07.26** — Principal ruling logged under *Class 5 Decisions* → "Binding paper set — the C5 'Annual-2025' file is a duplicate of HY-2026". The C5 binding set is three papers; sourcing the genuine Annual-2025 paper remains an open dependency, and Block 3's Annual Q8 evidence stays unverifiable until it is found.

---

### PD-034 — `audit_scope: pt_overlap_only` extends to the §6.7 paired-week recovery
**Decision:** The manifest flag **`audit_scope: "pt_overlap_only"`** — which makes a sheet visible **only** to `gate_pt_zero_overlap()` — is authorised for a **second** shape alongside PD-032's two-week `a`/`b` split block: the **§6.7 paired-week recovery**, where one week's Performance Test was **built but not administered** and its assessment is carried into a **combined PT** the following week. In that shape the combined PT is audited against **both blocks' worksheets *and* the unadministered PT itself**, because PD-029 requires zero overlap against both.
**Rationale:** PD-029 imposed the zero-overlap requirement on `C4B0506-PT` (*"freshly authored, zero-overlap against `C4B05-PT` and all Block-5 worksheets"*) but PD-032 scoped the only mechanism that can check it to split blocks, and PD-029 itself states the paired-week recovery is **not** governed by PD-025/PD-032. The requirement was therefore **unverifiable by any script** — a gap, not a design choice. Extending the flag's authorisation closes it without touching the mechanism: `graded_sheets()` already filters scoped sheets out of every other gate, so no de-patterning, mark-total, held-word or values result is affected by loading reference sheets.
**Evidence that this was not academic:** on first run under the extended scope the `C4B0506-PT` **failed** — PT Part E prompts `meal` and `bird` are **verbatim** duplicates of Block 5 CW-1 Part B (items 22, 25) and HW-1 Part B (item 23), the same *"expand the noun"* task with the same prompt nouns; PT B3 and D4 were near-duplicates of `C4B05-CW4`/`CW2`, and PT D1 (*"Yusuf prayed at dawn"*) shadowed `C4B05-PT` #27 (*"Yusuf prays at the mosque"*) — an **unspent** item, since that PT was never sat. The C4B06 master's v1 log had claimed *"PT zero-overlap verified against all 16 worksheets"*; the claim was false and no script could have caught it.
**Boundary:** the flag remains **reference-only**. A scoped sheet is never graded, never contributes marks, and never enters the held-word or de-patterning surface. It does not license combining PTs — PD-029's boundary against that stands.
**What led to this:** the C4 Block 6 review (08.08.26), Principal-approved as part of the F2 ruling.
**Affected files:** `audits/scripts/run_all.py` (`graded_sheets()` docstring — authorisation only, no logic change); `audits/scripts/README_manifest.md`. Extends PD-032; amends nothing. Forward-only.
**Status:** Ruled (Principal, 08.08.26); applied at C4 Block 6.

---

### PD-035 — PD-012 block-local status extends to concepts required by the Drive Plan §2 cap without an exam anchor
**Decision:** The **PD-012 block-local teaching set** may be declared where a **Drive Plan §2 depth cap requires a concept that the held pool cannot supply**, whether or not a binding exam paper tests that concept. PD-012's trigger is widened from *"exam-required"* to *"required by the binding papers **or** by the Drive Plan §2 cap."* Every PD-012 protection is unchanged: block-local words are gradeable **only** inside their own block's CW/HW/PT, are **never** dictation or spelling items, are **not** held by later blocks, and are **not** in the spaced-revision cycle. **First application: the C4 Block 6 time-noun set** — `Sunday · Monday · Thursday · Saturday · June · July · summer · winter · spring · evening · night · dawn` (12). `morning` and `day` are already held and stay held. The set is **block-scoped**: Blocks 8–9 must re-declare if they want the same words; it is **not** a standing C4 set (Principal ruling), and it is **not** added to File 2.
**Rationale:** the four existing non-held instruments are all anchored to exam requirement — PD-009 exemplars (rule-demonstrators, not vocabulary), PD-011 override (*"exam-anchored vocabulary"*), PD-012 block-local (*"exam-required items"*, rationale *"binding papers test a concept…"*), PD-026 (function-word grammar targets). C4 Block 6's time strand is **book/TG-anchored with no exam anchor at all**: the §2 cap reads *"**Place/time** prepositions"* and TG outcome 9.3.4 reads *"use prepositions to indicate positions **and indicate time**"*, but **both binding C4 preposition items test place** (HY25 Q6(f) *"a bird **on** the tree"*; Annual Q4(f) *"The keys are **on** the desk"*) and HY26 carries no P.O.S. question. So a Drive-Plan-mandated concept had no available instrument — a gap in the instrument set, not a defect in the block.
**Why recasting was not the alternative:** the at/on/in contrast **is** the concept — the preposition is selected by the *type* of its object (clock time → *at*, day/date → *on*, month/season/part-of-day → *in*). File 2 holds exactly **two** time nouns by W6, `morning` and `day`, and both sit in the **same** category, so the pool cannot produce a single contrasting pair. Recasting onto held vocabulary would not have shrunk the block; it would have deleted a capped concept, which is a Drive Plan change and not the builder's to make.
**Boundary:** this widens the *trigger* for block-local status, not its *protections*, and it does **not** license open-class vocabulary being used unheld for convenience. The concept must be traceable to a §2 cap line or a binding paper; incidental carriers are recast, not declared. At C4 Block 6 the ten avoidable carriers (*bench, corner, drawer, garden, grandfather, hole, poor, porch, room, run*) were **recast onto held words**, not declared — the declaration covers only what the concept requires.
**Audit support:** enforced by the new `block_local` manifest field (T1) — a word listed in both `block_local` and `dictation` is a FAIL, as is a word declared both exemplar and block-local. Self-test: `audits/scripts/selftest_block_local.py`.
**What led to this:** the C4 Block 6 review (08.08.26), F5.
**Affected files:** `C4_ENG_Block06_Preposition_*` (declaration); `audits/scripts/run_all.py` + `README_manifest.md` (the field). Extends PD-012; amends nothing. Forward-only.
**Status:** Ruled (Principal, 08.08.26); applied at C4 Block 6.

---

### PD-036 — Cross-sheet repetition gate: no carrier sentence repeats across a block's sheets
**Decision:** A new audit gate, `gate_cross_sheet_repetition()` in `audits/scripts/run_all.py`, fails any block in which the same normalised item text appears on more than one graded sheet (CW, HW, or PT). **Threshold: `CROSS_SHEET_MAX_REPEATS = 0`** — the maximum number of identical carrier sentences tolerated across a block's sheets is zero; every graded sentence is unique across the block. The constant is a single named value so the Principal can loosen it later if it proves too strict.
**Rationale:** C4 Block 6 reached review with **38 sentences repeated over 78 placements** (CW-4 was 16/20 recycled, HW-4 11/20); 40 items had to be re-authored by hand at promotion. The de-patterning, within-sheet duplicate, and CW↔HW gates each look at a narrower surface and all passed while this accumulated. The C4B06 promotion standard (199 sentences, zero repeats) is codified as the threshold.
**Relation to existing gates:** strictly tighter than the CW↔HW "≤2 identical item texts per day" allowance (Run Book §6.5), which remains on the books but can never bind while this gate holds at 0. `audit_scope: "pt_overlap_only"` reference sheets are excluded, as everywhere.
**Corrections ledger:** promotes **CR-009** (PATTERN → PROMOTED). Self-test with seeded error: `audits/scripts/selftest_cross_sheet.py`.
**What led to this:** the C4 Block 6 promotion sweep (08.08.26); gate drafted there and flagged for ruling; ruled at the corrections-ledger promotions (08.08.26).
**Affected files:** `audits/scripts/run_all.py`, `audits/scripts/selftest_cross_sheet.py`, `audits/scripts/README_manifest.md`, `governance/CORRECTIONS.md`. Additive. Forward-only.
**Status:** Ruled (Principal, 08.08.26).

---

### PD-037 — Corrections-ledger promotions, batch 1: option-list completeness and HW key transcribability gates
**Decision:** Two PATTERN rows of `governance/CORRECTIONS.md` are promoted to audit gates in `audits/scripts/run_all.py`, both additive:
1. **Option-list completeness** (`gate_option_list()`, promotes **CR-008**): every keyed answer in a part must appear in that part's printed option list, declared via a new optional part-level `"options"` manifest field. Parts that declare no `options` are not checked (the gate reports itself vacuous). Six C4B06 sheets historically keyed *Adverb* against printed options that excluded it — the one defect class a pupil meets directly in the exam-hall sense.
2. **HW key transcribability** (`gate_hw_key()`, promotes **CR-006**): no part's answer sequence may be positionally identical to the same-named part of its paired sheet (sequences of length ≥3, compared once per pair). The whole-sheet ≤35% positional gate passed C4B06 while five individual HW parts carried keys identical to their CW counterparts, making the homework key transcribable positionally.
**Corrections ledger:** CR-006 and CR-008 move PATTERN → PROMOTED citing this PD. Self-tests with seeded errors: `audits/scripts/selftest_option_list.py`, `audits/scripts/selftest_hw_key.py`.
**What led to this:** CLAUDE.md §5A corrections feedback loop, first promotion batch (08.08.26); both error types reached 3+ occurrences in the C4B06 review.
**Affected files:** `audits/scripts/run_all.py`, the two self-tests, `audits/scripts/README_manifest.md`, `governance/CORRECTIONS.md`. Additive. Forward-only.
**Status:** Ruled (Principal, 08.08.26).

---

### PD-038 — PD-036 zero-repeat standard governs; CW↔HW ≤2-identical-items allowance kept as backstop only
**Decision:** PD-036's zero-repeat standard supersedes the CW↔HW ≤2-identical-items allowance, which can never bind at 0. The ≤2 rule stays in `run_all.py` as a defense-in-depth check but is no longer the governing standard. `CROSS_SHEET_MAX_REPEATS` remains 0 (Principal threshold ruling). The CW↔HW gate's report line now carries "(superseded by PD-036 zero-repeat, kept as backstop)".
**Status:** Ruled (Principal, 08.08.26).

---

### PD-039 — C1 Block 6: the recognition-only cap is lifted to S3 free pronoun rewrite (this block only)
**Decision:** C1 Drive Plan §2 row 6 caps Block 6 at *"recognition ONLY… NO sentence rewriting, NO pronoun production"* (Ruling A, with the 5-mark Annual gap accepted). For **C1 Block 6 only** this is lifted to **S3 free rewrite** — the child rewrites a given sentence replacing the naming word with its pronoun, no word box — so that the Annual Q3 format (*"Rewrite the sentences using pronouns"* [5]) is taught directly and the accepted gap is closed. Graded rewrite targets **he / she / it / they** only; **I / we / you** stay at recognition and matching. The Bloom band is knowingly stretched to Apply/Create for this task; the cohort-age objection was recorded and overruled. Block-scoped: it does not propagate to other classes and does not reopen frozen blocks. Ruling A is annotated *"superseded for C1 B6 by PD-039"*, not deleted (Charter §K.3, forward-only).
**What led to this:** the C1 Block 6 build (W6) was authored in chat against a provisional number **PD-028**, which the Decision Log had already assigned to the C3 Block 7 weighting ruling. The citation is corrected to PD-039 throughout `blocks/C1/_wip/C1_ENG_Block06_Pronoun_v1.md` on import.
**Affected files:** `blocks/C1/_wip/C1_ENG_Block06_Pronoun_v1.md`; forward-only note owed on C1 Drive Plan §2 row 6, §7 and §9b.
**Status:** Ruled (Principal, 09.08.26).

---

### PD-040 — C1: combined Block 5 + Block 6 Performance Test `C1B0506-PT`
**Decision:** Block 5's Performance Test was postponed by a holiday, so Blocks 5 and 6 fall on the same Thursday. They are assessed by one canonical combined test, **`C1B0506-PT`** (27 marks). Block 5 (demonstratives) is assessed **text-based** — fill-blank with a bracketed near/far · one/many hint — not picture-cued, matching the Sunday W6 reteach. A pointer is added to `C1B05-PT` recording that its live PT is superseded by `C1B0506-PT`. All W6 worksheets carry the `C1B06-` prefix so they do not collide with Block 5's W5 picture sheets.
**What led to this:** same provisional-numbering error as PD-039 — the build cited **PD-029**, which the log had already assigned to the C4 spine renumbering. Corrected to PD-040 on import.
**Affected files:** `blocks/C1/_wip/C1_ENG_Block06_Pronoun_v1.md`; pointer owed on `C1B05-PT`; C1 Drive Plan §4 W6 row.
**Status:** Ruled (Principal, 09.08.26).

---

### PD-041 — C2: combined Block 6a + 6b Performance Test `C2B06ab-PT` (reverses the 08.08.26 disregard)
**Decision:** 6a's Thursday Performance Test was postponed by a holiday; both halves of the two-week Block 6 now fall on one Thursday and are delivered as a **single combined test, `C2B06ab-PT`** (30 marks), covering 6a (doing words · am/is/are) and 6b (have/has · match). This **overrides PD-025's one-PT-per-week shape for this cycle only**. Consequences recorded: (a) 6a's master has no live standalone PT this cycle — its items are carried into the combined PT, and a dependency pointer is owed on the 6a master; (b) the combined PT is the **first retention signal** for the whole two-week block, so it — not a separate 6a PT — sizes the post-W6 batch (Run Book §9.8); (c) the have/has section of the PT reuses **5 held subject+object strings** from the worksheets because the Class-2 held-scope have/has pair space is exhausted by eight full-scale worksheets — verbatim-disjointness is **waived for the have/has section only**; dictation, doing-word, am/is/are and match remain fully disjoint. ID coinage `C2B06ab-PT` follows the Run Book §7 half-qualifier convention, extended to a combined test.
**This reverses an earlier ruling.** On 08.08.26 the "combined 6a+6b PT / PD-028" line in the C2B06b kickoff was ruled a **stale citation and disregarded**, and the approved Phase 3 blueprint was built on a standalone `C2B06b-PT` per PD-025. On 09.08.26 the Principal ruled that the combined test is what is wanted: the chat-built 6b master stands, the 08.08.26 disregard is **superseded**, and the blueprint and `blocks/C2/_wip/STATE.md` are corrected to match. The earlier ruling is retained struck through, not deleted (Charter §K.3).
**Supersedes:** PD-025 for this cycle only; the 08.08.26 C2B06b STATE decision 1.
**Affected files:** `blocks/C2/_wip/C2_ENG_Block06b_HaveHasMatch_v1.md`, `blocks/C2/_wip/C2B06b_blueprint.md`, `blocks/C2/_wip/STATE.md`; pointer owed on `C2_ENG_GrammarBlock06a_Verbs_v1.md`; C2 Drive Plan §4 / §7 forward-only note.
**Status:** Ruled (Principal, 09.08.26).

---

### PD-042 — House character **Rabab** is male (Charter §H.5 amendment); project-wide non-mahram re-screen owed
**Decision:** Charter §H.5's house-character roster lists Rabab among the girls' names. Rabab is **reclassified male**. The C2 Block 6b Principal review pass applied this immediately: a non-mahram sweep of that block fixed four female+Rabab / cross-gender pairs (Porshi and Rabab ×3, Maryam and Yusuf). Because the roster is used drive-wide, a **project-wide §H.4 non-mahram re-screen of every delivered block** is owed — flagged here, not yet run.
**What led to this:** the 6b build cited a provisional **PD-030**, a number the log had already assigned to the `C4B04-AK` consolidation. Corrected to PD-042 on import.
**Affected files:** Charter §H.5 roster; `CLAUDE.md` §5 house-character line; every delivered block master (re-screen pending).
**Status:** Ruled (Principal, 09.08.26). Re-screen **OPEN**.

---

### PD-043 — C3: combined Block 6 (Article) + Block 7 (Adjective) Performance Test `C3B0607-PT`
**Decision:** Block 6's Performance Test was postponed by the holiday, so Blocks 6 and 7 are assessed together in one combined Thursday test, **`C3B0607-PT`** (34 marks: Article 9 · Adjective 11 · shared dictation 10 · self-try 4), scored at 0.5 marks per sentence in Parts B, C, E and F. The PT leads with dictation (Part A) then grammar (Parts B–E) as a single continuous A–E run — a deliberate house convention that reverses the binding-paper order.
**What led to this:** the C3 Block 7 build cited a provisional **PD-031**, already assigned to the sacred-words-in-match ruling. Corrected to PD-043 on import. The same file's answer-key heading read `C3B07-PT` against a paper ID of `C3B0607-PT`; corrected to the canonical ID.
**Affected files:** `blocks/C3/_wip/C3_ENG_Block07_Adjective_v1.md`; C3 Drive Plan §4 / §7 forward-only note.
**Status:** Ruled (Principal, 09.08.26).

---

### ⚑ Numbering defect flagged 09.08.26 — **PD-036 is assigned twice**
`PD-036 — The genuine C5 Annual-2025 paper is in the project; the binding set is four` and `PD-036 — Cross-sheet repetition gate: no carrier sentence repeats across a block's sheets` are both present in this log under the same number. Both are live and cited in delivered files (C5 Drive Plan v1.7 and the C4B06 promotion respectively). **Pending Principal ruling** on which keeps PD-036 and what number the other takes. Not resolved silently. No new PD number was consumed by this flag.

---

*End of working log as of 01.08.26. Several items from the most recent Class 4 Block 02 and Class 3 Block 02 discussions are still pending your classification/confirmation and are not yet included above.*
