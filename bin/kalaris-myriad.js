#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const root = path.resolve(path.dirname(__filename), '..');
const dataPath = path.join(root, 'data', 'canonical', 'all-tasks.jsonl');
const domainsPath = path.join(root, 'data', 'canonical', 'domains.json');

function parseArgs(argv) {
  const positional = [];
  const flags = {};
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (next !== undefined && !next.startsWith('--')) { flags[key] = next; i += 1; }
      else flags[key] = true;
    } else positional.push(a);
  }
  return { positional, flags };
}

async function loadTasks() {
  const tasks = [];
  const input = fs.createReadStream(dataPath, { encoding: 'utf8' });
  const rl = readline.createInterface({ input, crlfDelay: Infinity });
  for await (const line of rl) if (line.trim()) tasks.push(JSON.parse(line));
  return tasks;
}

function domainId(value) {
  if (value === undefined) return null;
  const m = String(value).match(/\d+/);
  if (!m) throw new Error(`Invalid domain: ${value}`);
  const n = Number(m[0]);
  if (!Number.isInteger(n) || n < 1 || n > 100) throw new Error(`Domain must be 1-100: ${value}`);
  return n;
}

function printHelp() {
  console.log(`MYRIAD CLI

Usage:
  kalaris-myriad stats [--json]
  kalaris-myriad list domains [--json]
  kalaris-myriad list tasks [--domain <1-100>] [--limit <n>] [--json]
  kalaris-myriad search <query> [--domain <1-100>] [--limit <n>] [--json]
  kalaris-myriad show <task-id-or-routing-name> [--json]
  kalaris-myriad export --format <jsonl|json|md> --output <path> [--domain <1-100>]
  kalaris-myriad validate [--json]
  kalaris-myriad init [directory] [--domain <1-100>]
`);
}

function output(value, jsonMode = false) {
  if (jsonMode) console.log(JSON.stringify(value, null, 2));
  else console.log(value);
}

function taskLine(t) { return `${t.id}  ${t.goal}`; }

async function validate(tasks) {
  const errors = [];
  if (tasks.length !== 10000) errors.push(`Expected 10000 tasks, found ${tasks.length}`);
  for (const key of ['id']) {
    const vals = tasks.map(t => t[key]);
    if (new Set(vals).size !== vals.length) errors.push(`Duplicate ${key}`);
  }
  const names = tasks.map(t => t.routing?.name);
  const titles = tasks.map(t => t.goal);
  if (new Set(names).size !== tasks.length) errors.push('Duplicate routing name');
  if (new Set(titles).size !== tasks.length) errors.push('Duplicate title');
  const grouped = new Map();
  for (const t of tasks) {
    if (!grouped.has(t.domain_id)) grouped.set(t.domain_id, []);
    grouped.get(t.domain_id).push(t);
    const expected = `MYR-D${String(t.domain_id).padStart(3,'0')}-T${String(t.task_number).padStart(3,'0')}`;
    if (t.id !== expected) errors.push(`Bad ID ${t.id}; expected ${expected}`);
    if (t.maturity?.scientific_validation_claim !== 'none') errors.push(`Unsupported validation claim ${t.id}`);
    if (t.execution_contract?.human_review_required !== true) errors.push(`Missing human review ${t.id}`);
  }
  if (grouped.size !== 100) errors.push(`Expected 100 domains, found ${grouped.size}`);
  for (const [did, vals] of grouped) {
    if (vals.length !== 100) errors.push(`Domain ${did} has ${vals.length} tasks`);
    const ws = new Map();
    for (const v of vals) ws.set(v.workstream_index, (ws.get(v.workstream_index) || 0) + 1);
    if (ws.size !== 10 || [...ws.values()].some(n => n !== 10)) errors.push(`Domain ${did} workstream structure invalid`);
  }
  return { status: errors.length ? 'FAIL' : 'PASS', task_count: tasks.length, domain_count: grouped.size, errors };
}

const { positional, flags } = parseArgs(process.argv.slice(2));
const command = positional[0] || 'help';

try {
  if (command === 'help' || flags.help) { printHelp(); process.exit(0); }
  if (command === 'stats') {
    const tasks = await loadTasks();
    const stats = {
      release: '1.0.0', tasks: tasks.length,
      domains: new Set(tasks.map(t => t.domain_id)).size,
      batches: new Set(tasks.map(t => t.batch_id)).size,
      workstreams: new Set(tasks.map(t => `${t.domain_id}:${t.workstream_index}`)).size,
      maturity: 'taxonomy-defined', seed_skills: 3,
    };
    if (flags.json) output(stats, true);
    else output(`MYRIAD ${stats.release}\n${stats.domains} domains · ${stats.workstreams} workstreams · ${stats.tasks} tasks · ${stats.batches} batches\nMaturity: ${stats.maturity}; full seed skills: ${stats.seed_skills}`);
  } else if (command === 'list') {
    const what = positional[1] || 'domains';
    if (what === 'domains') {
      const domains = JSON.parse(fs.readFileSync(domainsPath, 'utf8'));
      if (flags.json) output(domains, true);
      else output(domains.map(d => `${String(d.domain_id).padStart(3,'0')}  ${d.name}  (${d.task_count})`).join('\n'));
    } else if (what === 'tasks') {
      let tasks = await loadTasks();
      const did = domainId(flags.domain);
      if (did) tasks = tasks.filter(t => t.domain_id === did);
      const limit = Math.max(1, Number(flags.limit || 50));
      tasks = tasks.slice(0, limit);
      if (flags.json) output(tasks, true); else output(tasks.map(taskLine).join('\n'));
    } else throw new Error(`Unknown list target: ${what}`);
  } else if (command === 'search') {
    const query = positional.slice(1).join(' ').trim();
    if (!query) throw new Error('Search query is required');
    const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    const did = domainId(flags.domain);
    const tasks = await loadTasks();
    const scored = [];
    for (const t of tasks) {
      if (did && t.domain_id !== did) continue;
      const title = t.goal.toLowerCase();
      const name = t.routing.name.toLowerCase();
      const hay = [t.domain, t.workstream, t.goal, t.objective, ...t.routing.keywords].join(' ').toLowerCase();
      let score = 0;
      for (const term of terms) {
        if (title.includes(term)) score += 5;
        if (name.includes(term)) score += 4;
        if (hay.includes(term)) score += 1;
      }
      if (score > 0 && terms.every(term => hay.includes(term))) scored.push({ score, task: t });
    }
    scored.sort((a,b) => b.score - a.score || a.task.id.localeCompare(b.task.id));
    const limit = Math.max(1, Number(flags.limit || 20));
    const results = scored.slice(0, limit).map(x => x.task);
    if (flags.json) output(results, true); else output(results.length ? results.map(taskLine).join('\n') : 'No matching tasks.');
  } else if (command === 'show') {
    const key = positional[1];
    if (!key) throw new Error('Task ID or routing name is required');
    const tasks = await loadTasks();
    const found = tasks.find(t => t.id.toLowerCase() === key.toLowerCase() || t.routing.name === key);
    if (!found) throw new Error(`Task not found: ${key}`);
    if (flags.json) output(found, true);
    else output(`# ${found.id} — ${found.goal}\n\nDomain: ${found.domain}\nWorkstream: ${found.workstream}\nRouting name: ${found.routing.name}\nStatus: ${found.maturity.status}\n\n${found.objective}\n\nBoundary: computational-advisory; qualified review required.`);
  } else if (command === 'export') {
    const format = String(flags.format || 'jsonl').toLowerCase();
    const out = flags.output;
    if (!out) throw new Error('--output is required');
    let tasks = await loadTasks();
    const did = domainId(flags.domain);
    if (did) tasks = tasks.filter(t => t.domain_id === did);
    let body;
    if (format === 'jsonl') body = tasks.map(t => JSON.stringify(t)).join('\n') + '\n';
    else if (format === 'json') body = JSON.stringify(tasks, null, 2) + '\n';
    else if (format === 'md') body = tasks.map(t => `## ${t.id} — ${t.goal}\n\n${t.objective}\n`).join('\n');
    else throw new Error(`Unsupported format: ${format}`);
    fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
    fs.writeFileSync(path.resolve(out), body, 'utf8');
    output(`Wrote ${tasks.length} tasks to ${path.resolve(out)}`);
  } else if (command === 'validate') {
    const report = await validate(await loadTasks());
    if (flags.json) output(report, true);
    else output(`${report.status}: ${report.task_count} tasks, ${report.domain_count} domains${report.errors.length ? `\n${report.errors.join('\n')}` : ''}`);
    if (report.status !== 'PASS') process.exitCode = 1;
  } else if (command === 'init') {
    const destination = path.resolve(positional[1] || 'myriad-project');
    const did = domainId(flags.domain);
    if (fs.existsSync(destination) && fs.readdirSync(destination).length) throw new Error(`Destination is not empty: ${destination}`);
    fs.mkdirSync(path.join(destination, 'data'), { recursive: true });
    let tasks = await loadTasks();
    if (did) tasks = tasks.filter(t => t.domain_id === did);
    fs.writeFileSync(path.join(destination, 'data', 'tasks.jsonl'), tasks.map(t => JSON.stringify(t)).join('\n') + '\n');
    fs.writeFileSync(path.join(destination, 'myriad.config.json'), JSON.stringify({ schema_version:'1.0.0', domain: did, task_count: tasks.length }, null, 2) + '\n');
    fs.writeFileSync(path.join(destination, 'README.md'), `# MYRIAD project\n\nInitialized with ${tasks.length} canonical task nodes.\n`);
    output(`Initialized ${destination} with ${tasks.length} tasks.`);
  } else throw new Error(`Unknown command: ${command}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exitCode = 1;
}
