# The Gradient Source-to-Destination Map Draft

Status: DRAFT / PLANNING ONLY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Last Refreshed: 2026-07-07 (post-`ca6410e` VIS-001 import; post-`d36444a` folder register housekeeping)

Constraint: This map does not authorize migration, extraction, source promotion, canon change, external edits, commits, or app/RPC work.

## Mapping Principles

- Source clusters remain intact during initial migration planning.
- Primary destination is provisional until migration approval.
- Functional references may point to source clusters without duplicating or fragmenting them.
- Derivatives require source citation and receipts.
- Release/export packages remain separate from source systems.
- Implementation folders do not define institutional authority.

## Source Cluster Map

| Source ID | Source Cluster | Provisional Primary Destination | Functional Reference Destinations | Migration Action Proposed | Receipt Required? | Status | Notes |
|---|---|---|---|---|---|---|---|
| `TG-SRC-PUB-001` | Publishing Constitution eight-volume source cluster | `07_publishing/publishing_constitution/` | `06_visual_language/`, `03_governance/`, `09_agents/`, `08_platform/`, `12_archive_refs/`, `11_receipts/` | `IMPORT_SOURCE_CLUSTER_LATER`; `CREATE_DERIVATIVE_CONTROL_LATER`; `REQUIRES_HUMAN_RATIFICATION` | Yes, before import or derivative controls | Reviewed / provisional | Preserve as intact publishing doctrine source cluster. Not a Gradient Constitution amendment unless later admitted and ratified through governance. Exact source pages/files still require inventory confirmation. |
| `TG-SRC-VIS-001` | GFVP source/spec/object/prompt/QC system | `06_visual_language/gfvp/` | `07_publishing/series/gfvp/`, `11_receipts/`, `04_registries/` | **`COMPLETED_SOURCE_CLUSTER_IMPORT`** (receipt `TG-REC-MIG-001`; commit `ca6410e`) | Yes — executed | **Imported / committed** | 248 md/csv imported under lifecycle paths per exact import manifest. Post-import audit PASS. **`TG-SRC-PUB-002` deferred** (25 PNGs on Drive; zip unlocated). Not canon promotion. Planning index: `06_visual_language/gfvp/SOURCE_CLUSTER_MANIFEST.md`. |
| `TG-SRC-PUB-002` | GFVP release/export packages | `07_publishing/series/gfvp/` | `06_visual_language/gfvp/`, `11_receipts/`, `12_archive_refs/` | `IMPORT_RELEASE_PACKAGE_LATER`; `REFERENCE_ONLY`; `REQUIRES_SOURCE_INVENTORY` | Yes, before any import; no for reference-only inventory entries | **Deferred / not imported** | Binaries, images, zips, PDFs, and release assets remain on Drive only. 25 PNGs in synced Drive; zip unlocated. Git should prefer lightweight manifests and references until authorized. |
| `TG-SRC-KNO-001` | Card System | `05_knowledge_systems/` | `04_registries/`, `02_stewardship/`, `03_governance/`, `11_receipts/`, later `08_platform/` | `IMPORT_SOURCE_CLUSTER_LATER`; `CREATE_DERIVATIVE_CONTROL_LATER`; `REQUIRES_SOURCE_INVENTORY` | Yes, before import or derivative controls | Reviewed / provisional | Split placement likely. Dedicated model unresolved. Implementation references must not define authority. |
| `TG-SRC-REG-001` | Engine Registry | `05_knowledge_systems/` and `04_registries/` | `09_agents/`, `03_governance/`, `11_receipts/`, later `08_platform/` | `IMPORT_SOURCE_CLUSTER_LATER`; `CREATE_DERIVATIVE_CONTROL_LATER`; `REQUIRES_SOURCE_INVENTORY` | Yes, before import or derivative controls | Reviewed / provisional | Split placement strongly supported. `09_agents/` is reserved only for executable or agent-facing contracts. |
| `TG-SRC-ARC-001` | Archive of Becoming | `12_archive_refs/` | `11_receipts/`, `03_governance/`, possible future archive model | `IMPORT_SOURCE_CLUSTER_LATER`; `REFERENCE_ONLY`; `REQUIRES_SOURCE_INVENTORY` | Yes, before import; possibly yes for archive/admission derivatives | Reviewed / provisional | Raw institutional memory and provenance references lean to `12_archive_refs/`. Future dedicated archive model remains possible. |

## Migration Action Vocabulary

- `NO_ACTION`: No migration-control action proposed for the source cluster at this time.
- `REFERENCE_ONLY`: Record a pointer, citation, or inventory reference without moving source material.
- `IMPORT_SOURCE_CLUSTER_LATER`: Candidate for later intact source-cluster import after inventory, review, and approval.
- `COMPLETED_SOURCE_CLUSTER_IMPORT`: Source-cluster import executed under approved receipt and committed to repo (planning record only; does not authorize further imports by itself).
- `IMPORT_RELEASE_PACKAGE_LATER`: Candidate for later release/export package import after package inventory, review, and approval.
- `CREATE_DERIVATIVE_CONTROL_LATER`: Candidate for a future derivative control that cites source and requires a receipt if it changes institutional behavior.
- `REQUIRES_SOURCE_INVENTORY`: Source locations, completeness, status, or package boundaries must be inventoried before action.
- `REQUIRES_HUMAN_RATIFICATION`: Human approval or governance ratification is required before the action can affect authority, canon, status, or institutional behavior.

## Open Questions

- Which source clusters have complete source locations? **`TG-SRC-VIS-001` complete for md/csv source system; `TG-SRC-PUB-002` binaries/zip still open.**
- Which source clusters are still Notion-only? Publishing Constitution, Card System, Engine Registry, Archive of Becoming — pending inventory passes.
- Which Drive packages correspond to release/export packages? GFVP `06_`/`08_` folders identified; zip unlocated.
- Which candidate imports require receipts? All physical imports; VIS-001 executed under `TG-REC-MIG-001`.
- Which candidate derivatives require human ratification? Authority-bearing clusters per map rows.

## Recommended Next Gate

**First source-cluster import complete (`TG-SRC-VIS-001`, `ca6410e`).** Choose the next **read-only inventory** track:

1. **`TG-SRC-PUB-002`** — GFVP release/export inventory (25 PNGs, deferred receipt md, zip location).
2. **`TG-SRC-PUB-001`** — Publishing Constitution source inventory (Notion-heavy; likely next source-cluster candidate).

Do not import without receipt gate. Do not create derivative controls yet. Do not resume app/RPC work.

## Output Summary

What changed:

- Created this source-to-destination map draft.
- Mapped known source clusters to provisional primary and functional reference destinations.
- Added draft migration action vocabulary for later approval gates.
- **2026-07-07 refresh:** Updated `TG-SRC-VIS-001` to imported/committed at `ca6410e` under `TG-REC-MIG-001`; marked `TG-SRC-PUB-002` deferred; repointed next gate to PUB-002 inventory or PUB-001 inventory.

What should be locked:

- This map is planning-only and not canonical.
- `TG-SRC-VIS-001` import record: 248 md/csv at `ca6410e`; receipt `TG-REC-MIG-001`; PUB-002 excluded.
- Source clusters remain intact on Drive; repo mirror is migration-control derivative only.
- No further migration, extraction, source promotion, canon change, external edit, commit, or app/RPC work is authorized by this map.

What remains living:

- Inventories for `TG-SRC-PUB-002`, `TG-SRC-PUB-001`, `TG-SRC-ARC-001`, `TG-SRC-REG-001`, `TG-SRC-KNO-001`.
- Exact release/export package locations (zip, cloud-only binaries).
- Receipt requirements for candidate imports and derivative controls.
- Human ratification requirements for authority-bearing derivatives.

Concrete next steps:

1. Authorize read-only **`TG-SRC-PUB-002`** inventory pass, and/or **`TG-SRC-PUB-001`** Publishing Constitution inventory pass.
2. Draft exact import manifest / migration plan only after inventory and human ratification — same receipt-gated playbook as VIS-001.
3. Do not move source files, create derivative controls, or resume app/RPC work until explicitly authorized.
