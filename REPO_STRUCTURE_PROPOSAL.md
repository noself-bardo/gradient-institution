# Repo Structure Proposal

Status: DRAFT v0.2 / MIGRATION WORKSPACE ONLY

This structure is approved only as a migration workspace, not as the final institutional architecture.

It creates places for the migration MVP without forcing The Gradient into a final repo ontology too early.

## Proposed Top-Level Layout

`00_command_center/`

Current operating state, next actions, active work, commitments, and review queues.

`01_constitution/`

Constitutional baseline, ratification history, locked architecture, and institutional doctrine once reviewed for migration.

`02_stewardship/`

Stewardship doctrine, human approval boundaries, care practices, validation responsibilities, and exercises that define institutional behavior.

`03_governance/`

Operating rules, policies, decision records, permissions, lifecycle rules, and non-canonical governance scaffolding.

`04_registries/`

Stable IDs, status vocabulary, relationship maps, event schemas, and registry manifests.

`05_knowledge_systems/`

Cards, claims, relationships, engines, knowledge objects, capability maps, and internal reasoning systems.

`06_visual_language/`

Visual canon, foundational atlas systems, visual specifications, object systems, prompt systems, and visual QC material.

GFVP source/spec/object/prompt/QC material belongs here:

- `06_visual_language/gfvp/`

`07_publishing/`

Publication rules, publishing constitution, series packaging, export manifests, and downstream release products.

GFVP released publication/export packages belong here:

- `07_publishing/series/gfvp/`

Publishing Constitution belongs here by default:

- `07_publishing/publishing_constitution/`

If source review shows the Publishing Constitution functions as institutional doctrine rather than publishing-operational law, it may instead belong under `01_constitution/`.

`08_platform/`

Application code, Supabase work, Control Center, schemas, migrations, dashboards, and registry backends after approval.

Control Center and Supabase work do not resume until inventories are reviewed.

`09_agents/`

Agent runbooks, permission boundaries, automation contracts, and operating loops.

Codex, Zo Computer, and agent contracts belong here after source review.

`10_inventories/`

Notion, Drive, local package, Supabase, and migration inventories.

`11_receipts/`

Review, approval, failure, completion, QC summary, handoff, and migration receipts that should be source-controlled.

`12_archive_refs/`

References to historical/provenance material that should remain outside the canonical working set unless promoted.

## Initial Migration Rule

Do not copy large Drive binaries, zips, images, or PDFs into this repo during the first pass.

Use references, paths, file names, statuses, and selective checksums for important release packages only after approval.

## First Package Families

The first migration pass covers:

- GFVP
- Publishing Constitution

GFVP is not treated only as a publication. It is primarily represented as a visual-canon / foundational-atlas system, with publication outputs downstream.

Control Center, Supabase RPC work, and dashboard implementation are deferred until the repo skeleton and migration manifest are approved.
