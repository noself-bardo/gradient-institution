# Drive Inventory

Status: DRAFT / AGENT-ASSISTED GFVP RECONCILIATION PASS

Authority: Not canonical

Constraint: This inventory does not authorize migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work.

Drive root inspected:

`C:\Users\steve\My Drive\The Gradient`

GFVP package root inspected:

`C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01`

Drive is asset and package storage. It is not the live Git working directory and should not become the canonical repo.

No Drive files were edited, moved, renamed, deleted, copied, or migrated.

## Agent-Assisted Inventory Scope

Four read-only Cursor subagents gathered evidence:

- Agent 1: GFVP Source System Inventory.
- Agent 2: GFVP Publication/Export Inventory.
- Agent 3: GFVP Receipts/QC/Review Inventory.
- Agent 4: Duplicate/Mirror Audit.
- Follow-up reconciliation agents: GFVP Binary Locator, GFVP Receipt Mapper, and GFVP Authority Mapper.

Allowed agent scope was evidence gathering and classification only. Agents did not make final placement decisions.

## Top-Level Findings

- The GFVP batch package is present under `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01`.
- The GFVP batch package contains approximately 283 markdown/CSV files in the accessible synced tree.
- No image binaries were found inside the accessible synced GFVP batch package.
- No GFVP `.png`, `.zip`, or `.pdf` release/export binaries were found in the accessible synced Drive search performed by the agents.
- Approved/generated image files are documented by receipts and handoffs but were not present as local synced binaries.
- The repo contains planning/inventory metadata only; no GFVP source payloads were found in the migration workspace.
- `GFVP_RECEIPT_BINARY_AUTHORITY_RECONCILIATION_DRAFT.md` records the current receipt-to-binary and authority reconciliation.

## GFVP Subareas Observed

- `00_README/`
- `01_SOURCES/`
- `02_PLATE_BRIEFS/`
- `03_PROMPT_PACKETS/`
- `04_PREFLIGHT_QC/`
- `05_LOCKED_PROMPTS/`
- `06_GENERATED_OUTPUTS/`
- `07_OUTPUT_QC/`
- `08_APPROVED_OUTPUTS/`
- `09_HANDOFFS/`
- `10_ADMISSION_RECOMMENDATIONS/`
- `11_OBJECT_SPECIFICATIONS/`
- `12_COMPILER_PROMPTS/`
- `13_ROADMAPS/`
- `99_ARCHIVE/`

## Consolidated GFVP Inventory Findings

Proposed destinations below align to `TG_SRC_VIS_001_DESTINATION_STRUCTURE_DRAFT.md` (lifecycle-grouped under `06_visual_language/gfvp/`, not flat mirror).

Agent swarm verification (2026-07-06): **25 PNG files** present in synced Drive (`06_GENERATED_OUTPUTS/`: 14; `08_APPROVED_OUTPUTS/`: 11). GFVP zip/export package still not found locally.

| Inventory ID | Source System | Title / Filename | Location / Path / Link | File Type | Artifact Class | Related Source ID | Current Authority | Proposed Destination | Migration Action | Review Status | Risk Level | Duplicate / Mirror Notes | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `DRV-GFVP-001` | Google Drive / GFVP | GFVP Batch 01 package root | `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01` | Folder | Source-system root / package root | `TG-SRC-VIS-001`; `TG-SRC-PUB-002` for release/export subset | Drive storage; not repo canon | `06_visual_language/gfvp/`; release refs under `07_publishing/series/gfvp/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REQUIRES_SOURCE_INVENTORY` | Agent-assisted first pass | High | No repo mirror; Notion Visual Canon/GFVP pages may mirror context | Mixed source, control, receipt, and release metadata; keep cluster intact until approval. |
| `DRV-GFVP-002` | Google Drive / GFVP | Package README and lock receipt | `00_README/README.md`; `00_README/LOCK_RECEIPT.md` | Markdown | Package control / lock receipt | `TG-SRC-VIS-001` | Package README says not canon by default; text locks accepted by Steven per receipts | `06_visual_language/gfvp/package_control/00_README/`; receipt refs under `11_receipts/` | `REFERENCE_ONLY`; `IMPORT_SOURCE_CLUSTER_LATER` | Reviewed by agents | High | README status differs from roadmap on approved plate count | Locks text/process boundaries; does not authorize image generation or canon promotion. |
| `DRV-GFVP-003` | Google Drive / GFVP | Batch manifest | `01_SOURCES/BATCH_01_MANIFEST.md` | Markdown | Source manifest / plate index | `TG-SRC-VIS-001` | Draft/stale relative to 40-plate roadmap | `06_visual_language/gfvp/package_control/01_SOURCES/` | `REQUIRES_SOURCE_INVENTORY` | Authority conflict identified | High | Stale 8-plate index conflicts with locked 40-plate roadmap | Do not treat as current production authority without lineage mapping. |
| `DRV-GFVP-004` | Google Drive / GFVP | Plate briefs P001-P008 | `02_PLATE_BRIEFS/` | Markdown folder | Legacy plate brief source | `TG-SRC-VIS-001` | Locked historically; superseded for generation by object-spec/compiler workflow | `06_visual_language/gfvp/legacy_workflow/plate_briefs/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REFERENCE_ONLY` | Locked / superseded | Medium | Semantic drift against later object specs | P003/P004 meanings diverge between early brief set and later atomic object specs. |
| `DRV-GFVP-005` | Google Drive / GFVP | Prompt packets P001-P008 | `03_PROMPT_PACKETS/` | Markdown folder | Legacy prompt packet | `TG-SRC-VIS-001` | Superseded by object-spec/compiler workflow | `06_visual_language/gfvp/legacy_workflow/legacy_prompt_packets/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REFERENCE_ONLY` | Superseded / historical | Medium | Intentional mirror with `05_LOCKED_PROMPTS/`; P001 spot-check identical | Preserve as historical; not active generation source. |
| `DRV-GFVP-006` | Google Drive / GFVP | Preflight QC | `04_PREFLIGHT_QC/` | Markdown folder | Preflight QC | `TG-SRC-VIS-001` | QC complete for legacy prompt phase | `06_visual_language/gfvp/legacy_workflow/qc/preflight/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REFERENCE_ONLY` | QC complete | Low | Legacy QC overlaps with later compiler QC | Includes summary, revision targets, second-pass QC, and per-plate QC. |
| `DRV-GFVP-007` | Google Drive / GFVP | Locked prompts (9 files) | `05_LOCKED_PROMPTS/` | Markdown folder | Locked prompt packet | `TG-SRC-VIS-001` | Locked historically; image gate closed | `06_visual_language/gfvp/legacy_workflow/legacy_locked_prompts/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REFERENCE_ONLY` | Locked / superseded | Medium | 8 prompts + `LOCK_RECEIPT_READY_FOR_IMAGE_GATE.md`; mirror with `03_PROMPT_PACKETS/` | Lock receipt does not open image gate. |
| `DRV-GFVP-008` | Google Drive / GFVP | Object specifications and object QC | `11_OBJECT_SPECIFICATIONS/` | Markdown folder | Object specifications / object QC / object lock receipts | `TG-SRC-VIS-001`; cross-refs `TG-SRC-KNO-001`, `TG-SRC-REG-001`, `TG-SRC-ARC-001` | Active sandbox source-of-truth for object workflow | `06_visual_language/gfvp/active_workflow/object_specifications/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REQUIRES_SOURCE_INVENTORY` | Mixed: approved P002-P011; text-ready P012-P039; P040 spec-only | High | P003 has multiple versions; P002/P003 standalone lock receipt gap | P001 has no object spec; P040 has spec/QC but no compiled prompt. |
| `DRV-GFVP-009` | Google Drive / GFVP | Compiler prompts and compiler QC | `12_COMPILER_PROMPTS/` | Markdown folder | Compiled prompt / compiler QC | `TG-SRC-VIS-001` | Derived compiler outputs from object specs | `06_visual_language/gfvp/active_workflow/compiler_prompts/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REQUIRES_SOURCE_INVENTORY` | Mixed by plate approval state | High | P003 and P007 keep multi-version chains | Do not treat compiler output as source without object-spec lineage. |
| `DRV-GFVP-010` | Google Drive / GFVP | Roadmaps, production protocol, pack receipts | `13_ROADMAPS/` | Markdown/CSV folder | Roadmap / production protocol / review sheets / text receipts | `TG-SRC-VIS-001`; release references to `TG-SRC-PUB-002` | 40-plate roadmap locked; pack statuses vary | `06_visual_language/gfvp/roadmaps/`; receipt refs under `11_receipts/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REFERENCE_ONLY` | Roadmap locked; Pack B-F human review pending | High | Markdown and CSV roadmap mirror; pack receipts overlap handoffs | Includes `GFVP_40_PLATE_ROADMAP_v0-1.md`, `.csv`, production protocol, roadmap lock, Pack A text lock, Pack B-F records. |
| `DRV-GFVP-011` | Google Drive / GFVP | Handoffs and remediation logs | `09_HANDOFFS/` | Markdown folder | Handoff / remediation / completion report | `TG-SRC-VIS-001` | Codex handoff and remediation evidence | `06_visual_language/gfvp/production_evidence/handoffs/`; receipt refs under `11_receipts/` | `IMPORT_SOURCE_CLUSTER_LATER`; `REFERENCE_ONLY` | Handoff/remediation complete for available docs | Medium | Pack remediation overlaps roadmap review sheets | Includes P012-P040 manifest and completion/remediation reports. |
| `DRV-GFVP-012` | Google Drive / GFVP | Generated output receipts + PNGs | `06_GENERATED_OUTPUTS/` | Markdown + PNG folder | Generation receipts / generated output metadata | `TG-SRC-PUB-002`; references `TG-SRC-VIS-001` | Receipts document generated candidates; 14 PNGs present in sync | Drive remains binary home; metadata refs under `11_receipts/` | `REFERENCE_ONLY`; `REQUIRES_SOURCE_INVENTORY` | Receipts + PNGs present | High | 10 md + 14 png | Deferred TG-SRC-PUB-002; do not co-import with VIS-001. |
| `DRV-GFVP-013` | Google Drive / GFVP | Output QC reports | `07_OUTPUT_QC/` | Markdown folder | Output QC record | `TG-SRC-PUB-002`; authority reference for `TG-SRC-VIS-001` | QC evidence for generated plates | Reference only; not source payload | `REFERENCE_ONLY`; `REQUIRES_SOURCE_INVENTORY` | QC complete for P001-P011 per agents | Medium | P003/P007 have versioned QC chains; Notion QC may mirror | Authority reference only; not co-imported as VIS-001 payload. |
| `DRV-GFVP-014` | Google Drive / GFVP | Approved output receipts + PNGs | `08_APPROVED_OUTPUTS/` | Markdown + PNG folder | Approval receipt cluster | `TG-SRC-PUB-002`; references `TG-SRC-VIS-001` | P001-P011 approvals documented; 11 PNGs present in sync | `11_receipts/` references; binaries remain in Drive | `REFERENCE_ONLY`; `REQUIRES_SOURCE_INVENTORY` | Approval receipts + PNGs present | High | Notion receipt pages may mirror selected approvals | Deferred TG-SRC-PUB-002; do not co-import with VIS-001. |
| `DRV-GFVP-015` | Google Drive / GFVP | Approved plate PNG set P001-P011 | `08_APPROVED_OUTPUTS/*.png` | PNG | Approved visual output / release asset | `TG-SRC-PUB-002` | Documentarily approved; 11 PNGs in synced Drive | Remain in Drive; lightweight repo manifest under `07_publishing/series/gfvp/` later | `REFERENCE_ONLY`; deferred import | PNGs present in sync | Medium | Previously reported absent; swarm re-verified present | Import still deferred and unauthorized. |
| `DRV-GFVP-016` | Google Drive / GFVP | Generated candidate PNG set | `06_GENERATED_OUTPUTS/*.png` | PNG | Generated candidate output | `TG-SRC-PUB-002` | Generated candidate status | Remain in Drive | `REFERENCE_ONLY`; deferred import | PNGs present in sync | Medium | 14 PNGs including P003/P007 version chains | Import still deferred and unauthorized. |
| `DRV-GFVP-017` | Google Drive / GFVP | GFVP package ZIP | Referenced as `gradient_foundational_visual_package_batch_01.zip`; not found locally | ZIP | Export package | `TG-SRC-PUB-002` | Unknown | Remain in Drive if located | `REQUIRES_SOURCE_INVENTORY` | Not found | High | No synced Drive/Projects zip found by agents | Referenced by package workflow, but local path not verified. |
| `DRV-GFVP-018` | Google Drive / GFVP | Archive / failure / IDR materials | `99_ARCHIVE/` | Markdown folder | Archive / failure-mode / revision log / doctrine | `TG-SRC-VIS-001`; possible `12_archive_refs/` references | Historical sandbox evidence | `06_visual_language/gfvp/archive/` or `12_archive_refs/` reference | `REFERENCE_ONLY` | Archived / accepted/rejected mixed | Medium | Failure archive placement unresolved | Includes meta-conversation drift failure and IDR-007 doctrine. |
| `DRV-GFVP-019` | Google Drive / GFVP | Admission recommendation folder | `10_ADMISSION_RECOMMENDATIONS/` | Empty folder | Planned admission recommendations | `TG-SRC-VIS-001` | Empty/not started | TBD | `NO_ACTION` | Empty | Low | None | No admission recommendations were observed. |
| `DRV-GFVP-020` | Notion + Drive | GFVP Notion receipt/QC mirrors | Notion rows `NTN-REC-001`-`NTN-REC-003`; Drive `07_OUTPUT_QC/`, `08_APPROVED_OUTPUTS/`, `13_ROADMAPS/` | Notion pages + markdown | Cross-system receipt/QC mirror | `TG-SRC-VIS-001`; `TG-SRC-PUB-002` | Unmapped evidence across systems | `11_receipts/` references | `REFERENCE_ONLY`; `REQUIRES_SOURCE_INVENTORY` | Notion metadata only; Drive receipts present | High | Notion-to-Drive mapping incomplete | Need mapping before treating receipt trail as complete. |
| `DRV-GFVP-021` | Drive / adjacent visual lineage | Crisis Liturgies release/report duplicates | `05_IMAGERY/`, `09_RELEASES/`, root lock matrix under Drive root | Markdown | Adjacent visual release evidence | Candidate future source ID; not GFVP | Out of GFVP scope | `12_archive_refs/` or `07_publishing/` later | `REFERENCE_ONLY` | Sampled by duplicate audit | Medium | Cross-folder duplicates in Drive, not GFVP package | P001 QC cites Crisis Liturgy visual inheritance; not a GFVP release package. |

## Plate Coverage Snapshot

| Plate Range | Object Spec | Compiler Prompt | Output Approved | Notes |
|---|---|---|---|---|
| P001 | No | No | Yes, per staged-run approval receipt | Legacy prompt workflow only. |
| P002-P011 | Yes | Yes | Yes, per receipts/roadmap/handoff | Approved outputs documented; binaries missing locally. |
| P012-P015 | Yes | Yes | No | Pack A text locked; images not approved. |
| P016-P039 | Yes | Yes | No | Level A remediated; human review pending. |
| P040 | Spec and QC only | No | No | Image gate blocked until P001-P039 approved or waived. |

## Duplicate / Mirror Findings

- No local GFVP package mirror was found in the migration repo; repo contains planning/control docs only.
- `03_PROMPT_PACKETS/` and `05_LOCKED_PROMPTS/` are intentional legacy prompt/locked-prompt mirrors.
- Early `02_PLATE_BRIEFS/` and later `11_OBJECT_SPECIFICATIONS/` form a supersession chain and should not be conflated.
- `01_SOURCES/BATCH_01_MANIFEST.md` appears stale relative to `13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.md`.
- P003 and P007 retain multi-version chains that require authority/version mapping before import.
- `GFVP_40_PLATE_ROADMAP_v0-1.md` and `.csv` are format mirrors.
- Generated/approved output receipts reference PNG binaries that were not found in the accessible synced local Drive tree.
- Notion GFVP receipt pages and Drive markdown receipts may represent parallel evidence for the same events, but mapping is unresolved.
- No GFVP release folder or zip was found under accessible Drive or Projects paths.

## Publishing Constitution Finding

No obvious Drive file was found by earlier filename searches for `Publishing`.

The Notion metadata pass identified the Publishing Constitution source cluster pages. If a Drive/source export exists, it remains unlocated.

## Current Blockers Before Migration Candidate Selection

- Approved/generated GFVP PNG binaries are documented but not found in synced local Drive.
- GFVP package ZIP/export package is referenced but not found locally.
- Notion-to-Drive receipt/QC mapping is incomplete.
- `NTN-REC-001` maps to P003 approval and `NTN-REC-003` maps to P006 output QC; `NTN-REC-002` for P009 remains ambiguous between output approval and object/source lock evidence.
- `BATCH_01_MANIFEST.md` and the locked 40-plate roadmap disagree on current production authority.
- P002/P003 appear approved/locked by roadmap/handoff but lack standalone object lock receipt files.
- README/roadmap/handoff appear to differ on approved plate count.
- P003/P007 version chains require explicit current-version mapping.
- Source-system and release/export package boundaries remain unresolved for import purposes.

## First-Pass Rules

- Do not move any Drive files.
- Do not rename package folders.
- Do not copy binaries into Git.
- Do not import generated outputs as source material.
- Do not treat receipt metadata as binary verification.
- Do not treat source clusters as canonical by default.
- Use selective checksums later for important zips, approved outputs, binaries, and release packages after they are located.

## Open Questions

- Where are approved GFVP image binaries stored?
- Where are generated/candidate GFVP PNGs stored?
- Where is `gradient_foundational_visual_package_batch_01.zip`, if it exists?
- Which receipt trail is authoritative when Notion and Drive both record an approval/QC event?
- Does `NTN-REC-002` represent P009 output approval, object/source lock, or another approval event?
- Which Drive folder contains GFVP release/export packages, if any?
- Is the whole GFVP batch folder the export unit, or is there a distinct release package folder?
- Which index governs current plate identity and status: `BATCH_01_MANIFEST.md`, the locked roadmap, Notion Issue 03, or a combination?
- Should P002/P003 receive retrospective lock receipts, or is roadmap/handoff evidence sufficient?
- Which GFVP assets are approved outputs versus source/control files?
- Where is Publishing Constitution v0.1 stored in Drive, if at all?
