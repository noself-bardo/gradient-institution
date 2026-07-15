# CL-PHASE-02 — Rollback Plan v0.2

**Date:** 2026-07-13T20:10:48Z  
**Default method:** DELETE_WRITTEN_TARGETS_ONLY  
**written_targets_ref:** manifest.`written_targets`

---

# 1. Doctrine

Copy → validate → register → (later) controlled retirement.  
Rollback removes only targets listed in the batch write receipt / `written_targets`.  
Sources never deleted. Frozen binaries never modified.  
Identical hashes are not deletion authority.

---

# 2. CL-MIG-001

- Planned written targets: 21
- Overwrite default: forbidden
- Fixture drill: **not executed** in Phase 02A (explicitly deferred)

---

# 3. Forbidden rollback actions

- Delete Drive archive trees
- Delete mirrors because hashes match
- Modify frozen PDFs/PNGs
- Create/destroy CL-VI
- Un-quarantine CL-VII
- Git reset/force as rollback tool without separate authorization
