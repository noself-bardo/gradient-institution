# TG-SRC-PUB-002 Exact Import Manifest
Status: DRAFT / EXACT IMPORT MANIFEST ONLY
Authority: Not canonical
Baseline Commit: `29e989824c1b681ec06c3b4d057d3449c7f3b82a`
Prepared: 2026-07-07
Ratification: **SCOPE RATIFIED 2026-07-07** (S1–S5; planning only — see `TG_SRC_PUB_002_RATIFICATION_PACKET_DRAFT.md`)
Source ID: `TG-SRC-PUB-002`
Drive Root: `gradient_foundational_visual_package_batch_01`
Provisional Destination Root: `07_publishing/series/gfvp/`

Related Migration Plan: `TG_SRC_PUB_002_MIGRATION_PLAN_DRAFT.md`

Related Migration Receipt: `11_receipts/TG_REC_MIG_002_PUB_002_IMPORT_RECEIPT_DRAFT.md`

Related Post-Import Audit: `TG_SRC_PUB_002_POST_IMPORT_AUDIT_DRAFT.md`

Constraint: This manifest does **not** authorize migration, extraction, file copy, folder creation, source promotion, canon change, external edits, commits, or app/RPC work.

---

## Purpose

Enumerate the **46-file co-import candidate set** for `TG-SRC-PUB-002` release/export planning per ratified scope **S1** (21 md + 25 PNG from `06_GENERATED_OUTPUTS/` and `08_APPROVED_OUTPUTS/` only).

## VIS-001 / PUB-002 Boundary

| Cluster | Repo location | Posture |
|---|---|---|
| `TG-SRC-VIS-001` | `06_visual_language/gfvp/` (`ca6410e`) | Source system imported; **excludes** `06_`/`08_` payloads |
| `TG-SRC-PUB-002` | `07_publishing/series/gfvp/` (proposed) | Release/export; **separate** from VIS-001 |

Import of this manifest does **not** modify VIS-001 paths. PUB-002 materials must not be placed under `06_visual_language/gfvp/`.

## Scope Boundaries

| Bucket | Count | Posture |
|---|---:|---|
| **This manifest (co-import candidate)** | **46** | Include rows below |
| `06_GENERATED_OUTPUTS/` md | 10 | **Include** |
| `06_GENERATED_OUTPUTS/` PNG | 14 | **Include** |
| `08_APPROVED_OUTPUTS/` md | 11 | **Include** |
| `08_APPROVED_OUTPUTS/` PNG | 11 | **Include** |
| **`07_OUTPUT_QC/` md** | 14 | **Reference-only (S2)** — **not in this manifest** |
| Export zip files | 3 candidates | **Reference-only mirror (S3)** — **not in this manifest** |
| PDFs | 0 | **Excluded** |

### `07_OUTPUT_QC/` Reference-Only Note (S2)

Fourteen output QC md files in `07_OUTPUT_QC/` provide authority metadata for P001–P011 output chains (including P003/P007 version chains). **Ratified reference-only by default.** Cite in migration plan or receipt cross-refs if needed. Co-import requires **separate human ratification** — not granted 2026-07-07.

### Zip Mirror Candidate Note (S3)

| Candidate | Path | Posture |
|---|---|---|
| Strong full-package mirror | `gradient_foundational_visual_package_batch_01_LEVEL_A_CODEX_COMPLETE_v1-0.zip.zip` (Drive; ~31.9 MB; 25 PNGs) | **Planning reference only** — not canonical release; **not** an import row |
| Partial exports | `Downloads/gradient_foundational_visual_package_batch_01.zip`; `(1).zip` | **Not ratified** as authority |

Zip files are **excluded** from co-import enumeration. Live Drive folder paths in this manifest are the planning source of truth unless separately ratified.

## Folder Summary

| Drive Folder | md | PNG | Rows | Proposed Destination Group |
|---|---:|---:|---:|---|
| `06_GENERATED_OUTPUTS/` | 10 | 14 | 24 | `generated_outputs/receipts/` + `generated_outputs/candidates/` |
| `08_APPROVED_OUTPUTS/` | 11 | 11 | 22 | `approved_outputs/receipts/` + `approved_outputs/plates/` |
| **Total** | **21** | **25** | **46** | |

## Proposed Destination Layout (Planning Only)

    07_publishing/series/gfvp/
      generated_outputs/
        receipts/          (10 md)
        candidates/        (14 png)
      approved_outputs/
        receipts/          (11 md)
        plates/            (11 png)

**No subfolders are created by this manifest document.**

---

## Exact Import Rows

| Import ID | Source ID | Source Path | Filename | File Type | Artifact Class | Current Authority Role | Proposed Repo Subpath Under `07_publishing/series/gfvp/` | Include Status | Risk / Ambiguity | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `IMP-001` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P002_GENERATION_RECEIPT.md` | `P002_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P002_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-002` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P003_GENERATION_RECEIPT.md` | `P003_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P003_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-003` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P004_GENERATION_RECEIPT.md` | `P004_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P004_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-004` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P005_GENERATION_RECEIPT.md` | `P005_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P005_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-005` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P006_GENERATION_RECEIPT.md` | `P006_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P006_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-006` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P007_GENERATION_RECEIPT.md` | `P007_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P007_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-007` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P008_GENERATION_RECEIPT.md` | `P008_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P008_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-008` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P009_GENERATION_RECEIPT.md` | `P009_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P009_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-009` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P010_GENERATION_RECEIPT.md` | `P010_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P010_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-010` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/P011_GENERATION_RECEIPT.md` | `P011_GENERATION_RECEIPT.md` | Markdown | `GENERATION_RECEIPT` | Generation receipt metadata | `07_publishing/series/gfvp/generated_outputs/receipts/P011_GENERATION_RECEIPT.md` | **Include** | Medium | Documents candidate output generation |
| `IMP-011` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P001_identity_constitutional-knowledge-ecology_generated_v0-1.png` | `GFVP_B01_P001_identity_constitutional-knowledge-ecology_generated_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P001_identity_constitutional-knowledge-ecology_generated_v0-1.png` | **Include** | Medium | P001 generated candidate; legacy staged-run output |
| `IMP-012` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P002_admission-gate_candidate_v0-1.png` | `GFVP_B01_P002_admission-gate_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P002_admission-gate_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-013` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P003_source-review_candidate_v0-2.png` | `GFVP_B01_P003_source-review_candidate_v0-2.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P003_source-review_candidate_v0-2.png` | **Include** | Medium | Superseded P003 candidate; retain per filename preservation (S1) |
| `IMP-014` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P003_source-review_candidate_v0-3.png` | `GFVP_B01_P003_source-review_candidate_v0-3.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P003_source-review_candidate_v0-3.png` | **Include** | Medium | Superseded P003 candidate; retain per filename preservation (S1) |
| `IMP-015` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P003_source-review_candidate_v0-4.png` | `GFVP_B01_P003_source-review_candidate_v0-4.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P003_source-review_candidate_v0-4.png` | **Include** | Low | — |
| `IMP-016` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P004_metabolization-boundary_candidate_v0-1.png` | `GFVP_B01_P004_metabolization-boundary_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P004_metabolization-boundary_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-017` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P005_card_candidate_v0-1.png` | `GFVP_B01_P005_card_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P005_card_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-018` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P006_claim_candidate_v0-1.png` | `GFVP_B01_P006_claim_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P006_claim_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-019` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P007_relationship_candidate_v0-1.png` | `GFVP_B01_P007_relationship_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P007_relationship_candidate_v0-1.png` | **Include** | Medium | Superseded P007 candidate; retain per filename preservation (S1) |
| `IMP-020` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P007_relationship_candidate_v0-2.png` | `GFVP_B01_P007_relationship_candidate_v0-2.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P007_relationship_candidate_v0-2.png` | **Include** | Low | — |
| `IMP-021` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P008_evidence_candidate_v0-1.png` | `GFVP_B01_P008_evidence_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P008_evidence_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-022` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P009_source_candidate_v0-1.png` | `GFVP_B01_P009_source_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P009_source_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-023` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P010_history_candidate_v0-1.png` | `GFVP_B01_P010_history_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P010_history_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-024` | `TG-SRC-PUB-002` | `06_GENERATED_OUTPUTS/GFVP_B01_P011_decision_candidate_v0-1.png` | `GFVP_B01_P011_decision_candidate_v0-1.png` | PNG | `GENERATED_CANDIDATE_OUTPUT` | Generated candidate visual output | `07_publishing/series/gfvp/generated_outputs/candidates/GFVP_B01_P011_decision_candidate_v0-1.png` | **Include** | Low | — |
| `IMP-025` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P001_APPROVAL_RECEIPT.md` | `P001_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P001_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-026` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P002_APPROVAL_RECEIPT.md` | `P002_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P002_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-027` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P003_APPROVAL_RECEIPT.md` | `P003_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P003_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-028` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P004_APPROVAL_RECEIPT.md` | `P004_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P004_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-029` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P005_APPROVAL_RECEIPT.md` | `P005_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P005_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-030` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P006_APPROVAL_RECEIPT.md` | `P006_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P006_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-031` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P007_APPROVAL_RECEIPT.md` | `P007_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P007_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-032` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P008_APPROVAL_RECEIPT.md` | `P008_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P008_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-033` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P009_APPROVAL_RECEIPT.md` | `P009_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P009_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-034` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P010_APPROVAL_RECEIPT.md` | `P010_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P010_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-035` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/P011_APPROVAL_RECEIPT.md` | `P011_APPROVAL_RECEIPT.md` | Markdown | `APPROVAL_RECEIPT` | Output approval receipt metadata | `07_publishing/series/gfvp/approved_outputs/receipts/P011_APPROVAL_RECEIPT.md` | **Include** | Medium | Approval documented; receipt metadata not sole binary proof |
| `IMP-036` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P001_identity_constitutional-knowledge-ecology_APPROVED_v0-1.png` | `GFVP_B01_P001_identity_constitutional-knowledge-ecology_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P001_identity_constitutional-knowledge-ecology_APPROVED_v0-1.png` | **Include** | Medium | P001 approved output; legacy workflow path |
| `IMP-037` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P002_admission-gate_APPROVED_v0-1.png` | `GFVP_B01_P002_admission-gate_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P002_admission-gate_APPROVED_v0-1.png` | **Include** | Low | — |
| `IMP-038` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P003_source-review_APPROVED_v0-4.png` | `GFVP_B01_P003_source-review_APPROVED_v0-4.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P003_source-review_APPROVED_v0-4.png` | **Include** | Low | Current approved P003 output v0-4 |
| `IMP-039` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P004_metabolization-boundary_APPROVED_v0-1.png` | `GFVP_B01_P004_metabolization-boundary_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P004_metabolization-boundary_APPROVED_v0-1.png` | **Include** | Low | — |
| `IMP-040` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P005_card_APPROVED_v0-1.png` | `GFVP_B01_P005_card_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P005_card_APPROVED_v0-1.png` | **Include** | Low | — |
| `IMP-041` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P006_claim_APPROVED_v0-1.png` | `GFVP_B01_P006_claim_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P006_claim_APPROVED_v0-1.png` | **Include** | Low | — |
| `IMP-042` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P007_relationship_APPROVED_v0-2.png` | `GFVP_B01_P007_relationship_APPROVED_v0-2.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P007_relationship_APPROVED_v0-2.png` | **Include** | Low | Current approved P007 output v0-2 |
| `IMP-043` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P008_evidence_APPROVED_v0-1.png` | `GFVP_B01_P008_evidence_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P008_evidence_APPROVED_v0-1.png` | **Include** | Low | — |
| `IMP-044` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P009_source_APPROVED_v0-1.png` | `GFVP_B01_P009_source_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P009_source_APPROVED_v0-1.png` | **Include** | Low | — |
| `IMP-045` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P010_history_APPROVED_v0-1.png` | `GFVP_B01_P010_history_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P010_history_APPROVED_v0-1.png` | **Include** | Low | — |
| `IMP-046` | `TG-SRC-PUB-002` | `08_APPROVED_OUTPUTS/GFVP_B01_P011_decision_APPROVED_v0-1.png` | `GFVP_B01_P011_decision_APPROVED_v0-1.png` | PNG | `APPROVED_VISUAL_OUTPUT` | Approved visual output / release asset | `07_publishing/series/gfvp/approved_outputs/plates/GFVP_B01_P011_decision_APPROVED_v0-1.png` | **Include** | Low | — |

---

## Recommendation

### **`EXECUTED`**

Import manifest rows IMP-001–IMP-046 physically imported 2026-07-07 to `07_publishing/series/gfvp/`. Post-import audit **PASS**.

Physical import complete. Commit separately authorized.

---

## Output Summary

**What changed:** Physical import executed — 46 files copied per IMP rows; post-import audit **PASS**.

**What should be locked after review:** 46-file set; destination paths; exclusion boundaries.

**What remains living:** Commit authorization; zip canonical designation; optional `07_` co-import ratification.

**Concrete next steps:**

1. Human review working tree diff.
2. Authorize commit separately if desired: `AUTHORIZED — COMMIT TG-SRC-PUB-002 IMPORT`.
