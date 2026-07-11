# CL-IV Print-Ready Authorization Record

**Collection:** Crisis Liturgies IV — Depressive Infrastructure / Domestic Collapse Cycle  
**Date:** 2026-07-11  
**Status:** **WEB COMMIT COMPLETE — DEPLOY PENDING (NETLIFY SITE NOT WIRED FOR TG-WEB-001)**  
**Review document:** `CLIV_PRINT_READY_AUTHORIZATION_REVIEW_v1.0.md`  
**Public reader prep:** `CL-IV_PUBLIC_READER_PDF_PREP_v1.0.md` (Drive)  
**Public release:** `CLIV_PUBLIC_RELEASE_AUTHORIZATION_v1.0.md`  
**Public upload:** `CLIV_PUBLIC_ASSET_UPLOAD_v1.0.md`  
**Web patch:** `CLIV_WEB_PUBLICATION_PATCH_v1.0.md`  
**Preview validation:** `CLIV_WEB_PREVIEW_VALIDATION_v1.0.md`  
**Commit/deploy:** `CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md`  

---

## Authorization Determination

| Field | Value |
|---|---|
| Print-ready verdict | PRINT-READY AUTHORIZATION APPROVED WITH NOTES |
| Public reader PDF prep | **COMPLETE** |
| Public release authorization | **APPROVED WITH NOTES** |
| Public asset upload | **COMPLETE** |
| Image gate | CLOSED |
| Frozen snapshot altered | NO |

---

## Approved Print Asset

| Field | Value |
|---|---|
| Filename | `CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_PRINT.pdf` |
| Steward snapshot path | `09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0/07_OUTPUT_QC/` |
| Pages | 48 |
| Issues | 12 (CL-IV-001 – CL-IV-012) |
| Page size | 1086 × 1448 pt |
| SHA-256 | `ca9e2cae59d067e36bedcbdc996a7b6eb9d7704652a5dbee607f371b617b89ae` |

---

## Status Transition

| From | To | Date |
|---|---|---|
| FROZEN RELEASE SNAPSHOT COMPLETE — NOT PRINT-READY | **PRINT-READY AUTHORIZATION APPROVED — NOT PUBLIC-RELEASED** | 2026-07-11 |

---

## Public Reader Asset (Derivative)

| Field | Value |
|---|---|
| Filename | `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| Drive path | `06_RELEASE_ASSEMBLY/.../public_reader_pdf_v1.0/` |
| SHA-256 | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` |
| Size | ~10.3 MB (screen-optimized) |
| Public URL | `https://github.com/noself-bardo/gradient-institution/releases/download/tg-web-pdf-assets/crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| Website patch | **COMPLETE** (`data/companion.json`) |

---

## Gate Status

| Gate | State |
|---|---|
| Visual production | LOCKED |
| Archive lock | LOCKED |
| Release snapshot | FROZEN |
| Print-ready authorization | **APPROVED WITH NOTES** |
| Public reader PDF prep | **COMPLETE** |
| Public release authorization | **APPROVED WITH NOTES** |
| Public asset upload | **COMPLETE** |
| Image generation | **CLOSED** |
| Website / hosting | **PATCHED** (companion registry) |
| Local preview validation | **PASS** |
| Commit / deploy | **COMMIT COMPLETE** (`cbf914c`) · **DEPLOY PENDING** |

---

## Accepted Notes

- CL-IV-011 Page 3 layout-prep safe-area patch verified
- JPEG embedding recompression delta documented (non-blocking)
- No unresolved crop risks
- No canon/safety blockers

---

## Next Actions (Pending Netlify Deploy)

1. Wire Netlify to publish `08_platform/tg-web-001`
2. Run live publication verification
3. Optional: `SRC-CL-PDF-IV` in `sources.json`

**Commit complete. See `CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md`.**

---

## References

- `CLIV_PRINT_READY_AUTHORIZATION_REVIEW_v1.0.md`
- `TG-WEB-001_SOURCE_POLICY.md`
- `TG-WEB-001_PUBLIC_PDF_STRATEGY.md`
- Frozen snapshot README: `CL-IV_RELEASE_SNAPSHOT_README.md`
