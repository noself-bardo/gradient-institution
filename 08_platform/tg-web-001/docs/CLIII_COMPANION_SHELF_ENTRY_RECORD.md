# CL-III Companion Shelf Entry Record

Status: Complete  
Authority: Implementation / Servant Layer — not canonical  
Scope: TG-WEB-001 companion shelf integration for Crisis Liturgies III: Emergency Objects  
Date: 2026-07-08

## What Was Added

| Location | Change |
|---|---|
| `data/companion.json` | New `CL-VOL-III` shelf entry — Crisis Liturgies III: Emergency Objects (CL-025 through CL-036) |
| `app.js` | Extended companion ledger renderer to display optional boundary fields (range, web availability, reader status, PDF status, archive note, boundary note, source note) |
| `data/sources.json` | New `SRC-CL-PDF-III` source registry entry |
| `assets/pdf/README.md` | CL-III print PDF path and frozen snapshot ingest note |
| `index.html` | Companion shelf and reader-path copy updated to reflect CL-III shelf-only status |
| `README.md` | Link to this record |
| `docs/TG-WEB-001_INSTITUTIONAL_RECORD.md` | Implementation status note for CL-III companion shelf entry |

## What Was Not Added

- CL-III artifact pages or individual CL-025 through CL-036 plate reader routes
- CL-III entries in `data/artifacts.json` or `data/reader-path.json`
- Local copy of `CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf` in `assets/pdf/`
- Ingest of 48 CL-III final PNGs into `assets/img/`
- Live plate reader gallery integration for CL-III
- Drive archive file reads or writes
- PDF rebuild, image generation, canon edits, or prompt packet revisions
- Execution of `tools/cl_iii_release_assembly_prep.py`

## PDF Action Guard

`pdfAction()` in `app.js` probes each PDF path via `HEAD` before rendering. When the file is absent, the UI renders a non-clickable `<span class="act pending" aria-disabled="true">READER PDF NEEDED</span>` — not an anchor. CL-VOL-III therefore exposes no dead public link until local ingest completes.

## Source-of-Truth Used

Applied in this order:

1. **`docs/CLIII_RELEASE_ASSEMBLY_READINESS_RECORD.md`** — boundary/provenance; current controlling CL-III state (print PDF approved, archive lock approved, indexing closed, frozen snapshot complete); release assembly folder as historical provenance only
2. **`docs/TG-WEB-001_SOURCE_POLICY.md`** — companion series rules; no Drive links on public buttons; honest pending state for non-ingested PDFs
3. **`docs/TG-WEB-001_INSTITUTIONAL_RECORD.md`** — TG-WEB-001 servant-layer scope
4. **`README.md`** — documentation structure and asset checklist conventions
5. **Existing Vol I/II patterns** — `data/companion.json` ledger entries, `renderLedger` in `app.js`, `assets/pdf/README.md` accession table

Approved print PDF reference (not copied):

```text
Frozen release snapshot:
09_RELEASE_SNAPSHOTS/CRISIS_LITURGIES/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0

Expected local target when ingested:
assets/pdf/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf
```

Release assembly folder (`06_RELEASE_ASSEMBLY/...`) was **not** used as current state.

## Current CL-III Web Boundary

| Field | Value |
|---|---|
| Title | Crisis Liturgies III: Emergency Objects |
| Range | CL-025 through CL-036 |
| Shelf status | Archived print release |
| Web availability | Companion shelf entry only |
| Live plate reader | Not yet integrated |
| Local PDF button | Shows **READER PDF NEEDED** until ingest |
| Archive state (controlling) | Print PDF approved; final archive lock approved; indexing closed; frozen release snapshot complete |
| Authority | Companion only — not governing |

## Unresolved Path / Asset Gaps

| Gap | Impact | Resolution |
|---|---|---|
| `assets/pdf/CRISIS_LITURGIES_III_EMERGENCY_OBJECTS_v1.0_PRINT.pdf` not in repo | Open Volume button shows pending | Copy approved print PDF from frozen release snapshot when ingest is authorized |
| No CL-III thumbnails in `assets/img/` | Artifact grid remains Vol I/II only | Future gallery ingest — 48 finals or curated subset |
| No per-artifact CL-III pages | No deep-link reader for CL-025 through CL-036 | Future plate reader expansion |
| Frozen snapshot lives on Drive, not Git | Web gateway cannot self-verify PDF bytes | Human ingest step required per `assets/pdf/README.md` |

These gaps are **non-blocking** for the companion shelf entry itself.

## Future Full CL-III Gallery Ingest

**Status: Ready for review — not started**

Prerequisites met in archive/snapshot layers:

- Print PDF approved
- Final archive lock approved
- Indexing closed
- Frozen release snapshot complete

Remaining work before full gallery ingest:

1. Human authorization to copy print PDF into `assets/pdf/`
2. Curated or full PNG ingest strategy for `assets/img/`
3. Plate reader route design for CL-025 through CL-036 (separate from Vol I/II patterns if needed)
4. QA pass per `TG-WEB-001_QA_CHECKLIST.md`

Do **not** treat release assembly readiness documents as blockers or as current state.

## Disposition

```text
CL-III COMPANION SHELF ENTRY COMPLETE WITH NON-BLOCKING GAPS
```
