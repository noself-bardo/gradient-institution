# TG-SRC-PUB-002 Migration Plan Draft

Status: DRAFT / PLAN ONLY

Authority: Not canonical

Baseline Commit: `29e989824c1b681ec06c3b4d057d3449c7f3b82a`

Prepared: 2026-07-07

Source ID: `TG-SRC-PUB-002`

Drive Root: `gradient_foundational_visual_package_batch_01`

Related Inventory: `TG_SRC_PUB_002_INVENTORY_DRAFT.md`

Related Ratification Packet: `TG_SRC_PUB_002_RATIFICATION_PACKET_DRAFT.md`

Related Decision Summary: `TG_SRC_PUB_002_HUMAN_DECISION_SUMMARY_DRAFT.md`

Related Exact Import Manifest: `TG_SRC_PUB_002_EXACT_IMPORT_MANIFEST_DRAFT.md`

Related Migration Receipt: `11_receipts/TG_REC_MIG_002_PUB_002_IMPORT_RECEIPT_DRAFT.md`

Related Post-Import Audit: `TG_SRC_PUB_002_POST_IMPORT_AUDIT_DRAFT.md`

Related Source ID (boundary): `TG-SRC-VIS-001` (imported `ca6410e` under `TG-REC-MIG-001`; PUB-002 excluded from VIS-001 scope)

Constraint: This plan does **not** authorize file copy, migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work.

---

## 1. Status Header

| Field | Value |
|---|---|
| Title | TG-SRC-PUB-002 Migration Plan Draft |
| Status | DRAFT / PLAN ONLY |
| Authority | Not canonical |
| Source ID | `TG-SRC-PUB-002` |
| Related Inventory | `TG_SRC_PUB_002_INVENTORY_DRAFT.md` |
| Related Ratification Packet | `TG_SRC_PUB_002_RATIFICATION_PACKET_DRAFT.md` |
| Related Decision Summary | `TG_SRC_PUB_002_HUMAN_DECISION_SUMMARY_DRAFT.md` |
| Related Exact Import Manifest | `TG_SRC_PUB_002_EXACT_IMPORT_MANIFEST_DRAFT.md` |
| Related Migration Receipt | `11_receipts/TG_REC_MIG_002_PUB_002_IMPORT_RECEIPT_DRAFT.md` |
| Constraint | This plan does not authorize file copy, migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work |

---

## 2. Migration Objective

Import the GFVP **release/export package** materials from Drive root `gradient_foundational_visual_package_batch_01` into the repository at **`07_publishing/series/gfvp/`**, using the exact **46-file** import manifest (`IMP-001`–`IMP-046`) and ratified PUB-002 planning decisions **S1–S5**.

The objective is to establish a **controlled, receipt-gated, verifiable** copy of **21 md + 25 PNG** release/export artifacts while:

- Preserving strict **VIS-001 / PUB-002 separation** (no source-system md/csv from `00_`–`05_`, `09_`, `11_`, `12_`, `13_`, `99_`; no co-import into `06_visual_language/gfvp/`).
- Preserving **original filenames** (per S1 filename-preservation posture).
- Citing ratified planning decisions for scope, reference-only exclusions, and zip mirror posture.
- **Not** promoting imported materials to institutional canon.
- **Not** treating repo placement as binary verification, publication authorization, or canonical release designation.

Drive remains the system of record for reference-only `07_OUTPUT_QC/` metadata and zip mirror candidates until separately authorized.

---

## 3. Source Scope

### In scope (46 files — exact import manifest)

| Bucket | Count | Source |
|---|---:|---|
| Co-import candidate md/PNG | **46** | `TG_SRC_PUB_002_EXACT_IMPORT_MANIFEST_DRAFT.md` (IMP-001–IMP-046) |
| Release/export materials | 46 | Generation receipts, approval receipts, generated candidates, approved plates |

**Drive folders included (Import? Yes per ratified S1):**

| Drive Folder | md | PNG | Total | Destination group |
|---|---:|---:|---:|---|
| `06_GENERATED_OUTPUTS/` | 10 | 14 | 24 | `generated_outputs/receipts/` + `generated_outputs/candidates/` |
| `08_APPROVED_OUTPUTS/` | 11 | 11 | 22 | `approved_outputs/receipts/` + `approved_outputs/plates/` |
| **Total** | **21** | **25** | **46** | |

### Explicitly excluded (not in import manifest)

| Excluded class | Count | Reason |
|---|---:|---|
| `07_OUTPUT_QC/` md | **14** | **S2** — reference-only; cite paths, do not co-import |
| Export zip files | **3 candidates** | **S3** — planning mirror only; not canonical release; not import rows |
| VIS-001 source-system md/csv | **248** | Already imported under `06_visual_language/gfvp/` (`ca6410e`); **S4** boundary |
| PDFs / publication exports | **0** | None observed in inventory |
| Notion page bodies | — | External; metadata reference only |
| Supabase / app / RPC material | — | Out of scope |
| Any file outside IMP-001–IMP-046 | — | Not in ratified 46-file default scope |

**Inventory context:** 60 md + 25 PNG in PUB-002-relevant Drive folders; **46** co-import candidate per S1; **14** `07_` md reference-only per S2.

---

## 4. Ratified Authority Basis

Planning decisions recorded in `TG_SRC_PUB_002_RATIFICATION_PACKET_DRAFT.md` and `TG_SRC_PUB_002_HUMAN_DECISION_SUMMARY_DRAFT.md` (2026-07-07). This plan cites them; it does not re-ratify or extend scope.

| Basis | Ratification | Application in this plan |
|---|---|---|
| **S1** — Default 46-file scope | **APPROVED** | Import only `06_GENERATED_OUTPUTS/` + `08_APPROVED_OUTPUTS/` (21 md + 25 PNG) |
| **S2** — `07_OUTPUT_QC/` reference-only | **APPROVED** | 14 output QC md files excluded; cite in receipt cross-refs if needed |
| **S3** — Zip mirror candidate | **APPROVED FOR PLANNING ONLY** | `batch_01_LEVEL_A_CODEX_COMPLETE_v1-0.zip.zip` is strong mirror candidate; **not** canonical release; not co-imported |
| **S4** — VIS-001 / PUB-002 separation | **REAFFIRMED** | Destination `07_publishing/series/gfvp/`; no PUB-002 files under `06_visual_language/gfvp/` |
| **S5** — Physical import | **NOT AUTHORIZED** by ratification | Receipt gate required before file copy |
| Exact import manifest | **Drafted 2026-07-07** | Per-file destination map: IMP-001–IMP-046 |
| **`TG-SRC-VIS-001`** | **Imported `ca6410e`** | Source system separate; VIS-001 excludes `06_`/`08_` payloads |

---

## 5. Proposed Destination

### Primary destination

`07_publishing/series/gfvp/`

### Lifecycle substructure (planning only)

**No folders are created by this plan document.**

```text
07_publishing/series/gfvp/
  generated_outputs/
    receipts/          (10 md — P002–P011 generation receipts)
    candidates/        (14 png — generated candidate outputs)
  approved_outputs/
    receipts/          (11 md — P001–P011 approval receipts)
    plates/            (11 png — approved visual outputs)
```

**Mapping authority:** Each file's proposed repo subpath is defined in `TG_SRC_PUB_002_EXACT_IMPORT_MANIFEST_DRAFT.md` (column: Proposed Repo Subpath Under `07_publishing/series/gfvp/`). That manifest is the authoritative per-file destination map for future import execution.

**Functional reference destinations (not co-import targets):** `06_visual_language/gfvp/` (VIS-001 source system); `11_receipts/` (migration receipt filing when authorized); `07_OUTPUT_QC/` on Drive (reference-only per S2).

**Version-chain notes (planning):** P003 and P007 include superseded generated candidates alongside current approved plates; all retained per S1 filename preservation. P001 follows legacy workflow path in both generated and approved folders.

---

## 6. Import Sequence

Future physical import must follow this ordered sequence. **None of these steps are authorized by this plan alone** — execution requires human-approved **`TG-REC-MIG-002`** before step 4.

| Step | Action | Verification |
|---:|---|---|
| **1** | **Confirm working tree state** | Clean or intentionally scoped dirty state documented; baseline commit noted; no unauthorized edits in flight |
| **2** | **Verify exact 46-file import manifest** | Reconcile `TG_SRC_PUB_002_EXACT_IMPORT_MANIFEST_DRAFT.md` (46 rows) against synced Drive; confirm IMP-001–IMP-046 paths exist; re-enumerate `06_`/`08_` folders |
| **3** | **Create destination subfolders** | Create `generated_outputs/receipts/`, `generated_outputs/candidates/`, `approved_outputs/receipts/`, `approved_outputs/plates/` under `07_publishing/series/gfvp/` — only after receipt approval |
| **4** | **Copy files according to import manifest** | Copy 46 md/PNG files Drive → repo per IMP rows; preserve filenames; read-only copy from Drive source |
| **5** | **Verify file counts and paths** | 46 files present; 21 md + 25 PNG; each path matches import manifest column; folder sums match §3 table |
| **6** | **Verify no VIS-001 source-system files imported** | 0 md/csv from VIS-001 lifecycle folders; 0 files placed under `06_visual_language/gfvp/` as part of this import |
| **7** | **Verify no `07_OUTPUT_QC/` files imported** | 0 files from `07_OUTPUT_QC/`; 14 reference-only md remain on Drive only |
| **8** | **Verify zip candidates are not imported** | 0 zip files copied; zip mirror candidates remain reference-only per S3 |
| **9** | **Update receipt with execution results** | Complete `TG-REC-MIG-002` execution fields; link post-import audit |
| **10** | **Run post-import audit** | Repeat verification checklist §8; compare working tree to import manifest |
| **11** | **Stop before commit unless separately approved** | No git commit without explicit human authorization |

---

## 7. Required Receipt

### Gate

**Physical import (steps 3–4 onward) requires human-approved receipt `TG-REC-MIG-002` (`MIG`) before any file copy.**

This migration plan does **not** substitute for the receipt. The exact import manifest alone does **not** satisfy the receipt requirement.

### Proposed receipt

| Field | Value |
|---|---|
| Receipt ID | `TG-REC-MIG-002` (provisional) |
| Receipt Type | `MIG` |
| Title (working) | TG-SRC-PUB-002 GFVP Release/Export Package Physical Import |
| Storage | `11_receipts/TG_REC_MIG_002_PUB_002_IMPORT_RECEIPT_DRAFT.md` |
| Receipt status | **EXECUTED / AWAITING COMMIT AUTHORIZATION** |
| Receipt signoff | **Yes** — 2026-07-07 (Steven) |
| Execution authorized | **Yes** — 2026-07-07 (Steven) |
| Physical import executed | **Yes** — 46/46 files (2026-07-07) |
| Post-import audit | **PASS** — `TG_SRC_PUB_002_POST_IMPORT_AUDIT_DRAFT.md` |

### Receipt must cite

1. **Source ID:** `TG-SRC-PUB-002`
2. **Exact import manifest:** `TG_SRC_PUB_002_EXACT_IMPORT_MANIFEST_DRAFT.md` (46 rows, IMP-001–IMP-046)
3. **Ratified PUB-002 decisions S1–S5** — per ratification packet and human decision summary
4. **VIS-001 / PUB-002 boundary:** VIS-001 at `06_visual_language/gfvp/` (`ca6410e`); PUB-002 at `07_publishing/series/gfvp/`; no cross-placement
5. **`07_OUTPUT_QC/` reference-only exclusion:** 14 md not co-imported (S2)
6. **Zip mirror candidate exclusion:** zip files planning reference only; not canonical release (S3)
7. **Verification steps:** §6 steps 5–8 and §8 checklist
8. **Non-authorization boundaries:** No canon promotion; no VIS-001 re-import; no `07_` co-import without separate ratification; no zip canonical designation; no Notion/Drive/Supabase edits; no publication authorization; no commit unless separately authorized; receipt metadata is not sole binary proof

### Standard fields

Populate all standard receipt fields per `RECEIPT_TEMPLATE_DRAFT.md`, including explicit **What Is Authorized** / **What Is Not Authorized** blocks.

**Supporting planning artifacts:** inventory draft, ratification packet, human decision summary, exact import manifest, this migration plan.

---

## 8. Verification Checklist

Execute after physical import (step 10). All items must pass before considering import complete.

| # | Check | Expected result |
|---:|---|---|
| 1 | Files copied | **46** files in repo under `07_publishing/series/gfvp/` |
| 2 | Markdown files copied | **21** md |
| 3 | PNG files copied | **25** PNG |
| 4 | `07_OUTPUT_QC/` files copied | **0** |
| 5 | VIS-001 source-system files copied | **0** (no md/csv from VIS-001 scope; nothing placed under `06_visual_language/gfvp/` by this import) |
| 6 | Zip files copied | **0** |
| 7 | Destination paths | Every imported file matches exact import manifest proposed subpath |
| 8 | Source files modified | **No** modifications to Drive originals |
| 9 | External systems edited | **No** Notion, Drive, Supabase, or app changes |
| 10 | Receipt created/executed | `TG-REC-MIG-002` approved before copy; post-import execution fields completed |
| 11 | Working tree reviewed | Diff reviewed before any commit decision |
| 12 | Commit | **Not performed** unless separately approved |

---

## 9. Risks / Caveats

| Risk | Mitigation / note |
|---|---|
| Exact import manifest is draft until physical verification | Re-verify IMP rows against Drive immediately before import (step 2) |
| Zip mirror is planning-only | **S3** — `batch_01_LEVEL_A_CODEX_COMPLETE_v1-0.zip.zip` is not canonical release authority; live Drive folders are planning source of truth |
| **`NTN-REC-002` / P009 ambiguity** | Deferred; do not resolve from metadata during import; P009 approval receipt and plate import per manifest only |
| Release import ≠ canon promotion | Repo placement is migration-control derivative only |
| Commit separately authorized | Import completion does not imply commit approval |
| PUB-002 is publication/release scope | Not VIS-001 source-system scope; do not merge clusters |
| P003/P007 superseded candidates | Multiple generated versions retained per S1; current approved plates identified in manifest notes |
| P001 legacy workflow path | Both generated and approved P001 artifacts follow legacy staged-run path |
| Receipt metadata ≠ binary proof | Approval/generation receipt md documents process; PNG binaries are separate artifacts |
| `07_` authority metadata | Output QC chains available on Drive for reference; excluded unless separately ratified |

---

## 10. Stop Gates

Separate human approval is required before:

| Gate | Action blocked without approval |
|---|---|
| **Draft `TG-REC-MIG-002`** | Authoring/filing migration receipt content |
| **Physical import** | Steps 3–4 (folder creation, file copy) |
| **Post-import commit** | Any git commit of imported payload |
| **Inclusion of `07_OUTPUT_QC/`** | Co-import of 14 reference-only output QC md files |
| **Zip / release-package authority claim** | Designating any zip as canonical release package |
| **App/RPC/platform work** | Platform implementation tied to GFVP release import |

---

## 11. Recommendation

This migration plan draft is **planning documentation only**. It does not satisfy any stop gate in §10.

### **`EXECUTED / AWAITING COMMIT AUTHORIZATION`**

Physical import executed 2026-07-07 under `AUTHORIZED — EXECUTE TG-SRC-PUB-002 PHYSICAL IMPORT`. **46/46** files copied to `07_publishing/series/gfvp/`. Post-import audit **PASS**.

| Meaning | Does | Does not |
|---|---|---|
| **`EXECUTED / AWAITING COMMIT AUTHORIZATION`** | Import complete per manifest; receipt and audit filed | Authorize commit, canon promotion, or external edits |

**Commit candidacy** remains **`NOT_AUTHORIZED`** until explicit `AUTHORIZED — COMMIT TG-SRC-PUB-002 IMPORT`.

---

## Output Summary

**What changed:** Created controlled migration plan for `TG-SRC-PUB-002` citing 46-file exact import manifest and ratified planning decisions S1–S5.

**What should be locked after plan review:** Import scope (46 md/PNG); `07_` reference-only exclusion; zip reference-only posture; VIS-001/PUB-002 separation; destination map under `07_publishing/series/gfvp/`; receipt gate before copy; stop gates.

**What changed:** Physical import executed — 46 md/PNG copied to `07_publishing/series/gfvp/`; post-import audit **PASS**.

**What should be locked after review:** Import scope; destination paths; exclusion boundaries; receipt execution record.

**What remains living:** Human working-tree review; commit authorization; `NTN-REC-002` P009 resolution; optional `07_` co-import; zip canonical designation.

**Concrete next steps:**

1. Human review working tree diff (46 imported files + planning/receipt docs).
2. Authorize commit separately if desired: `AUTHORIZED — COMMIT TG-SRC-PUB-002 IMPORT`.
3. Do not treat import as canon promotion.
