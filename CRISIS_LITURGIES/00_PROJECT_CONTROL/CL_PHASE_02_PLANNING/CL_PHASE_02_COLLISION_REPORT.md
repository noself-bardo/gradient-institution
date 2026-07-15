# CL-PHASE-02-OUT-007
## Collision Report

**Mode:** PLAN ONLY  
**Date:** 2026-07-13  
**Scope:** Destination collisions and structural conflicts inside the canonical namespace plan  
**Rule:** Identical hashes are not permission to delete. Collisions stop copy until human disposition.

---

# 1. Executive finding

The proposed target namespace is **not an empty directory**. Live trees already occupy paths that the blueprint wants to standardize. Phase 02 planning therefore treats the current `CRISIS_LITURGIES` contents as **pre-migration occupancy**, not as ratified final layout.

No rename, move, or delete is authorized by this report.

---

# 2. Destination occupancy (canonical namespace today)

| Path | Occupancy class | Collision with blueprint | Planned disposition (plan only) |
|---|---|---|---|
| `CRISIS_LITURGIES/00_CHACHIPTI_PRODUCTION_LANE/` | Live governance/handoff packet | Conflicts with clean `00_INSTITUTIONAL_CONTROL` / `02_PRODUCTION_STANDARDS` / `13_HANDOFFS` split | Classify: admit conforming components; quarantine overbroad governance claims (Q-001); leave source until CL-MIG-001 authorized |
| `CRISIS_LITURGIES/00_CHACHIPTI_PRODUCTION_LANE.zip` | Package duplicate | Same | Register as release/handoff duplicate or evidence; do not delete |
| `CRISIS_LITURGIES/EXPANSION_VOLUMES/CL-EV-001_THE_PYGMALION_MACHINE/` | Live EV-001 tree | Blueprint prefers `05_VOLUMES/CL-EV-001_…` and retires `EXPANSION_VOLUMES/` as a top-level class | Target path currently empty; source path must remain until copy+verify; eventual retirement of `EXPANSION_VOLUMES/` requires separate human authorization after NP-010 gates |
| `CRISIS_LITURGIES/00_PROJECT_CONTROL/CL_PHASE_02_PLANNING/` | Authorized planning write | None (intended) | Retain |

---

# 3. Repo-sibling collision (outside namespace but in migration path)

| Path | Notes |
|---|---|
| `gradient-institution/CRISIS_LITURGIES_V_DUAL_POWER_DOMESTICS/` | Verified CL-V live tree (CF-001 closed). Planned future target: `CRISIS_LITURGIES/05_VOLUMES/CL-V_DUAL_POWER_DOMESTICS/`. Copy would create a second tree until source retirement is separately authorized. |

---

# 4. Name / topology collisions

| Conflict ID | Subject | Severity | Detail | Required human decision |
|---|---|---|---|---|
| COL-001 | `00_PROJECT_CONTROL` vs `00_INSTITUTIONAL_CONTROL` | S2 | Packet and Phase 00–02 use `00_PROJECT_CONTROL`; architecture §12 proposes `00_INSTITUTIONAL_CONTROL`. | Keep both during transition (recommended) or rename after MIG-001 |
| COL-002 | `EXPANSION_VOLUMES/` vs `05_VOLUMES/` | S3 | Live EV-001 uses expansion path; blueprint uses volumes path. | Authorize copy to `05_VOLUMES` then later controlled retirement of empty expansion path |
| COL-003 | Chachipti lane folder vs institutional standards | S3 | Packet claims vs CL-OPS / CL-PROD-ARCH boundaries. | Follow Q-001; no silent adoption as constitution |
| COL-004 | CL-V three matching final PDFs | S4 | Same SHA-256 at multiple paths. | Classify canonical + registered mirrors; prohibit deletion |
| COL-005 | CL-I/II/III/IV multiple candidate roots | S4 | Collection candidates report many FINAL/LOCK/RELEASE artifacts with differing hashes. | Per-batch canonical selection; stop on disputed state |
| COL-006 | CL-EV-001 repo tree vs Drive tree | S4 | Dual high-confidence roots; completion claims disputed. | Keep `RETURN_FOR_REVISION`; choose working canonical only after CF-004 reconciliation |
| COL-007 | Death Bit `_codex_work` vs `My Drive\CL_DEATH_OF_THE_BIT` | S3 | Working assembly vs legacy handoff mirror. | Working tree vs mirror classification; profile remains deferred |
| COL-008 | Proposed `05_VOLUMES/CL-EV-001_…` currently absent | S1 | Empty target — good for future copy | Still requires dry-run and authorization |
| COL-009 | Forbidden CL-VI path creation | S3 | Negative finding; number unassigned | Never create directory |
| COL-010 | CL-VII production folder temptation | S4 | Only handoff evidence exists | Quarantine only |

---

# 5. Duplicate doctrine interaction (CF-014)

Phase 00B quantified **1,276** duplicate-hash groups.

This planning phase:

- does **not** classify all groups;
- requires classification **only for groups touched by an authorized batch**;
- treats collision of destinations as a hard stop even when hashes match.

---

# 6. Stop rule for future copy agents

Stop and return for human review if:

1. target path already exists and overwrite is not explicitly authorized;
2. source state is `DISPUTED` / `UNKNOWN` without a quarantine path;
3. collection ID would create CL-VI;
4. operation would modify a frozen release binary;
5. identical-hash peers lack relationship classification for the batch;
6. rollback cannot name exact written targets.

---

# 7. Recommended disposition order for collisions

1. COL-001 transitional control naming (document, do not block MIG-001).
2. COL-003 Chachipti classification inside MIG-001.
3. COL-004 / COL-005 / COL-006 / COL-007 only inside their later collection batches.
4. COL-002 only after EV-001 copy verification.
5. COL-009 / COL-010 permanent prohibitions.
