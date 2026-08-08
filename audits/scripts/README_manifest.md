# Audit manifest schema (`<BLOCKID>_manifest.json`)

The manifest is the machine-readable extraction of a block's graded content. The
agent builds it in `_wip/` **during** the build (not after, from memory) and keeps it
in sync with every edit to the sheets. `run_all.py` verifies the manifest; the human
verifies the manifest matches the sheets (spot-check).

```json
{
  "block_id": "C2B06b",
  "build_week": 6,
  "exemplars": ["hour", "honest"],

  "sheets": [
    {
      "name": "CW1",
      "type": "worksheet",          // "worksheet" or "pt"
      "pair": "HW1",                // paired sheet for the ≤35% overlap gate
      "stated_total": 30,           // the total printed on the sheet
      "parts": [
        {
          "name": "A",
          "marks": null,            // optional part-level mark override
          "items": [
            {
              "text": "Yusuf ___ a red pen.",   // full item text as printed
              "answer": "has",                   // the keyed answer
              "trigger": "pen",                  // the held word the item grades
              "marks": 1
            }
          ],
          "answers": null           // optional: bare answer sequence when items
                                    // are not itemised (e.g. a tick column)
        }
      ]
    },
    {
      "name": "PT",
      "type": "pt",
      "stated_total": 30,
      "parts": [ ... ]
    }
  ],

  "dictation": ["pen", "book", "..."],
  "pt_self_try_words": ["cat", "..."],
  "demo_box_words": ["tree", "..."]
}
```

Field notes:

- **`trigger`** — the word whose held/exemplar status justifies grading the item.
  This is what the held-word gate checks; carrier text is not checked. If the
  manifest omits `trigger` everywhere, the gate reports itself vacuous — fill it in.
- **`answers`** (part-level) — use for parts where only the answer sequence matters
  for de-patterning (e.g. a/an columns) and items are enumerated elsewhere.
- **`pair`** — declare on the CW side; one direction is enough.
- **`audit_scope`** (sheet-level, optional) — set to `"pt_overlap_only"` to make a
  sheet visible **only** to the PT zero-overlap gate. Use it to bring another
  block's **already-validated** worksheets into the PT comparison without
  re-running de-patterning, mark totals, held-word or the other gates over them.
  A sheet with no `audit_scope` key is graded normally, so manifests that declare
  none are unaffected. Self-test: `audits/scripts/selftest_audit_scope.py`.
  Authorised for two shapes:
  - **PD-032** — a two-week `a`/`b` split block whose b-half PT grades a-half grammar.
  - **PD-034** — a §6.7 **paired-week recovery**: a PT built but not administered,
    whose assessment is carried into a combined PT the following week
    (PD-029: `C4B05-PT` → `C4B0506-PT`). Load the other block's worksheets **and the
    unadministered PT** as reference sheets — PD-029 requires zero overlap against both.
- **`exemplars`** — PD-009 Grammar Exemplars declared for this block only.
- **`block_local`** — PD-012 block-local teaching set: taught in-block, gradeable in
  this block's CW/HW/PT only, **not** in File 2, **not** held downstream, and **never**
  a dictation or spelling item. The gate enforces that last rule: a word listed in both
  `block_local` and `dictation` is a FAIL. Declaring a word in both `block_local` and
  `exemplars` is also a FAIL — they are different instruments, pick one.
- **`build_week`** — the week the block runs; held words must have release week ≤ this.
- All text is stored exactly as printed; the scripts normalise internally.

## File 2 loader

`--file2 <pool.xlsx>`: the loader scans each worksheet's header row for a word
column (`word`, `english`, or any header containing "word") and an optional release
column (any header containing `week`, `release`, or `batch`). If your File 2 layout
differs, either rename headers or extend `load_file2_words()` in `run_all.py`.

## What is deliberately NOT automated

- **Naturalness** — every sentence read by a human before promotion.
- **One-defensible-answer** — the script only surfaces cross-sheet conflicts; the
  real check (could another answer also be correct?) is a human read of the key.
- **Non-mahram pairing / imagery / attribution screens** — human, per Charter §H.
