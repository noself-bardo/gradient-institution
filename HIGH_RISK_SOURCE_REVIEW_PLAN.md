# The Gradient High-Risk Source Review Plan

Status: DRAFT / MIGRATION WORKSPACE ONLY

Authority: Not canonical

Constraint: This plan does not authorize migration, folder restructuring, source promotion, external edits, or commits.

## Review Targets

- `04 Archive of Becoming`
- `05 Engine Registry`
- `06 Card System`
- Publishing Constitution

## Review Questions For Each Target

### `04 Archive of Becoming`

What is this source area for?

- Pending.

Does it define doctrine, practice, registry state, knowledge model, publication workflow, archive/provenance, platform implementation, or agent behavior?

- Pending. Existing draft documents identify it as a high-risk archive/provenance area, but no source review has been performed.

What is its current authority?

- Pending.

What would break if it were placed in the wrong folder?

- It could flatten archive, memory, provenance, official records, and governance into a generic reference folder.

What evidence is needed before placement?

- Source page contents.
- Archive purpose.
- Whether it stores raw memory, official records, archive governance, or all three.
- Provenance and preservation requirements.

What candidate destination(s) remain viable?

- `12_archive_refs/`
- Possible future archive model.
- `03_governance/` for archive rules, if source review shows governance content.

Does it require split placement?

- Pending.

Does it require a future dedicated model?

- Pending; likely possible.

### `05 Engine Registry`

What is this source area for?

- Pending.

Does it define doctrine, practice, registry state, knowledge model, publication workflow, archive/provenance, platform implementation, or agent behavior?

- Pending. Existing draft documents suggest it may span knowledge model, registry state, and executable automation contracts.

What is its current authority?

- Pending.

What would break if it were placed in the wrong folder?

- It could confuse conceptual engines, registry records, executable automation, and agent contracts.

What evidence is needed before placement?

- Engine examples.
- Registry schema or records, if any.
- Whether engines are conceptual, executable, or both.
- Automation boundaries and source-of-truth expectations.

What candidate destination(s) remain viable?

- `05_knowledge_systems/`
- `04_registries/`
- `09_agents/` for executable agent-facing engines.

Does it require split placement?

- Pending; likely possible.

Does it require a future dedicated model?

- Pending.

### `06 Card System`

What is this source area for?

- Pending.

Does it define doctrine, practice, registry state, knowledge model, publication workflow, archive/provenance, platform implementation, or agent behavior?

- Pending. Existing draft documents identify cards as user-facing knowledge objects and claims/relationships as internal reasoning atoms.

What is its current authority?

- Pending.

What would break if it were placed in the wrong folder?

- It could distort the knowledge model by treating cards as simple content files, registry rows, or implementation specs before their institutional role is understood.

What evidence is needed before placement?

- Card specification.
- Claims and relationships model.
- Lifecycle rules.
- Implementation needs.
- Whether cards are canonical objects, interface objects, registry objects, or all three.

What candidate destination(s) remain viable?

- `05_knowledge_systems/`
- `04_registries/`
- Possible future dedicated area or specification model if approved.

Does it require split placement?

- Pending.

Does it require a future dedicated model?

- Pending; likely possible.

### Publishing Constitution

What is this source area for?

- Pending.

Does it define doctrine, practice, registry state, knowledge model, publication workflow, archive/provenance, platform implementation, or agent behavior?

- Pending. Existing draft documents say it may be publishing-operational law or institutional doctrine.

What is its current authority?

- Pending.

What would break if it were placed in the wrong folder?

- It could misclassify publishing rules as downstream workflow when they are constitutional doctrine, or misclassify workflow rules as top-level institutional doctrine.

What evidence is needed before placement?

- Actual eight-volume source.
- Status.
- Authority layer.
- Scope of governance.
- Relationship to broader constitution and publication workflow.

What candidate destination(s) remain viable?

- `07_publishing/publishing_constitution/`
- `01_constitution/` if institutional doctrine.

Does it require split placement?

- Pending.

Does it require a future dedicated model?

- Pending.

## Risk Criteria

Low: placement is descriptive and reversible.

Medium: placement may influence workflow, source discovery, or downstream interpretation.

High: placement may distort institutional architecture, canon authority, registry logic, or provenance.

## Review Output Template

```markdown
## Source Area

Name:

## Source Evidence Reviewed

- 

## Current Authority

Pending / Draft / Active / Locked / Canonical / Receipt / Archive / Unknown

## Functional Classification

Doctrine / Practice / Registry State / Knowledge Model / Publication Workflow / Archive-Provenance / Platform Implementation / Agent Behavior / Mixed

## Candidate Destination(s)

- 

## Split Placement Needed?

Yes / No / Pending

## Dedicated Model Needed?

Yes / No / Pending

## Placement Risk

Low / Medium / High

## Recommendation

Pending.

## Open Questions

- 

## Decision Status

Unresolved.
```

## First-Pass Recommendation

Do not resolve the four high-risk areas yet.

Recommended review order:

1. `06 Card System`
2. `05 Engine Registry`
3. `04 Archive of Becoming`
4. Publishing Constitution

Rationale:

Card System and Engine Registry likely determine the shape of knowledge systems and registries. Archive and Publishing Constitution are authority-sensitive and should be reviewed after those distinctions are clearer.

## Freeze Conditions

This plan does not authorize:

- migration
- folder restructuring
- source promotion
- external edits
- commits
- Notion writes
- Drive edits
- Supabase edits
- app/RPC work
- canon changes
