# C3B08-AK — pre-build blueprint (Phase 3)

**Block:** C3B08 Pronoun · **Master:** `blocks/C3/C3_ENG_Block08_Pronoun_v2_2.md`
**Status:** APPROVED 15.08.26. §D closed by **PD-068** — CR-040 waived (no edit), word lists duplicated (master v2.3).
**Built:** `extracts/C3/C3B08-AK.md`, §6.11 consistency check PASS.

---

## §A — What the AK covers

| Artefact | Graded items | Marks |
|---|---|---|
| CW1 · HW1 · CW2 · HW2 | 28 · 26 · 28 · 26 | 108 |
| CW3 · HW3 · CW4 · HW4 | 28 · 26 · 28 · 26 | 108 |
| `C3B08-PT` | 22 itemised + dictation + rubric | 34 |
| **Assignment** | **not written — section omitted under PD-067** | — |

Order is §3.15's fixed sequence: `CW1 · HW1 · CW2 · HW2 · CW3 · HW3 · CW4 · HW4 · PT`.
Answers only, no question text (§3.15 r.2). Original numbering preserved exactly (§3.15 r.1).
Dictation word list and the Part F self-try assignment list move **into** the AK (§3.15 r.3) and
come out of the master's PT administration block at the same time.

## §B — Rulings this build stands on

- **PD-067** (this session) — AK assembled before the Assignment exists; Assignment section omitted and declared.
- **v2.2** — PT renumbered continuously (CR-038). The AK keys `PT` as A 1–10 · B (a)–(h) · C 11–16 · D 17–20 · E 21–24 · F.
- Answers **re-derived from item text**, then cross-checked against the manifest — Principal's ruling, 15.08.26.

## §C — Cross-check result (161 agree · 13 differ · all 13 resolved in the master's favour)

| Items | Manifest said | AK will say | Why |
|---|---|---|---|
| HW1 B12 · CW2 B18 · HW3 C19 (Rabab) | `she` / `She` | `he` / `He` | PD-057, applied to the master at v1.5; manifest never updated |
| 8 × Part D / PT Part E | `describing word` | `adjective` | v1.9 terminology alignment to the Annual paper |
| CW2 C28 · HW2 C24 | `You` | `you` | **CR-039** — mid-sentence vocative blank; the capital was a key error |

## §D — Decisions required before build

1. **⚑ OPEN FAIL — PD-036 cross-sheet repetition.** `Maryam` is a bare Part B item on **CW1 #16 and HW1 #12**;
   threshold is zero. Created by v1.5's balance repair (CR-040). Recommended fix: **HW1 B12 `Maryam` → `Fatima`**
   — answer stays `she`, Part B balance stays he 2 · she 2 · it 2 · they 2, no adjacent repeat, CW1↔HW1 positional
   overlap unmoved at 0/8, and `Fatima` appears nowhere else on either Part B. Requires a v2.3 master (§K.3 forward-only).
2. **PT dictation and self-try lists** — confirm they move out of the master's administration block into the AK,
   leaving a pointer, per §3.15 r.3.

## §E — Verification plan

`run_all.py` re-run after any change · §6.11 consistency check (every graded item has exactly one answer; no answer
references a non-existent item; numbering continuous and non-duplicated per artefact; per-artefact totals recomputed
from the key match the printed totals) · human naturalness and one-defensible-answer read stays with the Principal.

## §F — Audit state at blueprint time

`audits/reports/C3B08_audit_2026-08-15.txt` — 12 PASS, **1 FAIL** (§D.1). Mark totals recomputed from the rebuilt
manifest and matching on all nine artefacts: CW 28 · HW 26 × 4, PT 34.
