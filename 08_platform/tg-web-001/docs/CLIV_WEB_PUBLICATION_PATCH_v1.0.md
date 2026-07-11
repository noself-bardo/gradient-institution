# CL-IV Web Publication Patch v1.0

**Collection:** Crisis Liturgies IV — Depressive Infrastructure / Domestic Collapse Cycle  
**Patch date:** 2026-07-11  
**Review type:** Website registry patch only — no deploy, no publication-live marking  
**Prior gate:** Public asset upload PASS  

---

## Verdict

# WEB PUBLICATION PATCH PASS

**Authorized status:** WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY

The `CL-VOL-IV` companion shelf entry is patched and locally preview-validated. Commit and deploy remain blocked until separately authorized.

---

## Patched File

| Field | Value |
|---|---|
| Registry file | `data/companion.json` |
| Target entry | `CL-VOL-IV` (`id`: `cl-vol-iv`) |
| Entries modified | **1** (CL-IV only) |
| Schema fields invented | **0** |

---

## CL-VOL-IV Registry State (Post-Patch)

| Field | Value |
|---|---|
| `acc` | `CL-VOL-IV` |
| `title` | Crisis Liturgies IV — Depressive Infrastructure |
| `status` | `Reader PDF hosted` |
| `href` | `https://github.com/noself-bardo/gradient-institution/releases/download/tg-web-pdf-assets/crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| `actionLabel` | `OPEN READER PDF` |
| `hostNote` | GitHub Releases tag tg-web-pdf-assets; filename crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf |
| `sourceNote` | Steward copy remains in Drive / release snapshots (not a public link) |
| `usedFor` | Expanded plate system, infrastructure grief, public-facing explanatory rhythm — 12 issues, 48 pages, screen reader PDF |
| `assetType` | pdf (screen reader PDF) |

---

## Validation Checklist (10 / 10)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | `companion.json` valid JSON | **PASS** | `python -m json.tool` |
| 2 | `CL-VOL-IV` exists exactly once | **PASS** | Single entry with `acc: CL-VOL-IV` |
| 3 | `href` points to authorized GitHub Release URL | **PASS** | Matches upload record |
| 4 | No print PDF filename in public-facing CL-IV fields | **PASS** | `CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_PRINT.pdf` removed |
| 5 | No internal paths in CL-IV entry | **PASS** | No `09_RELEASE_SNAPSHOTS`, `06_RELEASE_ASSEMBLY`, or Windows paths |
| 6 | No Drive paths in CL-IV entry | **PASS** | Generic steward note only |
| 7 | No snapshot zip URL | **PASS** | Not present |
| 8 | Other entries unchanged | **PASS** | CL-VOL-I, CL-VOL-II, CL-CANON-1.1, CL-TRN-001 unmodified |
| 9 | Local validation run | **PASS** | JSON parse + entry scan + HEAD probe HTTP 200 |
| 10 | Deploy not performed | **PASS** | Deferred |

---

## Public Asset Reference

| Field | Value |
|---|---|
| Filename | `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| SHA-256 | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` |
| Size | 10,782,162 bytes (~10.3 MB) |
| Pages | 48 |
| Issues | 12 (CL-IV-001 through CL-IV-012) |

---

## Scope Compliance

| Rule | Result |
|---|---|
| CL-IV / CL-VOL-IV only patched | **PASS** |
| Existing schema preserved | **PASS** |
| No Drive paths exposed | **PASS** |
| No local Windows paths exposed | **PASS** |
| No frozen snapshot paths exposed | **PASS** |
| No print PDF exposed | **PASS** |
| No snapshot zip exposed | **PASS** |
| `companion.json` only (no `sources.json` patch) | **PASS** |
| Deploy not performed | **PASS** |
| Publication not marked live | **PASS** |

---

## UI Behavior (Expected at Preview)

Per `app.js` `pdfAction()`:

- Non-empty `href` + HEAD probe 200 → renders clickable `OPEN READER PDF` anchor
- Public URL opens in new tab (`target="_blank"`, `rel="noopener noreferrer"`)
- Ledger `ACCESS` line shows `AVAILABLE` when HEAD probe succeeds

---

## Status Transition

| From | To | Date |
|---|---|---|
| PUBLIC ASSET UPLOAD COMPLETE — PENDING WEBSITE PATCH | **WEB PUBLICATION PATCH COMPLETE — PENDING LOCAL PREVIEW VALIDATION** | 2026-07-11 |

---

## Gate Status

| Gate | State |
|---|---|
| Visual production | LOCKED |
| Archive lock | LOCKED |
| Release snapshot | FROZEN |
| Print-ready authorization | APPROVED WITH NOTES |
| Public reader PDF prep | COMPLETE |
| Public release authorization | APPROVED WITH NOTES |
| Public asset upload | COMPLETE |
| **Website patch** | **COMPLETE** |
| **Local preview validation** | **PASS** |
| Commit | **PENDING** |
| Deploy | **PENDING** |
| Image generation | CLOSED |

## Status Transition

| From | To | Date |
|---|---|---|
| PUBLIC ASSET UPLOAD COMPLETE — PENDING WEBSITE PATCH | **WEB PUBLICATION PATCH COMPLETE — PENDING LOCAL PREVIEW VALIDATION** | 2026-07-11 |
| WEB PUBLICATION PATCH COMPLETE — PENDING LOCAL PREVIEW VALIDATION | **WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY** | 2026-07-11 |

---

## Next Actions (After Commit Authorization)

1. Commit `data/companion.json` patch + validation records
2. Deploy site (Netlify HTML/CSS/JS only) when authorized
3. Optional: add `SRC-CL-PDF-IV` to `sources.json` in a separate pass

**Local preview validation complete. See `CLIV_WEB_PREVIEW_VALIDATION_v1.0.md`.**

---

## References

- `CLIV_WEB_PREVIEW_VALIDATION_v1.0.md`
- `CLIV_WEB_PREVIEW_VALIDATION_REGISTER_v1.0.md`
- `CLIV_PUBLIC_ASSET_UPLOAD_v1.0.md`
- `CLIV_PUBLIC_RELEASE_RECORD.md`
- `TG-WEB-001_PUBLIC_PDF_STRATEGY.md`
- `data/companion.json`
