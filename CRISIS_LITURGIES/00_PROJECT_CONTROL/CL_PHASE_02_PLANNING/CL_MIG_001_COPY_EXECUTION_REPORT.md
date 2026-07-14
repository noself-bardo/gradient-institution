# CL_MIG_001_COPY_EXECUTION_REPORT

**Date:** 2026-07-13T23:57:43Z  
**Batch:** CL-MIG-001 — GOVERNANCE_AND_REGISTRIES  
**Mode:** COPY (copy-only)

---

# 1. Gate 1 — authorization integrity

| Check | Result |
|---|---|
| attached files present | PASS |
| schema Draft 2020-12 | PASS |
| manifest validates | PASS |
| mode=COPY / copy_authorized=true | PASS |
| destructive auths false | PASS |
| planned 38 / deferred MIG-0039 | PASS |

Attached SHA-256:

- authorization: `c24734895282a1a4415f8a873bda116c637d7ea4aae59e42a21f6c40dbbd9bf2`
- manifest: `702ddbb456ee0d83eda6ab796c9586a7420810a09bb2fac9e5a053b8b01c18cc`
- schema: `c12385ab19f701a7e6d1623abfb77cc1178981e79ecd71b10e439b2d61a1cb85`

Human authorization record: `CL_MIG_001_COPY_ONLY_AUTHORIZATION_RECORD_v1.0.md`

# 2. Gate 2 — pre-copy

All 38 planned items: source exists/readable, bytes match, hash match, target absent.

# 3. Gate 3 — parents

Created directories: **13** (exact parents only). See `CL_MIG_001_CREATED_DIRECTORIES.csv`.

# 4. Gate 4 — copy + verify

| Metric | Value |
|---|---:|
| destinations created | 38 |
| ledger PASS | 38 |
| destination bytes matched | 38 |
| destination SHA-256 matched | 38 |
| overwrites | 0 |
| STOP exceptions | 0 |

# 5. Source retention

| Metric | Value |
|---|---:|
| sources retained unchanged | 38 / 38 |
| source deletions | 0 |
| source moves/renames | 0 |

# 6. Scope hygiene

- Chachipti / MIG-0039 copied: **0**
- unmanifested copies: **0**
- Git commits performed by this run: **0**
- source retirement: **not performed**

# 7. Verdict

```text
PASS — CL-MIG-001 COPY COMPLETE; 38/38 VERIFIED; SOURCES RETAINED
```
