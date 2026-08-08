# C4 Block 6 — build state

**Block ID:** `C4B06` · **Week:** W6 (Sun–Wed teaching, Thu combined PT) · **Master:** `C4_ENG_Block06_Preposition_v1.md` (v1.3, recovered)
**Topic:** Preposition — place / time / relation; identify (P.O.S.) + use.
**Active build switched to C4B06 on 08.08.26 at the Principal's instruction.** `C2B06b` is parked at Phase 3.

---

## Phase reached

**Phase 4 — Build: COMPLETE as drafted (v1.3, built 06.08.26). Now in review.**

- **Teacher Script / Teaching Days 1–4 — CHECKED (Principal, prior session). Not re-reviewed, not rebuilt.**
- **CW-1…4 · HW-1…4 · `C4B0506-PT` — audited this session for the first time. NOT clean.**
- Audit suite run: `audits/reports/C4B06_audit_2026-08-08.txt`. Manifest: `_wip/C4B06_manifest.json` (273 items).
- **4 of 10 gates FAIL.** The block **cannot be presented for "done"** until each FAIL is corrected or given an
  explicit ruling recorded here (CLAUDE.md §4).

**BC-1 closed** — the master was recovered from `_wip/inbox/`. **BC-2 closed** — Drive Plan v1.11 authored.

---

## Inventory of the recovered master

`C4_ENG_Block06_Preposition_v1.md` — 1179 lines, v1.3, built 06.08.26 with three logged review passes
(v1.1 Clue Card → preposition-only · v1.2 Friday→Sunday day-example · v1.3 adverb/definitions/birthday/terminology).

| Component | Present | State |
|---|---|---|
| Provenance & build-against table | ✔ | cites Drive Plan **v1.11** §2 row 6 verbatim — correct under the new numbering |
| Teaching & sourcing decisions, Teacher checklist | ✔ | — |
| Preposition Clue Card (Place / Time / Relation + Bangla) | ✔ | — |
| Teaching Days 1–4, 6–8 steps each, 12-prompt Exit Check per day | ✔ | **already checked — left untouched** |
| CW-1…4 / HW-1…4 (8 worksheets) | ✔ | **audited this session — defects below** |
| `C4B0506-PT` (Parts A–F, 36 marks) | ✔ | **audited this session — defects below** |
| `C4B06-AK` consolidated answer key | ✔ | keys complete for all 9 artefacts |
| Version log | ✔ | v1 → v1.3 |
| `_wip/C4B06_manifest.json` | ✘ → **built this session** | was missing; CLAUDE.md §4 requires it be maintained *during* the build |
| Audit report | ✘ → **produced this session** | none existed; v1's "all audits green" claim was never evidenced in-repo |

## Reconciliation against PD-029

| Requirement (PD-029) | State |
|---|---|
| Preposition = **Block 6**; master + extract IDs on the new numbering | ✔ IDs are `C4B06-CW1…4`, `C4B06-HW1…4`, `C4B06-AK` |
| Combined **`C4B0506-PT`** grading Block 5 + Block 6 in the W6 slot | ✔ built, Parts A–F, 36 marks |
| `C4B05-PT` retained, not administered separately; pointer in both files | ✔ pointer present at master line 30 |
| Adj/Pronoun items **freshly authored, zero-overlap vs `C4B05-PT` and all Block-5 worksheets** | ✘ **BREACHED — see F2** |
| Ruling cited as **PD-029** | ✘ **master cites PD-028 (×2) — see F8** |

---

## FAILURES — Principal ruling required before any correction is applied

### F1 · CW↔HW overlap — **FAIL on all four pairs** (gate: ≤35%)

`CW1↔HW1 39% · CW2↔HW2 56% · CW3↔HW3 37% · CW4↔HW4 48%`

Broken down by part, the cause is unambiguous — **Part A is fine everywhere; every secondary part shares an
identical key with its pair:**

| Pair | Part A | Part B | Part C |
|---|---|---|---|
| CW1↔HW1 | 30% ✔ | **6/6 = 100%** — both `in · on · under · near · into · at` | 0% ✔ |
| CW2↔HW2 | 30% ✔ | **6/6 = 100%** — both `at · on · in · in · on · at` | **6/6 = 100%** — both `at · at · on · on · in · in` |
| CW3↔HW3 | 25% ✔ | **6/6 = 100%** — both `with · from · of · to · from · with` | 0% ✔ |
| CW4↔HW4 | 35% ✔ | **5/5 = 100%** — both `Preposition · Noun · Preposition · Verb · Preposition` |  |

A pupil holding the classwork can transcribe the homework key **positionally, without reading a single item** —
precisely the risk the gate exists to catch. The item *texts* differ; only the answer **sequences** were reused.
**Fix is cheap:** reorder each HW secondary part (and re-key). No new items needed.

### F2 · PT zero-overlap vs Block 5 — **FAIL** (PD-029 requirement)

Run with the eight delivered Block-5 worksheets + `C4B05-PT` loaded as `audit_scope: pt_overlap_only` reference
sheets (383 comparison items):

- **VERBATIM** — PT **Part E** prompt `meal ______` ≡ **B5-CW1 Part B item 22** *and* **B5-HW1 Part B item 23**
- **VERBATIM** — PT **Part E** prompt `bird ______` ≡ **B5-CW1 Part B item 25**
  → Block 5 CW-1/HW-1 Part B is *"Expand the noun — add a describing word before each noun, write the full
  sentence, underline the adjective"*; PT Part E is the **same task with the same prompt nouns**.
- **NEAR** — PT B3 *"The teacher praised him warmly."* ~ **B5-CW4** *"The teacher praises him warmly."* (tense only)
- **NEAR** — PT D4 *"Mother cooked the meal."* ~ **B5-CW2** *"Her mother cooked a fine meal."*

**The master's v1 version log claims:** *"PT zero-overlap verified against all 16 worksheets (8 Preposition + 8
delivered Adj/Pron, verbatim + 6-word-run)."* **That claim is false.** Two prompts are verbatim duplicates.

*Note:* this run applied the `pt_overlap_only` flag, whose authorisation (**PD-032**) is scoped to a two-week
`a`/`b` split block. PD-029 states the paired-week recovery is **not** governed by PD-025/PD-032. **Using the flag
here needs an explicit ruling or a scope extension** (staged question 4 — now live).

### F3 · Held-word — **FAIL: `quickly` is a W7 word graded in a W6 block**

- **CW-3 Part A #2** — *"The doctor runs **quickly**."* → keyed **Adverb**
- **HW-4 Part A #16** — *"The doctor runs **quickly**."* → keyed **Adverb**

File 2 releases `quickly` at **W7**. The W6 adverb batch is *always · carefully · slowly · happily · loudly*.
A graded answer on an unreleased word. **Hard defect — no reading of the rules permits it.**

### F4 · Held-word — **`run` is not in File 2 in any form**

- **HW-1 Part A #9** and **CW-4 Part A #11** — *"The boys **run** fast."* → keyed **Verb**.
  Not `run`, not `runs` — absent from the pool entirely, and not in the declared block-local set.

### F5 · Undeclared non-held vocabulary on the graded surface

The master declares **one** non-held set: a block-local **place-noun** set of ten (*box, ball, desk, table, chair,
bag, gate, wall, bed, pot*). Nine of those are used and are properly covered. **Everything below is used on
graded sheets and is declared nowhere:**

- **Time nouns (12)** — `dawn, evening, July, June, Monday, night, Saturday, spring, summer, Sunday, Thursday,
  winter`. These are the **objects of the graded time prepositions** and carry all of Day 2, CW-2 and HW-2.
  The block teaches time prepositions without declaring a single time noun.
- **Other (10)** — `bench, corner, drawer, garden, grandfather, hole, poor, porch, room, run`.
  `garden` is a **PT Part E graded prompt**; `bench, corner, drawer, porch, hole, grandfather` sit in the PT.

Under Drive Plan §5 a non-held word may appear in a *teaching example* but "never as the answer in a graded item."
These are carriers inside graded items, not answers — a boundary the Drive Plan does not settle. **Needs a ruling:**
extend the block-local declaration to cover the time nouns and PT carriers, or recast the items onto held words.

### F6 · Values lexicon — singing content on six graded items

The gate caught **one** (`HW-2 Part B #24` — *"The birds **sing** ___ the morning."*). It missed five more
because the lexicon matches whole tokens and these are inflected (**F10**):

| Sheet | Item |
|---|---|
| CW-1 A2 · CW-2 A13 · CW-4 A10 | *"A **small** bird sang."* |
| HW-3 A2 · CW-4 A9 *(same sentence, two sheets)* | *"The girl **sings** loudly."* |
| HW-4 A3 | *"The girl **sings** happily."* |

**The delivered Block 5 set precedent** (v1.11): *"His sister **sings** very well"* → *"reads very well"*;
*"a beautiful bird **sang** sweetly"* → *"sat on the branch"*, both under *"Content-rule (no music/singing/dancing,
Charter §H)"*. On that precedent these six items need the same treatment. Carrier verbs only — the graded targets
(*small / loudly / happily*) are untouched by any recast.

### F7 · One-defensible-answer — the Part C match tasks are not uniquely determined

**Script cannot catch this; it is the human gate.**

- **CW-3 / HW-3 Part C** — match `with · from · of · to` to `my sister · my brother · my teacher · my friend`
  (CW-3) / `my aunt · my brother · my cousin · my uncle` (HW-3). **Every one of the 24 pairings is valid English.**
  *with my teacher*, *from my friend*, *of my sister*, *to my brother* — all natural. The keyed answer is
  unrecoverable by the pupil and unmarkable by the teacher. **This task cannot be graded as printed.**
- **CW-1 / HW-1 Part C** — place match is partly constrained but still ambiguous: the key pairs `on → the wall`
  and `under → the table`, yet ***on** the table* is at least as natural, and *at/near the river*, *near/at the
  gate* are interchangeable.

The instruction *"Each preposition fits exactly one"* asserts a uniqueness the item set does not have.

### F8 · Governance citations — three wrong, one missing

| Where | Cites | Should cite |
|---|---|---|
| line 23 (provenance), line 1179 (v1 log) | **PD-028** for the *block-local place-noun set* | **PD-012** — block-local teaching set. PD-028 is the **C3 Block 7 adjective weighting** and has never governed block-local words under any numbering. |
| line 30, line 1028 (PT banner) | **PD-028** for the *Block 5 → 6 PT carry-forward* | **PD-029**. This is the exact stale citation PD-029's own Numbering note documents. |
| line 24 — *"No PD-009 / PD-011 mechanism needed"* | *(nothing)* | **PD-026** — function-word grammar targets take none of the three non-held statuses. The claim is **correct in substance**; it simply cites no authority. |

Charter §K.3 protects *delivered* files from retro-editing. **This master is an unpromoted `_wip` draft**, so
correcting the citations before promotion is in scope — but it touches governance references, so it is flagged,
not silently changed.

### F9 · Cap arithmetic — "nine" prepositions, ten listed

Lines 40, 46 and 107 all say **nine** cap prepositions and then list **ten**:
*in · on · under · at · with · from · into · near · of · to*. The Drive Plan §2 cap lists the same ten. Cosmetic,
but it is in the teacher-facing checklist.

### F10 · Adverb missing from four Part A option lists **while those sheets grade adverb**

| Sheet | Option list | Adverb-keyed items |
|---|---|---|
| CW-1 | Noun, Verb, Adjective, Pronoun, Preposition | **#19** |
| CW-2 | Noun, Verb, Adjective, Pronoun, Preposition | **#9** |
| CW-3 | Noun, Verb, Adjective, Pronoun, Preposition | **#2** |
| HW-3 | Noun, Verb, Adjective, Pronoun, Preposition | **#2** |
| CW-4 / HW-4 | noun, verb, adjective, **adverb**, pronoun, preposition | ✔ consistent |

v1.3's log states it fixed *"the **CW-4 and HW-4** Part-A instructions"* — it fixed only those two. Four sheets
still ask for an answer the printed options exclude. Same defect class as Block 05 v1.11 item (1).

### F11 · Attribution screen

*"A **tall** tree gives shade."* — **CW-1 A11** and **CW-2 A8**. The standing screen recasts natural phenomena
given as autonomous agents (*"the sun gives…"*). Graded target is *tall*; a recast costs nothing.

### F12 · PT Part F — `this` has no marking note

Self-try box: `on · near · from · kind · this · them`. Under the C4 boundary *this* before a noun is an
**Adjective**, standing alone a **Pronoun**. The pupil supplies the sentence, so **both are correct depending on
what they write** — and the rubric scores "correct word-class placement". The AK gives the marker no guidance.

---

## Gates that PASS (no action)

- **De-patterning** — 25 answer sets, max run ≤2, no strict alternation.
- **Within-sheet duplicates** — clean.
- **Rehearsal/graded disjointness** — PT self-try box (`on · near · from · kind · this · them`) shares nothing
  with the Wednesday demo set (`under · at · with`).
- **Mark totals** — all nine recomputed from the key and equal to every stated total:
  CW1 37 · HW1 31 · CW2 38 · HW2 32 · CW3 36 · HW3 30 · CW4 31 · HW4 31 · **PT 36**.
- **Sacred-word guard** — clean; dictation list (`pollution · waste · smoke · noise · air · ear · kindness ·
  people · street · clothes`) is the W6 held batch, no sacred word, no block-local word (PD-012 compliant).

## Tooling defects found in the audit suite itself

- **T1 — no `block_local` field.** `gate_heldword()` knows only `exemplars`. A block using **PD-012** cannot pass
  the gate without misdeclaring its block-local words as PD-009 exemplars. Needs an additive `block_local` list,
  same shape as the `audit_scope` flag. **This is why F5's list reads long — the script has no way to see a
  legitimate PD-012 declaration.**
- **T2 — values lexicon misses inflections.** `VALUES_LEXICON` is matched against whole normalised tokens, so
  `sing` catches *sing* but not *sings · sang · singing · songs*. Five of the six F6 items evaded it. Needs
  stem/prefix matching.

Both are **additive script changes touching `audits/`** — same approval class as the PD-032 change, so neither is
made without instruction.

---

## Decisions confirmed

| # | Decision | Who / when |
|---|---|---|
| 1 | BC-1 ruled *"partially built — recover what exists"*; master supplied via `_wip/inbox/`. | Principal, 08.08.26 |
| 2 | BC-2 ruled *"author Drive Plan v1.11 now"*. Written, forward-only; spine now 16 blocks, Preposition = 6. | Principal, 08.08.26 |
| 3 | Teacher Script / Teaching Days 1–4 already checked — **not re-reviewed, not rebuilt** this session. | Principal, 08.08.26 |

## Exact next step

**Principal rules F1–F12.** Nothing in the master has been edited — the recovered file sits unmodified in
`_wip/inbox/`, and all findings are recorded here against it.

Recommended order once ruled: **F3 · F4 · F10** (single-item fixes, no knock-on) → **F1** (reorder HW secondary
keys; no new items) → **F6 · F11** (carrier-verb recasts on the Block 05 precedent) → **F7** (Part C match tasks
need redesign, not repair) → **F2** (re-author PT Part E prompts + B3/D4) → **F5** (declaration or recast — the
one that may need new vocabulary) → **F8 · F9 · F12** (citations, arithmetic, marking note).

Re-run `audits/scripts/run_all.py` after every correction; the manifest at `_wip/C4B06_manifest.json` is built and
must be kept in sync. **No promotion to `blocks/C4/` until every gate is PASS or carries a ruling recorded above.**
