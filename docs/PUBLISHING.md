# Publishing checklist

1. Choose and add an explicit license; the release defaults to `UNLICENSED`.
2. Set the real GitHub repository URL in `package.json` and `CITATION.cff` if desired.
3. Confirm the npm package name is available or select a scoped package name.
4. Run `npm ci`, `npm test`, `python scripts/validate_release.py`, and `npm pack --dry-run`.
5. Inspect the package tarball contents.
6. Configure repository secrets only in GitHub settings, never in committed files.
7. Tag a signed release and attach the checksum manifest.
8. Publish only after Kalaris Labs approves the license and distribution terms.
