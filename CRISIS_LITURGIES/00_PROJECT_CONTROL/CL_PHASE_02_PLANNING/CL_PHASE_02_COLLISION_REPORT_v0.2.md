# CL-PHASE-02 — Collision Report v0.2

**Date:** 2026-07-13T20:10:48Z  
**Rules:** one target per item; file exists → STOP; directory exists → inspect; hash match ≠ overwrite permission.

---

# 1. Live destination occupancy

| Path | Class | MIG-001 |
|---|---|---|
| `00_CHACHIPTI_PRODUCTION_LANE/` | Premigration occupancy | EXCLUDED → CL-MIG-008 |
| `00_CHACHIPTI_PRODUCTION_LANE.zip` | Package duplicate | EXCLUDED |
| `EXPANSION_VOLUMES/` | Live EV-001 tree | UNTOUCHED |
| `00_PROJECT_CONTROL/` | Transitional control | Planning writes only |
| `00_INSTITUTIONAL_CONTROL/` | Absent | Planned durable root |
| `06_BUILDER/` | Absent | Planned schema targets |

See `CL_MIG_001_DESTINATION_OCCUPANCY.csv` for proposed-target occupancy classes.

---

# 2. Naming collision (documented, not mutated)

| ID | Subject | Disposition |
|---|---|---|
| COL-001 | `00_PROJECT_CONTROL` vs `00_INSTITUTIONAL_CONTROL` | Transitional vs durable — both kept conceptually |
| COL-002 | `EXPANSION_VOLUMES` vs `05_VOLUMES` | Expansion untouched in MIG-001 |
| COL-003 | Chachipti lane | Deferred to CL-MIG-008 |
| COL-009 | CL-VI | No directory |
| COL-010 | CL-VII | Quarantine only |

---

# 3. MIG-001 destination file collisions

From PLAN manifest: **0** `FILE_EXISTS_STOP`.  
Parent directories for durable topology are mostly **PARENT_ABSENT** (expected; creation not performed in planning).
