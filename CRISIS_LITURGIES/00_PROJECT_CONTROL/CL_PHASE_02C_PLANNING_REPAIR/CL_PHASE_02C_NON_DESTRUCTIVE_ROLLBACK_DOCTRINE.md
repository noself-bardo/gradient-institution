# CL_PHASE_02C — Non-Destructive Rollback Doctrine

**Date (UTC):** 2026-07-13T20:11:36Z  
**Status:** PENDING HUMAN RATIFICATION (RAT-CL-005)  
**Supersedes for future batches:** Phase 02 `CL_PHASE_02_ROLLBACK_PLAN.md` RB-A delete-first method  

---

```text
ROLLBACK IS NOT DELETION.
```

---

## 1. Doctrine

Migration rollback is an **evidence and routing** operation. It freezes a failed or disputed batch, preserves both source and destination artifacts, compares hashes, and restores references without destroying either side.

Deletion of any artifact — source or destination — is **outside** rollback and requires a separate, explicit destruction authorization record.

---

## 2. Mandatory sequence

1. **Freeze** the affected migration batch (`mode: ROLLBACK` or batch status FROZEN_DISPUTED).
2. **Verify** the copy receipt (item list, timestamps, claimed written paths).
3. **Compare** source and destination hashes (`source_hash` vs `post_copy_hash` / on-disk).
4. **Mark** the destination artifact as `DISPUTED` or `SUPERSEDED` in the manifest / registry (labeling only).
5. **Preserve** both source and destination pending human review (no delete, no overwrite, no merge).
6. **Restore references or routing** so active program pointers no longer treat the disputed destination as authoritative.
7. **Require separate destruction authorization** for any eventual deletion, if ever warranted.

---

## 3. Allowed rollback methods

| Method | Meaning |
|---|---|
| `FREEZE_MARK_DISPUTED_PRESERVE_BOTH` | Default |
| `REVERSE_ROUTING_ONLY` | Pointer/registry correction only |
| `QUARANTINE_LABEL_WITHOUT_DELETE` | Add quarantine label/record; files stay |

Forbidden as rollback:

- deleting written targets
- deleting sources
- automatic merging
- inferred “latest wins”
- `git reset --hard` / force-push as rollback
- builder repair as silent rollback

---

## 4. Evidence required before claiming rollback complete

- original_source_path
- source_parent
- source_sha256
- source_bytes
- source_modified_time
- destination_path
- destination_hash (post-copy or on-disk)
- copy_receipt_reference
- verification_state / dispute label
- human reviewer identity / authorization id

---

## 5. Interaction with CL-MIG-001A / 001B

Neither batch is executable in this phase. When a future authorized copy occurs, this doctrine is binding unless a later ratified doctrine explicitly replaces it.

---

## 6. Explicit statement

```text
ROLLBACK IS NOT DELETION.
```
