# CL-IV Web Publication Patch — Diff Summary v1.0

**Patch date:** 2026-07-11  
**File:** `08_platform/tg-web-001/data/companion.json`  
**Entry:** `CL-VOL-IV` only  

---

## Summary

One entry patched. Five fields changed. Zero schema additions. Four sibling entries unchanged.

---

## Changed Fields (`CL-VOL-IV`)

| Field | Before | After |
|---|---|---|
| `status` | `Reader PDF needed` | `Reader PDF hosted` |
| `href` | `""` (empty) | `https://github.com/noself-bardo/gradient-institution/releases/download/tg-web-pdf-assets/crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| `actionLabel` | `OPEN VOLUME (PDF)` | `OPEN READER PDF` |
| `hostNote` | `Public reader asset host pending — preferred GitHub Releases tag tg-web-pdf-assets; filename CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_PRINT.pdf` | `GitHub Releases tag tg-web-pdf-assets; filename crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| `sourceNote` | `Steward copy from 09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0 (not a public link)` | `Steward copy remains in Drive / release snapshots (not a public link)` |
| `usedFor` | `Expanded plate system, infrastructure grief, public-facing explanatory rhythm` | `Expanded plate system, infrastructure grief, public-facing explanatory rhythm — 12 issues, 48 pages, screen reader PDF` |

---

## Unchanged Fields (`CL-VOL-IV`)

| Field | Value |
|---|---|
| `id` | `cl-vol-iv` |
| `acc` | `CL-VOL-IV` |
| `title` | Crisis Liturgies IV — Depressive Infrastructure |
| `role` | Visual / interpretive companion |
| `authority` | Companion, not authority |
| `assetType` | pdf |
| `publicSafe` | true |

---

## Unchanged Entries

| `acc` | `href` | `status` |
|---|---|---|
| `CL-VOL-I` | `""` | `Reader PDF needed` |
| `CL-VOL-II` | `""` | `Reader PDF needed` |
| `CL-CANON-1.1` | `""` | `Reader PDF needed` |
| `CL-TRN-001` | `""` | `Reader PDF needed` |

---

## Removed from Public-Facing CL-IV Text

- Print filename: `CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_PRINT.pdf`
- Frozen snapshot path: `09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0`

---

## Files Not Modified

| File | Reason |
|---|---|
| `data/sources.json` | Optional `SRC-CL-PDF-IV` deferred |
| `assets/pdf/README.md` | Out of patch scope |
| `app.js` | No renderer changes required |
| `index.html` | No copy changes required |

---

## Verdict

**WEB PUBLICATION PATCH PASS**
