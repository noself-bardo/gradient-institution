# Drive Inventory

Status: DRAFT / FIRST PASS

Drive root inspected:

`C:\Users\steve\My Drive\The Gradient`

Drive is asset and package storage. It is not the live Git working directory and should not become the canonical repo.

## First-Pass Scope

Initial inventory focuses on:

- GFVP
- Publishing Constitution

Control Center and platform packages are deferred.

## Top-Level Finding

The GFVP package family is present under:

`C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01`

The broad Drive scan returned 770 files under the Gradient root.

The GFVP name search returned 206 files.

## GFVP Subareas Observed

- `02_PLATE_BRIEFS`
- `03_PROMPT_PACKETS`
- `04_PREFLIGHT_QC`
- `05_LOCKED_PROMPTS`
- `09_HANDOFFS`
- `11_OBJECT_SPECIFICATIONS`
- `12_COMPILER_PROMPTS`
- `13_ROADMAPS`

## Important GFVP Files Observed

Remediation and completion:

- `09_HANDOFFS/GFVP_PACK_B_REMEDIATION_LOG_v1-0.md`
- `09_HANDOFFS/GFVP_PACK_B_REMEDIATION_COMPLETION_REPORT_v1-0.md`
- `09_HANDOFFS/GFVP_LEVEL_A_REMEDIATION_COMPLETION_REPORT_v1-0.md`
- `09_HANDOFFS/GFVP_LEVEL_A_REMEDIATION_LOG_v1-0.md`

Roadmaps and receipts:

- `13_ROADMAPS/GFVP_PACK_B_TEXT_PRODUCTION_RECEIPT.md`
- `13_ROADMAPS/GFVP_PACK_B_REVIEW_SHEET_v0-1.md`
- `13_ROADMAPS/GFVP_PACK_F_TEXT_PRODUCTION_RECEIPT.md`
- `13_ROADMAPS/GFVP_PACK_F_REVIEW_SHEET_v0-1.md`

P001 observed:

- `02_PLATE_BRIEFS/P001_identity_constitutional-knowledge-ecology.md`
- `03_PROMPT_PACKETS/P001_identity_constitutional-knowledge-ecology_prompt.md`
- `04_PREFLIGHT_QC/P001_identity_constitutional-knowledge-ecology_qc.md`
- `05_LOCKED_PROMPTS/P001_identity_constitutional-knowledge-ecology_prompt.md`

P016-P040 material observed:

- Object specifications in `11_OBJECT_SPECIFICATIONS`
- Compiled prompts and QC in `12_COMPILER_PROMPTS`

## Publishing Constitution Finding

No obvious Drive file found by the first filename searches for `Publishing`.

The word `Constitution` appears in GFVP-related files, especially P001 and P040, but the dedicated Publishing Constitution source has not yet been located in Drive.

Likely next step: locate through Notion first, then map any linked Drive source.

## First-Pass Rules

- Do not move any Drive files.
- Do not rename package folders.
- Do not copy binaries into Git.
- Do not checksum everything in the first pass.
- Use selective checksums later for important zips, approved outputs, binaries, and release packages.

## Open Questions

- Where are approved GFVP image binaries stored?
- Which Drive folder contains release packages?
- Are any GFVP zips present outside the synced `The Gradient` folder?
- Where is Publishing Constitution v0.1 stored?
- Which Drive files correspond to ratified versus draft state?
