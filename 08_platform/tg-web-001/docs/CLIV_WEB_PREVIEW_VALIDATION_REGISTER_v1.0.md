# CL-IV Web Preview Validation Register v1.0

**Validation date:** 2026-07-11  
**Verdict:** WEB PREVIEW VALIDATION PASS  
**Status:** WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY  

---

## Run Configuration

| Parameter | Value |
|---|---|
| Server | `python -m http.server 8765` |
| Root | `08_platform/tg-web-001/` |
| Target entry | `CL-VOL-IV` |
| Authorized URL | `https://github.com/noself-bardo/gradient-institution/releases/download/tg-web-pdf-assets/crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |

---

## Check Register (35 / 35 PASS)

| ID | Check | Result |
|---|---|---|
| R-001 | `companion.json` valid JSON | PASS |
| R-002 | `index.html` served locally | PASS |
| R-003 | `CL-VOL-IV` exists exactly once in registry | PASS |
| R-004 | Registry `href` = authorized URL | PASS |
| R-005 | Registry `status` = `Reader PDF hosted` | PASS |
| R-006 | Registry `actionLabel` = `OPEN READER PDF` | PASS |
| R-007 | Registry `hostNote` contains screen filename | PASS |
| R-008 | Registry `hostNote` contains `tg-web-pdf-assets` | PASS |
| R-009 | Registry `sourceNote` has no snapshot path | PASS |
| R-010 | Registry `usedFor` contains 12 issues, 48 pages, screen reader PDF | PASS |
| R-011 | Authorized URL HEAD returns 200 | PASS |
| R-012 | `CL-VOL-IV` ledger entry renders | PASS |
| R-013 | CTA text = `OPEN READER PDF` | PASS |
| R-014 | CTA ≠ `READER PDF NEEDED` | PASS |
| R-015 | Anchor `href` = authorized URL | PASS |
| R-016 | ACCESS line = `AVAILABLE` | PASS |
| R-017 | No `09_RELEASE_SNAPSHOTS` in CL-IV UI | PASS |
| R-018 | No `06_RELEASE_ASSEMBLY` in CL-IV UI | PASS |
| R-019 | No `My Drive` in CL-IV UI | PASS |
| R-020 | No Windows paths in CL-IV UI | PASS |
| R-021 | No Googleusercontent in CL-IV UI | PASS |
| R-022 | No `.zip` in CL-IV UI | PASS |
| R-023 | No print PDF filename in CL-IV UI | PASS |
| R-024 | No `archive-lock` in CL-IV UI | PASS |
| R-025 | No `checksum` in CL-IV UI | PASS |
| R-026 | `CL-VOL-I` renders | PASS |
| R-027 | `CL-VOL-I` shows pending CTA | PASS |
| R-028 | `CL-VOL-II` renders | PASS |
| R-029 | `CL-VOL-II` shows pending CTA | PASS |
| R-030 | `CL-CANON-1.1` renders | PASS |
| R-031 | `CL-CANON-1.1` shows pending CTA | PASS |
| R-032 | `CL-TRN-001` renders | PASS |
| R-033 | `CL-TRN-001` shows pending CTA | PASS |
| R-034 | Desktop layout CSS present | PASS |
| R-035 | Mobile breakpoint CSS present | PASS |

---

## Files Validated (Read-Only)

| File | Modified |
|---|---|
| `data/companion.json` | No |
| `index.html` | No |
| `app.js` | No |
| `styles.css` | No |
| `data/sources.json` | No (deferred) |

---

## Out of Scope (Confirmed Not Run)

- Netlify deploy
- Publication-live marking
- Asset upload
- Frozen snapshot modification
- Public reader PDF modification
- Image regeneration
- `companion.json` further edits

---

## Disposition

```text
WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY
```
