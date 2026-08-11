# C4 Block 7 — build state

**Block ID:** `C4B07` · **Block:** Verb & Subject–Verb Agreement · **Week:** W7 (solo, FULL, protected)
**Status: PHASE 4 OPEN — SENTENCE BANK CLOSED AND APPROVED AT 256 (Principal, 11.08.26).
All three units have passed the human naturalness read. Worksheets may now draw on the bank.
No master drafted.**
Blueprint `blocks/C4/_wip/C4B07_blueprint.md` — **APPROVED (Principal, 10.08.26).**
Bank unit 1 `C4B07_bank_S1_S2_candidate.md` (S1–S2) · unit 2 `C4B07_bank_S3_S7_candidate.md` (S3–S7) ·
unit 3 `C4B07_bank_ext_candidate.md` (extensions). **BANK COMPLETE AT 256 — the full block requirement.**
**Human naturalness read — batches 1 and 2 (S1–S7, 160 lines) DONE (Principal, 11.08.26).** Rulings:
**(1)** S7 error-find containment CONFIRMED — never a model sentence, never read aloud as correct, never in a
demo box, never duplicated elsewhere as a correct sentence. **(2)** S3's eight consecutive `washes` lines
ACCEPTED as a held-vocabulary pool limit; File 2 **not** widened in this batch; `carry` retained (the `-ies`
rule needs it); any pool expansion takes its own ruling, per the C3 size-adjective precedent (CR-030 → PD-047).
**(3)** Collective nouns `family`/`team` CONFIRMED singular and **locked as project convention — PD-058**;
British plural usage may not reopen this at audit. **(4)** S3-21 revised → *The doctor discusses the food.*
(**CR-034**). **(5)** S5-15 revised → *Nusair has a new stamp.* (**CR-035**). Both replacements re-checked for
PD-036 uniqueness and held-token status; every word in each is already attested in verified bank lines.
**Unit 3 (extensions, 96 lines) READ 11.08.26 — all five review points ruled KEEP, no line changed:**
S4-42 *Raima is sad* (mild negative state on a roster name admitted) · `destroy` S1-51/S2-56 (W6 pollution
batch, register accepted) · `care for` S1-41/S2-36/S2-59 (two-word verb admitted; agreement sits on
`care`/`cares`) · S1-46 length outlier noted · `near` clearance confirmed and recorded so audit does not
re-flag it. **The §3 human gate is now satisfied for the whole 256-line bank.**
Unit 1's Counts block was stale ("63 … 29 usable, 1 failed") and is corrected to **64** — S2-30 was repaired,
not lost.
Programmatic verification over the whole bank: **256 sentences, 256 distinct (PD-036 zero-repeat holds),
zero unheld tokens, no duplicate IDs.** Two defects were caught by that pass and are now fixed — S2-30 `boys`/`ball`
(**CR-033**, 3rd occurrence of the unheld-word type) and the S1-35/S3-23 duplicate created by relocating
`carries` into Strand 3. A third flag — `near` (S1-47/S1-60/S2-37) — was **checked and cleared**: it is a
function word excluded from File 2 at source and a **Block 6 taught preposition** (56 occurrences in the B6
master; in the CR-006 key), carrier text only, never a graded target. Recorded so it is not re-flagged.

**Unit 4 — answer-key architecture** `C4B07_answer_architecture.md` + `C4B07_number_sequences.json`.
No sentence text, so not blocked by the bank read. **Finding:** `gate_pair_overlap()` measures answer-string
overlap, which in this block is blind — every SVA answer is a different word, so it reads near 0% and passes
meaninglessly. The exploitable dimension is one bit per item, **singular or plural subject**, and no gate
sees it. A binary dimension also **cannot** meet the 35% limit by chance (two random S/P sequences agree
~50%); the undesigned baseline was **50/58/69/38%**. Deliberate anti-correlation brings all four pairs to
**26.9 / 30.8 / 30.8 / 26.9%**, with max run ≤2, no strict alternation, balanced, every part slice
independently valid. **Proposed and NOT self-applied:** an optional item-level `number` field plus
`gate_number_sequence()` — additive, vacuous on existing manifests, but a new gate, so it needs a PD.
No number derived; read the next free one from HEAD when writing it. Matters beyond this block — Blocks 8–11
all grade a binary form choice.

**⚑ Pool finding, flagged not resolved:** the `-es/-ies` sub-rule rests on **exactly five held verbs**
(`wash · mix · finish · discuss · carry`) and **`carry` is the only `-ies` verb in the entire 160-word pool**.
Same shape as C3's missing size adjectives (CR-030 → PD-047): a pool gap, not a block defect. No declaration
proposed — recasting is not blocked, so PD-035 does not authorise one. A wider `-es` set is a File 2 change
and needs its own ruling.
Phase 2 list: `blocks/C4/_wip/C4B07_phase2_questions.md` (all five ruled — see table below).

**Phase 2 headline — the pronoun blocker dissolved on inspection.** C4B07 is recommended **not** to replicate
PD-051: here a pronoun is never the keyed answer (the answer is a verb form), so it is carrier text and the
held-word gate keys on `trigger`; `is/are` blanks are already covered by **PD-026**. What *did* fail is the
cap's own example verb — **`go` is absent from the pool** — and the fix is recast onto the 34 SVA-safe held
verbs, per PD-035's "incidental carriers are recast, not declared". Also verified absent: `be · is · are ·
has · have · student · baker · girl · boy · man`. `child` is held W3; `children` is its taught Block-2 plural.

---

## Phase reached

**Phase 1 — Orientation, read-only. Done.** Record: `blocks/C4/_wip/C4B07_orientation.md`.
Nothing has been drafted. No `C4B07` master file exists and none may be written until the
Phase 3 blueprint is approved.

Sources re-opened at source this session, not cited from a prior session:
Charter v1.6 · Run Book v1.17 · **C4 Drive Plan v1.11** · Decision Log PD-001→PD-055 ·
CORRECTIONS.md → CR-032 · Pool v4 + Batch Order v2 · **all three C4 binding papers parsed from bytes** ·
format mirror **C4B06** (promoted v1.5) · Starter Template v2.0.

## Governance baseline (confirmed this session, neither reopened)

| Ruling | Effect on this build |
|---|---|
| **PD-036** + **PD-038** | Cross-sheet repetition gate, `CROSS_SHEET_MAX_REPEATS = 0`. CW↔HW ≤2 allowance is backstop only |
| **PD-054** | `clue` / `instructions` / `boxes` visible to values, sacred and held-word screens. Held-word binds on `clue` only. Bangla glosses required (CR-011) |

*(PD-055 is the reissued C5 binding-set ruling — C5 only, no effect here.)*

## Decisions confirmed

- Block 7 = Verb & SVA under **PD-029 / Drive Plan v1.11** numbering. Anything citing "Block 7 =
  Preposition" or "Block 8 = Verb" is pre-v1.11 and stale.
- Anchors are **HY25 Q5 (5×2=10)** and **Annual Q7 (5×1=5)** — SVA choose-the-form. **HY26 has no SVA
  question.** The tense fill-ins belong to Blocks 8–11 and are out of scope.
- Held scope at W7 = the **whole 160-word pool**; **39 held verbs**, 34 safe for SVA.
- W7 fresh batch is **17 words, all nouns/adverbs — no verbs**. The HW Vocabulary Writing box is
  noun/adverb by design (CR-012); this is not a defect.

## Phase 2 — RULED (Principal, 10.08.26). All five closed.

| # | Question | Ruling |
|---|---|---|
| **Q1** | Pronoun declaration? | **No declaration — logged as PD-056.** C4B07 does not replicate PD-051; a pronoun is never the keyed answer here, so it is carrier text and the gate keys on `trigger`. `is/are` covered by PD-026. **Closes PD-052's C4 replication flag in the negative** (C1/C2/C5 stay open). `go` is absent from the pool → *He goes* recast onto held verbs per PD-035; survives in teacher script only |
| **Q2** | `each + singular` | **Recast, no declaration.** `each` is PD-026 closed-class; the noun moves to held vocabulary — `Each of the **children** ___ (has / have)` (`child` held W3, `children` its taught Block-2 irregular plural). Anchor subjects likewise recast: `student → child/friend`, `baker → worker` (W6), `girl/boy →` §H.5 roster names |
| **Q3** | PT mark weighting | **1 mark per item throughout**, worksheets and PT. HY25's 5×2 weighting recorded in the Teaching Days notes so the teacher knows the exam may weight the same item double |
| **Q4** | Annual Q7(b) `English ___ (be)` | **Mirror BOTH formats throughout** *(Principal ruled against the agent's slash-pair-only recommendation)*. Graded sheets carry the two-option slash pair **and** the single-base-verb variant. Subjects recast to held vocabulary — the proper-noun subject `English` is not reproduced |
| **Q5** | Dual-job words | **No restriction on SVA fill-in items** (the blank sits in the verb slot, so the frame fixes the class and one answer is defensible). **Barred from any word-class identification item** in this block |

### Build consequences of Q4 (both formats)

- Two item shapes for one skill: **`(walk / walks)`** and **`(be)` / `(go)`-style single base verb**. The
  Teaching Days must introduce both explicitly or the second will read as a misprint to pupils.
- The single-base-verb shape has **no printed option list**, so `gate_option_list()` (PD-037 / CR-008, CR-017)
  applies to the slash-pair parts only. Parts must be split by shape so `options` can be declared honestly on
  the ones that have them.
- The single-base-verb shape is the **harder** item — the pupil supplies the form unaided. Distribute it so it
  does not cluster, and keep the marks equal at 1 apiece per Q3.

## Standing rulings folded in

- **PD-056** — no pronoun declaration (this build).
- **PD-026** — `is/are`, `has/have`, `each` are closed-class grammar targets, not vocabulary.
- **PD-035** — incidental carriers recast, not declared; declaration only where recasting deletes the concept.
- **CR-032** — every graded item declares a `trigger` on its **lexical verb**, never on the pronoun or be-form.

## Superseded — Phase 2 questions as originally issued

1. **Pronoun declaration.** `he/she/it/they/we` are absent from File 2 by design, but the cap's headline
   example is *He goes (not He go)*. C3B08 ruled **PD-051** for the same wall; **PD-052 flagged cross-class
   replication to C4 as NOT executed.** C4B07 needs its own PD-012/PD-035 block-local declaration. **Hard
   blocker** — without it the block cannot legally write its own core example.
2. **`each + singular`** — `each` is a function word, `student` is not in the pool; the anchor item is
   `Each of the students ___ (has/have)`. Block-local or exemplar route needed.
3. **PT mark weighting** — the two anchors disagree (5×2 vs 5×1) on an identical format.
4. **Annual Q7(b) `English ___ (be)`** — single base verb, not a slash pair, and a proper noun subject.
   Mirror the slash-pair only, or carry the variant?
5. **Dual-job POS ambiguity** — one-defensible-answer risk from held verbs that are common nouns and vice
   versa.

## Standing risks carried into the build

- **CR-020 alternation is the dominant risk.** SVA answers are binary (`walk/walks`, `is/are`); at C2B06b
  108 of 275 marks were winnable by alternating. De-patterning must be designed in, not audited in after.
- **CR-032 trigger discipline** — SVA answers are verb *forms*, not content words. Without a declared
  `trigger` on every graded item the held-word gate goes vacuously green over the whole block, exactly as
  it did across C3's entire Article half.
- **CR-016/CR-019 × PD-054** — a Bangla clue on an SVA item can disclose subject number. Care or omission.
- **Optative verbs** `forgive · grant · bless · protect · reward` must never be SVA items (§H.3).
- **File 2 label re-map** — `Weekly Plan!C8` still reads "B8 Simple Past" for W7; weeks trustworthy,
  labels not. Carried forward, not resolved.
- **Bangla `VALUES_LEXICON` widening** — 4 of 22 entries Bangla, English-only inflection matching. Stated
  follow-on to PD-054, not ruled.

## Next step

**Bank approved — Phase 4 continues with Day 1 sheet construction** (`C4B07-CW1` / `C4B07-HW1`) drawn from
Strands 1–2, with the manifest built alongside per CLAUDE.md §4.1 and the `number` sequence from
`C4B07_number_sequences.json` applied at authoring time (de-patterning designed in, not audited in — CR-020).

**⚠ BLOCKER — the audit suite cannot run.** The sandbox shell failed to start on 11.08.26
(`session disk not found`), so `python3 audits/scripts/run_all.py` is unavailable. Under CLAUDE.md §4 no sheet
may be presented as final without verbatim script output. Sheets may be **drafted**; none may be **promoted**
until the suite runs. Do not certify by eye.

**Two proposals still unruled** (both raised earlier, neither self-applied): `gate_number_sequence()` — the
singular/plural bit that no existing gate can see, and which matters for Blocks 8–11 too — and the
`gate_depattern()` threshold for 2-valued near-alternating parts. Both are new/changed gates and need a PD.
Read the next free number from HEAD at the time of writing (PD-058 was taken by this session).

### Superseded — the pre-approval next step

**Phase 3 blueprint issued — awaiting approval.** On approval, Phase 4 opens with the **candidate sentence
bank presented for human read**, not with a finished sheet (CLAUDE.md §3: banks are hand-authored and
human-vetted before any worksheet uses them).

**One proposal raised in the blueprint, deliberately not self-applied:** `gate_depattern()` reads the answer
sequence and would not flag a 2-valued *near*-alternating part. Closing that is a threshold change to an
existing gate and needs its own PD. Flagged, not drafted.
