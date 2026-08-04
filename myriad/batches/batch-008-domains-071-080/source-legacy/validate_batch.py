from pathlib import Path
import json,re,sys,unicodedata
root=Path(__file__).resolve().parent
phase=root.parent
tasks=[json.loads(x) for x in (root/'all-tasks.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
manifest=json.loads((root/'BATCH_MANIFEST.json').read_text())
errors=[]
if manifest.get('domain_count')!=10: errors.append('domain_count must be 10')
if manifest.get('tasks_per_domain')!=100: errors.append('tasks_per_domain must be 100')
if len(tasks)!=1000: errors.append(f'expected 1000 tasks, found {len(tasks)}')
for label,key in [('IDs','id'),('routing names','name'),('titles','title')]:
 vals=[t[key].casefold() if key=='title' else t[key] for t in tasks]
 if len(vals)!=len(set(vals)): errors.append(f'{label} are not unique')
counts={}; works={}
weak=re.compile(r'^(analy[sz]e|review|assess|evaluate|process|handle|optimi[sz]e|study|investigate)( the)? (data|results|target|compound|screen|assay|model|process)s?$',re.I)
placeholder=re.compile(r'\b(todo|tbd|placeholder|sample task|example only|lorem|dummy|etc\.)\b',re.I)
def tokens(s):
 s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
 return set(re.findall(r'[a-z0-9]+',s))
def sig(s): return ' '.join(sorted(tokens(s)))
sigs=[]; mintitle=999
for t in tasks:
 counts[t['domain_id']]=counts.get(t['domain_id'],0)+1
 works.setdefault(t['domain_id'],{}).setdefault(t['workstream_index'],0); works[t['domain_id']][t['workstream_index']]+=1
 if not re.fullmatch(r'MYR-D\d{3}-T\d{3}',t['id']): errors.append(f'invalid ID {t["id"]}')
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',t['name']): errors.append(f'invalid name {t["name"]}')
 wc=len(t['title'].split()); mintitle=min(mintitle,wc)
 if wc<8: errors.append(f'title too short {t["id"]}')
 if weak.fullmatch(t['title'].rstrip('.')): errors.append(f'generic title {t["id"]}')
 if placeholder.search(t['title']): errors.append(f'placeholder language {t["id"]}')
 if not t.get('execution_boundary'): errors.append(f'missing boundary {t["id"]}')
 if len(t.get('required_completion_evidence',[]))<5: errors.append(f'insufficient completion evidence {t["id"]}')
 if len(t.get('activation_keywords',[]))<5: errors.append(f'insufficient activation keywords {t["id"]}')
 sigs.append(sig(t['title']))
for did in range(71,81):
 if counts.get(did)!=100: errors.append(f'domain {did} has {counts.get(did,0)} tasks')
 if set(works.get(did,{}))!=set(range(1,11)): errors.append(f'domain {did} missing workstreams')
 if any(v!=10 for v in works.get(did,{}).values()): errors.append(f'domain {did} workstream counts are not all 10')
if len(sigs)!=len(set(sigs)): errors.append('normalized title signatures are not unique')
near=[]; tok=[tokens(t['title']) for t in tasks]
for i in range(len(tasks)):
 for j in range(i+1,len(tasks)):
  a,b=tok[i],tok[j]; score=len(a&b)/len(a|b)
  if score>=0.92: near.append((tasks[i]['id'],tasks[j]['id'],round(score,3)))
if near: errors.append(f'near-duplicate title pairs: {near[:10]}')
previous=[]
for p in sorted(phase.glob('batch-00[1-7]-domains-*/all-tasks.jsonl')):
 previous.extend(json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip())
for key in ['id','name','title']:
 old={x[key].casefold() if key=='title' else x[key] for x in previous}
 clashes=[t['id'] for t in tasks if (t[key].casefold() if key=='title' else t[key]) in old]
 if clashes: errors.append(f'cross-batch {key} clashes: {clashes[:10]}')
report={'valid':not errors,'errors':errors,'batch':'008','domain_range':[71,80],'domain_count':10,'task_count':len(tasks),
 'tasks_per_domain':{str(k):v for k,v in sorted(counts.items())},'unique_ids':len({t['id'] for t in tasks}),
 'unique_routing_names':len({t['name'] for t in tasks}),'unique_titles':len({t['title'].casefold() for t in tasks}),
 'minimum_title_word_count':mintitle,'normalized_near_duplicate_pairs_at_or_above_0_92':len(near),
 'cross_batch_task_count_checked':len(previous)+len(tasks),'placeholder_scan':'pass' if not any('placeholder' in e for e in errors) else 'fail',
 'execution_boundary_records':sum(bool(t.get('execution_boundary')) for t in tasks),
 'completion_evidence_records':sum(len(t.get('required_completion_evidence',[]))>=5 for t in tasks)}
print(json.dumps(report,indent=2)); sys.exit(1 if errors else 0)
