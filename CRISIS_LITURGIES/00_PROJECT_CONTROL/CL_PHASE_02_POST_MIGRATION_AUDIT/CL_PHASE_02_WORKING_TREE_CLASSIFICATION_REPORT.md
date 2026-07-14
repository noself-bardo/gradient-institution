# CL Phase 02 Working-Tree Classification Report

**Date:** 2026-07-14
**Repository:** `C:\Users\steve\Projects\gradient-institution`
**Scope:** read-only classification of `git status --short --untracked-files=all` after CL-MIG-001 closure push
**CL-MIG-001 commit:** `f61e6bcd0f8d6d872967b245f4ff67ffb2f1af0f`
**Mode:** classify only — no stage, commit, push, delete, move, rename, restore, reset, stash, or repair

## Executive verdict

- CL-MIG-001 remains closed and pushed; local and `origin/main` HEAD match.
- Git index remains empty.
- None of the 56 committed CL-MIG-001 paths are locally modified.
- Remaining working-tree material is overwhelmingly parallel later-phase work, collection/expansion trees, Chachipti (deferred), platform publication edits, superseded Phase 02 planning packets, and a bounded set of duplicate extraction artifacts.
- Chachipti production lane remains separate from CL-MIG-001.
- Phase 02B–02M materials read as legitimate later-phase migration control, not accidental repetition of the closed 56-path allowlist.

## Repository integrity checks

| Check | Result |
|---|---|
| Local HEAD | `f61e6bcd0f8d6d872967b245f4ff67ffb2f1af0f` |
| origin/main HEAD | `f61e6bcd0f8d6d872967b245f4ff67ffb2f1af0f` |
| Heads match expected closure commit | `YES` |
| Git index empty | `YES` |
| CL-MIG-001 committed paths locally dirty | `0` |
| Tracked files changed by repeating earlier CL-MIG-001 steps | `NO (0 of 56 dirty)` |
| Status entries classified | `666` |

## Classification counts

| Classification | Count |
|---|---:|
| `CHACHIPTI_CONTROLLED_MATERIAL` | 9 |
| `COLLECTION_OR_EXPANSION_MATERIAL` | 408 |
| `DUPLICATE_EXTRACTION_ARTIFACT` | 22 |
| `LATER_PHASE_MIGRATION_WORK` | 147 |
| `LEGITIMATE_PREEXISTING_WORK` | 28 |
| `PLATFORM_OR_PUBLICATION_WORK` | 6 |
| `SUPERSEDED_CONTROL_PACKET` | 46 |
| **TOTAL** | **666** |

## Answers to required determination questions

### ZIP / extracted packages inside the repository

`*.zip` is gitignored (`.gitignore:18`), so ZIP files do **not** appear in `git status --short --untracked-files=all`. Disk scan still found the following ZIP / double-ZIP artifacts under the repo working tree:

- `CRISIS_LITURGIES/00_CHACHIPTI_PRODUCTION_LANE.zip`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_MIG_001_POST_COPY_VERIFICATION_2026-07-13.zip.zip`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02A2_SOURCE_RECOVERY_REVIEW_2026-07-13.zip.zip`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02A3_ZERO_WRITE_DRY_RUN_REVIEW_2026-07-13.zip.zip`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02A3_ZERO_WRITE_DRY_RUN_REVIEW_R2_2026-07-13.zip.zip`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02A_PATCHED_PLANNING_REVIEW_2026-07-13.zip.zip`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING rename.zip`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING_REVIEW_2026-07-13.zip.zip`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_canonical_source/CL-V_CANONICAL_RESTORE_PACKET_v1.zip`

Extracted package directories that **do** appear in status (or are tracked) include:

- `CL_PHASE_02_PLANNING/CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/` — untracked package extract (duplicate vs commit-control)
- `CL_PHASE_02_PLANNING/CL_MIG_001_CLOSURE/...` — untracked duplicate of committed final closure
- `CL_PHASE_02_PLANNING/CL_PHASE_01_PORTABLE_AUTHORITY_SOURCES_2026-07-13/` — authorized retained portable sources
- Tracked (committed): `CL_MIG_001_COMMIT_CONTROL/`, `CL_MIG_001_FINAL_CLOSURE_2026-07-13/`

### Duplicate closure / schema / manifest / authorization files

Same-name control artifacts exist in multiple locations. Notable multipaths:

- Final closure MD/JSON/SHA256SUMS: committed `CL_MIG_001_FINAL_CLOSURE_2026-07-13/` **and** untracked `CL_MIG_001_CLOSURE/CL_MIG_001_FINAL_CLOSURE_2026-07-13/`
- Schema v1.2: committed under `CL_MIG_001_COMMIT_CONTROL/` **and** untracked under planning root **and** `CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/`
- COPY manifest / copy-authorization record: commit-control **and** copy-authorization extract
- Builder schema basenames also appear under later-phase `05_BUILDER_CONTRACTS/` and Phase 02C repair

### Phase 02B through 02L (and observed 02M)

Classified as **LATER_PHASE_MIGRATION_WORK**. These directories contain sequential receipts, authorization packets, MIG-001A/001B scopes, parent materialization, and closeout registers that are **not** the closed 56-path allowlist. They represent parallel later work, not accidental extraction repetition of CL-MIG-001 destinations.

### Chachipti separation

`CRISIS_LITURGIES/00_CHACHIPTI_PRODUCTION_LANE/` remains present and untracked; no Chachipti path was in the CL-MIG-001 56-path commit. Classification: **CHACHIPTI_CONTROLLED_MATERIAL**. Deferred to CL-MIG-008 posture remains intact.

### Tracked-file mutation by repeated steps

Only locally modified tracked files are platform/root README and tg-web-001 publication files. **Zero** of the 56 CL-MIG-001 committed paths show working-tree modifications.

### Git index / HEAD

- Index empty: `YES`
- Local == remote == `f61e6bc...`: `YES`

## DUPLICATE_EXTRACTION_ARTIFACT exact list

- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_CLOSURE/CL_MIG_001_FINAL_CLOSURE_2026-07-13/CL_MIG_001_FINAL_VERIFICATION_AND_CLOSURE_v1.0.json`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_CLOSURE/CL_MIG_001_FINAL_CLOSURE_2026-07-13/CL_MIG_001_FINAL_VERIFICATION_AND_CLOSURE_v1.0.md`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_CLOSURE/CL_MIG_001_FINAL_CLOSURE_2026-07-13/SHA256SUMS.txt`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/CL_MIGRATION_MANIFEST.schema.v1.2.json`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/CL_MIG_001_COPY_AUTHORIZATION_REQUIREMENTS.json`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/CL_MIG_001_COPY_ONLY_AUTHORIZATION_RECORD_v1.0.md`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/CL_MIG_001_CURSOR_COPY_ONLY_EXECUTION_PACKET.md`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/CL_MIG_001_MIGRATION_MANIFEST_COPY_v1.2.1.json`
- `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/CL_MIG_001_COPY_AUTHORIZATION_2026-07-13/SHA256SUMS.txt`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/00_CODEX_HANDOFF/CL-V_CODEX_TAKEOVER_PROMPT.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/01_PROTOCOLS/CL-V_IMAGE_GATE_PROTOCOL.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/01_PROTOCOLS/CL-V_PRODUCTION_RUN_PROTOCOL.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/02_ENGINE_CONTRACTS/CL-V_ENGINE_CONTRACTS.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/03_STATUS_AND_QUEUE/CL-V_REMAINING_ISSUE_RISK_MAP.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/03_STATUS_AND_QUEUE/CL-V_STATUS_AND_TASK_QUEUE.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/04_CURSOR_COMMANDS/CURSOR_COMMAND_CL-051_PROMOTION.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/04_CURSOR_COMMANDS/CURSOR_COMMAND_COMPLETE_ISSUE_DIAGNOSTIC_TEMPLATE.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/04_CURSOR_COMMANDS/CURSOR_COMMAND_PREPARE_NEXT_ISSUE_OVERLAY_TEMPLATE.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/05_QC_AND_PROMOTION/CL-V_QC_AND_PROMOTION_PROTOCOL.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/06_FAILURE_RECOVERY/CL-V_FAILURE_RECOVERY_PROTOCOL.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/CL-V_ALL_IN_ONE_CODEX_HANDOFF.md`
- `CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/11_CURSOR_HANDOFF/_CODEX_PACKET_EXTRACT/CL-V_CODEX_PRODUCTION_HANDOFF_PACKET/README_QUICKSTART.md`

## UNEXPLAINED_REQUIRES_REVIEW exact list

- (none)

## Disposition summary (no actions executed)

| Disposition | Count |
|---|---:|
| `MOVE_OUTSIDE_REPOSITORY` | 13 |
| `PRESERVE` | 557 |
| `REVIEW_FOR_SEPARATE_COMMIT` | 41 |
| `SUPERSEDE_WITH_RECORD` | 55 |

**Action currently authorized for every row:** NO (classification-only pass).

## Method

1. Ran `git status --short --untracked-files=all` (666 entries).
2. Assigned exactly one classification category per returned path.
3. Cross-checked CL-MIG-001 commit path set for local dirtiness.
4. Scanned disk for `*.zip` despite gitignore.
5. Wrote this report and the CSV ledger as **untracked** files under `CL_PHASE_02_POST_MIGRATION_AUDIT/`.

## Confirmation of non-mutation

- No files moved, deleted, staged, committed, or pushed by this pass.
- No CL-MIG-001 migration/closure/commit/push script rerun.
- CL-MIG-002 not begun.
- These reports left untracked by design.
