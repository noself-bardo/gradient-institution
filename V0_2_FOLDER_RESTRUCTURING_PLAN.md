# The Gradient v0.2 Folder Restructuring Plan

Status: DRAFT / EXECUTED LOCALLY AFTER EXPLICIT APPROVAL

Authority: Not canonical

Constraint: This plan records the approved local placeholder-only folder restructuring. It does not authorize further folder restructuring, migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work.

## Current Known v0.2 Target Structure

- `00_command_center/`
- `01_constitution/`
- `02_stewardship/`
- `03_governance/`
- `04_registries/`
- `05_knowledge_systems/`
- `06_visual_language/`
- `07_publishing/`
- `08_platform/`
- `09_agents/`
- `10_inventories/`
- `11_receipts/`
- `12_archive_refs/`

## Resolved v0.1 Placeholder Issues

- Old `08_inventories/` became `10_inventories/`.
- Old `04_registry/` became `04_registries/`.
- Placeholder folders now match the known v0.2 numbering.
- Existing placeholders are marked `DRAFT / MIGRATION WORKSPACE ONLY`.
- Restructuring empty placeholders was not treated as source migration.

## Read-Only Inventory Findings

Inventory source:

- `V0_2_FOLDER_INVENTORY_DRAFT.md`

Current folders are v0.2-shaped after explicit approval.

Placeholder-only folders:

- `00_command_center/`
- `01_constitution/`
- `02_stewardship/`
- `03_governance/`
- `05_knowledge_systems/`
- `06_visual_language/`
- `07_publishing/`
- `08_platform/`
- `09_agents/`
- `12_archive_refs/`

Folders containing draft-control files:

- `04_registries/` contains `STATUS_VOCABULARY_DRAFT.md`
- `10_inventories/` contains local, Drive, Notion, and Supabase inventory drafts
- `11_receipts/` contains a placeholder README and the v0.2 folder restructuring receipt draft

No migrated source clusters were found inside current top-level folders.

## Proposed Restructuring Principles

- Restructure placeholders only, not source files.
- Preserve all existing draft control docs.
- Do not move imported source clusters yet.
- Do not create derivative controls during restructuring.
- Create placeholder READMEs only if needed to mark draft/noncanonical status.
- Record any executed restructuring later with a receipt.

## Executed Action Plan

1. Inventoried current top-level folders and placeholder READMEs.
2. Identified folders that were empty placeholders versus folders containing source/control files.
3. Proposed rename/create/delete actions for placeholders only.
4. Preserved existing draft control files at repo root.
5. Created or updated placeholder README language to say draft migration workspace only.
6. Received explicit approval before executing physical folder changes.
7. Created restructuring receipt draft in `11_receipts/`.

## Placeholder-Only Execution Record

This records the executed action. It does not authorize further physical changes.

1. Kept `00_command_center/`.
2. Kept `01_constitution/`.
3. Replaced `02_specifications/` with `02_stewardship/` as a placeholder-only folder.
4. Created `03_governance/`.
5. Renamed `04_registry/` to `04_registries/`, preserving `STATUS_VOCABULARY_DRAFT.md`.
6. Created `05_knowledge_systems/`.
7. Created `06_visual_language/`.
8. Replaced `03_publications/` with `07_publishing/` as a placeholder-only folder.
9. Replaced `06_apps/` with `08_platform/` as a placeholder-only folder.
10. Replaced `07_agents/` with `09_agents/` as a placeholder-only folder.
11. Renamed `08_inventories/` to `10_inventories/`, preserving all inventory draft files.
12. Replaced `05_receipts/` with `11_receipts/` as a placeholder plus draft receipt folder.
13. Replaced `09_archive_refs/` with `12_archive_refs/` as a placeholder-only folder.
14. Standardized placeholder README language to `DRAFT / MIGRATION WORKSPACE ONLY`.
15. Left all root draft-control files at repo root.
16. Created `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md`.

## Remaining Safe Restructure Candidates

Safe only after a new explicit execution approval:

- Further README wording cleanup.
- Receipt ID/type adjustment.
- Future approved movement of root draft-control files.

## Do-Not-Touch Candidates

Do not touch during placeholder restructuring:

- Root draft-control files.
- Source review files.
- Source ID index.
- Receipt template.
- Migration manifest unless separately approved.
- Source clusters.
- External systems.

## Do Not Touch

- source clusters
- Drive/Notion/Supabase
- app code
- canon files
- review files
- source ID index
- receipt template
- migration manifest except by later explicit approval

## Approval Gate

The user explicitly approved execution of this plan on 2026-07-06.

No further folder restructuring may occur until the user explicitly approves a new execution plan.

## Output Summary

What changed:

- Executed the approved v0.2 placeholder-only folder restructuring locally.
- Created `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md`.

What should be locked:

- No further physical folder changes are authorized without new explicit approval.
- No migration or source movement is authorized.

What remains living:

- Whether restructuring should be performed before or after a first commit.
- Whether the provisional receipt ID/type should be accepted.
- Whether root draft-control files should remain at repo root until after first commit.

Concrete next steps:

1. Review the executed local v0.2 folder structure.
2. Decide whether to approve a commit in a separate explicit instruction.
3. Do not migrate, extract, promote source, change canon, edit external systems, or resume app/RPC/platform work until explicitly authorized.
