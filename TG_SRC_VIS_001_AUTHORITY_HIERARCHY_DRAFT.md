# TG-SRC-VIS-001 Authority Hierarchy Draft

Status: DRAFT / AUTHORITY REVIEW ONLY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Constraint: This hierarchy does not authorize migration, extraction, source promotion, canon change, external edits, commits, app/RPC work, file moves, file renames, or folder restructuring.

## Scope

Source ID: `TG-SRC-VIS-001`

Source Cluster: GFVP source/spec/object/prompt/QC system

Deferred:

- `TG-SRC-PUB-002`
- approved/generated binaries
- release/export packages

## Draft Authority Hierarchy

This hierarchy is proposed for migration planning only and requires human review before any import.

### Tier 0: Migration-Control Context

| Priority | Source | Role |
|---:|---|---|
| 0.1 | `SOURCE_OF_TRUTH_POLICY.md` | Migration-era source system rules. |
| 0.2 | `SOURCE_TO_DESTINATION_MAP_DRAFT.md` | Source ID and provisional destination mapping. |
| 0.3 | `FIRST_MIGRATION_CANDIDATE_REVIEW_TG_SRC_VIS_001.md` | Candidate status and `NEEDS_SOURCE_INVENTORY` recommendation. |
| 0.4 | Inventories and reconciliation drafts | Planning evidence only; not canonical authority. |

### Tier 1: GFVP Scope and Plate Identity

| Priority | File / Source | Defines | Notes |
|---:|---|---|---|
| 1 | `13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.md` | 40-plate atomic atlas, plate IDs, object names, families, production status | Strongest current Drive evidence. |
| 2 | `13_ROADMAPS/GFVP_40_PLATE_ROADMAP_LOCK_RECEIPT.md` | Scope-lock receipt | Count field may be stale; use for lock evidence, not counts until reconciled. |
| 3 | Notion `NTN-VIS-005` Plate Taxonomy | Possible locked sandbox taxonomy | Metadata-only; body not reconciled to roadmap. |
| Historical | `01_SOURCES/BATCH_01_MANIFEST.md` | Original 8-plate index | Stale relative to roadmap. |
| Historical | `02_PLATE_BRIEFS/` and README legacy plate list | Legacy broad plate meanings | Superseded by atomic object-spec workflow. |

### Tier 2: Plate Status

| Priority | File / Source | Defines | Notes |
|---:|---|---|---|
| 1 | Roadmap table | Per-plate status | Preferred status source pending human confirmation. |
| 2 | `08_APPROVED_OUTPUTS/*_APPROVAL_RECEIPT.md` | Visual output approval/lock metadata | Release binaries deferred; receipt metadata still useful. |
| 3 | `13_ROADMAPS/GFVP_PACK_*_REVIEW_SHEET_v0-1.md` | Pack text review state | Human review status remains living for B-F. |
| 4 | `13_ROADMAPS/GFVP_PACK_*_TEXT_PRODUCTION_RECEIPT.md` | Pack text production completion | Does not authorize image generation. |
| 5 | `09_HANDOFFS/` | Chronology and operational handoff evidence | Useful but not sole status authority. |
| Stale summary | `00_README/README.md` | Operational overview | Counts and legacy lists may lag. |

### Tier 3: Source Authority

| Priority | File / Source | Defines | Notes |
|---:|---|---|---|
| 1 | `11_OBJECT_SPECIFICATIONS/README.md` | Object spec as source of truth for generation | Core active workflow rule. |
| 2 | `11_OBJECT_SPECIFICATIONS/GFVP-OBJ-*.md` | Per-plate object definitions | Headers may lag downstream approval status. |
| 3 | External source citations inside object specs | Institutional source references | Not imported or promoted by this review. |
| 4 | Notion `NTN-VIS-004` Source Inventory | Possible source-location guide | Metadata-only. |
| Superseded | `03_PROMPT_PACKETS/`, `05_LOCKED_PROMPTS/`, `02_PLATE_BRIEFS/` | Legacy prompt/brief workflow | Preserve as historical if imported. |

### Tier 4: Production Protocol

| Priority | File / Source | Defines | Notes |
|---:|---|---|---|
| 1 | `13_ROADMAPS/GFVP_BATCH_PRODUCTION_PROTOCOL_v0-1.md` | Sandbox production workflow | Defines human-gated versus automatable stages. |
| 2 | `11_OBJECT_SPECIFICATIONS/README.md` | Object spec -> QC -> compile -> QC -> gate -> generate -> QC -> approve flow | Active workflow. |
| 3 | `13_ROADMAPS/GFVP_P012_P040_QC_PROTOCOL.md` | Text-completion QC | Applies to P012-P040 text substrate. |
| 4 | `09_HANDOFFS/GFVP_CODEX_HANDOFF_FINISH_P012_P040.md` | Text-only handoff scope | Does not authorize release/import. |

### Tier 5: Lock Status

| Lock Type | Primary Evidence | Notes |
|---|---|---|
| Roadmap scope lock | `GFVP_40_PLATE_ROADMAP_LOCK_RECEIPT.md` | Locks scope/sequence, not all outputs. |
| Legacy text automation lock | `00_README/LOCK_RECEIPT.md` | Original 8-plate prompt era only. |
| Object/prompt-ready lock | `11_OBJECT_SPECIFICATIONS/*_LOCK_RECEIPT.md` | Present for P004-P011 pattern; P002/P003 gap. |
| Visual output lock | `08_APPROVED_OUTPUTS/*_APPROVAL_RECEIPT.md` | Receipt metadata only; binaries deferred. |
| Pack text lock | `GFVP_PACK_A_TEXT_LOCK_RECEIPT.md` | P011-P015 text lock only. |
| Composite lock | Approval + output QC + handoff + roadmap | Proposed for P002/P003, pending human decision. |

## Conflict Table

| Conflict ID | Domain | Source A | Source B | Conflict | Severity | Proposed Handling |
|---|---|---|---|---|---|---|
| `AUTH-C1` | Scope / plate index | `BATCH_01_MANIFEST.md` | `GFVP_40_PLATE_ROADMAP_v0-1.md` | 8-plate legacy index vs 40-plate atomic atlas | High | Treat manifest as historical unless human overrides. |
| `AUTH-C2` | Plate identity | README legacy plate list / plate briefs | Roadmap / object specs | P003/P004/P007 meanings diverge | High | Use roadmap/object specs for current identity; preserve legacy as history. |
| `AUTH-C3` | Approved count | README / some receipts | Roadmap / handoff / P011 approval | Count drift: 10 vs 11 approved | Medium | Human confirm 11 and mark stale counts. |
| `AUTH-C4` | Object spec status | P002/P003 spec headers | Downstream approval receipts | Spec headers appear stale | Medium | Do not infer lock status from headers alone. |
| `AUTH-C5` | Lock pattern | P004-P011 standalone object locks | P002/P003 composite evidence | Process inconsistency | Medium | Human decide if composite evidence suffices. |
| `AUTH-C6` | Notion vs Drive receipts | `NTN-REC-*` metadata | Drive receipt files | Partial mapping only | High | Keep as unresolved until deeper mapping. |
| `AUTH-C7` | P009 Notion receipt | `NTN-REC-002` | P009 output/object/source lock files | Ambiguous event type | Medium | Requires later Notion page review. |
| `AUTH-C8` | Receipt vs binary proof | Approval/generation receipts | Missing local PNGs | Receipt metadata without binary verification | Critical for `TG-SRC-PUB-002` | Keep release/export deferred. |
| `AUTH-C9` | Pack B-F status | Roadmap table | Pack review sheets/production receipts | Remediated/human-review state not fully reflected | Medium | Human review before status registry. |
| `AUTH-C10` | Notion taxonomy | `NTN-VIS-005` metadata | Drive roadmap | Possible divergence unknown | High | Compare only after explicit deeper Notion review. |
| `AUTH-C11` | Next image-gate candidate | `GFVP_PACK_A_TEXT_LOCK_RECEIPT.md` (P011) | README, handoff, roadmap, completion report (P012) | Pack A text lock names P011 as next gate; P011 already visually approved | High | Treat P012 as next candidate; mark pack gate line stale. |
| `AUTH-C12` | Internal count drift | Roadmap lock receipt count block | Roadmap body count block | Both dated 2026-07-04; lock receipt says 10 approved, body says 11 | Medium | Roadmap body overrides lock receipt count fields. |
| `AUTH-C13` | README/handoff self-contradiction | Summary "Approved: 10 plates" | Same-file P011 approved narrative | README and handoff document P011 complete but summary count lags | Medium | Use per-plate evidence over summary lines. |
| `AUTH-C14` | Remediation absent from roadmap | Roadmap P016–P039 status | Pack B–F review sheets + Level A remediation reports | Roadmap never uses "remediated"; pack sheets document Level A remediation | Medium | Elevate pack review sheets above roadmap for pack text status until reconciled. |
| `AUTH-C15` | Remediation timeline | Completion report 2026-07-04 | Pack B receipt/review 2026-07-05 | Completion report says Pack B ready for review; next day Pack B remediated | Medium | Treat remediation reports as superseding completion report for Pack B–F. |
| `AUTH-C16` | Manifest header stale | `BATCH_01_MANIFEST.md` header | Current production state | Header still references P006 image-gate review; P011 approved | High | Historical only unless human overrides. |

## Recommended Source-of-Truth Ordering

For `TG-SRC-VIS-001` planning:

1. `GFVP_40_PLATE_ROADMAP_v0-1.md` body and table for current plate identity/status, pending human confirmation.
2. Roadmap lock receipt for scope/sequence lock only — **ignore stale count fields** when they disagree with roadmap body (AUTH-C12).
3. `GFVP_BATCH_PRODUCTION_PROTOCOL_v0-1.md` for production process.
4. `11_OBJECT_SPECIFICATIONS/README.md` and per-plate object specs for source authority.
5. Per-plate evidence chains: object QC, compiler QC, output QC, approval receipts, handoffs.
6. Pack review sheets and text production receipts for pack-level text status — **above roadmap table for Pack B–F** until roadmap reflects Level A remediation (AUTH-C14/C15).
7. `09_HANDOFFS/` for chronology and operational context.
8. README for orientation, after checking against roadmap.
9. Batch manifest, plate briefs, prompt packets, and locked prompts as historical/superseded legacy workflow.
10. Notion GFVP pages as metadata/reference until source-location review is completed.

## Human Review Required Before Migration

- Ratify or revise this authority hierarchy.
- Confirm whether `BATCH_01_MANIFEST.md` is historical/superseded.
- Confirm approved plate count.
- Decide P002/P003 composite lock sufficiency.
- Decide stale object-spec header policy.
- Reconcile Notion `NTN-REC-002`.
- Confirm Notion plate taxonomy relationship to Drive roadmap.
- Confirm next image-gate candidate is P012 (AUTH-C11).
- Reconcile Pack B–F remediation status vocabulary (AUTH-C14/C15).
- Decide how receipts should be referenced from `11_receipts/`.

## Output Summary

What changed:

- Agent swarm pass added AUTH-C11 through AUTH-C16, refined source-of-truth ordering for count fields and Pack B–F remediation.

What should be locked:

- This hierarchy is planning-only.
- It does not make final institutional authority decisions.
- It does not authorize migration or canon promotion.

What remains living:

- Human authority ratification.
- Notion/Drive receipt model.
- P002/P003 lock evidence decision.
- Stale manifest/README treatment.
