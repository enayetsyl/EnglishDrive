# One-time setup

## On your machine (developer)
1. Copy your existing English Drive files into this structure (governance/, file2/,
   exam-papers/, blocks/, extracts/). Confirmed masters go directly in blocks/<class>/.
2. `git init && git add -A && git commit -m "initial import"`
3. Create a private GitHub repo, then:
   `git remote add origin <url> && git push -u origin main`
4. Optional: open the folder in Claude Desktop (Cowork/Code tab) and ask the agent to
   verify the structure and CLAUDE.md are being picked up.

## On the teacher's machine (once, by you)
1. Install Git + Claude Desktop; clone the repo to a fixed folder.
2. Authenticate GitHub once (GitHub CLI: `gh auth login`, or credential manager).
3. Pin the folder in Claude Desktop's Cowork/Code tab.
4. Her workflow forever after: open app → type "start" → answer which block →
   review → "done".

## Audit suite check
`python3 audits/scripts/run_all.py <manifest.json> --file2 file2/<BatchOrder>.xlsx`
Use the class's **Batch Order** file (it carries the Word → Week release map), not the
Pool file. Requires `pip install openpyxl`.
