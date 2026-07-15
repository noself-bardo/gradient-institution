# CL-MIG-001-AUTH
## Copy-Only Migration Authorization Record v1.0

**Status:** AUTHORIZED  
**Authorized:** July 13, 2026  
**Authorizing authority:** Human Founder  
**Authorization phrase:** `Authorize CL-MIG-001 copy-only migration with checksum verification and no source retirement.`

# Authorized scope

The authorized operation is limited to:

- creating the nine exact destination parent directories required by the validated manifest;
- copying the 38 exact planned files;
- refusing all overwrites;
- verifying destination byte counts and SHA-256 values;
- writing execution, exception, verification, and rollback records;
- leaving every source file and source directory unchanged.

# Prohibited

This authorization does not permit:

- deleting, moving, renaming, or retiring any source;
- overwriting any target;
- modifying file contents;
- copying Chachipti materials;
- executing `CL-MIG-008`;
- building, rendering, publishing, or archive-admitting;
- changing collection states;
- changing frozen releases;
- committing to Git;
- cleaning up duplicate files;
- removing planning artifacts.

# Locked execution facts

- batch: `CL-MIG-001 — GOVERNANCE_AND_REGISTRIES`
- exact copy candidates: 38
- deferred candidates: 1
- deferred item: `MIG-0039`
- deferred destination: Chachipti classification under `CL-MIG-008`
- expected existing target files: 0
- required destination parent directories: 9
- source retirement: prohibited
- rollback mode: remove only files and empty directories created by this run, and only after an explicit rollback command

# Stop conditions

The execution must stop before writing when:

- the COPY manifest fails schema validation;
- a source is missing, unreadable, or hash-mismatched;
- a target file already exists;
- a target path differs from the manifest;
- a path-reference STOP is detected;
- a source would be altered;
- a command would delete, move, rename, build, render, publish, archive-admit, or commit;
- the copy count would exceed 38;
- Chachipti would be included.

# Completion requirement

A successful execution must return:

```text
PASS — CL-MIG-001 COPY COMPLETE; 38/38 VERIFIED; SOURCES RETAINED
```

Any exception must stop the run and return:

```text
STOP — CL-MIG-001 COPY INCOMPLETE; NO SOURCE RETIREMENT PERFORMED
```
