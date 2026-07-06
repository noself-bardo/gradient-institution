# The Gradient Path Reference Audit Draft

Status: DRAFT / PATH REFERENCE AUDIT ONLY

Authority: Not canonical

Constraint: This audit does not authorize migration, extraction, source promotion, canon change, external edits, app/RPC work, commits, or additional folder restructuring.

## Audit Scope

Local repo docs only:

`C:\Users\steve\Projects\gradient-institution`

Purpose:

- Identify old v0.1 path references after the approved placeholder-only v0.2 folder restructuring.
- Distinguish mechanical path updates from historical before/after records.
- Avoid altering source evidence, source review conclusions, canon, receipts, or external systems.

## Search Patterns

Searched for old v0.1 folder paths and labels:

- `08_inventories/`
- `04_registry/`
- `02_specifications/`
- `03_publications/`
- `05_receipts/`
- `06_apps/`
- `07_agents/`
- `09_archive_refs/`
- Backslash variants of the same paths
- Human-readable labels such as `02 Specifications`, `04 Registry`, and `08 Inventories`

No backslash-style old repo paths were found.

## Recommended Mechanical Updates

These references point to local migration-control files whose physical folder moved from `08_inventories/` to `10_inventories/`. Updating them would not change source evidence or source review conclusions.

| Old path found | File containing reference | Recommended replacement | Safe to update mechanically | Human review needed | Historical v0.1 reference |
|---|---|---|---|---|---|
| `08_inventories/DRIVE_INVENTORY.md` | `SOURCE_REVIEW_PUBLISHING_CONSTITUTION.md` | `10_inventories/DRIVE_INVENTORY.md` | Yes | No | No |
| `08_inventories/NOTION_INVENTORY.md` | `SOURCE_REVIEW_04_ARCHIVE_OF_BECOMING.md` | `10_inventories/NOTION_INVENTORY.md` | Yes | No | No |
| `08_inventories/NOTION_INVENTORY.md` | `SOURCE_REVIEW_05_ENGINE_REGISTRY.md` | `10_inventories/NOTION_INVENTORY.md` | Yes | No | No |
| `08_inventories/NOTION_INVENTORY.md` | `SOURCE_REVIEW_06_CARD_SYSTEM.md` | `10_inventories/NOTION_INVENTORY.md` | Yes | No | No |

## Applied Updates

Status: APPLIED / MECHANICAL PATH REFERENCES ONLY

Applied on: 2026-07-06

Approved scope:

- Replace current-path references from `08_inventories/` to `10_inventories/` only in the four source-review docs identified by this audit.

Files updated:

- `SOURCE_REVIEW_PUBLISHING_CONSTITUTION.md`
- `SOURCE_REVIEW_04_ARCHIVE_OF_BECOMING.md`
- `SOURCE_REVIEW_05_ENGINE_REGISTRY.md`
- `SOURCE_REVIEW_06_CARD_SYSTEM.md`

Not changed:

- Historical references in restructuring records.
- Historical references in receipts.
- Source-observed labels such as `02 Specifications`.
- Source evidence, conclusions, recommendations, authority language, canon, or external systems.
- Commits.

## Historical Restructuring References

These references intentionally describe the old path as part of a before/after restructuring record. They should remain unless a later editorial pass changes the record format.

| Old path found | File containing reference | Recommended replacement | Safe to update mechanically | Human review needed | Historical v0.1 reference |
|---|---|---|---|---|---|
| `08_inventories/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `04_registry/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `02_specifications/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `03_publications/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `05_receipts/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `06_apps/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `07_agents/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `09_archive_refs/` | `V0_2_FOLDER_RESTRUCTURING_PLAN.md` | None | No | No | Yes |
| `02_specifications/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `04_registry/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `03_publications/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `06_apps/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `07_agents/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `08_inventories/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `05_receipts/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `09_archive_refs/` | `V0_2_FOLDER_INVENTORY_DRAFT.md` | None | No | No | Yes |
| `04_registry/STATUS_VOCABULARY_DRAFT.md` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `08_inventories/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `02_specifications/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `03_publications/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `04_registry/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `05_receipts/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `06_apps/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `07_agents/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |
| `09_archive_refs/` | `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | None | No | No | Yes |

## Source-Observed Labels Requiring Care

These are not repo path references. They appear to record observed Notion page labels or future Notion fetch targets, so they should not be mechanically changed to v0.2 repo folder names.

| Old label found | File containing reference | Recommended replacement | Safe to update mechanically | Human review needed | Historical/source-observed reference |
|---|---|---|---|---|---|
| `02 Specifications` | `MIGRATION_MANIFEST.md` | None for this audit | No | Yes, before any Notion taxonomy or destination mapping change | Yes |
| `02 Specifications` | `10_inventories/NOTION_INVENTORY.md` | None for this audit | No | Yes, before any Notion taxonomy or destination mapping change | Yes |

## Audit Conclusion

Only four references are safe mechanical path updates:

- `SOURCE_REVIEW_PUBLISHING_CONSTITUTION.md`
- `SOURCE_REVIEW_04_ARCHIVE_OF_BECOMING.md`
- `SOURCE_REVIEW_05_ENGINE_REGISTRY.md`
- `SOURCE_REVIEW_06_CARD_SYSTEM.md`

All restructuring-plan, inventory, and receipt references to old v0.1 paths should remain historical.

The `02 Specifications` labels in `MIGRATION_MANIFEST.md` and `10_inventories/NOTION_INVENTORY.md` should remain source-observed Notion labels unless a future human review explicitly remaps them.

## Output Summary

What changed:

- Created this path-reference audit draft.
- Applied the four approved mechanical path updates in source-review docs.
- No receipt, inventory, manifest, canon, or external file was edited.

What should be locked:

- Old path references inside before/after restructuring records should remain historical.
- Source-observed Notion labels should not be mechanically rewritten as repo folder names.
- No commit is authorized by this audit.

What remains living:

- Whether to keep `02 Specifications` as a source-observed Notion label or later map it to a v0.2 repo destination.
- Whether receipt ID/type normalization should happen before commit.

Concrete next steps:

1. Review this audit.
2. Do not edit historical restructuring records, source-observed labels, canon, receipts, or external systems without separate explicit approval.
3. Decide whether receipt ID/type normalization should happen before commit.
4. Do not commit unless explicitly approved.
