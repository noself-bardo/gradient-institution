# CL-MIG-001B — Builder Schemas Scope

**Batch ID:** CL-MIG-001B  
**Class:** BUILDER_SCHEMAS  
**Executable:** NO  
**Repository posture:** REPOSITORY CANDIDATE  

---

## Inclusion rules

1. Only Phase 02C revised JSON Schema files:
   - `CL_PHASE_02C_MIGRATION_MANIFEST_SCHEMA.json`
   - `CL_PHASE_02C_EXTERNAL_BINARY_REFERENCE_SCHEMA.json`
2. Source sha256 recorded.
3. Exact destination under `00_PROJECT_CONTROL/05_BUILDER_CONTRACTS/`.
4. Phase 02 schemas are **EXCLUDED** as superseded.

## Exclusion rules

- Obsolete Phase 02 schema files
- Any non-schema content
- Builder executables, installs, dependency trees
- Anything with unresolved authority

## Authority requirements

- RAT-CL-004 batch scope approval
- RAT-CL-002 repository candidate acknowledgment
- Schema validation PASS recorded
- Separate `AUTHORIZE_COPY: CL-MIG-001B`

## Required destination parent

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\05_BUILDER_CONTRACTS
```

**NOT MATERIALIZED** until RAT-CL-006.

## Destination occupancy requirement

Target filenames ABSENT; parent EXISTS at copy time; no overwrite.

## Rollback requirements

Non-destructive doctrine; freeze/mark disputed; preserve source and destination; no deletion.

## Verification requirements

- JSON Schema Draft 2020-12 check
- Byte-identical sha256 after copy
- Manifest verification_state VERIFIED

## Ratification requirements

RAT-CL-001, RAT-CL-002, RAT-CL-004, RAT-CL-005, RAT-CL-006.

## Current preflight counts (planning)

- Revised schema mapping rows: 2
- Batch is **not executable**
