# C1 Block 6 — build state

**Block ID:** `C1B06` · **Week:** W6 (Sun–Wed teaching, Thu combined PT) · **Master:** `_wip/C1_ENG_Block06_Pronoun_v1.md` (internal v1.1)
**Topic:** Pronoun — recognition + guided rewrite. Mixed week: **Sunday = Block 5 (Demonstrative) text-based reteach**; Mon–Wed = Block 6 Pronoun; Thursday = combined `C1B0506-PT`.

---

## Phase reached

**Phase 4 — BUILT IN CHAT, IMPORTED TO `_wip/` 09.08.26. NOT AUDITED. NOT PROMOTED.**

The block was authored outside the repo, in chat, not unit-by-unit in-repo. The finished master was imported on
09.08.26 under the forward-only stem (CLAUDE.md §6). It carries full minute-by-minute teacher scripts for all four
teaching days, 8 worksheets (10 items each), the combined Thursday PT and the answer key.

**Consequence:** there is **no `_wip/C1B06_manifest.json`** and `audits/scripts/run_all.py` has **never been run** on
this block. The master's own line *"full §6.5 seven-audit sweep PASS"* is a claim from the chat build, not output from
this repo's audit suite, and does not satisfy CLAUDE.md §4 — which also requires ten gates, not seven.
**This block may not be presented as final until the manifest exists and every gate returns PASS.**

## Decisions confirmed

| # | Decision | Who / when |
|---|---|---|
| 1 | **Cap lifted to S3 free pronoun rewrite for C1 Block 6 only**, overriding Drive Plan §2 row 6 "recognition ONLY" (Ruling A). Graded rewrite targets **he / she / it / they**; I / we / you stay at recognition and matching. Bloom band knowingly stretched; cohort-age objection recorded and overruled. Logged **PD-039**. | Principal, 09.08.26 |
| 2 | **Combined Block 5 + Block 6 Performance Test `C1B0506-PT`** (27 marks) — Block 5's PT was postponed by a holiday. Block 5 assessed **text-based** (fill-blank + bracketed near/far · one/many hint), not picture-cued. Logged **PD-040**. | Principal, 09.08.26 |
| 3 | **Stale PD numbers corrected on import: PD-028 → PD-039, PD-029 → PD-040** (9 and 4 citations respectively). Both provisional numbers had already been taken in the Decision Log — PD-028 by the C3 B07 weighting ruling, PD-029 by the C4 spine renumbering. | Agent, 09.08.26 |
| 4 | Master imported to `_wip/` as `C1_ENG_Block06_Pronoun_v1.md`; CRLF normalised to LF; internal Master-ID line updated to the new stem. **Not promoted** — promotion waits on the audit run and an explicit "done". | Agent, 09.08.26 |
| 5 | Sheet-ID convention: all W6 worksheets carry the `C1B06-` prefix. **CW-1/HW-1 are the Sunday Block 5 reteach**; CW-2…CW-4 / HW-2…HW-4 are Block 6 Pronoun. The prefix prevents collision with Block 5's W5 picture sheets (`C1B05-CW1…HW4`). | Build decision, carried |

## Pending — must close before promotion

1. **Manifest + full audit run.** Build `_wip/C1B06_manifest.json` (schema `audits/scripts/README_manifest.md`) covering all 8 worksheets + `C1B0506-PT`, run `run_all.py`, paste the verbatim output and save the report. Nothing in this block has been checked by a script in this repo.
2. **Parts F and G overlap waiver.** The master waives item-shape overlap between PT Parts F/G and the worksheets, citing Block 4/B5 precedent, and holds §6.5 disjointness to the Part E self-try only. **This is narrower than CLAUDE.md §4's PT zero-overlap gate** (zero PT item texts identical, normalised, to any worksheet item) as tightened by PD-036/PD-038. The waiver needs an explicit ruling recorded here, or the PT items need re-authoring.
3. **Pointer owed on `C1B05-PT`** — "live PT superseded by `C1B0506-PT` (PD-040)".
4. **C1 Drive Plan forward-only notes owed** — §2 row 6 annotated "superseded for C1 B6 by PD-039" (not deleted, Charter §K.3), plus §7 and §9b (the production self-try is now permitted for this block).
5. **Supersedes an older draft.** `extracts/C1/Other/Draft Blocks/C1 blocks/C1_ENG_GrammarBlock06_Pronoun_v1.md` is the earlier recognition-only, Bangla-delivery v1 of this block. It is left in place untouched; say the word if you want it retired.
6. **PD-042 §H.5 re-screen** — Rabab is now male drive-wide. This block has **not** been swept.

## Next step

Build `_wip/C1B06_manifest.json` from the imported master, run the audit suite, and bring the PT-overlap waiver (pending item 2) to the Principal as a ruling before anything is promoted.
