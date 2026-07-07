# TG-SRC-VIS-001 File Inventory Draft

Status: DRAFT / READ-ONLY SOURCE INVENTORY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Constraint: This inventory does not authorize migration, extraction, source promotion, canon change, external edits, commits, app/RPC work, file moves, file renames, or folder restructuring.

## Scope

Source ID: `TG-SRC-VIS-001`

Source Cluster: GFVP source/spec/object/prompt/QC system

Drive source root:

`C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01`

Deferred:

- `TG-SRC-PUB-002`
- generated PNGs
- approved PNGs
- release/export packages
- missing zip packages
- unrelated local packages

## Inventory Summary

The read-only file inventory found 283 markdown/CSV files plus one empty folder in the synced GFVP batch package.

Agent swarm verification (read-only, 2026-07-06): **25 PNG files** are present in deferred release folders (`06_GENERATED_OUTPUTS/`: 14; `08_APPROVED_OUTPUTS/`: 11). No ZIP or PDF was found. PNGs remain **out of import scope** under `TG-SRC-PUB-002` until explicitly authorized.

| Folder | Files | Inventory Posture | Proposed Destination Under `06_visual_language/gfvp/` | Include in Migration Candidate? |
|---|---:|---|---|---|
| `00_README/` | 2 | Package control and lock receipt | `package_control/00_README/` | Yes |
| `01_SOURCES/` | 1 | Historical/stale batch manifest | `package_control/01_SOURCES/` | Maybe |
| `02_PLATE_BRIEFS/` | 8 | Legacy plate briefs | `legacy_workflow/plate_briefs/` | Maybe |
| `03_PROMPT_PACKETS/` | 8 | Legacy prompt packets | `legacy_workflow/legacy_prompt_packets/` | Maybe |
| `04_PREFLIGHT_QC/` | 11 | Legacy preflight QC | `legacy_workflow/qc/preflight/` | Yes |
| `05_LOCKED_PROMPTS/` | 9 | Legacy locked prompts and gate-readiness receipt | `legacy_workflow/legacy_locked_prompts/` | Yes / Maybe |
| `06_GENERATED_OUTPUTS/` | 10 | Generation receipt metadata for deferred outputs | Reference only | No |
| `07_OUTPUT_QC/` | 14 | Output QC metadata | Reference only or future receipt refs | Maybe |
| `08_APPROVED_OUTPUTS/` | 11 | Approval receipt metadata for deferred outputs | Reference only | No |
| `09_HANDOFFS/` | 8 | Handoffs/remediation/completion reports | `production_evidence/handoffs/` | Yes |
| `10_ADMISSION_RECOMMENDATIONS/` | 0 | Empty planned slot | Omit until populated | No |
| `11_OBJECT_SPECIFICATIONS/` | 93 | Active object-specification workflow | `active_workflow/object_specifications/` | Yes / Maybe |
| `12_COMPILER_PROMPTS/` | 85 | Active compiler-prompt workflow | `active_workflow/compiler_prompts/` | Yes / Maybe |
| `13_ROADMAPS/` | 19 | Roadmap, protocol, review sheets, receipts | `roadmaps/` | Yes |
| `99_ARCHIVE/` | 4 | Archive/failure/revision/IDR records | `archive/` | Yes / Maybe |

## File Inventory Classification

| Inventory Item ID | Source ID | File Path / Source Location | Filename | File Class | Authority Role | Version / Status | Proposed Destination Under `06_visual_language/gfvp/` | Include in Migration Candidate? | Risk / Ambiguity | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `VIS-001-001` | `TG-SRC-VIS-001` | `00_README/` | `README.md` | Package orientation | Package control / boundary document | v0.1; operational status; not canon | `package_control/00_README/` | Yes | High | Contains useful boundary language but has approved-count drift. |
| `VIS-001-002` | `TG-SRC-VIS-001` | `00_README/` | `LOCK_RECEIPT.md` | Lock receipt | Legacy text/process lock | Locked; image gate closed | `package_control/00_README/` | Yes | High | Locks the legacy prompt phase only. |
| `VIS-001-003` | `TG-SRC-VIS-001` | `01_SOURCES/` | `BATCH_01_MANIFEST.md` | Manifest | Historical 8-plate index | v0.1; stale vs roadmap | `package_control/01_SOURCES/` | Maybe | High | Treat as historical unless human confirms otherwise. |
| `VIS-001-004` | `TG-SRC-VIS-001` | `02_PLATE_BRIEFS/` | P001-P008 plate briefs | Plate briefs | Legacy source/orientation | Locked historically; superseded | `legacy_workflow/plate_briefs/` | Maybe | Medium | P003/P004 semantics diverge from atomic roadmap. |
| `VIS-001-005` | `TG-SRC-VIS-001` | `03_PROMPT_PACKETS/` | P001-P008 prompt packets | Prompt packets | Legacy broad prompts | Superseded | `legacy_workflow/legacy_prompt_packets/` | Maybe | Medium | Mirror/supersession relationship with locked prompts. |
| `VIS-001-006` | `TG-SRC-VIS-001` | `04_PREFLIGHT_QC/` | 11 preflight QC files | Preflight QC | Legacy QC evidence | Complete | `legacy_workflow/qc/preflight/` | Yes | Low | Applies to legacy prompt workflow. |
| `VIS-001-007` | `TG-SRC-VIS-001` | `05_LOCKED_PROMPTS/` | P001-P008 locked prompts plus lock receipt | Locked prompts | Legacy locked prompt set | Locked; superseded for generation | `legacy_workflow/legacy_locked_prompts/` | Yes / Maybe | Medium | Keep as historical locked source, not active generation source. |
| `VIS-001-008` | `TG-SRC-VIS-001` | `09_HANDOFFS/` | 8 handoff/remediation files | Handoff/control | Completion, remediation, and handoff evidence | Filled / prepared | `production_evidence/handoffs/` | Yes | Medium | Important chronology but not sole status authority. |
| `VIS-001-009` | `TG-SRC-VIS-001` | `11_OBJECT_SPECIFICATIONS/` | `README.md`, schema, doctrine, P002-P040 specs/QC/locks | Object specifications | Active object-spec source system | Mixed approved/text-ready/spec-only | `active_workflow/object_specifications/` | Yes / Maybe | High | P001 absent; P002/P003 lock pattern differs; P003 multi-version chain. |
| `VIS-001-010` | `TG-SRC-VIS-001` | `12_COMPILER_PROMPTS/` | Compiler prompts/QC for P002-P039 | Compiler prompts | Derived compiler outputs from object specs | Mixed; P003/P007 version chains | `active_workflow/compiler_prompts/` | Yes / Maybe | High | P040 has no compiled prompt; P003/P007 superseded versions need explicit marking. |
| `VIS-001-011` | `TG-SRC-VIS-001` | `13_ROADMAPS/` | Roadmap, protocol, pack review sheets, text receipts | Roadmap/protocol/receipts | Scope, status, production workflow | Roadmap locked; pack status mixed | `roadmaps/` | Yes | High | Strongest current scope/status evidence, but count fields drift across docs. |
| `VIS-001-012` | `TG-SRC-VIS-001` | `99_ARCHIVE/` | IDR, failure mode, revision logs | Archive | Failure, doctrine, version lineage | Mixed archived/accepted/rejected | `archive/` | Yes / Maybe | Medium | P003 revision log is important for version chain. |
| `VIS-001-013` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/` | P002-P011 generation receipts | Generation receipt metadata | Release/export lineage evidence | Receipts only; binaries absent | Reference only | No | Critical for PUB-002 | Deferred with release/export cluster. |
| `VIS-001-014` | `TG-SRC-PUB-002` | `07_OUTPUT_QC/` | P001-P011 output QC files | Output QC metadata | Output verification evidence | Metadata only; binaries absent | Reference only or future receipt refs | Maybe | High | Useful for authority review, not source-system payload by default. |
| `VIS-001-015` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/` | P001-P011 approval receipts | Approval receipt metadata | Output approval evidence | Receipts only; approved PNGs absent | Reference only | No | Critical for PUB-002 | Deferred until binaries/export package are located or manually confirmed. |
| `VIS-001-016` | `TG-SRC-VIS-001` | `10_ADMISSION_RECOMMENDATIONS/` | Empty folder | Empty planned slot | None | Empty | Omit until populated | No | Low | Do not create an empty repo mirror unless later approved. |
| `VIS-001-017` | `TG-SRC-VIS-001` | `11_OBJECT_SPECIFICATIONS/` | `GFVP_OBJECT_SCHEMA_v0-1.md` | Object schema | Structural spec template | v0-1 | `active_workflow/object_specifications/` | Yes | Medium | Governs all object specs. |
| `VIS-001-018` | `TG-SRC-VIS-001` | `11_OBJECT_SPECIFICATIONS/` | `GFVP_ORIENTATION_DOCTRINE_GATE_BOUNDARY_PLATES_v0-1.md` | Orientation doctrine | Gate/boundary plate rules | v0-1 | `active_workflow/object_specifications/` | Yes | Medium | Gate/boundary doctrine. |
| `VIS-001-019` | `TG-SRC-VIS-001` | `12_COMPILER_PROMPTS/` | `GFVP_IMAGE_PROMPT_COMPILER_v0-1.md` | Compiler doctrine | Active compiler specification | v0-1 | `active_workflow/compiler_prompts/` | Yes | High | Critical control file. |
| `VIS-001-020` | `TG-SRC-VIS-001` | `13_ROADMAPS/` | `GFVP_40_PLATE_ROADMAP_v0-1.csv` | Roadmap table | Machine-readable plate index | v0-1 | `roadmaps/` | Yes | Medium | Format mirror of MD roadmap. |
| `VIS-001-021` | `TG-SRC-VIS-001` | `05_LOCKED_PROMPTS/` | `LOCK_RECEIPT_READY_FOR_IMAGE_GATE.md` | Lock receipt | Legacy image-gate readiness | Locked | `legacy_workflow/legacy_locked_prompts/` | Yes | Medium | Distinct from `00_README/LOCK_RECEIPT.md`. |
| `VIS-001-022` | `TG-SRC-VIS-001` | `11_OBJECT_SPECIFICATIONS/` | `GFVP-OBJ-P009-SOURCE_SELECTION_LOCK_RECEIPT.md` | Selection lock receipt | P009 source-selection lock | Locked | `active_workflow/object_specifications/` | Yes | Medium | Selection-lock subtype. |
| `VIS-001-023` | `TG-SRC-VIS-001` | `11_OBJECT_SPECIFICATIONS/` | `GFVP-OBJ-P010-HISTORY_SELECTION_LOCK_RECEIPT.md` | Selection lock receipt | P010 history-selection lock | Locked | `active_workflow/object_specifications/` | Yes | Medium | Selection-lock subtype. |
| `VIS-001-024` | `TG-SRC-VIS-001` | `13_ROADMAPS/` | `GFVP_PACK_A_TEXT_LOCK_RECEIPT.md` | Pack text lock | P011–P015 text lock | Locked | `roadmaps/` | Yes | Medium | Image-gate section may be stale (AUTH-C11). |
| `VIS-001-025` | `TG-SRC-VIS-001` | `13_ROADMAPS/` | `GFVP_P012_P040_BATCH_COMPLETION_PROMPT.md` | Batch completion prompt | P012–P040 text completion instruction | v1-0 | `roadmaps/` | Yes | Low | Operational prompt. |

## Duplicate / Mirror Rules

| Mirror Pair | Rule |
|---|---|
| `GFVP_40_PLATE_ROADMAP_v0-1.md` ↔ `.csv` | Import both; treat MD as primary authority; CSV is format mirror. |
| `03_PROMPT_PACKETS/` ↔ `05_LOCKED_PROMPTS/` | Import both under `legacy_workflow/` as historical; neither is active generation source. |
| `02_PLATE_BRIEFS/` → `11_OBJECT_SPECIFICATIONS/` | Legacy superseded; preserve for lineage. |
| `01_SOURCES/BATCH_01_MANIFEST.md` → 40-plate roadmap | Historical/superseded unless human overrides. |
| Notion `NTN-REC-*` ↔ Drive receipt folders | Reference only until Notion mapping authorized. |

## Sub-Count Breakdown (Verified)

| Folder | Sub-class | Count |
|---|---|---:|
| `11_OBJECT_SPECIFICATIONS/` | Control docs (README, schema, orientation) | 3 |
| `11_OBJECT_SPECIFICATIONS/` | Plate specs P002–P040 | 40 |
| `11_OBJECT_SPECIFICATIONS/` | Object QC | 40 |
| `11_OBJECT_SPECIFICATIONS/` | Standard lock receipts P004–P011 | 8 |
| `11_OBJECT_SPECIFICATIONS/` | Selection lock receipts P009, P010 | 2 |
| `12_COMPILER_PROMPTS/` | Compiler doctrine | 1 |
| `12_COMPILER_PROMPTS/` | Compiled prompts P002–P039 | 41 |
| `12_COMPILER_PROMPTS/` | Compiler QC | 43 |
| `12_COMPILER_PROMPTS/` | P040 compiler | 0 |

## File-Level Appendix (Complete Enumeration)

Agent swarm verified all 283 md/csv files. Full lists for folders ≤19 files:

### `00_README/` (2)
`README.md`, `LOCK_RECEIPT.md`

### `01_SOURCES/` (1)
`BATCH_01_MANIFEST.md`

### `02_PLATE_BRIEFS/` (8)
`P001_identity_constitutional-knowledge-ecology.md` through `P008_implementation_servant-layer.md`

### `03_PROMPT_PACKETS/` (8)
`P001_*_prompt.md` through `P008_*_prompt.md`

### `04_PREFLIGHT_QC/` (11)
`BATCH_01_PREFLIGHT_QC_SUMMARY.md`, P001–P008 per-plate QC, `REVISION_TARGETS_P006_P008.md`, `SECOND_PASS_QC_P006_P008.md`

### `05_LOCKED_PROMPTS/` (9)
`LOCK_RECEIPT_READY_FOR_IMAGE_GATE.md`, P001–P008 locked prompts

### `09_HANDOFFS/` (8)
`GFVP_B01_HANDOFF.md`, `GFVP_CODEX_HANDOFF_FINISH_P012_P040.md`, Level A remediation log/completion, P012–P040 completion report and text manifest, Pack B remediation log/completion

### `13_ROADMAPS/` (19)
Roadmap md/csv, lock receipt, production protocol, P012–P040 batch completion prompt and QC protocol, Pack A–F review sheets and text production receipts, Pack A text lock receipt

### `99_ARCHIVE/` (4)
`FAILURE_MODE_META_CONVERSATION_DRIFT.md`, `IDR-007_ONE_PLATE_EQUALS_ONE_INSTITUTIONAL_OBJECT.md`, `REVISION_LOG_P003_SOURCE_REVIEW_v0-2.md`, `REVISION_LOG_P006_P008.md`

### Large folders (pattern inventory)

- **`11_OBJECT_SPECIFICATIONS/` (93):** `GFVP-OBJ-P{002-040}-*_v0-*.md`, matching `*_OBJECT_QC_*`, lock receipts P004–P011, selection locks P009/P010.
- **`12_COMPILER_PROMPTS/` (85):** `GFVP_IMAGE_PROMPT_COMPILER_v0-1.md` + P002–P039 compiled prompts/QC; P003 v0-1–v0-4 chain; P007 v0-1/v0-2 chain; no P040.
- **`07_OUTPUT_QC/` (14):** P001 approved; P003 v0-2/3/4 chain; P007 v0-1/2 chain; P002–P011 otherwise v0-1. Reference-only for authority; deferred co-import.
- **`06_GENERATED_OUTPUTS/` (10 md + 14 png):** P002–P011 generation receipts. **TG-SRC-PUB-002 — no import.**
- **`08_APPROVED_OUTPUTS/` (11 md + 11 png):** P001–P011 approval receipts. **TG-SRC-PUB-002 — no import.**

Per-file IDs for large folders follow pattern rows `VIS-001-026` through `VIS-001-030` in manifest design draft.

| Plate Range | Object Spec | Compiler Prompt | Output Approved | Inventory Note |
|---|---|---|---|---|
| P001 | No | No | Yes by receipt | Legacy prompt workflow only; release binary deferred. |
| P002-P011 | Yes | Yes | Yes by receipts/roadmap/handoff | Source-system evidence available; release binaries deferred. |
| P012-P015 | Yes | Yes | No | Pack A text locked; no image approval. |
| P016-P039 | Yes | Yes | No | Level A remediated; human review pending. |
| P040 | Spec and QC only | No | No | Image gate blocked until prior plates approved or waived. |

## Inventory Decision

Recommendation remains: `NEEDS_SOURCE_INVENTORY`

Before import, the source inventory must mark:

- Current authority hierarchy.
- Current P003/P007 version chains.
- P002/P003 composite lock evidence decision.
- Legacy prompt/brief supersession status.
- Which output QC/approval receipt metadata is reference-only.
- A do-not-import boundary for `TG-SRC-PUB-002`.

## Open Questions

- Should `BATCH_01_MANIFEST.md` be imported as historical package control or held out as stale?
- Should both prompt packets and locked prompts be preserved, or should one be treated as a mirror?
- Should output QC metadata be included with the source cluster or referenced from receipts only?
- How should P001 be represented without object spec/compiler workflow files?
- How should P040 be represented without compiler prompt/output material?
- Should empty `10_ADMISSION_RECOMMENDATIONS/` be omitted until populated?

## Output Summary

What changed:

- Agent swarm pass expanded inventory with control-file rows VIS-001-017 through VIS-001-025, mirror rules, sub-count breakdown, and file-level appendices.
- Corrected PNG finding: 25 PNGs present in synced Drive (deferred PUB-002); zip still missing.

What should be locked:

- This is planning-only.
- `TG-SRC-PUB-002` remains deferred.
- No file migration, extraction, movement, or source promotion is authorized.

What remains living:

- Exact import set.
- Historical/superseded treatment for legacy workflow materials.
- Output QC/receipt reference strategy.
- Human authority decisions listed above.
