# CL-PHASE-02 — Target Namespace Blueprint v0.2

**Mode:** PLANNING PATCH ONLY  
**Supersedes for planning review:** `CL_PHASE_02_TARGET_NAMESPACE_BLUEPRINT.md` (original retained)  
**Date:** 2026-07-13T20:10:48Z

---

# 1. Canonical targets (unchanged)

| Role | Path |
|---|---|
| Canonical active repository | `C:\Users\steve\Projects\gradient-institution` |
| Canonical CL namespace | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES` |
| Archive / frozen-release / controlled-mirror | `C:\Users\steve\My Drive\The Gradient` |
| Legacy Death Bit handoff mirror | `C:\Users\steve\My Drive\CL_DEATH_OF_THE_BIT` |

---

# 2. Model correction (binding for v0.2)

Fields are separated:

| Field | Purpose | Allowed values |
|---|---|---|
| `artifact_role` | What kind of institutional artifact | AUTHORITY_RECORD, ACCEPTED_DECISION, RELEASE_PROFILE, STATE_RECORD, REGISTRY, SCHEMA, EVIDENCE_REFERENCE, EXTERNAL_BINARY_REFERENCE, HANDOFF_RECORD, QUARANTINE_RECORD |
| `relationship_class` | Source/target relationship doctrine | CANONICAL_ACTIVE_SOURCE, FROZEN_RELEASE, REGISTERED_MIRROR, STORAGE_MIRROR, BACKUP, PUBLICATION_DERIVATIVE, WORKING_COPY, SUPERSEDED_WORKING_COPY, ORPHANED_DUPLICATE, QUARANTINE |
| `batch_class` | Migration batch type | e.g. GOVERNANCE_AND_REGISTRIES (orthogonal) |
| `state_dimensions` | Eight collection state axes | Must use exact values from `CL_COLLECTION_STATE_MAP_v1.0` — **file currently MISSING** |

---

# 3. Topology (provisional)

`00_PROJECT_CONTROL` remains **transitional**.  
`00_INSTITUTIONAL_CONTROL` is **durable**.  
`EXPANSION_VOLUMES` remains **untouched** in Phase 02 / MIG-001.  
No CL-VI directory. CL-VII quarantine only.  
Pygmalion remains `RETURN_FOR_REVISION`. Death Bit remains `WORKING_ASSEMBLY`.

```text
CRISIS_LITURGIES/
├── 00_PROJECT_CONTROL/          # transitional
├── 00_INSTITUTIONAL_CONTROL/    # durable
├── 01_CANON/
├── 02_PRODUCTION_STANDARDS/
├── 03_RELEASE_PROFILES/
├── 04_COLLECTION_REGISTRY/
├── 05_VOLUMES/
├── 06_BUILDER/
├── 07_ACTIVE_RUNS/
├── 08_CORRECTIVE_LANES/
├── 09_RELEASE_CANDIDATES/
├── 10_FROZEN_RELEASES/
├── 11_PUBLICATION/
├── 12_ARCHIVE/
├── 13_HANDOFFS/
├── 90_QUARANTINE/
└── 99_TEMP/
```

Live occupancy today: `00_CHACHIPTI_PRODUCTION_LANE/`, `EXPANSION_VOLUMES/`, `00_PROJECT_CONTROL/`.  
Chachipti is **out of MIG-001**; deferred to `CL-MIG-008-CHACHIPTI_CLASSIFICATION`.

---

# 4. Collision / copy rules (v0.2)

- One manifest item → exactly one target path (no `+` joins).
- Existing destination file → STOP.
- Existing destination directory → inspect, do not overwrite.
- Same hash does not permit overwrite.
- Rollback uses exact `written_targets` list only.

---

# 5. External binaries

Git holds references conforming to `CL_EXTERNAL_BINARY_REFERENCE.schema.v1.1.json` (multiple locators; ≥1 portable; absolute path never sole locator).
