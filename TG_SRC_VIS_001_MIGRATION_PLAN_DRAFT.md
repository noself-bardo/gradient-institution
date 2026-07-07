# TG-SRC-VIS-001 Migration Plan Draft

Status: DRAFT / PLAN ONLY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Prepared: 2026-07-06

Source ID: `TG-SRC-VIS-001`

Drive Root: `gradient_foundational_visual_package_batch_01`

Related Manifest: `06_visual_language/gfvp/SOURCE_CLUSTER_MANIFEST.md`

Related Import Manifest: `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md`

Ratification Record: `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md`

Constraint: This plan does **not** authorize file copy, migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work.

---

## 2. Migration Objective

Import the GFVP **source/spec/object/prompt/QC source-system** materials from Drive root `gradient_foundational_visual_package_batch_01` into the repository at **`06_visual_language/gfvp/`**, using the lifecycle-grouped destination structure ratified under **E1**.

The objective is to establish a **controlled, receipt-gated, verifiable** copy of **248 md/csv source-system files** while:

- Preserving strict **VIS-001 / PUB-002 separation** (no PNGs, no release/export packages, no deferred receipt payloads from `06_GENERATED_OUTPUTS/` or `08_APPROVED_OUTPUTS/`).
- Preserving **original filenames** (C4 ratified).
- Citing ratified planning decisions for authority, version chains, and P001 representation.
- **Not** promoting imported materials to institutional canon.
- **Not** treating repo placement as binary verification or publication authorization.

Drive remains the system of record for deferred PUB-002 assets until separately authorized.

---

## 3. Source Scope

### In scope (248 files — exact import manifest)

| Bucket | Count | Source |
|---|---:|---|
| Co-import candidate md/csv | **248** | `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` (IMP-001–IMP-248) |
| Lifecycle / source / control materials | 248 | Object specs, compiler prompts, roadmaps, legacy workflow, handoffs, archive lineage, package control |

**Drive folders included (Import? Yes per ratified bundle):**

| Drive Folder | Files | Destination group |
|---|---:|---|
| `00_README/` | 2 | `package_control/00_README/` |
| `01_SOURCES/` | 1 | `package_control/01_SOURCES/` |
| `02_PLATE_BRIEFS/` | 8 | `legacy_workflow/plate_briefs/` |
| `03_PROMPT_PACKETS/` | 8 | `legacy_workflow/legacy_prompt_packets/` |
| `04_PREFLIGHT_QC/` | 11 | `legacy_workflow/qc/preflight/` |
| `05_LOCKED_PROMPTS/` | 9 | `legacy_workflow/legacy_locked_prompts/` |
| `09_HANDOFFS/` | 8 | `production_evidence/handoffs/` |
| `11_OBJECT_SPECIFICATIONS/` | 93 | `active_workflow/object_specifications/` |
| `12_COMPILER_PROMPTS/` | 85 | `active_workflow/compiler_prompts/` |
| `13_ROADMAPS/` | 19 | `roadmaps/` |
| `99_ARCHIVE/` | 4 | `archive/` |

### Explicitly excluded (not in import manifest)

| Excluded class | Count | Source ID / reason |
|---|---:|---|
| PNG binaries | **25** | `TG-SRC-PUB-002` — 14 in `06_`, 11 in `08_` |
| Deferred receipt md | **21** | `TG-SRC-PUB-002` — generation/approval receipt metadata in `06_`, `08_` |
| Reference-only output QC md | **14** | `07_OUTPUT_QC/` — authority reference only (D6); cite paths, do not co-import |
| Empty slot | **0** | `10_ADMISSION_RECOMMENDATIONS/` — omit (D7) |
| GFVP zip / export package | — | Unlocated; `TG-SRC-PUB-002` |
| PDFs / publication exports | — | `TG-SRC-PUB-002` |
| Notion page bodies | — | External; metadata reference only |

**Inventory context:** 283 total md/csv in Drive package; 262 inventory-scope (includes reference `07_`); **248** co-import candidate.

---

## 4. Ratified Authority Basis

Planning decisions recorded in `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md` (2026-07-06 bundles). This plan cites them; it does not re-ratify or extend scope.

| Basis | Ratification | Application in this plan |
|---|---|---|
| Roadmap controls plate identity | **A1** | Plate ID/name/status from `GFVP_40_PLATE_ROADMAP_v0-1.md` |
| Approved plate count/range | **A3** | **11** plates **P001–P011** — planning status only |
| Next image-gate candidate | **A6** | **P012** — planning only; no generation/publication authorized |
| P002/P003 composite lock | **B1/B3** | Source inventory only; not binary/publication verification |
| Historical manifest / legacy workflow | **A2, D3, D4** | Legacy folders imported as historical evidence |
| Remediation vocabulary | **A7** | Secondary/historical; must not override roadmap |
| Authority hierarchy | **A4** | Hierarchy constrained by A7; roadmap primary for plate identity |
| P003 version chain | **C1** | spec v0-2 → compiler v0-4 → output QC v0-4 → approval v0-4 (reference metadata for QC/approval deferred PUB-002) |
| P007 version chain | **C2** | spec v0-1 → compiler v0-2 → output QC v0-2 → approval v0-2; lock v0-1 predates regen |
| Version index representation | **C3** | Manifest-only; no `_version_index/` sidecar |
| Preserve filenames | **C4** | No rename on import |
| Include `11_`/`12_` with annotations | **D2** | 178 active-workflow files with version/lock notes in manifest |
| P001 legacy-only | **D2 / P001** | IMP-004, IMP-012, IMP-021, IMP-032 only; no `active_workflow/` rows |
| Include/exclude bundle | **D1, D5–D8** | See §2 exclusions |
| Lifecycle destination | **E1, E2** | Grouped substructure; no flat Drive numeric mirror |
| Receipt/registry cross-refs | **E3** | Defer `11_receipts/`, `04_registries/` wiring until receipt policy ratified |
| PUB-002 boundary | **F1, F2, F4** | Binaries deferred; 25 PNGs acknowledged; missing zip does not block this plan |
| Exact import manifest | **Accepted 2026-07-06** | Migration-plan drafting only until physical verification |
| **`TG-SRC-PUB-002`** | **Reaffirmed deferred** | No release import in this plan |

---

## 5. Proposed Destination

### Primary destination

`06_visual_language/gfvp/`

### Lifecycle-grouped substructure (E1 ratified)

Planning-only layout — **no subfolders are created by this plan document.**

```text
06_visual_language/gfvp/
  SOURCE_CLUSTER_MANIFEST.md          (already present — planning index)

  package_control/
    00_README/                         (2 files)
    01_SOURCES/                        (1 file)

  legacy_workflow/
    plate_briefs/                      (8 files)
    legacy_prompt_packets/             (8 files)
    legacy_locked_prompts/             (9 files)
    qc/preflight/                      (11 files)

  active_workflow/
    object_specifications/             (93 files)
    compiler_prompts/                    (85 files)

  production_evidence/
    handoffs/                            (8 files)

  roadmaps/                            (19 files)

  archive/                             (4 files)
```

**Mapping authority:** Each file's proposed repo subpath is defined in `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` (column: Proposed Repo Subpath). That manifest is the authoritative per-file destination map for future import execution.

**Functional reference destinations (not co-import targets):** `11_receipts/`, `04_registries/`, `07_publishing/series/gfvp/` (PUB-002 deferred per E3).

**P001 note:** No files under `active_workflow/` for P001; legacy rows only (IMP-004, IMP-012, IMP-021, IMP-032).

---

## 6. Import Sequence

Future physical import must follow this ordered sequence. **None of these steps are authorized by this plan alone** — execution requires human-approved **`TG-REC-MIG-001`** before step 4.

| Step | Action | Verification |
|---:|---|---|
| **1** | **Confirm working tree state** | Clean or intentionally scoped dirty state documented; baseline commit noted; no unauthorized edits in flight |
| **2** | **Verify exact import manifest** | Reconcile `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` (248 rows) against synced Drive; confirm IMP-001–IMP-248 paths exist; re-run import manifest audit |
| **3** | **Create destination subfolders** | Create lifecycle groups under `06_visual_language/gfvp/` per §4 — only after receipt approval |
| **4** | **Copy files according to import manifest** | Copy 248 md/csv files Drive → repo per IMP rows; preserve filenames (C4); read-only copy from Drive source |
| **5** | **Verify file counts and paths** | 248 files present; each path matches import manifest column; folder sums match §2 table |
| **6** | **Verify no PNG/PUB-002 files imported** | 0 `.png`; 0 files from `06_`/`08_` payloads; 0 zip/PDF; 0 `07_OUTPUT_QC/` co-import |
| **7** | **Update inventory/docs with import receipt references** | Link executed import to `TG-REC-MIG-001`; note any deferred reference-only citations for `07_` |
| **8** | **Create/file import receipt** | `TG-REC-MIG-001` human-approved **before** step 4; filed under `11_receipts/` when authorized |
| **9** | **Run post-import audit** | Repeat verification checklist §8; compare working tree to import manifest |
| **10** | **Stop before commit unless separately approved** | No git commit without explicit human authorization |

---

## 7. Required Receipt

### Gate

**Physical import (steps 3–4 onward) requires human-approved receipt `TG-REC-MIG-001` (`MIG`) before any file copy.**

This migration plan does **not** substitute for the receipt. The source cluster manifest alone does **not** satisfy the receipt requirement.

### Proposed receipt

| Field | Value |
|---|---|
| Receipt ID | `TG-REC-MIG-001` (provisional) |
| Receipt type | `MIG` |
| Title (working) | TG-SRC-VIS-001 GFVP Source Cluster Physical Import |
| Storage | `11_receipts/` (when filing authorized) |

### Receipt must cite

1. **Source ID:** `TG-SRC-VIS-001`
2. **Exact import manifest:** `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` (248 rows, IMP-001–IMP-248)
3. **Ratified decisions:** A1, A3, A6, B1/B3, A2/D3/D4, A7, A4, C1, C2, C3, C4, D2/P001, D1, D5–D8, E1, E2, E3, F1, F2, F4 — per human decision summary
4. **Destination map:** This plan §4 + per-row subpaths in exact import manifest
5. **Excluded PUB-002 boundary:** 25 PNGs, 21 deferred receipt md, zip unlocated, `07_` reference-only — no co-import
6. **Verification steps:** §5 steps 5–6 and §8 checklist
7. **Non-authorization boundaries:** No canon promotion; no PUB-002 import; no retrospective lock receipts; no Notion/Drive/Supabase edits; no image generation; no publication; no commit unless separately authorized; composite P002/P003 lock is source-inventory only

### Standard fields

Populate all standard receipt fields per `RECEIPT_TEMPLATE_DRAFT.md`, including explicit **What Is Authorized** / **What Is Not Authorized** blocks.

**Supporting planning artifacts:** source cluster manifest, exact import manifest, import manifest audit, ratification packet, human decision summary, destination structure draft, migration plan readiness draft, first migration candidate review.

---

## 8. Verification Checklist

Execute after physical import (step 9). All items must pass before considering import complete.

| # | Check | Expected result |
|---:|---|---|
| 1 | Files copied | **248** md/csv files in repo under `06_visual_language/gfvp/` lifecycle paths |
| 2 | PNGs copied | **0** |
| 3 | PUB-002 artifacts copied | **0** (no `06_`/`08_` payload, no zip, no PDF) |
| 4 | Source files modified | **No** modifications to Drive originals |
| 5 | External systems edited | **No** Notion, Drive, Supabase, or app changes |
| 6 | Destination paths | Every imported file matches exact import manifest proposed subpath |
| 7 | Folder sums | Match §2 source scope table (2+1+8+8+11+9+8+93+85+19+4 = 248) |
| 8 | P001 representation | No P001 files under `active_workflow/`; legacy rows only |
| 9 | P003/P007 annotations | Current-chain files present per C1/C2; superseded versions retained per C4 |
| 10 | Receipts created | `TG-REC-MIG-001` approved and filed before copy; post-import receipt fields completed |
| 11 | Reference-only `07_` | **14** files **not** co-imported; cited only if needed in receipt |
| 12 | Working tree reviewed | Diff reviewed before any commit decision |
| 13 | Commit | **Not performed** unless separately approved |

---

## 9. Risks / Caveats

| Risk | Mitigation / note |
|---|---|
| Exact import manifest is draft until physical verification | Re-verify IMP rows against Drive immediately before import (step 2) |
| **`TG-SRC-PUB-002` deferred** | No PNG/zip/release import; receipt metadata in `06_`/`08_` remains reference-only |
| GFVP zip missing | Unlocated; does not block VIS-001 source import plan; blocks PUB-002 release verification |
| P009 / `NTN-REC-002` ambiguity | Deferred; do not resolve from metadata during import |
| Notion deep mapping | Deferred; Notion not import payload |
| Import ≠ canon promotion | Repo placement is migration-control derivative only |
| P002/P003 composite lock | Source inventory only (B1/B3); not binary verification |
| P007 lock/regen mismatch | Documented in C2; object lock v0-1 predates compiler/output v0-2 |
| P001 workflow asymmetry | Legacy-only by design; absence from `active_workflow/` is intentional |
| Stale count fields in README/roadmap lock receipt | Historical per A2/A3; roadmap body controls approved count |
| Commit separately authorized | Import completion does not imply commit approval |
| Superseded compiler/spec versions | Retained per C4; manifest rows mark current vs superseded |

---

## 10. Stop Gates

Separate human approval is required before:

| Gate | Action blocked without approval |
|---|---|
| **Draft `TG-REC-MIG-001`** | Authoring/filing migration receipt content |
| **Physical import** | Steps 3–4 (folder creation, file copy) |
| **Post-import commit** | Any git commit of imported payload |
| **`TG-SRC-PUB-002` work** | PNG/zip/release import, binary verification, publication |
| **App/RPC work** | Platform implementation tied to GFVP import |

---

## 11. Recommendation

This migration plan draft is **planning documentation only**. It does not satisfy any stop gate in §10.

### **`READY_FOR_RECEIPT_DRAFT`**

This migration plan is ready for **human review**. The recommended next step is drafting **`TG-REC-MIG-001`** — **not** importing files.

| Meaning | Does | Does not |
|---|---|---|
| **`READY_FOR_RECEIPT_DRAFT`** | Plan + import manifest + ratification sufficient to draft migration receipt | Authorize physical import, file copy, folder creation, commit, or PUB-002 work |

**Physical import candidacy** (`migration_readiness` in source cluster manifest) remains **`NEEDS_SOURCE_INVENTORY`** until receipt approval and explicit import authorization change that posture.

---

## Output Summary

**What changed:** Created controlled migration plan for `TG-SRC-VIS-001` citing 248-file exact import manifest and ratified planning decisions.

**What should be locked after plan review:** Import scope (248 md/csv); PUB-002 exclusions; E1 destination map; receipt gate before copy; stop gates.

**What remains living:** Human review of this plan; draft `TG-REC-MIG-001`; physical import execution; post-import audit; commit authorization; PUB-002 deferred work.

**Concrete next steps:**

1. Human review this migration plan draft.
2. Authorize drafting `TG-REC-MIG-001` only.
3. Human approve receipt before any folder creation or file copy.
4. Execute import sequence §5 only after receipt approval.
5. Do not commit unless separately approved.
