# TG-SRC-VIS-001 Destination Structure Draft

Status: DRAFT / STRUCTURE PROPOSAL ONLY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Constraint: This structure does not authorize migration, extraction, source promotion, canon change, external edits, commits, app/RPC work, file moves, file renames, folder creation, or folder restructuring.

## Scope

Source ID: `TG-SRC-VIS-001`

Provisional primary destination:

`06_visual_language/gfvp/`

Deferred:

- `TG-SRC-PUB-002`
- release/export packages
- approved/generated PNGs
- missing zip/export package

## Proposed Internal Structure

Planning-only structure:

```text
06_visual_language/gfvp/
  README.md
  SOURCE_CLUSTER_MANIFEST.md

  package_control/
    00_README/
    01_SOURCES/

  roadmaps/

  active_workflow/
    object_specifications/
    compiler_prompts/

  legacy_workflow/
    plate_briefs/
    legacy_prompt_packets/
    legacy_locked_prompts/
    qc/
      preflight/

  production_evidence/
    handoffs/

  archive/
```

No folders should be created from this proposal without later explicit approval.

## Source Folder Mapping

| Drive Folder | Proposed Planning Destination | Migration Posture | Notes |
|---|---|---|---|
| `00_README/` | `package_control/00_README/` | Yes | Package boundary and lock receipt. |
| `01_SOURCES/` | `package_control/01_SOURCES/` | Maybe | Historical/stale manifest; include only with supersession note. |
| `02_PLATE_BRIEFS/` | `legacy_workflow/plate_briefs/` | Maybe | Legacy broad plate briefs. |
| `03_PROMPT_PACKETS/` | `legacy_workflow/legacy_prompt_packets/` | Maybe | Legacy broad prompt packets. |
| `04_PREFLIGHT_QC/` | `legacy_workflow/qc/preflight/` | Yes | Legacy preflight QC evidence. |
| `05_LOCKED_PROMPTS/` | `legacy_workflow/legacy_locked_prompts/` | Yes / Maybe | Historical locked prompt copies. |
| `06_GENERATED_OUTPUTS/` | Reference only | No | Deferred `TG-SRC-PUB-002` generation receipt metadata. |
| `07_OUTPUT_QC/` | Reference only or future receipt refs | Maybe | Output QC metadata may support authority review. |
| `08_APPROVED_OUTPUTS/` | Reference only | No | Deferred `TG-SRC-PUB-002` approval receipt metadata. |
| `09_HANDOFFS/` | `production_evidence/handoffs/` | Yes | Handoffs, remediation, completion reports. |
| `10_ADMISSION_RECOMMENDATIONS/` | Omit until populated | No | Empty folder. |
| `11_OBJECT_SPECIFICATIONS/` | `active_workflow/object_specifications/` | Yes / Maybe | Active source authority. |
| `12_COMPILER_PROMPTS/` | `active_workflow/compiler_prompts/` | Yes / Maybe | Derived compiler outputs; version chains require notes. |
| `13_ROADMAPS/` | `roadmaps/` | Yes | Roadmap, protocol, pack review/receipt docs. |
| `99_ARCHIVE/` | `archive/` | Yes / Maybe | Failure, IDR, revision lineage. |

## Rationale

- Preserve source clusters intact where possible.
- Group by lifecycle rather than raw Drive numbering.
- Keep active workflow separate from legacy workflow.
- Keep source-system materials separate from publication/release outputs.
- Preserve multi-version chains without renaming files.
- Use root-level manifest docs for authority hierarchy and do-not-import rules.

## Proposed Root Files

If migration is later approved, the `gfvp/` root could contain:

- `README.md`: source ID, not-canon disclaimer, import boundary, source lineage.
- `SOURCE_CLUSTER_MANIFEST.md`: file counts, authority hierarchy, supersession notes, do-not-import list, receipt requirements.

These files should not be created until explicitly approved.

## Explicitly Outside `gfvp/`

| Material | Source ID | Proposed Handling |
|---|---|---|
| Approved PNGs | `TG-SRC-PUB-002` | Defer; keep in Drive until located/confirmed. |
| Generated/candidate PNGs | `TG-SRC-PUB-002` | Defer; keep in Drive if located. |
| Export zip/package | `TG-SRC-PUB-002` | Defer until located/confirmed. |
| Release/package manifests | `TG-SRC-PUB-002` | Future `07_publishing/series/gfvp/` lightweight refs only. |
| Receipt index copies | Cross-reference | Future `11_receipts/` references only after receipt policy. |
| Status registry | Cross-reference | Future `04_registries/` derivative only after approval. |

## Anti-Patterns

- Mirroring all Drive folders flatly under `gfvp/`.
- Importing `06_GENERATED_OUTPUTS/`, `07_OUTPUT_QC/`, and `08_APPROVED_OUTPUTS/` as active source-system content.
- Treating `BATCH_01_MANIFEST.md` as current plate status authority.
- Renaming versioned files during import.
- Splitting per-plate files into new plate folders before source inventory is locked.
- Importing both prompt packets and locked prompts as active generation sources.
- Creating empty `admission_recommendations/` just to mirror an empty Drive folder.
- Treating repo placement as canon promotion.

## Migration Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Authority conflict between manifest, roadmap, README, handoff, Notion taxonomy | High | Require authority hierarchy approval before import. |
| P003/P007 multi-version chains | High | Preserve filenames and add manifest current-version pointers. |
| P002/P003 composite lock evidence | Medium | Document gap; do not create retrospective receipts without approval. |
| Legacy workflow semantic drift | Medium | Keep under `legacy_workflow/` with supersession notes. |
| Receipt/output folders blurring source/release boundary | High | Keep `TG-SRC-PUB-002` deferred and reference-only. |
| Missing binaries | Critical for `TG-SRC-PUB-002` | Do not include release/export binaries in `TG-SRC-VIS-001`. |
| Notion mirror ambiguity | Medium | Treat Notion GFVP pages as references until source-location review. |

## Open Questions

- Should raw Drive numeric folder names be preserved inside grouped folders?
- Should `01_SOURCES/` stay under package control or move to archive treatment?
- Should output QC metadata be excluded entirely or referenced from a receipt index?
- Should `99_ARCHIVE/` stay under GFVP or be referenced from `12_archive_refs/`?
- Should a future `_version_index/` sidecar exist for P003/P007, or should version mapping live only in `SOURCE_CLUSTER_MANIFEST.md`?
- Should `04_registries/` receive a future plate-status registry derivative?

## Recommended Next Gate

Review `TG_SRC_VIS_001_HUMAN_REVIEW_PACKET_DRAFT.md` and `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_DRAFT.md` before any file import.

The manifest design should settle:

- authority hierarchy
- include/exclude list
- version-chain representation
- receipt-reference strategy
- do-not-import boundary for `TG-SRC-PUB-002`

## Output Summary

What changed:

- Created this destination structure draft for `TG-SRC-VIS-001`.

What should be locked:

- Planning only.
- No folder creation or source movement.
- No migration, extraction, source promotion, canon change, or app/RPC work.

What remains living:

- Human approval of structure.
- Manifest design.
- Receipt reference strategy.
- Authority hierarchy decision.
