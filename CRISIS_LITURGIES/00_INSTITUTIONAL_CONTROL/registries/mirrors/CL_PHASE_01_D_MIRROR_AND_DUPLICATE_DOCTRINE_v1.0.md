# CL-PHASE-01-D
## Mirror and Duplicate Doctrine v1.0

**Final disposition:** ACCEPTED WITH PATCHES  
**Ratified:** July 13, 2026  
**Ratifying authority:** Human Founder  
**Effective immediately:** YES  
**Migration authorization:** NO  
**Deletion authorization:** NO  
**Renaming authorization:** NO  
**Rendering authorization:** NO

---

# 1. Governing principle

A duplicate hash establishes content identity.

It does not establish institutional redundancy.

Two files with the same SHA-256 may occupy different legitimate institutional roles. No file may be deleted, replaced, or retired solely because another file has the same hash.

# 2. Locked relationship classes

## `CANONICAL_ACTIVE_SOURCE`

The authoritative editable machine source.

Rules:

- exists inside the canonical active repository;
- is Git-governed;
- may generate candidates;
- cannot overwrite frozen releases;
- only one active authoritative instance may originate machine state for a given artifact identity.

## `FROZEN_RELEASE`

An immutable release artifact accepted by human authority.

Rules:

- checksum-locked;
- never overwritten;
- corrections produce a new version or namespaced candidate;
- may have registered mirrors;
- remains authoritative even when copied elsewhere.

## `REGISTERED_MIRROR`

An intentionally maintained exact copy of a canonical artifact.

Rules:

- declares its source;
- preserves the source checksum;
- cannot originate state;
- drift creates an exception requiring review.

## `STORAGE_MIRROR`

A preservation copy optimized for recovery rather than active use.

Rules:

- may be Drive-based or offline;
- retains a manifest and recovery route;
- cannot be treated as the active source;
- may preserve large binaries referenced by the Git repository.

## `BACKUP`

A time-bound or policy-bound recovery copy.

Rules:

- records source and creation time;
- may have finite retention;
- cannot be deleted merely because another copy exists;
- retirement requires the applicable retention policy.

## `PUBLICATION_DERIVATIVE`

A web, screen, print, compressed, or platform-specific derivative.

Rules:

- remains linked to the authoritative release;
- is not interchangeable with the master artifact;
- public availability does not equal institutional publication authority;
- derivative status must identify format and source release.

## `WORKING_COPY`

An active but non-authoritative editable or exported copy.

Rules:

- must not be represented as final;
- may be replaced during production;
- should declare its parent source when known;
- cannot become canonical by path age, modification time, or filename alone.

## `SUPERSEDED_WORKING_COPY`

A working copy displaced by a later accepted working state.

Rules:

- may be retained for provenance;
- may later become eligible for quarantine or retirement;
- cannot be deleted until dependency, reference, and recovery checks pass.

## `ORPHANED_DUPLICATE`

An exact copy with no verified institutional role.

Rules:

- remains preserved pending classification;
- cannot be selected as canonical by filename, age, or location alone;
- may become retirement-eligible only after provenance review.

## `QUARANTINE`

A preserved artifact excluded from active authority because its state, provenance, quality, or purpose is disputed.

Rules:

- cannot feed the builder;
- cannot be published or archive-admitted as accepted work;
- cannot be deleted merely because it is rejected;
- remains available as evidence.

# 3. Named patches

## CL-PHASE-01-D-P01 — Batch classification

The institution is not required to classify all 1,276 duplicate-hash groups before any future work can proceed.

Classification occurs:

- by collection;
- by migration batch;
- by release family;
- when a duplicate group becomes operationally relevant.

## CL-PHASE-01-D-P02 — No automated deletion

No automated tool, agent, script, builder, Cursor workflow, or Codex workflow may delete a duplicate based solely on hash identity or class assignment.

Deletion requires explicit human authorization.

## CL-PHASE-01-D-P03 — Preserve quarantine evidence

Quarantined and rejected materials remain evidence.

Quarantine is not a disposal category.

## CL-PHASE-01-D-P04 — Path-reference scan

Before retirement, the system must scan for references to the current path in:

- manifests;
- build scripts;
- configuration;
- HTML or web manifests;
- publication records;
- QC records;
- handoff packets;
- repository documentation.

## CL-PHASE-01-D-P05 — Distributed binary authority

Large binaries may remain in the Drive archive or storage mirror while authoritative manifests, checksums, and state records live in the Git repository.

The canonical active repository does not need to physically contain every large frozen binary.

## CL-PHASE-01-D-P06 — Per-artifact relationship records

A duplicate relationship record must identify:

- artifact identity;
- SHA-256;
- current path;
- relationship class;
- authoritative parent;
- collection;
- state;
- dependency status;
- migration batch;
- disposition authority.

## CL-PHASE-01-D-P07 — Retirement is separate from migration

Successful migration does not itself authorize deletion or retirement of a legacy source.

Retirement is a later, separately authorized event.

# 4. Locked precedence of authority

When exact copies exist, decision-origin authority is evaluated in this order:

1. `FROZEN_RELEASE`
2. `CANONICAL_ACTIVE_SOURCE`
3. `REGISTERED_MIRROR`
4. `STORAGE_MIRROR`
5. `BACKUP`
6. `PUBLICATION_DERIVATIVE`
7. `WORKING_COPY`
8. `SUPERSEDED_WORKING_COPY`
9. `QUARANTINE`
10. `ORPHANED_DUPLICATE`

This precedence determines which artifact may originate state. It does not authorize the removal of lower-ranked copies.

# 5. Locked deletion gate

A file may be considered for retirement or deletion only when all are true:

1. it has an assigned relationship class;
2. it is not the only copy occupying its institutional role;
3. source and retained-copy hashes match;
4. no manifest or document references its current path;
5. no build, publication, QC, or recovery process depends on it;
6. a retained copy exists in the correct authority domain;
7. rollback is possible;
8. the action appears in an approved migration or retirement manifest;
9. explicit human authorization has been issued.

# 6. Initial known classifications

## CL-V final PDF

- print-assembly final:
  `WORKING_COPY` or `CANONICAL_ACTIVE_SOURCE`, pending exact release-origin review;
- release snapshot copy:
  `FROZEN_RELEASE`;
- storage mirror copy:
  `STORAGE_MIRROR`.

No copy is deleted.

## CL-I and CL-II screen PDFs

The verified `09_RELEASES` files are `FROZEN_RELEASE` or registered release derivatives, subject to their manifests.

## The Death of the Bit Drive root

The 22-file Drive root is a legacy handoff mirror and must be classified under `REGISTERED_MIRROR`, `STORAGE_MIRROR`, or `QUARANTINE` at migration time. It is not an active operational source.

# 7. Final lock state

```text
CL-PHASE-01-D: RATIFIED
DISPOSITION: ACCEPTED_WITH_PATCHES
DUPLICATE_HASH_EQUALS_REDUNDANCY: FALSE
AUTOMATED_DELETION: PROHIBITED
QUARANTINE_IS_DISPOSAL: FALSE
MIGRATION_AUTHORIZED: NO
```
