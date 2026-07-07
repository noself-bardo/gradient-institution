# TG-SRC-VIS-001 Source Cluster Manifest Design Review

Status: DRAFT / DESIGN REVIEW ONLY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Review Target: `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_DRAFT.md`

Ratification Reference: `TG_SRC_VIS_001_HUMAN_DECISION_SUMMARY_DRAFT.md` (2026-07-06)

Constraint: This review does not authorize migration, extraction, file movement, source promotion, canon change, external edits, commits, or app/RPC work.

**Revision note (2026-07-06):** `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_DRAFT.md` was revised per human approval to address R-01–R-07 identified below. Recommendation below reflects the **pre-revision** review; a separate re-check is required before changing to `READY_TO_DRAFT_MANIFEST`.

## Purpose

Assess whether the source-cluster manifest **design** is fit to guide drafting of `06_visual_language/gfvp/SOURCE_CLUSTER_MANIFEST.md` given the human ratification bundle. This review does not draft the manifest file.

---

## 1. Design Fit Check

Assessment of ratified planning decisions against the manifest design draft.

| Ratified Decision | Design Support | Fit | Notes |
|---|---|---|---|
| **A1** — Roadmap controls plate identity | Section 3 Tier 1; Section 9 plate coverage | **Good** | Roadmap named primary authority. Design text still says "pending human review packet A1–A4" — should cite A1 as **ratified**. |
| **A3** — 11 approved plates P001–P011 | Section 6 lock register; Section 9 plate matrix | **Partial** | Approved set implied but never states **11** explicitly. Section 9 says "update when human confirms counts" — count is now ratified. |
| **B1/B3** — P002/P003 composite lock (source inventory only) | Sections 5–6 composite notation | **Good** | Matches ratified scope: composite for source-system only; no binary/publication verification. Section 5 still says "after human lock decision (B1–B3)" — decision is recorded. |
| **A6** — P012 next image-gate candidate | — | **Missing** | No design section for next-gate / operational sequencing. AUTH-C11 handling absent. |
| **A2/D3/D4** — Historical manifest, count drift, legacy workflow | Sections 3 Tier H, 4 supersession, Section 2 legacy paths | **Partial** | Historical treatment well specified. Section 2 footnote still treats D3/D4 as conditional ("Include only if human review confirms") — **ratified as Yes**. |
| **A7** — Remediation vocabulary historical/secondary | Section 3 Tier 6 pack review sheets | **Misaligned** | Design lists pack sheets as pack text status authority (Tier 6) without A7's **secondary/historical** constraint or "does not override roadmap" rule. Pre-ratification swarm language implied elevation above roadmap; human rejected that. |

### Fit Summary

| Fit Level | Count | Decision IDs |
|---|---:|---|
| Good | 2 | A1, B1/B3 |
| Partial | 2 | A3, A2/D3/D4 |
| Missing | 1 | A6 |
| Misaligned | 1 | A7 |

The design skeleton supports most ratified decisions but requires targeted revision before manifest drafting to avoid encoding stale or superseded authority rules.

---

## 2. Required Manifest Sections

| Required Section | Present in Design? | Section(s) | Assessment |
|---|---|---|---|
| Source cluster ID | **Yes** | Header block (`source_id: TG-SRC-VIS-001`) | Adequate. |
| Source cluster scope | **Yes** | §1 Scope and Boundary; §2 Inventory Summary | Adequate. |
| Authority hierarchy | **Yes** | §3 Authority Hierarchy | Present; needs ratification status update and A7 secondary treatment. |
| File class taxonomy | **Partial** | §2 folder posture table only | No explicit taxonomy (package control, legacy, active workflow, production evidence, archive, deferred). Folder table implies classes but drafter lacks normative definitions. |
| Plate identity map | **Partial** | §9 Plate Coverage Matrix | Matrix covers workflow columns, not roadmap-derived plate ID → object name → family map. A1 ratification expects roadmap-anchored identity. |
| Version chain map | **Partial** | §5 Current Version Index | P003/P007 exemplars only; P002–P011 extension deferred to unratified C1–C2. Insufficient alone for full approved-plate manifest. |
| Lock / approval evidence map | **Yes** | §6 Lock Evidence Register | Adequate structure; must apply B1/B3 ratification to P002/P003 rows explicitly. |
| Deferred PUB-002 boundary | **Yes** | §1, §7, header `deferred_source_ids` | Strong. Correctly separates VIS-001 from PUB-002. |
| Excluded binaries / exports | **Yes** | §7 Do-Not-Import List | Adequate; correctly notes 25 PNGs present but import deferred. |
| Unresolved decisions | **Yes** | §11 Open Questions | Present; should cross-ref deferred ratification items and unratified packet IDs (A4, C*, D1/D2/D5–D8, E*, F*). |
| Receipt requirements | **Yes** | §8 Receipt Reference Strategy; §12 precondition 4 | Adequate. |
| Migration-readiness status | **Partial** | §12 Import Preconditions; header `migration_authorized: false` | Preconditions 1–3 partially satisfied by ratification but design still lists them as pending gates. No explicit `migration_readiness: NEEDS_SOURCE_INVENTORY` field. |

### Section Coverage Score

- **Fully covered:** 6 / 12
- **Partially covered:** 5 / 12
- **Missing as distinct section:** 1 (operational next-gate — required by A6)

---

## 3. Risks / Gaps

Gaps that would make actual manifest drafting **unsafe or misleading** without design revision.

| Risk ID | Gap | Severity | Manifest Drafting Risk |
|---|---|---|---|
| **R-01** | No **P012 next image-gate** section (A6 ratified) | **High** | Manifest omits ratified operational planning fact; stale Pack A gate line may persist uncorrected. |
| **R-02** | **A7 misalignment** — pack remediation not marked historical/secondary | **High** | Manifest could treat pack review sheets as overriding roadmap for Pack B–F text status — contradicts human ratification. |
| **R-03** | Section 2 **D3/D4 conditional footnote** stale post-ratification | **Medium** | Drafter may leave legacy folders as "Maybe" instead of confirmed historical include set. |
| **R-04** | Section 3 authority table still labeled **"pending human review"** | **Medium** | Ratified A1/A3/A7 not distinguished from open A4; authority section reads as provisional when partially locked. |
| **R-05** | **Plate identity map** absent as roadmap-derived table | **Medium** | A1 ratification not operationalized; plate names/families may be inferred from wrong legacy sources. |
| **R-06** | **Approved count (11)** not a required manifest field | **Medium** | Stale "10" references could survive in manifest without explicit supersession pointer. |
| **R-07** | Version index **P002–P011 incomplete** (C1–C2 unratified) | **Medium** | Safe to draft P003/P007 rows; unsafe to draft full approved-plate version map without defaults or explicit deferral. |
| **R-08** | Conflict table range **AUTH-C1–C10 only** | **Low** | AUTH-C11–C16 (count drift, next gate, remediation) not in design conflict register. |
| **R-09** | **File class taxonomy** not normative | **Low** | Inconsistent class labels across manifest sections during drafting. |
| **R-10** | Import preconditions **1–3** not updated for partial ratification | **Low** | Manifest may over-state open gates already resolved by 2026-07-06 bundle. |

**Safe to draft now (with revision guidance):** header, scope, PUB-002 boundary, do-not-import list, P002/P003 composite lock rows, historical supersession narrative, receipt strategy skeleton.

**Unsafe without revision:** operational next-gate field, pack B–F authority treatment, include/exclude Yes/Maybe footnotes, full plate identity map, complete approved-plate version index.

---

## 4. Recommendation

### **`NEEDS_DESIGN_REVISION`**

The manifest design is structurally sound and covers most required sections, but it is **not yet safe to draft** `SOURCE_CLUSTER_MANIFEST.md` without revising the design draft to:

1. Add a **Production Status / Next Gate** section recording P012 (A6) and marking stale Pack A gate line as historical.
2. Revise Section 3 Tier 6 and related text to reflect **A7 historical/secondary** — remediation vocabulary informative only; roadmap retains plate identity authority.
3. Update Section 2 import table: D3/D4 legacy folders and batch manifest → **Yes** (ratified); remove conditional footnote.
4. Add explicit manifest fields: **`approved_plate_count: 11`**, **`approved_plates: P001–P011`**, **`migration_readiness: NEEDS_SOURCE_INVENTORY`**.
5. Add **Plate Identity Map** subsection (roadmap-derived P001–P040 ID, object name, family) with legacy semantic drift notes.
6. Mark ratified authority decisions in Section 3 and Section 12 preconditions (partial satisfaction).
7. Extend conflict register to **AUTH-C11–C16** or reference authority hierarchy draft.

**Not BLOCKED:** Ratified decisions can be expressed; gaps are design-doc updates, not fundamental conflicts.

**Not READY_TO_DRAFT_MANIFEST:** Drafting now would likely encode pre-ratification defaults (A7 elevation, missing A6, conditional D3/D4).

---

## 5. Design Review Checklist (against target draft)

| Check | Result |
|---|---|
| Section outline covers candidate-review gaps | **Partial** — missing next-gate |
| PUB-002 boundary explicit | **Pass** |
| Version chains without file renaming | **Pass** |
| Ratified A1/A3/B1/B3/A6/A2/D3/D4/A7 reflected | **Fail** — A6 missing; A7 misaligned; A3/D3/D4 partial |
| Receipt reference strategy acceptable | **Pass** |
| Import preconditions sufficient | **Partial** — need ratification state update |
| Design approval ≠ migration authorization | **Pass** |

---

## Output Summary

### What changed

- Created this design review assessing `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_DRAFT.md` against the 2026-07-06 human ratification bundle.
- Identified fit levels, required-section coverage, and drafting risks R-01 through R-10.
- Recommended **`NEEDS_DESIGN_REVISION`** before manifest content drafting.

### What should be locked

- This review is planning-only and not canonical.
- Ratified human decisions (A1, A3, B1/B3, A6, A2/D3/D4, A7) remain the authority for what the manifest must eventually express.
- Candidate recommendation remains **`NEEDS_SOURCE_INVENTORY`**.
- **`TG-SRC-PUB-002`** remains deferred.
- No migration, extraction, file movement, manifest file creation, external edits, app/RPC work, or commit authorized.

### What remains living

- Revision of `TG_SRC_VIS_001_SOURCE_CLUSTER_MANIFEST_DESIGN_DRAFT.md` to address R-01–R-07 (recommended before drafting).
- Unratified packet decisions: A4, C1–C4, D1/D2/D5–D8, E1–E3, F1/F2/F4.
- Deferred: Notion GFVP mapping, `NTN-REC-002`, export zip, PUB-002 release import.
- Actual `SOURCE_CLUSTER_MANIFEST.md` drafting — **not authorized in this task**.

### Concrete next steps

1. Revise manifest **design draft** to address R-01–R-07 (especially A6 next-gate section and A7 secondary treatment).
2. Re-run this design review or human spot-check after revision.
3. If design revision accepted, authorize manifest **content drafting** as repo proposal only — still no import.
4. Do not populate `06_visual_language/gfvp/`, move files, edit external systems, or commit until explicitly authorized.
