# The Gradient Receipt ID Normalization Audit Draft

Status: DRAFT / RECEIPT ID AUDIT ONLY

Authority: Not canonical

Constraint: This audit does not authorize receipt edits, migration, extraction, source promotion, canon change, external edits, app/RPC work, commits, or additional folder restructuring.

## Audit Scope

Reviewed local draft-control receipt files:

- `RECEIPT_TEMPLATE_DRAFT.md`
- `HIGH_RISK_SOURCE_REVIEW_RECEIPT_DRAFT.md`
- `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md`

Purpose:

- Check receipt IDs and receipt types against `RECEIPT_TEMPLATE_DRAFT.md`.
- Assess whether a migration receipt type is appropriate for placeholder-only folder restructuring.
- Identify safe normalization updates for later approval.

## Template Baseline

`RECEIPT_TEMPLATE_DRAFT.md` defines receipt IDs as:

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

The template says receipt IDs are provisional until migration approval.

## Audit Findings

| Receipt file | Current receipt ID | Current receipt type | Expected receipt type under template | Issue, if any | Recommendation | Mechanical update safe | Human approval needed |
|---|---|---|---|---|---|---|---|
| `RECEIPT_TEMPLATE_DRAFT.md` | None; template field only | None; template field only | Not applicable | No issue. This file defines the format rather than instantiating a receipt. | No receipt ID/type update needed. | No | No |
| `HIGH_RISK_SOURCE_REVIEW_RECEIPT_DRAFT.md` | `TG-REC-REV-001` | `REV` | `REV` | No ID/type mismatch. The receipt records a source review phase and matches the template. | Keep as-is unless a later numbering policy changes all receipt IDs. | No | No |
| `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md` | `TG-REC-APP-001 (provisional)` | `Approval / folder restructuring control` | `APP` if the receipt records explicit approval; not `MIG` | Type is semantically aligned with approval, but not normalized to the template code. ID includes provisional prose outside the code. | Normalize later to `Receipt ID: \`TG-REC-APP-001\`` and `Receipt Type: \`APP\`` if the user approves. Keep the prose context in title/action/authority fields. | Yes, because it is a formatting/type-code normalization only | Yes, because it changes a receipt record before first commit |

## `TG-REC-MIG-001` Assessment

`TG-REC-MIG-001` is not appropriate for the v0.2 placeholder-only folder restructuring receipt.

Reason:

- The template defines `MIG` as a migration action.
- The approved restructuring explicitly did not migrate source files, extract source clusters, promote canon, or move source material.
- The receipt's authority basis is user approval for placeholder-only restructuring, so `APP` is the closer current template type.

If a future policy wants a distinct receipt type for restructuring, the current template does not define one. Until then, `APP` is preferable to `MIG` for this receipt.

## Recommended Normalization

Safe only after explicit approval:

```markdown
Receipt ID: `TG-REC-APP-001`

Receipt Type: `APP`
```

Apply only to:

- `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md`

Do not change:

- `HIGH_RISK_SOURCE_REVIEW_RECEIPT_DRAFT.md`
- `RECEIPT_TEMPLATE_DRAFT.md`
- historical old-path references inside the restructuring receipt
- source evidence, conclusions, authority basis, or authorization boundaries

## Applied Updates

Status: APPLIED / RECEIPT METADATA ONLY

Applied on: 2026-07-06

Approved scope:

- Normalize only `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md`.
- Change receipt metadata to `Receipt ID: \`TG-REC-APP-001\`` and `Receipt Type: \`APP\``.

Files updated:

- `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md`

Not changed:

- `HIGH_RISK_SOURCE_REVIEW_RECEIPT_DRAFT.md`
- `RECEIPT_TEMPLATE_DRAFT.md`
- Historical old-path references inside the restructuring receipt.
- Source evidence, conclusions, authority basis, authorization boundaries, canon, or external systems.
- Commits.

## Output Summary

What changed:

- Created this receipt ID/type normalization audit draft.
- Applied the approved metadata-only normalization to `11_receipts/V0_2_FOLDER_RESTRUCTURING_RECEIPT_DRAFT.md`.
- No template, source-review, inventory, manifest, canon, or external file was edited.

What should be locked:

- Placeholder-only folder restructuring should not be classified as `MIG`.
- `HIGH_RISK_SOURCE_REVIEW_RECEIPT_DRAFT.md` should remain `TG-REC-REV-001` / `REV`.
- No commit is authorized by this audit.

What remains living:

- Whether the receipt template should eventually define a dedicated restructuring/control receipt type.
- Whether receipt IDs remain provisional until a later migration-control policy is accepted.

Concrete next steps:

1. Review this audit.
2. Do not use `TG-REC-MIG-001` for placeholder-only folder restructuring unless the template is explicitly changed and approved.
3. Decide whether the receipt template should eventually define a dedicated restructuring/control receipt type.
4. Do not commit unless explicitly approved.
