# TG-WEB-001 — Source Policy

Status: Baseline Built / Asset Integration Pending  
Authority: Servant layer policy — subordinate to SOURCE_OF_TRUTH_POLICY.md at repo root

## Purpose

Define which sources may appear in the Archive Gateway, how they are labeled, and what link behavior is permitted.

## Source Eligibility

### May appear as public sources

- Ratified or locked constitutional and charter documents (with correct status label)
- Institutional Decision Records marked as governance sources
- Engine Registry entries with public Notion pages
- Validated case studies with reader-facing pages
- Visual Language doctrine and GFVP reference pages
- Companion publications explicitly marked as companion, not governing
- Reader-facing PDFs when actually present and readable

### Must not appear as public sources

- Internal production trackers
- Prompt handoffs and release status pages
- Unreviewed migration drafts from gradient-institution repo
- Agent contracts without separate review and approval
- Supabase schema or RPC documentation as governing authority
- ChatGPT project history without capture in Notion or Git

## Status Discipline

Every source entry must carry one of:

- **locked** — passed ratification gates
- **living** — under active review or practice
- **candidate** — proposed but not validated
- **pending** — known but not yet publicly available
- **companion** — reader-facing, not governing

Do not flatten these distinctions in UI copy or metadata.

## Role Labels

- **governing** — constitutional, charter, specification, or registry authority
- **companion** — explains or accompanies governing doctrine

Crisis Liturgies are always **companion**, never governing.

## Link Rules

1. Every public action must open a readable **local PDF** in `assets/pdf/`.
2. Do not link to Notion, Google Drive, release trackers, or production handoff pages.
3. Thumbnails live in `assets/img/` — companion artifacts only, not governing authority.
4. Open PDFs in new tabs with `rel="noopener noreferrer"`.
5. Distinguish companion from governing at every point of use.

## Crisis Liturgies III — Companion Series Boundary

CL-III (Emergency Objects) has completed print, archive lock, indexing, and frozen release snapshot stages.

For any web or gallery integration:

1. Use source-of-truth order documented in [CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md](CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md)
2. Treat `06_RELEASE_ASSEMBLY/.../CRISIS_LITURGIES_III_EMERGENCY_OBJECTS` as **supporting provenance only**
3. Do **not** display release-assembly “PDF BUILD NOT STARTED” as current status
4. Do not rebuild PDFs, regenerate images, alter canon, or modify source artwork
5. `tools/cl_iii_release_assembly_prep.py` is read-only verification evidence — do not run to overwrite Drive assets

Public PDF distribution is governed by [TG-WEB-001_PUBLIC_PDF_STRATEGY.md](TG-WEB-001_PUBLIC_PDF_STRATEGY.md). Public buttons use relative `assets/pdf/` paths on the deploy origin only — never Drive or Notion URLs.

## Data File Authority

JSON data files in `/data/` are implementation convenience. They do not govern the institution. When data conflicts with Notion or constitutional sources, the higher layer wins per source-of-truth order.

## Update Process

1. Verify source eligibility against this policy.
2. Update the relevant JSON file with correct status and role.
3. Run QA checklist link pass before deployment.
4. Do not promote status (e.g., candidate → locked) without human ratification.
