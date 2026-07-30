# Systems Visualizer Branch Integration Recovery

**Date:** 2026-07-29
**Decision:** **RECOVERED LOCALLY; HOSTED TEST PENDING**

The original local infrastructure commit `2b48733` was removed by automated
workspace maintenance before it could be published. GitHub connectivity is now
restored. This record documents the exact recovery performed before retrying
publication.

## Recovered branch

- Repository: `noself-bardo/gradient-institution`
- Branch: `implementation/systems-visualizer-baseline-integration`
- Base: current remote `main` at `c08b9ce672bdf9484c2905f4e4bc6daf641f9931`

The branch contains only:

1. one catalog-derived migration for the nine historical `public` tables;
2. three migrations recovered verbatim from the production ledger;
3. one empty private Storage bucket declaration;
4. operational documentation; and
5. one fail-closed preflight.

## Recovery evidence

The three ledger-recorded migrations match the hashes preserved in the
2026-07-27 verification packet exactly:

| Migration | SHA-256 | Result |
|---|---|---|
| `20260701165821_001_gradient_platform_foundation_systems_visualizer.sql` | `68e719f5f43a370ea6f00942c696a20f718c05db34b2d7594882c9f0d1be7b8b` | PASS |
| `20260701165844_002_gradient_platform_foundation_hardening.sql` | `749c2482586a08f161c2c1462fb68497425c799b95743a79f63bbf1f5381c727` | PASS |
| `20260701165947_003_gradient_authenticated_read_policies.sql` | `2fe046413ff6296a5992854a0a45000103e2828ad94985610ccbb258b2032211` | PASS |

The pre-ledger migration was regenerated from the live catalog because the
original unpublished bytes did not survive workspace maintenance. It preserves
the previously verified structure: 9 RLS-enabled tables, 66 columns, 23
constraints, 11 constraint-backed indexes, no triggers, no policies, and the
existing table grants. Its recovered SHA-256 is
`6cb87f02bc78c9299d39a74be57e9a242af5e3776d0013b57672aada19c5f548`.

## Local replay

The four migrations replayed successfully from empty state in an isolated
PGlite `0.3.14` test database after creating only the three Supabase client-role
prerequisites (`anon`, `authenticated`, and `service_role`).

- `public` tables: **9**
- `gradient` tables: **15**
- Local fail-closed preflight: **PASS**
- Runtime tables detected: **0**

## Stop gates

- Private Crisis Liturgies pilot contract included: **no**
- Crisis Liturgies runtime tables included: **0**
- Production changes: **0**
- Production data or Storage objects copied: **0**
- Preview branch created: **0**

The next action is the already-authorized publication and one automatic
Supabase preview-branch verification. The preview must be deleted after evidence
is captured, and work must stop before runtime-table design.
