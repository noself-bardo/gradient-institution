# GFVP Source Cluster Manifest

---
manifest_type: source_cluster
source_id: TG-SRC-VIS-001
source_cluster: GFVP source/spec/object/prompt/QC system
drive_root: gradient_foundational_visual_package_batch_01
provisional_destination: 06_visual_language/gfvp/
manifest_status: DRAFT / SOURCE CLUSTER MANIFEST
authority: NOT_CANONICAL
baseline_commit: f8aad4f2396cd92be7f53fa220c07797403f3dd4
migration_readiness: NEEDS_SOURCE_INVENTORY
migration_authorized: false
receipt_required_before_import: true

# Ratified planning fields (2026-07-06; planning only — not canon)
roadmap_plate_identity_authority: true
approved_plate_count: 11
approved_plate_range: P001-P011
next_image_gate_candidate: P012
remediation_vocabulary_role: historical_secondary
historical_manifest_treatment: stale manifest/count drift and legacy workflow are historical evidence, not current controlling authority
deferred_pub_002_boundary: true

deferred_source_ids:
  - TG-SRC-PUB-002
---

**Constraint:** This manifest does not authorize migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work.

**Ratification reference:** Human ratification bundle recorded 2026-07-06 in `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md`. When `roadmap_plate_identity_authority` is `true`, the controlling Drive document is `13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.md` (decision A1).

---

## 1. Source Cluster Scope

### In scope (planning index for `TG-SRC-VIS-001`)

- GFVP source/spec/object/prompt/QC system
- Manifests (`BATCH_01_MANIFEST.md`, roadmap lock receipts, this manifest)
- Source materials (`01_SOURCES/`, external citations in object specs)
- Plate briefs (`02_PLATE_BRIEFS/`) — historical legacy workflow
- Prompt packets (`03_PROMPT_PACKETS/`) — historical legacy workflow
- Locked prompts (`05_LOCKED_PROMPTS/`) — historical legacy workflow
- Preflight QC (`04_PREFLIGHT_QC/`)
- Output QC — **authority reference only** (`07_OUTPUT_QC/` receipt metadata; not release import)
- Object specifications (`11_OBJECT_SPECIFICATIONS/`)
- Compiler prompts (`12_COMPILER_PROMPTS/`)
- Roadmap / production protocol / review sheets (`13_ROADMAPS/`)
- Handoff and control docs (`09_HANDOFFS/`, `00_README/`)
- Relevant source-system lock and selection receipts (object locks, pack text locks, roadmap scope lock, legacy text lock)
- Archive lineage (`99_ARCHIVE/`)

### Out of scope (explicit exclusion)

- Approved/generated PNG binaries
- Release/export packages (zip, PDF, publication exports)
- Missing zip packages (GFVP export zip unlocated)
- Publication outputs under `TG-SRC-PUB-002`
- Unresolved binary claims (receipt metadata is not binary verification)
- Entire deferred cluster: **`TG-SRC-PUB-002`**

### Drive source root

`gradient_foundational_visual_package_batch_01`

Detailed file inventory evidence: `TG_SRC_VIS_001_FILE_INVENTORY_DRAFT.md` (283 markdown/CSV files inventoried read-only).

### Source inventory summary

Read-only inventory: **283** markdown/CSV files plus one empty folder. Agent swarm verification (2026-07-06): **25 PNG files** present in synced Drive (`06_GENERATED_OUTPUTS/`: 14; `08_APPROVED_OUTPUTS/`: 11). PNGs remain **out of import scope** under `TG-SRC-PUB-002`.

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

**D3/D4 ratified (2026-07-06):** Legacy workflow folders (`02`–`05`) and historical batch manifest (`01_SOURCES/`) are **included as historical evidence**, not current controlling authority. Import posture **Yes** applies only to future authorized migration — not authorized by this manifest.

---

## 2. Ratified Planning Fields

| Field | Value | Notes |
|---|---|---|
| `roadmap_plate_identity_authority` | `true` | Roadmap (`GFVP_40_PLATE_ROADMAP_v0-1.md`) controls plate identity for VIS-001 source inventory planning (A1). |
| `approved_plate_count` | `11` | Planning status only; does not authorize PUB-002 release import (A3). |
| `approved_plate_range` | `P001-P011` | Per-plate evidence required for version/lock detail beyond roadmap table. |
| `next_image_gate_candidate` | `P012` | Planning only; no image generation or publication action authorized (A6). |
| `remediation_vocabulary_role` | `historical_secondary` | Pack B–F remediation may inform interpretation; must not override roadmap plate identity (A7). |
| `historical_manifest_treatment` | stale manifest/count drift and legacy workflow are historical evidence, not current controlling authority | Batch manifest, README/handoff count drift, plate briefs, prompt packets, and locked prompts are historical (A2/D3/D4). |
| `deferred_pub_002_boundary` | `true` | PNGs, generation/approval folders, zip, and release exports remain out of VIS-001 import scope. |

---

## 3. Authority Hierarchy

Planning hierarchy for `TG-SRC-VIS-001` (not institutional canon). Lower tiers must not override ratified fields above without new human ratification.

| Priority | Authority | Role |
|---:|---|---|
| 1 | Human ratification record (`TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md`, 2026-07-06) | Binds planning decisions A1, A3, B1/B3, A6, A2/D3/D4, A7; does not authorize migration. |
| 2 | Roadmap for plate identity (`13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.md`) | Primary plate ID, object name, family, and roadmap-table status (A1). |
| 3 | This source cluster manifest | Planning index and migration-control derivative once drafted; **not canon**. |
| 4 | Object specs, compiler prompts, QC artifacts, approval receipts | Local per-plate status, version chains, and lock evidence within VIS-001 scope. |
| 5 | Pack review sheets, text production receipts, remediation vocabulary | Secondary historical context for pack B–F text production (A7); may inform interpretation only. |
| 6 | Stale manifest, README/handoff summary counts, legacy plate briefs | Historical evidence only; not current controlling authority (A2/D3/D4). |

**Anti-override rules:**

- Remediation vocabulary must not override roadmap plate identity.
- Receipt metadata must not be treated as binary or release verification.
- Composite lock for P002/P003 is accepted for source inventory only (B1/B3); not for PUB-002.

Supporting planning drafts: `TG_SRC_VIS_001_AUTHORITY_HIERARCHY_DRAFT.md`, `TG_SRC_VIS_001_VERSION_LOCK_REVIEW_DRAFT.md`.

---

## 4. File Class Taxonomy

| Class | Description | Typical Drive locations |
|---|---|---|
| `MANIFEST` | Package or batch index documents | `01_SOURCES/`, roadmap lock receipts, this file |
| `README_ORIENTATION` | Package boundary and operational overview | `00_README/` |
| `SOURCE_MATERIAL` | Institutional source citations and batch source index | `01_SOURCES/`, citations in object specs |
| `PLATE_BRIEF` | Legacy broad plate briefs | `02_PLATE_BRIEFS/` |
| `PROMPT_PACKET` | Legacy prompt packets | `03_PROMPT_PACKETS/` |
| `LOCKED_PROMPT` | Legacy locked prompt copies | `05_LOCKED_PROMPTS/` |
| `PREFLIGHT_QC` | Legacy preflight QC | `04_PREFLIGHT_QC/` |
| `OUTPUT_QC_REFERENCE` | Output QC metadata (reference only) | `07_OUTPUT_QC/` |
| `OBJECT_SPEC` | Active object specifications and object QC | `11_OBJECT_SPECIFICATIONS/` |
| `COMPILER_PROMPT` | Compiled prompts and compiler QC | `12_COMPILER_PROMPTS/` |
| `ROADMAP_PROTOCOL` | Roadmap, production protocol, pack docs | `13_ROADMAPS/` |
| `REVIEW_SHEET` | Pack review sheets and text review state | `13_ROADMAPS/GFVP_PACK_*` |
| `HANDOFF_CONTROL` | Handoffs, completion reports, remediation | `09_HANDOFFS/` |
| `SOURCE_SYSTEM_RECEIPT` | Lock, approval, generation receipts (metadata) | Object locks, `08_APPROVED_OUTPUTS/*.md`, pack locks |
| `DEFERRED_RECEIPT` | Receipts pointing at deferred binaries | `06_GENERATED_OUTPUTS/`, `08_APPROVED_OUTPUTS/` |
| `EXCLUDED_BINARY` | PNG and other binary outputs | `06_GENERATED_OUTPUTS/`, `08_APPROVED_OUTPUTS/` — **PUB-002** |
| `EXCLUDED_PUBLICATION_OUTPUT` | Zip, PDF, release/export packages | Unlocated zip; **PUB-002** |

---

## 5. Plate Identity Map

Derived from `GFVP_40_PLATE_ROADMAP_v0-1.md` (ratified A1). Approved planning range **P001–P011** (A3). Next image-gate candidate **P012** (A6).

### P001–P011 (approved planning range)

| Plate ID | Plate Name / Object | Planning Status | Current Version Evidence | Lock / Approval Evidence | Notes |
|---|---|---|---|---|---|
| P001 | The Gradient as Constitutional Knowledge Ecology | Approved / Locked (planning) | Roadmap; object-spec workflow anchor | Roadmap; approval receipt metadata (PUB-002 deferred) | Identity / system map; staged-run anchor. |
| P002 | Admission Gate | Approved / Locked (planning) | Object spec v0-1; compiler v0-1 chain | **Composite lock** (B1/B3); no standalone object lock receipt | Gate/boundary plate; process variance recorded. |
| P003 | Source Review | Approved / Locked (planning) | **spec v0-2 → compiler v0-4 → output QC v0-4 → approval v0-4** | **Composite lock** (B1/B3); `NTN-REC-001` mirror | Legacy brief meant Ecology of Memory; superseded. |
| P004 | Metabolization Boundary | Approved / Locked (planning) | Object spec v0-1 (exemplar pattern) | **Standalone object lock:** `GFVP-OBJ-P004-METABOLIZATION-BOUNDARY_LOCK_RECEIPT.md` | Exemplar for P004–P011 lock pattern. |
| P005 | Card | Approved / Locked (planning) | Object spec + compiler chain (index TBD) | Object lock receipt pattern (manifest population pending) | Human-facing knowledge object. |
| P006 | Claim | Approved / Locked (planning) | Object spec + compiler chain (index TBD) | Object lock receipt pattern (manifest population pending) | Internal reasoning atom. |
| P007 | Relationship | Approved / Locked (planning) | **spec v0-1 → compiler v0-2 → output QC v0-2 → approval v0-2** | Object lock v0-1 (predates v0-2 regen); approval receipt metadata | Legacy brief meant IDR; active identity = Relationship. |
| P008 | Evidence | Approved / Locked (planning) | Object spec + compiler chain (index TBD) | Object lock receipt pattern (manifest population pending) | Support / grounding plate. |
| P009 | Source | Approved / Locked (planning) | Object spec + compiler chain (index TBD) | Object/source lock files; **`NTN-REC-002` ambiguity deferred** | Origin / provenance plate. |
| P010 | History | Approved / Locked (planning) | Object spec + compiler chain (index TBD) | Object lock receipt pattern (manifest population pending) | Trace without authority. |
| P011 | Decision | Approved / Locked (planning) | Object spec + compiler chain (index TBD) | Object lock; pack A text lock context | Governance object; last plate in approved planning range. |

### P012 (next image-gate candidate — planning only)

| Plate ID | Plate Name / Object | Planning Status | Current Version Evidence | Lock / Approval Evidence | Notes |
|---|---|---|---|---|---|
| P012 | Institutional Decision Record | Image Gate Candidate | Text packet approved per roadmap; object-spec/QC substrate in progress | Pack A text lock names stale next-gate line; **P012 ratified as next candidate (A6)** | No image generation authorized by this manifest. |

P013–P040: see roadmap table in Drive; not in approved planning range P001–P011; full manifest rows deferred until version index populated.

---

## 6. Known Version Chains

Documented current chains (from `TG_SRC_VIS_001_VERSION_LOCK_REVIEW_DRAFT.md`):

| Plate | Current chain | Risk / notes |
|---|---|---|
| **P003** | object spec **v0-2** → compiler **v0-4** → output QC **v0-4** → approval **v0-4** | High — spans multiple version axes; no standalone object lock receipt; generation receipt stale vs v0-4. |
| **P007** | object spec **v0-1** → compiler **v0-2** → output QC **v0-2** → approval **v0-2** | Medium — object lock receipt predates v0-2 compiler/output regeneration. |

**P002–P011 version index:** Full per-plate version index for P001, P002, P004–P006, P008–P011 remains **to be populated** (decisions C1–C4 not ratified). This manifest records roadmap status and the two fully mapped chains only.

---

## 7. Lock / Approval Evidence

| Plate / pattern | Evidence model | Scope |
|---|---|---|
| **P002 / P003** | Composite lock accepted **for source inventory only** (B1/B3) | Approval + output QC + compiler QC + object spec/QC + roadmap + handoff; **not** binary/publication verification |
| **P004** | Standalone object lock receipt | `11_OBJECT_SPECIFICATIONS/GFVP-OBJ-P004-METABOLIZATION-BOUNDARY_LOCK_RECEIPT.md` — exemplar for P004–P011 pattern |
| **P005–P011** | Standalone object lock receipts (expected pattern) | Per-plate lock files require manifest population and review before import planning |
| **P002 / P003** | Process variance | Missing standalone object lock receipts; no retrospective receipts authorized in this phase |
| **P001, P005–P006, P008–P011** | Partially inventoried | Approval receipt metadata in `08_APPROVED_OUTPUTS/` (reference only); full chains not yet indexed |
| **Roadmap scope** | `GFVP_40_PLATE_ROADMAP_LOCK_RECEIPT.md` | Scope/sequence lock; ignore stale count fields when they disagree with roadmap body |
| **Legacy text era** | `00_README/LOCK_RECEIPT.md` | Original 8-plate prompt phase only — historical |

**Not authorized:** Using composite or receipt metadata as proof of PNG integrity, export completeness, or PUB-002 import readiness.

---

## 8. Deferred PUB-002 Boundary

| Item | Status |
|---|---|
| PNG binaries | **Excluded** from VIS-001 manifest import scope |
| Release/export packages | **Excluded**; belong to deferred **`TG-SRC-PUB-002`** review/import scope |
| PNG inventory (read-only sync) | **25 PNGs** present: 14 in `06_GENERATED_OUTPUTS/`, 11 in `08_APPROVED_OUTPUTS/` |
| GFVP zip | **Missing** / unlocated locally |
| Receipt metadata | Useful for authority reference; **is not binary verification** |
| Import authorization | **None** for PUB-002 or PNG import |

Generation and approval folders may be cited as `OUTPUT_QC_REFERENCE`, `DEFERRED_RECEIPT`, or `EXCLUDED_BINARY` classes only.

---

## 9. Proposed Destination Structure

Planning-only internal layout under `06_visual_language/gfvp/`. **No subfolders are created by this manifest.**

```text
06_visual_language/gfvp/
  README.md                          (future orientation — not yet present)
  SOURCE_CLUSTER_MANIFEST.md         (this file — planning index only)

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

Source folder mapping detail: `TG_SRC_VIS_001_DESTINATION_STRUCTURE_DRAFT.md`.

Functional reference destinations (not primary import targets): `11_receipts/`, `04_registries/`, `07_publishing/series/gfvp/` (PUB-002 deferred).

---

## 10. Notion Cross-Reference Index (Metadata Only)

From `10_inventories/NOTION_INVENTORY.md`. Notion page bodies are **not** imported payload or plate identity authority pending deep mapping authorization.

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

Deep Notion GFVP mapping remains **deferred**. Do not resolve `NTN-REC-002` P009 ambiguity from metadata alone.

---

## 11. Unresolved Decisions

Decisions not ratified in the 2026-07-06 bundle remain open for future human review (`TG_SRC_VIS_001_HUMAN_REVIEW_PACKET_DRAFT.md`):

| ID | Topic |
|---|---|
| **A4** | Accept or revise full authority ordering draft |
| **C1–C4** | P003/P007 chain representation in manifest; full P002–P011 version index |
| **D1, D2, D5–D8** | Include/exclude folder set and migration posture per folder |
| **E1–E3** | Destination structure acceptance; cross-reference deferrals |
| **F1, F2, F4** | PUB-002 boundary details; PNG acknowledgment policy |
| — | **Notion GFVP mapping** (deep page-to-Drive reconciliation) |
| — | **P009 ambiguity** (`NTN-REC-002` event type) |
| — | **Export zip** location and completeness |
| — | **PUB-002 release import** scope and authorization |
| — | **Full P002–P011 version index** population |

---

## 12. Receipt Requirements

Before any future import of `TG-SRC-VIS-001` source material into this repository:

1. A **migration receipt** must be created and human-approved.
2. The receipt must cite this manifest, the exact import file set, and resolved decisions above.
3. Import must remain separate from **`TG-SRC-PUB-002`** unless separately authorized.
4. No retrospective lock receipts, canon promotion, or binary import may be inferred from this manifest.

This manifest alone **does not satisfy** the receipt requirement.

---

## 13. Migration Readiness Status

| Field | Value |
|---|---|
| **Recommendation** | `NEEDS_SOURCE_INVENTORY` |
| **Migration authorized** | `false` |
| **Manifest status** | DRAFT — planning index only |

**Reason:** Manifest drafting is complete enough to index the cluster, but physical migration still requires an exact import set, resolution of remaining decisions (§11), a migration plan aligned with destination structure, and an approved receipt (§12).

**Planning baseline:** Accepted as draft planning index 2026-07-06 per `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_REVIEW_DRAFT.md`. Does not authorize migration or import.

**Candidate review:** `FIRST_MIGRATION_CANDIDATE_REVIEW_TG_SRC_VIS_001.md` — recommendation unchanged: suitable for read-only inventory and authority mapping; **not ready for migration**.

---

## Planning Evidence Index

| Document | Role |
|---|---|
| `TG_SRC_VIS_001_FILE_INVENTORY_DRAFT.md` | Detailed file inventory |
| `TG_SRC_VIS_001_AUTHORITY_HIERARCHY_DRAFT.md` | Authority tiers and conflicts |
| `TG_SRC_VIS_001_VERSION_LOCK_REVIEW_DRAFT.md` | P003/P007 chains; P002/P003 composite lock |
| `TG_SRC_VIS_001_DESTINATION_STRUCTURE_DRAFT.md` | Proposed repo layout |
| `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_DRAFT.md` | Manifest schema (superseded by this file for content) |
| `TG_SRC_VIS_001_MANIFEST_READINESS_RECHECK_DRAFT.md` | Readiness gate before drafting |
| `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md` | Ratification record |
| `FIRST_MIGRATION_CANDIDATE_REVIEW_TG_SRC_VIS_001.md` | Migration candidacy |
| `SOURCE_TO_DESTINATION_MAP_DRAFT.md` | Source cluster map |
| `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_REVIEW_DRAFT.md` | Manifest review; baseline acceptance record |

---

## Output Summary (manifest)

**What changed:** Accepted as draft planning baseline (2026-07-06). Applied review revisions R-M01 (per-folder inventory summary) and R-M02 (Notion metadata cross-reference index). No source files copied; no subfolders created; no canon promotion.

**What should be locked:**

- Draft planning index status for `TG-SRC-VIS-001`
- Ratified header fields and P001–P011 planning range
- PUB-002 exclusion boundary; `TG-SRC-PUB-002` deferred
- Composite-lock scope limitation for P002/P003
- Authority hierarchy ordering for migration planning
- Migration readiness: `NEEDS_SOURCE_INVENTORY`

**What remains living:**

- Per-file import manifest rows
- Full P002–P011 version chains
- Unresolved decisions §11
- Optional revisions R-M03–R-M10 (not applied)
- Deep Notion mapping and P009/`NTN-REC-002` resolution
- Physical migration, import receipt, and PUB-002 release import

**Concrete next steps:**

1. Resolve or defer checklist items A4, C1–C4, D1/D2/D5–D8, E1–E3, F1/F2/F4.
2. Populate full version index and per-plate lock evidence rows.
3. Produce exact import set and migration plan.
4. Obtain migration receipt before any import.
5. Keep `TG-SRC-PUB-002` deferred until zip located and release scope confirmed.
