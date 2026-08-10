# C4B07 — Answer-key architecture (CR-020 mitigation, designed not audited)

**Phase 4, unit 4.** Contains **no sentence text** — this is the answer-key skeleton only, so it needs no
bank approval and is not blocked by the pending naturalness read. Sequences are fixed in
`blocks/C4/_wip/C4B07_number_sequences.json` and will be bound to bank lines only after you approve them.

---

## The finding this unit produced

The blueprint said "author the subject-number sequence deliberately". Doing it exposed something the
existing gates cannot see:

**`gate_pair_overlap()` measures positional overlap of *answer strings*. In this block that measure is
blind to the thing a pupil can actually exploit.**

Every SVA item's answer is a different word (`plays`, `washes`, `are`, `has`…), so the answer-string
alphabet is naturally wide and CW↔HW answer overlap will read near 0% — a comfortable, meaningless pass.
The exploitable dimension is one bit per item: **is the subject singular or plural?** Get that, and the
verb form follows mechanically. That bit is invisible to every gate in the suite.

**And a binary dimension cannot meet a 35% positional-overlap limit by chance.** Two independent random
S/P sequences agree ~50% of the time. My first attempt produced 50 / 58 / 69 / 38% across the four pairs —
all failing a limit the answer-string measure would have reported as passing. **The HW number sequence has
to be deliberately anti-correlated with its CW pair.** It does not happen on its own.

---

## The designed sequences — all constraints verified programmatically

30 parts across CW1–4, HW1–4 and the PT. Every part satisfies, by construction:

- **max run ≤ 2** on the subject-number sequence
- **no strict alternation** (the C2B06b failure — 108 of 275 marks winnable by flipping)
- **balanced** singular/plural within each part
- **every part slice independently valid**, not merely the concatenated sheet

CW↔HW positional overlap of the **subject-number** sequence, after deliberate anti-correlation:

| Pair | Overlap | Limit | |
|---|---|---|---|
| CW1 ↔ HW1 | **26.9%** | 35% | PASS |
| CW2 ↔ HW2 | **30.8%** | 35% | PASS |
| CW3 ↔ HW3 | **30.8%** | 35% | PASS |
| CW4 ↔ HW4 | **26.9%** | 35% | PASS |

Against the un-designed baseline of 50 / 58 / 69 / 38%.

---

## Part map (item counts, 1 mark each per Q3)

| Sheet | Parts | Items |
|---|---|---|
| CW1 · CW2 · CW3 | A 10 · B 10 · C 10 | 30 |
| CW4 | A 8 · B 8 · C 7 · D 7 | 30 |
| HW1 · HW2 · HW3 | A 9 · B 9 · C 8 | 26 |
| HW4 | A 7 · B 7 · C 6 · D 6 | 26 |
| PT | B 10 · C 10 · D 7 · E 5 *(+ A dictation)* | 32 |

---

## ⚑ Proposal — a `number` field and a gate. NOT self-applied.

The manifest has no way to express subject number, so nothing can check the above. I propose, for your
ruling rather than my action:

1. Add an optional item-level **`number`** field (`"S"` / `"P"`) to the manifest schema.
2. Add **`gate_number_sequence()`** applying to any part that declares it: max run ≤2, no strict
   alternation, and CW↔HW positional overlap ≤35% **on the number sequence** — the same thresholds already
   in force for answer strings, applied to the dimension that actually carries the guessing risk.

This is **additive** and vacuous on every existing manifest, exactly like `options` (PD-037) and
`block_local` (PD-035). It is a **new gate**, though, so it needs a PD — and per the standing rule I have
**derived no number for it**; the next free one must be read from HEAD at the moment of writing.

**Why it matters beyond this block:** Blocks 8–11 are the rest of the tense cluster and every one of them
grades a binary or near-binary form choice. C2B06b already lost 108 of 275 marks to this. Without the
field, C4B07's mitigation is a design convention that the next builder cannot see and no script enforces —
it would survive exactly as long as someone remembers it.

---

## Still blocked

Binding these sequences to sentences needs the **naturalness read**, the **S7 handling rule**, and the
**collective-concord** confirmation. Nothing here consumes a bank line.
