# CL_PHASE_02K — HUMAN COPY AUTHORIZATION RECORD

**Phase:** CL_PHASE_02K — CL-MIG-001B Controlled Copy and Verification  
**Recorded (UTC):** 2026-07-14T12:20:59Z  
**Repository posture:** ACTIVE REPOSITORY CANDIDATE — PERMANENT INSTITUTIONAL AUTHORITY NOT RATIFIED  
**Authorization scope:** CL-MIG-001B ONLY  

---

## Human authorization (quoted exactly)

```text
AUTHORIZE COPY: CL-MIG-001B ONLY.

Authorize the controlled copy of RAT-FILE-CL-020 and RAT-FILE-CL-021 according to AUTH-COPY-CL-MIG-001B and the Phase 02J complete execution bundle.

Authorized destination parent:

C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\05_BUILDER_CONTRACTS

Authorization conditions:

1. Recalculate and verify each source SHA-256 immediately before copying.
2. Stop if either source hash differs from the Phase 02J record.
3. Stop if either exact destination file already exists.
4. Copy each source without modifying its content, filename, timestamps where preservable, or source location.
5. Verify the SHA-256 of each destination copy against its authorized source hash.
6. Preserve every source file unchanged.
7. Record the approved interpretation of `canonical_repo_root` in the batch execution receipt:
   “The Crisis Liturgies program root within the active repository candidate. It does not declare permanent Gradient repository authority.”
8. Create no admission sidecars.
9. Create no additional destination parent or destination file.
10. Do not execute CL-MIG-001A.
11. Do not move, rename, replace, overwrite, or delete any file.
12. Do not stage or commit repository changes.
13. ROLLBACK IS NOT DELETION.

This authorization applies only to the two CL-MIG-001B source copies. It does not authorize CL-MIG-001A, Git staging, commit, publication, rendering, deployment, or deletion.
```

---

## Authorized files

| ratification_decision_id | destination_artifact_id | source_filename | authorization_id | batch_id |
|---|---|---|---|---|
| RAT-FILE-CL-020 | DEST-ART-036 | CL_PHASE_02C_MIGRATION_MANIFEST_SCHEMA.json | AUTH-COPY-CL-MIG-001B | CL-MIG-001B |
| RAT-FILE-CL-021 | DEST-ART-037 | CL_PHASE_02C_EXTERNAL_BINARY_REFERENCE_SCHEMA.json | AUTH-COPY-CL-MIG-001B | CL-MIG-001B |

## Authorized destination parent

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\05_BUILDER_CONTRACTS
```

## Binding control sources (read only)

- `CRISIS_LITURGIES\00_PROJECT_CONTROL\CL_PHASE_02H_FILE_AUTHORITY_ADJUDICATION`
- `CRISIS_LITURGIES\00_PROJECT_CONTROL\CL_PHASE_02I_AUTHORITY_RATIFICATION_AND_COPY_PREFLIGHT`
- `CRISIS_LITURGIES\00_PROJECT_CONTROL\CL_PHASE_02J_COMPLETE_EXECUTION_BUNDLE`

Phase 02J sources of truth:

- `CL_PHASE_02J_COMPLETE_DESTINATION_ARTIFACT_REGISTER.csv`
- `CL_PHASE_02J_CL_MIG_001B_FINAL_AUTHORIZATION_PACKET.md`

## Explicit exclusions

- CL-MIG-001A: NOT AUTHORIZED
- Admission sidecars: NOT AUTHORIZED
- Git staging / commit / push / pull / fetch / checkout / reset / restore / clean: NOT AUTHORIZED
- Move / rename / replace / overwrite / delete: NOT AUTHORIZED
- Build / render / publish / deploy: NOT AUTHORIZED

## Rollback doctrine

ROLLBACK IS NOT DELETION.
