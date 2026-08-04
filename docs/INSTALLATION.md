# Installation

## Repository checkout

```bash
git clone <repository-url>
cd <repository-directory>
npm install
npm test
node bin/kalaris-myriad.js stats
```

## Local package archive

```bash
npm install -g ./artifacts/npm/kalaris-myriad-1.0.0.tgz
kalaris-myriad stats
```

## NPX after npm publication

```bash
npx kalaris-myriad stats
```

## GitHub package spec after pushing

```bash
npx github:<owner>/<repository> stats
```

Set the repository URL in `package.json` before publication.
