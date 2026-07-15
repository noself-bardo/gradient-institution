# CL-MIG-001-EXEC
## Cursor Copy-Only Migration Execution Packet

Use the existing Cursor chat:

```text
CL PHASE 02 — MIGRATION PLAN ONLY
```

This chat may now execute one bounded copy-only migration batch.

# Attach these files

1. `CL_MIG_001_COPY_ONLY_AUTHORIZATION_RECORD_v1.0.md`
2. `CL_MIG_001_MIGRATION_MANIFEST_COPY_v1.2.1.json`
3. `CL_MIGRATION_MANIFEST.schema.v1.2.json`

# Governing paths

Repository:

```text
C:\Users\steve\Projects\gradient-institution
```

Crisis Liturgies namespace:

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES
```

Planning and receipt directory:

```text
C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\CL_PHASE_02_PLANNING
```

# Authorized operation

Execute exactly the 38 `PLANNED` items in:

```text
CL_MIG_001_MIGRATION_MANIFEST_COPY_v1.2.1.json
```

You may:

- validate the schema and manifest;
- re-read and hash every source before copy;
- create only the exact missing destination parent directories;
- copy each exact file to its exact target path;
- verify destination bytes and SHA-256;
- write execution evidence inside the planning directory.

# Absolute prohibitions

Do not:

- overwrite any file;
- copy an item not present in the manifest;
- alter, move, rename, delete, or retire any source;
- include `MIG-0039`;
- execute `CL-MIG-008`;
- modify frozen releases;
- change collection state;
- build, render, publish, or archive-admit;
- commit;
- run cleanup or duplicate removal;
- remove planning files;
- infer a replacement source.

# Gate 1 — authorization integrity

Before any target write:

1. Confirm all three attached files exist.
2. Compute and record their SHA-256 values.
3. Validate the schema as Draft 2020-12.
4. Validate the COPY manifest against it.
5. Confirm:
   - `mode = COPY`
   - `copy_authorized = true`
   - human authorization record is nonempty
   - deletion authorization is false
   - source rename authorization is false
   - builder authorization is false
   - commit authorization is false
   - 38 planned items
   - 1 deferred item
   - deferred item is `MIG-0039`

If any check fails, stop before creating a directory or copying a file.

# Gate 2 — pre-copy source and target validation

For all 38 planned items:

- source exists;
- source is a regular readable file;
- source byte count matches;
- source SHA-256 matches;
- target file does not exist;
- target path exactly matches the manifest;
- no duplicate target exists;
- no path-reference STOP exists.

If any item fails, stop before the first copy.

# Gate 3 — exact parent-directory creation

Create only the missing parent directories required by the 38 target paths.

Record every created directory in:

```text
CL_MIG_001_CREATED_DIRECTORIES.csv
```

Do not create speculative topology beyond the manifest targets.

# Gate 4 — copy and immediate verification

Copy one item at a time.

After each copy:

1. verify destination byte count;
2. verify destination SHA-256;
3. append the result to the execution ledger;
4. stop immediately if verification fails.

Do not continue after a mismatch.

# Required execution outputs

Write only inside the planning directory:

1. `CL_MIG_001_COPY_EXECUTION_LEDGER.csv`
2. `CL_MIG_001_CREATED_DIRECTORIES.csv`
3. `CL_MIG_001_COPY_EXCEPTIONS.csv`
4. `CL_MIG_001_POST_COPY_VERIFICATION.csv`
5. `CL_MIG_001_SOURCE_RETENTION_CHECK.csv`
6. `CL_MIG_001_PATH_REFERENCE_POST_COPY.csv`
7. `CL_MIG_001_ROLLBACK_MANIFEST.json`
8. `CL_MIG_001_COPY_EXECUTION_REPORT.md`
9. `CL_MIG_001_COPY_EXECUTION_RECEIPT.md`
10. `SHA256SUMS_CL_MIG_001_EXECUTION.txt`

# Required verification

The final report must prove:

- 38 / 38 source files retained;
- 38 / 38 destination files created;
- 38 / 38 destination byte counts matched;
- 38 / 38 destination SHA-256 values matched;
- 0 overwrites;
- 0 source changes;
- 0 source deletions;
- 0 source moves or renames;
- 0 unmanifested copies;
- 0 Chachipti files copied;
- 0 Git commits;
- rollback manifest lists only files and directories created by this run.

# Rollback rule

Do not execute rollback automatically.

The rollback manifest may list:

- the 38 created destination files;
- only directories created by this run;
- deletion order for a future explicitly authorized rollback.

It may not list any source file.

# Completion verdict

Return exactly one:

```text
PASS — CL-MIG-001 COPY COMPLETE; 38/38 VERIFIED; SOURCES RETAINED
```

or:

```text
STOP — CL-MIG-001 COPY INCOMPLETE; NO SOURCE RETIREMENT PERFORMED
```

Do not commit after completion.
