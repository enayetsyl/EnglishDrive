# C4 Block 7 — build state

**Block ID:** `C4B07` · **Block:** Verb & Subject–Verb Agreement · **Week:** W7 (solo, FULL, protected)
**Status: PHASE 2 ISSUED (10.08.26). No master drafted. Awaiting Principal rulings on Q1–Q4.**
Question list: `blocks/C4/_wip/C4B07_phase2_questions.md`.

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

**Phase 2 — one consolidated Q&A list** to the Principal (the five pending questions above).
No build content, no sentence bank, no blueprint until those are answered.
