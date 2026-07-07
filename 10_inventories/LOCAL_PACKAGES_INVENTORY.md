# Local Packages Inventory

Status: DRAFT / AGENT-ASSISTED READ-ONLY PASS

Authority: Not canonical

Constraint: This inventory does not authorize migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work.

## Known Local Roots

Repo root:

`C:\Users\steve\Projects\gradient-institution`

Drive sync root:

`C:\Users\steve\My Drive\The Gradient`

## Current Local Git State

`gradient-institution` has a baseline commit:

`f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Current uncommitted planning files are migration-control drafts only.

## Known Non-Canonical Local Material

Earlier Control Center package work existed under:

`C:\Users\steve\Projects`

That work is provisional and is not part of the first GFVP + Publishing Constitution migration pass.

Agent duplicate/mirror audit observed:

- `gradient-control-center-app` exists under `C:\Users\steve\Projects` as a sibling local project.
- It is not a GFVP duplicate.
- It remains out of scope for the GFVP Drive/source package completion pass.
- It should not be imported or treated as platform source until a separate platform/local package inventory is explicitly approved.

## GFVP Local Mirror Findings

- No local GFVP package mirror was found in `C:\Users\steve\Projects\gradient-institution`.
- The migration repo contains inventory/planning/source-review documents only, not GFVP source payloads.
- No GFVP release folder or zip was found under accessible `C:\Users\steve\Projects` paths by the duplicate/export/reconciliation agents.
- Downloads were checked for the reconciliation pass: three GFVP markdown copies were reported, but no GFVP zip/export package was found.
- Agent swarm re-verification (2026-07-06): **25 GFVP PNG files** are present in the synced Drive package (`06_GENERATED_OUTPUTS/`: 14; `08_APPROVED_OUTPUTS/`: 11). PNG import remains deferred under `TG-SRC-PUB-002`. GFVP zip/export package still not found locally.

## Local Duplicate / Mirror Risks

| Inventory ID | Source System | Title / Filename | Location / Path / Link | File Type | Artifact Class | Related Source ID | Current Authority | Proposed Destination | Migration Action | Review Status | Risk Level | Duplicate / Mirror Notes | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LOC-AUD-001` | Local repo | No GFVP payload mirror in migration repo | `C:\Users\steve\Projects\gradient-institution` | Repo tree | Negative finding | `TG-SRC-VIS-001`; `TG-SRC-PUB-002` | Repo contains draft controls only | N/A | `NO_ACTION` | Agent-assisted check | Low | Not a duplicate; repo has references only | Confirms no source files were migrated into repo. |
| `LOC-AUD-002` | Local Projects | `gradient-control-center-app` | `C:\Users\steve\Projects` | Local project | Platform/local package trace | Candidate future `TG-SRC-PLT-*` | Provisional; not inventoried for this phase | `08_platform/` only after separate approval | `REFERENCE_ONLY`; deferred | Out of scope | Low | Not GFVP duplicate | Do not edit or import during GFVP inventory. |
| `LOC-AUD-003` | Local Downloads | Scattered GFVP markdown copies | `C:\Users\steve\Downloads` | Markdown | Stray source copy | `TG-SRC-VIS-001` | Unknown | None until reviewed | `REQUIRES_SOURCE_INVENTORY` | Three markdown copies reported; no binaries found | Medium | Potential partial duplicate of Drive source files | Needs explicit local sweep approval before classification beyond binary-location check. |
| `LOC-AUD-004` | Local / Drive | Missing GFVP release zip | Expected `gradient_foundational_visual_package_batch_01.zip`; not found under scanned Drive/Projects/Downloads paths | ZIP | Missing export package | `TG-SRC-PUB-002` | Unknown | Remain in Drive if found | `REQUIRES_SOURCE_INVENTORY` | Not found | High | Missing release/export mirror; see GFVP-BIN-004 | PNGs present in sync (25); zip still missing. See `GFVP_RECEIPT_BINARY_AUTHORITY_RECONCILIATION_DRAFT.md`. |

## First-Pass Rule

Do not import local packages into this repo until they appear in the migration manifest with source, destination, and status.

Do not inspect or import Downloads, Codex exports, generated image folders, or sibling app projects further without explicit approval for a local package sweep.

## Open Questions

- Are there extracted Codex packages outside Google Drive?
- Are there local GFVP zips in Downloads?
- Are there generated image folders outside the synced Drive root?
- Are there ChatGPT or Codex export bundles that need source registration?
- Are the missing GFVP PNG binaries stored in an unsynced Drive location, a Codex workspace, another machine, or cloud-only storage?
- Should the scattered Downloads GFVP markdown copies be treated as duplicates, drafts, or ignored local residue?
