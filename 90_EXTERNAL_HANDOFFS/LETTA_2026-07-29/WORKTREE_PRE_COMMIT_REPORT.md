# Letta Handoff Repository Baseline — Clean-Clone Pre-Commit Report

**Prior worktree attempt:** `CHECKOUT_BLOCKED_BY_WINDOWS_PATH_LENGTH / NO_IMPORT_OCCURRED / DIRTY_CHECKOUT_PROTECTED / SAFE_TO_RETRY_IN_SHORT_CLONE`  
**Current result:** Clean-clone candidate import complete; pre-commit only.

This final audit environment is a **clean short-path clone**, not a Git worktree.

## Dirty checkout and incomplete-branch protection

- Dirty checkout status receipt: `C:\Users\steve\Projects\gradient-institution-audit-staging-20260729\DIRTY_CHECKOUT_STATUS_RECEIPT.txt`
- Fetch receipt: `C:\Users\steve\Projects\gradient-institution-audit-staging-20260729\FETCH_RECEIPT.txt`
- Incomplete branch inspection: `C:\Users\steve\Projects\gradient-institution-audit-staging-20260729\INCOMPLETE_BRANCH_INSPECTION_RECEIPT.txt`
- The incomplete local audit branch was verified as identical to `origin/main`, unattached to a worktree, unpushed, and without unique commits before deletion.
- No stale worktree metadata was identified as prunable.
- The original dirty checkout was not checked out, pulled, merged, rebased, reset, stashed, cleaned, copied into, committed, or otherwise changed.

## Clean clone and branch

- **Clone:** `C:\g-intake`
- **Remote:** `https://github.com/noself-bardo/gradient-institution.git`
- **Branch:** `audit/letta-handoff-repository-baseline-20260729`
- **Base / HEAD / origin/main:** `de444af4aecc8f92c8aa6c4a500e9ecea9f8d5e3`
- **Upstream:** `origin/main`
- The branch was created with no pre-existing remote branch and began with a clean working tree.

## Path-length result

The five longest tracked paths checked out successfully. The maximum projected absolute path length under `C:\g-intake` was 210 characters, including:

`CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_PHASE_01_PORTABLE_AUTHORITY_SOURCES_2026-07-13/04_PHASE_CLOSURES/CL_PHASE_01_AUTHORITY_PROFILE_ROOT_RECONCILIATION_CHARTER_2026-07-13.json`

## Candidate package

- **ZIP:** `C:\Users\steve\My Drive\The Gradient\90_EXTERNAL_HANDOFFS\LETTA_2026-07-29\reports\repository-control-candidates-20260729.zip`
- **Expected and verified SHA-256:** `F7A2F55C7FF68617669FCE89A122A213E0CF3BF532AD6C2EE157F2924D75FF22`
- **Staging directory:** `C:\g-stage`
- **Inventory:** `C:\g-stage\STAGING_INVENTORY.json`
- **Extracted files:** 14, all approved control files and validators; no ZIP, extracted Letta package, credentials, runtime secrets, or binary archive was imported.

## Imported files

- `00_CONTROL/CURRENT_STATE.md`
- `00_CONTROL/PORTFOLIO_MATRIX.yaml`
- `00_CONTROL/AUTHORITY_REGISTER.yaml`
- `00_CONTROL/SOURCE_ACCESS_REGISTER.yaml`
- `00_CONTROL/SUPERSESSION_REGISTER.yaml`
- `00_CONTROL/CONTRADICTION_REGISTER.yaml`
- `00_CONTROL/STATUS_VOCABULARY.yaml`
- `00_CONTROL/EVIDENCE_VOCABULARY.yaml`
- `00_CONTROL/VERIFICATION_QUEUE.yaml`
- `scripts/validate_portfolio_matrix.py`
- `scripts/validate_authority_sources.py`
- `scripts/validate_status_vocabulary.py`
- `scripts/validate_project_boundaries.py`
- `scripts/validate_change_summary.py`
- `90_EXTERNAL_HANDOFFS/LETTA_2026-07-29/ARCHIVE_POINTER.md`
- `90_EXTERNAL_HANDOFFS/LETTA_2026-07-29/WORKTREE_PRE_COMMIT_REPORT.md`

## Excluded and deferred

Excluded: the original Letta ZIP, extracted historical package, Letta MemFS data, credentials, runtime secrets, binary archives, and ChatGPT lane history. Imported Letta records remain historical secondary evidence; the repository baseline is not current authority.

## Validation

- All five validators passed.
- All eight JSON-compatible YAML control files parsed.
- All five validation scripts compiled successfully.
- `git diff --check` passed.
- There are no imported next-gate fields, so no conflicting inherited next gates.
- No absolute Letta-agent memory paths were found in imported control files or validators.
- Crisis Liturgies remains separated into program, pipeline, individual-volume, and migration/reconciliation candidates. The Container Never Bursts and The Death of the Bit are separate records.
- Historical Letta evidence is explicitly non-governing; Drive archive material is referenced only through `ARCHIVE_POINTER.md` and a historical-source record.
- No Notion, Drive archive content, GitHub remote, or ChatGPT source was modified.

Validator output:

```text
PASS: 22 candidate rows; 17 legacy records; field evidence complete
PASS: 2 complete source records; authority precedence is valid
PASS: 11 evidence labels and 10 status labels
PASS: 6 Crisis Liturgies candidate boundaries; no inherited child status
PASS: change-summary counts and source/branch accounting are consistent
PASS: 8 JSON-compatible YAML control files parsed
PASS: 5 validation scripts compile
PASS: git diff --check
PASS: no imported next-gate fields, so no conflicting inherited gates
PASS: no absolute Letta-agent memory paths
```

## Proposed diff and status

- **Complete proposed diff:** `C:\g-stage\PROPOSED_IMPORT.diff`
- **Diff statistics:** 16 new files, 545 added lines, 0 deletions.
- **`git diff --check`:** passed.
- **`git status --short`:**

```text
?? 00_CONTROL/
?? 90_EXTERNAL_HANDOFFS/
?? scripts/
```

## Proposed commit

`feat(control): add repository portfolio and authority baseline`

At the fetched `origin/main` base, this add-only change has no filename collision and should be conflict-free for a draft pull request. This statement applies only to `origin/main` at the recorded base commit; it does not predict later remote changes.

No commit, push, or pull request was created.
