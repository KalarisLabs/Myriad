#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys, hashlib
from collections import Counter, defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'data/canonical/all-tasks.jsonl'
errors, warnings = [], []
records = []
for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
    try: records.append(json.loads(line))
    except json.JSONDecodeError as exc: errors.append(f'line {line_no}: {exc}')
if len(records) != 10000: errors.append(f'expected 10000 records, found {len(records)}')
for label, vals in [
    ('IDs',[r.get('id') for r in records]),
    ('routing names',[r.get('routing',{}).get('name') for r in records]),
    ('titles',[r.get('goal') for r in records]),
    ('objectives',[r.get('objective') for r in records]),
]:
    dups = [x for x,n in Counter(vals).items() if n > 1]
    if dups: errors.append(f'duplicate {label}: {dups[:5]}')
by_domain = defaultdict(list)
placeholder = re.compile(r'\b(todo|tbd|placeholder|lorem ipsum|sample task|example only|fill in|replace me)\b', re.I)
for r in records:
    by_domain[r.get('domain_id')].append(r)
    did, tn = r.get('domain_id'), r.get('task_number')
    expected = f'MYR-D{did:03d}-T{tn:03d}' if isinstance(did,int) and isinstance(tn,int) else None
    if r.get('id') != expected: errors.append(f"bad ID {r.get('id')} expected {expected}")
    if r.get('domain_code') != f'D{did:03d}': errors.append(f"bad domain code {r.get('id')}")
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(r.get('domain_slug',''))): errors.append(f"bad domain slug {r.get('id')}")
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', str(r.get('routing',{}).get('name',''))): errors.append(f"bad routing name {r.get('id')}")
    if placeholder.search(r.get('goal','') + ' ' + r.get('objective','')): errors.append(f"placeholder text {r.get('id')}")
    if len(r.get('routing',{}).get('description','')) < 80: errors.append(f"short routing description {r.get('id')}")
    if not r.get('routing',{}).get('keywords'): errors.append(f"missing keywords {r.get('id')}")
    if r.get('execution_contract',{}).get('human_review_required') is not True: errors.append(f"human review not required {r.get('id')}")
    if not r.get('execution_contract',{}).get('no_call_when'): errors.append(f"missing no-call {r.get('id')}")
    if r.get('maturity',{}).get('scientific_validation_claim') != 'none': errors.append(f"unsupported scientific validation claim {r.get('id')}")
if set(by_domain) != set(range(1,101)): errors.append('domain IDs are not exactly 1-100')
for did, vals in sorted(by_domain.items()):
    if len(vals) != 100: errors.append(f'domain {did} has {len(vals)} tasks')
    ws = Counter(v.get('workstream_index') for v in vals)
    if set(ws) != set(range(1,11)) or any(n != 10 for n in ws.values()): errors.append(f'domain {did} workstreams invalid: {dict(ws)}')
    ddir = root / 'myriad/domains' / f"D{did:03d}-{vals[0]['domain_slug']}"
    for rel in ['README.md','TASKS.md','tasks.json','tasks.jsonl']:
        if not (ddir/rel).is_file(): errors.append(f'missing {ddir/rel}')
    node_files = list((ddir/'nodes').glob('MYR-D*-T*.md')) if (ddir/'nodes').exists() else []
    if len(node_files) != 100: errors.append(f'domain {did} has {len(node_files)} node Markdown files')
for batch in range(1,11):
    start, end = (batch-1)*10+1, batch*10
    bdir = root / 'myriad/batches' / f'batch-{batch:03d}-domains-{start:03d}-{end:03d}'
    for rel in ['README.md','SCIENTIFIC_BASIS.md','BATCH_MANIFEST.json','VALIDATION_REPORT.json','CHECKSUMS.json','validate_batch.py','all-tasks.jsonl']:
        if not (bdir/rel).is_file(): errors.append(f'missing {bdir/rel}')
report = {
    'status': 'FAIL' if errors else 'PASS',
    'task_count': len(records), 'domain_count': len(by_domain), 'batch_count': 10,
    'unique_ids': len({r.get('id') for r in records}),
    'unique_routing_names': len({r.get('routing',{}).get('name') for r in records}),
    'unique_titles': len({r.get('goal') for r in records}),
    'unique_objectives': len({r.get('objective') for r in records}),
    'node_markdown_count': sum(1 for _ in (root/'myriad/domains').glob('D*/nodes/*.md')),
    'errors': errors, 'warnings': warnings,
    'limitations': ['Automated validation does not constitute task-by-task scientific peer review.'],
}
(root/'reports').mkdir(exist_ok=True)
(root/'reports/FINAL_VALIDATION_REPORT.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report, indent=2))
sys.exit(1 if errors else 0)
