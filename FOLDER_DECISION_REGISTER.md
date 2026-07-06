# The Gradient Folder Decision Register

Status: DRAFT / MIGRATION WORKSPACE ONLY

Authority: Not canonical

Constraint: No migration or restructuring authorized by this document

## Current Locked Draft Assumptions

- v0.2 top-level structure is accepted as draft migration workspace only.
- GFVP source/spec/object/prompt/QC system maps to `06_visual_language/gfvp/`.
- GFVP released/export packages map to `07_publishing/series/gfvp/`.
- Inventories map to `10_inventories/`.
- Receipts/reviews/QC summaries map to `11_receipts/`.
- Platform/app/Supabase work remains frozen under `08_platform/`.

## Decision Table

| Source Area | Candidate Destination(s) | Current Lean | Risk Level | Why Unresolved | Evidence Needed | Next Review Action | Decision Status |
|---|---|---|---|---|---|---|---|
| `03 Book of Becoming` | `02_stewardship/`, `12_archive_refs/`, possible future dedicated area | No lean | Medium | It may contain enduring stewardship practice, reflective institutional memory, or curated archive material. | Source page contents, authority status, whether entries are doctrine, practice, or reflections. | Review source page and classify by function. | Unresolved |
| `04 Archive of Becoming` | `12_archive_refs/`, possible future archive model, `03_governance/` for archive rules, `11_receipts/` for receipt artifacts | `12_archive_refs/` provisional lean; future archive model possible | High | Archive preserves raw institutional memory, including becoming events, revisions, failed ideas, abandoned paths, historical records, stewardship exercises, and contradictions; premature placement could still flatten memory, provenance, official records, and governance. | Linked admission/archive pages, official record rules, archive entry structure, custody/retrieval requirements. | Review linked archive/admission pages only if needed and explicitly authorized. | Explicitly unresolved |
| `05 Engine Registry` | `05_knowledge_systems/`, `04_registries/`, `09_agents/` only for executable agent-facing contracts | Split placement likely between `05_knowledge_systems/` and `04_registries/` | High | Engine Registry records engines, classes, statuses, validation basis, lock boundaries, and next actions; premature placement could still confuse conceptual doctrine, registry state, and execution contracts. | Representative engine pages, required registry fields, official statuses, automation boundaries. | Review representative engine pages only if needed and explicitly authorized. | Explicitly unresolved |
| `06 Card System` | `05_knowledge_systems/`, `04_registries/`, possible future dedicated area or specification model if approved | `05_knowledge_systems/` primary lean; split placement likely | High | Cards are user-facing knowledge objects and derived outputs of engine metabolization; premature placement could flatten conceptual, registry, stewardship, visual, and platform concerns. | Card taxonomy, archetypes, lifecycle rules, relationship grammar, implementation needs. | Review remaining Card System source content before migrating any card files. | Explicitly unresolved |
| `07 Foundational Lineages` | `05_knowledge_systems/`, `12_archive_refs/`, `01_constitution/` if authority-bearing | No lean | Medium | Lineages may be provenance, canon background, or interpretive knowledge structure. | Lineage page contents, authority role, whether lineages govern decisions. | Review source page and sample lineage records. | Unresolved |
| `08 Praxis Domains` | `05_knowledge_systems/`, `03_governance/`, possible future domain folder | No lean | Medium | Praxis may describe applications, operating contexts, or governance for implementation domains. | Domain examples, whether domains define practice or merely classify work. | Review source page and classify by use. | Unresolved |
| `09 Worlds and Case Studies` | `12_archive_refs/`, `05_knowledge_systems/`, possible future case-study area | No lean | Medium | Worlds/case studies may be provenance, applied examples, or active project families. | Page contents, status of Moon Joe/Valley High/visual canon projects, whether active or archival. | Review source page and identify active versus archival material. | Unresolved |
| `12 Community Charters` | `03_governance/`, `02_stewardship/`, `01_constitution/` if authority-bearing | No lean | Medium | Charters may be constitutional, governance templates, or stewardship practice. | Charter contents, intended authority, whether templates or ratified documents. | Review source page before placement. | Unresolved |
| Publishing Constitution | `07_publishing/publishing_constitution/` for full source cluster; derivative controls may reference `06_visual_language/`, `03_governance/`, `09_agents/`, `08_platform/`, `12_archive_refs/`, `11_receipts/`; `01_constitution/` only if later governance-admitted | `07_publishing/publishing_constitution/` primary provisional lean | High | Full eight-volume body is ratified publishing-department doctrine for visual knowledge production, but explicitly not an amendment to The Gradient Constitution unless later admitted and ratified through governance. | Binding index/source packet if any; decision whether to keep volumes together or extract derivative controls. | Decide extraction policy before migration. | Explicitly unresolved |
| Engine Registry dual-placement question | `05_knowledge_systems/` plus `04_registries/`, possibly `09_agents/` | Dual-placement likely | High | Engines may need conceptual source files, registry records, and executable automation contracts. | Engine data model, examples, automation boundaries, source-of-truth expectations. | Define rule for concept file versus registry row versus agent contract. | Unresolved |
| Archive model question | `12_archive_refs/`, possible future `archive/` model, `03_governance/` for archive rules | No lean | High | Archive is institutionally important and may not be reducible to references. | Archive purpose, official record rules, provenance requirements, preservation policy. | Review archive source and decide whether `12_archive_refs/` is sufficient. | Explicitly unresolved |
| Existing v0.1 placeholder folder rename/restructure question | Rename v0.1 folders to v0.2 structure, leave until approval, or bridge with README redirects | Leave until approval | Medium | Renaming too early may create churn before source placement decisions are resolved. | Human approval of v0.2 physical folder changes and migration timing. | Decide whether to restructure empty placeholders before source import. | Unresolved |

## Initial Decision Logic

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

## Required Treatment Of High-Risk Areas

### `04 Archive of Becoming`

Risk: High.

This remains explicitly unresolved. Premature placement could distort institutional architecture by reducing archive, memory, provenance, official records, and governance to a generic reference folder.

### `05 Engine Registry`

Risk: High.

This remains explicitly unresolved. Premature placement could distort institutional architecture by confusing conceptual engines, registry records, executable automation, and agent contracts.

### `06 Card System`

Risk: High.

This remains explicitly unresolved. Premature placement could distort institutional architecture because cards appear central to the knowledge model and may need more than a generic knowledge-systems destination.

### Publishing Constitution

Risk: High.

This remains explicitly unresolved. Premature placement could distort institutional architecture by misclassifying publishing rules as either downstream workflow or top-level institutional doctrine before source review.

## Review Notes

This register should remain a living migration-control document until the first source review pass is complete.

It does not authorize:

- folder restructuring
- file migration
- source promotion
- canon edits
- Notion writes
- Drive edits
- Supabase edits
- commits
