# Status Vocabulary Draft

Status: DRAFT / FOR REVIEW

This vocabulary is collected from the intake. It is not yet a database enum or final institutional policy.

## Candidate Statuses

- draft
- sandbox
- candidate
- text-ready
- text-locked
- image-gate-candidate
- image-gate-open
- generated-candidate
- QC-pass
- revision-required
- approved
- rejected
- archived
- superseded
- blocked
- canon
- non-canon

## Required Clarifications

- Whether `canon` and `non-canon` are statuses, classifications, or authority labels.
- Whether `QC-pass` should be normalized to lowercase, e.g. `qc-pass`.
- Whether `approved` differs from `visually-approved`, `text-approved`, or `publication-approved`.
- Whether `text-locked` and `approved` can coexist on the same object.
- Whether image gate states apply only to plates/images or also to packages.

## Stable ID Families Needed

- documents
- decisions
- receipts
- plates
- object specs
- prompts
- images
- packages
- publications
- engines
- capabilities
- sources
- failures
- reviews
- approvals
- status events

## Event Types To Define Later

- status changed
- source imported
- receipt created
- review requested
- review completed
- image gate opened
- image generated
- image approved
- revision requested
- object superseded
- package archived

Do not implement these in Supabase until the registry model is reviewed.
