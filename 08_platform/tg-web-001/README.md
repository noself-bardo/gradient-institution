# The Gradient Archive Gateway

Institutional Asset ID: TG-WEB-001  
Parent Institution: The Gradient  
Authority Layer: Implementation / Servant Layer  
Status: Baseline Built / Asset Integration Pending  
Canonical Boundary: This site explains The Gradient. It does not define The Gradient.

The Archive Gateway is a public-facing orientation layer for The Gradient institution. It helps readers understand the Constitution, source spine, knowledge architecture, engines, case studies, visual language, and implementation stack without mistaking the interface for the institution.

## Project Metadata

| Field | Value |
|---|---|
| Asset ID | TG-WEB-001 |
| Title | The Gradient Archive Gateway |
| Parent Institution | The Gradient |
| Authority Layer | Implementation / Servant Layer |
| Status | Baseline Built / Asset Integration Pending |
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

This implementation lives within the `gradient-institution` repository at `08_platform/tg-web-001/`. The preferred standalone repository name is `the-gradient-archive-gateway` when extracted for Netlify deployment.

## Required Institutional Records

| System | Record | Status |
|---|---|---|
| Notion | TG-WEB-001 — The Gradient Archive Gateway | Created under 10 Implementation |
| Google Drive | TG-WEB-001_ARCHIVE_GATEWAY/ | Pending |
| GitHub | the-gradient-archive-gateway (preferred) / this path | Active |
| Netlify | thegradient.netlify.app or future canonical URL | Pending deployment |
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
- All sources open as **local PDFs** in `assets/pdf/` — no Notion dependency
- Companion artifact thumbnails in `assets/img/`
- Data-driven shelves and modules in `data/*.json`
- Source lineage archived from Desktop `gradient explainer html` → [docs/source-archive/](docs/source-archive/README.md)

## Asset Checklist Before Deploy

Copy PDFs and PNGs per:

- [assets/pdf/README.md](assets/pdf/README.md)
- [assets/img/README.md](assets/img/README.md)

## Local Development

```bash
cd 08_platform/tg-web-001
python -m http.server 8080
```

Open `http://localhost:8080`. No build step required.

## Netlify Deployment (thegradient.netlify.app)

**Option A — from this repo (quick PoC):**

1. Connect `gradient-institution` to Netlify
2. Set **Publish directory** to `08_platform/tg-web-001`
3. Deploy

**Option B — standalone repo (preferred long-term):**

Extract `tg-web-001/` to `the-gradient-archive-gateway` and deploy from repo root.

```bash
# If netlify CLI is installed:
cd 08_platform/tg-web-001
netlify deploy --prod --dir .
```

Netlify is public distribution only — gateway, not institution, not source of truth.

## Documentation

- [Institutional Record](docs/TG-WEB-001_INSTITUTIONAL_RECORD.md)
- [Source Policy](docs/TG-WEB-001_SOURCE_POLICY.md)
- [CL-III Release Assembly Readiness Record](docs/CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md)
- [QA Checklist](docs/TG-WEB-001_QA_CHECKLIST.md)
