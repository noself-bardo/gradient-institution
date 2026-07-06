# The Gradient Receipt Template Draft

Status: DRAFT / MIGRATION WORKSPACE ONLY

Authority: Not canonical

Constraint: This template does not authorize migration, extraction, folder restructuring, source promotion, canon change, external edits, commits, or app/RPC work.

## Receipt ID Format

`TG-REC-[TYPE]-[###]`

Draft receipt types:

- `REV` = source review
- `APP` = approval
- `LOCK` = lock decision
- `MIG` = migration action
- `EXT` = extraction action
- `QC` = quality control
- `HAND` = handoff
- `GOV` = governance/ratification

Receipt IDs are provisional until migration approval.

## Standard Receipt Fields

```markdown
# [Receipt Title]

Receipt ID:

Receipt Type:

Title:

Date:

Actor / Steward:

Related Source ID(s):

Related File(s) / Page(s):

Action Taken:

Authority Basis:

Evidence Reviewed:

Decision / Outcome:

What Changed:

What Did Not Change:

What Is Authorized:

What Is Not Authorized:

Risk / Caveats:

Follow-Up Required:

Approval / Ratification Status:
```

## When Receipts Are Required

Receipts are required for:

- migration actions
- extraction actions
- source promotion
- lock decisions
- governance/ratification decisions
- derivative controls that change institutional behavior
- registry schema/status changes
- agent contract creation
- platform implementation requirements
- QC reviews that affect approval or lock status

## Where Receipts Live

- Receipts live in `11_receipts/`.
- During pre-migration draft phase, this template lives at repo root unless/until folder restructuring is approved.
- Receipts should cite source IDs from `SOURCE_ID_INDEX_DRAFT.md`.

## Anti-Patterns

- Do not use receipts to authorize work retroactively.
- Do not bury approval in prose without a receipt.
- Do not treat a source review as a lock decision.
- Do not treat migration as canon promotion.
- Do not create behavior-changing derivatives without receipts.
- Do not commit or migrate based on this draft template alone.

## Recommendation

Recommendation: adopt this receipt template as draft migration-control infrastructure before any extraction, migration, folder restructuring, source promotion, or commit.

## Output Summary

What changed:

- Created this draft receipt template.

What should be locked:

- Receipts are required for future behavior-changing migration-control actions.
- This template does not authorize any action by itself.

What remains living:

- Final receipt ID types.
- Final receipt storage structure.
- Whether source reviews should produce receipts retroactively.
- Whether receipt IDs should be assigned before or after approval.

Concrete next steps:

1. Review this receipt template draft.
2. If accepted, use it for future migration, extraction, review, approval, lock, handoff, QC, and governance receipts.
3. Do not migrate, extract, restructure, promote, commit, or resume app/RPC work until explicitly authorized.
