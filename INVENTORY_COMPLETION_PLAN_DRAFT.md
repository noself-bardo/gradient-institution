# The Gradient Inventory Completion Plan Draft

Status: DRAFT / PLANNING ONLY

Authority: Not canonical

Baseline Commit: `f8aad4f2396cd92be7f53fa220c07797403f3dd4`

Last Refreshed: 2026-07-07 (post-`ca6410e` VIS-001 import; post-`d36444a` folder register housekeeping)

Constraint: This plan does not authorize migration, extraction, source promotion, canon change, folder restructuring, external edits, commits, or app/RPC work.

## Purpose

Complete source inventories before selecting migration candidates — and maintain inventory gates for clusters not yet imported.

**`TG-SRC-VIS-001` source inventory and physical import are complete** (committed `ca6410e` under receipt `TG-REC-MIG-001`). This plan now defines the **next** inventory gates for remaining clusters under the hybrid source-preservation policy. It does not move files, copy source material, create derivative controls, update external systems, or change canonical status.

## Inventory Principles

- Inventory before import.
- Source clusters remain intact until explicitly approved for migration.
- Source inventories should identify locations, status, authority, completeness, and known gaps.
- Release/export packages should be inventoried separately from source systems.
- Binary assets, zips, PDFs, images, and generated packages remain outside Git unless explicitly approved.
- External systems may be inspected only after explicit approval for that inventory pass.
- Implementation/platform inventories do not authorize app/RPC/platform work.

## Current Inventory Baseline

| Inventory Area | Current File | Current Status | Known Coverage | Main Gaps |
|---|---|---|---|---|
| Drive | `10_inventories/DRIVE_INVENTORY.md` | DRAFT / AGENT-ASSISTED GFVP RECONCILIATION PASS | GFVP batch root observed; source/spec/object/prompt/QC folders classified; receipt/QC/review folders classified; generated/approved output receipt folders identified; duplicate/mirror risks recorded; receipt-to-binary and authority reconciliation summarized | Approved/generated PNG binaries missing from accessible local sync; GFVP zip/export package not found; P009 Notion receipt ambiguity; manifest/roadmap authority conflict |
| Notion | `10_inventories/NOTION_INVENTORY.md` | DRAFT / READ-ONLY METADATA PASS | Root page, top-level skeleton, active commitments, top-level page URLs, Publishing Constitution pages, Visual Canon/GFVP pages, platform/control references, Codex/automation references, GFVP receipt/QC examples | Full source-location audits for individual clusters, GFVP Notion-to-Drive receipt mapping, possible databases |
| Local Packages | `10_inventories/LOCAL_PACKAGES_INVENTORY.md` | DRAFT / AGENT-ASSISTED READ-ONLY PASS | Repo now mirrors **248** GFVP source-system md/csv under `06_visual_language/gfvp/` (`ca6410e`); sibling Control Center app out-of-scope; Downloads checked for GFVP binaries/zip with only markdown residue found | Generated image folders, export zip, and Codex/ChatGPT exports outside accessible local paths still unresolved — **`TG-SRC-PUB-002`** |
| Supabase | `10_inventories/SUPABASE_INVENTORY.md` | DEFERRED / NOT YET INVENTORIED | Do-not-touch rule and future inventory requirements documented | Project identity, schemas, tables, functions/RPCs, auth, RLS, policies, migration history, write policy |

## Source Cluster Inventory Requirements

| Source ID | Source Cluster | Required Inventory Completion | External Inspection Needed? | Completion Gate |
|---|---|---|---|---|
| `TG-SRC-PUB-001` | Publishing Constitution eight-volume source cluster | Confirm exact Notion pages, page IDs, source completeness, ratification/status claims, and whether Drive/source exports exist | Notion yes; Drive maybe | Complete source page list and authority/status map before migration-candidate review |
| `TG-SRC-VIS-001` | GFVP source/spec/object/prompt/QC system | ~~Confirm complete Drive folder map…~~ **Complete** — 248 md/csv imported; post-import audit PASS | Drive yes (done); Notion maybe | **Complete** — imported `ca6410e` under `TG-REC-MIG-001`; PUB-002 excluded |
| `TG-SRC-PUB-002` | GFVP release/export packages | Identify release/export folders, approved image binaries, zips/PDFs/images, package manifests, and release status evidence | Drive yes | Release/export package inventory separated from source-system inventory |
| `TG-SRC-KNO-001` | Card System | Confirm Notion source pages, linked Engine Metabolization Template, related GFVP Card/Claim/Relationship/Evidence specs, and status boundaries | Notion yes; Drive maybe | Complete source list and split-reference candidates before derivative controls |
| `TG-SRC-REG-001` | Engine Registry | Confirm Notion source pages, registry schema/status concepts, related GFVP Engine/Registry/Practice Framework specs, and executable/agent-facing boundaries | Notion yes; Drive maybe | Complete source list before registry import or derivative schema work |
| `TG-SRC-ARC-001` | Archive of Becoming | Confirm Notion source pages, linked admission/archive pages, GFVP Archive/Book/History/Source specs, and archive/reference boundaries | Notion yes; Drive maybe | Complete source list before archive placement or reference model decision |

## Proposed Inventory Passes

### Pass 1: Notion Source Location Completion

Goal:

- Confirm exact source pages and authority/status boundaries for Notion-heavy clusters.

Targets:

- Publishing Constitution pages and all eight volumes.
- Card System.
- Engine Registry.
- Archive of Becoming.
- GFVP receipts/approvals if represented in Notion.

Output:

- Updated Notion inventory draft or a dedicated Notion source-location audit after explicit approval.

### Pass 2: Drive Source Package Completion

Goal:

- Complete **remaining** GFVP release/export package boundaries and non-VIS-001 cluster Drive packages.

Targets:

- ~~GFVP source/spec/object/prompt/QC folders.~~ **VIS-001 complete** — source system in repo at `06_visual_language/gfvp/`.
- Approved image locations (`06_`/`08_` PNGs).
- Text-lock and visual approval receipts (deferred PUB-002 metadata).
- Release/export packages, zips, PDFs, images, and package manifests.

Output:

- Updated Drive inventory draft or dedicated PUB-002 package audit after explicit approval.

### Pass 3: Local Package Sweep

Goal:

- Identify any local extracted packages or generated outputs outside the synced Drive root.

Targets:

- Downloads, local project folders, Codex/ChatGPT export bundles, generated image folders, and local GFVP zips only if explicitly approved for inspection.

Output:

- Updated local packages inventory or local package audit after explicit approval.

### Pass 4: Supabase Read-Only Inventory

Goal:

- Inventory Supabase only after source maps are stable enough to understand registry/platform relevance.

Targets:

- Project name/ref, schemas, tables, functions/RPCs, auth providers, RLS status, policies, migration history, current write policy, and do-not-touch list.

Output:

- Updated Supabase inventory after explicit approval.

## Required Inventory Fields

For each source cluster or package, record:

- Source ID.
- Source cluster name.
- System of record.
- Exact location or URL/path.
- Source type.
- Authority/status.
- Completeness.
- Related receipts or approvals.
- Related release/export packages.
- Proposed primary destination.
- Functional reference destinations.
- Known gaps.
- Do-not-move rule.
- Receipt requirement before import or derivative control.

## Open Questions

- Which source clusters have complete source locations? **`TG-SRC-VIS-001` complete; `TG-SRC-PUB-002` binaries/zip open; others pending.**
- Which source clusters are still Notion-only? PUB-001, KNO-001, REG-001, ARC-001 — pending Pass 1.
- Which Drive packages correspond to release/export packages?
- Which GFVP assets are approved outputs versus source/control files?
- Which source clusters require source IDs before migration?
- Which candidate imports require receipts?
- Which candidate derivatives require human ratification?
- When should Supabase move from deferred inventory to read-only inventory?

## Agent-Assisted GFVP Findings

Agent-assisted read-only inventory revealed these blockers:

- Approved/generated GFVP PNG binaries are documented by receipts but were not found in the synced local Drive package.
- `gradient_foundational_visual_package_batch_01.zip` or equivalent export package was referenced but not found under accessible Drive/Projects paths.
- Notion-to-Drive GFVP receipt/QC mapping remains incomplete.
- `01_SOURCES/BATCH_01_MANIFEST.md` appears stale relative to `13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.md`.
- P002/P003 approval/lock evidence may rely on roadmap/handoff/approval receipts rather than standalone object lock receipts.
- P003/P007 version chains need current-version mapping.

Follow-up receipt-to-binary and authority reconciliation clarified:

- Local accessible paths, including Drive sync, Projects, Downloads, and the migration repo, do not contain the approved/generated PNG binaries or package zip.
- `NTN-REC-001` maps to P003 approval and `NTN-REC-003` maps to P006 output QC.
- `NTN-REC-002` for P009 remains ambiguous without deeper Notion page review.
- P003 current chain is object spec v0-2 -> compiler v0-4 -> output QC v0-4 -> approved output v0-4.
- P007 current chain is object spec v0-1 -> compiler v0-2 -> output QC v0-2 -> approved output v0-2.

## Post-Import Baseline Update (2026-07-07)

After physical import and commit of `TG-SRC-VIS-001`:

| Item | Status |
|---|---|
| Source inventory | **Complete** — 283 md/csv in Drive package; 248 co-import candidate imported |
| Exact import manifest | **Executed** — `TG_SRC_VIS_001_EXACT_IMPORT_MANIFEST_DRAFT.md` (IMP-001–248) |
| Migration receipt | **Executed** — `TG-REC-MIG-001`; filed `11_receipts/TG_REC_MIG_001_VIS_001_IMPORT_RECEIPT_DRAFT.md` |
| Repo commit | **`ca6410e`** — 248 md/csv + migration control stack |
| Post-import audit | **PASS** — `TG_SRC_VIS_001_POST_IMPORT_AUDIT_DRAFT.md` |
| Folder register | Updated **`d36444a`** — VIS-001 recorded in `FOLDER_DECISION_REGISTER.md` |
| **`TG-SRC-PUB-002`** | **Deferred** — 25 PNGs on Drive; 21 deferred receipt md; zip unlocated |
| Canon promotion | **No** — draft migration workspace only |

## Recommended Next Gate

**VIS-001 complete.** Choose the next **read-only inventory** track (no import without receipt gate):

### Option A — `TG-SRC-PUB-002` (recommended if unblocking release track)

- Read-only inventory of 25 PNGs, deferred receipt md in `06_`/`08_`, zip/export package search.
- Output: PUB-002 exact import manifest draft (planning only).
- Rationale: Binaries and zip gaps remain the primary open GFVP blockers.

### Option B — `TG-SRC-PUB-001` Publishing Constitution

- Notion source-location completion for eight-volume cluster.
- Output: PUB-001 file/page inventory and migration-candidate review draft.
- Rationale: Natural next source-cluster candidate; partially reviewed already.

Do not import without receipt gate. Do not create derivative controls yet. Do not resume app/RPC work.

## Output Summary

What changed:

- Created this inventory completion plan draft.
- Identified inventory gaps across Drive, Notion, local packages, and Supabase.
- Proposed read-only inventory passes before migration-candidate selection.
- Updated gates after Notion metadata pass, GFVP Drive findings, and receipt-to-binary reconciliation.
- **2026-07-07 refresh:** Marked `TG-SRC-VIS-001` inventory/import **complete** (`ca6410e`, `TG-REC-MIG-001`); removed stale pre-import gates; repointed next gates to PUB-002 and/or PUB-001 inventory.

What should be locked:

- Inventory planning does not authorize migration, extraction, canon promotion, external edits, commits, or app/RPC work.
- `TG-SRC-VIS-001` import record: 248 md/csv at `ca6410e`; PUB-002 excluded.
- Drive source clusters remain intact; release/export packages remain separate from source systems.
- `TG-SRC-PUB-002` deferred until separately authorized.

What remains living:

- Read-only inventory authorization for **`TG-SRC-PUB-002`** and/or **`TG-SRC-PUB-001`**.
- Exact release/export package locations (zip, cloud-only binaries).
- GFVP receipt-to-binary mapping for deferred PUB-002 payloads.
- Inventories for `TG-SRC-ARC-001`, `TG-SRC-REG-001`, `TG-SRC-KNO-001`.
- Supabase inventory timing.

Concrete next steps:

1. Choose next inventory track: **`TG-SRC-PUB-002`** read-only inventory (recommended) and/or **`TG-SRC-PUB-001`** Publishing Constitution inventory.
2. Execute authorized read-only pass only — no import, no external edits.
3. Draft exact import manifest / migration plan after inventory and human ratification (VIS-001 playbook).
4. Keep `TG-SRC-PUB-002` deferred for physical import until receipt gate satisfied.
5. Do not move source files, create derivative controls, edit external systems, or resume app/RPC work until explicitly authorized.
