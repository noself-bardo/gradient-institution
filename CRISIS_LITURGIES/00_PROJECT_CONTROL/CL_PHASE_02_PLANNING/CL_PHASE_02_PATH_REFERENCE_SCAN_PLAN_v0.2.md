# CL-PHASE-02 — Path Reference Scan Plan v0.2

**Date:** 2026-07-13T20:10:48Z  
**Executed for:** CL-MIG-001 planned COPY_FILE text/json sources (read-only)  
**Results:** `CL_MIG_001_PATH_REFERENCE_HITS.csv`, `CL_MIG_001_PATH_REFERENCE_BREAKAGE_RISK.json`

---

# 1. Scope

Scan only files selected as PLANNED `COPY_FILE` items for CL-MIG-001.

Skip binaries. Do not rewrite sources. Do not run rollback drill.

---

# 2. Pattern families

| Family | Risk default |
|---|---|
| ABS_PATH | WARN (rewrite only on copied targets if later authorized) |
| DRIVE_ROOT_REF | WARN |
| LEGACY_TOPOLOGY_REF | WARN |
| URL_STATE_CLAIM | WARN (Q-014; not publication proof) |
| READ_ERROR | STOP |

---

# 3. This-run results

- files_scanned: 21
- hits: 33
- STOP: 0
- WARN: 33

Dry-run pass criterion remains: zero unresolved STOP.
