#!/usr/bin/env node
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cli = path.join(root, 'bin', 'kalaris-myriad.js');
function main() {
  const request = process.argv.slice(2).join(' ').trim();

  if (!request) {
    console.error('Usage: node examples/task-router.js <biotech request>');
    process.exitCode = 1;
    return;
  }

  const candidates = JSON.parse(execFileSync(process.execPath, [
    cli, 'search', request, '--limit', '1', '--json'
  ], { cwd: root, encoding: 'utf8' }));

  if (candidates.length === 0) {
    console.log(JSON.stringify({ status: 'no-route', request, task: null }, null, 2));
    process.exitCode = 0;
    return;
  }

  const task = candidates[0];
  console.log(JSON.stringify({
    status: 'routed',
    request,
    task: {
      id: task.id,
      routing_name: task.routing.name,
      objective: task.objective,
      expected_evidence: task.execution_contract.required_completion_evidence,
      review_boundary: {
        mode: task.execution_contract.mode,
        human_review_required: task.execution_contract.human_review_required,
        no_call_when: task.execution_contract.no_call_when,
        scientific_validation_claim: task.maturity.scientific_validation_claim
      }
    }
  }, null, 2));
}

main();
