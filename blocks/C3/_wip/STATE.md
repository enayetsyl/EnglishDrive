# C3 Block 7 — build state

**Block ID:** `C3B07` · **Week:** W6 (Sun–Wed teaching, Thu combined PT) · **Master:** `_wip/C3_ENG_Block07_Adjective_v1.md`
**Topic:** Adjective — describing words (*what kind / how many / which / whose*), attributive position only; dual-job anchor *clean*.

---

## Phase reached

**Phase 4 — BUILT IN CHAT, IMPORTED TO `_wip/` 09.08.26. NOT AUDITED. NOT PROMOTED.**

Authored outside the repo, in chat. A copy had already been dropped into `extracts/C3/TN/` as
`C3_ENG_GrammarBlock07_Adjective_v1.md`; the uploaded file is **byte-identical to it** once line endings are
normalised, so no content was lost or superseded by the import. The block never reached `blocks/C3/` and never had a
`blocks/C3/_wip/` entry — `blocks/C3/` still holds Blocks 1–6 only.

**Consequence:** there is **no `_wip/C3B07_manifest.json`** and `audits/scripts/run_all.py` has **never been run** on
this block. Nothing here has been checked by a script in this repo. **It may not be presented as final until the
manifest exists and every gate returns PASS.**

## Decisions confirmed

| # | Decision | Who / when |
|---|---|---|
| 1 | Graded-item weighting **55/25/20 descriptive : possessive-demonstrative : number** — **PD-028**, correctly cited in the file and unchanged. The possessive/demonstrative/number strands are taught in-cap but tested by no binding paper; the weighting is deliberate and must not be "reconciled" toward the exam. | Principal, 08.08.26 |
| 2 | **Combined Block 6 (Article) + Block 7 (Adjective) Performance Test `C3B0607-PT`** — 34 marks (Article 9 · Adjective 11 · shared dictation 10 · self-try 4), 0.5 marks per sentence in Parts B, C, E, F. Block 6's PT was postponed by the holiday. Logged **PD-043**. | Principal, 09.08.26 |
| 3 | **Stale PD number corrected on import: PD-031 → PD-043.** PD-031 was already taken (sacred words barred from match tasks). | Agent, 09.08.26 |
| 4 | **Internal ID inconsistency fixed:** the answer-key heading read `C3B07-PT` against a paper ID of `C3B0607-PT`; corrected to the canonical combined ID. | Agent, 09.08.26 |
| 5 | Master imported to `_wip/` as `C3_ENG_Block07_Adjective_v1.md` (forward-only stem, CLAUDE.md §6); CRLF normalised; the internal **Filename** field updated. **Not promoted.** | Agent, 09.08.26 |

## Pending — must close before promotion

### BC-1 · ✅ **CLOSED 09.08.26 — ruled PD-047.** `big` and `table` are a PD-012 block-local set (as extended by PD-035); the four `big` items and the `wooden–table` pair are unchanged, the header row now declares the set, and the Sunday-script citation reads PD-047. Superseded text retained below.

#### Superseded statement of BC-1 (retained for the record)

~~⛔ Unresolved PD citation — *big* and *table*~~

The Sunday script reads *"**big** and **table** are taught this block — PD-029, PD-030"*. Neither number holds that
ruling: PD-029 is the C4 spine renumbering, PD-030 the `C4B04-AK` consolidation. The citation has been replaced in the
file with **"PD pending, see `_wip/STATE.md` BC-1"** rather than guessed at.

**This also contradicts the file's own header**, which states *"All 29 pool adjectives held by end W6 — zero gap; **no
block-local set, no override**."* Either *big* / *table* are pool-held (in which case the sentence is simply wrong and
should be cut), or they are block-local declarations under **PD-012 as extended by PD-035** (in which case the header's
"no block-local set" line is wrong). **Principal ruling needed.** Not resolved silently.

### Other

1. **Manifest + full audit run.** Build `_wip/C3B07_manifest.json` covering all 8 worksheets + `C3B0607-PT`, run `run_all.py`, paste the verbatim output, save the report.
2. **PT zero-overlap across two blocks.** `C3B0607-PT` grades Block 6 (Article) as well as Block 7, so the zero-overlap gate must see **Block 6's worksheets too** — the same widened scope PD-032 defined for split blocks and PD-034 extended to paired-week recovery. Declare the scope in the manifest before running.
3. **Roll = 17 is a Principal ruling, not file-verified** (the file says so itself). Exit Check prompt counts depend on it.
4. **C3 Drive Plan §4 / §7 forward-only note owed** — Block 6's PT is combined this cycle as `C3B0607-PT` (PD-043).
5. **Duplicate copy.** `extracts/C3/TN/C3_ENG_GrammarBlock07_Adjective_v1.md` is the same file under the old stem. On promotion, `blocks/C3/C3_ENG_Block07_Adjective_v1.md` becomes authoritative and the `extracts/TN/` copy should be regenerated from it, not edited in place.
6. **PD-042 §H.5 re-screen** — Rabab is now male drive-wide. This block has **not** been swept.

## Next step

Get the BC-1 ruling, then build `_wip/C3B07_manifest.json` and run the audit suite.

---

## Audit run 1 — 09.08.26 · `audits/reports/C3B07_audit_2026-08-09.txt`

Manifest `_wip/C3B07_manifest.json` parsed directly from the master (9 sheets, 255 items; every worksheet item matched
to an answer-key entry with none missing). **First script run in this repo.** **8 gates PASS · 5 FAIL.**

**FAIL 1 — cross-sheet repetition (PD-036): ~60 sentences on more than one sheet**, several on three or four —
`We see a polluted river.` on **CW1, CW4, HW3 and the PT**; `Yusuf has a clean hand.` on CW1, CW2, CW3;
`It is a joyful morning.` on HW1, HW2, HW4; `We see a good school.` on CW2, CW3, HW1. This is the block's dominant
defect and needs a repetition pass on the scale of C4B06's (38 repeats → 0).

**FAIL 2 — mark totals: PT computes 34.5 against a stated 34.** Part B is printed as *"[10 blanks × 0.5 = 5]"* but
carries **11 blanks** (items 1, 6 and 8 each have two) — and the answer key supplies all 11. Either the paper loses a
blank or the total becomes 34.5.

**FAIL 3 — held-word: `big` is not in File 2** (4 graded items: CW1 A, HW2 A ×2, HW4 A). **This independently confirms
BC-1** above — the master's bogus "PD-029, PD-030" citation was covering a word with no held status, while the header
claims "all 29 pool adjectives held, no block-local set". The BC-1 ruling now has evidence behind it.

**FAIL 4 — PT zero-overlap (3 items).** PT Part E reuses `We see a polluted river.` (CW4), `Porshi has two gardens.`
(HW2) and `That hat is on the bed.` (HW3) verbatim.

**FAIL 5 — de-patterning: PT Part F is a strict alternation** — adjective · verb · adjective · verb.

**Passed:** CW↔HW positional overlap (0% on all four pairs) · within-sheet duplicates · option lists (5 parts) ·
HW key transcribability (10 pairs) · rehearsal disjointness · sacred-word · values lexicon · one-defensible-answer.

### Three findings no gate catches — human screens

1. **⛔ Two conflicting answer keys for the same Thursday paper.** The key at *Answer Key → Performance Test* matches
   the printed combined PT (Parts A–G, 34 marks). A **second, stale key** at the end of the file
   (`Part B (passage) · Part C: cozy, her, this, old, red, some · Part D: 1. adjective 2. verb · Part E self-try`)
   describes an **adjective-only paper that no longer exists**. A teacher could mark from the wrong one. **Delete or
   supersede it** — needs your say-so, since deleting outside `.git/` requires it.
2. **Off-roster character name.** **Rani** appears three times (CW2 Part C item 4; PT Part B item 6; PT Part C item 3).
   Charter §H.5's roster is Yusuf, Abdullah, Nusair, Abdur Rahim, Aisha, Raima, Maryam, Fatima, Porshi, Rabab, Jesmin.
2. **No worksheet prints a mark total.** Computed: CW1/HW1/CW2/HW2 33 · CW3/HW3 32 · CW4 36 · HW4 34. The header
   predicts "30 CW / 28 HW". Nothing to check the key against until a total is printed on each sheet.

**Manifest note:** number, possessive and demonstrative words (*two, three, four, many, some, few, all, my, his, her,
our, their, this, that*) are declared as **PD-009 exemplars**, following the C5B07 precedent — the master calls them
"carriers, not pool-held", but they are graded answers and the gate requires an instrument. Dual-job Part D items carry
`clean` as the trigger, not the grammar label.

---

## Audit run 2 — 09.08.26 · approved repair applied · `audits/reports/C3B07_audit_2026-08-09.txt`

Applied exactly the approved set, nothing more. **Result: 11 PASS · 2 FAIL, both ruled.**

| # | Change | Scale |
|---|---|---|
| 1 | PT Part B item 8 → `I see ___ ostrich.` | 1 item + 1 key line — **PT now 34/34, Article 9, no half-marks** |
| 2 | `big` + `table` declared block-local (PD-047) | header row + 1 script citation + manifest — **zero content change**; held-word gate now PASSES 220 targets |
| 5 | 9 match replacements (naming word only, every adjective preserved) | CW3 3 · HW3 1 · CW4 2 · HW4 3; four sets re-deranged; **no pair now appears more than twice** |
| 6 | PT Part F reordered 2·1·3·4 | **no sentence rewritten**; key reordered; de-patterning now PASSES |
| 8 | Stale PT key struck through under a do-not-mark warning | **Part A dictation list retained** — the only record of the ten words |
| 9 | `Rani` → Porshi (script) · Maryam (PT B#6) · Fatima (PT C#3) | carrier names only; **no key, mark or task structure moved** |
| — | 40 match placements itemised in the manifest | structural; they were invisible to every gate before |

**Gate movement**

| Gate | Before | After |
|---|---|---|
| De-patterning | FAIL — PT Part F alternation | **PASS** |
| Mark totals | FAIL — PT 34.5 vs 34 | **PASS — PT 34/34** |
| Held-word / block-local | FAIL — `big` ×4 | **PASS — 220 targets** |
| CW↔HW overlap | PASS | PASS (4% / 0% / 0% / 0%) |
| HW key transcribability | PASS (10 pairs) | PASS (**14** pairs — match parts now visible) |
| PT zero-overlap | FAIL — 3 items | FAIL — same 3, **ruled PD-048(8)** |
| Cross-sheet repetition | FAIL — 64 texts | FAIL — 76 texts, **all ruled PD-048(6,7,9)** |

The cross-sheet count rises from 64 to 76 only because the 12 surviving match pairs are now **visible** for the first
time; every one sits at exactly two appearances, which is the Option-2 target. Within-sheet duplicates, option lists,
rehearsal disjointness, sacred-word, values lexicon and one-defensible-answer all PASS.

**Both remaining failures are ruled (PD-048).** No unruled failure stands.

## Still open

1. **File 2 size-adjective gap** — the C3 pool holds **no** size adjectives (*big, small, little, tall, long, short*).
   PD-047 covers this block; filling the pool affects every C3 block and needs its own ruling. **Flagged, unfilled.**
2. **PD-032/PD-034 widened PT overlap not yet run** — `C3B0607-PT` grades Block 6 (Article) too, so Block 6's
   worksheets should be loaded as `pt_overlap_only` reference, exactly as was done for C2. Not run.
3. **C3 Drive Plan §4/§7 forward-only note** owed (combined `C3B0607-PT`, PD-043).
4. **Roll = 17** is a Principal ruling, not file-verified.
5. **PD-042 §H.5 re-screen** (Rabab now male) — this block not swept.
6. **`extracts/C3/TN/` duplicate** under the old stem — regenerate from the master at promotion, don't edit in place.
7. **No worksheet prints a mark total** — recorded as a gap, not a failure (PD-048); no governing file requires one.

**Block remains in `_wip/` — not promoted.** Corrections logged **CR-025 … CR-030**.

---

## PD-032 / PD-034 widened PT overlap — RUN 09.08.26 · ⚑ 3 NEW findings, no content changed

Block 6's **eight Article worksheets (236 items)** loaded into `_wip/C3B07_manifest.json` as
`"audit_scope": "pt_overlap_only"` reference. `C3B0607-PT` is now compared against **353 worksheet items** across both
blocks. Block 6's own PT was not loaded — it was never administered and its assessment is carried into this paper
(PD-043), so comparing against it would flag the carry itself.

**Result — the Article half of the PT is not disjoint from Block 6.**

| PT item | Duplicates | Answer |
|---|---|---|
| **Part B #4** — `He is ___ honest boy.` | `B6-HW4` | *an* |
| **Part B #7** — `It is ___ university bag.` | `B6-HW4` | *a* |
| **Part C #6** — `She has an kite.` | `B6-CW4` | *a* |

**Assessment impact — not uniform, and two of these are stronger than earlier overlap findings.**

- **Part C #6 (`kite`) is straightforwardly rule-derived** — a consonant sound takes *a*. Same standing as the items
  ruled under PD-044/PD-046; no meaningful advantage.
- **Part B #4 and #7 are the two exception items of the whole Article topic** — silent-*h* (*honest* sounds like a
  vowel → *an*) and the *"yu"* sound (*university* → *a*). These are precisely the cases where a pupil is most likely
  to **recall** rather than apply the sound test, because the rule's surface form (look at the letter) gives the wrong
  answer. A pupil who met these exact sentences in Block 6 homework can reproduce them without hearing the sound.
  The advantage is real, though it is worth **1 mark in total** (2 blanks × 0.5).
- Both Part B hits come from **the same sheet, `B6-HW4`**, which suggests the PT's Article half was drafted with that
  homework open rather than authored fresh.

**Reported for ruling; no content changed** (Principal instruction, 09.08.26). Unlike the C2 equivalent, this one is
not covered by any existing waiver.

**No other gate result moved** — the reference sheets are visible only to the PT overlap gate.

## C3 Drive Plan §4 / §7 — DONE 09.08.26

`governance/driveplans/C3_ENG_DrivePlan_v1_8.md` — forward-only notes at **§4** (Block 6's PT combined into
`C3B0607-PT` this cycle, 34 marks, PD-043) and **§7** (Annual 2025 Q8 examined in the combined paper, per-anchor mark
values preserved). No row amended.

## Corrections approaching PATTERN — flagged only, no rule created

Three types now sit at **2 occurrences**; a third makes each PATTERN under CLAUDE.md §5A and obliges a proposal:

| Type | Occurrences | Origin |
|---|---|---|
| **Attribution — autonomous natural giver** | CR-004 (C4B06) · CR-023 (C2B06b) | *"the sun gives us light"* |
| **Cross-sheet repetition of match pairings** | CR-022 (C2B06b) · CR-026 (C3B07) | recall instead of derivation |
| **Unheld word graded** | CR-001 (C4B06) · CR-030 (C3B07) | `quickly`/`run`/`shelf` · `big`/`table` |

**No standing rule introduced and no gate changed.** Recorded so the third occurrence is recognised when it arrives.

