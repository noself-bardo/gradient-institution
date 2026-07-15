# CL-MIG-001A — Program Governance and Registries Scope

**Batch ID:** CL-MIG-001A  
**Class:** PROGRAM_GOVERNANCE_AND_REGISTRIES  
**Executable:** NO  
**Repository posture:** REPOSITORY CANDIDATE  

---

## Inclusion rules

1. Record is Crisis Liturgies **program** governance text or program evidence register (`.md` / `.json`).
2. Source exists, is readable, and has SHA-256.
3. Exact single destination under program-local control:
   - `00_PROJECT_CONTROL/01_PROGRAM_GOVERNANCE/` for architecture / protocol exports
   - `00_PROJECT_CONTROL/03_PHASE_EVIDENCE/` for Phase 00/00B/00C evidence registers
4. Destination is not compound; no inference.
5. Authority state must be resolved **before** eligibility for copy (currently all blocked).
6. Destination parent must exist and be vacant for the target filename before COPY mode.
7. Rollback reference includes source path + sha256.

## Exclusion rules

- Binaries, zip packages, `.gdoc` stubs
- Drive inventory payloads / tooling (external reference only)
- Chachipti components (until RAT-CL-008)
- AUTHOR_FROM_RATIFICATION placeholders without authored sources
- Gradient institutional constitution / stewardship files (reference only — never copy into CL)
- Collection production assets, releases, proofs
- CL-VI any form
- Any unresolved-authority file (Rule 13)

## Authority requirements

- RAT-CL-002 repository candidate acknowledgment
- RAT-CL-003 batch scope approval
- RAT-CL-001 program-local topology
- Per-file authority_evidence recorded
- Separate `AUTHORIZE_COPY: CL-MIG-001A` before any copy

## Required destination parent

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\01_PROGRAM_GOVERNANCE
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE
```

Both currently **NOT MATERIALIZED**. Materialization requires RAT-CL-006 (not this phase).

## Destination occupancy requirement

Target file must be **ABSENT**. Overwrite prohibited. Parent must **EXISTS** at copy time.

## Rollback requirements

Follow `CL_PHASE_02C_NON_DESTRUCTIVE_ROLLBACK_DOCTRINE.md`.  
**ROLLBACK IS NOT DELETION.**

## Verification requirements

- Pre-copy dry-run with zero stop results
- Post-copy sha256 match to source_hash
- Manifest item verification_state → VERIFIED
- Schema validation against CL_PHASE_02C_MIGRATION_MANIFEST_SCHEMA.json

## Ratification requirements

RAT-CL-001, RAT-CL-002, RAT-CL-003, RAT-CL-005, RAT-CL-006 (and RAT-CL-007 before registry authorship admits).

## Current preflight counts (planning)

- Governance remap candidates (blocked on authority/parent): 19
- Batch is **not executable**
