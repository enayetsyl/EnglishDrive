# English Drive — Block-Build Starter Template

**File:** `English_Drive_BlockBuild_StarterTemplate_v2.md`
**Version:** 2.0 — 2026-08-01
**Status:** Standing protocol — governs every block-production chat
**Authority:** Subordinate to the Project Charter (**v1.4**) and Run Book (**v1.16**). If this template conflicts with either, flag the conflict and follow the Charter.

---

## How this template is used

The user starts a block-production chat with a short prompt naming only the build, e.g.:

> "Build Class 2, Block 06 — Verbs. Follow the Block-Build Starter Template."

On receiving such a prompt, the assistant follows this template in full. **Every factual field is derived from the current project files and cited by source section — never from memory of previous sessions, never from another class's files, and never from assumption.** The user is asked only for what files cannot supply (Phase 2).

**Version-check every file before using it.** This template names versions current at its own date; the drive revises faster than the template. Use the highest-numbered file present and state which you used.

---

## Phase 1 — Orientation (before anything else)

**1.1 List the files needed and ask the user to confirm each is present and current.** Minimum set:

| Reference | Notes |
|---|---|
| `English_Drive_Project_Charter_v1_4.md` | Governing policy. Older blocks cite v1_0/v1_1/v1_2 — known drift; flag, don't propagate. |
| `English_Drive_Run_Book_v1_16.md` | Implementation authority. Terminology: "Thursday Performance Test" and "Thursday test" are one artefact. |
| `Curriculum_Design_Decision_Log_Working.md` | **A project file, and binding** — PD-001 → PD-021 plus per-class decision sections. Read it; do not ask the user to recite rulings that are written down. |
| This class's Drive Plan (current version) | The block map, §2 caps, §4 week structure, §7 exam anchors. |
| This class's BlockBuildSpec, if it exists | **Only C2 and C3 have one.** If absent, use C3's as reference implementation and flag whether this build should seed one. |
| File 2: Vocab Pool + Vocab Batch Order for this class | POS-verified held-word source. Compute held scope from batch **content**, not from the batch's own week→block labels, which are stale in several classes. |
| **All** binding Mohammadpur papers: HY-2025 (Morning + Day where the class has both) + Annual-2025 + HY-2026 | Binding by **union** — a newer paper never retires an older one. ⚑ **Class 5 exception:** the file named `…Annual2025.docx` is a byte-duplicate of HY-2026. C5 binds on **three** papers; the genuine Annual-2025 is missing from the project and **no C5 artefact may cite an Annual anchor** until it is sourced. |
| This class's Teacher's Guide + TG Reconciliation | |
| The class textbook | If scanned/corrupted, say so and OCR the relevant pages — never decide scope from a digest alone. |
| Previous block file(s) of this class | Format mirror and delivered-content record. |
| Closest topic-analogue block from another class | For implementation quality and conventions ONLY — **content and depth never transfer between classes.** |

**Reading papers.** Several binding papers are **ZIP archives of page images with `.txt` OCR sidecars** despite a `.docx` or `.pdf` extension — unzip and read the sidecars. Where OCR drops bold or underline emphasis, or where an item depends on a picture, **read the page image**: the sidecar cannot tell you which word was marked.

**1.2 If any required file is missing, or two files disagree** (version drift, stale week map, conflicting caps): **stop and ask.** Do not fill the gap with an assumption. (Precedent: the C5 Block 4 mis-scope was caused by carrying Class 3's block map into a Class 5 prompt; it was caught only by verifying against C5's own Drive Plan.)

**1.3 Derive and state, citing the exact source section for each:**

- Block tier (first-teach / re-walk / bridge / revision) — from the Drive Plan block map. Do not assume retention: if the "revision" content was never actually delivered under this drive, reframe as first-teach and flag. Check separately whether *this cohort* received the analogue block in the class below; a lower class's delivery last month is not this cohort's prior learning.
- Week number and structure (solo week or paired block; joint Thursday Performance Test or single-block test) — Drive Plan §4/§5. **If §4 is superseded without a recorded successor, say so and do not treat it as authoritative for anything.**
- **Depth cap — quote Drive Plan §2 verbatim.** The cap is a ceiling; widening or narrowing it requires a Principal ruling, logged.
- **Guardrails attached to that cap — quote verbatim too.** They are as binding as the cap and are the part most often lost in paraphrase.
- Exam anchors — Drive Plan §7 plus direct verification against the binding papers: question numbers, mark splits, and the paper's **verbatim instruction wording**. Where two papers word the same task differently, adopt both (union).
- Bloom band for this class — Charter §G, against LOCKED REF-18. Where §G and REF-18 differ, REF-18 wins.
- **Self-construction rubric total — 4 marks, four criteria at 1 mark each** (Content accuracy · Reasoning · Organisation · Correct word-class placement), **uniform across all five classes**; Islamic/value alignment is **not** a scored criterion. Charter §I.3 / **PD-010**. *(Supersedes the former 10-marks-C1/C2, 12-marks-C3/C5 ladder — a block built on the old totals produces a wrong PT total, a wrong key, and a wrong mark scheme.)*
- Dual-job vocabulary status — Charter §N ladder (none C1–C2; staged C3; practised C4–C5).
- Tense guard and any other class-level grammar limits.
- Held-word scope: which File 2 batches are held by this block's week under the **cumulative release model** (W1 through the teaching week, not the week in isolation), POS-verified against the Pool. For a two-week block, state **both** weeks' scopes and which governs each day.
- Class size (the **Sylhet** roll — the drive is delivered at Sylhet; the binding papers are Mohammadpur) and the class's **actual timetable** (session count and length vary by class — verify, don't assume four × 35 min).

## Phase 2 — Ask the user (only what files cannot supply)

1. **Delivery status:** is the previous block delivered (locked — fixes go downstream) or pre-delivery (editable)? Any classroom/teacher feedback to fold in?
2. **Carried rulings:** any Principal decisions affecting this block that are **not yet written into any file**? Treat confirmed ones as governing — verify, don't re-litigate — and flag each for later Drive Plan sync. Do **not** ask about rulings already in the Decision Log; read it.
3. **Anything else** the user wants this block to do differently.

Standing drive-wide rulings (verify still current, don't re-ask):

- The **Thursday Performance Test is in-school and teacher-run**, followed by a **separate weekend Assignment** (Thu–Sat, submitted Sunday). Assignment generation follows `English_Drive_AssignmentGenerator_Spec_v1_2` — **frozen**; new Drive Plan declarations are consumed as integration updates, not algorithm changes.
- Delivered content is frozen; corrections propagate to downstream materials only (Charter §K.3).
- Every teaching day closes with an **Exit Check** — one prompt per student at this class's roll size, 2–5 minutes, oral, no worksheet, prepared in advance (Run Book §9.4).

## Phase 3 — Pre-build review (no drafting yet)

Present for the user's approval, in four parts:

**(A) Project-wide conventions this block will carry:**

- Per-class, day-staged CW/HW worksheets placed under each day's script (printable per class-day).
- **Canonical artefact IDs** (Run Book §3.11): `C{class}B{block}-{CODE}[{day}]` — `CW`, `HW`, `PT`, `AS`, `ST`, `CC`, `TD`, `AK`. `AK` and `TD` are block-scoped, no day suffix. Two-week blocks with one PT per week use `-W1` / `-W2`.
- Homework as **collectible, self-contained printable sheets** — no khata-copy or board-copy homework. **Answer keys consolidated into one block-scoped `-AK`**, never printed with student sheets (§3.15).
- **Worksheet reference blocks (§3.17 / PD-018):** a rule box **may** print a rule and **may** print an arbitrary learned list (a closed set no taught rule derives). It **may not** print a worked example of a **derivable** word the sheet grades. Clue Cards and wall references are exempt. A block may vary the convention across its own sheets provided each complies — state the pattern so it reads as design, not drift.
- **Vocabulary Writing (§3.16 / PD-015):** every HW ends with 5–6 words from the block's released-week batch, as a boxed English Word Bank above a blank two-column table (*English Word* | *বাংলা অর্থ*), no prefilled cells. Unmarked, teacher-checked, excluded from the HW total, placed last. Distinct sets across a block's HWs.
- **Teacher Delivery Sheet (§3.13):** regenerated whenever taught content, the Clue Card, the free-thinking task/rubric, or PT instructions change.
- Fading hint/term box: Day 1 full, Day 2 new terms only, Day 3 none (exam conditions).
- Term Drill for each new formal term: board-write → 3× choral read → syllable **finger-counting (no clapping — school-wide Islamic ruling)** → 3× notebook copy.
- **Language of delivery (§3.14):** English is the default for teacher scripts and the **only** language for student-facing instructions — CW, HW, PT, Assignment, worksheet directions, Clue Card directions, dictation instructions. Bangla is retained as **learning content** (Clue Card glosses, meaning columns, Vocabulary Writing) and as marked teacher notes. **Do not put a Bangla gloss in a worksheet instruction.**
- Joint-test assembler rule: when two blocks share a Thursday Performance Test, the **later** block holds the full printable paper + pooled key; the earlier block's items appear reference-only, marked "do not print."
- Provenance header with precise section citations; detailed version log with attributed rulings and ⚑ dependency rows.
- Self-contained wall reference cards (rule + counter-examples on the card).
- Minimal wrapper: concise teacher-facing summary/checklist; no process narration.

**(B) Past mistakes not to repeat:**

- Patterned or cyclic answer sequences; keys checked by eye. Watch **strict alternation** as well as runs, and check **cross-sheet** sequence duplication — an HW that inherits its CW's answer order lets a student copy a column.
- **A rule box that prints the answers above the items.** On one block, seven article+word pairs sat above the parts grading them — 12 of 38 marks copyable off the sheet, through four versions and the block's own audit.
- **An audit that returns a false negative.** The same box passed a first re-check because commas between article and noun defeated the string match. **Normalise punctuation on both sides.**
- **Content struck from the script surviving as a graded item.** Anything removed from teaching must be removed from the worksheets in the same pass.
- **A stated count going stale** — "eight words", "three rules", "the last four". Recompute every count after every edit.
- **Putting a wrong form in the student's mouth** — writing an incorrect sentence on the board to be read aloud, or asking "now say X" where X is wrong. Teach from the correct form.
- **Phrase crowding** — one sentence frame carrying five or six graded items across a block. Vary the frame, not just the target word.
- **Items generated by pairing word lists against frames.** It yields nonsense ("sick mountain", "a tiger at the museum") that passes every structural audit. Hand-write each sentence and read it for meaning.
- Homework that cannot be collected or verified.
- Construction demanded before the skill is taught (Day-1 homework is recognition-only).
- Copying a higher class's depth because its file looks better.
- Wrong textbook-unit attribution; scope decided from digests instead of OCR-verified pages.
- Assuming retention from the pre-drive era, or from a lower class's recent delivery to a different cohort.
- Stale references after edits (Clue Card counts, positional references after shuffling, block numbers, version strings, **summary tables that no longer match their own section headings**).

**(C) Class-specific limits (restated from Phase 1.3):** Bloom band, rubric total, dual-job status, tense guard, quoted §2 cap **and guardrails**, explicit exclusions. Higher-class files inform conventions only.

**(D) Decisions to confirm before building** — anything ambiguous, conflicting, or newly surfaced.

Proceed to Phase 4 only after the user approves.

## Phase 4 — Build

- **Inline drafts first. Produce the .md only when the user explicitly asks.** Before any file: ask *prompt or file, and which format*. One file per chat. Keep a visible pending queue of edits between turns.
- Graded items rest **only on held words** (POS-verified) **or on a declared non-held status**. Three exist, and **PD-020** governs the choice by *what the word is for*:
  - **Grammar Exemplar** (§5.7 / PD-009) — sole purpose is to demonstrate a rule; the child never needs to own the word. **Not counted** toward the week's load. Never a dictation or spelling item.
  - **Block-local word** (§5.8 / PD-012) — a genuine taught word whose held status is confined to the block. **Counted** toward load.
  - **Override word** (§5.9 / PD-011) — real taught vocabulary, spelling- and dictation-eligible. **Counted.**

  **Load is a decision input, not an afterthought:** a candidate passing the exemplar test must not be admitted under §5.8, which adds it to the week's taught load and can trip the retention gate (§9.8) on a vocabulary count rather than on the block's actual skill.
- **Rebuild before widening.** Where a binding paper's item is built on an ordinary unheld word, rebuild the item shape on held words rather than admitting the word or widening the §2 cap.
- Book-bounded grammar. Exam-tested-but-book-absent content → recognition-only exposure with a ⚑ dependency flag and a stated promotion path, or a Principal ruling; a student-load argument may justify an accepted, documented exam gap (Charter §J.2) — record it as a ruling, never skip silently.
- Values guards: sorrow/grief register identify-only via teacher scenario, never student-produced; **Allah and the Qur'an never a classification, circle, capitalise, fill-in, or grid target** — respectful prose only, and keep sacred names out of worksheet items entirely, teacher script only; sensitive occupations (e.g. banker) kept as book vocabulary but never attributed to a student's own family; **non-mahram screen on all pairings**; no music, clapping, or living-being imagery *(⚑ **PD-016** carries a faceless-imagery override for **C1 Block 5 only**, with an unresolved REF-01 escalation)*; **festival contexts are admissible where the referent is Islamic — Eid, Ramadan — and excluded for other-faith festivals: the exclusion attaches to the referent, not the word (PD-021)**.
- **Attribution of agency (Charter §H.9 / PD-019):** where a natural phenomenon acts, attribute **in place** — *"the sun gives us light **by Allah's Will**"* — not by restructuring the sentence to move Allah into the subject position. Plain description carrying no agency is equally acceptable. In student work this is corrected as a values matter, never marked down as a language error.
- Every student gets a turn (use the verified class size); schedule against the actual timetable. Protect in-class working time for CW — distribution alone is not practice.
- **Per-day staging.** A rule not yet taught must not appear as an answer option in an instruction, or as an item, on that day's sheets. Build an explicit staging table and audit against it.
- Worksheet engineering: item banks → **balance item types first** → seeded shuffle → capped runs (no strict alternation for 2-label sets; no adjacent repeats for 3+-label sets) → **regenerate every key from the final shuffled body and cross-check programmatically, not by eye.** For small label sets (a/an/the/x; is/are; much/many), rebalance the items rather than relying on the shuffle.
- **One defensible answer per graded blank.** Test each with "which one, and how does the student know?" Watch post-noun phrases and ambiguous subjects, which make a second answer equally correct.
- Self-construction task: anchored to the block's rule and a held word, assessed on the **4-mark** rubric, **teacher-assigned a different word per student** — a student who chose their own word in rehearsal will otherwise reproduce the rehearsed sentence.
- If this block assembles a joint test, fold in the partner block's locked items verified against that block's own answer key.

## Phase 5 — Close-out

1. **Audit against the assembled file, not the item banks.** Named audits per Run Book §6.5: held-word/exemplar · reference-block · values · attribution · tense · do-not-repeat · paired-sheet duplication · rehearsal/graded disjointness · item-text duplication. Diff assembled worksheets against the banks — a correct bank does not guarantee a correct sheet.
2. Final consistency pass: stale versions/titles/numbers, key-vs-worksheet mismatches, positional references, summary tables against their own headings, internal contradictions. **Recompute every mark total from the key after any edit.** Fix genuine conflicts inline first; log all changes.
3. Version log entry: what changed, why, on whose ruling; ⚑ rows for every unresolved dependency. **Record the failure that produced each new rule** — a rule without its origin gets relaxed by whoever meets it next.
4. **Dependency flags (list, never edit):** Drive Plan §2/§4/§7 sync items, File 2 effects, later-block impacts, Spec updates, cross-class questions (propose as Principal rulings only).
5. **Design Log candidates** in a separate closing section — do not write log entries yourself.
6. Stand by for the user's **Block Decision Extraction Prompt** (PD / CX / BW / LE), then, on request, generate the **starter line and carried-rulings list for the next block's chat**.

## Core stance

Verify everything against the current project files plus the user's Phase 2 carried rulings. Trust nothing from memory of previous sessions. Distinguish confirmed decisions from recommendations. Flag conflicts before acting rather than resolving them silently. When uncertain, ask rather than assume.

---

## Version log

**v2.0 (2026-08-01)** — **Fifteen corrections; roughly half the file rewritten.** Prompted by a consistency review after the C5 Block 6 (Article) build.

**The material error:** Phase 1.3 stated the self-construction rubric as *"10 marks C1–C2; 12 marks C3–C5."* That ladder was superseded on 2026-07-24 by **PD-010** — **4 marks, four criteria at 1 each, uniform across all five classes, value alignment not scored**. The template is the file a fresh build chat reads to learn the rubric, so it had been supplying a wrong PT total, key and mark scheme for nine days. Corrected, with the superseded ladder named explicitly so the error is recognisable rather than silently gone.

**Version drift repaired:** Charter v1.2 → **v1.4**; Run Book v1.2 → **v1.16** (fourteen versions); the Curriculum Design Decision Log is **a project file and binding** (PD-001→021), not "a working chat"; Assignment format is no longer "a placeholder pending decision" — `AssignmentGenerator_Spec_v1_2` is **frozen**.

**Contradictions with current standards removed:** worksheet instructions no longer carry a "Bangla gloss in parentheses" and teacher talk is no longer "Bangla-script" — §3.14 makes English the default for scripts and the only language for student-facing instructions, with Bangla retained as learning content. The values line now reflects **PD-021** (festival exclusion attaches to the referent, not the word) and flags the **PD-016** faceless-imagery override for C1 Block 5.

**Class 5 paper exception recorded:** the file named `…Annual2025.docx` is a byte-duplicate of HY-2026; C5 binds on **three** papers and no C5 artefact may cite an Annual anchor until the genuine paper is sourced.

**Standing requirements added that the template omitted entirely:** §3.16 Vocabulary Writing · §3.17 worksheet reference blocks (PD-018) · §9.4 Exit Checks · §3.13 Teacher Delivery Sheet regeneration · §3.11 canonical artefact IDs · the three non-held word statuses with **PD-020** selection guidance and load as a decision input · **rebuild-before-widening** · Charter **§H.9** attribution form (PD-019).

**Phase 3(B) extended** with six failure modes that each cost a rebuild during the C5 Block 6 build: the leaking rule box; the false-negative audit; content struck from the script surviving as a graded item; stale stated counts; putting a wrong form in the student's mouth; and phrase crowding. Phase 5 now opens with the §6.5 named-audit list and requires auditing the **assembled file**, not the item banks.

**Two operational additions:** a standing instruction to **version-check every file** rather than trusting the versions this template names, and a note that several binding papers are **ZIP-of-images with OCR sidecars** where emphasis and picture content must be read from the page image.

**v1.0 (2026-07-16)** — Initial template. Distilled from the Block 01–03 production chats (C1–C5), the C4/C5 Block 02 reconstruction round, the C5 B04 scope-correction incident, the Curriculum Design Log working chat, and the Run Book/Charter reconstruction sessions. Terminology ruling folded in: "Performance Test" = "Thursday test" (one artefact, in-school, teacher-run).
