# CL-PHASE-02-CHARTER
## Non-Destructive Migration Planning v1.0

**Status:** AUTHORIZED FOR PLANNING ONLY  
**Date opened:** July 13, 2026  
**Physical migration authorization:** NO  
**Deletion authorization:** NO  
**Renaming authorization:** NO

---

# 1. Purpose

Phase 02 will design the exact, reversible, checksum-verified migration into:

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES
```

No file will move during planning.

# 2. Required planning outputs

## A. Target namespace blueprint

Define the new repository structure for:

- authority and canon;
- release profiles;
- collection registries;
- active volume specifications;
- builders and validators;
- migration manifests;
- active candidates;
- quarantine references;
- release manifests;
- external binary references.

## B. Collection migration sequence

Recommended order:

1. governance and registries;
2. CL-I through CL-III as historical release references;
3. CL-V as the verified modern frozen release;
4. CL-IV as a qualified frozen snapshot;
5. CL-EV-001 as `RETURN_FOR_REVISION`;
6. The Death of the Bit as a qualified `WORKING_ASSEMBLY`;
7. CL-VII only as quarantined evidence;
8. CL-VI remains unassigned and receives no collection folder.

## C. Per-collection manifests

Each migration manifest must state:

- collection ID;
- source path;
- target path;
- source relationship class;
- target relationship class;
- state dimensions;
- file count;
- byte count;
- SHA-256 values;
- external dependencies;
- path references;
- copy method;
- verification method;
- rollback method;
- exclusions;
- human authorization.

## D. Duplicate classification

Classify only duplicate groups touched by the current migration batch.

Do not attempt a global cleanup of all 1,276 groups.

## E. External binary strategy

Large binaries may remain in Drive.

The Git repository should hold:

- authoritative manifest;
- checksum;
- Drive-relative or stable reference;
- role classification;
- recovery route.

## F. Dry-run validation

Before copying, run:

- source existence checks;
- destination collision checks;
- path-reference scans;
- available disk-space checks;
- Git status checks;
- checksum-tool tests;
- rollback simulation.

# 3. Phase 02 stop conditions

Stop when:

- a source state is disputed;
- a target filename collides;
- a source hash is missing;
- an external dependency cannot be located;
- a frozen release would be altered;
- a profile is absent;
- a path reference would break;
- the destination is not clean;
- rollback cannot be demonstrated.

# 4. First recommended migration batch

The first batch should contain only governance and registries.

It should not contain PDFs, PNGs, layout sources, or collection binaries.

Proposed batch:

```text
CL-MIG-001 — GOVERNANCE_AND_REGISTRIES
```

Contents:

- ratified architecture records;
- CL-OPS cross-reference;
- CCR-CL-003;
- Release Profile Registry;
- Canonical Root Ratification;
- Mirror and Duplicate Doctrine;
- Collection State Language Standard;
- Collection State Map;
- Phase 00 evidence references;
- migration schemas and validators.

# 5. Next concrete action

Create a new dedicated Cursor chat named:

```text
CL PHASE 02 — MIGRATION PLAN ONLY
```

Attach the Phase 02 planning packet generated with this closure record.

The first Cursor run must be read-only except for writing the proposed migration plan under:

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\CL_PHASE_02_PLANNING\
```

No source file may be copied yet.
