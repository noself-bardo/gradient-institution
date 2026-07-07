# TG-SRC-PUB-002 Ratification Packet

Status: DRAFT / HUMAN RATIFICATION RECORDED

Authority: Not canonical

Baseline Commit: `fecbce2db201a0e4f25f6eb21f18c5f73610a57c`

Prepared: 2026-07-07

Ratified: 2026-07-07 (planning scope bundle)

Related Inventory: `TG_SRC_PUB_002_INVENTORY_DRAFT.md` (committed `fecbce2`)

Related Source ID: `TG-SRC-VIS-001` (imported `ca6410e` under `TG-REC-MIG-001`; PUB-002 excluded)

Constraint: This packet does **not** authorize migration, extraction, file copy, folder creation, source promotion, canon change, external edits, commits, or app/RPC work.

---

## Purpose

Record human ratification of **planning scope** for `TG-SRC-PUB-002` (GFVP release/export packages) after read-only inventory completion. Enables exact import manifest **drafting** only — not physical import.

---

## Human Ratification Record (2026-07-07)

| Decision ID | Human Decision | Scope |
|---|---|---|
| **S1** | **APPROVED** — Default import planning scope | **46 files** from `06_GENERATED_OUTPUTS/` and `08_APPROVED_OUTPUTS/` only (21 md + 25 PNG) |
| **S2** | **APPROVED** — `07_OUTPUT_QC/` reference-only | **Not** in PUB-002 import manifest unless separately ratified |
| **S3** | **APPROVED FOR PLANNING ONLY** — Zip mirror candidate | `gradient_foundational_visual_package_batch_01_LEVEL_A_CODEX_COMPLETE_v1-0.zip.zip` on Drive is a **strong full-package mirror candidate** for planning; **not** canonical release package without later receipt/review |
| **S4** | **REAFFIRMED** — VIS-001 / PUB-002 boundary | PUB-002 is release/export scope; remains separate from VIS-001 source-system import (`ca6410e`) |
| **S5** | **NOT AUTHORIZED** — Physical import | No file copy, folder creation, or repo placement until receipt gate satisfied |

**Signoff phrase recorded:**

```text
APPROVED — TG-SRC-PUB-002 SCOPE RATIFICATION FOR PLANNING
```

**Does not authorize:** migration, import, extraction, canon promotion, treating zip as canonical release, commits, external edits, or app/RPC work.

---

## Ratified Scope Detail

### S1 — Default 46-file planning set

| Drive Folder | md | PNG | Total |
|---|---:|---:|---:|
| `06_GENERATED_OUTPUTS/` | 10 | 14 | 24 |
| `08_APPROVED_OUTPUTS/` | 11 | 11 | 22 |
| **Total** | **21** | **25** | **46** |

**Provisional destination root:** `07_publishing/series/gfvp/` (lifecycle substructure TBD in migration plan draft).

**Excluded from default set:**

- `07_OUTPUT_QC/` (14 md) — S2 reference-only
- Export zip files — planning reference only (S3); not default co-import enumeration
- PDFs — none observed
- All VIS-001 source-system folders — already imported under `06_visual_language/gfvp/`

### S2 — `07_OUTPUT_QC/` reference-only

Fourteen output QC md files remain **authority/reference metadata**. Cite in migration plan or receipt cross-refs if needed. Co-import requires separate human ratification (not granted 2026-07-07).

### S3 — Zip authority (planning only)

| Attribute | Value |
|---|---|
| Candidate path | `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01_LEVEL_A_CODEX_COMPLETE_v1-0.zip.zip` |
| Size | ~31.9 MB |
| PNG count inside | 25 (matches synced Drive `06_`/`08_` set) |
| Planning posture | Strong full-package **mirror candidate** |
| Canonical release posture | **Not designated** — requires later receipt/review |
| Partial zips in Downloads | **Not** ratified as authority (`batch_01.zip` 32 KB; `(1).zip` 4 PNGs only) |

### S4 — VIS-001 boundary

| Cluster | Status | Repo location |
|---|---|---|
| `TG-SRC-VIS-001` | Imported | `06_visual_language/gfvp/` (`ca6410e`) |
| `TG-SRC-PUB-002` | Deferred / planning only | Not in repo (0 PNGs in gfvp tree) |

Release/export materials must not be co-imported into VIS-001 lifecycle paths.

### S5 — Physical import

Physical import candidacy remains **`NOT_AUTHORIZED`**. Requires future:

1. Exact import manifest draft + human acceptance
2. Migration plan draft + human review
3. Migration receipt (provisional `TG-REC-MIG-002` or assigned ID) + signoff
4. Explicit `AUTHORIZED — EXECUTE TG-SRC-PUB-002 PHYSICAL IMPORT`

---

## Readiness Projection

| Gate | Status after this ratification |
|---|---|
| Read-only inventory | **Complete** — `TG_SRC_PUB_002_INVENTORY_DRAFT.md` |
| Planning scope ratification | **Complete** — this packet |
| Exact import manifest draft | **`READY_TO_DRAFT_EXACT_IMPORT_MANIFEST`** |
| Migration plan draft | **Not ready** — requires manifest draft + review |
| Physical import | **Not authorized** |
| Commit of import payload | **Not authorized** |

---

## Deferred (Not Ratified)

- Co-import of `07_OUTPUT_QC/` md into PUB-002 manifest
- Canonical designation of any zip as release authority
- `NTN-REC-002` P009 ambiguity resolution
- Notion GFVP receipt deep mapping
- Binary checksum / release verification workflow
- Physical import or commit authorization

---

## Output Summary

**What changed:** Recorded human planning-scope ratification for `TG-SRC-PUB-002` (S1–S5).

**What should be locked:** 46-file default scope; `07_` reference-only; VIS-001/PUB-002 separation; zip as planning mirror only; physical import not authorized.

**What remains living:** Exact import manifest drafting; migration plan; receipt; zip canonical review; optional `07_` co-import ratification.

**Concrete next steps:**

1. Authorize **`AUTHORIZED — DRAFT TG-SRC-PUB-002 EXACT IMPORT MANIFEST`** only.
2. Do not import, copy files, or commit import payload until full receipt gate.
