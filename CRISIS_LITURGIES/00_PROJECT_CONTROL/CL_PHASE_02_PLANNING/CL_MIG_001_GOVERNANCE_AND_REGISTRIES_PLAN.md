# CL-MIG-001
## Governance and Registries Migration Plan

**Batch ID:** CL-MIG-001  
**Batch class:** GOVERNANCE_AND_REGISTRIES  
**Mode:** PLAN ONLY — no copy authorized by this document alone  
**Sequence position:** First migration batch (Phase 02 charter §4)  
**Contains binaries:** NO (no PDFs, PNGs, layout sources, or collection binaries)

---

# 1. Objective

Seed the canonical namespace with institutional control records, schemas, and registries so later collection batches have a machine-readable authority surface.

This batch establishes structure and records. It does not admit collections, publish, archive, or resolve disputed volume states.

---

# 2. Preconditions

| Gate | Requirement |
|---|---|
| Phase 01 | CLOSED / PASS |
| Canonical root | `gradient-institution\CRISIS_LITURGIES` ratified |
| Planning package | Human review of this Phase 02 plan package |
| Explicit human authorization | Separate copy-authorization record required before any copy |
| Destination | Collision dispositions for CL-MIG-001 paths resolved |
| Schemas | `CL_MIGRATION_MANIFEST.schema.json` and `CL_EXTERNAL_BINARY_REFERENCE.schema.json` accepted |
| Git | Clean or explicitly acknowledged dirty state; no commit as part of copy unless separately authorized |
| Builder | Must not run |

---

# 3. Intended contents

| Item | Source (evidence / authority) | Planned target (under CRISIS_LITURGIES) | Action class |
|---|---|---|---|
| CL-PROD-ARCH-001 v0.2 | Drive `…\00_PROJECT_CONTROL_CL_OPS_001\` | `00_INSTITUTIONAL_CONTROL/authority/` | COPY_TEXT |
| CL-PROD-ARCH-001A ratification | same | `00_INSTITUTIONAL_CONTROL/accepted_decisions/` | COPY_TEXT |
| CL-OPS-001 | Drive / Notion export as available | `00_INSTITUTIONAL_CONTROL/authority/` | COPY_OR_EXPORT |
| CCR-CL-003 (accepted with patches) | Phase 01 / Notion | `03_RELEASE_PROFILES/CCR-CL-003/` | COPY_OR_AUTHOR |
| Release Profile Registry | Phase 01 decision surface | `03_RELEASE_PROFILES/` | AUTHOR_FROM_RATIFICATION |
| Canonical Root Ratification | Phase 01 final closure | `00_INSTITUTIONAL_CONTROL/accepted_decisions/` | AUTHOR_FROM_RATIFICATION |
| Mirror and Duplicate Doctrine | Phase 01 final closure | `00_INSTITUTIONAL_CONTROL/registries/mirrors/` + `duplicates/` | AUTHOR_FROM_RATIFICATION |
| Collection State Language Standard | Phase 01 | `04_COLLECTION_REGISTRY/` | AUTHOR_FROM_RATIFICATION |
| Collection State Map (skeleton) | Phase 00/00B + Phase 01 | `04_COLLECTION_REGISTRY/CL_COLLECTION_STATE_MAP.json` | AUTHOR_SKELETON |
| Phase 00 evidence package references | Drive control + Downloads packages | `00_PROJECT_CONTROL/` + `12_ARCHIVE/provenance/` refs | COPY_TEXT_OR_REFERENCE |
| Phase 01 closure records | Drive package | `00_PROJECT_CONTROL/` | COPY_TEXT |
| Migration schemas | This planning package | `06_BUILDER/schemas/` | COPY_SCHEMA |
| Chachipti packet (components only) | Repo `00_CHACHIPTI_PRODUCTION_LANE/` | Standards/handoffs as admitted; governance claims → `90_QUARANTINE/chachipti_governance_claims/` | CLASSIFY_THEN_COPY |
| Death Bit profile deferral | Phase 01-F | `03_RELEASE_PROFILES/deferred/CL_DEATH_OF_THE_BIT_SPECIAL_PROFILE/` | COPY_TEXT |

---

# 4. Exclusions (hard)

- All collection PNG/PDF/layout binaries
- CL-I…V / EV-001 / Death Bit production trees
- Creating `CL-VI` paths
- Promoting CL-VII out of quarantine
- Altering frozen releases on Drive or in repo
- Deleting or retiring any legacy root
- Global duplicate-group cleanup

---

# 5. Relationship classes used in this batch

| Class | Meaning |
|---|---|
| `AUTHORITATIVE_CONTROL_RECORD` | Ratified governance text |
| `DERIVED_REGISTRY` | Machine-readable registry authored from ratification |
| `EVIDENCE_REFERENCE` | Pointer/hash to Phase 00/00B evidence without relocating roots |
| `QUARANTINE_GOVERNANCE` | Preserved but non-controlling claims |
| `SCHEMA` | Validation contracts for later batches |

---

# 6. Copy method (when later authorized)

1. Build `CL_MIG_001_MIGRATION_MANIFEST.json` conforming to schema.
2. Dry-run: existence, collision, disk space, Git status, path-ref scan, rollback simulation.
3. Copy text/JSON only into target paths listed in manifest.
4. Hash every written file; record in manifest and batch receipt.
5. Do not delete sources.
6. Do not commit unless separately authorized.

Verification: byte-identical SHA-256 for pure copies; schema validation for authored JSON; human spot-check of quarantine classification for Chachipti materials.

---

# 7. Rollback method

1. Delete **only** files listed as written by CL-MIG-001 receipt (never sources).
2. Restore any overwritten targets from pre-batch snapshot if overwrite was authorized (default: no overwrite).
3. Leave legacy Drive and repo sources untouched.
4. Record rollback receipt under `00_PROJECT_CONTROL/CL_MIG_001/`.

Default policy: **copy-only, no overwrite**. If a target exists, stop (collision).

---

# 8. Human authorization required

A future record must explicitly state:

```text
AUTHORIZE_COPY: CL-MIG-001
DESTINATION: C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES
DELETION: NO
RENAME_SOURCES: NO
BUILDER: NO
COMMIT: <YES/NO as separately decided>
```

Until that record exists, this plan is non-operative for filesystem mutation beyond the planning directory already authorized.
