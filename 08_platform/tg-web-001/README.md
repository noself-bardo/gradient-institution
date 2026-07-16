# The Gradient Archive Gateway

Institutional Asset ID: TG-WEB-001  
Parent Institution: The Gradient  
Authority Layer: Implementation / Servant Layer  
Status: Recovery Protocol v1.0 Locked / Production Redeploy Pending
Canonical Boundary: This site explains The Gradient. It does not define The Gradient.

The Archive Gateway is a public-facing orientation layer for The Gradient institution. It helps readers understand the Constitution, source spine, knowledge architecture, engines, case studies, visual language, and implementation stack without mistaking the interface for the institution.

## Project Metadata

| Field | Value |
|---|---|
| Asset ID | TG-WEB-001 |
| Title | The Gradient Archive Gateway |
| Parent Institution | The Gradient |
| Authority Layer | Implementation / Servant Layer |
| Status | Recovery Protocol v1.0 Locked / Production Redeploy Pending |
| Public Function | Orientation and source navigation |
| Canonical Boundary | Explainer only; governing documents remain authoritative |
| Primary Institutional Home | The Gradient → 10 Implementation |
| Visual Language Home | The Gradient → 11 Visual Language |

## Institutional Placement

```text
The Gradient
→ 10 Implementation
→ TG-WEB-001 — The Gradient Archive Gateway
```

Cross-linked to:

```text
The Gradient
→ 11 Visual Language
→ Interactive HTML Explainer / Archive Gateway
```

## Source of Truth Order

When conflicts arise, use this hierarchy:

1. The Gradient Constitution
2. Locked Charter / IDRs / Specifications
3. The Gradient Operating System
4. Notion institutional records
5. Google Drive durable source files
6. Supabase / Registry records when available
7. GitHub source code
8. Netlify deployment

GitHub stores implementation. GitHub does not govern the institution.

Netlify serves the public site. Netlify does not govern the institution.

## Repository Context

This implementation lives only within the canonical `gradient-institution` repository at `08_platform/tg-web-001/`. Do not extract it into a standalone repository or create a second deployment repository.

## Required Institutional Records

| System | Record | Status |
|---|---|---|
| Notion | TG-WEB-001 — The Gradient Archive Gateway | Created under 10 Implementation |
| Google Drive | TG-WEB-001_ARCHIVE_GATEWAY/ | Pending |
| GitHub | `noself-bardo/gradient-institution` → `08_platform/tg-web-001` | Active / canonical implementation source |
| Netlify | `thegradient.netlify.app` | Existing site / production redeploy pending |
| Supabase Registry | platform_assets entry for TG-WEB-001 | Pending — registry write path not yet active |

## Structure

```text
/
  README.md
  index.html
  styles.css
  app.js
  netlify.toml
  .nojekyll
  /data
    sources.json
    engines.json
    case-studies.json
    glossary.json
    rooms.json
    institutional-metadata.json
  /assets
    /pdf
      (Crisis Liturgies PDFs — pending)
  /docs
    TG-WEB-001_INSTITUTIONAL_RECORD.md
    TG-WEB-001_SOURCE_POLICY.md
    TG-WEB-001_QA_CHECKLIST.md
```

## Branch Naming

```text
main
rebuild/TG-WEB-001-archive-gateway-v0.1
qa/TG-WEB-001-link-and-accessibility-pass
release/TG-WEB-001-public-v0.1
```

## Commit Convention

```text
TG-WEB-001: establish archive gateway metadata
TG-WEB-001: split monolithic explainer into semantic structure
TG-WEB-001: add source registry
```

## Plate Reader (Current PoC)

The active build is a Crisis Liturgies–informed **plate reader** with snap-scroll field atlas layout:

- Plates TG-000 through TG-011 (entry → living practice → sources → companion → diagnosis → response → organs → loop → modules A–F → boundary vows → reader path → institutional record)
- Public reader PDFs: **external public reader asset host** (GitHub Releases preferred; Supabase Storage fallback) — not Netlify PDF upload
- Live companion shelf entries: CL-I, CL-II, and CL-IV (hosted on GitHub Releases; CL Canon and Translation Doctrine are unpublished and render as plain text "NOT YET PUBLISHED" with no button)
- CL-III is documented only and remains outside the live companion manifest until separately ratified; CL-V is reserved as future only
- `assets/pdf/` is optional local preview cache only — not the public deployment source
- Data-driven shelves and modules in `data/*.json`
- Source lineage archived from Desktop `gradient explainer html` → [docs/source-archive/](docs/source-archive/README.md)

## Asset Checklist Before Deploy

1. Verify the CL-I / CL-II / CL-IV GitHub Release URLs during build or release QC; do not perform browser-side cross-origin HEAD probes
2. Keep `data/companion.json` as the only public companion-shelf manifest
3. Deploy the existing Netlify site from `main` with publish directory `08_platform/tg-web-001` (no PDF upload)
4. Run live link, mobile, accessibility, and leakage checks before declaring publication complete
5. See [assets/pdf/README.md](assets/pdf/README.md) for local cache notes only

## Netlify Deployment (thegradient.netlify.app)

Netlify hosts the **explainer site only**. Do not upload large print PDFs through Netlify manual deploy.

**Publish directory:** `08_platform/tg-web-001`

Netlify is public distribution for the gateway UI — not the PDF asset host, not the institution, not the source of truth.

## Locked Recovery Authority

The ratified operational recovery protocol is recorded at [`../TG-WEB-001_RECOVERY_PROTOCOL_v1.0.md`](../TG-WEB-001_RECOVERY_PROTOCOL_v1.0.md). It governs current TG-WEB implementation and deployment when older operational records conflict. Historical records remain evidence of prior work, not executable instructions.

## Documentation

- [Institutional Record](docs/TG-WEB-001_INSTITUTIONAL_RECORD.md)
- [Source Policy](docs/TG-WEB-001_SOURCE_POLICY.md)
- [CL-III Release Assembly Readiness Record](docs/CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md)
- [CL-III Companion Shelf Entry Record](docs/CLIII_COMPANION_SHELF_ENTRY_RECORD.md)
- [Public PDF Strategy](docs/TG-WEB-001_PUBLIC_PDF_STRATEGY.md)
- [Next Actions](docs/TG-WEB-001_NEXT_ACTIONS.md)
- [QA Checklist](docs/TG-WEB-001_QA_CHECKLIST.md)
