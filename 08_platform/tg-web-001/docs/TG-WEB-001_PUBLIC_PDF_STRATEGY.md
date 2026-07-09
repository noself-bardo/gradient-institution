# TG-WEB-001 — Public Web PDF Strategy

Status: Strategy pivoted (TG-WEB-004)  
Authority: Implementation / Servant Layer — not canonical  
Asset: TG-WEB-001 — The Gradient Archive Gateway  
Date: 2026-07-09  
Prior commits: `7627766` (strategy lock) · `747fd0a` / `c9b0572` (Netlify deploy-only attempt) · `7760026` (CL-IV companion)

## Final Determination

```text
TG-WEB-001 PDF STRATEGY APPROVED WITH NON-BLOCKING GAPS
PUBLIC READER ASSET HOST: GitHub Releases (preferred) / Supabase Storage (fallback)
NETLIFY: site host only — not PDF host
```

---

## 1. Pivot reason (TG-WEB-004)

Netlify manual deploy does not allow or fails on large Crisis Liturgies print PDFs. Therefore the prior **deploy-only Netlify assets** model cannot be used for public reader PDFs.

| Do not | Do |
|---|---|
| Use Git LFS | Host PDFs on GitHub Releases (preferred) |
| Commit PDFs to Git | Or Supabase Storage public bucket (fallback) |
| Upload PDFs via Netlify manual deploy | Keep Netlify as HTML/CSS/JS host only |
| Point public hrefs at Drive / snapshots | HEAD-probe public reader URLs only |

---

## 2. Policy language

Public reader PDFs are served from a **public object/release asset URL**. Netlify hosts the explainer site only. Large print PDFs are not committed to Git and are not uploaded through Netlify manual deploy. The UI may link only to reader-facing public PDF URLs and must HEAD-probe them before enabling OPEN PDF.

---

## 3. Layer roles

| Layer | Role |
|---|---|
| **Netlify** | Public site host (HTML / CSS / JS / JSON) |
| **Public reader asset host** | GitHub Releases (preferred) or Supabase Storage public bucket |
| **Git** | Code, data, docs, asset-mount metadata (`.gitkeep`, README) — never `*.pdf` |
| **`assets/pdf/`** | Optional **local preview cache** only — not the public deployment source |
| **Drive / release snapshots** | Canonical steward-copy sources — never public hrefs |

---

## 4. Preferred public URL pattern

```text
https://github.com/<OWNER>/<REPO>/releases/download/tg-web-pdf-assets/<FILENAME>.pdf
```

Release tag (recommended): `tg-web-pdf-assets`

Intended filenames:

| Accession | Filename |
|---|---|
| CL-VOL-I | `CRISIS_LITURGIES_COMPLETE_v1.0_PRINT.pdf` |
| CL-VOL-II | `CRISIS_LITURGIES_II_PRIVATE_INSTRUMENTS_v1.0_PRINT.pdf` |
| CL-VOL-IV | `CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_PRINT.pdf` |

Until URLs exist: companion `href` is empty (`""`) and `status` is `Reader PDF needed`.

When hosted: set `href` to the public URL and `status` to `Reader PDF hosted`.

---

## 5. UI behavior

1. If `href` is empty → **READER PDF NEEDED** (no network call required)
2. If `href` exists → HEAD-probe
3. HEAD 200 → **OPEN PDF**
4. HEAD fail / 404 → **READER PDF NEEDED**
5. No fallback to Drive, Notion, snapshots, trackers, release status pages, or production handoff pages

---

## 6. Companion series status

| Volume | Live shelf | Public PDF host | Notes |
|---|---|---|---|
| CL-I | Yes (intended) | Pending GitHub Releases / Supabase | Live companion once hosted |
| CL-II | Yes (intended) | Pending | Live companion once hosted |
| CL-IV | Yes (intended) | Pending | Live companion once hosted |
| CL-III | **No** | — | Documented only until separately admitted |
| CL-V | **No** | — | Future only |

Crisis Liturgies remain **companion, not authority**.

---

## 7. PDF class taxonomy (unchanged roles)

| Class | Public host | Authority |
|---|---|---|
| Companion print release (CL-I/II/IV) | External public reader asset host | Companion |
| Governing exports | External host when ready | Governing |
| Companion canon / translation | External host when ready | Companion |
| Screen / assembly / prep | Never public | Provenance only |

---

## 8. Before GitHub push / Netlify site deploy

1. Netlify publish dir = `08_platform/tg-web-001` (**site only** — no PDF upload requirement)
2. Create GitHub Release `tg-web-pdf-assets` (or Supabase public bucket) with CL-I / CL-II / CL-IV PRINT PDFs
3. Fill companion `href` values with public URLs; set status to `Reader PDF hosted`
4. HEAD-probe QA on each URL
5. Confirm no `*.pdf` tracked in Git
6. Confirm no public hrefs to Drive / Notion / trackers

---

## 9. Related documents

- [TG-WEB-001_NEXT_ACTIONS.md](TG-WEB-001_NEXT_ACTIONS.md)
- [TG-WEB-001_SOURCE_POLICY.md](TG-WEB-001_SOURCE_POLICY.md)
- [TG-WEB-001_INSTITUTIONAL_RECORD.md](TG-WEB-001_INSTITUTIONAL_RECORD.md)
- [assets/pdf/README.md](../assets/pdf/README.md)
