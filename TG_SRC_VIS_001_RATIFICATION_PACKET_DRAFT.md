# TG-SRC-VIS-001 Ratification Packet

Status: DRAFT / HUMAN RATIFICATION PACKET — **RATIFIED 2026-07-06**

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Prepared: 2026-07-06

Ratified: 2026-07-06 (migration-plan prerequisite bundle)

Prior ratification: 2026-07-06 bundle (A1, A3, B1/B3, A6, A2/D3/D4, A7) in `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md`

Constraint: This packet does **not** authorize migration, extraction, file copy, folder creation, source promotion, canon change, external edits, commits, or app/RPC work.

---

## Purpose

Prepare human ratification decisions required before **`TG_SRC_VIS_001_MIGRATION_PLAN_DRAFT.md`** authoring, per `TG_SRC_VIS_001_MIGRATION_PLAN_READINESS_DRAFT.md`.

Companion artifact: `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` (**248 rows** — **ACCEPTED AS DRAFT IMPORT ENUMERATION 2026-07-06**; migration-plan drafting only; no file copy).

---

## Human Ratification Record (2026-07-06 — Migration-Plan Prerequisite Bundle)

| Decision ID | Human Decision | Scope |
|---|---|---|
| **A4** | **APPROVED** — Authority hierarchy constrained by A7 | Roadmap controls plate identity; remediation vocabulary secondary/historical |
| **C1** | **APPROVED** — P003 current planning chain | spec v0-2 → compiler v0-4 → output QC v0-4 → approval v0-4 |
| **C2** | **APPROVED** — P007 current planning chain | spec v0-1 → compiler v0-2 → output QC v0-2 → approval v0-2; lock v0-1 predates regen |
| **D2** | **APPROVED** — Include `11_`/`12_` with annotations | Annotated source-system md/csv only; no PUB-002 binaries/outputs |
| **P001 (D2)** | **APPROVED** — Legacy-only representation | IMP-004, IMP-012, IMP-021, IMP-032; no `active_workflow/` rows |
| **E1** | **APPROVED** — Lifecycle-grouped destination mapping | For migration-plan drafting only |
| **Bundle** | **APPROVED** — D1, D5–D8, E2, E3, C3, C4, F1, F2, F4 | Include/exclude and boundary formalization |
| **248-file manifest** | **ACCEPTED AS DRAFT IMPORT ENUMERATION** | Migration-plan drafting only; no file copy |
| **PUB-002** | **REAFFIRMED DEFERRED** | PNGs, release/export, zip, publication outputs excluded from VIS-001 |

**Does not authorize:** migration, import, extraction, canon promotion, PUB-002 release import, commits, or app/RPC work.

## Agents / Lanes Used

| Lane | Output used in this packet |
|---|---|
| Lane 1 — Human ratification packet builder | Decision tables below |
| Lane 3 — P001 representation policy | P001 (under D2) section |
| Lane 4 — Ratification bundle synthesis | Bundled approval language |

---

## Prior Ratified Decisions (unchanged)

| ID | Status |
|---|---|
| A1, A3, A6, A2/D3/D4, A7, B1/B3 | **Ratified 2026-07-06** — planning only |

---

## High-Priority Required Decisions

| Priority | ID | Exact decision needed |
|---:|---|---|
| 1 | **E1** | Accept lifecycle-grouped destination under `06_visual_language/gfvp/` |
| 2 | **C1, C2** | Accept P003 and P007 current version chains |
| 3 | **D2 + P001** | Include `11_`/`12_` with annotations; adopt P001 legacy-only representation |
| 4 | **A4** | Accept authority hierarchy draft constrained by ratified A7 |

---

## Decision Table — Required Prerequisite Bundle

| decision_id | exact_decision_needed | recommended_answer | evidence | risk_if_approved | risk_if_rejected | scope_limitation | authorizes_migration |
|---|---|---|---|---|---|---|---|
| **A4** | Accept or revise full authority ordering in `TG_SRC_VIS_001_AUTHORITY_HIERARCHY_DRAFT.md` (resolve AUTH-C14/C15 vs A7) | **Accept** draft ordering **as constrained by A7**: roadmap controls plate identity; pack sheets/remediation are historical/secondary only | Authority hierarchy draft; manifest §3; A7 ratified 2026-07-06 | Pack B–F text nuance under-documented if fully subordinated | Conflicting authority rules in migration plan | Planning-only hierarchy; not canon | **No** |
| **C1** | Accept P003 chain: spec v0-2 → compiler v0-4 → output QC v0-4 → approval v0-4 | **Accept** | Version/lock review; manifest §6; exact import manifest IMP-053, IMP-146, IMP-150 | Superseded P003 versions mislabeled if annotations incomplete | P003 import rows wrong | Source-inventory annotation only; B1/B3 composite scope unchanged | **No** |
| **C2** | Accept P007 chain: spec v0-1 → compiler v0-2 → output QC v0-2 → approval v0-2 | **Accept**; document object lock v0-1 predates v0-2 regen | Version/lock review; manifest §6; IMP-057, IMP-159, IMP-161 | Lock/version mismatch unless documented | P007 lineage omitted from plan | Source-inventory annotation only | **No** |
| **D2** | Include `11_OBJECT_SPECIFICATIONS/` (93) and `12_COMPILER_PROMPTS/` (85) with version/lock annotations | **Accept** inclusion in 248-file set with annotations per C1/C2/B1/B3 | File inventory; exact import manifest; migration plan readiness B-MP-03 | Core payload imported without metadata if C1/C2 skipped | ~178 files ambiguous in plan | md/csv only; no `07_` co-import | **No** |
| **P001 (D2)** | How to represent P001 without object spec or compiler | **Legacy-only / roadmap-anchored**: IMP-004, IMP-012, IMP-021, IMP-032 under `legacy_workflow/`; **no** `active_workflow/` rows; `workflow_class: legacy_staged_run_anchor` | Migration plan readiness B-MP-06; handoff P001 staged-run narrative; file inventory plate matrix | P001 appears incomplete unless absence documented | P001 rows inconsistent; blocks plan finalization | Planning status only (A3); no fabricated specs | **No** |
| **E1** | Accept lifecycle-grouped repo structure (not flat Drive mirror) | **Accept** per destination structure draft and manifest §9 | Destination structure draft; exact import manifest destination column | Requires per-file mapping discipline (248 rows) | Plan cannot assign repo paths | Planning-only; no folder creation by ratification | **No** |

---

## Decision Table — Recommended Formalization Bundle

| decision_id | exact_decision_needed | recommended_answer | evidence | risk_if_approved | risk_if_rejected | scope_limitation | authorizes_migration |
|---|---|---|---|---|---|---|---|
| **D1** | Include `00_README/`, `04_PREFLIGHT_QC/`, `09_HANDOFFS/`, `13_ROADMAPS/` | **Accept** | Manifest §1 table; exact import manifest rows | Low | Import set incomplete | Formalization only | **No** |
| **D5** | Exclude `06_` and `08_` (PUB-002) | **Accept** | Manifest §8; deferred_pub_002_boundary | Low | Scope creep into PUB-002 | Binaries/receipt md excluded | **No** |
| **D6** | `07_OUTPUT_QC/` reference-only (14 files) | **Accept** | Manifest §1; not in 248-row manifest | Low | Ambiguity on 14 QC files | Reference citation only | **No** |
| **D7** | Omit empty `10_ADMISSION_RECOMMENDATIONS/` | **Accept** | File inventory (0 files) | Low | Empty folder mirror | No rows | **No** |
| **D8** | Include `99_ARCHIVE/` (4 files) | **Accept** | IMP-245–248; P003 revision log | Low | P003 lineage dropped | Lineage preserved | **No** |
| **E2** | No flat numeric-folder mirror at repo root | **Accept** | Destination anti-patterns | Low | Legacy/active conflation | Follows E1 | **No** |
| **E3** | Defer `11_receipts/` and `04_registries/` cross-refs | **Accept deferral** | Manifest §9 functional refs | Low | Premature receipt wiring | Cross-refs later | **No** |
| **C3** | Version chains in manifest only (no sidecar) | **Accept** default | Manifest design; manifest §6 | Low | Wrong repo structure | Default stands | **No** |
| **C4** | Preserve original filenames on import | **Accept** | Destination anti-patterns | Low | Broken receipt cross-refs | Rename prohibited | **No** |
| **F1** | Exclude binaries/zip/PDF from VIS-001 | **Accept** | Manifest §8 | Low | PUB-002 blur | PUB-002 deferred | **No** |
| **F2** | Missing binaries do not block source planning | **Accept** | Manifest baseline accepted | Low | False blocker | Planning only | **No** |
| **F4** | Acknowledge 25 PNGs; defer import | **Accept** | Manifest §8 | Low | False absence claim | Deferral locked | **No** |

---

## P001 Representation Policy (Lane 3 Summary)

| Item | Finding |
|---|---|
| P001 direct co-import files | 4 legacy files (IMP-004, IMP-012, IMP-021, IMP-032) |
| Object spec / compiler | **Absent by design** — staged-run anchor |
| Include without object spec? | **Yes** — as legacy workflow + roadmap identity |
| Recommended annotation | `legacy_staged_run_anchor`; exclude from P002–P011 active-workflow index |
| Risk | Medium–High (workflow asymmetry) |
| Blocks migration plan until D2 ratified? | **Resolved** — ratified 2026-07-06 |

Reference-only (not in 248 manifest): `07_OUTPUT_QC/P001_output_qc_approved.md`, `08_APPROVED_OUTPUTS/P001_APPROVAL_RECEIPT.md`.

---

## Recommended Bundled Approval Language

**Paragraph 1 — Scope and non-authorization**

I ratify the following **planning-only** decisions for source cluster `TG-SRC-VIS-001` (`gradient_foundational_visual_package_batch_01`), effective as of this sign-off. These decisions support drafting a future migration plan and align the exact import manifest (`TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md`) only. They do **not** authorize physical migration, file copy, extraction, source promotion, canon change, retrospective lock receipts, Notion/Drive/Supabase edits, image generation, publication, `TG-SRC-PUB-002` release import, or any commit unless separately authorized. `migration_authorized` remains **false**; `TG-REC-MIG-001` is still required before physical import.

**Paragraph 2 — Minimum prerequisite bundle (A4, C1, C2, D2, E1, P001)**

I accept **E1**: lifecycle-grouped destination under `06_visual_language/gfvp/`. I accept **C1** and **C2** for P003 and P007 current version chains (with P007 lock/regen note). I accept **D2**: include `11_OBJECT_SPECIFICATIONS/` and `12_COMPILER_PROMPTS/` in the 248-file co-import set with version/lock annotations. Under D2, I accept **P001 legacy-only representation** (IMP-004, IMP-012, IMP-021, IMP-032; no active_workflow rows). I accept **A4**: authority hierarchy **as constrained by A7**.

**Paragraph 3 — Formalization bundle (D1, D5–D8, E2, E3, C3, C4, F1, F2, F4)**

I accept the include/exclude and boundary bundle: 248 co-import md/csv; 14 reference-only `07_`; 21 deferred receipt md + 25 deferred PNGs excluded under PUB-002; omit empty `10_`; preserve filenames; defer receipt/registry cross-refs.

**Paragraph 4 — Next gate**

Ratification enables **`READY_TO_DRAFT_MIGRATION_PLAN`** review only. Next: draft migration plan → draft `TG-REC-MIG-001` → human approve receipt → then physical import (still separately authorized).

---

## What Remains Deferred

- Notion GFVP deep mapping
- `NTN-REC-002` P009 ambiguity
- Export zip location / PUB-002 release import
- Full P002–P011 version index beyond C1/C2
- Physical import, folder creation, commits

---

## What This Approval Does NOT Authorize

- Migration, import, extraction, file movement
- Canon or source promotion
- PUB-002 binaries or release packages
- Retrospective lock receipts
- External system edits or app/RPC work
- Commits

---

## Output Summary

**What changed:** Human ratified migration-plan prerequisite bundle (2026-07-06). Recorded in `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md`. Migration plan readiness advanced to **`READY_TO_DRAFT_MIGRATION_PLAN`**.

**What should be locked:** E1 destination map; C1/C2 chains; D2/P001 representation; A4 hierarchy; 248-file import enumeration; PUB-002 deferral.

**Concrete next steps:** Authorize drafting `TG_SRC_VIS_001_MIGRATION_PLAN_DRAFT.md` only (not yet drafted). Then draft `TG-REC-MIG-001` before any physical import.
