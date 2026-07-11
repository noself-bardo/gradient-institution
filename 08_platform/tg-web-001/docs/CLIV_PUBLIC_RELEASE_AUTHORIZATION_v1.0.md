# CL-IV Public Release Authorization v1.0

**Collection:** Crisis Liturgies IV — Depressive Infrastructure / Domestic Collapse Cycle  
**Issue range:** CL-IV-001 through CL-IV-012  
**Review date:** 2026-07-11  
**Review type:** Public release decision gate only — no upload, no deploy, no website patch  
**Prior gates:** Print-ready APPROVED WITH NOTES · Public reader prep PASS WITH NOTES  

---

## Verdict

# PUBLIC RELEASE AUTHORIZATION APPROVED WITH NOTES

**Authorized status:** PUBLIC RELEASE AUTHORIZATION APPROVED — PENDING PUBLIC ASSET UPLOAD

Public release is authorized for the **screen reader PDF only**. Upload, website patch, and deploy remain blocked until a separate upload step completes.

---

## Authorized Public Asset

| Field | Value |
|---|---|
| File | `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| Steward path | `06_RELEASE_ASSEMBLY/CRISIS_LITURGIES/CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE/public_reader_pdf_v1.0/` |
| SHA-256 | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` |
| Size | 10,782,162 bytes (~10.3 MB) |
| Pages | 48 |

**Not authorized for public release:** print PDF, frozen snapshot, snapshot zip, internal QC records.

---

## Authorization Checklist (20 / 20)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Public reader PDF exists | **PASS** | Verified on steward Drive |
| 2 | Public reader PDF passed QC | **PASS** | `CL-IV_PUBLIC_READER_PDF_QC_v1.0.md` — PASS WITH NOTES |
| 3 | Reader PDF has 48 pages | **PASS** | Independent verification |
| 4 | Reader PDF is browser-suitable | **PASS** | ~10.3 MB; screen-optimized |
| 5 | No internal Drive paths exposed | **PASS** | Binary scan clean |
| 6 | No source folder paths exposed | **PASS** | Binary scan clean |
| 7 | No checksum manifests embedded | **PASS** | No embedded records |
| 8 | No archive-lock records embedded | **PASS** | No embedded records |
| 9 | No operational metadata exposed | **PASS** | Canon/safety + metadata scan |
| 10 | No personal names exposed | **PASS** | Inherited from print/public reader QC chain |
| 11 | No child depiction | **PASS** | Inherited from print/public reader QC chain |
| 12 | No partner depiction | **PASS** | Inherited from print/public reader QC chain |
| 13 | No photo drift | **PASS** | Inherited from visual grammar QC |
| 14 | No slogan drift | **PASS** | Inherited from canon/safety QC |
| 15 | Print-ready authorization exists | **PASS** | `CLIV_PRINT_READY_AUTHORIZATION_RECORD.md` |
| 16 | Frozen v1.0 snapshot unchanged | **PASS** | Snapshot intact; print PDF checksum verified |
| 17 | Website/public metadata ready to be created | **PASS WITH NOTE** | `companion.json` entry exists; `href` + screen filename update pending upload |
| 18 | Public asset strategy identified | **PASS** | GitHub Releases `tg-web-pdf-assets` (preferred) per `TG-WEB-001_PUBLIC_PDF_STRATEGY.md` |
| 19 | Public release does not expose snapshot zip | **PASS** | Screen PDF only; zip not in release scope |
| 20 | Public release does not expose print PDF | **PASS** | Print PDF steward-only; screen derivative authorized |

---

## Integrity Verification (This Review)

| Asset | SHA-256 | Match |
|---|---|---|
| Public reader PDF | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` | **YES** |
| Print PDF (unchanged) | `ca9e2cae59d067e36bedcbdc996a7b6eb9d7704652a5dbee607f371b617b89ae` | **YES** |

---

## Accepted Notes (Non-Blocking)

1. **Screen PDF is the public asset** — not `CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_PRINT.pdf`. Print PDF remains steward/print authority only.
2. **JPEG screen compression** — derivative tonal delta documented; acceptable for public browser reading.
3. **Companion metadata update pending** — `companion.json` `hostNote` currently references print filename; update to screen filename at upload/patch step.
4. **Upload not performed** — authorization does not constitute upload or deploy.
5. **Image gate** — remains CLOSED.

---

## Public Asset Strategy (Identified, Not Executed)

| Step | Target | Status |
|---|---|---|
| Host | GitHub Releases tag `tg-web-pdf-assets` (preferred) or Supabase Storage | Pending |
| Upload file | `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` | Pending |
| Companion `href` | Public release URL after upload | Pending |
| Companion `status` | `Reader PDF hosted` after HEAD-probe PASS | Pending |
| `sources.json` | Optional `SRC-CL-PDF-IV` registry entry | Pending |

---

## Explicitly Not Authorized (This Gate)

| Action | Status |
|---|---|
| Upload public asset | NOT PERFORMED |
| Patch website / `companion.json` | NOT PERFORMED |
| Deploy | NOT PERFORMED |
| Expose print PDF publicly | NOT AUTHORIZED |
| Expose frozen snapshot / zip | NOT AUTHORIZED |
| Modify frozen snapshot | NOT AUTHORIZED |
| Modify print or screen PDF | NOT AUTHORIZED |
| Image generation | NOT AUTHORIZED |

---

## Authorization Chain

| Gate | Status |
|---|---|
| Frozen snapshot | COMPLETE |
| Archive lock | APPROVED |
| Print-ready authorization | APPROVED WITH NOTES |
| Public reader PDF prep | PASS WITH NOTES |
| **Public release authorization** | **APPROVED WITH NOTES** |
| Public asset upload | **PENDING** |
| Website patch | **PENDING** |
| Deploy | **PENDING** |

---

## References

- `CLIV_PUBLIC_RELEASE_RECORD.md`
- `CLIV_PRINT_READY_AUTHORIZATION_RECORD.md`
- `CL-IV_PUBLIC_READER_PDF_PREP_v1.0.md` (Drive)
- `CL-IV_PUBLIC_READER_PDF_QC_v1.0.md` (Drive)
- `TG-WEB-001_PUBLIC_PDF_STRATEGY.md`
- `TG-WEB-001_SOURCE_POLICY.md`
