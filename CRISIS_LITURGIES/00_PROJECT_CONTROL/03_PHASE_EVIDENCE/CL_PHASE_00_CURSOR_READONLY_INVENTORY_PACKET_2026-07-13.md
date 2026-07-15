# CL-PHASE-00-005
## Cursor Read-Only Recursive Inventory Packet

**Status:** READY FOR EXECUTION  
**Authority:** CL-PROD-ARCH-001A / NP-010 Non-Destructive Migration  
**Mode:** READ ONLY  
**No rendering. No file repair. No moves. No renames. No deletion. No Git commit.**

# Objective

Produce a complete file-level inventory of every known Crisis Liturgies root on the Windows machine so Phase 00 can replace path claims with directly verified evidence.

# Required roots

Inspect these exact roots when they exist:

1. `C:\Users\steve\My Drive\The Gradient`
2. `C:\Users\steve\Projects\gradient-institution`
3. Any sibling folder whose name contains:
   - `CRISIS_LITURGIES`
   - `Crisis Liturgies`
   - `CL-`
   - `CL_`
   - `PYGMALION`
   - `DEATH_OF_THE_BIT`
   - `DUAL_POWER`
   - `DEPRESSIVE_INFRASTRUCTURE`
4. Known special roots:
   - `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\EXPANSION_VOLUMES\CL-EV-001_THE_PYGMALION_MACHINE`
   - `C:\Users\steve\My Drive\The Gradient\_codex_work\CL_DEATH_OF_THE_BIT_V07_20260710_145556\CL_DEATH_OF_THE_BIT`
   - any exact match for `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS`
   - any exact match for `CRISIS_LITURGIES_VII`

Do not scan unrelated personal directories beyond the named roots and name-filtered sibling folders.

# Output directory

Create only:

`C:\Users\steve\My Drive\The Gradient\00_PROJECT_CONTROL\CL_PHASE_00_DISK_INVENTORY_20260713\`

If `00_PROJECT_CONTROL` does not exist, stop and report the missing parent. Do not improvise another output location.

# Required outputs

## 1. `CL_PHASE_00_DISK_ROOTS.json`

For every inspected root:

- absolute path;
- exists true/false;
- filesystem type when available;
- file count;
- directory count;
- total byte size;
- earliest and latest modification time;
- Git repository true/false;
- current branch and commit if Git;
- read errors;
- junctions, symlinks or shortcuts encountered.

## 2. `CL_PHASE_00_FILE_INVENTORY.csv`

One row per file:

- root ID;
- absolute path;
- root-relative path;
- filename;
- extension;
- byte size;
- created time;
- modified time;
- SHA-256;
- MIME or file signature when determinable;
- duplicate hash group;
- Git tracked/untracked/ignored status when applicable;
- probable class:
  - CANON
  - SOURCE
  - PROMPT
  - GENERATED_ASSET
  - QC
  - LAYOUT
  - PDF
  - MANIFEST
  - RELEASE
  - SNAPSHOT
  - MIRROR
  - HANDOFF
  - TEMP
  - QUARANTINE
  - UNKNOWN

## 3. `CL_PHASE_00_DUPLICATE_HASH_GROUPS.json`

Include every SHA-256 present at more than one path.

Do not call duplicates redundant. Record:

- hash;
- byte size;
- paths;
- filename differences;
- probable relationship:
  - exact mirror;
  - copied working file;
  - release duplicate;
  - unknown.

## 4. `CL_PHASE_00_COLLECTION_CANDIDATES.json`

Detect and summarize candidate roots for:

- CL-I
- CL-II
- CL-III
- CL-IV
- CL-V
- CL-VI
- CL-VII
- CL-EV-001
- The Death of the Bit
- adjacent or expansion volumes

For each candidate include:

- absolute root;
- evidence files;
- issue range;
- PNG count;
- PDF count;
- manifest count;
- checksum records;
- release or lock records;
- latest state language found;
- confidence;
- conflicts.

## 5. `CL_PHASE_00_KNOWN_CHECKSUM_TESTS.json`

Explicitly test:

- CL-V final PDF expected SHA-256:
  `a86f13005aee1eecba61f80b87f72fbb6b258edad3ec5c79971c7f21559a4a46`
- CL-I screen PDF expected SHA-256:
  `68f9e6cd5ef3046be3bcf505e9d697a7d74ade4d0e63c9c81ef810be125cbc86`
- CL-II screen PDF expected SHA-256:
  `7e8a9291f4cbd2d1366fed8d9e232a4683440ee746bafccc22f08c5ee55cd9ea`

Report MATCH, MISMATCH, or NOT FOUND. Never alter a mismatching file.

## 6. `CL_PHASE_00_DISK_CONFLICTS.md`

Report:

- identical titles with different hashes;
- identical hashes at multiple paths;
- multiple `FINAL`, `LOCK`, `RELEASE`, or `RUN_STATE` claims for one volume;
- active files outside expected volume roots;
- links to missing targets;
- font dependencies outside the project;
- source assets outside the project;
- untracked generated files;
- empty or placeholder directories presented as complete lanes.

## 7. `CL_PHASE_00_DISK_INVENTORY_RECEIPT.md`

State:

- commands run;
- roots inspected;
- roots not accessible;
- files read;
- files changed: MUST BE 0 outside the output directory;
- files moved: 0;
- files deleted: 0;
- Git changes: 0;
- inventory verdict:
  - PASS
  - PASS WITH ACCESS GAPS
  - RETURN FOR SCOPE REPAIR

# Safety requirements

- Use streaming hashes.
- Do not follow symlinks or junctions outside the named roots.
- Do not open or execute binaries.
- Do not modify timestamps.
- Do not normalize line endings.
- Do not run formatters.
- Do not install dependencies.
- Do not use cloud sync operations that change file state.
- Do not commit outputs.
- Do not upload anything.
- Stop if a command would require elevated permissions.

# First action

Print the exact roots that will be scanned and the exact output directory. Then run a dry path-existence check before hashing any file.
