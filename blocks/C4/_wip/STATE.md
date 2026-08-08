# C4 Block 6 — build state

**Block ID:** `C4B06` · **Week:** W6 (Sun–Wed teaching, Thu PT) · **Master (planned):** `C4_ENG_Block06_Preposition_v1.md`
**Topic:** Preposition — place/time prepositions the book uses; identify (P.O.S.) + use.
**Active build switched to C4B06 on 08.08.26 at the Principal's instruction.** `C2B06b` is **parked at Phase 3**
(blueprint drafted, awaiting approval) — see `blocks/C2/_wip/STATE.md`; nothing in C2 is closed or discarded.

---

## Phase reached

**Phase 1 — Orientation: COMPLETE (08.08.26). Phase 2 NOT started — blocked.**
No blueprint. No build content. No sentence bank.
**Two blocking governance conflicts must be ruled before Phase 2 questions can even be framed** (§ "Blocking conflicts" below).

## Blocking conflicts — Principal Decisions required

### BC-1 — `C4_ENG_Block06_Preposition_v1.md` is cited as existing but has never existed in this repo

**PD-029** ("Affected files") names `C4_ENG_Block06_Preposition_v1.md` as the file carrying the combined
`C4B0506-PT`, and records **"Status: Applied (C4 Blocks 5–6); logged retrospectively 08.08.26"**, attributing it
to "the C4 Block 5/Block 6 build sessions (06.08.26)."

**Verified in the repo — the file does not exist and never has:**

- `blocks/C4/` holds Blocks 01–05 only; `blocks/C4/_wip/` was empty (`.gitkeep` only).
- `extracts/C4/` holds `C4B01`–`C4B05` artefacts only. **No `C4B06-*` and no `C4B0506-PT` anywhere.**
- Full-history search across all four commits (`git log --all`, incl. `--diff-filter=D`) returns **no C4 Block-6
  or Preposition path ever tracked or deleted**.
- `assignments/C4/C4_Eng_Assignment_W6.docx` exists but is a **cumulative Blocks 1–5 revision sheet**
  (P.O.S. · noun gender + collective · sentence types · articles · adjective + pronoun) — **it contains no
  preposition content**, consistent with Block 6 never having been built.

**Ruling needed:** is the Block 6 build (a) **outside the repo** and to be imported before any work starts, or
(b) **not yet built**, making PD-029's status line aspirational and `C4B06` a **fresh Phase 1→4 build**?
The agent must not assume either. If (b), PD-029's status line needs a forward-only correction.

### BC-2 — the Drive Plan version PD-029 relies on does not exist

PD-029 attributes the renumbering (**Adjective + Pronoun → Block 5 · Preposition → Block 6**) to
**"Drive Plan v1.11"**. `governance/driveplans/` holds only **`C4_ENG_DrivePlan_v1_10.md`**, whose §2 spine and
§4 schedule still read **Adjective = 5 · Pronoun = 6 · Preposition = 7** (17 blocks / 15 weeks).

So the authority for "Block 6 = Preposition" is missing from the repo, and under the **only** Drive Plan present,
**"C4B06" resolves to Pronoun** — already delivered inside `C4_ENG_Block05_AdjectivePronoun_v1.md`.

**Ruling needed:** confirm `C4B06` = **Preposition** (PD-029 reading, assumed here for orientation only), and
either supply/author **Drive Plan v1.11** or issue a forward-only note that v1_10 §2/§4 are superseded on the
numbering. Until then every "Block N" citation in the C4 build is ambiguous.

*Corroborating evidence that the PD-029 reading is the intended one:* `C4_ENG_Block05_AdjectivePronoun_v1.md`
v1.11 already renamed its PT header "Block 5–6" → "Block 5" with a provenance note, and its own review log
(line 1366) carries a standing flag: **"⚑ Drive Plan §7 stale block numbers … Carried from C4B04; still pending."**

## Non-blocking defect — File 2 block labels are stale (weeks are correct)

`file2/C4_ENG_VocabBatchOrder_v2.xlsx` and `C4_ENG_VocabPool_v4.xlsx` (Weekly Plan sheets) carry
**pre-B3-insert** block numbers and are marked **"[PENDING re-map]"**: they read *W4 = B4 Adjective + B5 Pronoun*,
**W5 = B6 Preposition**, *W6 = B7 Verb & SVA*. Drive Plan v1.8's log said this re-map was "unblocked by this
patch"; it was never applied.

**The week alignment is correct — verified empirically, not by eye.** Block 05 is Drive Plan **W5** and grades
File 2 **W5** vocabulary (`card` ×33, `magazine` ×5, `environment` ×5, `fair` ×3, `form` ×3 occurrences in the
master), alongside W4 words. Therefore **File 2 week N = Drive Plan week N**; only the *block-number labels* are
stale. **No vocabulary-timing risk to this build.** Labels should be corrected forward-only, on instruction.

## Orientation findings (Phase 1, verified at source)

- **Governing versions read:** Charter v1.5 · Run Book v1.17 · **C4 Drive Plan v1.10** (only version present) ·
  Block-Build Starter Template v2 · Decision Log (working, through PD-032) · format mirror
  `blocks/C4/C4_ENG_Block05_AdjectivePronoun_v1.md` (through v1.12).
- **Depth cap (Drive Plan v1_10 §2, Preposition row):** place/time prepositions the book uses —
  **in, on, under, at, with, from, into, near, of, to**. Identify (P.O.S.) + use.
  **Guardrail: no prepositional-verb / idiom work.**
- **Format mirror — Block 05 shape:** four days (2 Adjective / 1 Pronoun / 1 mixed) · 12-prompt Exit Check per
  day (Sylhet roll 12) · 8 worksheets · Wednesday Self-try ungraded demo, graded Self-try = **PT Part E** on a
  disjoint box · answer keys consolidated into a single `-AK` · **PT total 36**.
- **Vocabulary (File 2), W6 = the Preposition week:** fresh batch **18** — pollution, waste, smoke, noise, air,
  ear, kindness, people, street, clothes, poster, factory, worker (13 Noun) + **always, carefully, slowly,
  happily, loudly (5 Adverb — the pool's first adverbs)**.
  **Held scope at W6 = 143** (73 Noun · 39 Verb · 26 Adjective · 5 Adverb). W5's 21 words are held and reusable.
  *Adverb is already a taught class (Block 1 teaches the four core classes), so the W6 adverbs are legitimate
  distractors in a mixed identify task — no conflict, flagged only because they arrive this week.*

### Exam anchors — verified in the papers themselves, magic bytes checked

| Paper | Magic bytes | Verdict |
|---|---|---|
| `Class 4 English Mohammadpur Half Yearly Question 2025.docx` | `504b0304` | genuine ZIP/docx |
| `Class 4 English Mohammadpur Half Yearly Question 2026.docx` | `504b0304` | genuine ZIP/docx |
| `Class 4 English Mohammadpur Final Question 2025.pdf` | `25504446` | genuine PDF |

- **HY25 Q6 — "Identify the parts of speech of the underlined words" [10×1=10].** Underline runs extracted from
  the XML (the targets are not recoverable from plain-text extraction): *beautifully · and · little · football ·
  sit · **on** · my · quickly · tomorrow · beautiful.*
  → **exactly one preposition item: *on*** — "I saw a bird **on** the tree."
- **AN25 Q4 — "Identify the Parts of Speech of the bold word in each sentence" [10×1=10]:** *Islam · They ·
  strong · white · always · **on** · and · Alas! · new · help.*
  → **exactly one preposition item: *on*** — "The keys are **on** the desk."
- **HY26 — no P.O.S. question and no preposition item anywhere in the paper.**

**Consequence for the build (the central Phase 2 design problem).** Preposition is **never a standalone question**
in any binding C4 paper. It is a **single 1-mark slot inside a mixed identify-the-P.O.S. set**, and in both papers
that carry it the tested preposition is **the same word, *on***. The block's graded surface therefore cannot be
built on exam-format mirroring alone (Rule 8 / §7 gives one item), so the **identify ↔ use ratio and the shape of
the "use" items need a Principal ruling** rather than an agent default.

*Noted, already settled:* AN25 Q4(h) tests ***Alas!*** as an interjection, which the Drive Plan bars from the C4
taught set (Islamic register only — SubhanAllah!/MashaAllah!/Alhamdulillah!/Inna lillah!). Interjection is a
Block 13 target, not Block 6; recorded here only so the tension is not rediscovered later.

## PT shape — carried obligation from PD-029

PD-029 rules that the W5 `C4B05-PT` was **built but never administered** (slot lost to a holiday) and that its
assessment is **carried into a combined `C4B0506-PT`**, grading Block 5 (Adjective + Pronoun) **and** Block 6
(Preposition) in the **Week-6 slot**. `C4B05-PT` is retained as the built-but-unused record and is **not to be
administered separately**. The combined PT's Adjective/Pronoun items must be **freshly authored, zero-overlap**
against `C4B05-PT` **and all Block-5 worksheets**.

`extracts/C4/PT/C4B05_PT.md` (+ `.docx`) exists and is the zero-overlap reference surface.
`C4B0506-PT` **does not exist** — it was to live in the missing Block 6 master (BC-1).

**Open item — audit scope.** Zero-overlap against Block 5's eight worksheets *plus* Block 6's eight is the same
widened-surface problem PD-032 solved for a two-week split block, and the mechanism now exists in
`audits/scripts/run_all.py` (`audit_scope: "pt_overlap_only"`, commit `4b5c162`). **PD-032 authorises it for the
split-block case only**; PD-029 explicitly states the paired-week recovery is **not** governed by PD-025/PD-032.
Applying the flag here needs an explicit ruling (or a scope extension logged as a new PD).

## Pending questions for Phase 2 (not yet asked — gated behind BC-1/BC-2)

1. BC-1 — import the existing Block 6, or build fresh?
2. BC-2 — confirm `C4B06` = Preposition; supply or author Drive Plan v1.11.
3. Identify ↔ use ratio for the graded surface, given the papers supply one 1-mark identify item.
4. May graded identify items reuse ***on***, or must the taught set spread across the capped ten?
5. `C4B0506-PT` part split and total (Block 05's PT total was 36; this one carries two blocks).
6. Audit-scope ruling for the widened PT zero-overlap surface (extend PD-032, or new PD).
7. Does Block 6 build its own W6 assignment, given `C4_Eng_Assignment_W6.docx` already exists as a
   Blocks 1–5 cumulative revision sheet with no preposition content? (Same coexistence question as C2 W6.)
8. File 2 label re-map — correct now, or leave to a separate governance pass?

## Exact next step

**Principal rules BC-1 and BC-2.** No Phase 2 question list is issued and no blueprint is drafted until the
block's identity and its predecessor artefact are settled — under the repo's only Drive Plan, "C4B06" names a
block that has already been delivered, and the ruling that says otherwise cites two files that are not here.
