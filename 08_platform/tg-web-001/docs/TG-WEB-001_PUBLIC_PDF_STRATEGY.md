# TG-WEB-001 — Public Web PDF Strategy

Status: Strategy pass complete  
Authority: Implementation / Servant Layer — not canonical  
Asset: TG-WEB-001 — The Gradient Archive Gateway  
Date: 2026-07-08  
Base commit: `f714118`

## Final Determination

```text
TG-WEB-001 PDF STRATEGY APPROVED WITH NON-BLOCKING GAPS
```

The public PDF distribution model is approved. Known gaps (governing PDF export, canon/translation exports, GitHub large-file remediation, CL-III shelf admission) are tracked in [TG-WEB-001_NEXT_ACTIONS.md](TG-WEB-001_NEXT_ACTIONS.md) and do not invalidate the strategy itself.

---

## 1. Purpose

Resolve how TG-WEB-001 serves public-facing PDFs **before** GitHub push or CL-III companion shelf admission — without linking to Notion, Google Drive login pages, internal trackers, or local Drive paths in public UI.

---

## 2. Governing Principles

1. **Public UI opens relative web paths only** — `assets/pdf/<filename>.pdf` on the deployed Netlify origin.
2. **Drive is canonical storage, not public href target** — Drive paths may appear in docs and manifests; never in `href` attributes or JSON `url` fields exposed to readers.
3. **Deploy bundle ≠ Git source of truth** — Git holds code, data, and small docs. Large print PDFs are **deploy assets**, not institutional canon.
4. **HEAD probe honesty** — Missing deploy assets show **READER PDF NEEDED**; no dead links, no login redirects.
5. **Companion ≠ governing** — Crisis Liturgies print PDFs are companion sources. Constitution, Charter, IDRs, White Paper are governing exports.
6. **Print ≠ screen** — Only **PRINT** PDFs approved for public companion shelves. Screen PDFs from archived HTML Drive IDs are deprecated.
7. **CL-III documented, not live** — Approved print release may be referenced in docs; not admitted to live Plate Reader until intentional companion shelf pass.

---

## 3. Where Public-Facing PDFs Should Live

### 3.1 Public web layer (what readers open)

| Layer | Location | Role |
|---|---|---|
| **Deploy publish root** | Netlify publish dir: `08_platform/tg-web-001/` | Serves HTML, CSS, JS, data |
| **Public PDF directory** | `assets/pdf/` within publish root | All `OPEN DOCUMENT (PDF)` targets |
| **Public image directory** | `assets/img/` within publish root | Companion thumbnails only (Vol I/II); not CL-III gallery |

Public URL pattern:

```text
https://thegradient.netlify.app/assets/pdf/<filename>.pdf
```

Data model (`data/companion.json`, `data/governing.json`, etc.) stores **relative paths** only:

```text
assets/pdf/CRISIS_LITURGIES_COMPLETE_v1.0_PRINT.pdf
```

### 3.2 Canonical institutional storage (not public links)

| Layer | Location | Role |
|---|---|---|
| **Drive print exports** | `09_RELEASES/.../04_Print_Exports/` (Vol I/II) | Historical release exports |
| **Drive output QC** | `07_OUTPUT_QC/CRISIS_LITURGIES/...` (CL-III print PDF evidence) | Approved print artifact |
| **Drive release snapshots** | `09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0` | CL-III frozen snapshot (admission source) |
| **Drive archive** | `08_ARCHIVE/CRISIS_LITURGIES/...` | Long-term archive lock state |
| **Future gateway folder** | `TG-WEB-001_ARCHIVE_GATEWAY/` on Drive | Steward-approved web deploy manifest + copies |

### 3.3 Git repository (implementation only)

| In Git | Out of Git (deploy-only) |
|---|---|
| `index.html`, `styles.css`, `app.js` | Large print PDFs (preferred) |
| `data/*.json` with relative `pdf` paths | Full CL-III print PDF until deploy strategy executed |
| `docs/*` | PNG artifact grids until found |
| Small governing PDFs (<50 MB each) when exported | Vol I print PDF if Git LFS not used |

---

## 4. Distribution Model — Approved Approach

### Model: **Deploy-Bundle Relative PDFs (Hybrid Git)**

```text
Drive canonical PRINT export
        ↓  (steward copy manifest — not Cursor auto-copy)
08_platform/tg-web-001/assets/pdf/   ← Netlify publish directory
        ↓
Relative href in Plate Reader data
        ↓
Reader opens PDF on same origin (new tab)
```

| Method | Approved? | Use when |
|---|---|---|
| Relative paths in `assets/pdf/` on Netlify | **Yes — primary** | All public PDF buttons |
| Committed to Git | **Conditional** | Governing PDFs if each file <100 MB; Vol I/II only via Git LFS or remove from Git |
| External URL (Drive, Notion) | **No** | Never for public buttons |
| CDN separate from Netlify | **Future option** | If print corpus exceeds Netlify/git practical limits |
| Excluded until deploy | **Yes** | Missing files → READER PDF NEEDED |

**Do not** point public UI at local Drive paths (`C:\Users\steve\My Drive\...`) or `drive.google.com` links.

---

## 5. PDF Class Taxonomy

| Class | Examples | Authority | Public-safe when | Typical size |
|---|---|---|---|---|
| **Governing print export** | Constitution, White Paper, IDRs, Charter | Governing | Steward exports reader PDF; file present at deploy | Small–medium |
| **Companion print release** | CL Vol I, II, III PRINT PDFs | Companion | PRINT approved; companion boundary labeled | Large |
| **Companion canon / translation** | CL Canon v1.1, Translation Doctrine | Companion governance / doctrine | Reader-facing PDF export complete | Small–medium |
| **Screen / prep / assembly** | Screen PDFs, release assembly folders | Provenance only | **Never public** | — |

Approved print PDFs differ from governing PDFs in **role label and shelf**, not file format. Both use the same relative-path deploy pattern.

---

## 6. Current Asset Inventory & Public Safety

### 6.1 Crisis Liturgies Vol I / II (live companion shelf)

| File | Deploy path | In Git (5d91582) | Size | Public-safe? |
|---|---|---|---|---|
| `CRISIS_LITURGIES_COMPLETE_v1.0_PRINT.pdf` | `assets/pdf/...` | Yes | ~135 MB | **Yes — companion PRINT** |
| `CRISIS_LITURGIES_II_PRIVATE_INSTRUMENTS_v1.0_PRINT.pdf` | `assets/pdf/...` | Yes | ~70 MB | **Yes — companion PRINT** |

PRINT Drive IDs (manifest reference only — not public links):

- Vol I: `1BWkZDG1945DTQ15fTS4414NEJZrURevJ`
- Vol II: `1jQOjrhLlz2t_eEl-fM7JiRKN72yPAseZ`

Vol I/II are **public-safe as companion sources** when served from Netlify `assets/pdf/`. They must remain labeled companion, not governing.

### 6.2 Governing PDFs (governing shelf — all pending)

| File | Status | Public-safe? |
|---|---|---|
| `constitution-v0.1.pdf` | Not exported to deploy dir | Pending export |
| `founding-white-paper-v0.1.pdf` | Not exported | Pending export |
| `idr-002-relationships.pdf` | Not exported | Pending export |
| `idr-003-implementation.pdf` | Not exported | Pending export |
| `charter-locked-decisions-v0.1.pdf` | Not exported | Pending export |

UI correctly shows **READER PDF NEEDED** via HEAD probe until files are placed.

### 6.3 Companion canon / translation (pending)

| File | Status |
|---|---|
| `crisis-liturgies-canon-v1.1.pdf` | Pending reader-facing export |
| `crisis-liturgy-translation-doctrine.pdf` | Pending reader-facing export |

### 6.4 Crisis Liturgies III (documented only — not on live shelf)

| Item | State |
|---|---|
| Print PDF | **APPROVED** (archive lock, indexing closed, snapshot complete) |
| Expected filename | `CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf` |
| Canonical admission source | `09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0` |
| Evidence path (tools reference) | `07_OUTPUT_QC/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS/` |
| Live Plate Reader | **Not admitted** |
| Public-safe as companion PRINT? | **Yes — when copied to deploy bundle from snapshot** |
| May be referenced in docs now? | **Yes — as approved print release, inactive on live reader** |

CL-III may be documented as an approved print release **without** companion shelf JSON changes or live buttons until intentional admission pass.

---

## 7. How Drive Paths Appear Safely

| Context | Drive path allowed? |
|---|---|
| `docs/*.md` manifests | Yes — provenance reference |
| `data/*.json` `sourceNote` field | Yes — non-linking metadata |
| `data/*.json` `pdf` or `url` field | **No — relative web path only** |
| HTML `href` | **No Drive, No Notion** |
| Public-visible plate copy | Describe “local reader PDF” not Drive location |

---

## 8. File Size & Performance Risks

| Risk | Detail | Mitigation |
|---|---|---|
| **Vol I ~135 MB** | Slow first open on mobile; Netlify bandwidth | Accept for PoC; consider compressed reader edition later (separate approval) |
| **Combined CL I+II ~205 MB** | Large Netlify deploy | Deploy bundle acceptable; monitor Netlify asset limits |
| **CL-III print PDF** | Likely large (48 plates) | Copy to deploy at admission; do not commit to Git without LFS |
| **GitHub 100 MB file limit** | Vol I exceeds limit | **Must remediate before GitHub push** — Git LFS, or remove PDFs from Git and deploy via Netlify-only asset upload |
| **Repo clone size** | Institution repo + 205 MB PDFs | Prefer standalone `the-gradient-archive-gateway` repo for web-only deploy |
| **HEAD probe on large files** | Netlify returns 200 HEAD | Acceptable; no full download until click |

---

## 9. GitHub & Deploy Risks

| Risk | Severity | Before push |
|---|---|---|
| GitHub rejects Vol I (>100 MB) | **High** | Git LFS migration OR remove PDFs from Git history and use deploy-only assets |
| Pushing institution repo with web PDFs | Medium | Consider extracting TG-WEB-001 to standalone repo |
| Netlify publish dir misconfigured | Medium | Confirm `08_platform/tg-web-001` not repo root |
| Accidental Drive URL in data | High | QA grep: no `notion.com`, `drive.google` in `data/`, `index.html`, `app.js` |
| `.gitattributes` missing for PDF | Medium | Add `*.pdf binary` under tg-web-001 to prevent CRLF corruption |
| Public implies canon | High | Footer + boundary banner remain mandatory |

---

## 10. Plate Reader Data Model (unchanged this pass)

- `data/companion.json` — `pdf` relative path + metadata; Vol I/II only on live shelf
- `data/governing.json` — governing exports; all pending at deploy
- `app.js` — HEAD probe → link or **READER PDF NEEDED**
- No CL-III entry in live data (per admission gate)

---

## 11. Before GitHub Push

Required:

1. **Remediate large PDF Git tracking** — LFS or remove Vol I/II from Git; document deploy copy manifest
2. **Confirm public QA** — no Notion/Drive in live UI; boundary footer present
3. **Decide repo target** — `gradient-institution` subpath vs standalone `the-gradient-archive-gateway`
4. **Export governing PDFs** to `assets/pdf/` on deploy machine (may omit from Git if large)
5. **Create Drive folder** `TG-WEB-001_ARCHIVE_GATEWAY/` with deploy manifest listing PRINT sources
6. **Netlify config** — publish dir, cache headers for PDFs (optional `Cache-Control` add later)

Optional before push:

- Export canon / translation companion PDFs
- Vol I/II thumbnails in `assets/img/`

Not required before push:

- CL-III shelf admission
- CL-III PDF in deploy bundle
- Governing PDFs in Git (deploy-only acceptable)

---

## 12. Before CL-III Companion Shelf Admission

Required:

1. This strategy approved (done)
2. Copy `CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf` from **frozen release snapshot** — not release assembly folder
3. Verify PRINT QC / snapshot manifest matches filename
4. Place at `assets/pdf/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf`
5. Human admission record — update docs, then `data/companion.json` in separate commit
6. HEAD probe QA on deploy
7. Confirm companion boundary copy on Plate TG-003

Not required for admission:

- CL-025–CL-036 PNG gallery ingest
- Individual artifact routes
- Rebuild PDF or regenerate images

---

## 13. What This Pass Did Not Do

- No shelf JSON changes
- No PDF copies
- No live reader modifications
- No routes
- No CL-III ingest
- No artwork or canon changes

---

## 14. Related Documents

- [TG-WEB-001_SOURCE_POLICY.md](TG-WEB-001_SOURCE_POLICY.md)
- [TG-WEB-001_INSTITUTIONAL_RECORD.md](TG-WEB-001_INSTITUTIONAL_RECORD.md)
- [CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md](CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md)
- [TG-WEB-001_NEXT_ACTIONS.md](TG-WEB-001_NEXT_ACTIONS.md)
- [assets/pdf/README.md](../assets/pdf/README.md)
