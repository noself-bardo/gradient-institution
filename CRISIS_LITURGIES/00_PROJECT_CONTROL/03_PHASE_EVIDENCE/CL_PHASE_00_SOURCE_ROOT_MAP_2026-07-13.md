# CL-PHASE-00-002
## Source Root Map

**Status:** CONTROLLED DISCOVERY  
**Date:** 2026-07-13  
**Mutation policy:** No root may be moved, deleted, renamed, or retired during Phase 00.

# Root map

| ID | Root | System | Role | Write state | Access | Risk | Required action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ROOT-001 | The Gradient Google Drive root | GOOGLE_DRIVE | PRIMARY_STORAGE_CANDIDATE | EXISTING / NOT YET STRUCTURALLY LOCKED | CONNECTED_READ | Multiple active, release, archive and _codex_work trees coexist. | Recursive inventory and classification; no moves yet. |
| ROOT-002 | CL-OPS-001 project control folder | GOOGLE_DRIVE | ACTIVE_GOVERNANCE_CONTROL | AUTHORIZED_FOR_CONTROL_RECORDS | CONNECTED_READ_WRITE_PENDING_UPLOAD | Currently contains only CL-OPS-001 and Chachipti audit. | Store Phase 00 control package and preserve prior files. |
| ROOT-003 | Current local evidence sandbox | CHATGPT_RUNTIME | TEMPORARY_EVIDENCE_STAGING | YES | DIRECT | Ephemeral runtime; not institutional storage. | Hash, package and upload control artifacts. |
| ROOT-004 | Codex repository evidence scope | LOCAL_CODEX_REPOSITORY | REPOSITORY_EVIDENCE | UNKNOWN | HANDOFF_ONLY | Repository-scoped handoff may omit other roots, including CL-V. | Run read-only recursive inventory from Cursor/Codex. |
| ROOT-005 | Legacy release root | DRIVE_SYNCED_OR_LOCAL_REPOSITORY | FROZEN_HISTORICAL_RELEASE | MUST_BE_READ_ONLY | MANIFEST_EVIDENCE | Historical structure predates current standards. | Attach retrospective provenance without altering binaries. |
| ROOT-006 | Release snapshot root | DRIVE_SYNCED_OR_LOCAL_REPOSITORY | FROZEN_SNAPSHOT_STORAGE | NEW_NAMESPACED_SNAPSHOTS_ONLY | PARTIAL_EVIDENCE | Multiple volume conventions and potentially incomplete indexes. | Inventory folders, manifests and checksums. |
| ROOT-007 | Storage mirror root | LOCAL_OR_DRIVE_SYNCED | REDUNDANT_PRESERVATION | CONTROLLED_MIRRORS_ONLY | CHAT_EVIDENCE_ONLY | CL-V mirror is not found in connected Drive search. | Direct disk verification. |
| ROOT-008 | Pygmalion local repository | WINDOWS_LOCAL_GIT | ACTIVE_OR_HISTORICAL_VOLUME_REPOSITORY | PAUSED_PENDING_RECONCILIATION | CHAT_EVIDENCE_ONLY | Publication-complete claims conflict with later reconstruction QC. | Read-only inventory of control, source, assets, fonts, QC, manifests and Git state. |
| ROOT-009 | Pygmalion Drive folder | GOOGLE_DRIVE | VOLUME_STORAGE_AND_EXPORT | PAUSED_PENDING_RECONCILIATION | CONNECTED_PARTIAL | Direct child listing is insufficient to prove run state. | Recursive tree and checksum comparison against local repository. |
| ROOT-010 | The Death of the Bit local Drive-synced repository | WINDOWS_LOCAL_AND_DRIVE_SYNC | ACTIVE_WORKING_VOLUME | PAUSED_FOR_ARCHITECTURE_RECONCILIATION | MANIFEST_AND_DRIVE_EVIDENCE | Working proof is substantial but not an admitted final release. | Inventory source, proof, editorial and lock records; resolve page profile. |
| ROOT-011 | CL-V frozen snapshot | LOCAL_OR_DRIVE_SYNCED | CLAIMED_FROZEN_RELEASE | MUST_BE_READ_ONLY | CHAT_EVIDENCE_ONLY | Missing from Codex handoff and connected Drive search. | Locate exact root and verify known SHA-256. |
| ROOT-012 | CL-V storage mirror | LOCAL_OR_DRIVE_SYNCED | CLAIMED_MIRROR | MUST_BE_READ_ONLY | CHAT_EVIDENCE_ONLY | Mirror existence not directly inspected. | Compare 103 payload files and metadata-only extras against source snapshot. |
| ROOT-013 | Notion institutional workspace | NOTION | HUMAN_READABLE_GOVERNANCE_INDEX | CONTROLLED | CONNECTED | Parallel or superseded pages may appear equally current. | Create Phase 00 index and mark disputed records explicitly. |
| ROOT-014 | ChatGPT Gradient project corpus | CHATGPT | PROVENANCE_AND_HUMAN_DECISION_HISTORY | ONGOING | SEARCHABLE_CONTEXT / NO_FULL_EXPORT | Chat claims can outpace repository and Notion records. | Capture only ratified decisions and evidence references into institutional records. |
| ROOT-015 | GitHub web/publication repositories | GITHUB | PUBLICATION_DERIVATIVES | UNKNOWN | CHAT_EVIDENCE_ONLY_IN_PHASE_00 | Web availability may be mistaken for archive admission. | Verify releases and checksums during publication audit, not infer collection state. |

# Governing interpretation

- A **canonical operational root** is a logical authority designation, not a claim that all bytes must live in one physical service.
- Registered read-only mirrors and public derivatives may exist outside the active root.
- A mirror becomes a conflict only when it can receive unregistered active production or independently claim current state.
- Existing legacy roots remain protected by NP-010 until checksums, provenance, replacement paths and recovery routes are verified.
