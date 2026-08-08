# C4 Block 6 — build state

**Block ID:** `C4B06` · **Week:** W6 (Sun–Wed teaching, Thu PT) · **Master (planned):** `C4_ENG_Block06_Preposition_v1.md`
**Topic:** Preposition — place/time prepositions the book uses; identify (P.O.S.) + use.
**Active build switched to C4B06 on 08.08.26 at the Principal's instruction.** `C2B06b` is **parked at Phase 3**
(blueprint drafted, awaiting approval) — see `blocks/C2/_wip/STATE.md`; nothing in C2 is closed or discarded.

---

## Phase reached

**Phase 1 — Orientation: COMPLETE (08.08.26). Phase 2 NOT started — blocked on BC-1.**
No blueprint. No build content. No sentence bank. **BC-2 closed** (Drive Plan v1.11 authored, Principal-approved).
**BC-1 open:** the partial Block 6 material has to be recovered from outside the repo before Phase 2 is framed.

## Blocking conflicts — status

| # | Conflict | Ruling (Principal, 08.08.26) | State |
|---|---|---|---|
| **BC-1** | Block 6 master cited by PD-029 but absent from the repo | **"Partially built — recover what exists."** Some Block 6 material exists outside the repo; it is to be inventoried and reconciled against PD-029, and the phase gate restarted from where the evidence lands. **The agent does not rebuild from scratch.** | **OPEN — waiting on the Principal to supply the material.** Verified absent from the whole working mount (repo, all four commits incl. deletions, untracked/ignored, and `uploads/`). Nothing to inventory yet. |
| **BC-2** | Drive Plan v1.11 cited by PD-029 but absent | **"Author Drive Plan v1.11 now"** — forward-only, PD-029 renumbering only. | **CLOSED — `governance/driveplans/C4_ENG_DrivePlan_v1_11.md` written.** See below. |

### BC-2 — RESOLVED

`C4_ENG_DrivePlan_v1_11.md` written beside v1_10 (forward-only, Charter §K.3; v1_10 retained unedited).
**Numbering change only** — no depth cap, pairing, week count, protected week or teaching scope altered.

- §2: rows 5–6 merged into **Block 5** with sub-rows **5a Adjective / 5b Pronoun**; **Preposition → 6**;
  former rows 8–17 renumbered **7–16**. Spine is now **16 blocks** (was 17); **15 weeks unchanged** — the pair
  already shared W5.
- §3 · §4 (verdict, table, "why this shape") · §5 (POS routing) · §7 (table) · summary · pre-flight ·
  disposition note all renumbered. Diff confined to those sections; verified line-by-line against v1_10.
- **Standing flag closed.** The "⚑ Drive Plan §7 stale block numbers" flag carried in the C4 review logs since
  C4B04 (still open at `C4_ENG_Block05_AdjectivePronoun_v1.md` line 1366) is cleared: §7's paper-fidelity prose
  cited *Articles (Block 3)* → now **Block 4**, and *Sentence types (Block 13)* → now **Blocks 3 / 13** with
  first-teach vs recap made explicit. Both were wrong even against v1_10's own spine.
- **§7 gains a Preposition paper-fidelity bullet** recording the orientation finding below.
- **Noted in the version log:** v1_10 was internally inconsistent — its §2 **row 1** and **§8** already used the
  post-renumbering references (*Pronoun→B5, Preposition→B6, Conjunction/Interjection→B12*) while its spine table
  contradicted them. v1.11 resolves this in favour of the delivered blocks and PD-029.
- **`C4B05-*` extract IDs unchanged** (PD-029).

**Consequence: `C4B06` = Preposition is now settled in governance, not just in a Decision Log citation.**

### BC-1 — OPEN. `C4_ENG_Block06_Preposition_v1.md` is cited as existing but is not in this repo

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

**Ruled: "partially built — recover what exists."** The build does not restart from zero and the agent does not
author a competing master. **What is needed from the Principal, before Phase 2 can be framed:**

1. The **Block 6 master** in whatever state it reached (`C4_ENG_Block06_Preposition_v1.md` or its working draft).
2. Any **`C4B06-*` extracts** — TD / CW / HW / PT / Clue Card — including partial ones.
3. **`C4B0506-PT`** if it was drafted, since PD-029 makes it the carrier of the unadministered `C4B05-PT`.
4. Any **audit report or manifest** from that build (`_wip/C4B06_manifest.json`, `audits/reports/C4B06_*`).

Drop them anywhere in the drive folder (a `blocks/C4/_wip/inbox/` folder is fine) and say the word. **On receipt
the agent will:** inventory every file · reconcile the content against PD-029 and against Drive Plan v1.11 ·
determine the true phase reached from the artefacts rather than from the log line · re-run the audit suite over
whatever graded material exists · and report the recovered state before any new content is drafted.

**If a search turns up nothing**, that is itself the finding — PD-029's *"Status: Applied (C4 Blocks 5–6)"* line
would then need a forward-only correction and `C4B06` becomes a fresh Phase 1→4 build. The agent will not make
that call unilaterally.

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

- **Governing versions read:** Charter v1.5 · Run Book v1.17 · **C4 Drive Plan v1.11** (authored this session;
  v1.10 was the only version present at orientation) · Block-Build Starter Template v2 · Decision Log (working,
  through PD-032) · format mirror `blocks/C4/C4_ENG_Block05_AdjectivePronoun_v1.md` (through v1.12).
- **Depth cap (Drive Plan §2, Preposition = Block 6):** place/time prepositions the book uses —
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

## Pending questions for Phase 2 (staged — issued once BC-1 closes)

Held back deliberately: several of these are answered differently depending on what the recovered Block 6
material already settles, and Phase 2 is meant to be **one consolidated list**, not a drip.

1. Identify ↔ use ratio for the graded surface, given the papers supply one 1-mark identify item.
2. May graded identify items reuse ***on***, or must they spread across the capped ten prepositions?
3. `C4B0506-PT` part split and total (Block 05's PT total was 36; this one carries two blocks).
4. Audit-scope ruling for the widened PT zero-overlap surface (extend PD-032, or a new PD).
5. Does Block 6 build its own W6 assignment, given `C4_Eng_Assignment_W6.docx` already exists as a
   Blocks 1–5 cumulative revision sheet with no preposition content? (Same coexistence question as C2 W6.)
6. File 2 label re-map — correct now, or leave to a separate governance pass? (Labels only; weeks verified correct.)
7. Does PD-029's status line get a forward-only correction to match whatever BC-1 recovery finds?

## Exact next step

**Principal locates and supplies the partial C4B06 material** (list at BC-1 above). On receipt: inventory →
reconcile against PD-029 + Drive Plan v1.11 → establish the true phase reached from the artefacts → re-run the
audit suite over any graded material → report recovered state. **No new build content is drafted before that.**

Drive Plan v1.11 is written and needs no further action. `C2B06b` stays parked at Phase 3, unchanged.
