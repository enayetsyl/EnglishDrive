# Corrections Ledger — English Drive

Append-only. One row per correction from teacher or Principal review.

Format: | ID | Date | Class/Block | Sheet | Error type | Example (before → after) | Rule extracted | Status |

Status: OPEN (logged) · PATTERN (3+ same type — must become a rule/check) · PROMOTED (now in CLAUDE.md, a gate, or the sentence-bank rules — cite where)

---

| ID | Date | Class/Block | Sheet | Error type | Example (before → after) | Rule extracted | Status |
|---|---|---|---|---|---|---|---|
| CR-001 | retrofit 08.08.26 | C4B06 | CW-1 A3 · HW-1 A14 · CW-3 A2 · HW-4 A16 · HW-1 A9 · CW-4 A11 · +22 (F5) | Unheld word graded | `quickly` (W7) → `slowly`; `run` (absent from File 2) → held verbs; `shelf` → block-local; `red` → `colourful` (held W3) | Every graded target verified against File 2 (release week ≤ build week) or a declared block-local/exemplar set before drafting | PROMOTED — held-word gate + `block_local` manifest field (T1), PD-012/PD-035 |
| CR-002 | retrofit 08.08.26 | C4B06 | C4B0506-PT | Cross-block PT overlap (PD-029 breach) | Part E prompts `meal`, `bird` verbatim from B5 sheets; D1 Yusuf item vs unsat `C4B05-PT` → re-authored (river · teacher · picture · village · spoon; "Abdullah washed his hands") | PT items authored against the full overlap corpus, incl. the prior block and unsat PTs | PROMOTED — PT zero-overlap gate + `audit_scope` (PD-032/PD-034) |
| CR-003 | retrofit 08.08.26 | C4B06 | CW-1/2/4 · HW-2/3/4 (6 items) | Values-lexicon miss (inflection evasion) | "The girl **sings** loudly" → "reads loudly"; "A small bird **sang**" → "sat on the tree" | Values screen matches stems, not whole tokens | PROMOTED — T2 stem matching in values screen |
| CR-004 | retrofit 08.08.26 | C4B06 | CW-1 A11 · CW-2 A8 | Attribution (autonomous natural giver) | "A tall tree **gives shade**" → "A tall tree **grows in the village**" | Natural phenomena never presented as autonomous givers | PROMOTED — CLAUDE.md §5 (human screen; no script check yet) |
| CR-005 | retrofit 08.08.26 | C4B06 | CW-1/3 · HW-1/3 Part C | No unique defensible answer (free-match format) | 4×6 preposition–phrase match, all 24 pairings valid English → choose-between-two, 18 items | Forced-choice items must have exactly one defensible answer; free matching against natural phrases is banned | OPEN |
| CR-006 | retrofit 08.08.26 | C4B06 | HW-1…4 Parts B/C (5 parts) | HW key transcribable from CW | HW-1 B key `in·on·under·near·into·at` mirrored CW-1 → reordered `at·under·in·into·on·near` (39%→0%) | HW answer sequences must not be positionally derivable from the paired CW | PATTERN — scriptable (secondary-key positional check); proposal pending |
| CR-007 | retrofit 08.08.26 | C4B06 + C2B06b | master provenance · PT banner · C2 kickoff | Wrong/stale PD citation | PD-028 cited for block-local set → PD-012; PD-028 for PT carry-forward → PD-029; C2B06b kickoff "combined PT / PD-028" → PD-025 rules | Every PD citation verified against the Decision Log at source before writing | PATTERN — 4 occurrences; citation-check proposal pending |
| CR-008 | retrofit 08.08.26 | C4B06 | CW-1/2/3 · HW-3 (earlier CW-4/HW-4 in v1.3) | Option list omits a graded class | Options "Noun, Verb, Adjective, Pronoun, Preposition" but items keyed **Adverb** → "Adverb" added, all 8 sheets (F10 widened) | Instruction option lists must contain every class keyed on that sheet | PATTERN — 6 occurrences; scriptable from manifest; proposal pending |
| CR-009 | retrofit 08.08.26 | C4B06 | all 8 sheets + PT | Cross-sheet sentence repetition | 38 sentences repeated over 78 placements (CW-4 was 16/20 recycled) → 40 items re-authored; 199 sentences, zero repeats | No sentence reused across the sheets of a block | PATTERN — gate drafted, awaiting ruling (proposed PD-036) |
| CR-010 | retrofit 08.08.26 | C4B06 | CW/HW 1–4 | Unnatural or weak sentence (human read) | v1.5: A7 recast, A8 `man`; v1.6: 5 Principal-supplied rewrites + 9 re-authored items | Naturalness gate is human (§4); recurrence argues hand-authored bank discipline (§3) for every block | PATTERN — remedy proposal pending |
| CR-011 | retrofit 08.08.26 | C4B06 | CW/HW Part B clues · relation clues (sheets 2–4) · `(together)` | Clue language English → Bangla | Part B fill-in clues → Bangla; relation clues → Bangla; `(together)` → `(সঙ্গে)` | Student-facing clue glosses are written in Bangla | PATTERN — 3 occurrences; drive-wide rule proposal pending |
| CR-012 | retrofit 08.08.26 | C4B06 | HW 1–4 Vocabulary Writing | Wrong vocabulary batch | Boxes drawn from a stale batch → re-based on the W6 batch | Vocabulary Writing always drawn from the current week's File 2 batch | OPEN |
| CR-013 | retrofit 08.08.26 | C4B06 | HW-2 A7 | Grammar error in item text | "**on** the month" → "**in** the month" | — (human read) | OPEN |
| CR-014 | retrofit 08.08.26 | C4B06 | teacher text (3 places) | Stated count ≠ list | "**nine** cap prepositions", ten listed → "ten" ×3 | Stated counts recomputed against the lists they describe | OPEN |
| CR-015 | retrofit 08.08.26 | C4B06 | PT Part F / AK | Dual-class word with no marking note | Self-try `this` (Adjective before noun / Pronoun alone) → AK note: mark against the pupil's own sentence; same for `kind` | AK carries a marking note for any dual-class word in a self-try box | OPEN |
| CR-016 | retrofit 08.08.26 | C4B06 | CW/HW-2 (v1.6) | Clue discloses the graded answer | English time clues removed (v1.6 Principal edit) | Clues must not give away the graded answer | OPEN |
