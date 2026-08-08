# English Skill-Building Drive — Agent Protocol (CLAUDE.md)

This repository is the authoritative build layer for the English Skill-Building Drive
(Classes 1–5, School for Community Development, Sylhet). The governing policy documents
live in `governance/` and bind every action in this repo. This file defines *how the
agent must operate*; the Charter, Run Book and Drive Plans define *what is correct*.

---

## 1. Session protocol

**On every session start (including the `start` command):**

1. Run `git pull` **before reading any file**. If the pull fails or reports conflicts:
   STOP. Report the exact error. Do not build from a stale or conflicted tree.
2. Read `blocks/<class>/_wip/STATE.md` for any class with an active build.
3. Report to the user, in ≤6 lines: repo status, any in-progress build (block, phase
   reached, what is confirmed, what is pending), and ask what to work on.
4. Do not start drafting until the user confirms the task.

**The `start` command.** When the user's message is just "start" (or "শুরু"), perform
steps 1–3 above and wait.

**On every phase completion and at session end:**

```
git add -A
git commit -m "<class><block>: <phase or change in plain words>"
git push
```

If push is rejected (remote ahead): `git pull --no-rebase`, resolve nothing silently —
if there is any conflict, STOP and report. Never force-push. Never discard local work.

**File deletion.** Deleting files inside `.git/` (lock files, git housekeeping) is
normal operation. Deleting any file OUTSIDE `.git/` requires stating the file and
reason in chat BEFORE the deletion, every time. Never delete `_wip/` contents except
as part of an approved promotion.

---

## 2. Work-in-progress rule (no inline-only drafts)

- Every draft is written to `blocks/<class>/_wip/` as a file **immediately**. Nothing
  exists only in the chat. Chat shows the draft; the file is the record.
- `blocks/<class>/_wip/STATE.md` is updated after **every** phase boundary with:
  block ID, phase reached, decisions confirmed (with who/when), pending questions,
  and the exact next step.
- Commit and push `_wip/` at every phase boundary (Section 1).
- **Promotion:** a file moves from `_wip/` to the class folder (or to `extracts/`)
  **only** on the user's explicit "done" for that file. Promotion = move the file,
  update STATE.md, commit with message `<class><block>: FINAL <filename>`.
- Never delete `_wip/` history mid-build; clear it only after promotion is complete.

---

## 3. Phase-gated build protocol (summary — full text in governance/)

Follow `governance/specs/English_Drive_BlockBuild_StarterTemplate_v2.md` and
Run Book §6–§8. In brief:

- **Phase 1 — Orientation (read-only).** Re-open and re-read: Charter, Run Book, the
  class's Drive Plan, File 2 (pool + batch order), **all** binding exam papers for the
  class, the Block-Build Spec / most recent validated block, and the format-mirror
  block. Never rely on a previous session's citation of a version.
- **Phase 2 — Q&A.** Ask only what the files cannot answer. One consolidated list.
- **Phase 3 — Pre-build review blueprint.** Written to `_wip/`, approved by the user
  before any build content is drafted.
- **Phase 4 — Build.** One unit of work at a time; pause for review between units.
- **Sentence banks are hand-authored and human-vetted.** The agent may draft a
  candidate bank, but it is presented for human approval **before** any worksheet uses
  it. Never generate graded items by pairing word lists against sentence frames.
  An arrangement engine may select and order from an approved bank — never invent
  pairings.

**Pending decisions.** Any conflict with the Charter, Run Book, or a Drive Plan, and
any situation the governing files do not settle, is a Principal Decision. STOP, state
the conflict precisely, and wait. Never resolve a governance question silently, and
never propagate a governance change across files without explicit instruction.

---

## 4. Mandatory programmatic audits (before ANY file is presented as final)

All checks are run by executing the scripts in `audits/scripts/` — **never certified
"by eye" or from the model's own reading**. The workflow:

1. During build, maintain the machine-readable answer manifest
   `_wip/<BLOCKID>_manifest.json` (schema: `audits/scripts/README_manifest.md`).
   The manifest is the extraction of every graded answer set, item text, stated
   mark totals, and dictation list from the draft sheets.
2. Run: `python3 audits/scripts/run_all.py _wip/<BLOCKID>_manifest.json --file2 <path>`
3. Paste the **verbatim script output** into the chat and save it to
   `audits/reports/<BLOCKID>_audit_<date>.txt` (the script does this automatically).
4. A build may be presented for "done" only when every gate is PASS, or a FAIL has an
   explicit user ruling recorded in STATE.md.

The gates (Run Book §6.5 / §6.8 / §6.11):

| Gate | Rule |
|---|---|
| De-patterning | every graded answer set: max run ≤2, no strict alternation |
| CW↔HW positional overlap | ≤35% per paired sheet |
| CW↔HW identical items | ≤2 identical item texts per day |
| PT zero-overlap | zero PT item texts identical (normalised) to any worksheet item |
| Rehearsal/graded disjointness | PT Self-try box shares zero words with the demo box |
| Held-word / exemplar | every graded answer traces to a held word in File 2 (release week ≤ build week) or a declared exemplar — verified on the trigger word, not carrier text |
| One defensible answer | flagged list reviewed by human — script surfaces duplicate-answer candidates; final call is human |
| Mark totals | recomputed from the key; must equal every stated total |
| Sacred-word guard | Allah / আল্লাহ / Quran / কুরআন never a graded classification target (teacher prose is permitted) |
| Values lexicon screen | no music/instrument or festival lexicon in any student-facing text; flags for human review |
| Within-sheet duplicates | no duplicate item texts inside one sheet |

**String matching is punctuation- and case-normalised on both sides** (a comma once
defeated an audit — see Starter Template §B). The scripts already do this; never
substitute an ad-hoc comparison.

**The naturalness gate is human.** No script certifies that a sentence makes sense.
Every sentence bank and every graded sentence is read by a human before promotion.

---

## 5. Standing content guards (Charter §H — always in force)

- §H.3 sacred-word guard: Allah/Quran never a graded classification target.
- §H.4: no non-mahram pairing in any sentence.
- §H.8: no living-being imagery on graded sheets.
- Attribution screen: natural phenomena attributed to Allah, never autonomous
  ("the sun gives…" → recast).
- No music/instruments, no other-faith festival content, modesty and good character
  throughout. House characters: Yusuf, Abdullah, Nusair, Abdur Rahim; Aisha, Raima,
  Maryam, Fatima, Porshi, Rabab, Jesmin.
- No "exam framing" in teacher scripts.
- Exam-format fidelity: graded items mirror the binding Muhammadpur/Mohammadpur paper
  formats as verified from the papers themselves (papers may be ZIP archives despite
  their extension — verify magic bytes before parsing).

---

## 6. Repository map

```
governance/    Charter, Run Book, Decision Log, driveplans/, specs/   (policy — edit only on explicit instruction)
file2/         vocab pools + batch orders (xlsx, per class)
exam-papers/   binding papers (read-only in practice)
blocks/C1–C5/  confirmed block masters; _wip/ for drafts + STATE.md
extracts/      TD / CW / HW / PT deliverables per class
assignments/   weekly assignments + coverage log
audits/        scripts/ (the audit suite) · reports/ (per-build outputs)
```

- Confirmed masters are **never edited in place** for a new version: write the new
  version as a new file (`_v1_6.md` beside `_v1_5.md`), forward-only version log
  inside the file (Charter §K.3).
- Only surgical edits: change exactly what the review comment specifies; confirm
  scope before anything broader.
- **Naming (forward-only).** New block masters use the stem
  `C#_ENG_Block##_Topic_v#.md` (no "GrammarBlock"). Existing filenames are never
  renamed retroactively.

## 7. Communication style

The Principal communicates concisely ("confirm", "done", "good"). Infer scope from
short instructions, state the inferred scope in one line, and proceed. Keep wrappers
minimal — deliver the artefact, flag only real conflicts, pending decisions, or
quality risks. Teacher-facing documents carry a concise checklist wrapper; detailed
guidance lives inside the deliverable.
