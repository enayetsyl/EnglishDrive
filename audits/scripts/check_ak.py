#!/usr/bin/env python3
"""Run Book Section 6.11 Stage 8 - Teacher Answer Key consistency check.

Verifies an AK extract against the block manifest:
  1. every graded item in every artefact has exactly one answer in the AK
  2. no answer in the AK refers to an item number that does not exist
  3. item numbering is continuous and non-duplicated within each artefact
  4. per-artefact mark totals computed from the AK match the printed totals

Usage: python3 audits/scripts/check_ak.py <AK.md> <manifest.json>
A mismatch blocks delivery (Run Book Section 8.2).
"""
import json, re, sys

def parse_ak(path):
    """Recognise the three AK heading styles in use:
         '## CW1 ...' / '## `C3B08-PT` ...'   (C3B08)
         '**CW1**'                             (C3B07)
         '**CW-1 Part A:** 1.Noun 2.Verb ...'  (C4B06, answers inline on the label line)
    """
    txt = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    label = re.compile(
        r'^(?:#{2,3}\s+(?:[A-Za-z ]*?—\s*)?`?|\*\*)'
        r'(?:[A-Z]?\d?[A-Z]?\d*B\d+[a-b]?-)?'      # optional C3B08- / C3B0607- prefix
        r'((?:CW|HW|PT)-?\d?)'
        r'(?:`|\*\*|\s|$)', re.I)
    arts, cur = {}, None
    for line in txt.split('\n'):
        m = label.match(line.strip())
        if line.startswith('###') and not m:
            cur = None
        if m:
            cur = m.group(1).upper().replace('-', '')
            arts.setdefault(cur, {'nums': [], 'letters': [], 'total': None})
            rest = line[m.end():]          # C4B06 puts answers on the label line
        elif cur is None:
            continue
        else:
            rest = line
        t = re.search(r'\*\*Stated total: (\d+)', line)
        if t:
            arts[cur]['total'] = int(t.group(1))
        tot = re.search(r'\*\*Total: (\d+) marks?\*\*', line)
        if tot and arts[cur]['total'] is None:
            arts[cur]['total'] = int(tot.group(1))
        r = rest.strip()
        if not re.match(r'^(\(a\)|\d+\.)', r):
            continue                      # not an answer row (prose, note, total line)
        for n in re.findall(r'(?:^|[\s·])(\d+)\.(?=\s*\S)', r):
            arts[cur]['nums'].append(int(n))
        for l in re.findall(r'\(([a-h])\)\s*\w', r):
            arts[cur]['letters'].append(l)
    return arts

def main(akp, manp):
    ak = parse_ak(akp)
    man = json.load(open(manp, encoding='utf-8'))
    fails, notes = [], []
    for sh in man['sheets']:
        if sh.get('audit_scope') == 'pt_overlap_only':
            continue          # another block's sheets, loaded for PT overlap only (PD-032/PD-034)
        name = sh['name']
        if name not in ak:
            fails.append('%s: artefact missing from the AK' % name); continue
        a = ak[name]
        n_items = sum(len(p['items']) for p in sh['parts'])
        n_ak = len(a['nums']) + len(a['letters'])
        if n_items != n_ak:
            fails.append('%s: %d graded items in the manifest, %d answers in the AK' % (name, n_items, n_ak))
        dup = {x for x in a['nums'] if a['nums'].count(x) > 1}
        if dup:
            fails.append('%s: duplicated item numbers in the AK: %s' % (name, sorted(dup)))
        if a['nums']:
            lo, hi = min(a['nums']), max(a['nums'])
            gaps = sorted(set(range(lo, hi + 1)) - set(a['nums']))
            if gaps:
                fails.append('%s: numbering not continuous, missing %s' % (name, gaps))
        marks = sum(i['marks'] for p in sh['parts'] for i in p['items'])
        if name == 'PT':
            marks += 14  # Part A dictation 10 + Part F rubric 4, not itemised
        if a['total'] is None:
            fails.append('%s: no stated total printed in the AK' % name)
        elif a['total'] != sh['stated_total'] or marks != sh['stated_total']:
            fails.append('%s: AK states %s, manifest states %s, recomputed %s'
                         % (name, a['total'], sh['stated_total'], marks))
        else:
            notes.append('%s: %d items, %g marks' % (name, n_ak, marks))
    print('AK CONSISTENCY CHECK (Run Book Section 6.11) - %s' % akp)
    print('-' * 72)
    for n in notes:
        print('  [ok]   %s' % n)
    for f in fails:
        print('  [FAIL] %s' % f)
    print('-' * 72)
    print('RESULT: %s' % ('PASS' if not fails else 'FAILURES PRESENT - delivery blocked'))
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
