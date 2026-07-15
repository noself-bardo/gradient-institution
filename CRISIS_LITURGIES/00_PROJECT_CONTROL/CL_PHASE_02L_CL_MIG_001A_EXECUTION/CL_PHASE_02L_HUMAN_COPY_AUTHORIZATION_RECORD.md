# CL_PHASE_02L — Human Copy Authorization Record

**Phase:** CL_PHASE_02L — CL-MIG-001A Controlled Copy, Sidecar Creation, and Verification

**Authorization ID:** AUTH-COPY-CL-MIG-001A

**Batch ID:** CL-MIG-001A

**Recorded at (UTC):** 2026-07-14T17:43:45Z

**Repository posture:** ACTIVE REPOSITORY CANDIDATE — PERMANENT INSTITUTIONAL AUTHORITY NOT RATIFIED

---

## Exact human authorization (verbatim)

```text
AUTHORIZE COPY: CL-MIG-001A ONLY.

Authorize the controlled creation of the complete CL-MIG-001A execution bundle according to AUTH-COPY-CL-MIG-001A and the Phase 02J complete execution bundle.

Authorized destination parents:

C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\01_PROGRAM_GOVERNANCE

C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE

Authorized execution scope:

* 18 ratified source-file copies
* 17 associated `.admission.json` sidecars
* 35 total destination artifacts

Authorization conditions:

1. Recalculate and verify every source SHA-256 immediately before copying.
2. Stop the batch before creating any destination artifact if any source hash differs from the Phase 02J record.
3. Stop if any exact source-copy or sidecar destination already exists.
4. Copy sources without modifying their content, filenames, or source locations.
5. Create sidecars only from the exact canonical payloads and hashes recorded in Phase 02J.
6. Verify every copied source file against its authorized source SHA-256.
7. Verify every generated sidecar against its authorized payload SHA-256.
8. Preserve every source file unchanged.
9. Apply the deterministic creation order recorded in Phase 02J.
10. RAT-FILE-CL-002 remains deferred and excluded.
11. Do not execute CL-MIG-001B again.
12. Do not create additional parents, subfolders, files, sidecars, or placeholders.
13. Do not move, rename, replace, overwrite, or delete any file.
14. Do not stage or commit repository changes.
15. ROLLBACK IS NOT DELETION.

This authorization applies only to the 35 destination artifacts specified for CL-MIG-001A in the Phase 02J execution bundle. It does not authorize Git staging, commit, publication, rendering, deployment, deletion, Chachipti classification, or any deferred record.
```
