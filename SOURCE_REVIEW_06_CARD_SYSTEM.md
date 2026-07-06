# Source Review - 06 Card System

Status: DRAFT / READ-ONLY REVIEW

Authority: Not canonical

Constraint: This review does not authorize migration, placement, restructuring, source promotion, or canon changes.

## Source Evidence Reviewed

No dedicated `06 Card System` source file was available in the local repo during the local-only review.

Approved read-only Notion source reviewed:

- `06 Card System` Notion page: `https://app.notion.com/p/391deacab3a581eeaabfcfbadd7b907f`

No adjacent Notion pages were fetched.

Reviewed local migration-control files:

- `FOLDER_DECISION_REGISTER.md`
- `HIGH_RISK_SOURCE_REVIEW_PLAN.md`
- `10_inventories/NOTION_INVENTORY.md`
- `REPO_STRUCTURE_PROPOSAL.md` via local search result

Reviewed local Drive source-adjacent GFVP files:

- `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01\00_README\README.md`
- `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01\11_OBJECT_SPECIFICATIONS\GFVP-OBJ-P005-CARD_v0-1.md`
- `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01\11_OBJECT_SPECIFICATIONS\GFVP-OBJ-P006-CLAIM_v0-1.md`
- `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01\11_OBJECT_SPECIFICATIONS\GFVP-OBJ-P007-RELATIONSHIP_v0-1.md`
- `C:\Users\steve\My Drive\The Gradient\gradient_foundational_visual_package_batch_01\11_OBJECT_SPECIFICATIONS\GFVP-OBJ-P008-EVIDENCE_v0-1.md`

Approved read-only linked Notion source reviewed:

- `Engine Metabolization Template`: `https://app.notion.com/p/391deacab3a58121a683e851aa244124`

Evidence limitation:

The `06 Card System` Notion page is currently a scaffold. It states the purpose as "the Card as the user-facing knowledge object" and lists contents to add, including Card Taxonomy v1.0, seven archetypes, Card principles, Card lifecycle, Relationship grammar, Card templates, First real Cards, and Engine Metabolization Template.

The `Engine Metabolization Template` page was reviewed after explicit authorization. It is a reusable template v0.1 for converting an existing engine, prompt package, workflow, or methodological system into a Gradient Card ecosystem without rewriting, flattening, or overclaiming it.

The `Fuckification Engine - Controlled Symbolic Mutation` adjacent page was not fetched.

The GFVP files are visual-canon/object-specification evidence about Card, Claim, Relationship, and Evidence objects. They are not a complete Card System source review by themselves.

## Functional Classification

Knowledge model:

- Strongly indicated.
- Local Notion inventory states that Cards are the user-facing knowledge object, Claims are internal reasoning atoms, and Relationships replace folders.
- The `06 Card System` Notion page directly states its purpose as "the Card as the user-facing knowledge object."
- The Notion page lists Card Taxonomy, seven archetypes, Card principles, Card lifecycle, Relationship grammar, Card templates, and First real Cards as contents to add.
- The Engine Metabolization Template defines a repeatable output ecosystem: one Structure Card, two to four Source Cards, three to six Claim Cards, one Frame Card, one Practice Card, one Reflection Card, and one Relationship Map.
- GFVP object specs describe Card, Claim, Relationship, and Evidence as distinct institutional objects with roles, boundaries, fields, and review traces.

Registry state:

- Indicated but not sufficient for placement.
- The object specs define fields such as source links, trust state, related claims, related relationships, confidence, scope, and review history. These are registry-readable concepts, but the specs repeatedly forbid reducing the objects to database schemas or rows.
- The `06 Card System` Notion page does not define registry fields, statuses, IDs, tables, or dashboard-readable state.
- The Engine Metabolization Template includes fields such as Type, State, Visibility, Recognition, Evidence, Supported By, Relationship, Operationalizes, Validation Result, and Relationship Map. These are registry-readable concepts, but the template does not define a registry schema.

Object/specification system:

- Strongly indicated through GFVP evidence; indicated as future/planned through Notion scaffold.
- The reviewed files are object specifications for Card, Claim, Relationship, and Evidence, each with purpose, constitutional role, boundaries, required fields, outputs, non-outputs, labels, compiler notes, and QC requirements.
- The Notion page names Card templates and Card lifecycle as planned contents, but does not yet provide the specification text.
- The Engine Metabolization Template provides concrete card templates for Structure, Source, Claim, Frame, Practice, and Reflection cards.

Source/evidence/claim structure:

- Strongly indicated.
- The Claim spec defines a claim as a bounded interpretive assertion.
- The Evidence spec defines evidence as a bounded support object.
- The Relationship spec defines typed institutional links between Cards, Claims, Sources, Evidence, Practices, and History.
- The Engine Metabolization Template makes provenance preservation explicit through Source Cards and requires claims to be supported by Source Cards.

Platform implementation dependency:

- Pending.
- The reviewed files include fields and link structures that future software may need, but they explicitly reject app dashboard, database schema, and UI-card metaphors as the conceptual form.
- The Notion page does not define platform implementation.
- The Engine Metabolization Template does not define platform implementation, but its repeatable fields and relationship map imply future structured implementation needs.

Stewardship/governance workflow:

- Strongly indicated as a workflow, though not as final governance authority.
- The object specs repeatedly distinguish Card/Claim/Relationship/Evidence from canon, validation, promotion, and final truth. This implies governance and stewardship boundaries, but does not fully define workflow authority.
- The Notion page lists Card lifecycle and Card principles as future contents, which may affect stewardship or governance, but the content is not present yet.
- The Engine Metabolization Template includes review questions and a locking rule: do not lock a metabolized engine after one pass unless the source artifact is mature, provenance is clear, claims are supported, risks are named, and a steward explicitly approves the result.

Other:

- Visual-canon dependency is strongly indicated because the reviewed evidence comes from GFVP object specifications and approved/locked plate workflow context.
- Cards appear to be derived outputs from engine metabolization, not raw source objects. Source Cards preserve provenance, but they are still Card objects created by the metabolization process.
- Cards also function as lifecycle objects: template states include Living, Reviewed, Locked, Capture, Constitutional, Deprecated, Private, Community, and Public.

## Placement Analysis

### `05_knowledge_systems/`

Why it fits:

- The evidence frames Cards, Claims, Relationships, and Evidence as a knowledge ecology.
- Cards are human-facing knowledge objects.
- Claims are internal reasoning atoms.
- Relationships replace folders.
- Evidence grounds interpretation without becoming proof or canon.
- The system appears conceptual and institutional before it is technical.
- The Engine Metabolization Template treats Cards as the core output form of metabolizing engines into a Gradient knowledge ecosystem.

Why it may fail:

- If the Card System has constitutional authority beyond knowledge modeling, `05_knowledge_systems/` may understate its institutional role.
- If the Card System is the central user-facing object model for the whole institution, it may eventually deserve a dedicated area rather than a sub-area.
- If Card lifecycle and locking rules become governance policy, some material may belong in `03_governance/` or `02_stewardship/` rather than only `05_knowledge_systems/`.

Evidence that would confirm it:

- Completed Card System source content defining cards, claims, relationships, and evidence primarily as knowledge objects.
- Lifecycle and use rules that are conceptual rather than database-first.

Evidence that would reject it:

- Source material showing Card System is primarily constitutional doctrine, a registry schema, or software implementation.

### `04_registries/`

Why it fits:

- Reviewed object specs include structured fields that could become registry records or schema attributes.
- Cards, Claims, Relationships, and Evidence all carry IDs, links, trust states, confidence, scope, and review history concepts.
- Relationships may need registry-readable typed links.
- The Engine Metabolization Template uses State, Visibility, Recognition, Supported By, Relationship, Operationalizes, Validation Result, and Relationship Map fields.

Why it may fail:

- The reviewed source explicitly says Card is not a database row, Claim is not a database schema, Relationship is not a database join table, and Evidence is not a database row.
- Treating Card System as primarily registry state could distort its institutional meaning.
- The Engine Metabolization Template presents a practice/template workflow, not a database design.

Evidence that would confirm it:

- A registry schema or dashboard requirement showing Cards, Claims, Relationships, and Evidence must be tracked as structured records.
- Status/event requirements for Card System objects.
- Completed Card Taxonomy, lifecycle, or template material that defines stable IDs, statuses, or registry-readable fields.

Evidence that would reject it:

- Source material insisting Card System remains conceptual, visual, or stewardship-facing only, with no structured state obligations.

### Possible future dedicated area or specification model if approved

Why it fits:

- Card System may be central enough to The Gradient to outgrow a single subfolder.
- The reviewed evidence suggests a coherent object model: Card, Claim, Relationship, Evidence, Source, History, Practice, and Review.
- The system may need separate conceptual, registry, visual, and implementation layers.
- The Engine Metabolization Template adds multiple card archetypes and a repeatable relationship map, suggesting a broader Card System model may be needed.

Why it may fail:

- Creating a dedicated model too early could inflate architecture before the source page is reviewed.
- It may duplicate `05_knowledge_systems/`, `04_registries/`, and `06_visual_language/`.

Evidence that would confirm it:

- Completed source content showing Card System is a primary institutional layer, not just one knowledge-system component.
- Multiple downstream dependencies across Visual Language, Registries, Platform, Stewardship, and Governance.

Evidence that would reject it:

- Source review showing Card System is a bounded subsection of Knowledge Systems.

## Split Placement Analysis

Split placement likely remains viable, but not finalized.

Possible split:

- Conceptual/card doctrine: `05_knowledge_systems/`
- Registry-readable IDs/status/link/state: `04_registries/`
- Visual object specs and GFVP plates: `06_visual_language/gfvp/`
- Receipts, QC, reviews, approval proof: `11_receipts/`
- Future platform implementation: `08_platform/`
- Stewardship workflow and locking/review practice: `02_stewardship/` or `03_governance/`, pending source review.

Reasons split placement may be needed:

- The reviewed evidence separates human-facing Card objects from internal Claim and Relationship structures.
- The specs distinguish institutional concepts from database schemas, UI, dashboards, validation, promotion, and canon.
- GFVP object specs are visual-canon artifacts, but the Card System itself appears broader than GFVP.
- The Engine Metabolization Template produces derived Card objects from source engines while preserving provenance and requiring steward approval before locking.

Reasons not to finalize split placement yet:

- The dedicated `06 Card System` page has been reviewed, but it is a scaffold rather than a complete source.
- Linked adjacent pages were not fetched.
- The current evidence comes partly through GFVP, which may emphasize visual-object representation rather than the full institutional model.

## Risk Assessment

Placement risk: High.

Reason:

Card System placement may distort institutional architecture, canon authority, registry logic, or provenance if reduced too early to a folder, database schema, UI pattern, or publication artifact.

Specific risks:

- Putting everything in `05_knowledge_systems/` may hide registry and implementation needs.
- Putting everything in `04_registries/` may reduce institutional knowledge objects to rows and links.
- Putting everything in `06_visual_language/` may confuse visual representation with the underlying system.
- Putting everything in `08_platform/` may incorrectly treat the Card System as software.

## Recommendation

Provisional lean, pending source review completion:

Treat `05_knowledge_systems/` as the primary conceptual destination for Card System material, with likely split placement for registry-readable structures, visual-canon object specs, receipts, stewardship/governance workflow, and future platform implementation.

Do not finalize placement from the current Notion evidence alone. The Card System page confirms the area as user-facing knowledge objects, and the Engine Metabolization Template confirms Cards as derived outputs of a repeatable stewardship workflow. However, the full Card Taxonomy, lifecycle, archetypes, and relationship grammar are not yet reviewed.

Next evidence needed is either completed Card System source content or explicit authorization to review linked supporting pages.

Do not migrate files yet.

## Open Questions

- Where is the completed source content for Card Taxonomy v1.0?
- Where are the seven archetypes, Card principles, Card lifecycle, Relationship grammar, Card templates, and First real Cards?
- Is the linked `Engine Metabolization Template` necessary to understand Card System placement?
- Is Card System an institutional layer, a knowledge model, a UI model, or all three?
- Are Cards canonical objects, interface objects, registry objects, or derived practice objects?
- Are Source Cards source objects, or derived provenance-preserving Card objects? Current evidence leans derived provenance-preserving Card objects.
- Which Card states are official lifecycle states versus template examples?
- What are the official relationships among Card, Claim, Relationship, Evidence, Source, Practice, and History?
- Does Card System define lifecycle states?
- Does Card System define approval, validation, or promotion rules, or only references them as external processes?
- What belongs in Git as source-controlled doctrine versus Supabase as structured state?
- Is a dedicated future `card_system/` model required?
- How should GFVP Card/Claim/Relationship/Evidence plates relate to the broader Card System?

## Output Summary

What changed:

- Created this read-only Card System source review draft.
- Appended approved read-only Notion evidence from the `06 Card System` page.
- Appended approved read-only Notion evidence from the linked `Engine Metabolization Template`.

What should be locked:

- No final placement decision.
- No migration.
- No folder restructuring.
- No source promotion.
- No canon changes.
- No external edits.

What remains living:

- Card System placement remains explicitly unresolved.
- Split placement remains likely but unapproved, now with stronger evidence for stewardship/governance workflow concerns.
- Dedicated model question remains open.

Concrete next steps:

1. Review this draft for whether the evidence separation is accurate.
2. Decide whether to authorize read-only review of any remaining Card System source content, if it exists, especially Card Taxonomy, lifecycle, archetypes, relationship grammar, and templates.
3. After fuller source review, update the Folder Decision Register with evidence-backed placement options.

## Placement Synthesis

### Provisional Functional Finding

Cards appear to be derived, user-facing knowledge objects produced through metabolization, not raw source objects.

### Primary Placement Lean

`05_knowledge_systems/` is the primary provisional lean for Card doctrine, taxonomy, archetypes, relationship grammar, templates, and conceptual model.

### Likely Split Placement

Likely supporting placements:

- `04_registries/` for card IDs, statuses, lifecycle/state fields, dashboard-readable registry data
- `02_stewardship/` for steward review, approval practice, and locking procedure
- `03_governance/` for policy-level lifecycle rules if they become institutional controls
- `11_receipts/` for approvals, QC, reviews, and lock receipts
- `08_platform/` only for later implementation, still frozen

### Dedicated Model Question

A future dedicated Card model may be needed, but should not be created until Card Taxonomy, archetypes, lifecycle, relationship grammar, templates, and first real Cards are reviewed.

### Recommendation

Recommendation: keep `06 Card System` unresolved, with `05_knowledge_systems/` as primary provisional lean and split placement likely pending further evidence.
