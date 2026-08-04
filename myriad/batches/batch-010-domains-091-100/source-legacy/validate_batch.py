from pathlib import Path
import json,re,sys,unicodedata
from collections import defaultdict
root=Path(__file__).resolve().parent
phase=root.parent
tasks=[json.loads(x) for x in (root/'all-tasks.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
manifest=json.loads((root/'BATCH_MANIFEST.json').read_text(encoding='utf-8'))
errors=[]
if manifest.get('domain_count')!=10: errors.append('domain_count must be 10')
if manifest.get('tasks_per_domain')!=100: errors.append('tasks_per_domain must be 100')
if len(tasks)!=1000: errors.append(f'expected 1000 tasks, found {len(tasks)}')
for label,key in [('IDs','id'),('routing names','name'),('titles','title')]:
 vals=[t[key].casefold() if key=='title' else t[key] for t in tasks]
 if len(vals)!=len(set(vals)): errors.append(f'{label} are not unique')
counts=defaultdict(int); works=defaultdict(lambda:defaultdict(int))
placeholder=re.compile(r'\b(todo|tbd|placeholder|sample task|example only|lorem|dummy|fill[ -]?in|coming soon|etc\.)\b',re.I)
def tokens(s):
 s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
 return set(re.findall(r'[a-z0-9]+',s))
def sig(s): return ' '.join(sorted(tokens(s)))
sigs=[]; mintitle=999; minobjective=999
for t in tasks:
 counts[t['domain_id']]+=1; works[t['domain_id']][t['workstream_index']]+=1
 if not re.fullmatch(r'MYR-D\d{3}-T\d{3}',t['id']): errors.append(f'invalid ID {t["id"]}')
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',t['name']): errors.append(f'invalid name {t["name"]}')
 tw=len(t['title'].split()); ow=len(t['objective'].split()); mintitle=min(mintitle,tw); minobjective=min(minobjective,ow)
 if tw<10: errors.append(f'title too short {t["id"]}')
 if ow<35: errors.append(f'objective too short {t["id"]}')
 if placeholder.search(t['title']) or placeholder.search(t['objective']): errors.append(f'placeholder language {t["id"]}')
 if not t.get('execution_boundary'): errors.append(f'missing boundary {t["id"]}')
 if len(t.get('required_completion_evidence',[]))<5: errors.append(f'insufficient completion evidence {t["id"]}')
 if len(t.get('activation_keywords',[]))<8: errors.append(f'insufficient activation keywords {t["id"]}')
 sigs.append(sig(t['title']))
for did in range(91,101):
 if counts.get(did)!=100: errors.append(f'domain {did} has {counts.get(did,0)} tasks')
 if set(works.get(did,{}))!=set(range(1,11)): errors.append(f'domain {did} missing workstreams')
 if any(v!=10 for v in works.get(did,{}).values()): errors.append(f'domain {did} workstream counts are not all ten')
if len(sigs)!=len(set(sigs)): errors.append('normalized title signatures are not unique')
previous=[]
for p in sorted(phase.glob('batch-*-domains-*/all-tasks.jsonl')):
 try: bn=int(p.parent.name.split('-')[1])
 except Exception: continue
 if bn<10: previous.extend(json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip())
for key in ['id','name','title']:
 old={x[key].casefold() if key=='title' else x[key] for x in previous}
 clashes=[t['id'] for t in tasks if (t[key].casefold() if key=='title' else t[key]) in old]
 if clashes: errors.append(f'cross-batch {key} clashes: {clashes[:10]}')
report={'valid':not errors,'errors':errors,'batch':'010','domain_range':[91,100],
'domain_count':10,'task_count':len(tasks),'tasks_per_domain':{str(k):v for k,v in sorted(counts.items())},
'unique_ids':len({t['id'] for t in tasks}),'unique_routing_names':len({t['name'] for t in tasks}),
'unique_titles':len({t['title'].casefold() for t in tasks}),'minimum_title_word_count':mintitle,
'minimum_objective_word_count':minobjective,'cross_batch_task_count_checked':len(previous)+len(tasks),
'placeholder_scan':'pass' if not any('placeholder' in e for e in errors) else 'fail',
'execution_boundary_records':sum(bool(t.get('execution_boundary')) for t in tasks),
'completion_evidence_records':sum(len(t.get('required_completion_evidence',[]))>=5 for t in tasks)}
print(json.dumps(report,indent=2)); sys.exit(1 if errors else 0)
