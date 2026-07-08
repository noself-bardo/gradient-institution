# TG-WEB-001 — Source Policy

Status: Active Rebuild  
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

## Data File Authority

JSON data files in `/data/` are implementation convenience. They do not govern the institution. When data conflicts with Notion or constitutional sources, the higher layer wins per source-of-truth order.

## Update Process

1. Verify source eligibility against this policy.
2. Update the relevant JSON file with correct status and role.
3. Run QA checklist link pass before deployment.
4. Do not promote status (e.g., candidate → locked) without human ratification.
