# CL-PHASE-00C-PATCH
## Disk Inventory Package Integrity Patch

**Mode:** READ ONLY EXCEPT INSIDE THE EXISTING INVENTORY OUTPUT DIRECTORY  
**Do not rescan or rehash the 5,173 source files unless a source-file hash is missing.**  
**Do not modify any Crisis Liturgies source, release, repository, or mirror.**

# Objective

Make the existing `CL_PHASE_00_DISK_INVENTORY_20260713` package internally consistent after the Roman-numeral collection matcher correction.

# Existing output directory

```text
C:\Users\steve\My Drive\The Gradient\00_PROJECT_CONTROL\CL_PHASE_00_DISK_INVENTORY_20260713\
```

# Required actions

1. Determine exactly which output files changed after the matcher correction.
2. Confirm whether `CL_PHASE_00_FILE_INVENTORY.csv` itself changed.
3. Confirm whether any individual source-file SHA-256 values changed or were recomputed.
4. Re-run only the derived collection-candidate classification if necessary.
5. Regenerate the output-package manifest and `SHA256SUMS.txt` from the final post-correction outputs.
6. Add `CL_PHASE_00_POST_CORRECTION_RECEIPT.md` stating:
   - files in the output directory that changed;
   - whether source files were re-read;
   - whether source-file hashes changed;
   - whether only derived classifications changed;
   - final output count;
   - final package checksum status.
7. Zip the entire output folder as `CL_PHASE_00_DISK_INVENTORY_20260713_FINAL.zip`.

# Prohibitions

- no source-file edits;
- no source-file moves;
- no source-file deletion;
- no repository commits;
- no rendering;
- no migration;
- no duplicate cleanup;
- no renumbering;
- no interpretation of disputed volume states.

# Completion verdict

Return one:

- `PASS — PACKAGE INTERNALLY CONSISTENT`
- `PASS WITH DOCUMENTED DERIVED-DATA EXCEPTION`
- `RETURN FOR INVENTORY REPAIR`
