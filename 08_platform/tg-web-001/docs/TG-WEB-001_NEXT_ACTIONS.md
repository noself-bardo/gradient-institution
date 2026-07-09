# TG-WEB-001 — Next Actions

Status: Active  
Authority: Implementation / Servant Layer  
PDF strategy: [TG-WEB-001_PUBLIC_PDF_STRATEGY.md](TG-WEB-001_PUBLIC_PDF_STRATEGY.md)

## Final Determination

```text
TG-WEB-001 PDF STRATEGY APPROVED WITH NON-BLOCKING GAPS
PUBLIC READER ASSET HOST — GitHub Releases preferred / Supabase Storage fallback
NETLIFY — site host only (PDF upload abandoned)
```

---

## Immediate — Public reader asset host

| # | Action | Owner | Status |
|---|---|---|---|
| 1 | **Pivot away from Netlify PDF hosting** — Netlify manual deploy fails on large print PDFs | Steward + implementer | Done (docs + companion placeholders) |
| 2 | Create GitHub Release tag `tg-web-pdf-assets` with CL-I / CL-II / CL-IV PRINT PDFs | Steward | **Pending** |
| 3 | Or create Supabase Storage public bucket as fallback host | Steward | Optional fallback |
| 4 | Fill `data/companion.json` `href` with public URLs; set status to `Reader PDF hosted` | Implementer | Blocked on #2 |
| 5 | HEAD-probe QA on each public URL | Implementer | After #4 |
| 6 | Deploy Netlify **site only** from `08_platform/tg-web-001` (no PDF upload) | Implementer | Ready anytime |
| 7 | Confirm no `*.pdf` in Git; no Drive/Notion public hrefs | Implementer | Ongoing |

Do **not** use Git LFS. Do **not** commit PDFs. Do **not** retry Netlify PDF upload.

---

## Priority 2 — Governing PDF Export

Export reader-facing PDFs, then host on the same public reader asset host (not Netlify):

| File | Source |
|---|---|
| `constitution-v0.1.pdf` | The Gradient Constitution v0.1 |
| `founding-white-paper-v0.1.pdf` | Founding White Paper v0.1 |
| `idr-002-relationships.pdf` | IDR-002 |
| `idr-003-implementation.pdf` | IDR-003 |
| `charter-locked-decisions-v0.1.pdf` | Charter locked decisions |

Until hosted: **READER PDF NEEDED** remains correct UI state.

---

## Priority 3 — Companion Canon / Translation PDFs

| File | Accession |
|---|---|
| `crisis-liturgies-canon-v1.1.pdf` | CL-CANON-1.1 |
| `crisis-liturgy-translation-doctrine.pdf` | CL-TRN-001 |

Host externally when reader-facing exports exist.

---

## Deferred — CL-III Companion Shelf Admission

CL-III must **not** appear in live `data/companion.json` until separately admitted.

Admission still requires: approved print PDF on public reader asset host + human sign-off. Source of truth remains frozen release snapshot / archive lock — not release assembly.

---

## Live companion status (current)

| Volume | Live shelf | Public PDF host |
|---|---|---|
| CL-I | Yes (intended) | Pending — `href` empty → READER PDF NEEDED |
| CL-II | Yes (intended) | Pending |
| CL-IV | Yes (intended) | Pending |
| CL-III | No — documented only | — |
| CL-V | No — future only | — |

---

## Future — CL-V Companion Admission

Crisis Liturgies V is expected as a future companion reader asset. Do not add to live companion shelf until the reader-facing PDF is complete, public-safe, and intentionally admitted.

---

## Disposition

```text
TG-WEB-001 — Baseline Built / Asset Integration Pending
PDF Strategy — external public reader asset host
Netlify — site host only
GitHub Releases — preferred PDF host (URLs pending)
CL-III — documented only
CL-V — future only
```
