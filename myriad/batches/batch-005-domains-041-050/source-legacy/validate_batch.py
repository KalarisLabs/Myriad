from pathlib import Path
import json,re,sys,unicodedata
root=Path(__file__).resolve().parent
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
weak=re.compile(r'^(analy[sz]e|review|assess|evaluate|process|handle|optimi[sz]e|study|investigate)( the)? (data|results|target|compound|screen|assay|model)s?$',re.I)
placeholder=re.compile(r'\b(todo|tbd|placeholder|sample task|example only|lorem|dummy)\b',re.I)
def sig(s):
 s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
 return ' '.join(re.findall(r'[a-z0-9]+',s))
sigs=[]
for t in tasks:
 counts[t['domain_id']]=counts.get(t['domain_id'],0)+1
 works.setdefault(t['domain_id'],{}).setdefault(t['workstream_index'],0); works[t['domain_id']][t['workstream_index']]+=1
 if not re.fullmatch(r'MYR-D\d{3}-T\d{3}',t['id']): errors.append(f'invalid ID {t["id"]}')
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',t['name']): errors.append(f'invalid name {t["name"]}')
 if len(t['title'].split())<8: errors.append(f'title too short {t["id"]}')
 if weak.fullmatch(t['title'].rstrip('.')): errors.append(f'generic title {t["id"]}')
 if placeholder.search(t['title']): errors.append(f'placeholder language {t["id"]}')
 if not t.get('execution_boundary'): errors.append(f'missing boundary {t["id"]}')
 if len(t.get('required_completion_evidence',[]))<5: errors.append(f'insufficient completion evidence {t["id"]}')
 if len(t.get('activation_keywords',[]))<5: errors.append(f'insufficient activation keywords {t["id"]}')
 sigs.append(sig(t['title']))
for did in range(41,51):
 if counts.get(did)!=100: errors.append(f'domain {did} has {counts.get(did,0)} tasks')
 if set(works.get(did,{}))!=set(range(1,11)): errors.append(f'domain {did} missing workstreams')
 if any(v!=10 for v in works.get(did,{}).values()): errors.append(f'domain {did} workstream counts are not all 10')
if len(sigs)!=len(set(sigs)): errors.append('normalized title signatures are not unique')
print(json.dumps({'valid':not errors,'errors':errors,'domains':10,'tasks':len(tasks),'per_domain':counts,'normalized_duplicate_signatures':len(sigs)-len(set(sigs))},indent=2))
sys.exit(1 if errors else 0)
