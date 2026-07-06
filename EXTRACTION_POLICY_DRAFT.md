# The Gradient Extraction Policy Draft

Status: DRAFT / MIGRATION WORKSPACE ONLY

Authority: Not canonical

Constraint: This policy does not authorize migration, extraction, folder restructuring, source promotion, canon changes, external edits, or commits.

## Problem Statement

Reviewed sources often function across multiple areas.

Examples:

- Publishing Constitution lives primarily in `07_publishing/publishing_constitution/` but references visual language, governance, agents, platform, archive, and receipts.
- Engine Registry splits between doctrine and registry state.
- Card System splits between knowledge model, registry state, stewardship/governance, and receipts.
- Archive of Becoming may be raw memory, provenance, custody, and future archive model.

The migration workspace needs a way to preserve source integrity while still allowing functional areas to use the parts of a source that govern them.

## Proposed Policy: Hybrid Source Preservation

- Keep source clusters whole in their primary home.
- Do not physically split ratified or source-cluster documents during initial migration.
- Create derivative controls, schemas, implementation notes, or operating procedures only when needed.
- Every derivative must cite its source cluster.
- Every derivative must have a receipt or review note in `11_receipts/` when it changes institutional behavior.
- Derivatives must not silently become canon.

## Placement Rules

Primary source home:

- The folder where the source cluster lives intact.
- The primary source home preserves original context, authority boundary, version, and scope.

Functional reference:

- A pointer from another folder to the source.
- A functional reference does not rewrite the source or become an independent authority.

Derivative control:

- A new extracted or rewritten document used for governance, registry, platform, agents, or production.
- A derivative control must cite the source cluster and state what it changes operationally.

Receipt:

- Proof of review, approval, lock, migration, or extraction.
- Receipts belong in `11_receipts/`.

## Folder-Specific Rules

`01_constitution/`

- Only admitted and ratified constitutional doctrine.

`03_governance/`

- Extracted policy/lifecycle controls only after review.

`04_registries/`

- Registry-readable fields/status/schema/state.

`05_knowledge_systems/`

- Doctrine, conceptual models, card/engine frameworks.

`06_visual_language/`

- Visual grammar, GFVP, prompt/object/QC systems.

`07_publishing/`

- Intact Publishing Constitution source cluster and publication workflow.

`08_platform/`

- Implementation notes only while app/RPC freeze remains active.

`09_agents/`

- Agent-facing contracts, runbooks, and automation boundaries only.

`11_receipts/`

- Extraction, approval, QC, review, lock, handoff, and migration proof.

`12_archive_refs/`

- Raw institutional memory, provenance, non-canon context, abandoned paths.

## Anti-Patterns

- Do not duplicate source clusters across folders.
- Do not split ratified sources into fragments without extraction receipts.
- Do not move doctrine into implementation folders.
- Do not turn archive references into canon by placement.
- Do not let platform needs define institutional architecture.
- Do not treat publishing doctrine as The Gradient Constitution without governance admission.

## Open Questions

- Should source clusters have stable IDs?
- Should derivative controls have a standard header?
- Should functional references be README links, index entries, or registry records?
- What receipt is required before extraction?
- When does extraction require human ratification?

## Draft Operating Mechanics

### Stable Source IDs

Every migrated source cluster should receive a stable source ID before migration.

Draft format:

`TG-SRC-[DOMAIN]-[###]`

Examples:

- `TG-SRC-PUB-001` for Publishing Constitution source cluster
- `TG-SRC-VIS-001` for GFVP source cluster
- `TG-SRC-REG-001` for Engine Registry source cluster
- `TG-SRC-ARC-001` for Archive of Becoming source cluster

IDs are provisional until migration approval.

### Derivative Control Header

Standard header for any derivative control:

- Title
- Status
- Derivative Type
- Source Cluster ID
- Source Path / Link
- Derived From
- Authority
- Changes Institutional Behavior: Yes/No
- Receipt Required: Yes/No
- Approved By
- Last Updated

Derivative controls must not silently become canon.

### Functional Reference Format

Lightweight functional reference entry:

- Reference Title
- Primary Source Home
- Source Cluster ID
- Functional Folder
- Why Referenced Here
- Do Not Duplicate Source: Yes

Functional references should point to intact source clusters rather than copying them.

### Receipt Requirement

A receipt is required when a derivative:

- changes institutional behavior
- extracts policy from a source cluster
- creates a registry schema or status vocabulary
- creates an agent contract
- creates a platform implementation requirement
- alters canon, governance, or lifecycle rules

Receipts should live in `11_receipts/`.

### Human Ratification Threshold

Human ratification is required when extraction:

- changes constitutional meaning
- changes governance rules
- changes lifecycle/status rules
- changes source authority
- promotes material to canon
- authorizes migration or folder restructuring
- resumes app/RPC/platform implementation

These mechanics are draft controls and do not authorize migration, extraction, restructuring, source promotion, canon change, external edits, commits, or app/RPC work.

## Recommendation

Recommendation: adopt hybrid source preservation as the draft migration policy: preserve source clusters intact in primary homes, create derivative controls only when needed, and require receipts for any extraction that changes institutional behavior.

## Output Summary

What changed:

- Created this draft extraction policy.

What should be locked:

- No migration is authorized by this policy.
- No extraction is authorized by this policy.
- No folder restructuring is authorized by this policy.
- Source clusters should remain intact during initial migration unless later approved.

What remains living:

- Stable ID rules for source clusters.
- Standard derivative-control headers.
- Functional reference format.
- Required receipt type before extraction.
- Threshold for human ratification.

Concrete next steps:

1. Review this policy draft.
2. If accepted, update the migration manifest to reference hybrid source preservation before any source migration.
3. Do not migrate, extract, restructure, or commit until explicitly authorized.
