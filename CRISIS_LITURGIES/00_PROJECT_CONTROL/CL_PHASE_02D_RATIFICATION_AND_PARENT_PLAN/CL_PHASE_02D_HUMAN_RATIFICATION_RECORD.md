# CL_PHASE_02D — Human Ratification Record

**Record ID:** CL-PHASE-02D-RATIFICATION-001  
**Date (UTC):** 2026-07-13T20:17:11Z  
**Phase:** CL_PHASE_02D — Ratification Record and Destination-Parent Materialization Plan  
**Repository posture:** REPOSITORY CANDIDATE — not permanent institutional authority  
**Source packet (read-only):** `CRISIS_LITURGIES\00_PROJECT_CONTROL\CL_PHASE_02C_PLANNING_REPAIR`  
**Output packet:** `CRISIS_LITURGIES\00_PROJECT_CONTROL\CL_PHASE_02D_RATIFICATION_AND_PARENT_PLAN`  

---

## Scope of this record

This record captures human ratification of RAT-CL-001 through RAT-CL-008 exactly as decided, and establishes the destination-parent materialization **plan**. It does **not** create destination parents, copy or migrate files, classify deferred authority records as authoritative, or auto-classify Chachipti components.

All `materialization_status` values in this packet remain:

```text
NOT AUTHORIZED
```

---

## Human ratification decisions (exact)

| Decision ID | Human decision |
|---|---|
| RAT-CL-001 | APPROVED |
| RAT-CL-002 | APPROVED WITH LIMITATION — repository remains an active candidate, not permanent institutional authority |
| RAT-CL-003 | APPROVED FOR PLANNING ONLY |
| RAT-CL-004 | APPROVED FOR PLANNING ONLY |
| RAT-CL-005 | APPROVED AND LOCKED — ROLLBACK IS NOT DELETION |
| RAT-CL-006 | APPROVED |
| RAT-CL-007 | INDIVIDUAL REVIEW RULE APPROVED; AUTHORITY OF FIVE RECORDS DEFERRED |
| RAT-CL-008 | CLASSIFY-BEFORE-COPY RULE APPROVED |

Register mirror: `CL_PHASE_02D_RATIFICATION_DECISION_REGISTER.csv`.

---

## Interpretive locks (non-mutating)

1. **RAT-CL-001 APPROVED** — Program-local Crisis Liturgies topology from Phase 02C is ratified for subsequent planning and eventual materialization packets. Rejected paths (`00_INSTITUTIONAL_CONTROL`, `CL-VI`, institutional constitution clones) remain prohibited.
2. **RAT-CL-002 APPROVED WITH LIMITATION** — `gradient-institution` remains an **active repository candidate**. No claim of permanent / canonical institutional authority is made by this ratification.
3. **RAT-CL-003 / RAT-CL-004 APPROVED FOR PLANNING ONLY** — CL-MIG-001A and CL-MIG-001B scopes are planning-locked. Neither batch is executable. No `AUTHORIZE_COPY` is granted.
4. **RAT-CL-005 APPROVED AND LOCKED** — Non-destructive rollback doctrine is locked: **ROLLBACK IS NOT DELETION.** Destruction remains a separate authorization class.
5. **RAT-CL-006 APPROVED** — Proposed destination parents under the ratified program-local topology are approved as the materialization candidate set. This packet lists them and verifies occupancy. Folder creation is still **NOT AUTHORIZED** until a later explicit materialization authorization instruction.
6. **RAT-CL-007** — Individual review rule for authorship of the five `AUTHOR_FROM_RATIFICATION` registry records is approved. **Authority of those five records remains deferred.** They are not authoritative in this phase. See `CL_PHASE_02D_OPEN_AUTHORITY_REGISTER.csv`.
7. **RAT-CL-008** — Classify-before-copy rule is approved. Chachipti components must be individually classified into exactly one of: keep-in-place handoff; program standard (future); quarantine claim; exclude. **No automatic classification** occurs in this phase. See `CL_PHASE_02D_CHACHIPTI_CLASSIFICATION_QUEUE.csv`.

---

## Destination-parent materialization plan (summary)

| Item | Value |
|---|---|
| Proposed topology parents in manifest | 15 |
| Nesting parents derived from provisional Chachipti map targets | 3 |
| Parents materialized this phase | 0 |
| `materialization_status` | NOT AUTHORIZED (all rows) |
| Occupancy verification | `CL_PHASE_02D_PARENT_OCCUPANCY_VERIFICATION.csv` |

Immediate MIG-relevant absent parents (mapping counts from Phase 02C revised map):

- `00_PROJECT_CONTROL\01_PROGRAM_GOVERNANCE` — 4 mappings (CL-MIG-001A)
- `00_PROJECT_CONTROL\02_PROGRAM_REGISTRIES` — 5 mappings (CL-MIG-001A; five deferred authority targets)
- `00_PROJECT_CONTROL\03_PHASE_EVIDENCE` — 15 mappings (CL-MIG-001A)
- `00_PROJECT_CONTROL\04_EXTERNAL_REFERENCES` — 13 mappings (EXCLUDED / pointer lane)
- `00_PROJECT_CONTROL\05_BUILDER_CONTRACTS` — 2 mappings (CL-MIG-001B)
- `80_QUARANTINE\chachipti_pending_classification` (+ nested) — provisional only; blocked on classification

---

## Open items retained (not closed by this ratification)

1. Five program registry records remain **authority-deferred** (MAP02C-0050 … MAP02C-0054).
2. Nine Chachipti components remain **unclassified** (MAP02C-0039 … MAP02C-0047).
3. No destination parent may be created until a future packet explicitly authorizes materialization with `materialization_status` advanced beyond `NOT AUTHORIZED`.
4. No CL-MIG-001A / CL-MIG-001B copy eligibility is claimed.

---

## Safety posture

- Phase 02, 02B, and 02C records were **not edited**.
- No destination parents created.
- No source files copied, moved, or deleted.
- No git stage/commit/fetch/pull/push.
- No build, render, publish, or deploy.

---

## Verdict for this phase

**PASS — RATIFICATION RECORDED AND PARENT MANIFEST READY FOR AUTHORIZATION**
