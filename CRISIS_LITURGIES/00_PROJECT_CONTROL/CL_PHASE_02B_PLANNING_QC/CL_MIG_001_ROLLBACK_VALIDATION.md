# CL_MIG_001 — Rollback Validation

**Date (UTC):** 2026-07-13T20:03:48Z  
**Reviewed protocol:** `CL_PHASE_02_ROLLBACK_PLAN.md`  
**Verdict:**

```text
ROLLBACK_READY_WITH_PATCHES
```

---

## 1. Doctrine conflict

Phase 02 default method RB-A `DELETE_WRITTEN_TARGETS_ONLY` **depends on deletion of destination material**.

Phase 02B requires future migration reversal **without** depending on:

- deletion of destination material
- filenames alone
- “latest” versions
- folder names alone
- automatic merging
- assumed repository authority

Therefore rollback is **not execution-ready** without a human-ratified patch such as:

1. Leave written targets in place;
2. Move written targets into `90_QUARANTINE/migration_rollback_<batch>/` only under explicit authorization;
3. Reverse-register the batch receipt;
4. Re-verify untouched sources by `rollback_source_reference` + `rollback_hash`.

---

## 2. Eligible-row field preservation check

Eligible rows: **21**

| Required rollback field | Pre-copy status |
|---|---|
| original_source_path | PRESENT on eligible rows |
| source_parent | PRESENT |
| source_sha256 | PRESENT |
| source_bytes | PRESENT |
| source_modified_time | PRESENT |
| future_destination_path | PRESENT (proposed) |
| future_destination_hash | ABSENT (exists only after copy) |
| copy_receipt_reference | ABSENT (no copy executed) |
| verification_state | ABSENT / NOT_STARTED |

Gaps recorded: none beyond expected pre-copy absences

---

## 3. Notes

Phase 02 RB-A delete-written-targets conflicts with Phase 02B non-delete rollback requirement. Eligible rows preserve source path/hash/bytes/mtime for re-verification, but post-copy destination hash and copy receipt do not yet exist (expected pre-copy). Rollback is not ready for execution without doctrine patch.

No rollback rehearsal was executed (would require creating `99_TEMP` targets — prohibited in this phase).
