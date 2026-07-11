# ZO-01 — Gradient Staging Inventory Receipt

**Sprint:** TG-PLAT-SPRINT-001
**Task ID:** ZO-01
**Authority:** TG-PLAT-SPRINT-001 (read-only)
**Mode:** Inventory only — no installations, no deployments, no credential changes
**Report timestamp:** 2026-07-11

---

## 1. Environment inventory (host)

### 1.1 System identity

- OS: Debian GNU/Linux 12 (bookworm) x86_64
- Container: gVisor, 9p filesystem
- Init: not systemd (systemctl unavailable); managed via `register_user_service`
- Privilege: root
- Timezone: UTC (host); USER preference America/New_York

### 1.2 Tooling availability

- `git` — present (cloned `noself-bardo/gradient-institution`)
- `python` — 3.12 available
- `node` / `bun` — present (Space substrate)
- `docker` — not present
- `gh` — present (GitHub CLI), not yet authenticated
- `sha256sum` — present
- `git-filter-repo` — not present
- `trufflehog` / `gitleaks` — not present
- `supabase` CLI — not present

### 1.3 Persistent paths

- USER workspace: `/home/workspace`
- ZO internal: `/home/.z/`
- Conversation workspace: `/home/.z/workspaces/con_qALZG1pEChGVwBMf`
- Service logs: `/dev/shm/` (tmpfs)
- Secrets surface: [Settings > Advanced](/?t=settings&s=advanced)

### 1.4 Memory and disk

- The host has no provisioned Postgres or Supabase in this environment. The Gradient implementation runs as an external Supabase project whose state is not reflected in this host's filesystem.

---

## 2. Authoritative repository

- URL: `https://github.com/noself-bardo/gradient-institution`
- Default branch: `main`
- Baseline commit: `baf3f5016f46d17bbb84efae0f47db989eadb1aa`
- Author: noself-bardo
- Date: 2026-07-09T00:07:31-04:00
- Subject: `chore(tg-web-001): prepare companion PDFs for external public hosting`
- Visibility: public
- Working tree at inventory: clean
- Top-level content: 49 Markdown files plus `08_platform/tg-web-001/` (static client-rendered archive reader; 243 KB)
- The clone used for inspection lives at `/home/workspace/Projects/gradient-institution` (read-only mode for ZO-01)

### 2.1 No secondary repositories authorized

The instruction "Do not create another repository" was honored. No other Gradient platform repository was created or identified as authoritative. No alternative candidate was found in the workspace.

---

## 3. `08_platform` directory contents

```
08_platform/README.md
08_platform/tg-web-001/.nojekyll
08_platform/tg-web-001/CNAME
08_platform/tg-web-001/LICENSE
08_platform/tg-web-001/README.md
08_platform/tg-web-001/STYLE_GUIDE.md
08_platform/tg-web-001/TG_WEB_001_KICKOFF.md
08_platform/tg-web-001/VERSION
08_platform/tg-web-001/_redirects
08_platform/tg-web-001/assets/css/...
08_platform/tg-web-001/assets/img/...
08_platform/tg-web-001/assets/pdfs/...
08_platform/tg-web-001/data/rooms.json
08_platform/tg-web-001/index.html
08_platform/tg-web-001/netlify.toml
08_platform/tg-web-001/styles.css
```

- The only platform module is `tg-web-001` (static client-rendered archive reader). There is no `tg-platform-001` or other backend module.
- No `08_platform/tg-platform-001/` exists in the baseline.
- There are no tracked CI workflows (`.github/workflows/` absent).

---

## 4. Supabase / migration presence

- No `supabase/` directory anywhere in the repository.
- No migration directory (`migrations/`, `db/migrations/`, `supabase/migrations/`) present.
- No `.sql` / `.psql` files tracked.
- No Supabase configuration files (`supabase/config.toml`, `supabase/.temp`, etc.) tracked.

### 4.1 Six known migration identifiers

Searched all tracked files (excluding `.git/`) for these identifiers as text content:

| Identifier | Found |
|---|---|
| `001_platform_foundation` | not found |
| `002_production_layer` | not found |
| `003_control_center` | not found |
| `004_archive_event_layer` | not found |
| `005_control_center_hardening` | not found |
| `006_registry_rpc_api_safe` | not found |

**Conclusion:** The repository contains **no** migration history, no migration identifiers, and no Supabase configuration. The live Supabase project that powers the Gradient implementation is fully external and unversioned relative to this repository.

---

## 5. GitHub readiness appendix

- `gh` CLI is installed in this environment.
- `gh auth status` has not been verified. No GitHub authentication was performed during ZO-01.
- The remote `origin` of the clone is `https://github.com/noself-bardo/gradient-institution.git` and is reachable (`git ls-remote` succeeded implicitly during the `git clone`).
- No GitHub Actions workflows are tracked in the repository, so no CI surface to reconcile.
- No `CODEOWNERS` or branch protection information is visible without an authenticated GitHub call.
- No pull request, issue, or release artifacts exist in the clone.

**To proceed with any GitHub-mediated action (PR, status check, branch protection review), human authorization and `gh auth login` are required.**

---

## 6. Discovered repository candidates

| Candidate | Path / URL | Verdict |
|---|---|---|
| `noself-bardo/gradient-institution` | `https://github.com/noself-bardo/gradient-institution` (cloned to `/home/workspace/Projects/gradient-institution`) | **Authoritative** — designated by human |
| Any secondary Gradient platform repository | — | Not authorized. None found in workspace or in the conversation context. |

**Search performed:** `ls` of `/home/workspace/Projects`, `find` over the conversation workspace and the user workspace, plus the conversation manifest. No additional Gradient platform repository exists on this host.

---

## 7. Recommendation for authoritative repository

**Recommendation:** Keep `noself-bardo/gradient-institution` as the sole authoritative working repository. It is the only Gradient platform repository the user has authorized; it is the only one that exists in this environment; and the human instruction explicitly forbade creating a second one.

- All TG-PLAT-SPRINT-001 work products should land in this repository under `08_platform/tg-platform-001/` and `11_receipts/`.
- Any future "registry" or "production" repository must be proposed in writing and authorized by a human before creation.
- The live Supabase project remains external. Schema reconciliation is the highest-priority follow-up.

---

## 8. Recommended minimal staging directory

```
/home/workspace/Projects/gradient-institution/         # authoritative clone
  08_platform/tg-platform-001/                         # platform-control baseline (this sprint)
  11_receipts/                                          # task receipts
```

A separate staging copy is unnecessary during the inventory phase. A future `12_staging/` directory may host ephemeral synthetic fixtures once authorized.

---

## 9. Proposed reproducible bootstrap script outline

```bash
#!/usr/bin/env bash
set -euo pipefail
# Gradient platform-control bootstrap (NOT executed during ZO-01)
REPO_DIR="/home/workspace/Projects/gradient-institution"
[ -d "$REPO_DIR" ] || git clone https://github.com/noself-bardo/gradient-institution.git "$REPO_DIR"
cd "$REPO_DIR"
git fetch --all
git checkout main
git status --porcelain
# Future: install supabase CLI, configure env, prepare synthetic fixtures.
```

---

## 10. Actions requiring human authorization

Any of the following require explicit human authorization before execution:

1. Authenticating `gh` or any GitHub credential.
2. Pushing, creating a branch on the remote, or opening a pull request.
3. Connecting to the live Supabase project or running the `supabase` CLI.
4. Creating a new Gradient platform repository.
5. Adding credentials, tokens, or service-role keys to the workspace.
6. Modifying the live Supabase schema, applying migrations, or writing production data.
7. Publishing new applications, exposing services, or binding public ports.
8. Importing restricted sources (private transcripts, voice recordings, family material).

---

## 11. Known unknowns

- The live Supabase schema is unknown to this environment; reconciliation is the next material task.
- The provenance of the six known migration identifiers is not recorded in this repository.
- The contents of `08_platform/tg-web-001/data/rooms.json` were not deeply inspected; deferred to a later, narrower read.
- Branch protection and CODEOWNERS state for `noself-bardo/gradient-institution` are unknown without an authenticated GitHub call.

---

## 12. Machine-readable receipt

```yaml
receipt_id: ZO-01-INVENTORY-RECEIPT-001
sprint: TG-PLAT-SPRINT-001
task_id: ZO-01
mode: read-only-inventory
status: INVENTORY_COMPLETE
timestamp: 2026-07-11
authoritative_repository:
  url: https://github.com/noself-bardo/gradient-institution
  default_branch: main
  baseline_commit: baf3f5016f46d17bbb84efae0f47db989eadb1aa
  visibility: public
  working_tree: clean
clone_path: /home/workspace/Projects/gradient-institution
supabase_state:
  supabase_directory_present: false
  migration_directory_present: false
  sql_files_present: false
  config_present: false
  known_migration_identifiers_found: []
platform_modules:
  - id: tg-web-001
    path: 08_platform/tg-web-001
    kind: static_client_rendered_archive_reader
  - id: tg-platform-001
    path: 08_platform/tg-platform-001
    kind: not_present_in_baseline
github_readiness:
  gh_installed: true
  gh_authenticated: false
  workflows_tracked: 0
secondary_repositories_authorized: 0
actions_requiring_human_authorization:
  - gh_auth_login
  - push_or_pr
  - supabase_connect
  - create_gradient_repo
  - add_credentials
  - modify_live_schema
  - publish_or_expose_service
  - import_restricted_sources
known_unknowns:
  - live_supabase_schema
  - provenance_of_six_known_migration_identifiers
  - branch_protection_state
```
