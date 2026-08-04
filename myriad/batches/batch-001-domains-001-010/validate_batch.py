#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent
records = []
for line_no, line in enumerate((root / 'all-tasks.jsonl').read_text(encoding='utf-8').splitlines(), 1):
    try:
        records.append(json.loads(line))
    except json.JSONDecodeError as exc:
        raise SystemExit(f'FAIL invalid JSON at line {line_no}: {exc}')
errors = []
if len(records) != 1000:
    errors.append(f'expected 1000 tasks, found {len(records)}')
ids = [r.get('id') for r in records]
names = [r.get('routing', {}).get('name') for r in records]
titles = [r.get('goal') for r in records]
for label, vals in [('IDs', ids), ('routing names', names), ('titles', titles)]:
    dup = [k for k,v in Counter(vals).items() if v > 1]
    if dup:
        errors.append(f'duplicate {label}: {dup[:5]}')
by_domain = defaultdict(list)
for r in records:
    by_domain[r.get('domain_id')].append(r)
if len(by_domain) != 10:
    errors.append(f'expected 10 domains, found {len(by_domain)}')
for did, vals in sorted(by_domain.items()):
    if len(vals) != 100:
        errors.append(f'domain {did} has {len(vals)} tasks')
    ws = Counter(v.get('workstream_index') for v in vals)
    if set(ws) != set(range(1,11)) or any(n != 10 for n in ws.values()):
        errors.append(f'domain {did} workstream structure invalid: {dict(ws)}')
    for v in vals:
        expected = f"MYR-D{did:03d}-T{v.get('task_number'):03d}"
        if v.get('id') != expected:
            errors.append(f"bad ID {v.get('id')} expected {expected}")
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(v.get('routing',{}).get('name',''))):
            errors.append(f"bad routing name in {v.get('id')}")
        if v.get('maturity',{}).get('scientific_validation_claim') != 'none':
            errors.append(f"unsupported validation claim in {v.get('id')}")
if errors:
    print('FAIL')
    for e in errors[:100]: print('-', e)
    sys.exit(1)
print(f'PASS: {len(records)} tasks, {len(by_domain)} domains, exact 10×10 structure, unique IDs/names/titles')
