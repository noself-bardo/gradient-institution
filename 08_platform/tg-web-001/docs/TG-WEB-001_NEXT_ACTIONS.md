# TG-WEB-001 — Next Actions

Status: Active  
Authority: Implementation / Servant Layer  
Base commit: `f714118`  
PDF strategy: [TG-WEB-001_PUBLIC_PDF_STRATEGY.md](TG-WEB-001_PUBLIC_PDF_STRATEGY.md)

## Final Determination

```text
TG-WEB-001 PDF STRATEGY APPROVED WITH NON-BLOCKING GAPS
```

---

## Immediate — Before GitHub Push

| # | Action | Owner | Blocker? |
|---|---|---|---|
| 1 | **Vol I remediation: DEPLOY-ONLY NETLIFY ASSETS** — PDFs untracked from Git; local/Netlify deploy bundle only. Git LFS not used. | Steward + implementer | Done (structure) |
| 2 | Add `08_platform/tg-web-001/.gitattributes` with `*.pdf binary` | Implementer | Recommended |
| 3 | Decide deploy repo: standalone `the-gradient-archive-gateway` vs `gradient-institution` subpath | Steward | Yes — affects Netlify config |
| 4 | Run pre-push QA grep — no `notion.com`, `drive.google` in `data/`, `index.html`, `app.js` | Implementer | Yes |
| 5 | Configure Netlify publish dir → `08_platform/tg-web-001` | Implementer | Yes for deploy |
| 6 | Create Drive folder `TG-WEB-001_ARCHIVE_GATEWAY/` with deploy manifest (PRINT source paths, SHA-256, filenames) | Steward | No |

---

## Priority 2 — Governing PDF Export

Export reader-facing PDFs from Notion/Drive to deploy bundle `assets/pdf/`:

| File | Source |
|---|---|
| `constitution-v0.1.pdf` | The Gradient Constitution v0.1 |
| `founding-white-paper-v0.1.pdf` | Founding White Paper v0.1 |
| `idr-002-relationships.pdf` | IDR-002 |
| `idr-003-implementation.pdf` | IDR-003 |
| `charter-locked-decisions-v0.1.pdf` | Charter locked decisions |

After export: verify HEAD probe returns 200 locally; governing shelf buttons open PDFs.

May deploy to Netlify without committing governing PDFs to Git if files remain under size policy.

---

## Priority 3 — Companion Canon / Translation PDFs

When reader-facing exports exist:

| File | Accession |
|---|---|
| `crisis-liturgies-canon-v1.1.pdf` | CL-CANON-1.1 |
| `crisis-liturgy-translation-doctrine.pdf` | CL-TRN-001 |

Until ready: **READER PDF NEEDED** remains correct UI state.

---

## Priority 4 — Vol I/II Thumbnails (Optional)

If exact six PNGs from original Netlify bundle are found, copy to `assets/img/` per [assets/img/README.md](../assets/img/README.md).

Do not generate, crop, or substitute images.

---

## Deferred — CL-III Companion Shelf Admission

**Do not start until priorities 1–3 are satisfied or explicitly waived by steward.**

CL-III must **not** appear in live `data/companion.json` until this checklist completes.

Admission checklist:

- [ ] Copy `CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf` from `09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0`
- [ ] Verify against snapshot manifest — not `06_RELEASE_ASSEMBLY/...`
- [ ] Place at `assets/pdf/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf`
- [ ] HEAD probe QA passes on deploy
- [ ] Separate commit: add `CL-VOL-III` to `data/companion.json` only after human admission sign-off
- [ ] Update Plate TG-003 copy if needed
- [ ] Do **not** ingest CL-025–CL-036 PNG gallery in same pass unless separately approved

CL-III may be referenced in docs as **approved print release, inactive on live Plate Reader** until this checklist completes.

---

## Live companion status (current)

| Volume | Live shelf | Deploy PDF |
|---|---|---|
| CL-I | Yes | Deploy-only |
| CL-II | Yes | Deploy-only |
| CL-IV | Yes | Deploy-only |
| CL-III | No — documented only | Pending admission |
| CL-V | No — future only | Not admitted |

---

## Future — CL-V Companion Admission

Crisis Liturgies V is expected as a future companion reader asset. Do not add to live companion shelf until the reader-facing PDF is complete, public-safe, and intentionally admitted.

---

## Explicitly Out of Scope

- Rebuild PDFs
- Regenerate images
- Alter canon or prompt packets
- Restore reverted CL-III shelf JSON work from prior session
- Point public UI at Drive paths
- Notion links on public buttons

---

## Disposition

```text
TG-WEB-001 — Baseline Built / Asset Integration Pending
PDF Strategy — APPROVED WITH NON-BLOCKING GAPS
GitHub Push — BLOCKED until large-file remediation (Vol I)
Netlify Deploy — Ready after push remediation + publish config
CL-III Live Shelf — Intentionally inactive
```

---

## Document Index

| Document | Purpose |
|---|---|
| [TG-WEB-001_PUBLIC_PDF_STRATEGY.md](TG-WEB-001_PUBLIC_PDF_STRATEGY.md) | Full PDF distribution strategy |
| [TG-WEB-001_SOURCE_POLICY.md](TG-WEB-001_SOURCE_POLICY.md) | Source eligibility and link rules |
| [CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md](CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md) | CL-III provenance boundary |
| [TG-WEB-001_QA_CHECKLIST.md](TG-WEB-001_QA_CHECKLIST.md) | Pre-deploy QA |
