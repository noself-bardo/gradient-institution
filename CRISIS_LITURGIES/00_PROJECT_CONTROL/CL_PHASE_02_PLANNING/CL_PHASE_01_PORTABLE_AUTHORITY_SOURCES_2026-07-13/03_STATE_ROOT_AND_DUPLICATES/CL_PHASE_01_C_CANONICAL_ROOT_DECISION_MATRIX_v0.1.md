# CL-PHASE-01-C
## Canonical Operational Root Decision Matrix v0.1

**Status:** RECOMMENDATION / NO MIGRATION AUTHORIZED  
**Date:** 2026-07-13  
**Evidence source:** CL-PHASE-00 disk inventory

# 1. Recommendation

Designate the following as the **canonical active operational repository**:

```text
C:\Users\steve\Projects\gradient-institution
```

Designate the Crisis Liturgies operational namespace within it as:

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES
```

Designate the following as the **institutional archive, frozen-release, and controlled mirror root**:

```text
C:\Users\steve\My Drive\The Gradient
```

Designate the following as a **legacy handoff mirror pending incorporation**:

```text
C:\Users\steve\My Drive\CL_DEATH_OF_THE_BIT
```

# 2. Why this is the correct split

The institution needs one logical active source of truth, but it does not need all large binaries in one physical service.

`gradient-institution` is the strongest active-root candidate because it has:

- a valid Git repository;
- a known `main` branch;
- a known commit;
- active institutional implementation material;
- the Pygmalion tree;
- the verified CL-V tree;
- machine-operable repository structure;
- better suitability for schemas, validators, build locks, and change review.

`The Gradient` Drive root is not a suitable active code and state authority because:

- all 3,706 inventoried files were reported as untracked;
- no valid branch or commit was recovered;
- it mixes release assemblies, snapshots, outputs, QC, prompts, archive records, and Codex work;
- it is optimized for storage and historical continuity rather than deterministic execution;
- Google Drive synchronization creates a greater risk of partial-state and duplicate-root ambiguity.

The Drive root remains indispensable as:

- frozen release storage;
- storage mirror;
- historical archive;
- large-binary repository;
- human-accessible institutional record;
- publication derivative source.

# 3. Scored matrix

Scale: 1 = poor, 5 = strong.

| Criterion | `gradient-institution` | `The Gradient` Drive root | Death Bit handoff root |
|---|---:|---:|---:|
| Valid Git lineage | 5 | 1 | 0 |
| Machine-readable operational suitability | 5 | 2 | 1 |
| Existing active CL implementation | 5 | 4 | 1 |
| Frozen-release and archive completeness | 2 | 5 | 1 |
| Large-binary suitability | 2 | 5 | 2 |
| Path stability for builders | 5 | 3 | 2 |
| Separation of active and frozen state | 4 | 1 | 2 |
| Change review and rollback | 5 | 1 | 1 |
| Portability | 4 | 3 | 2 |
| Migration risk if selected | 3 | 2 | 1 |
| **Operational-root score** | **40** | **27** | **13** |

# 4. Conditions before ratification

The recommendation may be ratified only with these conditions:

1. Frozen releases remain in place until copied and checksum-verified.
2. The active repository stores manifests and authoritative references to large binaries.
3. Drive mirrors cannot generate active state.
4. Every imported collection receives a migration manifest.
5. No existing legacy root is deleted during initial migration.
6. Pygmalion, CL-VII, and Death Bit remain quarantined or qualified according to their current states.
7. The final repository structure is created as a new namespace, not by reorganizing existing folders in place.

# 5. Recommended disposition

**ACCEPT AS THE PHASE 02 TARGET ROOT, SUBJECT TO PHASE 01 PROFILE AND DUPLICATE-DOCTRINE RATIFICATION.**
