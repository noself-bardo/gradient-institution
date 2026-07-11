# CL-IV Public Release Record

**Collection:** Crisis Liturgies IV — Depressive Infrastructure / Domestic Collapse Cycle  
**Date:** 2026-07-11  
**Status:** **WEB COMMIT COMPLETE — DEPLOY PENDING (NETLIFY SITE NOT WIRED FOR TG-WEB-001)**  
**Review document:** `CLIV_PUBLIC_RELEASE_AUTHORIZATION_v1.0.md`  
**Upload document:** `CLIV_PUBLIC_ASSET_UPLOAD_v1.0.md`  
**Patch document:** `CLIV_WEB_PUBLICATION_PATCH_v1.0.md`  
**Preview validation:** `CLIV_WEB_PREVIEW_VALIDATION_v1.0.md`  
**Commit/deploy:** `CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md`  

---

## Authorization Determination

| Field | Value |
|---|---|
| Verdict | PUBLIC RELEASE AUTHORIZATION APPROVED WITH NOTES |
| Public asset | Screen reader PDF only |
| Upload performed | **YES** |
| Public URL | `https://github.com/noself-bardo/gradient-institution/releases/download/tg-web-pdf-assets/crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| Website patched | **YES** (`data/companion.json` `CL-VOL-IV`) |
| Deploy performed | **NO** (Netlify not wired for TG-WEB-001) |
| Git commit | **YES** (`cbf914c` on `main`) |
| Local preview validation | **PASS** |
| Image gate | CLOSED |

---

## Authorized Public Asset

| Field | Value |
|---|---|
| Filename | `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| SHA-256 | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` |
| Size | 10,782,162 bytes (~10.3 MB) |
| Pages | 48 |
| Steward path | `06_RELEASE_ASSEMBLY/.../public_reader_pdf_v1.0/` |

---

## Steward-Only Assets (Not Public)

| Asset | SHA-256 | Public? |
|---|---|---|
| Print PDF | `ca9e2cae59d067e36bedcbdc996a7b6eb9d7704652a5dbee607f371b617b89ae` | **NO** |
| Frozen snapshot v1.0 | per `CL-IV_RELEASE_SNAPSHOT_CHECKSUMS.md` | **NO** |
| Snapshot zip | `CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_FROZEN_RELEASE.zip` | **NO** |

---

## Status Transition

| From | To | Date |
|---|---|---|
| PUBLIC READER PDF PREPARED — PENDING PUBLIC RELEASE AUTHORIZATION | **PUBLIC RELEASE AUTHORIZATION APPROVED — PENDING PUBLIC ASSET UPLOAD** | 2026-07-11 |
| PUBLIC RELEASE AUTHORIZATION APPROVED — PENDING PUBLIC ASSET UPLOAD | **PUBLIC ASSET UPLOAD COMPLETE — PENDING WEBSITE PATCH** | 2026-07-11 |
| PUBLIC ASSET UPLOAD COMPLETE — PENDING WEBSITE PATCH | **WEB PUBLICATION PATCH COMPLETE — PENDING LOCAL PREVIEW VALIDATION** | 2026-07-11 |
| WEB PUBLICATION PATCH COMPLETE — PENDING LOCAL PREVIEW VALIDATION | **WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY** | 2026-07-11 |
| WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY | **WEB COMMIT COMPLETE — DEPLOY PENDING (NETLIFY SITE NOT WIRED FOR TG-WEB-001)** | 2026-07-11 |

---

## Gate Status

| Gate | State |
|---|---|
| Visual production | LOCKED |
| Archive lock | LOCKED |
| Release snapshot | FROZEN |
| Print-ready authorization | APPROVED WITH NOTES |
| Public reader PDF prep | COMPLETE |
| **Public release authorization** | **APPROVED WITH NOTES** |
| Public asset upload | **COMPLETE** |
| Website patch | **COMPLETE** |
| Local preview validation | **PASS** |
| Commit | **COMPLETE** (`cbf914c`) |
| Deploy | **PENDING / BLOCKED** (Netlify not wired) |
| Image generation | CLOSED |

---

## Accepted Notes

- Public release uses screen PDF, not print PDF
- `companion.json` `CL-VOL-IV` patched with screen filename and public URL
- JPEG screen compression acceptable for browser delivery
- HEAD-probe verified at upload and patch validation
- Commit/push complete; Netlify TG-WEB-001 host not wired (`thegradient.netlify.app` serves Field Atlas)

---

## Next Actions (After Netlify Wiring)

1. Wire Netlify publish directory to `08_platform/tg-web-001` (or CLI deploy)
2. Run live publication verification
3. Optional: add `SRC-CL-PDF-IV` to `sources.json`

**Commit complete (`cbf914c`). Deploy pending. Publication not marked live.**

---

## References

- `CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md`
- `CLIV_WEB_DEPLOY_REGISTER_v1.0.md`
- `CLIV_WEB_PREVIEW_VALIDATION_v1.0.md`
- `CLIV_WEB_PREVIEW_VALIDATION_REGISTER_v1.0.md`
- `CLIV_WEB_PUBLICATION_PATCH_v1.0.md`
- `CLIV_WEB_PUBLICATION_PATCH_DIFF_SUMMARY_v1.0.md`
- `CLIV_PUBLIC_ASSET_UPLOAD_v1.0.md`
- `CLIV_PUBLIC_RELEASE_AUTHORIZATION_v1.0.md`
- `CLIV_PRINT_READY_AUTHORIZATION_RECORD.md`
- `TG-WEB-001_PUBLIC_PDF_STRATEGY.md`
- `data/companion.json` — `CL-VOL-IV` entry
