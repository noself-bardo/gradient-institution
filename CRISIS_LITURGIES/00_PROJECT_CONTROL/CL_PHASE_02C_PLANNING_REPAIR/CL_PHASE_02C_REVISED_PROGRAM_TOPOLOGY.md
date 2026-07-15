# CL_PHASE_02C — Revised Program Topology

**Date (UTC):** 2026-07-13T20:11:36Z  
**Repository posture:** REPOSITORY CANDIDATE — INSTITUTIONAL AUTHORITY NOT YET RATIFIED  
**Mode:** PLANNING REPAIR ONLY — no destination materialization  

---

## Locked direction applied

1. Crisis Liturgies is a **program** within The Gradient.
2. No second institutional hierarchy inside Crisis Liturgies.
3. Proposed Phase 02 stack `00_INSTITUTIONAL_CONTROL` … `99_TEMP` is **rejected**.
4. Institution-level constitution / governance / stewardship / registries remain in existing Gradient lanes (`01_constitution`, `02_stewardship`, `03_governance`, `04_registries`, etc.) and are **referenced**, not copied into CL.
5. Program operational control remains under `CRISIS_LITURGIES\00_PROJECT_CONTROL`.
6. Production lifecycle uses explicit program paths (`10_VOLUMES_ACTIVE` … `90_TEMPORARY`).
7. Existing occupancy retained: `00_CHACHIPTI_PRODUCTION_LANE`, `EXPANSION_VOLUMES`.
8. No CL-VI folder or placeholder.
9. Every proposed new parent is **NOT MATERIALIZED**; `materialization_authorized = NO`.

---

## Tree (informative)

```text
CRISIS_LITURGIES/                              # program root (existing)
├── 00_PROJECT_CONTROL/                        # EXISTING — program control
│   ├── CL_PHASE_02_PLANNING/                  # EXISTING — do not edit
│   ├── CL_PHASE_02B_PLANNING_QC/              # EXISTING — do not edit
│   ├── CL_PHASE_02C_PLANNING_REPAIR/          # THIS PACKET
│   ├── 01_PROGRAM_GOVERNANCE/                 # PROPOSED — NOT MATERIALIZED
│   ├── 02_PROGRAM_REGISTRIES/                 # PROPOSED — NOT MATERIALIZED
│   ├── 03_PHASE_EVIDENCE/                     # PROPOSED — NOT MATERIALIZED
│   ├── 04_EXTERNAL_REFERENCES/                # PROPOSED — NOT MATERIALIZED (pointers only)
│   ├── 05_BUILDER_CONTRACTS/                  # PROPOSED — NOT MATERIALIZED
│   └── 06_MIGRATION_BATCHES/                  # PROPOSED — NOT MATERIALIZED
├── 00_CHACHIPTI_PRODUCTION_LANE/              # EXISTING — classify pending
├── EXPANSION_VOLUMES/                         # EXISTING — EV working trees
├── 10_VOLUMES_ACTIVE/                         # PROPOSED — NOT MATERIALIZED
├── 20_SOURCE/                                 # PROPOSED — NOT MATERIALIZED
├── 30_GENERATED_OUTPUT/                       # PROPOSED — NOT MATERIALIZED
├── 40_QC/                                     # PROPOSED — NOT MATERIALIZED
├── 50_RELEASE_ASSEMBLY/                       # PROPOSED — NOT MATERIALIZED
├── 60_RELEASE_SNAPSHOTS/                      # PROPOSED — NOT MATERIALIZED
├── 70_ARCHIVE/                                # PROPOSED — NOT MATERIALIZED
├── 80_QUARANTINE/                             # PROPOSED — NOT MATERIALIZED
└── 90_TEMPORARY/                              # PROPOSED — NOT MATERIALIZED
```

Rejected (do not create): `00_INSTITUTIONAL_CONTROL`, `01_CANON` institutional clone, `CL-VI`, and any path that relocates Gradient constitution into CL.

---

## Institutional references

CL may author **pointer records** under `00_PROJECT_CONTROL/04_EXTERNAL_REFERENCES/` that cite:

- `gradient-institution/01_constitution`
- `gradient-institution/02_stewardship`
- `gradient-institution/03_governance`
- `gradient-institution/04_registries`
- Drive archive/frozen-release surfaces under `My Drive\The Gradient`

Pointer authoring is not authorized in this phase.

---

## Materialization

All proposed parents: `materialization_authorized = NO`.  
Creating them requires separate human decision **RAT-CL-006** after topology ratification **RAT-CL-001**.
