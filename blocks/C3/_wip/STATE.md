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

### BC-1 · ⛔ Unresolved PD citation — *big* and *table*

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
