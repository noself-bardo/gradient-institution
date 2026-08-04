# PR 17 Final Merge Receipt — CL-BUILDER / CL-METHOD-001

## Verdict

**MERGED / CUSTODY VERIFIED**

## Repository and pull request

- Repository: `noself-bardo/gradient-institution`
- Pull request: [PR 17 — Add Crisis Liturgies builder MVP and Engineering Stage 02](https://github.com/noself-bardo/gradient-institution/pull/17)
- Source branch: `agent/cl-builder-mvp-v0-1`
- Base branch: `main`
- Pre-merge branch head: `79fbb80ea9a4d430bb3e9ec52bbff2fa66871453`
- Merge commit: `fda112c5edbc46e4b30bb2031cabbe153986ac9a`
- Post-merge main SHA at merge-boundary verification: `fda112c5edbc46e4b30bb2031cabbe153986ac9a`
- Merge method: standard merge commit
- Merged at: `2026-08-04T19:12:38Z`

## CI and tests

- Pre-merge workflow: `Crisis Liturgies Builder Tests`
- Pre-merge workflow run ID: `30942103706`
- Pre-merge workflow conclusion: `SUCCESS`
- Post-merge workflow run ID: `30942223864`
- Post-merge workflow conclusion: `SUCCESS`
- Local tests: `22 / SUCCESS`
- CI tests: `22 / SUCCESS`
- Existing optional external Volume IV corpus-mount test: skipped locally and in CI because `/tmp/cliv_native` was not mounted.
- Committed Volume IV calibration regression: `PASS`

## Pull-request scope

- PR changed-file count: `37`
- PR additions/deletions: `+2588 / -0`
- Final REFUSAL integration commit: `79fbb80ea9a4d430bb3e9ec52bbff2fa66871453`
- Final integration changed-file count: `5`
- Final integration additions/deletions: `+183 / -16`

### Exact final integration files

- `CRISIS_LITURGIES/CL_BUILDER/README.md`
- `CRISIS_LITURGIES/CL_BUILDER/method/CL-METHOD-001.yaml`
- `CRISIS_LITURGIES/CL_BUILDER/method/CL-METHOD-001_PROVEN_PRODUCTION_METHOD_v1.0.md`
- `CRISIS_LITURGIES/CL_BUILDER/references/golden/CL-METHOD-001_REGRESSION_FIXTURES_v1.0.json`
- `CRISIS_LITURGIES/CL_BUILDER/tests/test_builder.py`

## Three-reference regression

- `CL-REF-001 — MIRROR`: `PASS`
- `CL-REF-002 — IVORY`: `PASS`
- `CL-REF-003 — REFUSAL`: `PASS_WITH_COVER_EXCEPTION`
- Canonical interior function order: unchanged
- REFUSAL cover classification: separate `ISSUE_COVER`
- Cover-density exception: applies only to `CL-PM-I02-COVER`
- Interior foreground limit: unchanged at `0.25`
- REFUSAL edge-black coverage: `1.0` on cover and all interiors
- REFUSAL chroma violations: `0`
- REFUSAL transparency violations: `0`
- Typography owner: deterministic layout
- SVG requirement: named layers, live text, vector tonal paths, zero embedded raster images
- REFUSAL package checksum mismatches: `0`

## Custody verification

- MIRROR frozen ZIP SHA-256: `68a5868069cbae0c03f4b8113be743effa480da94bf39f1c2fff1b963c956aab` — matched
- MIRROR proof PDF SHA-256: `d3238da1a29895e32396c2a201d7e22af54b9da04052e9f4aeb84a9fc08f08a1` — matched
- IVORY frozen ZIP SHA-256: `bdff76145940b347a1f52ea554b89aac59898e3bc7398291f7c6d621392dfc6f` — matched
- IVORY proof PDF SHA-256: `1d5c578163125499ba248a015fe569bcf527c0027d48ad694d7bf5deb53ad984` — matched
- REFUSAL package ZIP SHA-256: `5baebe4e73f363474de3ceb3708ed3c4a00498762f8ec220a72b9853a5ec2d6f` — matched
- REFUSAL proof PDF SHA-256: `b6f2a74bcea3be94cfe108c1b10adcfe0e223515f6753f5a36809589f6ebd721` — matched

## Safety and scope

- Render gate for unrelated issues: `CLOSED`
- Full-volume render authorization: `CLOSED`
- Approved visual masters mutated: `NO`
- Approved visual masters added to repository: `NO`
- Unrelated files included in PR: `NO`
- Source branch deletion: deferred until post-merge custody verification; branch was not deleted.

## Bounded exception

The external 48-page Volume IV corpus was not mounted at `/tmp/cliv_native`, so that optional mount-dependent test skipped locally and in CI. The committed calibration report and its profile-lock regression passed, and the governing MIRROR, IVORY, and REFUSAL custody hashes were independently verified.

## Final ruling

`MERGED / CUSTODY VERIFIED / RENDER GATE CLOSED`
