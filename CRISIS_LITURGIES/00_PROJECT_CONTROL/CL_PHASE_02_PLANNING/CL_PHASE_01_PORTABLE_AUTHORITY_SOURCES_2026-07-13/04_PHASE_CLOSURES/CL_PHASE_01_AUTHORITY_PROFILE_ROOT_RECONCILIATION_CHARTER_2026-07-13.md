# CL-PHASE-01-CHARTER
## Authority, Profile, and Root Decision Reconciliation

**Status:** AUTHORIZED / NOT YET COMPLETE  
**Date opened:** 2026-07-13  
**Authority:** CL-PROD-ARCH-001A and CL-PHASE-00-FINAL  
**Lead:** CL-CONV-001 — The Crisis Liturgies Conversion Architect  
**Migration authorization:** NO

---

# 1. Purpose

Phase 01 converts the evidence recovered in Phase 00 into a single, contradiction-free governance and production decision layer.

It will resolve:

1. the relationship between CL-OPS-001 and CL-PROD-ARCH-001;
2. the final authority hierarchy used by the builder;
3. the release-profile framework;
4. the four-page functional-code question;
5. the criteria for selecting the canonical operational root;
6. the permitted roles of legacy roots, mirrors, backups, publication derivatives, and active repositories;
7. the exact boundaries of Chachipti, Codex, Cursor, the builder, the Archivist, and CL-CONV-001.

# 2. Phase 01 workstreams

## Workstream A — Governance reconciliation

Produce one cross-reference record stating:

- CL-OPS-001 governs role execution and operational sequence;
- CL-PROD-ARCH-001A governs the broader system structure and locked institutional constraints;
- neither supersedes Crisis Liturgies Canon, accepted Canon Change Reports, or CL-GEN-STD-001;
- conflicts between them must stop execution rather than be interpreted by an agent.

Deliverable:

```text
CL-PHASE-01-A_GOVERNANCE_CROSS_REFERENCE_v1.0.md
```

## Workstream B — Release-profile decision

Resolve CCR-CL-003.

Possible outcomes:

1. ACCEPT as written;
2. ACCEPT WITH PATCHES;
3. REJECT and preserve profile-specific page systems;
4. RETURN FOR REVISION.

The decision must establish whether the invariant functions are:

- `RELIC_ENTRY`
- `WITNESS_RECORD`
- `SYSTEM_TRANSLATION`
- `ARCHIVE_DISPOSITION`

and how profile-specific display labels map to them.

Deliverables:

```text
CCR-CL-003_FINAL_DISPOSITION.md
CL_RELEASE_PROFILE_REGISTRY_v0.1.json
```

## Workstream C — Canonical-root decision criteria

Do not choose the root by intuition.

Evaluate each principal root against:

- institutional authority;
- repository completeness;
- Git lineage;
- source completeness;
- build-system compatibility;
- dependency containment;
- naming stability;
- Drive synchronization behavior;
- release and archive separation;
- recovery and backup integrity;
- portability;
- ability to prevent unregistered writes.

Deliverable:

```text
CL-PHASE-01-C_CANONICAL_ROOT_DECISION_MATRIX_v0.1.md
```

## Workstream D — Mirror and duplicate doctrine

Define relationships before cleanup:

- canonical active source;
- frozen release;
- registered mirror;
- storage mirror;
- backup;
- publication derivative;
- working copy;
- superseded working copy;
- orphaned duplicate;
- quarantine.

No duplicate may be deleted merely because its hash matches another file.

Deliverable:

```text
CL-PHASE-01-D_MIRROR_AND_DUPLICATE_DOCTRINE_v0.1.md
```

## Workstream E — State-language normalization

Create one normalized state vocabulary for:

- frozen release;
- print-ready;
- screen derivative;
- publication authorized;
- publicly released;
- working proof;
- corrective candidate;
- quarantined;
- historical reference.

Apply it first to:

- CL-IV;
- CL-V;
- Pygmalion;
- The Death of the Bit;
- CL-VII.

Deliverables:

```text
CL-PHASE-01-E_STATE_LANGUAGE_STANDARD_v0.1.md
CL_PHASE_01_COLLECTION_STATE_MAP_v0.1.json
```

# 3. Phase 01 stop conditions

Stop and request human disposition when:

- CCR-CL-003 cannot be resolved from existing decisions;
- two locked records appear to occupy the same authority level;
- canonical-root selection would require deleting or moving files;
- root evidence is incomplete;
- profile mapping would alter an existing frozen release;
- a collection designation would need to be invented;
- an agent would need to infer archive or publication state.

# 4. Phase 01 exit conditions

Phase 01 passes only when:

- governance records are explicitly cross-referenced;
- release profiles are ratified or intentionally left distinct;
- the authority hierarchy is unambiguous;
- one canonical-root recommendation is produced with scored evidence;
- mirror and duplicate roles are defined;
- collection state language is normalized;
- no migration has occurred.

# 5. Next irreversible milestone

The next irreversible milestone remains:

**Selection and creation of the canonical Crisis Liturgies operational root.**

That milestone belongs to Phase 02 and requires separate human authorization after Phase 01.
