# Migration Manifest

Status: DRAFT v0.2 / FIRST PASS

Scope: GFVP plus Publishing Constitution.

This manifest is a working source-to-destination map. It does not move files, promote documents, or ratify anything.

## Source Roots

- Notion root: `https://app.notion.com/p/391deacab3a581be9a7ac9d0cf84c752`
- Drive root: `C:\Users\steve\My Drive\The Gradient`
- Initial Drive package root found: `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01`
- Repo root: `C:\Users\steve\Projects\gradient-institution`

## Migration Priorities

1. Establish repo skeleton and policy.
2. Inventory GFVP and Publishing Constitution sources.
3. Classify files by status and destination.
4. Review before copying source material into Git.
5. Keep binaries and zips in Drive unless explicitly approved.

## Known Status Claims From Intake

- GFVP P001-P011 are visually approved and locked.
- GFVP P012-P015 are text-locked.
- P012 is the next image-gate candidate.
- P016-P040 Level A text substrate exists but is not fully accepted.
- Pack B remediation is reported, but revised files still need review.
- Publishing Constitution v0.1 is complete across eight volumes.

These claims need source linkage before being treated as registry data.

## Proposed Destinations

GFVP source/spec/object/prompt/QC system:

- Proposed repo destination: `06_visual_language/gfvp/`
- Drive source: `gradient_foundational_visual_package_batch_01`
- Treat GFVP as a visual-canon / foundational-atlas system, not merely a publication.
- Preserve Drive as binary/package source.

GFVP released publication/export packages:

- Proposed repo destination: `07_publishing/series/gfvp/`
- Keep binaries, zips, PDFs, images, and release assets in Drive unless explicitly approved.
- Use Git for lightweight manifests and references.

Publishing Constitution:

- Proposed repo destination: `07_publishing/publishing_constitution/`
- Source location: Notion and/or Drive source still needs inventory.
- If source review shows it functions as institutional doctrine rather than publishing-operational law, move the proposed destination to `01_constitution/`.
- Do not migrate until exact source files/pages are identified.

Receipts and reviews:

- Proposed repo destination: `11_receipts/`
- Candidate sources include GFVP handoffs, review sheets, production receipts, QC reports, and approval receipts.

Registry state:

- Proposed repo destination: `04_registries/`
- Store status vocabulary, stable ID rules, and event schema drafts before Supabase work.

Inventories:

- Proposed repo destination: `10_inventories/`

Control Center / Supabase / app work:

- Proposed repo destination: `08_platform/`
- Deferred until skeleton and manifest review is complete.

Codex / Zo / agent contracts:

- Proposed repo destination: `09_agents/`
- Do not formalize automation loops until permission boundaries are reviewed.

## Hybrid Source Preservation Policy

- The migration will preserve source clusters intact in their primary homes during initial migration.
- Functional folders may reference source clusters without duplicating or fragmenting them.
- Derivative controls may be created only when needed and must cite their source cluster.
- Derivatives that change institutional behavior require receipts in `11_receipts/`.
- Extraction does not make a derivative canonical unless governance admits and ratifies it.
- The draft operating mechanics are defined in `EXTRACTION_POLICY_DRAFT.md`.

## Draft Source ID and Extraction Controls

- Migrated source clusters should receive provisional stable source IDs before migration using `TG-SRC-[DOMAIN]-[###]`.
- Derivative controls should use the standard derivative-control header defined in `EXTRACTION_POLICY_DRAFT.md`.
- Functional references should point to intact source clusters rather than duplicating content.
- Human ratification is required before extraction changes constitutional meaning, governance rules, lifecycle/status rules, source authority, canon status, migration authorization, folder restructuring, or app/RPC implementation.

## Current Source Cluster Placement Leans

| Source Cluster | Primary Provisional Home | Split / Reference Candidates | Status |
|---|---|---|---|
| Publishing Constitution | `07_publishing/publishing_constitution/` | `06_visual_language/`, `03_governance/`, `09_agents/`, `08_platform/`, `12_archive_refs/`, `11_receipts/` | Unresolved; source cluster should remain intact |
| GFVP | `06_visual_language/gfvp/` | `07_publishing/series/gfvp/`, `11_receipts/` | Provisional; system/source stays separate from release packages |
| Card System | `05_knowledge_systems/` | `04_registries/`, `02_stewardship/`, `03_governance/`, `11_receipts/`, later `08_platform/` | Unresolved; split placement likely |
| Engine Registry | `05_knowledge_systems/` and `04_registries/` | `09_agents/` only for executable/agent-facing contracts | Unresolved; split placement strongly supported |
| Archive of Becoming | `12_archive_refs/` | `11_receipts/`, `03_governance/`, possible future archive model | Unresolved; future archive model possible |

This manifest update records draft migration policy only. It does not authorize migration, extraction, folder restructuring, source promotion, canon change, external edits, commits, or app/RPC work.

## First-Pass Drive Findings

Drive contains a GFVP batch root:

- `gradient_foundational_visual_package_batch_01`

GFVP-related files found by name search: 206.

Important subareas observed in the GFVP batch:

- `02_PLATE_BRIEFS`
- `03_PROMPT_PACKETS`
- `04_PREFLIGHT_QC`
- `05_LOCKED_PROMPTS`
- `09_HANDOFFS`
- `11_OBJECT_SPECIFICATIONS`
- `12_COMPILER_PROMPTS`
- `13_ROADMAPS`

Observed remediation and review files:

- `09_HANDOFFS/GFVP_PACK_B_REMEDIATION_LOG_v1-0.md`
- `09_HANDOFFS/GFVP_PACK_B_REMEDIATION_COMPLETION_REPORT_v1-0.md`
- `13_ROADMAPS/GFVP_PACK_B_TEXT_PRODUCTION_RECEIPT.md`
- `13_ROADMAPS/GFVP_PACK_B_REVIEW_SHEET_v0-1.md`
- `09_HANDOFFS/GFVP_LEVEL_A_REMEDIATION_COMPLETION_REPORT_v1-0.md`
- `09_HANDOFFS/GFVP_LEVEL_A_REMEDIATION_LOG_v1-0.md`

Observed P016-P040 material:

- Object specification files in `11_OBJECT_SPECIFICATIONS`
- Compiled prompt and QC files in `12_COMPILER_PROMPTS`

Observed P001 material:

- `02_PLATE_BRIEFS/P001_identity_constitutional-knowledge-ecology.md`
- `03_PROMPT_PACKETS/P001_identity_constitutional-knowledge-ecology_prompt.md`
- `04_PREFLIGHT_QC/P001_identity_constitutional-knowledge-ecology_qc.md`
- `05_LOCKED_PROMPTS/P001_identity_constitutional-knowledge-ecology_prompt.md`

## Gaps To Resolve

- Exact Publishing Constitution source pages/files.
- Exact approved image locations for GFVP P001-P011.
- Exact receipt locations for visual approval and text lock status.
- Whether GFVP P012-P015 text-locked files are in Drive, Notion, or both.
- Whether Pack B revised files are present and which files require review.
- Whether any local non-Drive packages exist outside `C:\Users\steve\My Drive\The Gradient`.

## Do Not Move Yet

- Approved GFVP images.
- Zipped Codex outputs.
- Completion reports.
- Source packets.
- Any file in approved/release folders.

## Next Manifest Step

After human approval, fetch the Notion child pages for:

- `00 Command Center`
- `01 Constitution`
- `02 Specifications`
- `09 Worlds and Case Studies`
- `10 Implementation`
- `The Gradient — Visual Canon Project`

Then map GFVP and Publishing Constitution pages to repo destinations.
