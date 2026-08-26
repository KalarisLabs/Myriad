import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cli = path.join(root, 'bin', 'kalaris-myriad.js');
const router = path.join(root, 'examples', 'task-router.js');
function run(args) {
  const r = spawnSync(process.execPath, [cli, ...args], { cwd: root, encoding: 'utf8' });
  assert.equal(r.status, 0, r.stderr || r.stdout);
  return r.stdout;
}

test('stats reports exact graph size', () => {
  const data = JSON.parse(run(['stats','--json']));
  assert.equal(data.tasks, 10000);
  assert.equal(data.domains, 100);
  assert.equal(data.workstreams, 1000);
});

test('show returns canonical task', () => {
  const data = JSON.parse(run(['show','MYR-D051-T001','--json']));
  assert.equal(data.id, 'MYR-D051-T001');
  assert.equal(data.domain_id, 51);
  assert.equal(data.maturity.scientific_validation_claim, 'none');
});

test('search returns relevant results', () => {
  const data = JSON.parse(run(['search','variant off-target','--domain','51','--limit','10','--json']));
  assert.ok(data.length > 0);
  assert.ok(data.every(x => x.domain_id === 51));
});

test('CLI validator passes', () => {
  const data = JSON.parse(run(['validate','--json']));
  assert.equal(data.status, 'PASS');
  assert.equal(data.task_count, 10000);
});

test('task router returns a bounded route without claiming completion', () => {
  const result = spawnSync(process.execPath, [router, 'variant', 'off-target'], {
    cwd: root,
    encoding: 'utf8'
  });
  assert.equal(result.status, 0, result.stderr || result.stdout);
  const data = JSON.parse(result.stdout);
  assert.equal(data.status, 'routed');
  assert.match(data.task.id, /^MYR-/);
  assert.equal(data.task.review_boundary.mode, 'computational-advisory');
  assert.equal(data.task.review_boundary.human_review_required, true);
  assert.equal(data.task.review_boundary.scientific_validation_claim, 'none');
  assert.ok(data.task.expected_evidence.length > 0);
  assert.equal('completed' in data, false);
});

test('task router emits complete JSON when no route matches', () => {
  const request = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz';
  const result = spawnSync(process.execPath, [router, request], {
    cwd: root,
    encoding: 'utf8'
  });
  assert.equal(result.status, 0, result.stderr || result.stdout);
  assert.deepEqual(JSON.parse(result.stdout), {
    status: 'no-route',
    request,
    task: null
  });
});
