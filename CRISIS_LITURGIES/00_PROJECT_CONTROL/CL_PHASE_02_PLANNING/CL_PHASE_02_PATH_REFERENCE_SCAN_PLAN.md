# CL-PHASE-02-OUT-008
## Path Reference Scan Plan

**Mode:** PLAN ONLY  
**Purpose:** Detect broken, ambiguous, or out-of-root path references before any migration copy batch.  
**Execution:** Deferred until a batch is human-authorized for dry-run. This document defines the scan; it does not run it against production trees as a mutating step.

---

# 1. Why this scan exists

Legacy Crisis Liturgies materials embed absolute Windows paths, Drive-relative paths, and cross-root links. NP-010 and L-006 require that active production not depend on undocumented external paths. A copy that preserves stale absolute references will look successful while being operationally false.

---

# 2. When to run

| Stage | Required |
|---|---|
| Phase 02 planning (this package) | Define plan only |
| Pre-copy dry-run for each `CL-MIG-###` | Mandatory |
| Post-copy verify | Mandatory for copied text/JSON/manifests |
| Global whole-corpus scan of all 5,173 files | Not required for MIG-001; optional later |

---

# 3. Roots in scope (read-only)

Scan sources listed in the batch manifest, plus:

1. `C:\Users\steve\Projects\gradient-institution\CRISIS_LITURGIES`
2. Batch-specific source paths from `CL_PHASE_02_SOURCE_TO_TARGET_MAP.csv`
3. Known siblings only when the batch includes them (e.g., CL-V tree)

Do not broaden into unrelated personal directories.

---

# 4. File classes to scan

Priority order:

1. `*.md`, `*.txt`, `*.json`, `*.csv`, `*.yml`, `*.yaml`
2. `*.py`, `*.ps1`, `*.sh`, `*.js`
3. Manifest / lock / handoff filenames matching `*MANIFEST*`, `*LOCK*`, `*HANDOFF*`, `*REGISTER*`, `*STATUS*`
4. Skip pure binaries (PDF/PNG/JPG/ZIP payloads) except companion sidecars

---

# 5. Patterns to detect

| Pattern family | Examples | Classification |
|---|---|---|
| Absolute Windows path | `C:\Users\steve\...` | `ABS_PATH` |
| Drive root literals | `My Drive\The Gradient`, `The Gradient\` | `DRIVE_ROOT_REF` |
| Repo-relative assuming old topology | `EXPANSION_VOLUMES\`, `CRISIS_LITURGIES_V_` | `LEGACY_TOPOLOGY_REF` |
| Sibling escape | paths leaving `CRISIS_LITURGIES` without registry | `OUT_OF_NAMESPACE` |
| URL-as-authority | raw http(s) used as state proof | `URL_STATE_CLAIM` (flag; Q-014) |
| Missing target after planned move | source path scheduled to relocate | `WILL_BREAK_ON_MOVE` |

---

# 6. Outputs (per dry-run)

Write under the batch control folder (future, not now):

```text
00_PROJECT_CONTROL/CL_MIG_XXX/
  PATH_REFERENCE_SCAN_RECEIPT.md
  PATH_REFERENCE_HITS.csv
  PATH_REFERENCE_BREAKAGE_RISK.json
```

`PATH_REFERENCE_HITS.csv` columns:

- `batch_id`
- `source_file`
- `line_no`
- `matched_text`
- `pattern_family`
- `referenced_path`
- `referenced_exists` (true/false/unknown)
- `planned_target_if_any`
- `risk` (`NONE` / `WARN` / `STOP`)
- `remediation` (`REWRITE_ON_COPY` / `EXTERNAL_REF` / `LEAVE` / `HUMAN`)

---

# 7. Risk rules

| Condition | Risk | Effect |
|---|---|---|
| Reference points outside canonical root and is required for builder/runtime | STOP | Block batch |
| Reference is historical prose only | WARN | Allow with note |
| Reference is Drive locator covered by `CL_EXTERNAL_BINARY_REFERENCE` | NONE/WARN | Prefer converting to external-ref ID |
| Reference would break if source retired | STOP | Block retirement; copy may proceed if source remains |
| URL used as sole publication proof | WARN | Do not promote to archive/publication state |

---

# 8. MIG-001 specific scan focus

For governance/registries batch, prioritize:

- Chachipti packet absolute paths
- Phase 00/01 documents pointing at Downloads or Drive control folders
- Schema `$id` / relative imports
- Any path that assumes `EXPANSION_VOLUMES` as the only EV home

MIG-001 should not require scanning all collection PNG trees.

---

# 9. Tooling posture

Preferred: read-only scripted scan (Python/PowerShell) emitting CSV/JSON.

Forbidden during scan:

- rewriting sources in place
- moving files
- deleting files
- running the builder
- committing

Rewrites, if ever authorized, occur only on **copied targets** listed in a migration manifest, never on frozen release binaries.

---

# 10. Pass criteria for a batch dry-run

1. Scan receipt exists.
2. Zero `STOP` hits remain unresolved.
3. Every `WARN` has an owner disposition.
4. External binary locators either validate or are marked `UNKNOWN` with recovery route.
5. Human signs dry-run acceptance before `mode: COPY`.
