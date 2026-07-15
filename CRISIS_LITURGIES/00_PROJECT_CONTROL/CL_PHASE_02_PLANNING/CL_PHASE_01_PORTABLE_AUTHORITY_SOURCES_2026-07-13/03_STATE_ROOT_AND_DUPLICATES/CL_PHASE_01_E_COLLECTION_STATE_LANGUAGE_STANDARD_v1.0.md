# CL-PHASE-01-E
## Collection State Language Standard v1.0

**Final disposition:** ACCEPTED WITH PATCHES  
**Ratified:** July 13, 2026  
**Ratifying authority:** Human Founder  
**Effective immediately:** YES  
**Migration authorization:** NO  
**Rendering authorization:** NO  
**Publication authorization:** NO  
**Archive-admission authorization:** NO

---

# 1. Governing principle

Crisis Liturgies state must be multidimensional.

No single word such as `FINAL`, `LOCKED`, `COMPLETE`, `RELEASED`, `PUBLIC`, or `ARCHIVED` may substitute for a complete state record.

Every collection must separately declare:

- specification state;
- production state;
- QC state;
- release state;
- print state;
- publication state;
- archive state;
- dispute or quarantine state.

# 2. Locked state vocabulary

## `CONCEPT_DEVELOPMENT`

The collection is still defining its thesis, issue sequence, or conceptual scope.

## `SPECIFICATION_DRAFT`

A specification exists but has not been ratified.

## `SPECIFICATION_FROZEN`

The governing volume specification is ratified and immutable for the current build lineage.

## `PRODUCTION_ACTIVE`

Writing, imagery, layout, assembly, repair, or rebuild work is in progress.

## `WORKING_ASSEMBLY`

A substantially assembled collection exists but has not passed all required QC or release gates.

## `CORRECTIVE_CANDIDATE`

A namespaced repair or replacement candidate exists and is under review.

## `RETURN_FOR_REVISION`

The current candidate failed a required review and may not proceed without repair.

## `QUARANTINED`

The artifact or collection is preserved but excluded from active authority because its state, provenance, quality, or validity is disputed.

## `QC_PASSED`

The relevant declared QC gates have passed for the specified candidate.

## `RELEASE_CANDIDATE`

A QC-passed candidate awaits explicit human release authorization.

## `FROZEN_RELEASE`

A checksum-locked release has received explicit human release authorization.

## `PRINT_READY`

A release candidate or frozen release satisfies its declared print-production requirements.

This state does not itself imply publication.

## `SCREEN_DERIVATIVE`

A screen-optimized derivative exists and is linked to an authoritative release or candidate.

## `PUBLICATION_AUTHORIZED`

Human authority has approved public distribution through specified channels.

## `PUBLICLY_AVAILABLE`

The artifact is reachable through a public channel.

This state does not itself prove publication authorization.

## `ARCHIVE_ADMITTED`

The Archivist has admitted the artifact into the active institutional archive after human authorization.

## `HISTORICAL_REFERENCE`

The artifact is preserved as historical evidence but does not govern current production.

## `SUPERSEDED`

A later accepted artifact occupies the former artifact's operational role.

Superseded does not mean deleted.

## `UNKNOWN_WITH_EVIDENCE_GAP`

A dimension cannot be resolved from available evidence.

The state record must identify the missing evidence and the action required to resolve it.

# 3. Named patches

## CL-PHASE-01-E-P01 — Multidimensional state records

Every official collection-state record must include all eight dimensions, even when one or more dimensions are `NONE` or `UNKNOWN_WITH_EVIDENCE_GAP`.

## CL-PHASE-01-E-P02 — Bare `FINAL` prohibited

`FINAL` may appear inside historical filenames or frozen artifacts.

It may not be used as the sole active institutional state.

## CL-PHASE-01-E-P03 — Preserve frozen historical language

Existing frozen releases retain their internal filenames, labels, and wording.

External metadata may normalize their state without modifying the artifact.

## CL-PHASE-01-E-P04 — Public availability is not publication authority

A working URL, public PDF, Netlify route, shared Drive link, or indexed file proves availability only.

It does not prove `PUBLICATION_AUTHORIZED`.

## CL-PHASE-01-E-P05 — Controlled use of unknown state

`UNKNOWN_WITH_EVIDENCE_GAP` is permitted only when the record also identifies:

- the missing evidence;
- the affected state dimension;
- the source roots already checked;
- the next verification action.

## CL-PHASE-01-E-P06 — Human acts required

The following states require explicit human action:

- `FROZEN_RELEASE`
- `PUBLICATION_AUTHORIZED`
- `ARCHIVE_ADMITTED`

No agent, builder, compiler, Cursor workflow, or Codex workflow may infer or self-grant them.

## CL-PHASE-01-E-P07 — State transitions are recorded events

Every transition into or out of:

- `RETURN_FOR_REVISION`
- `QUARANTINED`
- `RELEASE_CANDIDATE`
- `FROZEN_RELEASE`
- `PUBLICATION_AUTHORIZED`
- `ARCHIVE_ADMITTED`
- `SUPERSEDED`

must generate a dated state-change record with evidence and authority.

# 4. Locked collection states

## CL-I

- specification: `HISTORICAL_REFERENCE`
- production: complete historical production
- QC: historical pass evidence
- release: `FROZEN_RELEASE`
- print: print derivative exists
- publication: `UNKNOWN_WITH_EVIDENCE_GAP`
- archive: admitted historical release
- dispute: none

## CL-II

- specification: `HISTORICAL_REFERENCE`
- production: complete historical production
- QC: historical pass evidence
- release: `FROZEN_RELEASE`
- print: print derivative exists
- publication: `UNKNOWN_WITH_EVIDENCE_GAP`
- archive: admitted historical release
- dispute: none

## CL-III

- specification: `SPECIFICATION_FROZEN`
- production: complete
- QC: frozen archive evidence
- release: `FROZEN_RELEASE`
- print: release evidence exists
- publication: `UNKNOWN_WITH_EVIDENCE_GAP`
- archive: `ARCHIVE_ADMITTED`
- dispute: none

## CL-IV

- specification: `SPECIFICATION_FROZEN`
- production: complete frozen snapshot
- QC: incomplete for print release
- release: none verified
- print: not print-ready
- screen: `SCREEN_DERIVATIVE`
- publication: availability does not establish authority
- archive: preserved snapshot, not admitted as final print release
- dispute: qualified-state language required

## CL-V

- specification: `SPECIFICATION_FROZEN`
- production: complete
- QC: passed according to release records
- release: `FROZEN_RELEASE`
- print: `PRINT_READY`, final PDF verified
- publication: `UNKNOWN_WITH_EVIDENCE_GAP`
- archive: release snapshot and storage mirror verified
- dispute: none on existence or checksum

## CL-VI

- specification: none
- production: none
- QC: none
- release: none
- print: none
- publication: none
- archive: none
- dispute: designation unassigned

## CL-VII

- specification: `UNKNOWN_WITH_EVIDENCE_GAP`
- production: not verified
- QC: none verified
- release: none
- print: none
- publication: none
- archive: none
- dispute: `QUARANTINED`

## CL-EV-001 — The Pygmalion Machine

- specification: substantial, not reconciled as final
- production: substantial
- QC: `RETURN_FOR_REVISION`
- release: none
- print: no accepted print-ready release
- publication: not authorized
- archive: not admitted
- dispute: state and dependency reconciliation required

## The Death of the Bit

- specification: substantial special-volume candidate
- production: `WORKING_ASSEMBLY`
- QC: incomplete or internally conflicting
- release: none
- print: working proof only
- publication: not authorized
- archive: not admitted
- dispute: Boot Hymm and editorial architecture unresolved

# 5. Final lock state

```text
CL-PHASE-01-E: RATIFIED
DISPOSITION: ACCEPTED_WITH_PATCHES
BARE_FINAL_STATUS: PROHIBITED
PUBLIC_AVAILABILITY_EQUALS_AUTHORIZATION: FALSE
HUMAN_RELEASE_AUTHORITY_REQUIRED: TRUE
MIGRATION_AUTHORIZED: NO
```
