# Gradient Platform State Baseline

**Record ID:** TG-PLAT-BASELINE-001
**Authority:** TG-PLAT-SPRINT-001
**Status:** REVIEW REQUIRED
**Date:** 2026-07-11

## Repository Authority

The sole authoritative working repository is:

`noself-bardo/gradient-institution`

No secondary Gradient platform repository is authorized.

## Current Repository State

- Default branch: `main`
- Baseline commit: `baf3f5016f46d17bbb84efae0f47db989eadb1aa`
- Working tree at inventory: clean
- Repository visibility: public
- `08_platform/tg-web-001` is a static client-rendered archive reader
- No backend application exists in the repository
- No CI workflow exists in the repository

## Supabase State

The repository currently contains:

- no `supabase/` directory
- no migration directory
- no SQL migration files
- no Supabase configuration
- none of the six known migration identifiers

Known external migration identifiers:

1. `001_platform_foundation`
2. `002_production_layer`
3. `003_control_center`
4. `004_archive_event_layer`
5. `005_control_center_hardening`
6. `006_registry_rpc_api_safe`

The live Supabase implementation must be treated as external and unversioned relative to this repository until formally reconciled.

## Privacy Boundary

This public repository must not contain:

- therapy records
- mental-health testimony
- private family material
- raw voice recordings
- restricted transcripts
- credentials
- access tokens
- database passwords
- production database dumps
- Supabase service-role keys
- private archive sources

Only synthetic fixtures may be used during TG-PLAT-SPRINT-001.

## Current Freeze

Do not:

- modify the live Supabase schema
- create production migrations
- add credentials
- deploy services
- publish new applications
- import restricted sources
- authorize autonomous state changes

## Authorized Next Technical Work

1. Register this platform-control baseline.
2. Reconcile the live Supabase schema against recoverable migration history.
3. Design a synthetic-only packet contract.
4. Prepare an additive migration proposal.
5. Return the proposal to a human gate before database execution.
