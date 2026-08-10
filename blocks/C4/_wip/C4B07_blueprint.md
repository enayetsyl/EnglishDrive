# C4B07 — Phase 3 · Pre-build review blueprint

**Block:** Verb & Subject–Verb Agreement · **W7** · solo, FULL, protected · 4 days Sun–Wed, 35 min
**Status: AWAITING APPROVAL. No build content drafted.** Nothing below is a sentence bank or a graded item.

Binding into this build: Drive Plan **v1.11** §2 row 7 · **PD-056** (no pronoun declaration) ·
**PD-026** (`is/are`, `has/have`, `each` are closed-class grammar targets) · **PD-035** (recast, not declare) ·
**PD-036/PD-038** (cross-sheet repetition, threshold 0) · **PD-054** (clue/instructions/boxes screened) ·
**PD-010** (self-try rubric = 4 marks) · Phase 2 rulings Q1–Q5.

---

## 1. Learning outcomes

By the end of the block a Class 4 pupil can:

1. Find the verb in a simple present sentence.
2. Decide whether the subject is **one** or **more than one**.
3. Add **-s / -es / -ies** correctly to the verb when the subject is one (3rd person).
4. Choose **is / are** and **has / have** to match the subject.
5. Apply **each + singular**.
6. **Find and fix** a wrong agreement (*He go → He goes*) — the Analyze rung, §6.

Out of scope, stated so the teacher does not drift: any tense but simple present · negatives · questions ·
full person paradigms · irregular past forms (Block 8).

---

## 2. Day staging

| Day | Focus | New load |
|---|---|---|
| **Sun (1)** | Find the verb · one vs more-than-one subject · **-s** on regular verbs | Recognition + the core rule |
| **Mon (2)** | **-es / -ies** spelling cases (`washes · mixes · finishes · discusses · carries`) | Spelling sub-rule |
| **Tue (3)** | **is / are** and **has / have** · plural-only subjects (`people`, `clothes`) · collectives (`family`, `team`) | Be/have agreement |
| **Wed (4)** | **each + singular** · mixed review · **error-find** (*He go → He goes*) | Analyze rung + integration |

Rationale: the cap makes SVA *"woven into the verb work, not a standalone block"*, so Day 1 teaches the verb
and the agreement rule in one move rather than teaching verbs for two days and bolting agreement on.

---

## 3. Sheet plan

| Sheet | Parts | Items | Marks |
|---|---|---|---|
| CW1 / HW1 | A find-the-verb · B one-or-many · C slash-pair `-s` | 30 / 26 | 30 / 26 |
| CW2 / HW2 | A slash-pair `-es/-ies` · B **single-base-verb** · C error-find | 30 / 26 | 30 / 26 |
| CW3 / HW3 | A `is/are` slash-pair · B `has/have` slash-pair · C **single-base-verb** mixed | 30 / 26 | 30 / 26 |
| CW4 / HW4 | A `each +` singular · B mixed slash-pair · C mixed single-base-verb · D error-find | 30 / 26 | 30 / 26 |
| **PT** | A dictation · B slash-pair · C single-base-verb · D error-find · E self-try | ~32 | **32** |

**1 mark per item throughout (Q3).** Every HW carries the **W7 Vocabulary Writing box** — nouns/adverbs, since
the W7 batch has no verbs (CR-012; not a defect). Exit Check: **12 prompts/day**, C4 roll 12, as C4B05/B06.

**Both item formats appear on every sheet (Q4 ruling).** They are kept in **separate parts** so that
`options` can be declared honestly on the slash-pair parts only — the single-base-verb parts have no printed
option list, and `gate_option_list()` (PD-037 / CR-008 / CR-017) must not be fed a phantom one.

---

## 4. De-patterning design — the CR-020 problem, solved structurally

SVA choose-the-form is binary. At C2B06b, 15 answer sets ran `has·have·has·have…` and **108 of 275 marks were
winnable by alternating without applying the rule**. `gate_depattern()` catches run>2 and strict alternation,
but a *near*-alternating binary set still passes. So this is designed out, not audited out:

1. **Widen the answer alphabet inside each part.** No part is a pure two-value set. A slash-pair part mixes
   `-s/base`, `is/are` and `has/have` targets, so the answer alphabet is **six**, not two. Guessing by
   alternation stops being a strategy at all.
2. **The single-base-verb parts are open-response** — the pupil writes the form unaided, with no options to
   alternate between. Distributing these through every sheet breaks any binary run that survives (1).
3. **Subject-number sequence is authored, not incidental** — max run ≤2, no strict alternation, checked on the
   *subject* sequence as well as the answer sequence.
4. **CW↔HW keys are independently ordered** (CR-006 / `gate_hw_key()`), never a reorder of the same key.

**Proposed additional check, not self-applied:** `gate_depattern()` currently reads the answer sequence. It
would not flag a part whose answers are 2-valued and *nearly* alternating. If you want that closed, it is a
threshold change to an existing gate and needs its own PD — **flagged, not drafted**.

---

## 5. Trigger discipline — the CR-032 blind spot, third occurrence

Every graded answer here is a **verb form** or a **be/have form**, not a content word. That is exactly the
shape that made C3's entire Article half pass vacuously. Therefore:

- **Every graded item declares a `trigger` on its lexical verb** (`play`, `wash`, `carry`), which is held.
- Items whose answer is `is/are`/`has/have` declare the trigger on the **subject noun** instead, which is also
  held; the be/have form itself is PD-026 closed-class and needs no trace.
- **No item declares a trigger on a pronoun.** Pronouns are carrier text (PD-056).
- The manifest is built **during** the build, and the held-word gate must report a non-trivial checked count —
  a "gate is vacuous" warning is a build failure, not a pass.

---

## 6. Content guards active on every sheet

- **§H.3** — `forgive · grant · bless · protect · reward` are held only in the `May Allah ___` base frame and
  are **never** SVA items. No sacred word is ever a graded target.
- **§H.4** no non-mahram pairing · **§H.8** no living-being imagery (the words `bird`/`dog` are fine, pictures
  are not) · attribution screen (CR-004/CR-023 — no autonomous natural givers; this block's verbs make that a
  live risk, e.g. *The rain gives…*).
- **Roster** (§H.5, amended at PD-053): Yusuf, Abdullah, Nusair, Abdur Rahim; Aisha, Raima, Maryam, Fatima,
  Porshi, Rabab, Jesmin.
- **PD-054** — clue glosses in Bangla, and **on this block a clue must not disclose subject number**
  (CR-016/CR-019). Where a gloss would give the answer away, it is omitted rather than translated.
- **Q5** — dual-job words unrestricted on fill-in items, **barred from any word-class identification item**.

---

## 7. Deliverables

`C4_ENG_Block07_VerbSVA_v1.md` (master) · `C4B07_CW1…CW4` · `C4B07_HW1…HW4` · `C4B07_PT` · `C4B07_AK`
(PD-030: keys in `extracts/`) · `C4B07_TD` (Teaching Days 1–4) · Clue Card **Verb + SVA rows** added to the
running Word-Class Clue Card (§8 incremental build, as C4B05 added the Pronoun row) · `C4B07_manifest.json` ·
audit report.

---

## 8. Sentence bank

**Hand-authored and human-vetted (CLAUDE.md §3).** I will draft a candidate bank and present it for your
approval **before any worksheet uses it**. No worksheet item is generated by pairing word lists against
frames. An arrangement engine may order an approved bank; it may never invent pairings.

---

## 9. Approve, or amend

On approval I proceed to **Phase 4**, one unit at a time with a pause between units, starting with the
**candidate sentence bank** for your read — not with a finished sheet.
