# CL_PHASE_02J — Admission Sidecar Specification

**Phase:** CL_PHASE_02J — Admission Sidecars and Complete Execution Bundle  
**Generated (UTC):** 2026-07-14T12:15:29Z  
**Repository posture:** ACTIVE REPOSITORY CANDIDATE — PERMANENT INSTITUTIONAL AUTHORITY NOT RATIFIED  

This specification defines proposed destination admission sidecars only. Sidecars are not created at destination paths in this phase.

## Naming rule

```text
<complete-original-filename>.admission.json
```

Sidecars are placed in the same destination parent as the associated copied file. Original extensions are preserved. Hidden or generic shared filenames are not used.

## Counts

| Class | Count |
|---|---|
| RAT-FILE-CL-001 (no sidecar) | 1 |
| RAT-FILE-CL-003 / 004 (repository-candidate sidecars) | 2 |
| RAT-FILE-CL-005 through 019 (phase-evidence sidecars) | 15 |
| RAT-FILE-CL-020 / 021 (no sidecar; manifest metadata) | 2 |
| Total proposed admission sidecars | 17 |

## Fixed payload fields

| Field | Fixed value |
|---|---|
| schema | crisis-liturgies-admission-sidecar |
| schema_version | 1.0 |
| ratification_set | FILE-AUTHORITY-SET-CL-001 |
| source_content_modified | false |
| copy_authorized | false |

## Canonical serialization (future execution)

- UTF-8
- no byte-order mark
- keys sorted lexicographically
- two-space indentation
- LF line endings
- one final newline

`payload_sha256` is computed over that exact canonical byte sequence.

## CL-MIG-001B metadata (no sidecar)

```text
canonical_repo_root means the Crisis Liturgies program root within the active repository candidate. It does not declare permanent Gradient repository authority.
```

## Proposed sidecars

| admission_sidecar_id | ratification_decision_id | sidecar_filename | exact_sidecar_path | authority_state | operative_status | payload_sha256 |
|---|---|---|---|---|---|---|
| ADMIT-SC-001 | RAT-FILE-CL-003 | `CL_PROD_ARCH_001A_RATIFICATION_AND_NAMED_PATCH_RECORD_2026-07-13.json.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\01_PROGRAM_GOVERNANCE\CL_PROD_ARCH_001A_RATIFICATION_AND_NAMED_PATCH_RECORD_2026-07-13.json.admission.json` | OPERATIVE_PROGRAM_AUTHORITY | OPERATIVE_WITH_REPOSITORY_CANDIDATE_LIMITATION | `1253df93af20f25893a48103f8451d9843767c9f84d90b021f9ab864614f1b9f` |
| ADMIT-SC-002 | RAT-FILE-CL-004 | `CL_PROD_ARCH_001A_RATIFICATION_AND_NAMED_PATCH_RECORD_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\01_PROGRAM_GOVERNANCE\CL_PROD_ARCH_001A_RATIFICATION_AND_NAMED_PATCH_RECORD_2026-07-13.md.admission.json` | OPERATIVE_PROGRAM_AUTHORITY | OPERATIVE_WITH_REPOSITORY_CANDIDATE_LIMITATION | `846f728a1069e2d503bc64efc23e5d71bb7011c90c080d446e65629e8e2b739a` |
| ADMIT-SC-003 | RAT-FILE-CL-005 | `CL_PHASE_00_CURSOR_READONLY_INVENTORY_PACKET_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_CURSOR_READONLY_INVENTORY_PACKET_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `302870a20c5d02bf97000a953b035e407e71bf2fce21ceab5d4532844c3cfd17` |
| ADMIT-SC-004 | RAT-FILE-CL-006 | `CL_PHASE_00_EVIDENCE_FREEZE_COMPLETION_REPORT_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_EVIDENCE_FREEZE_COMPLETION_REPORT_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `697bbf9cec80e598d571b2296690478f66c5315ed27d9ee0d8f87ff50b86b79a` |
| ADMIT-SC-005 | RAT-FILE-CL-007 | `CL_PHASE_00_MASTER_CONFLICT_LEDGER_2026-07-13.json.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_MASTER_CONFLICT_LEDGER_2026-07-13.json.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `76b50d2e8aa002bb1692cda21d33efe5a8997466eb7ab28ecfe0f478c5e32667` |
| ADMIT-SC-006 | RAT-FILE-CL-008 | `CL_PHASE_00_MASTER_CONFLICT_LEDGER_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_MASTER_CONFLICT_LEDGER_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `fadf4bd20f53311f963a137bb421205f7c933943bb9e2178ecf526688b18dded` |
| ADMIT-SC-007 | RAT-FILE-CL-009 | `CL_PHASE_00_MASTER_EVIDENCE_REGISTER_2026-07-13.json.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_MASTER_EVIDENCE_REGISTER_2026-07-13.json.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `a31372a6b23df0b4d8d8f42ae991cca4693270329a46bd9457eda43ed390f9f6` |
| ADMIT-SC-008 | RAT-FILE-CL-010 | `CL_PHASE_00_MASTER_EVIDENCE_REGISTER_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_MASTER_EVIDENCE_REGISTER_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `a74512c67be539af5b6588adc211b6491879ae1ed8d8ffd540aeeb8c6a382c93` |
| ADMIT-SC-009 | RAT-FILE-CL-011 | `CL_PHASE_00_PACKAGE_MANIFEST_2026-07-13.json.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_PACKAGE_MANIFEST_2026-07-13.json.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `222fe24774bb9747fb8b64b2d04e04c8566a6f8177e9e5d9e373efada26b29c3` |
| ADMIT-SC-010 | RAT-FILE-CL-012 | `CL_PHASE_00_QUARANTINE_REGISTER_2026-07-13.json.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_QUARANTINE_REGISTER_2026-07-13.json.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `272f95aeb6f802a72e6e960a0a40130d62da87f3f970e30c8da8a57d41b94413` |
| ADMIT-SC-011 | RAT-FILE-CL-013 | `CL_PHASE_00_QUARANTINE_REGISTER_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_QUARANTINE_REGISTER_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `e31c97592a1b2ddd7ce1ad790cc8c4601b126bb3e5db7ff1ec5a40815c6dc427` |
| ADMIT-SC-012 | RAT-FILE-CL-014 | `CL_PHASE_00_SOURCE_ROOT_MAP_2026-07-13.json.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_SOURCE_ROOT_MAP_2026-07-13.json.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `ba06d7edd108517df80791cedbb3771dcc4b7e28069470853d069902520a91d7` |
| ADMIT-SC-013 | RAT-FILE-CL-015 | `CL_PHASE_00_SOURCE_ROOT_MAP_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00_SOURCE_ROOT_MAP_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `e2c06c74eb0b6c29cdbbd829d1bf66a12dd8e6bf6110db5517fecc21cabc1d54` |
| ADMIT-SC-014 | RAT-FILE-CL-016 | `CL_PHASE_00B_CURSOR_DISK_INVENTORY_RECONCILIATION_2026-07-13.json.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00B_CURSOR_DISK_INVENTORY_RECONCILIATION_2026-07-13.json.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `c8f336442093f03abf9ea9c48f4b3a1ec0dc4e95548f8b1afb76311ce441b3d9` |
| ADMIT-SC-015 | RAT-FILE-CL-017 | `CL_PHASE_00B_CURSOR_DISK_INVENTORY_RECONCILIATION_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00B_CURSOR_DISK_INVENTORY_RECONCILIATION_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `4799d92781882cddc8f3fb826b9a87a74b613aa00ff93ff7284ac3b65645a64b` |
| ADMIT-SC-016 | RAT-FILE-CL-018 | `CL_PHASE_00B_STATUS_UPDATE_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00B_STATUS_UPDATE_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `9e47e5575dd7d5007d657119eb59777276fb7ba4fd3a922cc2dc7ed6fa5647cb` |
| ADMIT-SC-017 | RAT-FILE-CL-019 | `CL_PHASE_00C_PACKAGE_INTEGRITY_PATCH_PACKET_2026-07-13.md.admission.json` | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES\00_PROJECT_CONTROL\03_PHASE_EVIDENCE\CL_PHASE_00C_PACKAGE_INTEGRITY_PATCH_PACKET_2026-07-13.md.admission.json` | ADMITTED_PHASE_EVIDENCE | NONOPERATIVE | `e79208156a7253c087186b5aa5d51f70072818929923d874ec4fe7d1647a76a3` |

## Required status labels

### Repository-candidate (003, 004)

```text
REPOSITORY_CANDIDATE — PERMANENT INSTITUTIONAL AUTHORITY NOT RATIFIED
```

### Admitted phase evidence (005–019)

```text
ADMITTED PHASE EVIDENCE — NONOPERATIVE

This record documents a completed planning or evidence phase.
It does not establish current program, repository, or institutional authority.
```

## Safety

No destination sidecar files were written. `automatic_collision_resolution` remains `NO`.
