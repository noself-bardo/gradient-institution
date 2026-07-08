# CL-III Release Assembly Readiness Record

Status: Historical milestone + current-state boundary  
Authority: Companion series provenance — not governing  
Scope: Crisis Liturgies III — Emergency Objects  
Related asset: TG-WEB-001 (future gallery / companion shelf integration)

## Purpose

Record the release assembly readiness audit for CL-III and distinguish it from the **current controlling state** after PDF, archive, indexing, and snapshot stages completed.

TG-WEB-001 must not regress CL-III to release-assembly state when presenting or linking companion material.

## Release Assembly Location (Supporting Provenance Only)

```text
Google Drive:
06_RELEASE_ASSEMBLY/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS
```

Documents produced at this stage:

| File | Role |
|---|---|
| `CLIII_RELEASE_ASSEMBLY_READINESS_REPORT.md` | Readiness audit summary |
| `CLIII_PRINT_ASSEMBLY_MANIFEST.md` | Print assembly manifest |
| `CLIII_PAGE_ORDER.md` | Page order CL-025 → CL-036 |
| `CLIII_SOURCE_FINALS_MANIFEST.md` | Source finals inventory |
| `CLIII_MISSING_ASSET_CHECK.md` | Missing/extra asset check |
| `CLIII_RELEASE_LOCK_STATUS.md` | Stage lock snapshot at assembly time |

## What Release Assembly Verified (Historical)

- 12 artifact folders: CL-025 through CL-036
- 48 final PNGs + 48 draft PNGs
- 12 generation receipts
- 12 output QC files
- All finals at 1086×1448
- No duplicate SHA-256 hashes
- No missing finals
- No extra finals outside range
- Source finals unmodified
- `CLIII_FULL_VISUAL_LOCK_AUDIT.md` returned **FULL VISUAL LOCK APPROVED**

## Critical Boundary — Do Not Misread Assembly Records

Release assembly documents state **PDF BUILD NOT STARTED** because they were created **before** later PDF, archive, indexing, and snapshot stages.

**Do not treat “PDF BUILD NOT STARTED” as the current project state.**

## Current Controlling CL-III State

| Stage | Status |
|---|---|
| Print PDF | **APPROVED** |
| Final archive lock | **APPROVED** |
| Indexing | **CLOSED** |
| Frozen release snapshot | **COMPLETE** |

## Source-of-Truth Order (Web / Gallery Implementation)

Use these layers in order when TG-WEB-001 or a future gallery references CL-III:

1. `08_ARCHIVE/CRISIS_LITURGIES/MASTER_COLLECTION_ROLLUP`
2. `00_OPERATING_SYSTEM/00_GOVERNANCE/THE_GRADIENT_ARTIFACT_REGISTRY.md`
3. `08_ARCHIVE/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS`
4. `09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0`
5. `06_RELEASE_ASSEMBLY/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS` — **supporting provenance only**

Lower layers may explain history. Higher layers govern what the public gateway may present as current.

## Verification Script (Read-Only Evidence)

Reusable verification workflow:

```text
tools/cl_iii_release_assembly_prep.py
```

Cursor may **inspect** this script as evidence of the verification workflow.

Cursor must **not** use it to:

- Overwrite files
- Rename files
- Regenerate artwork
- Rebuild PDFs
- Modify source assets

Script paths (Drive — not in this Git repo):

- Source: `05_IMAGERY/GENERATED_PROOFS/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS`
- Assembly output: `06_RELEASE_ASSEMBLY/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS`

## Artifact Range (CL-025 — CL-036)

| ID | Title |
|---|---|
| CL-025 | The Edible Ledger |
| CL-026 | The Extended Wait |
| CL-027 | The Tolerance Card |
| CL-028 | The Fused Budget |
| CL-029 | The Chokepoint Valve |
| CL-030 | The Threefold Threshold |
| CL-031 | The Serving Ceremony |
| CL-032 | The Reflective Flag |
| CL-033 | The Roof Tile |
| CL-034 | The Domestic Witness |
| CL-035 | The Lullaby Alarm |
| CL-036 | The Self-Clearing Receipt |

## TG-WEB-001 Implementation Constraints

When CL-III appears on the Archive Gateway or a companion gallery:

- Present as **companion source** — not governing authority
- Link to **approved print PDF** or frozen snapshot references — not release-assembly trackers
- Do not rebuild the PDF
- Do not regenerate images
- Do not alter canon
- Do not modify source artwork
- Do not use assembly-stage “NOT STARTED” labels as live status

## Disposition

```text
TG-WEB-001 — Baseline Built / Asset Integration Pending
CL-III — Print approved; snapshot complete; web integration not yet started
```
