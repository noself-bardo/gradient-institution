# CL-PHASE-02-OUT-009
## Rollback Plan

**Mode:** PLAN ONLY  
**Authority:** NP-010 Non-Destructive Migration  
**Default:** Sources never deleted; targets removable only if written by a named batch receipt.

---

# 1. Rollback doctrine

Migration is **copy → validate → register → (only later) controlled retirement**.

Therefore rollback of an in-progress or failed copy batch means:

1. remove or restore **targets written by that batch**;
2. leave all source roots untouched;
3. leave all frozen release binaries untouched;
4. preserve quarantine evidence;
5. record a rollback receipt.

Rollback is not license to “clean up” duplicates or retire legacy roots.

---

# 2. Preconditions for any future copy (so rollback stays possible)

| Control | Requirement |
|---|---|
| Overwrite | Default **forbidden**. Existing targets ⇒ STOP. |
| Manifest | Every written path listed with SHA-256 after write |
| Pre-batch snapshot | Optional but recommended for any batch that could touch existing dirs |
| Authorization | Human `AUTHORIZE_COPY` record with `DELETION: NO` |
| Quarantine | Quarantine paths treated as evidence, not trash |

---

# 3. Rollback methods

| Method ID | When used | Steps |
|---|---|---|
| RB-A `DELETE_WRITTEN_TARGETS_ONLY` | Default for failed/partial copy into empty targets | Delete exactly the files/dirs listed in batch write receipt; verify sources still hash; write rollback receipt |
| RB-B `RESTORE_FROM_PREBATCH_SNAPSHOT` | Only if an overwrite was explicitly authorized (rare) | Restore snapshot of overwritten targets; never restore by deleting sources |
| RB-C `MANIFEST_REVERSAL` | Authored registries/schemas | Remove authored files listed as `AUTHOR_NEW_RECORD`; keep planning package intact |
| RB-D `NO_OP` | `WRITE_EXTERNAL_REFERENCE_ONLY` items that never copied binaries | Delete only the reference JSON/md if needed; Drive binaries remain |

---

# 4. Batch-specific rollback sketches

## CL-MIG-001 — Governance and registries

- Expected writes: text/JSON/schemas under `00_INSTITUTIONAL_CONTROL/`, `03_RELEASE_PROFILES/`, `04_COLLECTION_REGISTRY/`, `06_BUILDER/schemas/`, selected quarantine copies.
- Rollback: RB-A + RB-C.
- Must not delete: Drive control package; repo Chachipti source lane until separately authorized; Phase 02 planning directory.

## Later collection batches (CL-MIG-002+)

- If copying into empty `05_VOLUMES/…` or `10_FROZEN_RELEASES/…` manifest trees: RB-A.
- If external refs only: RB-D.
- If a second tree was created beside a live source (e.g., CL-V): rollback removes the **new** tree only; original sibling tree remains canonical until intentional cutover.

---

# 5. What rollback must never do

- Delete Drive archive/release trees
- Delete matching-hash mirrors because they “look redundant”
- Modify frozen PDFs/PNGs
- Create or destroy CL-VI
- Promote or un-quarantine CL-VII as a side effect
- `git commit`, `git reset --hard`, or force-push as a rollback tool unless the human separately authorizes a Git operation
- Use builder repair to “fix” a failed migration

---

# 6. Rollback rehearsal (required in dry-run)

Before first real copy:

1. Create a throwaway target subdirectory under `99_TEMP/cl_mig_rollback_drill/`.
2. Copy two small text fixtures.
3. Hash and record a mini-manifest.
4. Execute RB-A.
5. Confirm fixtures gone and sources unchanged.
6. File drill receipt beside the batch plan.

If rehearsal fails, **STOP** — no production copy.

---

# 7. Recovery routes if rollback itself fails

1. Stop further mutation.
2. Preserve the failed target tree as `90_QUARANTINE/migration_failure_<batch>_<timestamp>/` via copy if needed (only if safe and authorized).
3. Rely on untouched sources + Phase 00 inventory hashes for reconstruction.
4. Escalate to human Founder / Archivist; do not improvise deletions.

---

# 8. Success criteria for a rollback

- Every path in the write receipt is absent or restored per method
- Zero source-path mutations
- Zero frozen-binary mutations
- Rollback receipt hashed and stored under `00_PROJECT_CONTROL/CL_MIG_XXX/`
- Collection state language unchanged except to note batch aborted
