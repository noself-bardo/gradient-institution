# Gradient Institution

Status: DRAFT / MIGRATION MVP

This repository is the proposed Cursor/Git home for The Gradient. It is not yet the final institutional source of truth. During migration, Notion remains the navigational authority and Google Drive remains the package, asset, and export store.

## Current Purpose

The first goal is to make Gradient navigable without relying on chat memory or manual copy/paste loops.

This repo should initially hold:

- canonical Markdown candidates
- migration manifests
- source-of-truth policy drafts
- registry and status schemas
- app and automation code after approval
- agent runbooks and permission rules

This repo should not initially hold:

- approved image binaries
- package zips
- heavy exports
- secrets
- unreviewed canon rewrites

## First MVP Boundary

Build a canonical repository and registry dashboard that can show current institutional state.

Initial workflow:

1. Inventory Notion, Drive, local packages, and later Supabase.
2. Classify records by stable ID, source, destination, and status.
3. Draft a migration manifest.
4. Review and approve structure before moving or rewriting source material.
5. Only then automate registry updates or dashboard views.

## Current Freeze

Do not continue Control Center or RPC write-layer work until the repo skeleton, migration manifest, and inventories are reviewed.

Supabase context from earlier platform work is provisional until inventoried.

## Non-Negotiables

- Do not invent canon.
- Do not treat software as the institution.
- Do not overwrite approved outputs.
- Do not move Drive files without an approved manifest.
- Do not change Notion structure without approval.
- Do not change Supabase schema without approval.
- Do not commit secrets.
- Do not generate images or open image gates.
- Do not ratify doctrine or approve publications.
