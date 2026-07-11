# CL-IV Public Asset Upload v1.0

**Collection:** Crisis Liturgies IV — Depressive Infrastructure / Domestic Collapse Cycle  
**Upload date:** 2026-07-11  
**Review type:** Public asset upload gate only — no website patch, no deploy  
**Prior gate:** Public release authorization APPROVED WITH NOTES  

---

## Verdict

# PUBLIC ASSET UPLOAD PASS

**Authorized status:** PUBLIC ASSET UPLOAD COMPLETE — PENDING WEBSITE PATCH

The authorized screen reader PDF is uploaded to the approved public asset channel. Website patch, deploy, and publication-live marking remain blocked until a separate patch step completes.

---

## Uploaded Asset

| Field | Value |
|---|---|
| Filename | `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| Steward source | `06_RELEASE_ASSEMBLY/CRISIS_LITURGIES/CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE/public_reader_pdf_v1.0/` |
| Upload channel | GitHub Releases |
| Repository | `noself-bardo/gradient-institution` |
| Release tag | `tg-web-pdf-assets` |
| Release title | TG-WEB Public PDF Assets |
| Public URL | `https://github.com/noself-bardo/gradient-institution/releases/download/tg-web-pdf-assets/crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |
| Release page | `https://github.com/noself-bardo/gradient-institution/releases/tag/tg-web-pdf-assets` |

---

## Upload Verification Checklist (6 / 6)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Public URL captured | **PASS** | GitHub Releases download URL recorded above |
| 2 | URL reachable (HEAD) | **PASS** | HTTP 200 |
| 3 | Asset downloaded / inspected | **PASS** | Full file downloaded from public URL |
| 4 | Uploaded size plausible | **PASS** | 10,782,162 bytes (~10.3 MB); matches steward source |
| 5 | Uploaded SHA-256 matches authorized hash | **PASS** | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` |
| 6 | Filename unchanged | **PASS** | `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` |

---

## Integrity Verification

| Asset | SHA-256 | Size (bytes) | Match |
|---|---|---|---|
| Steward source (pre-upload) | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` | 10,782,162 | **YES** |
| Public download (post-upload) | `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe` | 10,782,162 | **YES** |

---

## Upload Scope Compliance

| Rule | Result |
|---|---|
| Screen PDF only uploaded | **PASS** |
| Print PDF not uploaded | **PASS** |
| Frozen snapshot not uploaded | **PASS** |
| Snapshot zip not uploaded | **PASS** |
| Archive records not uploaded | **PASS** |
| Checksum manifests not uploaded | **PASS** |
| Frozen snapshot not modified | **PASS** |
| Screen PDF not modified | **PASS** |
| Website not patched | **PASS** (deferred) |
| Deploy not performed | **PASS** (deferred) |
| Publication not marked live | **PASS** (deferred) |
| `companion.json` not patched | **PASS** (deferred) |

---

## Release Asset Inventory (Post-Upload)

| Asset | Collection |
|---|---|
| `crisis-liturgies-vol-i-v1.0-screen.pdf` | CL-I |
| `crisis-liturgies-vol-ii-private-instruments-v1.0-screen.pdf` | CL-II |
| `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf` | **CL-IV** (this upload) |

---

## Status Transition

| From | To | Date |
|---|---|---|
| PUBLIC RELEASE AUTHORIZATION APPROVED — PENDING PUBLIC ASSET UPLOAD | **PUBLIC ASSET UPLOAD COMPLETE — PENDING WEBSITE PATCH** | 2026-07-11 |

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
| **Public asset upload** | **COMPLETE** |
| Website patch | **PENDING** |
| Deploy | **PENDING** |
| Image generation | CLOSED |

---

## Next Actions (After Website Patch Authorization)

1. Update `companion.json` `href` for `CL-VOL-IV` to public URL above
2. Update `companion.json` `status` to `Reader PDF hosted` after HEAD-probe confirmation
3. Update `hostNote` to reference screen filename (not print filename)
4. Optional: add `SRC-CL-PDF-IV` to `sources.json`
5. Deploy site (Netlify HTML/CSS/JS only)

**None of the above performed in this upload gate.**

---

## References

- `CLIV_PUBLIC_RELEASE_RECORD.md`
- `CLIV_PUBLIC_RELEASE_AUTHORIZATION_v1.0.md`
- `CLIV_PRINT_READY_AUTHORIZATION_RECORD.md`
- `TG-WEB-001_PUBLIC_PDF_STRATEGY.md`
- `data/companion.json` — `CL-VOL-IV` entry (not yet patched)
