# Gradient Cross-Platform Execution Packet

```yaml
registry_id: TG-TASK-###
authority: TG-PLAT-SPRINT-001
title: ""
objective: ""
non_goals: []
privacy_class: SYNTHETIC | PUBLIC | INTERNAL | RESTRICTED | SEALED
execution_platform: CURSOR | CODEX | ZO | LOCAL
branch_or_worktree: ""
inputs:
  files: []
  records: []
  urls: []
allowed_reads: []
allowed_writes:
  paths: []
  tables: []
  services: []
  endpoints: []
prohibited_actions: []
dependencies: []
acceptance_criteria: []
tests_required: []
rollback_procedure: ""
required_outputs:
  - implementation
  - tests
  - decision_log
  - execution_receipt
human_gate: NONE | REVIEW | PRIVACY | DESTRUCTIVE | RELEASE
```

## Receipt format

```yaml
task_id: TG-TASK-###
status: COMPLETE | PARTIAL | BLOCKED | FAILED
platform: ""
branch: ""
files_changed: []
database_changes: []
services_changed: []
tests_run: []
tests_passed: []
tests_failed: []
privacy_findings: []
unresolved_risks: []
recommended_next_state: ""
receipt_timestamp: ""
```
