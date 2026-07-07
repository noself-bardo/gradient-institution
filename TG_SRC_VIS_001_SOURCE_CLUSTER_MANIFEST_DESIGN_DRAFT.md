# TG-SRC-VIS-001 Source Cluster Manifest Design Draft

Status: DRAFT / MANIFEST DESIGN ONLY (REVISED 2026-07-06)

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Constraint: This design does not authorize migration, extraction, source promotion, canon change, external edits, commits, app/RPC work, file moves, file renames, folder creation in the repo destination, or creation of `06_visual_language/gfvp/SOURCE_CLUSTER_MANIFEST.md` until explicitly approved.

Prerequisite: Human ratification bundle recorded 2026-07-06 in `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md`. Design revised to align with ratified planning decisions.

## Purpose

Define the schema, sections, and content rules for a future `SOURCE_CLUSTER_MANIFEST.md` at:

`06_visual_language/gfvp/SOURCE_CLUSTER_MANIFEST.md`

This document is the design specification. It is not the manifest itself.

## Manifest Role

The source-cluster manifest will be a migration-control derivative that:

- Records what the `TG-SRC-VIS-001` cluster contains and excludes.
- Cites Drive source locations without replacing them.
- Embodies ratified authority hierarchy and version-chain pointers.
- Draws a hard boundary against `TG-SRC-PUB-002` release/export material.
- States receipt requirements before any future import.
- Does not promote the cluster to institutional canon.

Per `SOURCE_OF_TRUTH_POLICY.md`, manifests are safe to draft; populating the repo destination requires later approval.

## Proposed Manifest Header Block

Future manifest should open with a fixed header block:

```markdown
---
manifest_type: source_cluster
source_id: TG-SRC-VIS-001
source_cluster: GFVP source/spec/object/prompt/QC system
drive_root: gradient_foundational_visual_package_batch_01
provisional_destination: 06_visual_language/gfvp/
manifest_status: DRAFT
authority: NOT_CANONICAL
baseline_commit: f8aad4f2396cd92be7f53fa220c07797403f3dd4
migration_readiness: NEEDS_SOURCE_INVENTORY
migration_authorized: false
receipt_required_before_import: true

# Ratified planning fields (2026-07-06; planning only — not canon)
roadmap_plate_identity_authority: GFVP_40_PLATE_ROADMAP_v0-1.md
approved_plate_count: 11
approved_plate_range: P001-P011
next_image_gate_candidate: P012
remediation_vocabulary_role: historical_secondary
historical_manifest_treatment: superseded_by_40_plate_roadmap
deferred_pub_002_boundary: true

deferred_source_ids:
  - TG-SRC-PUB-002
---
```

**Field definitions:**

| Field | Value / Rule |
|---|---|
| `roadmap_plate_identity_authority` | `GFVP_40_PLATE_ROADMAP_v0-1.md` controls plate identity for VIS-001 source inventory planning (A1 ratified). |
| `approved_plate_count` | `11` — planning status only; does not authorize PUB-002 release import (A3 ratified). |
| `approved_plate_range` | `P001-P011` |
| `next_image_gate_candidate` | `P012` — planning only; no image generation or publication action authorized (A6 ratified). |
| `remediation_vocabulary_role` | `historical_secondary` — Pack B–F remediation may inform interpretation; must not override roadmap plate identity (A7 ratified). |
| `historical_manifest_treatment` | Batch manifest, README/handoff count drift, and legacy workflow are historical evidence, not current controlling authority (A2/D3/D4 ratified). |
| `deferred_pub_002_boundary` | `true` — PNGs, generation/approval folders, zip, and release exports remain out of VIS-001 import scope. |

## Manifest Section Outline

### 1. Scope and Boundary

Content rules:

- State source ID, cluster name, Drive root path, and provisional repo destination.
- Embed ratified header fields (table above) in prose or structured block.
- Explicitly exclude `TG-SRC-PUB-002` binaries, PNGs, zips, PDFs, and release/export packages (`deferred_pub_002_boundary: true`).
- State that repo placement does not constitute canon promotion.
- Cite `FIRST_MIGRATION_CANDIDATE_REVIEW_TG_SRC_VIS_001.md` recommendation: `NEEDS_SOURCE_INVENTORY`.
- State that approved plate count and next-gate fields are **planning status only**.

### 2. Source Inventory Summary

Content rules:

- File counts by Drive folder (from file inventory draft).
- Artifact class totals: markdown, CSV, empty folders.
- Agent swarm verification (read-only): **25 PNG files** present in synced Drive (`06_GENERATED_OUTPUTS/`: 14; `08_APPROVED_OUTPUTS/`: 11). Import remains unauthorized under `TG-SRC-PUB-002`.
- Link to `TG_SRC_VIS_001_FILE_INVENTORY_DRAFT.md` as detailed inventory evidence.

Proposed summary table:

| Drive Folder | Files | Posture | Proposed Repo Subpath | Import? |
|---|---:|---|---|---|
| `00_README/` | 2 | Package control | `package_control/00_README/` | Yes |
| `01_SOURCES/` | 1 | Historical manifest | `package_control/01_SOURCES/` | Yes |
| `02_PLATE_BRIEFS/` | 8 | Legacy historical | `legacy_workflow/plate_briefs/` | Yes |
| `03_PROMPT_PACKETS/` | 8 | Legacy historical | `legacy_workflow/legacy_prompt_packets/` | Yes |
| `04_PREFLIGHT_QC/` | 11 | Legacy QC | `legacy_workflow/qc/preflight/` | Yes |
| `05_LOCKED_PROMPTS/` | 9 | Legacy locked | `legacy_workflow/legacy_locked_prompts/` | Yes |
| `06_GENERATED_OUTPUTS/` | 10 | Receipt metadata | — | No (PUB-002) |
| `07_OUTPUT_QC/` | 14 | QC metadata | Reference only (authority) | No (co-import) |
| `08_APPROVED_OUTPUTS/` | 11 | Approval metadata | — | No (PUB-002) |
| `09_HANDOFFS/` | 8 | Production evidence | `production_evidence/handoffs/` | Yes |
| `10_ADMISSION_RECOMMENDATIONS/` | 0 | Empty | — | No |
| `11_OBJECT_SPECIFICATIONS/` | 93 | Active source | `active_workflow/object_specifications/` | Yes |
| `12_COMPILER_PROMPTS/` | 85 | Active derived | `active_workflow/compiler_prompts/` | Yes |
| `13_ROADMAPS/` | 19 | Scope/status/protocol | `roadmaps/` | Yes |
| `99_ARCHIVE/` | 4 | Lineage/archive | `archive/` | Yes |

**D3/D4 ratified (2026-07-06):** Legacy workflow folders (`02`–`05`) and historical batch manifest (`01_SOURCES/`) are **included as historical evidence**, not current controlling authority. Import posture is **Yes** with supersession notes in Section 5.

### 3. Authority Hierarchy (Ratified Subset)

Content rules:

- Embed human-ratified authority ordering (2026-07-06).
- **Roadmap controls plate identity** for VIS-001 source inventory planning (A1).
- Stale manifest, README/handoff count drift, and legacy workflow are **historical** — not current controlling authority (A2, D3, D4).
- Pack B–F remediation vocabulary is **historical/secondary** — may inform interpretation; **must not override roadmap plate identity** (A7).
- **Pack review sheets are not primary status authority over roadmap.** They may be cited as secondary/chronological evidence only.
- Mark unresolved conflicts by conflict ID (`AUTH-C1`–`AUTH-C16`).
- Do not silently resolve deferred conflicts; use `pending_human_confirmation` or `deferred` where needed.

Ratified hierarchy for manifest embedding:

| Tier | Authority | Role | Ratification |
|---:|---|---|---|
| 1 | `GFVP_40_PLATE_ROADMAP_v0-1.md` | **Plate identity authority** (primary) | A1 |
| 2 | Roadmap lock receipt | Scope/sequence lock only — ignore stale count fields | A1/A3 |
| 3 | `GFVP_BATCH_PRODUCTION_PROTOCOL_v0-1.md` | Production process | — |
| 4 | `11_OBJECT_SPECIFICATIONS/README.md` + per-plate specs | Source authority (generation definitions) | — |
| 5 | Per-plate QC/approval chain metadata | Plate-level evidence (reference; output folders deferred PUB-002) | B1/B3 |
| 6 | `09_HANDOFFS/` | Chronology and operational context | — |
| 7 | `00_README/README.md` | Orientation only — verify against roadmap; count fields historical | A3 |
| S | Pack review sheets, text production receipts, remediation reports | **Secondary/historical** — informative only; does not override Tier 1 | A7 |
| H | Batch manifest, plate briefs, prompt packets, locked prompts | **Historical/superseded** — lineage only | A2, D3, D4 |

**Anti-override rule:** No manifest row, status field, or pack-level summary may treat pack sheets or remediation vocabulary as superseding roadmap plate identity or approved-plate count.

### 4. Production Status and Next Gate (Ratified A3, A6)

Content rules:

- State **`approved_plate_count: 11`** and **`approved_plate_range: P001-P011`**.
- Clarify: planning status only — **does not authorize PUB-002 release import or binary verification**.
- State **`next_image_gate_candidate: P012`**.
- Clarify: planning only — **does not authorize image generation, publication action, or image-gate execution**.
- Mark stale references superseded for planning:
  - README/handoff/roadmap-lock-receipt summary lines showing "Approved: 10" → historical (A3).
  - `GFVP_PACK_A_TEXT_LOCK_RECEIPT.md` gate line naming P011 as next candidate → historical for sequencing (AUTH-C11, A6).
- Do not treat this section as operational authorization or registry state.

Proposed manifest fields (required):

```yaml
approved_plate_count: 11
approved_plate_range: P001-P011
next_image_gate_candidate: P012
planning_scope_only: true
image_generation_authorized: false
publication_action_authorized: false
```

### 5. Plate Identity Map (Roadmap-Derived)

Content rules:

- Derive plate ID, object name, and family from **`GFVP_40_PLATE_ROADMAP_v0-1.md`** (A1).
- Do not derive current plate identity from batch manifest, plate briefs, or legacy prompt packets.
- Note semantic drift where legacy briefs differ (P003, P004, P007) with pointer to Section 6 supersession.
- For P001–P011: mark planning approval status per A3 (not PUB-002 binary verification).
- For P012–P040: record roadmap status column only; next gate P012 called out in Section 4.

This section operationalizes `roadmap_plate_identity_authority` in the header.

### 6. Supersession and Historical Treatment

Content rules:

- Document legacy workflow supersession: plate briefs → prompt packets → locked prompts → object spec/compiler workflow.
- Record `BATCH_01_MANIFEST.md` as **historical** 8-plate index superseded by 40-plate roadmap (`historical_manifest_treatment`).
- Record README, roadmap lock receipt, and handoff **count drift** (10 vs 11) as historical — ratified count is **11** (A3).
- Record semantic drift for P003 (Ecology of Memory → Source Review) and P007 (Institutional Decision Records → Relationship).
- **D3/D4 ratified:** Legacy folders preserved under `legacy_workflow/` for lineage; **not active generation sources**.
- **A7 ratified:** Remediation vocabulary and pack review sheets cited as **historical/secondary** context only.

### 7. Current Version Index

Content rules:

- Manifest carries version pointers; no separate `_version_index/` sidecar unless later ratified (C3).
- Preserve original filenames; use manifest rows for "current" designation only.
- **B1/B3 ratified (2026-07-06):** P002/P003 use `Approved / Locked by composite evidence (source-system only)`.

Proposed version index table (exemplars — extend to P002–P011):

| Plate | Current Object Spec | Current Compiler | Current Output QC | Current Approval | Lock Posture | Notes |
|---|---|---|---|---|---|---|
| P003 | `GFVP-OBJ-P003-SOURCE-REVIEW_v0-2.md` | `GFVP-COMPILED-P003-SOURCE-REVIEW_PROMPT_v0-4.md` | `P003_output_qc_candidate_v0-4.md` | `P003_APPROVAL_RECEIPT.md` | Composite (source inventory only) | No standalone object lock receipt |
| P007 | `GFVP-OBJ-P007-RELATIONSHIP_v0-1.md` | `GFVP-COMPILED-P007-RELATIONSHIP_PROMPT_v0-2.md` | `P007_output_qc_candidate_v0-2.md` | `P007_APPROVAL_RECEIPT.md` | Composite + object lock v0-1 | Object lock predates v0-2 compiler regen |

Plates P012–P040: record text-ready / spec-only / no-compiler status from **roadmap**; no version chain beyond current spec file unless multi-version exists.

Output QC and approval filenames are **reference metadata** (PUB-002 deferred) — cite paths only, do not co-import.

### 8. Lock Evidence Register

Content rules:

- Separate lock types: roadmap scope, legacy text lock, object/prompt-ready, visual output, pack text, composite.
- For P002/P003, use ratified notation: **`Approved / Locked by composite evidence (source-system only)`** (B1/B3).
- Record process variance: missing standalone object lock receipts for P002/P003.
- Do not claim binary or publication verification.

| Plate | Lock Type | Primary Evidence | Binary Verified? |
|---|---|---|---|
| Scope | Roadmap scope lock | `GFVP_40_PLATE_ROADMAP_LOCK_RECEIPT.md` | N/A |
| Legacy era | Text automation lock | `00_README/LOCK_RECEIPT.md` | N/A (historical era) |
| P004–P011 | Object lock pattern | `*_LOCK_RECEIPT.md` in object specs | No (metadata only) |
| P002, P003 | Composite (source inventory only) | Spec + compiler QC + output QC + approval + roadmap | No — not publication verification |
| P001–P011 visual | Output approval metadata | `08_APPROVED_OUTPUTS/*` | **Deferred** (`TG-SRC-PUB-002`) |

### 9. Do-Not-Import List

Hard exclusions for `TG-SRC-VIS-001` import (`deferred_pub_002_boundary: true`):

| Item | Source ID | Reason |
|---|---|---|
| Approved PNG binaries | `TG-SRC-PUB-002` | Release asset; 11 PNGs present in sync; import deferred |
| Generated/candidate PNG binaries | `TG-SRC-PUB-002` | Release asset; 14 PNGs present in sync; import deferred |
| GFVP zip/export package | `TG-SRC-PUB-002` | Not located |
| PDFs and publication exports | `TG-SRC-PUB-002` | Release scope |
| `06_GENERATED_OUTPUTS/` payload | `TG-SRC-PUB-002` | Generation receipt metadata only |
| `08_APPROVED_OUTPUTS/` payload | `TG-SRC-PUB-002` | Approval receipt metadata only |
| Empty `10_ADMISSION_RECOMMENDATIONS/` | — | No content |
| Notion page bodies | External | Notion remains navigational authority; no external edit |

Soft exclusion (reference only, not co-imported):

| Item | Handling |
|---|---|
| `07_OUTPUT_QC/` | Cite from manifest for authority; optional future `11_receipts/` refs |
| Notion receipt mirrors (`NTN-REC-*`) | Metadata cross-ref only until Notion mapping authorized |

### 10. Receipt Reference Strategy

Content rules:

- Manifest states which receipt classes stay in-cluster vs. cross-reference from `11_receipts/`.
- No receipt copies created in this phase.

Proposed default:

| Receipt Class | Location on Import | Cross-Ref |
|---|---|---|
| Package/roadmap lock receipts | Co-located under `roadmaps/` or `package_control/` | Optional index in `11_receipts/` later |
| Object lock receipts (P004–P011) | Co-located with object specs | Optional |
| Handoffs/remediation | `production_evidence/handoffs/` | Secondary/historical context (A7) |
| Output QC and approval metadata | **Not imported** with VIS-001 | Future lightweight refs under `11_receipts/` when PUB-002 resolved |
| Notion mirrors | Not imported | URL/ID reference only |

### 11. Plate Coverage Matrix

Content rules:

- Single matrix for P001–P040: object spec, compiler, output approved (planning), inventory note.
- **Ratified approved range: P001–P011 (11 plates)** — planning status only (A3).
- Derive per-plate status labels from **roadmap** first; pack/remediation notes secondary only (A7).

### 12. Notion Cross-Reference Index (Metadata Only)

Content rules:

- List known Notion GFVP pages from `10_inventories/NOTION_INVENTORY.md`.
- Mark reconciliation status: `metadata_only`, `partially_mapped`, `unresolved`, `deferred`.
- Do not treat Notion as imported payload or plate identity authority pending deep mapping.

| Notion ID | Title | Relationship | Status |
|---|---|---|---|
| `NTN-VIS-001` | 11 Visual Language | Visual language area hub | Metadata only |
| `NTN-VIS-002` | Visual Canon Project hub | GFVP project hub | Metadata only |
| `NTN-VIS-003` | Issue 00: Charter | Source artifact candidate | Metadata only |
| `NTN-VIS-004` | Issue 02: Source Inventory | Source-location guide | Metadata only |
| `NTN-VIS-005` | Issue 03: Plate Taxonomy | Possible taxonomy authority | Unresolved vs roadmap — deferred |
| `NTN-REC-001` | Receipt mirror | P003 approval cross-ref | Partially mapped |
| `NTN-REC-002` | Receipt mirror | P009 ambiguity | Unresolved — deferred |
| `NTN-REC-003` | Receipt mirror | P006 output QC cross-ref | Partially mapped |

### 13. Open Questions and Deferred Decisions

Content rules:

- Carry forward **unratified** items from human review packet with decision IDs.
- List **deferred** ratification items explicitly:

| Topic | Status |
|---|---|
| Notion GFVP deep mapping | Deferred |
| `NTN-REC-002` P009 ambiguity | Deferred |
| Export zip location for PUB-002 | Deferred |
| PUB-002 release package import | Deferred |

- Unratified packet IDs still open: A4, C1–C4, D1/D2/D5–D8, E1–E3, F1/F2/F4.

### 14. Import Preconditions

Future manifest must end with explicit gates:

| # | Precondition | Status (2026-07-06) |
|---|---|---|
| 1 | Authority hierarchy for plate identity (A1) | **Ratified** |
| 2 | P002/P003 composite lock for source inventory (B1/B3) | **Ratified** |
| 3 | Approved plate count and legacy include set (A3, D3/D4) | **Partially ratified** — D1/D2/D5–D8 open |
| 4 | Next image-gate candidate (A6) | **Ratified** — planning only |
| 5 | Import receipt created and filed before any file copy | **Open** |
| 6 | `TG-SRC-PUB-002` remains out of scope | **Locked deferred** |
| 7 | Explicit migration authorization | **Not authorized** |

## Companion Root File: README.md

If migration is later approved, `06_visual_language/gfvp/README.md` should:

- Identify `TG-SRC-VIS-001` and link to `SOURCE_CLUSTER_MANIFEST.md`.
- State not-canon disclaimer and Drive-primary binary policy.
- Summarize import boundary vs. `TG-SRC-PUB-002` and ratified planning fields at high level.
- Not duplicate full inventory tables (point to manifest).

Design only; do not create until approved.

## Manifest Maintenance Rules

- Update manifest when Drive inventory changes; do not auto-sync from Drive.
- Version index rows change only on human-confirmed chain updates.
- Conflict IDs remain until explicitly resolved and marked in manifest.
- Ratified planning fields may not be changed without new human ratification.
- Manifest updates do not authorize re-import or canon promotion.

## Anti-Patterns for Manifest Authoring

- Using manifest as plate status registry (future `04_registries/` derivative is separate).
- Listing approved PNG paths as if import or publication verification were authorized.
- Treating pack review sheets or remediation reports as **primary** status authority over roadmap (A7).
- Elevating remediation vocabulary above roadmap plate identity (A7).
- Using batch manifest, legacy briefs, or stale count fields as current plate identity (A1, A2, D3/D4).
- Resolving AUTH-C6/C7/C10 or deferred Notion items without authorized review.
- Importing output QC/approval folders as active source workflow.
- Creating retrospective lock receipts to fill P002/P003 gaps without approval.
- Treating manifest approval, next-gate field, or approved count as migration/publication authorization.
- Treating `next_image_gate_candidate: P012` as authorization to generate or publish images (A6).

## ID Cross-Reference Index

| DRV ID | VIS ID | GFVP Reconciliation ID | Folder / Topic |
|---|---|---|---|
| `DRV-GFVP-012` | `VIS-001-013` | `GFVP-BIN-002` | `06_GENERATED_OUTPUTS/` |
| `DRV-GFVP-013` | `VIS-001-014` | `GFVP-REC-003` | `07_OUTPUT_QC/` |
| `DRV-GFVP-014` | `VIS-001-015` | `GFVP-BIN-001` | `08_APPROVED_OUTPUTS/` |
| `DRV-GFVP-015` | — | `GFVP-BIN-001` | Approved PNGs (11) |
| `DRV-GFVP-016` | — | `GFVP-BIN-002` | Generated PNGs (14) |
| `DRV-GFVP-017` | — | `GFVP-BIN-004` | Missing export zip |

Per-file IDs for large folders remain pattern-based (`VIS-001-026` through `VIS-001-030`).

## Relationship to Other Artifacts

| Artifact | Relationship |
|---|---|
| `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md` | Ratification source for header fields and Sections 3–4 |
| `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_REVIEW_DRAFT.md` | Prior design review; revision addresses R-01–R-07 |
| `TG_SRC_VIS_001_FILE_INVENTORY_DRAFT.md` | Detailed evidence; manifest summarizes |
| `TG_SRC_VIS_001_AUTHORITY_HIERARCHY_DRAFT.md` | Authority source; manifest embeds ratified subset |
| `TG_SRC_VIS_001_VERSION_LOCK_REVIEW_DRAFT.md` | Version/lock source; manifest embeds index |
| `TG_SRC_VIS_001_DESTINATION_STRUCTURE_DRAFT.md` | Folder mapping; manifest cites subpaths |
| `SOURCE_TO_DESTINATION_MAP_DRAFT.md` | Cluster-level map; manifest is cluster-specific |
| `10_inventories/DRIVE_INVENTORY.md` | Drive-wide inventory; manifest is VIS-001 scoped |

## Review Checklist for This Design

- [x] Ratified A1 roadmap plate identity reflected
- [x] Ratified A3 approved count 11 / P001–P011 reflected
- [x] Ratified A6 P012 next-gate section with no-action disclaimers
- [x] Ratified A7 remediation historical/secondary; no pack override
- [x] Ratified A2/D3/D4 historical legacy treatment
- [x] Ratified B1/B3 composite lock (source inventory only)
- [x] Required header fields present
- [x] PUB-002 boundary explicit
- [ ] Full P002–P011 version index (pending C1–C2 if needed)
- [ ] Unratified include/exclude IDs D1/D2/D5–D8
- [ ] Design re-review before manifest content drafting

## Recommended Next Gate

1. Re-review design against `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_REVIEW_DRAFT.md` (or update review note).
2. If accepted, authorize drafting `SOURCE_CLUSTER_MANIFEST.md` **content** as repo proposal only — still no file move or import.
3. Create import receipt draft before any copy operation.
4. Keep `TG-SRC-PUB-002` deferred.

Do not populate `06_visual_language/gfvp/` until migration is explicitly authorized.

## Output Summary

What changed:

- Revised design (2026-07-06) to align with human ratification bundle.
- Added header ratified planning fields and field definitions table.
- Added Section 4 Production Status and Next Gate (A3, A6).
- Added Section 5 Plate Identity Map (roadmap-derived, A1).
- Rewrote Section 3 authority hierarchy with A7 secondary tier and anti-override rule.
- Updated Section 2 import table — D3/D4 confirmed Yes with historical notes.
- Renumbered sections 5–14; updated import preconditions with ratification status.
- Expanded anti-patterns for pack override and A6 non-authorization.

What should be locked:

- Design only; no `SOURCE_CLUSTER_MANIFEST.md` file creation yet.
- Ratified planning fields in header block (planning scope only).
- `TG-SRC-PUB-002` remains deferred.
- No migration, extraction, movement, external edits, app/RPC work, or commits authorized.

What remains living:

- Design re-review and manifest content drafting authorization.
- Unratified decisions: A4, C1–C4, D1/D2/D5–D8, E1–E3, F1/F2/F4.
- Deferred: Notion mapping, P009 ambiguity, export zip, PUB-002 release import.
- Full P002–P011 version index extension.

Concrete next steps:

1. Re-check design review or note revision applied.
2. Authorize manifest content drafting if design accepted — still no import.
3. Do not commit unless separately approved.
