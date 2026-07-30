# Systems Visualizer baseline

This directory contains the recovered, publishable infrastructure baseline for
the existing Systems Visualizer Supabase project.

## Scope

- `migrations/20260701165820_000_recovered_pre_ledger_public_schema.sql`
  reconstructs the nine historical `public` workflow tables from the live
  catalog without copying data.
- The three later migrations are verbatim recoveries from the production
  migration ledger.
- `config.toml` declares an empty, private `visual-systems-assets` bucket.
- `scripts/verify_baseline.py` fails closed if the migration chain, bucket
  declaration, or runtime-table stop gate changes.

The seven proposed Crisis Liturgies Raw Reality runtime tables are deliberately
absent. This baseline contains no database rows, Storage objects, credentials,
private pilot contract, seed data, or production mutation.

## Preview-branch verification

With the repository connected to Supabase Git integration and automatic
branching enabled, pushing this Git branch should:

1. create a data-less preview branch;
2. run all four migrations in filename order;
3. provision the declared empty private bucket; and
4. leave production unchanged.

Run the local preflight before publication:

```bash
python3 supabase/scripts/verify_baseline.py
```

After hosted verification, delete the preview branch. Do not merge this branch
or design runtime tables as part of this test.
