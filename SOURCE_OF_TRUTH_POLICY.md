# Source Of Truth Policy

Status: DRAFT / FOR REVIEW

## Current Authority During Migration

Notion is the current navigational authority for The Gradient.

Google Drive stores packages, zips, images, exports, generated artifacts, and other binaries.

ChatGPT project history is founding provenance. It may explain why decisions were made, but it should not be used as the operating source of truth without being captured in Notion or Git.

Supabase is not yet the trusted institutional registry. It must be inventoried before any schema, data, auth, RLS, or RPC work continues.

Cursor/Git is the intended future home for source-controlled Markdown, schemas, app code, automation code, manifests, and agent runbooks.

## Target Direction

The migration should move operational clarity into this repo without pretending that every historical artifact is already clean, canonical, or current.

The repo should become the place where Cursor can answer:

- what exists
- where it came from
- what status it has
- what governs it
- what destination is proposed
- what still needs human approval

## Approval Boundaries

Safe without asking:

- read local repo files
- summarize documents
- draft manifests
- run non-destructive checks
- generate proposed Markdown drafts
- compare files
- identify missing receipts
- create review reports

Ask before doing:

- Notion writes
- Drive file creation or movement
- Supabase data writes
- local file edits to canonical docs
- package restructuring
- git commits
- schema migrations
- image generation
- image gate actions
- moving files into approved folders

Never without explicit approval:

- canon changes
- constitutional edits
- Supabase schema changes
- production deploys
- deleting files
- overwriting approved outputs
- committing secrets
- ratification
- final publication release
- changing this source-of-truth policy

## Storage Responsibilities

Git/Cursor stores:

- constitutional and governance Markdown after review
- publishing constitution material after review
- GFVP text substrate after review
- object specs, prompts, QC reports, schemas, app code, agent runbooks
- lightweight manifests and references to heavy assets

Drive stores:

- large images
- zipped packages
- PDFs
- binary exports
- release assets

Notion stores:

- human-readable summaries
- dashboards
- receipts
- review context
- status context during migration

Supabase should eventually store:

- structured registry state
- stable IDs
- status history
- relationships
- events
- dashboard backing data
