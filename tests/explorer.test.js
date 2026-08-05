import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = (filename) => fs.readFileSync(path.join(root, filename), 'utf8');

test('explorer uses canonical graph data and exposes its required controls', () => {
  const html = read('explorer/index.html');
  const app = read('explorer/app.js');
  assert.match(html, /id="search"/);
  assert.match(html, /id="domain"/);
  assert.match(html, /id="workstream"/);
  assert.match(html, /id="task-dialog"/);
  assert.match(app, /data\/canonical\/all-tasks\.jsonl/);
  assert.match(app, /routing\.name/);
  assert.match(app, /navigator\.clipboard/);
  assert.match(app, /KalarisLabs\/Myriad/);
  assert.match(read('explorer/server.js'), /pathname === '\/explorer\/'/);
});
