# C4 Block 6 — build state

**Block ID:** `C4B06` · **Week:** W6 · **Status: PROMOTED (08.08.26).**
**Master:** `blocks/C4/C4_ENG_Block06_Preposition_v1.md` — internal version **v1.5**, **all ten audit gates PASS**.

*(C4 filename convention: the file stays `_v1.md` and the internal version log carries the version —
same as `C4_ENG_Block05_AdjectivePronoun_v1.md`, which is internally at v1.12.)*

---

## Delivered

| Artefact | Path |
|---|---|
| Block master | `blocks/C4/C4_ENG_Block06_Preposition_v1.md` |
| Classwork ×4 | `extracts/C4/CW/C4B06_CW1…CW4.md` |
| Homework ×4 | `extracts/C4/HW/C4B06_HW1…HW4.md` |
| Combined Performance Test | `extracts/C4/PT/C4B0506_PT.md` |
| Teacher answer key | `extracts/C4/C4B06_AK.md` *(PD-030: keys live in `extracts/`, not `blocks/`)* |
| Preposition Clue Card | `extracts/C4/Clue Card/C4B06_CC.md` |
| Teaching Days 1–4 | `extracts/C4/TN/C4B06_TD.md` |
| Master reference copy | `extracts/C4/TN/C4_ENG_Block06_Preposition_v1.md` |
| Audit report | `audits/reports/C4B06_audit_2026-08-08.txt` |
| Manifest | `blocks/C4/_wip/C4B06_manifest.json` |

**Extract checks:** no answer-key text on any student-facing sheet · item counts match the manifest
(CW 34/29/33/28 · HW 31/26/30/28) · every stated total present and correct
(37 · 31 · 38 · 32 · 36 · 30 · 31 · 31 · PT 36) · all four HW sheets carry the **W6** Vocabulary Writing box.

## Final gate state

```
[PASS] De-patterning · CW↔HW overlap (19/22/17/32%) · PT zero-overlap (34 vs 451)
[PASS] Within-sheet duplicates · Rehearsal/graded disjoint · Mark totals
[PASS] Sacred-word guard · Values lexicon · Held-word/block-local · One-defensible-answer
RESULT: ALL GATES PASS
```

**Cross-sheet repetition: 199 sentences compared, zero repeats** (was 38 sentences over 78 placements).
**Mark totals never moved at any point in the review.**

## What this block required

Recovered from `_wip/inbox/` as v1.3 with **no manifest and no audit report ever produced**; the v1 log's claim
*"all audits green"* was unevidenced and false on two counts. Twelve findings (F1–F12), two audit-suite defects
(T1/T2), the Principal's own CW-1/HW-1 edits, and a cross-sheet repetition pass took it to v1.5.

The two that mattered most: **every CW↔HW pair shared an identical secondary answer key** (homework transcribable
from classwork positionally), and **the PT duplicated Block-5 items verbatim**, breaching PD-029 — including one
item from `C4B05-PT`, a test that was built but never sat. Neither was findable by any script until PD-034
authorised the widened audit scope.

## Governance written during this build

| # | Ruling |
|---|---|
| **Drive Plan v1.11** | PD-029 renumbering recorded; clears the "§7 stale block numbers" flag carried since C4B04 |
| **PD-034** | `audit_scope: pt_overlap_only` authorised for the §6.7 paired-week recovery |
| **PD-035** | PD-012's trigger extended to concepts required by the Drive Plan §2 cap without an exam anchor |

Block-local sets declared (PD-012/PD-035), **block-scoped, not added to File 2**:
**place (11)** box · ball · desk · table · chair · bag · gate · wall · bed · pot · shelf ·
**time (12)** Sunday · Monday · Thursday · Saturday · June · July · summer · winter · spring · evening · night · dawn.
Blocks 8–9 must **re-declare** if they want the time expressions.

## Open items carried forward

1. **Cross-sheet duplicate gate — CLOSED, ruled and live.** ~~Proposed, not ruled; PD-036 is the next free
   number.~~ *(That line was written mid-sweep on 08.08.26 and was stale the same day — corrected 10.08.26.)*
   Ruled as **PD-036** (Principal, 08.08.26): `gate_cross_sheet_repetition()` in `audits/scripts/run_all.py`,
   `CROSS_SHEET_MAX_REPEATS = 0` — every normalised item text unique across all of a block's graded sheets.
   **PD-038** settled its relation to the older CW↔HW ≤2-identical-items allowance: that rule stays in the script
   as a backstop but can never bind while the threshold is 0. Self-test `audits/scripts/selftest_cross_sheet.py`
   (5/5 assertions hold, incl. seeded error and `pt_overlap_only` exclusion); `CORRECTIONS.md` CR-009 **PROMOTED**.
   Next free PD number is **PD-051**, not PD-036.
2. **Clue text and instruction lines are unread by every gate.** `(together)` was a W7 word *carrying the answer*
   on five graded items and no gate saw it. **[AUD]**
3. **PT Part B option list shows five classes, the worksheets six.** No adverb is keyed on the PT, so it is not
   wrong — but it differs from the eight worksheets after the F10 ruling. Cosmetic; flagged, not changed.
4. **Attribution in the Teacher Script.** *"A tall tree gives shade"* recast on the worksheets, still present at
   the Day-3 script and one Exit Check. Teacher Script was out of scope; the §H attribution screen is standing.
5. **`quickly` / `mosque` in the Teacher Script and Exit Checks** — W7 words as oral teaching examples, permitted
   under Drive Plan §5. Recorded so it is not rediscovered.
6. **File 2 label re-map** — `VocabBatchOrder_v2` / `VocabPool_v4` still carry pre-B3-insert block labels marked
   "PENDING re-map". Weeks verified correct; labels only.
7. **`extracts/C4/TN/C4_ENG_Block05_AdjectivePronoun_v1 (1).md`** still carries a `" (1)"` suffix.
8. **Working-mount defect.** The mount refused `unlink` all session and **re-materialised renamed files** (git
   locks and `SESSION_LOG.md`), so the merge with the parallel C5 session was done in a sandbox clone and pushed
   from there. Delete permission was requested once and declined. `_wip/` copies could not be cleared for the same
   reason — `blocks/C4/` is authoritative; `_wip/C4_ENG_Block06_Preposition_v1_4.md` is a stale duplicate.

## Next step

C4B06 is delivered. `C2B06b` remains parked at Phase 3 (blueprint awaiting approval); a parallel session has
**C5B07** open. Next C4 block is **B7 Verb & Subject–Verb Agreement (W7)** — the first of the three protected
tense weeks.
