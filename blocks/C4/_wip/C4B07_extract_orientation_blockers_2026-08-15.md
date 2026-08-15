# C4B07 — extract build, Phase 1 orientation & blocker report

**Date:** 2026-08-15 · **Agent session** · **Status: STOPPED BEFORE BUILD — awaiting Principal ruling**

Nothing has been built. No extract, no manifest, no audit run. This file is the record of what
orientation found. Six items below are governance questions the governing files do not settle;
under CLAUDE.md §3 (Pending decisions) they are stated, not resolved.

---

## 1. Canonical IDs — confirmed from the master, not assumed from C3B08

`grep -o "C4B07-[A-Z]*[0-9]*"` over `C4_ENG_Block07_VerbSVA_v2_0.md` returns **11 distinct IDs**:

```
C4B07-CW1  C4B07-CW2  C4B07-CW3  C4B07-CW4
C4B07-HW1  C4B07-HW2  C4B07-HW3  C4B07-HW4
C4B07-PT   C4B07-TD   C4B07-AK
```

The master's own front-matter **Canonical IDs** line declares the same 11.

**Not twelve.** C3B08's twelfth was `CC` (Clue Card). **`C4B07-CC` is not declared** — although the
master *contains* two clue-card sections (§ *Verb & Agreement Clue Card*, line 167; § *Word-Role Clue
Card — rows added this week*, line 239) and the Teaching & sourcing decisions section commits to
"a dedicated **Verb & Agreement Clue Card** this week, plus Verb + SVA rows added to the running
Word-Class Clue Card (§8 incremental build)". C4B05 and C4B06 both have promoted `-CC` extracts.

`C4B07-AS` is not declared either, so the exclusion is moot.

**⚑ Q1 for ruling — is the Clue Card an extract this block?** Either the master's Canonical IDs line
is incomplete, or the Clue Card is intentionally not extracted. Not the agent's to settle.
Build count is **11** as declared, or **12** if `CC` is added.

---

## 2. The master is not where the task says it is

Task cited `blocks/C4/C4_ENG_Block07_VerbSVA_v2_0.md`. The file is at **repo root**
(`./C4_ENG_Block07_VerbSVA_v2_0.md`, 1880 lines, committed in this session's `sync.bat` run —
`create mode 100644 C4_ENG_Block07_VerbSVA_v2_0.md`).

It is in neither `blocks/C4/` (where §6 puts confirmed masters) nor `blocks/C4/_wip/` (where §2 puts
drafts). Its own status line reads **`⚑ NOT PROMOTABLE`**, which places it in `_wip/`.

**⚑ Q2 for ruling — where does this file belong?** Moving a file outside `.git/` requires the
Principal's approval per CLAUDE.md §1; the agent has not moved it.

---

## 3. There is no manifest. The audit-trail comparison has no object.

`blocks/C4/_wip/C4B07_manifest.json` **does not exist.** The only manifest in that folder is
`C4B06_manifest.json`.

Consequences for the checks the task asked for:

| Check requested | Result |
|---|---|
| Divergence count, manifest item texts vs master | **Not computable — no manifest exists.** Not "zero divergences" |
| `dictation` populated and current | **No file to inspect** |
| `pt_self_try_words` populated and current | **No file to inspect** |
| `demo_box_words` populated and current | **No file to inspect** |
| Audit report newer than the master's current version | **No C4B07 report exists at all.** `audits/reports/` holds C1B06, C2B06b, C3B07, C3B08 (×3), C4B06 (×2). Nothing for C4B07 |
| Superseded manifest kept beside the rebuild | **Nothing to supersede** |

This is not the C3B08 failure mode (a stale manifest carried forward). It is the prior condition:
**the manifest was never written.** The master agrees — front matter: *"The repo audit suite has not
run against this file."*

The manifest must therefore be authored from scratch: **224 worksheet items** (CW 30×4 = 120,
HW 26×4 = 104) **+ the PT** (A dictation 10 · B 10 · C 10 · D 6 · E 4 sentences). That is authoring
against a blocked schema — see §4.

---

## 4. E-7 — confirmed open at source, and it blocks the manifest itself

The master flags E-7 as **"Open, blocks the build"**. Verified against the repo suite, not taken on
the master's word:

- `audits/scripts/run_all.py` → `gate_heldword()` (line 485) reads exactly two declaration sets:
  `exemplars` and `block_local` (lines 504–505). **There is no `override` field, in the script or in
  `README_manifest.md`.**
- `go` and `work` are **PD-011 overrides** and are **absent from Pool v4** (PD-011 admits a word
  without amending the Pool — Principal, 12.08.26, File 2 expressly not amended).
- So every item carrying `go` or `work` as its `trigger` will FAIL `gate_heldword()`, and the schema
  offers no honest way to declare them. The master puts this at **16 items across CW2, HW2 and the PT**.

Declaring an override through the `block_local` field would be dishonest — PD-012 block-local words
are *never* dictation-eligible and are *not* held downstream, whereas `go` and `work` are **both**.
`gate_heldword()` also FAILs any word declared in both `block_local` and `dictation`
(`README_manifest.md` line 116) — so routing `go` through `block_local` would trip a second gate,
because `go` **is** dictation-eligible.

**⚑ Q3 for ruling — E-7.** Closing it means either adding an `override` field to the manifest schema
and to `gate_heldword()`, or ruling that PD-011 overrides are declared some other way. Either is a
**changed gate** and needs a PD. **Not self-applied.**

---

## 5. E-8 — the gates the master says it passed do not exist in the repo suite

The master's v2.0 version log lists, under **"Gates written during the build"**:

> `gate_rehearsal_disjoint()` rewritten to complete cloze prompts and read both sides of arrow
> transformations — the old sweep matched complete sentences only and had reported 31 live
> collisions as clean; `gate_object_head`; `gate_selftry_anticopy` (T10).

Checked against `audits/scripts/run_all.py`:

| Gate | In repo suite? |
|---|---|
| `gate_rehearsal_disjoint` | Present at line 310 — but it is the **OLD** version: a set intersection of `pt_self_try_words` × `demo_box_words`. It does **not** complete cloze prompts and does **not** read arrow transformations |
| `gate_object_head` | **Absent** |
| `gate_selftry_anticopy` | **Absent** |
| `gate_number_sequence` | **Absent** (proposed in STATE.md, never ruled) |

So the rewritten gate that found **31 live rehearsal/graded collisions** exists only in the build's
scratch work, not in `audits/scripts/`. **E-8 is genuinely open**, exactly as the master says.

Running `run_all.py` today would report `Rehearsal/graded disjoint` **PASS** on a word-set comparison
that the master itself records as having reported 31 real collisions as clean. That is a **false
green** — the precise failure the task's C3B08 warning is about.

**⚑ Q4 for ruling — E-8.** Porting the three gates into `audits/scripts/` is a new-gate change and
needs a PD. **Not self-applied.**

---

## 6. The source bank the master drew from is not in the repo

Master front matter: *"Sentence bank: `C4B07_bank_MERGED_312.md` (312 lines)."*

**That file does not exist.** `find . -name "*C4B07*"` returns only the three candidate bank files
(`_bank_S1_S2_candidate.md`, `_bank_S3_S7_candidate.md`, `_bank_ext_candidate.md` — the approved
**256**-line bank), plus STATE, blueprint, orientation, phase2 questions, answer architecture and
number sequences.

The master says the bank went **256 → 284 → 294 → 307 → 312** across units 4–9. **Units 4–9 and the
merged 312-line file are absent from the repo.** Item provenance for any extract therefore cannot be
traced to its bank line.

---

## 7. Governance records are behind the master

| Record | Says | Actual |
|---|---|---|
| `C4B07_STATE.md` | *"No master drafted."* · *"No `C4B07` master file exists"* · Phase 4 open at bank approval · *"⚠ BLOCKER — the audit suite cannot run"* | A **v2.0 complete-block master** exists, 1880 lines. STATE never records it |
| Master front matter | *"Decision Log through **PD-058**"* | Log high-water is **PD-069**. Eleven rulings post-date the master, including **PD-067** (AK before Assignment), which the task cites |
| `governance/CORRECTIONS.md` | ends at **CR-045** | Master v2.0 log cites **CR-046 … CR-053** as applied to the bank, and CR-049 by content. **Eight corrections are unlogged** — a standing §5A breach, pre-existing this session |

**⚑ Q5 — CR-046…CR-053 must be reconstructed into CORRECTIONS.md** before drafting, since §5A
requires re-reading it and stating which PATTERN/PROMOTED rules apply. The agent cannot reconstruct
them: the units that carried them are not in the repo (§6 above).

**⚑ Q6 — STATE.md needs correcting to reality.** Proposed, not applied.

---

## 8. What the agent did NOT do, and why

- Did not build any extract. Under CLAUDE.md §4 no file may be presented as final without verbatim
  passing script output; two gates are declared blocking by the master and confirmed blocking here.
- Did not run `run_all.py` — there is no manifest to run it against, and running it against a
  hand-built one now would produce the false green described in §5.
- Did not write or move the master.
- Did not assign a PD number. **Next free is PD-070** (Log's own note fixed PD-067 as next free;
  PD-067/068/069 are now taken). Assignment waits until the Principal says which of Q1–Q6 is being ruled.
- Did not resolve any of Q1–Q6.

## 9. Recommended order once ruled

1. Rule **Q3 (E-7)** and **Q4 (E-8)** — both are gate changes, both block everything downstream.
2. Port the three built gates into `audits/scripts/`; re-run the suite's selftests.
3. Locate or re-issue `C4B07_bank_MERGED_312.md` and bank units 4–9.
4. Reconstruct **CR-046…CR-053** into `CORRECTIONS.md`.
5. Rule **Q1** (Clue Card in or out) and **Q2** (master's location); correct STATE.md.
6. Author the manifest from the master (224 + PT items), run `run_all.py`, then build
   CW1–4, HW1–4, PT, then **TD and AK last** (§6.11 / PD-067).
