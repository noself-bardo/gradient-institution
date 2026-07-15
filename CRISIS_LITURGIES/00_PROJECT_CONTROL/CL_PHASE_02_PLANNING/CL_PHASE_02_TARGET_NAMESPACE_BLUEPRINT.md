# CL-PHASE-02-OUT-001
## Target Namespace Blueprint

**Mode:** PLAN ONLY  
**Date:** 2026-07-13  
**Authority:** CL-PHASE-02-CHARTER, CL-PROD-ARCH-001 §12 (provisional), CL-PHASE-01-FINAL  
**Physical mutation:** NOT AUTHORIZED

---

# 1. Canonical targets (Phase 01 ratified)

| Role | Path |
|---|---|
| Canonical active repository | `C:\Users\steve\Projects\gradient-institution` |
| Canonical Crisis Liturgies namespace | `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES` |
| Archive / frozen-release / controlled-mirror authority | `C:\Users\steve\My Drive\The Gradient` |
| Legacy Death of the Bit handoff mirror | `C:\Users\steve\My Drive\CL_DEATH_OF_THE_BIT` |

`gradient-institution\CRISIS_LITURGIES` is the sole active operational root for future Crisis Liturgies production (L-001 / NP-001).  
Drive remains freeze, distribution, and mirror authority (L-010 / NP-005).  
Git holds machine-readable operational state, manifests, checksums, and external binary references (L-011).

---

# 2. Design posture

1. Adopt CL-PROD-ARCH-001 §12 topology as the **proposed** target shape.
2. Treat that topology as **provisional until dry-run** (architecture already states this).
3. Keep Phase 00–02 control artifacts under `00_PROJECT_CONTROL/` until CL-MIG-001 folds them into institutional control.
4. Do **not** create a CL-VI collection directory.
5. Keep CL-VII under quarantine only.
6. Keep CL-EV-001 as `RETURN_FOR_REVISION` (not released / not archive-admitted by this plan).
7. Keep The Death of the Bit as `WORKING_ASSEMBLY` (special profile deferred; not an active template).
8. Do not infer publication or archive admission from path placement.

---

# 3. Proposed top-level namespace

```text
CRISIS_LITURGIES/
├── 00_PROJECT_CONTROL/                 # transitional Phase 00–02 control lane
├── 00_INSTITUTIONAL_CONTROL/           # durable authority / decisions / registries
├── 01_CANON/
├── 02_PRODUCTION_STANDARDS/
├── 03_RELEASE_PROFILES/
├── 04_COLLECTION_REGISTRY/
├── 05_VOLUMES/                         # active + working volume trees only
├── 06_BUILDER/
├── 07_ACTIVE_RUNS/
├── 08_CORRECTIVE_LANES/
├── 09_RELEASE_CANDIDATES/
├── 10_FROZEN_RELEASES/                 # manifests + pointers; large binaries may be external
├── 11_PUBLICATION/
├── 12_ARCHIVE/
├── 13_HANDOFFS/
├── 90_QUARANTINE/
└── 99_TEMP/
```

### Transitional note

Today the live tree already contains:

- `00_CHACHIPTI_PRODUCTION_LANE/`
- `EXPANSION_VOLUMES/CL-EV-001_THE_PYGMALION_MACHINE/`
- `00_CHACHIPTI_PRODUCTION_LANE.zip`

Those are **source collisions**, not approved final layout. Disposition is planned in the collision report and source-to-target map. No rename or move occurs in Phase 02 planning.

---

# 4. Layer responsibilities

| Path | Holds | Must not hold |
|---|---|---|
| `00_PROJECT_CONTROL/` | Phase packets, planning receipts, migration batch authorizations | Collection binaries |
| `00_INSTITUTIONAL_CONTROL/` | Authority records, accepted decisions, state machine, registries, current status | Generated art |
| `01_CANON/` | Canon exports, doctrines, symbol system, historical versions | Working proofs |
| `02_PRODUCTION_STANDARDS/` | Generation, print, archive, naming, QC, corrective-lane standards | Release binaries |
| `03_RELEASE_PROFILES/` | Ratified / deferred profiles; CCR-CL-003 artifacts | Volume source trees |
| `04_COLLECTION_REGISTRY/` | Multidimensional collection state map; IDs; qualified language | Unqualified FINAL/LOCKED prose alone |
| `05_VOLUMES/` | One folder per admitted collection ID under active or working status | CL-VI; CL-VII production tree |
| `06_BUILDER/` | Schemas, validators, compiler stubs, tests — planning only until builder phase | Live render outputs |
| `07_ACTIVE_RUNS/` | Registered run workspaces | Frozen releases |
| `08_CORRECTIVE_LANES/` | Corrective intakes and namespaced candidates | Overwrites of frozen releases |
| `09_RELEASE_CANDIDATES/` | Candidate packages awaiting human disposition | Declared frozen releases |
| `10_FROZEN_RELEASES/` | Immutable release manifests, checksums, provenance, external refs | In-place edits of frozen binaries |
| `11_PUBLICATION/` | Publication records linking approval ↔ manifest ↔ artifact ↔ URL | Inference from HTTP success |
| `12_ARCHIVE/` | Superseded / historical / rejected / provenance | Active production |
| `13_HANDOFFS/` | Cursor / Codex / external handoffs as records | Runtime authority |
| `90_QUARANTINE/` | Quarantined evidence with release conditions | Production control |
| `99_TEMP/` | Ephemeral registered temp only | Durable institutional state |

---

# 5. Collection placement rules

| Collection | Target class | Proposed path (plan) | State language (Phase 01 / 00B) |
|---|---|---|---|
| Governance / registries | CONTROL | `00_INSTITUTIONAL_CONTROL/`, `03_RELEASE_PROFILES/`, `04_COLLECTION_REGISTRY/` | N/A |
| CL-I | HISTORICAL_RELEASE_REFERENCE | `12_ARCHIVE/historical/CL-I_…` + `10_FROZEN_RELEASES/CL-I_…` manifests | COMPLETE / LOCKED HISTORICAL RELEASE |
| CL-II | HISTORICAL_RELEASE_REFERENCE | same pattern | COMPLETE / LOCKED HISTORICAL RELEASE |
| CL-III | FROZEN_RELEASE_REFERENCE | `10_FROZEN_RELEASES/CL-III_…` + archive refs | FROZEN RELEASE / ARCHIVE EVIDENCE |
| CL-IV | QUALIFIED_FROZEN_SNAPSHOT | `10_FROZEN_RELEASES/CL-IV_…` with qualified state record | FROZEN SNAPSHOT COMPLETE — NOT PRINT-READY |
| CL-V | VERIFIED_FROZEN_RELEASE | `05_VOLUMES/CL-V_DUAL_POWER_DOMESTICS/` (tree) + `10_FROZEN_RELEASES/CL-V_…` | Verified frozen release; mirrors registered |
| CL-VI | UNASSIGNED | **no directory** | NUMBER UNASSIGNED |
| CL-VII | QUARANTINED_EVIDENCE | `90_QUARANTINE/CL-VII/` only | DISPUTED / QUARANTINED |
| CL-EV-001 | RETURN_FOR_REVISION | `05_VOLUMES/CL-EV-001_THE_PYGMALION_MACHINE/` | RETURN_FOR_REVISION |
| The Death of the Bit | WORKING_ASSEMBLY | `05_VOLUMES/CL_DEATH_OF_THE_BIT/` (qualified working) | WORKING_ASSEMBLY; profile DEFERRED |

---

# 6. Volume template (proposed)

```text
{VOLUME_ID}_{SLUG}/
├── 00_CONTROL/
├── 01_SOURCE/
├── 02_VOLUME_SPEC/
├── 03_PAGE_SPECS/
├── 04_RENDER_PACKETS/
├── 05_GENERATED_ASSETS/          # may be external-ref heavy
├── 06_QC/
├── 07_LAYOUT/
├── 08_RELEASE_CANDIDATES/
├── 09_FROZEN_RELEASE/            # immutable once admitted
└── 10_PROVENANCE/
```

Historical volumes may use a thinner template (registry + frozen-release manifests + external refs) without inventing missing modern production trees.

---

# 7. External binary policy (summary)

Large PDFs/PNGs and Drive-resident release payloads may remain on Drive.

The repository must hold, for each referenced binary:

- role classification;
- SHA-256;
- stable Drive-relative or absolute source path;
- recovery route;
- relationship class (`CANONICAL_RELEASE`, `REGISTERED_MIRROR`, `WORKING_PROOF`, `QUARANTINE_EVIDENCE`, etc.).

Schema: `CL_EXTERNAL_BINARY_REFERENCE.schema.json`.

---

# 8. Explicit non-goals of this blueprint

- No physical copy, move, rename, or delete.
- No builder run.
- No publication or archive admission.
- No CL-VI folder.
- No promotion of Pygmalion out of `RETURN_FOR_REVISION`.
- No promotion of Death of the Bit out of `WORKING_ASSEMBLY`.
- No global classification of all 1,276 duplicate-hash groups.

---

# 9. Dry-run gates before any later copy phase

1. Destination collision disposition ratified for every conflicting path.
2. CL-MIG-001 governance batch approved.
3. Migration manifest schema validated.
4. External binary reference strategy accepted.
5. Path-reference scan plan executed for the batch.
6. Rollback simulation demonstrated for the batch.
