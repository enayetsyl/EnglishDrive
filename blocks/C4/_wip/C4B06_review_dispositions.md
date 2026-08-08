# C4B06 — review dispositions F1–F12

**Status:** proposals only. **The master has not been edited.** It sits unmodified at
`blocks/C4/_wip/inbox/C4_ENG_Block06_Preposition_v1.md`.
**Scope:** CW-1…4, HW-1…4, `C4B0506-PT`, `C4B06-AK`. **Teacher Script / Teaching Days 1–4 are out of scope** —
already checked, not re-reviewed, not proposed for change.
**Evidence:** `audits/reports/C4B06_audit_2026-08-08.txt` · manifest `_wip/C4B06_manifest.json` (273 items).

**Ruling types:** **[A]** agent may apply on your approval · **[PD]** Principal Decision (governance) ·
**[AUD]** touches `audits/` — approval class of the PD-032 change.

| # | Failure | Type | One-line resolution |
|---|---|---|---|
| F1 | Every CW↔HW pair shares an identical secondary-part key | **[A]** | Reorder the HW items; keys fall out different. No new items. |
| F2 | PT duplicates Block-5 worksheet items | **[A]** + **[PD]** on audit scope | Re-author 3 PT Part-E prompts + 2 near-duplicates. |
| F3 | `quickly` (W7) graded in a W6 block | **[A]** | Swap to a W6 adverb. |
| F4 | `run` absent from File 2 entirely | **[A]** | Recast both items onto held verbs. |
| F5 | 22 undeclared non-held words on graded sheets | **[PD]** | Declare a time-noun set under PD-012; recast the avoidable rest. |
| F6 | Six singing items | **[A]** on Block-05 precedent | Carrier-verb recasts; graded targets untouched. |
| F7 | Part C match tasks have no unique answer | **[PD]** | Redesign as choose-between-two (an exam-used format). |
| F8 | Three wrong PD citations, one missing | **[PD]** | PD-028 → PD-012 / PD-029; add PD-026. |
| F9 | "nine" cap prepositions, ten listed | **[A]** | Word fix ×3. |
| F10 | Adverb graded but absent from four option lists | **[A]** | Add "Adverb" to four instruction lines. |
| F11 | "A tall tree gives shade." | **[A]** | Attribution recast. |
| F12 | PT Part F `this` has no marking note | **[A]** | Add an AK note. |
| T1 | Audit suite has no `block_local` field | **[AUD]** | Additive field. |
| T2 | Values lexicon misses inflections | **[AUD]** | Stem matching. |

---

## F1 · Identical CW↔HW secondary keys — **[A]**

**Problem.** Item texts differ, but the *answer sequences* are identical, so the homework key is transcribable
from the classwork positionally.

**Proposal — reorder the HW items only. No item is rewritten, no mark total moves.**

| Sheet/part | Current key | Proposed print order (existing item numbers) | New key | Overlap |
|---|---|---|---|---|
| HW-1 B | `in · on · under · near · into · at` | 26, 23, 21, 25, 22, 24 | `at · under · in · into · on · near` | 39% → **0%** |
| HW-2 B | `at · on · in · in · on · at` | 23, 21, 25, 26, 24, 22 | `in · at · on · at · in · on` | → **0%** |
| HW-2 C | token list mirrors CW-2's order | print tokens as: *the morning · ten o'clock · the first of June · July · 9 o'clock · Sunday* | `in · at · on · in · at · on` | → **0%** |
| HW-3 B | `with · from · of · to · from · with` | 23, 21, 25, 26, 24, 22 | `of · with · from · with · to · from` | 37% → **0%** |
| HW-4 B | `Preposition · Noun · Preposition · Verb · Preposition` | 22, 21, 24, 23, 25 | `Noun · Preposition · Verb · Preposition · Preposition` | 48% → **20%** |

Re-check after: each pair's Part A is already compliant (30 / 30 / 25 / 35%), so the sheet totals land well under 35%.
De-patterning re-checked on the new sequences — no run >2, no strict alternation.

**For your eye:** this changes only the order pupils meet the items in. Classroom flow is unaffected — each part
is a self-contained list.

---

## F2 · PT overlaps Block 5 — **[A]** for the items · **[PD]** for the audit scope

**Verbatim duplicates (must go):**

| PT item | Duplicates |
|---|---|
| Part E prompt `meal` | B5-CW1 Part B #22 **and** B5-HW1 Part B #23 |
| Part E prompt `bird` | B5-CW1 Part B #25 |

Block 5's Part B is *"Expand the noun — add a describing word before each noun, write the full sentence, underline
the adjective."* PT Part E is the **same task with the same prompt nouns**.

**Near-duplicates (recommend recasting):**

| PT item | Block 5 |
|---|---|
| B3 *"The teacher praised **him** warmly."* | B5-CW4 *"The teacher praises him warmly."* — tense only |
| D4 *"Mother cooked **the meal**."* | B5-CW2 *"Her mother cooked a fine meal."* |
| D1 *"**Yusuf** prayed at dawn."* | **`C4B05-PT` #27** *"Yusuf prays at the mosque."* — same subject, same answer *He* |

D1 matters most: PD-029 requires zero overlap against **`C4B05-PT`** specifically, and that PT was built but never
sat — so the item is unspent and must not be reused.

**Proposal.** Block 5 used *tree, meal, friend, flower, bird, mountain, letter* as expand-the-noun prompts.
Replace PT Part E with five held nouns from outside that set:

> **river · teacher · picture · village · spoon**   *(river W5 · teacher W1 · picture W4 · village W2 · spoon W2)*

This also retires `garden`, which was unheld (F5).

- **B3** → *"The teacher thanked **him** warmly."* (target `him` = Pronoun, unchanged)
- **D4** → *"Father brought **the picture**."* → *it* (bring W5, picture W4 — both held)
- **D1** → *"**Abdullah** washed his hands."* → *He* (wash W1; house name, disjoint from `C4B05-PT`'s Yusuf item)

**[PD] required:** the run that found F2 loaded Block 5's sheets via `audit_scope: "pt_overlap_only"`. **PD-032
authorises that flag for a two-week `a`/`b` split block only**, and PD-029 states this paired-week recovery is
*not* governed by PD-025/PD-032. Ruling needed: extend PD-032's scope to the paired-week recovery, or log a new PD.
**Without it the PD-029 zero-overlap obligation cannot be mechanically verified at all.**

---

## F3 · `quickly` is a W7 word — **[A]**

Graded twice as an Adverb in a W6 block. W6 adverbs are *always · carefully · happily · loudly · slowly*.

| Item | Current | Proposed | Held check |
|---|---|---|---|
| CW-3 A2 | *"The doctor runs **quickly**."* | *"The doctor writes **slowly**."* | doctor W1 · write W1 · slowly W6 |
| HW-4 A16 | *"The doctor runs **quickly**."* | *"The worker digs **slowly**."* | worker W6 · dig W3 · slowly W6 |

Answer stays **Adverb** on both, so no key or de-patterning change. Also removes the duplicate sentence that sat
across two sheets.

---

## F4 · `run` is not in File 2 in any form — **[A]**

| Item | Current | Proposed | Held check |
|---|---|---|---|
| HW-1 A9 | *"The boys **run** fast."* | *"The children **play** every day."* | child W3 · play W1 · day W1 |
| CW-4 A11 | *"The boys **run** fast."* | *"The people **help** one another."* | people W6 · help W1 |

Answer stays **Verb** on both. Also retires `boys` (unheld) and the cross-sheet duplicate.

---

## F5 · Undeclared non-held vocabulary — **[PD]**

The master declares one non-held set: block-local **place nouns** *(box, ball, desk, table, chair, bag, gate,
wall, bed, pot)* — properly used, correct instinct, wrong citation (F8). Undeclared and in use:

**Group 1 — time nouns (12): `dawn · evening · July · June · Monday · night · Saturday · spring · summer ·
Sunday · Thursday · winter`.**
These are the **objects of every graded time preposition** and carry Day 2, CW-2 and HW-2 entirely. The block
teaches time prepositions without declaring a single time noun. They are **not avoidable** — you cannot teach
*on Sunday / in June / at dawn* without them, and the exam anchor requires the identify format over such items.

> **Recommendation:** declare a **block-local time-noun set under PD-012**, mirroring the place-noun set. PD-012
> fits exactly: taught in-block, gradeable in-block, not in File 2, not held downstream, **never dictation or
> spelling items** — and the PT dictation list already contains none of them, so the block is compliant today.

**Group 2 — avoidable carriers (10): `bench · corner · drawer · garden · grandfather · hole · poor · porch ·
room · run`.** Six sit in the PT. `run` is F4; `garden` is retired by F2.

> **Recommendation:** recast these onto held nouns rather than widen the declaration. Suggested swaps, all held —
> bench→*chair* (block-local), corner→*shop*, drawer→*box* (block-local), porch→*wall* (block-local),
> hole→*pot* (block-local), grandfather→*uncle*, room→*school*, *"the poor"*→*"the sick"* (sick W1, adjective-as-noun
> already used in HW-3 A12 *"We help the poor"* — same recast applies there).

**Why this is a [PD]:** Drive Plan §5 says a non-held word may appear in a *teaching example* but "never as the
answer in a graded item." These are **carriers inside graded items** — neither the answer nor a teaching example.
The Drive Plan does not settle that boundary, so it is a Principal Decision, not an agent call.

---

## F6 · Singing content — **[A]** on the delivered Block 05 precedent

Block 05 v1.11 already ruled this class of item under *"Content-rule (no music/singing/dancing, Charter §H)"*:
*"His sister **sings** very well"* → *"reads very well"*; *"a beautiful bird **sang** sweetly"* → *"sat on the branch"*.

| Sheet(s) | Current | Proposed |
|---|---|---|
| CW-1 A2 · CW-2 A13 · CW-4 A10 | *"A **small** bird sang."* | *"A **small** bird sat on the tree."* — mirrors the approved Block 05 recast |
| HW-3 A2 · CW-4 A9 | *"The girl **sings** loudly."* | *"The girl reads **loudly**."* — mirrors the approved Block 05 recast |
| HW-4 A3 | *"The girl **sings** happily."* | *"The child plays **happily**."* — child W3 · play W1 · happily W6 |
| HW-2 B24 | *"The birds **sing** ___ the morning."* | *"The children play ___ the morning."* — answer stays *in* |

**Carrier verbs only. Every graded target (*small · loudly · happily*, and *in*) is untouched**, so no key, no
mark total and no de-patterning result moves.

*Note:* `read` is not in File 2, but it is already an accepted unheld carrier on these sheets (CW-2 A5 *"My sister
reads a book"*) and was the Principal-approved replacement in Block 05. Flagged so the choice is visible, not hidden.

---

## F7 · Part C match tasks are not uniquely determined — **[PD]**

**CW-3 / HW-3 Part C.** Match `with · from · of · to` against four person-phrases (*my sister, my brother, my
teacher, my friend* / *my aunt, my brother, my cousin, my uncle*). **All 24 pairings are valid English** — *with my
teacher*, *from my friend*, *of my sister*, *to my brother* are each perfectly natural. The keyed answer is
unrecoverable by the pupil and unmarkable by the teacher. **As printed this task cannot be graded.**

**CW-1 / HW-1 Part C.** Place match is partly constrained but still ambiguous: the key pairs `on → the wall` and
`under → the table`, yet ***on** the table* is at least as natural; *at/near the river* and *near/at the gate* are
interchangeable. The instruction *"Each preposition fits exactly one"* asserts a uniqueness the set does not have.

**Proposal — convert all four Part C tasks to choose-between-two**, the format the school's own papers use for
forced-choice items (HY25 Q5, Annual Q7 — *"Choose the correct verb form"*), so it is exam-faithful and each item
has exactly one defensible answer. Item counts and marks unchanged (5 · 5 · 4 · 4).

Specimen, CW-3 Part C:

> **Part C — Circle the correct preposition.** *(4 items, 1 mark each)*
> 27. I got a letter (**from** / to) my sister.
> 28. I go to school (with / **to**) my friend. → *[reworded to force one answer — see note]*
> 29. This is the bag (**of** / with) my brother.
> 30. I give the book (of / **to**) my teacher.

**Note for your review:** item 28 as drafted is still loose (*"go to school with my friend"* and *"go to school to
my friend"* — the second is wrong English, so it does force the answer, but weakly). I would rather you rule the
**format** first; I will then author all 18 items and bring them back for the language check rather than guess at
the wording now.

**Alternative if you prefer to keep matching:** replace the right-hand column with full sentence-tails that only
one preposition completes (*"___ my sister — a letter came"*). This preserves the visual task but is harder to
make watertight; I recommend the choose-between-two.

---

## F8 · Governance citations — **[PD]**

| Where | Cites | Should cite | Why |
|---|---|---|---|
| line 23 (provenance), line 1179 (v1 log) | **PD-028** for the block-local place-noun set | **PD-012** | PD-028 is the *C3 Block 7 adjective weighting*. It has never governed block-local words under any numbering. PD-012 is the block-local teaching set. |
| line 30, line 1028 (PT banner) | **PD-028** for the Block 5→6 PT carry-forward | **PD-029** | Exactly the stale citation PD-029's own Numbering note documents. |
| line 24 — *"No PD-009 / PD-011 mechanism needed"* | — | **PD-026** | The claim is **correct in substance** — PD-026 rules that function-word grammar targets ("am/is/are, have/has, **and comparable closed-class items**") take none of the three non-held statuses. Prepositions are squarely comparable. It simply cites no authority. |

Charter §K.3 protects *delivered* files from retro-editing; this is an unpromoted `_wip` draft, so correcting
before promotion is in scope. Raised as **[PD]** because it touches governance references.

---

## F9 · "nine" cap prepositions, ten listed — **[A]**

Lines 40, 46, 107 say **nine** and list ten: *in · on · under · at · with · from · into · near · of · to*.
Drive Plan §2 cap lists the same ten. **Proposal:** "nine" → "ten" in all three places. Line 46 is teacher-facing
checklist text, so it is worth fixing even though it is cosmetic.

---

## F10 · Adverb graded but missing from four option lists — **[A]**

| Sheet | Option list | Adverb-keyed |
|---|---|---|
| CW-1 | Noun, Verb, Adjective, Pronoun, Preposition | #19 |
| CW-2 | Noun, Verb, Adjective, Pronoun, Preposition | #9 |
| CW-3 | Noun, Verb, Adjective, Pronoun, Preposition | #2 |
| HW-3 | Noun, Verb, Adjective, Pronoun, Preposition | #2 |

v1.3's log says it fixed *"the CW-4 and HW-4 Part-A instructions"* — it fixed only those two. Four sheets ask for
an answer the printed options exclude. Same defect class as Block 05 v1.11 item (1).

**Proposal:** add **Adverb** to the four instruction lines, matching CW-4/HW-4's wording. Label only — no item,
key or total changes. **Deliverability note:** this is the one defect a pupil meets directly in the exam hall
sense — a child who trusts the printed options cannot answer #19/#9/#2 at all.

---

## F11 · Attribution screen — **[A]**

*"A **tall** tree gives shade."* — CW-1 A11, CW-2 A8. The standing screen recasts natural phenomena presented as
autonomous givers (*"the sun gives…"*).

**Proposal:** *"A **tall** tree grows in the village."* (grow W3 · village W2). Target *tall* unchanged.

---

## F12 · PT Part F — `this` needs a marking note — **[A]**

Self-try box: `on · near · from · kind · this · them`. Under the C4 boundary *this* **before a noun** is an
**Adjective**; **standing alone** it is a **Pronoun**. The pupil writes their own sentence, so **both answers can
be right** — and the rubric scores "correct word-class placement". The AK gives the marker nothing.

**Proposal — add to `C4B06-AK` Part F:**

> *If the pupil chooses **this**: mark the part of speech against **their own sentence** — *Adjective* if *this*
> stands before a noun (*this bird is small*), *Pronoun* if it stands alone (*this is my bag*). Both are correct;
> do not mark to a single expected answer. Same rule for **kind** (Adjective in normal use).*

---

## T1 / T2 · Audit-suite defects — **[AUD]**

- **T1 — no `block_local` field.** `gate_heldword()` knows only `exemplars`. A block using **PD-012** cannot pass
  the gate without misdeclaring its block-local words as PD-009 exemplars — which would be a false record.
  **This is why F5's list reads long: the script cannot see a legitimate PD-012 declaration.** Fix is an additive
  `block_local` list, same shape and approval class as the `audit_scope` flag.
- **T2 — values lexicon misses inflections.** `VALUES_LEXICON` matches whole normalised tokens, so `sing` catches
  *sing* but not *sings · sang · singing · songs*. **Five of the six F6 items evaded it**; only the bare *sing*
  was caught. Fix is stem/prefix matching.

Both touch `audits/` and are therefore held for the same approval class as the PD-032 change.

---

## What happens after your rulings

1. Apply in this order: **F3 · F4 · F10** → **F1** → **F6 · F11** → **F7** → **F2** → **F5** → **F8 · F9 · F12**.
2. Keep `_wip/C4B06_manifest.json` in sync at every step *(one manifest correction is already pending regardless
   of rulings: the CW-2/HW-2 Part C token order was encoded column-grouped rather than in printed order — it does
   not change the F1 finding, since the two sheets are identical either way).*
3. Re-run `audits/scripts/run_all.py` after every correction; paste verbatim output.
4. **No promotion to `blocks/C4/`** until every gate is PASS or carries a ruling recorded in `_wip/STATE.md`.
