# CL_MIG_001 — Batch Scope Rule Set

**Batch ID:** CL-MIG-001  
**Mode:** PLAN / PREFLIGHT ONLY — no copy authorized  
**Repository posture:** repository candidate  

---

## 1. Inclusion rules

A file may be marked `ELIGIBLE_FOR_DRY_RUN` only if all are true:

1. Record is governance control text, registry text/JSON, or migration schema.
2. Extension is non-binary (`.md`, `.txt`, `.json`, `.csv`, `.yml`, `.yaml`) or explicit schema JSON.
3. Source file exists and is readable.
4. SHA-256 can be computed.
5. Proposed destination is a single concrete path under the proposed CL namespace.
6. Destination path does not currently exist as a file collision.
7. Path validation is `OK` or `PATH_LENGTH_WARN`.
8. Authority state is at least a documented candidate (not disputed quarantine-required without path).
9. MAP relationship assigns the file to `CL-MIG-001` intent (MAP-001 governance text or MIG001-SCHEMA).

Every eligible row still requires **separate human AUTHORIZE_COPY** before any mutation.

---

## 2. Exclusion rules

| Rule ID | Condition | Eligibility status |
|---|---|---|
| EX-BIN | PDF/PNG/ZIP/media/layout binaries | EXCLUDED_BINARY |
| EX-GDOC | `.gdoc` Drive stubs | EXCLUDED_AUTHORITY_UNRESOLVED |
| EX-EXT | MAP-002 external-reference-only inventory payloads | EXCLUDED_LIFECYCLE |
| EX-TOOL | Inventory `_*.py` / logs | EXCLUDED_NON_GOVERNANCE |
| EX-CHACHA | Chachipti files pending classify-then-copy | EXCLUDED_AUTHORITY_UNRESOLVED |
| EX-AUTH | Unresolved/disputed authority | EXCLUDED_AUTHORITY_UNRESOLVED |
| EX-COLL | Destination exists | EXCLUDED_COLLISION |
| EX-PATH | Invalid/unparseable/missing concrete destination | EXCLUDED_PATH_FAILURE |
| EX-MISS | Source missing | EXCLUDED_MISSING_SOURCE |
| EX-AUTHOR | AUTHOR_FROM_RATIFICATION without source file | BLOCKED |
| EX-PROD | Collection production trees / releases / proofs | EXCLUDED_NON_GOVERNANCE |
| EX-VI | Any CL-VI path creation | BLOCKED (prohibited) |

---

## 3. Counts from this preflight

| Metric | Count |
|---|---|
| total_files_considered | 54 |
| eligible_for_dry_run | 21 |
| excluded | 28 |
| blocked | 5 |

---

## 4. Explicit non-goals for CL-MIG-001

- No collection PNG/PDF/layout admission
- No CL-I…V / EV-001 / Death Bit tree copy
- No CL-VI directory
- No CL-VII promotion
- No frozen release mutation
- No destination folder creation in Phase 02B
- No Git commit / staging
