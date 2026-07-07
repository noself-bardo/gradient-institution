# The Gradient Folder Decision Register

Status: DRAFT / MIGRATION WORKSPACE ONLY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Constraint: No migration or restructuring authorized by this document.

Active draft state: `REPO_STRUCTURE_PROPOSAL.md` v0.2 and `MIGRATION_MANIFEST.md` v0.2 accepted as draft migration workspace only — not final institutional architecture.

## Current Locked Draft Assumptions

These placements are treated as **locked for draft migration planning** until explicitly revised. They do not authorize file moves.

- v0.2 top-level structure is accepted as **draft migration workspace only**.
- GFVP source/spec/object/prompt/QC system (`TG-SRC-VIS-001`) maps to `06_visual_language/gfvp/`.
- GFVP released/export packages (`TG-SRC-PUB-002`) map to `07_publishing/series/gfvp/`.
- Inventories map to `10_inventories/`.
- Receipts, reviews, and QC summaries map to `11_receipts/`.
- Platform, app, Supabase, and Control Center work (`TG-PLATFORM-007`) remain **frozen** under `08_platform/`.
- **`TG-SRC-VIS-001`** physically imported and committed at `ca6410e` under receipt **`TG-REC-MIG-001`** (248 md/csv into `06_visual_language/gfvp/`). Draft migration workspace only — **not canon promotion**.
- **`TG-SRC-PUB-002`** physically imported and committed at `c3154f0` under receipt **`TG-REC-MIG-002`** (46 md/PNG into `07_publishing/series/gfvp/`). Draft migration workspace only — **not canon promotion**.
- All other source clusters remain unmigrated. Cursor/Git remains a draft migration workspace only.

## Completed Physical Imports (Draft Record)

| Source ID | Receipt | Commit | Scope | Notes |
|---|---|---|---|---|
| `TG-SRC-VIS-001` | `TG-REC-MIG-001` | `ca6410e` | 248 md/csv → `06_visual_language/gfvp/` | PUB-002 excluded from VIS-001 scope; post-import audit PASS. Not canon promotion. |
| `TG-SRC-PUB-002` | `TG-REC-MIG-002` | `c3154f0` | 46 md/PNG → `07_publishing/series/gfvp/` | `07_OUTPUT_QC/` reference-only; zip excluded; VIS-001 boundary preserved; post-import audit PASS. Not canon promotion. |

This table records executed draft migration only. It does not authorize further imports, canon change, or new cluster work without explicit authorization.

## Decision Table

| Source Area | Candidate Destination(s) | Current Lean | Risk Level | Why Unresolved | Evidence Needed | Next Review Action | Decision Status |
|---|---|---|---|---|---|---|---|
| `03 Book of Becoming` | `02_stewardship/`, `12_archive_refs/`, possible future dedicated area | No lean | Medium | Curated wisdom/steward notes may be practice, reflective memory, or narrative archive — distinct from raw Archive of Becoming per source reviews. | Notion page body (authorized review only); authority status; whether entries are doctrine, practice, or reflections; boundary vs `04 Archive of Becoming`. | Classify by function using Initial Decision Logic; do not fetch Notion unless authorized. | Unresolved |
| `04 Archive of Becoming` | `12_archive_refs/`, possible future archive model, `03_governance/` for archive rules, `11_receipts/` for receipt artifacts | `12_archive_refs/` provisional (`TG-SRC-ARC-001`) | **High** | Preserves raw institutional memory and provenance; premature placement could flatten memory, official records, and governance into a generic reference folder. | Linked admission/archive pages; official record rules; archive entry structure; custody/retrieval requirements; GFVP archive-adjacent specs already reviewed partially. | Complete source inventory; decide whether `12_archive_refs/` suffices or future archive model required. | **Explicitly unresolved** |
| `05 Engine Registry` | `05_knowledge_systems/`, `04_registries/`, `09_agents/` only for executable agent-facing contracts | Split placement likely (`TG-SRC-REG-001`) | **High** | Records engines, classes, statuses, validation basis, and lock boundaries; premature placement could confuse conceptual doctrine, registry state, and execution contracts. | Representative engine pages; registry fields; official statuses; automation boundaries; GFVP Engine/Registry specs cross-refs. | Define rule: concept file vs registry row vs agent contract; complete source inventory. | **Explicitly unresolved** |
| `06 Card System` | `05_knowledge_systems/`, `04_registries/`, `02_stewardship/`, `03_governance/`, `11_receipts/`, later `08_platform/` | `05_knowledge_systems/` primary lean; split likely (`TG-SRC-KNO-001`) | **High** | Cards are central knowledge objects derived from engine metabolization; premature placement could flatten conceptual, registry, stewardship, visual, and platform concerns. | Card taxonomy, archetypes, lifecycle rules, relationship grammar; Engine Metabolization Template linkage. | Complete source inventory before any card file migration. | **Explicitly unresolved** |
| `07 Foundational Lineages` | `05_knowledge_systems/`, `12_archive_refs/`, `01_constitution/` if authority-bearing | No lean | Medium | Lineages may be provenance, canon background, or interpretive knowledge structure — not yet in source cluster map. | Lineage page contents; authority role; whether lineages govern decisions or merely document descent. | Review source page when authorized; assign provisional source ID. | Unresolved |
| `08 Praxis Domains` | `02_stewardship/`, `03_governance/`, `05_knowledge_systems/`, possible future domain folder | No lean | Medium | Praxis may describe applications, operating contexts, or governance for implementation domains. | Domain examples; whether domains define practice or merely classify work. | Review source page when authorized; classify by Initial Decision Logic. | Unresolved |
| `09 Worlds and Case Studies` | `12_archive_refs/`, `05_knowledge_systems/`, possible future case-study area | No lean | Medium | Worlds/case studies may be provenance, applied examples, or active project families (includes visual canon projects per root purpose). | Page contents; active vs archival status of case-study families; relationship to GFVP/visual canon. | Review source page when authorized; separate active projects from archive refs. | Unresolved |
| `12 Community Charters` | `03_governance/`, `02_stewardship/`, `01_constitution/` if authority-bearing | No lean | Medium–High | Charters may be governance templates, stewardship practice, or authority-bearing community adaptation rules. | Charter contents; intended authority; templates vs ratified documents. | Review source page when authorized; require human ratification if authority-bearing. | Unresolved |
| Publishing Constitution | `07_publishing/publishing_constitution/` primary; functional refs to `06_visual_language/`, `03_governance/`, `09_agents/`, `08_platform/`, `12_archive_refs/`, `11_receipts/`; `01_constitution/` only if governance-admitted | `07_publishing/publishing_constitution/` (`TG-SRC-PUB-001`) | **High** | Eight-volume ratified publishing-department doctrine; not a Gradient Constitution amendment unless later admitted. Misplacement as pure workflow or top-level doctrine distorts architecture. | Exact Notion page completeness; binding index/source packet; extraction policy for derivative controls. | Decide extraction policy and human ratification path before migration. | **Explicitly unresolved** |
| Engine Registry dual-placement question | `05_knowledge_systems/` + `04_registries/`; `09_agents/` for executable contracts only | Dual-placement likely | **High** | Same cluster as `05 Engine Registry` — engines may need intact source cluster plus registry derivative plus agent-facing contracts without fragmenting authority. | Engine data model; source-of-truth expectations; which layers are registry vs knowledge vs agent. | Resolve as part of `TG-SRC-REG-001` inventory and folder decision — not before source review. | Unresolved |
| Archive model question | `12_archive_refs/`, possible future dedicated archive model, `03_governance/` for archive rules | No lean | **High** | Same domain as `04 Archive of Becoming` — archive may be institutionally important beyond lightweight references. | Archive purpose; preservation policy; admission workflow; provenance requirements. | Decide if `12_archive_refs/` is terminal or placeholder for future archive ontology. | Unresolved |
| Existing v0.1 placeholder folder rename/restructure question | Rename v0.1 folders to v0.2 structure; leave until approval; bridge with README redirects | **Leave until approval** | Medium | Renaming empty placeholders before source placement decisions resolve could create churn and false permanence. | Human approval of v0.2 physical folder changes; timing relative to further source imports. | Use this register to resolve placements first; restructure only after explicit approval. First source import completed (`TG-SRC-VIS-001`, `ca6410e`). | Unresolved |

## Initial Decision Logic

Provisional classification rules for **candidate** destinations only. No placement is final without source review and human approval where required.

- If material defines institutional authority or enduring doctrine, candidate destination is `01_constitution/`, but only after source review.
- If material defines practice, care, procedure, or stewardship routines, candidate destination is `02_stewardship/`.
- If material records decisions, policies, ratification, governance rules, or lifecycle controls, candidate destination is `03_governance/`.
- If material tracks IDs, statuses, relationships, state, event schemas, or dashboard-readable registry data, candidate destination is `04_registries/`.
- If material defines cards, claims, evidence, engines, interpretive systems, capability systems, or knowledge models, candidate destination is `05_knowledge_systems/`.
- If material defines visual canon, GFVP, aesthetic systems, prompts, object specs, visual QC, or atlas logic, candidate destination is `06_visual_language/`.
- If material is a released issue, export, publication package, or publishing workflow, candidate destination is `07_publishing/`.
- If material concerns apps, Supabase, dashboards, implementation, RPCs, or Control Center software, candidate destination is `08_platform/`.
- If material concerns Codex, Cursor, Zo, agent contracts, runbooks, or automation boundaries, candidate destination is `09_agents/`.
- If material is source inventory, candidate destination is `10_inventories/`.
- If material is approval proof, QC, review, receipt, handoff, or audit trail, candidate destination is `11_receipts/`.
- If material is historical provenance, legacy context, abandoned path, or founding archive reference, candidate destination is `12_archive_refs/`.

**Cross-cutting rules:**

- Source clusters remain intact during initial migration planning (`SOURCE_TO_DESTINATION_MAP_DRAFT.md`).
- Functional references may point to source clusters without duplicating or fragmenting them.
- Implementation folders (`08_platform/`, `09_agents/`) must not define institutional authority.
- High-risk areas require source inventory and human ratification before folder creation or rename.

## Required Treatment of High-Risk Areas

These four areas remain **explicitly unresolved**. Premature folder assignment could distort institutional architecture.

### `04 Archive of Becoming` (`TG-SRC-ARC-001`)

**Risk: High.**

Archive preserves raw institutional memory — becoming events, revisions, failed ideas, abandoned paths, contradictions — without forcing narrative or canon. Placing it too early under a generic reference path, governance folder, or knowledge system could collapse the distinction between memory, provenance, official records, and operating doctrine. A future dedicated archive model may be required.

### `05 Engine Registry` (`TG-SRC-REG-001`)

**Risk: High.**

Engine Registry spans conceptual engine definitions, operational registry state, validation basis, lock boundaries, and possibly executable agent contracts. Dual placement between `05_knowledge_systems/` and `04_registries/` is likely, but deciding too early — or collapsing into `08_platform/` or `09_agents/` — could make registry data appear implementation-defined rather than institutionally governed.

### `06 Card System` (`TG-SRC-KNO-001`)

**Risk: High.**

Cards sit at the center of the knowledge model and connect to stewardship exercises, GFVP object specs, registries, and future platform surfaces. A single-folder placement under `05_knowledge_systems/` alone may be insufficient; split references are likely. Premature migration could treat cards as mere documentation rather than governed knowledge objects.

### Publishing Constitution (`TG-SRC-PUB-001`)

**Risk: High.**

The eight-volume Publishing Constitution is ratified publishing-department doctrine for visual knowledge production, explicitly not a Gradient Constitution amendment unless later admitted through governance. Placing it under `07_publishing/` vs `01_constitution/`, or extracting derivative controls too early, could misstate its authority relative to institutional doctrine and GFVP visual canon.

## Review Notes

This register is a living migration-control document. It tracks **unresolved** placement decisions only.

It does **not** authorize:

- folder restructuring or rename of v0.1 placeholders
- file migration or source import
- source promotion or canon change
- Notion, Drive, or Supabase edits
- app/RPC/platform work (`TG-PLATFORM-007` remains paused)
- commits

Do not fetch additional Notion pages unless explicitly authorized for a named inventory pass.

## Output Summary

### What changed

- Created/updated this folder decision register to track unresolved Notion/source placement decisions before any folder restructuring.
- Locked v0.2 draft assumptions for GFVP, inventories, receipts, and frozen platform work.
- Documented twelve unresolved source areas plus three cross-cutting questions (dual-placement, archive model, v0.1 rename).
- Applied Initial Decision Logic and high-risk treatment for Archive, Engine Registry, Card System, and Publishing Constitution.
- **2026-07-07 closeout housekeeping:** Recorded `TG-SRC-PUB-002` physical import committed at `c3154f0` under `TG-REC-MIG-002`; 46 md/PNG into `07_publishing/series/gfvp/`.

### What should be locked

- v0.2 top-level structure as **draft migration workspace only** — not final ontology.
- Resolved draft leans: `TG-SRC-VIS-001` → `06_visual_language/gfvp/` (**imported at `ca6410e`**); `TG-SRC-PUB-002` → `07_publishing/series/gfvp/` (**imported at `c3154f0`**); inventories → `10_inventories/`; receipts → `11_receipts/`.
- `TG-REC-MIG-001` execution record for VIS-001 (248 md/csv; PUB-002 excluded from VIS-001 scope).
- `TG-REC-MIG-002` execution record for PUB-002 (46 md/PNG; `07_`/zip excluded).
- `TG-PLATFORM-007` and all app/RPC work remain paused.
- No further migration, restructuring, canon promotion, external edits, or commits authorized by this register.

### What remains living

- All decision table rows marked Unresolved or Explicitly unresolved.
- High-risk placement for Archive, Engine Registry, Card System, Publishing Constitution.
- Engine Registry dual-placement and archive model questions.
- v0.1 placeholder folder rename/restructure timing.
- Medium-risk areas: Book of Becoming, Foundational Lineages, Praxis Domains, Worlds and Case Studies, Community Charters.
- **`TG-SRC-PUB-001`** Publishing Constitution — recommended next inventory candidate (frozen until authorized).
- Migration closeout state: `MIGRATION_CLOSEOUT_STATE_DRAFT.md` — pending closeout commit.

### Concrete next steps

1. **Migration closeout:** Commit `MIGRATION_CLOSEOUT_STATE_DRAFT.md` and register/map/plan housekeeping when authorized — then pause migration until a new track is explicitly authorized.
2. If resuming: start with read-only **`TG-SRC-PUB-001`** inventory (recommended next cluster).
3. Use Initial Decision Logic during authorized source reviews — do not assign final folders from metadata alone.
4. Resolve dual-placement and archive model questions only after source review and human ratification where required.
5. Defer v0.1 → v0.2 physical folder rename until placement decisions and migration authorization are explicit.
