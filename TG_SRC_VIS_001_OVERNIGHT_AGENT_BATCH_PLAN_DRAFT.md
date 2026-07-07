# TG-SRC-VIS-001 Overnight Agent Batch Plan

Status: DRAFT / AGENT ORCHESTRATION ONLY

Authority: Not canonical

Prepared: 2026-07-06

Purpose: Line up phased agent work for `TG-SRC-VIS-001` migration control. Human is stepping away; agents may execute **draft/read-only phases** overnight. **Stop gates** require human return.

**Do not infer authorization** beyond what each phase explicitly allows.

---

## Where We Are (Snapshot)

### Completed (planning only — nothing imported)

| Phase | Gate | Key artifacts |
|---:|---|---|
| **0** | Baseline | Repo at `f8aad4f`; `MIGRATION_MANIFEST.md`, inventories |
| **1** | Source inventory + human ratification (planning index) | File inventory, authority/version/destination drafts, human review packet |
| **2** | Manifest accepted | `06_visual_language/gfvp/SOURCE_CLUSTER_MANIFEST.md` (R-M01/R-M02 applied) |
| **3** | Prerequisite ratification + exact import set | `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` (248 rows), ratification packet, import audit **PASS_WITH_NOTES** |
| **4** | Migration plan drafted | `TG_SRC_VIS_001_MIGRATION_PLAN_DRAFT.md` — **`READY_FOR_RECEIPT_DRAFT`** |

### Current position

```text
[YOU ARE HERE]
    │
    ▼
Phase 5 ── draft TG-REC-MIG-001 (overnight OK: draft only)
    │
    ▼
Phase 6 ── pre-import re-verification (overnight OK: read-only)
    │
    ▼
══ STOP ══ Human: approve receipt + authorize physical import
    │
    ▼
Phase 7 ── physical import (248 md/csv) — NOT overnight unless human returns and approves
    │
    ▼
Phase 8 ── post-import audit
    │
    ▼
══ STOP ══ Human: authorize commit
```

### Status fields (do not conflate)

| Field | Current value | Meaning |
|---|---|---|
| Migration plan | **`READY_FOR_RECEIPT_DRAFT`** | Plan ready; next = receipt **draft** |
| Migration plan readiness | **`READY_TO_DRAFT_MIGRATION_PLAN`** → plan exists | Plan drafted |
| Physical import candidacy | **`NEEDS_SOURCE_INVENTORY`** | No file copy until receipt + explicit import auth |
| `TG-SRC-PUB-002` | **Deferred** | No PNGs, zip, release import |
| Physical import | **Not authorized** | No copy, move, folder create |
| Commit | **Not authorized** | Separate approval |

---

## Global Agent Prohibitions (All Phases)

Unless a phase **explicitly** authorizes an action:

- No file copy from Drive into repo
- No folder creation under `06_visual_language/gfvp/` (except `SOURCE_CLUSTER_MANIFEST.md` already present)
- No migration, extraction, canon promotion
- No Notion, Drive, Supabase, app/RPC edits
- No commit
- No `TG-SRC-PUB-002` import

Agents may: inspect, classify, compare, draft planning docs, re-verify read-only.

---

## Overnight Batch (Recommended Run Order)

Run phases **5 → 6** in sequence. **Stop before Phase 7.**

| Batch | Phase | Agent task | Human required? | Output |
|---:|---|---|---|---|
| **A** | 5 | Draft migration receipt | No (draft only) | `11_receipts/TG_REC_MIG_001_DRAFT.md` or repo-root draft per convention |
| **B** | 5b | Receipt readiness review | No | `TG_SRC_VIS_001_MIGRATION_RECEIPT_READINESS_DRAFT.md` |
| **C** | 6 | Pre-import Drive re-verification | No | `TG_SRC_VIS_001_PREIMPORT_VERIFICATION_DRAFT.md` |
| **D** | 6b | Refresh import manifest audit | No | Update `TG_SRC_VIS_001_IMPORT_MANIFEST_AUDIT_DRAFT.md` if drift found |
| **E** | — | Morning packet synthesis | No | `TG_SRC_VIS_001_MORNING_REVIEW_PACKET_DRAFT.md` |

**Optional parallel (low priority, defer if timeboxed):**

| Batch | Track | Task | Output |
|---|---|---|---|
| **F** | PUB-002 | Read-only deferred binary/receipt index | `TG_SRC_PUB_002_INVENTORY_DRAFT.md` |
| **G** | Manifest | Apply R-M03–R-M10 only if human pre-authorized | Manifest edits (not pre-authorized tonight) |

---

## Phase Specifications

### Phase 5 — Migration Receipt Draft

**Status:** NEXT (overnight authorized: **draft only**)

**Agent prompt seed:**

```text
CURSOR MIGRATION CONTROL — DRAFT TG-REC-MIG-001 ONLY

Create: 11_receipts/TG_REC_MIG_001_GFVP_SOURCE_IMPORT_DRAFT.md (or repo-root if 11_receipts/ omit policy)

Use: TG_SRC_VIS_001_MIGRATION_PLAN_DRAFT.md §7, RECEIPT_TEMPLATE_DRAFT.md,
     TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md, TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md

Include: all standard MIG fields, approval wording (draft), evidence list, non-authorization boundaries,
         verification checklist reference, 248-file manifest citation, PUB-002 exclusion.

Status: DRAFT / RECEIPT ONLY — does not authorize import.
Do not copy files. Do not commit.
```

**Deliverable checklist:**

- [ ] Receipt ID `TG-REC-MIG-001`, type `MIG`
- [ ] Cites exact import manifest (248 rows)
- [ ] Cites ratified decisions (A1–F bundle)
- [ ] Explicit What Is / Is Not Authorized
- [ ] Signature block empty — awaiting human

---

### Phase 5b — Receipt Readiness Review

**Agent prompt seed:**

```text
Review TG-REC-MIG-001 draft against migration plan §7 and receipt template.
Recommend: READY_FOR_HUMAN_RECEIPT_SIGNOFF | NEEDS_RECEIPT_REVISION
Do not authorize import. Do not commit.
```

---

### Phase 6 — Pre-Import Verification (Read-Only)

**Agent prompt seed:**

```text
CURSOR MIGRATION CONTROL — PRE-IMPORT VERIFICATION (READ-ONLY)

Re-enumerate Drive: gradient_foundational_visual_package_batch_01
Compare to TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md (248 IMP rows)

Report: missing paths, new paths, count drift, PNG/PUB-002 accidental inclusion risk.
Create: TG_SRC_VIS_001_PREIMPORT_VERIFICATION_DRAFT.md

Do not copy files. Do not commit.
```

**Pass criteria for morning:**

- 248/248 source paths exist
- 0 unexpected files required for co-import
- Folder sums unchanged

---

### Phase 6b — Import Manifest Audit Refresh

If Phase 6 finds **no drift:** note "audit still PASS_WITH_NOTES" in morning packet.

If **drift:** update exact import manifest draft + re-audit (draft only; no copy).

---

### Phase 7 — Physical Import

**Status:** BLOCKED until human return

**Requires human approval of:**

1. `TG-REC-MIG-001` (signed/filed)
2. Explicit message: **AUTHORIZED — EXECUTE TG-SRC-VIS-001 PHYSICAL IMPORT**

**Agent prompt seed (only after dual approval):**

```text
Execute TG_SRC_VIS_001_MIGRATION_PLAN_DRAFT.md §6 steps 1-9 only.
Copy 248 md/csv per exact import manifest. Create lifecycle subfolders.
Verify §8 checklist. Stop before commit unless separately approved.
```

---

### Phase 8 — Post-Import Audit

**After Phase 7 only.**

Verify: 248 files, 0 PNGs, paths match IMP rows, working tree diff documented.

---

### Phase 9 — Commit

**BLOCKED** until human: **AUTHORIZED — COMMIT TG-SRC-VIS-001 IMPORT**

---

## Deferred Tracks (Not on Critical Path)

| Track | Status | When |
|---|---|---|
| `TG-SRC-PUB-002` | Deferred | After VIS-001 import + zip located |
| Notion GFVP mapping | Deferred | Separate authorized pass |
| P009 / `NTN-REC-002` | Deferred | Notion page review |
| App/RPC (`TG-PLATFORM-007`) | Paused | Out of scope |
| Manifest R-M03–R-M10 | Optional | Low priority |
| `FOLDER_DECISION_REGISTER.md` | Do not touch | Per prior instruction |

---

## Morning Review Packet (Phase E Output)

Agent should produce one page for human return:

1. **Overnight completed:** list files created/updated
2. **Recommendation:** receipt ready for sign-off? pre-import verification pass/fail?
3. **Stop gates:** what human must approve next (receipt sign → import auth → commit auth)
4. **Do not proceed without:** explicit phrases for Phase 7 and 9
5. **PUB-002 / deferred:** unchanged

---

## Artifact Index (Control Stack)

| Layer | File |
|---|---|
| Planning index | `06_visual_language/gfvp/SOURCE_CLUSTER_MANIFEST.md` |
| Import enumeration | `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` |
| Import audit | `TG_SRC_VIS_001_IMPORT_MANIFEST_AUDIT_DRAFT.md` |
| Ratification | `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md` |
| Migration plan | `TG_SRC_VIS_001_MIGRATION_PLAN_DRAFT.md` |
| Migration readiness | `TG_SRC_VIS_001_MIGRATION_PLAN_READINESS_DRAFT.md` |
| Receipt (next) | `TG-REC-MIG-001` draft |
| Candidate review | `FIRST_MIGRATION_CANDIDATE_REVIEW_TG_SRC_VIS_001.md` |

---

## Explicit Human Approval Phrases (Use Verbatim)

| Gate | Phrase |
|---|---|
| Receipt draft OK | `APPROVED — DRAFT TG-REC-MIG-001` |
| Receipt sign / import gate | `APPROVED — TG-REC-MIG-001 SIGNOFF` + `AUTHORIZED — EXECUTE TG-SRC-VIS-001 PHYSICAL IMPORT` |
| Commit | `AUTHORIZED — COMMIT TG-SRC-VIS-001 IMPORT` |

Without these, agents stop at Phase 6.

---

## Output Summary

**Tonight (agents):** Phases 5, 5b, 6, 6b, E — drafts and read-only verification only.

**Tomorrow (human):** Review morning packet → sign receipt → authorize import → then agents run Phase 7–8 → authorize commit for Phase 9.

**Still locked:** PUB-002 deferred; no canon; no external edits; no commit unless authorized.
