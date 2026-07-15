# CL-MIG-001 — Governance and Registries Plan v0.2

**Batch ID:** CL-MIG-001  
**batch_class:** GOVERNANCE_AND_REGISTRIES  
**Mode:** PLAN only (`copy_authorized: false`)  
**File-level manifest:** `CL_MIG_001_MIGRATION_MANIFEST_PLAN.json`  
**Date:** 2026-07-13T20:10:48Z

---

# 1. Scope (corrected)

Includes only:

- governance / authority records;
- ratified decisions (when durable sources exist);
- registries (when ratification sources exist);
- schemas;
- state records (when `CL_COLLECTION_STATE_MAP_v1.0` exists);
- evidence references.

## Explicit exclusions

```text
CRISIS_LITURGIES\00_CHACHIPTI_PRODUCTION_LANE
CRISIS_LITURGIES\00_CHACHIPTI_PRODUCTION_LANE.zip
```

Planning-only placeholder batch:

```text
CL-MIG-008-CHACHIPTI_CLASSIFICATION
```

No Chachipti classify/copy in this run.  
`EXPANSION_VOLUMES` untouched. No collection binaries.

---

# 2. Counts from file-level PLAN manifest

| Metric | Count |
|---|---:|
| Total items | 40 |
| PLANNED COPY_FILE | 21 |
| BLOCKED | 18 |
| DEFERRED | 1 |
| written_targets (planned) | 21 |

---

# 3. Copy method rules

| item_kind | Requires |
|---|---|
| COPY_FILE | exact source path, exists, byte_count, SHA-256, exact target, occupancy, artifact_role, relationship_class |
| AUTHOR_NEW_RECORD | exact ratification source + SHA-256 + output schema; else BLOCKED |
| DEFERRED | placeholder only |

One item → one target path. Destination file exists → STOP.

---

# 4. Rollback

Method: `DELETE_WRITTEN_TARGETS_ONLY` using `written_targets`.  
Sources untouched. Deletion of sources prohibited.  
Rollback fixture drill **not executed** in Phase 02A.

---

# 5. Dry-run readiness

CL-MIG-001 is **not** fully ready for an unqualified dry-run greenlight while blocked ZIP exports and Phase 01 A–E / state-map files remain missing.

PLANNED subset (durable Drive control `.md`/`.json` + schemas) may be dry-run reviewed as a **partial** set after human acceptance of remaining gaps.
