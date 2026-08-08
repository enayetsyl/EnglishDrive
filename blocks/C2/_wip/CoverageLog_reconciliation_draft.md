# Coverage Log reconciliation — DRAFT rows for Principal confirmation

**Status:** ⛔ Draft only. **Nothing written into `English_Drive_AssignmentCoverageLog_v1.md` yet.**
**Method:** reconstructed **from the on-disk artefacts only**. Where a file cannot establish a
value it is left **blank with ⚑**, never guessed.
**Log state today:** `last run = C5 W3 · 2026-07-21` — stale for **all five classes**.

---

## Cross-cutting findings (apply to every class)

1. **⚑ No W5 assignment artefact exists for any class.** `assignments/C*/` holds W1, W2, W4 and W6 only. The W5 row cannot be reconstructed from artefacts for any class. Needs a Principal statement: was a W5 assignment delivered and lost, or was none given?
2. **⚑ Every W4 artefact is pure revision — none carries a current-set part for the block taught that week.** Uniform across all five classes, which suggests a deliberate W4 consolidation pass rather than five independent omissions. Spec §2.1 allows `C(N) = ∅` **only where the Drive Plan declares the week consolidation-only**; no such declaration was found. Cannot be resolved from the files.
3. **⚑ No delivery dates recoverable.** Every sheet's date field is a blank student fill-in (`Date- ______`). File mtimes are the git checkout time, not delivery. All `Delivered` values stay blank with ⚑.
4. `assignments/C3/C3_Eng_Assignment_W6.docx` and `.md` are **the same paper** — the only text differences are list numbers that the docx stores as auto-numbering. **Not a divergence**; no action needed.

---

## Class 2 — full draft (needed for `C2B06b-AS`)

### Table 1 — Block Ledger (proposed replacement)

| Block | Taught | Appearances | Last seen | Last format | Provenance |
|---|---|---|---|---|---|
| B01 Word & Sentence | W1 | 3 → **5** | W3 → **W6** | naming/doing-ID, passage-find | reconstructed from artefacts `C2_Eng_Assignment_W4.md` (Parts A, D) and `C2_Eng_Assignment_W6.docx` (Part A) |
| B02 Common & Proper + Capitals | W2 | 2 → **4** | W3 → **W6** | capital-rewrite, common/proper-ID | reconstructed from artefacts `C2_Eng_Assignment_W4.md` (Parts B, C), `C2_Eng_Assignment_W6.docx` (Part B) |
| B03 Article (a/an/the) | W3 | 1 → **3** | W3 → **W6** | article-fill | reconstructed from artefacts `C2_Eng_Assignment_W4.md` (Part E, ⚡ Challenge), `C2_Eng_Assignment_W6.docx` (Part C) |
| B04 Noun — Gender (m/f/common) | W3 | 1 → **3** | W3 → **W6** | write-feminine, write-masculine, gender-change-rewrite, gender-ID | reconstructed from artefacts `C2_Eng_Assignment_W4.md` (Parts F, G, H), `C2_Eng_Assignment_W6.docx` (Part D) |
| **B05 Plurals** *(new row)* | W4 | **1** | **W6** | plural-form | reconstructed from artefact `C2_Eng_Assignment_W6.docx` (Part E) |
| **B06 Verbs + be + have/has** *(new row)* | W5–W6 | **1** | **W6** | doing-word-ID | reconstructed from artefact `C2_Eng_Assignment_W6.docx` (Part F) |

### Table 2 — Assignment History (proposed new rows)

| Week | Current | Revision | SI | Delivered | Note |
|---|---|---|---|---|---|
| W4 | B04 (completing) | B01, B02, B03 | — | ⚑ | reconstructed from artefact `C2_Eng_Assignment_W4.md`. ⚑ **B05 Plurals carries no part** though the Block 5 master places plural teaching in W4 (Mon–Tue) — paper is otherwise 100% revision |
| W5 | ⚑ | ⚑ | ⚑ | ⚑ | ⚑ **No artefact.** Row cannot be reconstructed |
| W6 | B06 — **partial** | B01, B02, B03, B04, B05 | — | ⚑ | reconstructed from artefact `C2_Eng_Assignment_W6.docx`. Current-set coverage is **6a only** (Part F, doing words); have/has + match (6b) absent because 6b was not built when this sheet was made |

---

## Classes 1, 3, 4, 5 — gaps found (same staleness)

All four ledgers also stop at **W3**. Rows below are the reconstructable ones; **`Taught` weeks are left ⚑** because they must come from each class's Drive Plan §4, which I have not read for C1/C3/C4/C5 this session — I will read them before writing rather than infer from block numbering.

| Class | Week | Reconstructed from | Blocks covered | Flag |
|---|---|---|---|---|
| **C1** | W4 | `C1_Eng_Assignment_W4.md` | B01 (C), B02 (B), B03 (D, E) + months fixed drill (F) | ⚑ no current-set part (B04 Adjective absent) |
| **C1** | W6 | `C1_Eng_Assignment_W6.docx` | B02 (C), B03 (D), B04 (E), **B05 Demonstrative (F)** + drills (A, B) | current set present ✓ |
| **C3** | W4 | `C3_Eng_Assignment_W4.md` | B01 (A, C), B02 (B), B03 (C, D, G), B04 (E, F) | ⚑ no current-set part (B05 Gender absent) |
| **C3** | W6 | `C3_Eng_Assignment_W6.docx` (= `.md`) | B02 (B), B03 (C), B04 (D), B05 (E), **B06 Article (F)** | current set present ✓ |
| **C4** | W4 | `C4_Eng_Assignment_W4.md` | B01 (A, B), B02 (C, D, E), B03 (F, G, ⚡) | ⚑ no current-set part (B04 Article absent) |
| **C4** | W6 | `C4_Eng_Assignment_W6.docx` | B01 (A), B02 (B), B03 (C), B04 (D), **B05 Adjective+Pronoun (E)** | ⚑ **B06 Preposition absent** though `C4B0506-PT` places Block 6 in the W6 slot (PD-029) |
| **C5** | W4 | `C5_Eng_Assignment_W4.md` | B01 (A, H), B02 (B), B03 (G), B04 (C, D, E, F, ⚡) | ⚑ no current-set part (B05 Countability absent) |
| **C5** | W6 | `C5_Eng_Assignment_W6.md` | B01 (A), B02 (B), B03 (C), B04 (D), B05 (E), **B06 Article (F)** | current set present ✓ |

All eight rows carry `Delivered: ⚑` and a `reconstructed from artefact <filename>` provenance mark. All five classes need a `W5 | ⚑ no artefact` row.

---

## What I need from you

1. **Confirm the Class 2 rows** — those are the ones `C2B06b-AS` depends on.
2. **W5 (all classes)** — was an assignment delivered and lost, or was none given? Determines whether the row reads "no artefact" or "none delivered".
3. **The uniform W4 current-set absence** — deliberate consolidation pass, or a real gap? If deliberate, it should be recorded so the rotation algorithm reads it as `C(N) = ∅` rather than as missing data.
4. **C4 W6** — Block 6 Preposition has no assignment part despite being assessed that week; flag only, or does it need addressing?
5. Confirm I should **read the C1/C3/C4/C5 Drive Plan §4 tables** to fill the ⚑ `Taught` weeks before writing.
