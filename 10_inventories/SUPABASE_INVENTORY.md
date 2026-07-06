# Supabase Inventory

Status: DEFERRED / NOT YET INVENTORIED

Supabase is intentionally not treated as confirmed in this migration pass.

Earlier Control Center and Systems Visualizer context is provisional until directly inventoried.

## Current Rule

Do not edit:

- projects
- schemas
- tables
- RLS policies
- auth settings
- functions
- RPCs
- migrations
- data

## Intended Future Role

Supabase may become the structured institutional registry for:

- stable IDs
- statuses
- relationships
- status history
- events
- dashboard backing data

## Inventory Requirements Before Any Work

The Supabase inventory must establish:

- project name
- project ref
- schemas
- tables
- functions/RPCs
- auth providers
- RLS status
- policies
- migration history
- current write policy
- do-not-touch list

## Dependency

Begin Supabase inventory only after:

1. repo skeleton is reviewed
2. migration manifest draft is reviewed
3. first Notion and Drive source maps are understood
