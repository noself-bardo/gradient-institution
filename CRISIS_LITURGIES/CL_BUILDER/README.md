# Crisis Liturgies Builder

Status: **MVP v0.2 / ENGINEERING STAGE 02 COMPLETE / RENDER GATE CLOSED**

This directory implements the specification-driven Crisis Liturgies production layer authorized by:

- `CCR-CL-002` - Builder Authority and Production Gate Reform
- `CL-GEN-STD-001` - Crisis Liturgies Generation Standard v1.0
- `CCR-CL-003` - Four-Page Functional Code and Visual Palette Reconciliation

It converts a frozen volume specification into narrow render packets, validates visual outputs, and assembles deterministic typography. It does not author, reinterpret, or silently repair canon.

## Current boundary

Implemented:

- JSON Schemas for volumes, pages, render packets, render receipts, repair records, assembly manifests, releases, and build locks
- invariant four-page function validation
- matte-black and metallic-silver render enforcement
- removal of legacy conversational image-gate text from executable packets
- bounded partial-human-evidence exceptions for expansion volumes
- image QC for dimensions, black coverage, white fields, transparency, density, edge contamination, and chromatic drift
- measured 48-page Volume IV regression calibration
- provider-neutral fail-closed renderer job planning
- external-result ingestion, QC, checksums, accepted-asset promotion, and receipts
- deterministic manuscript parsing and PDF typography assembly
- normalized 48-page `CL-EV-001` specification
- current-state and event-log separation
- dry-run compilation and preflight reporting

Not implemented in v0.2:

- a selected external image-provider adapter
- automatic API render or rerender calls
- issue-batch retry orchestration against a provider
- final visual integration because `CL-EV-001` is not approved for render
- final build-lock creation after render authorization

## Authority hierarchy

```text
Crisis Liturgies Canon
> Generation Standard
> Release Profile
> Frozen Volume Specification
> Page Specification
> Render Packet
> Model Output
```

## Canonical page-function code

Every four-page issue maps profile-specific labels to:

1. `RELIC_ENTRY`
2. `WITNESS_RECORD`
3. `SYSTEM_TRANSLATION`
4. `ARCHIVE_DISPOSITION`

## Measured visual envelope

The v1.1 release profile is calibrated against the accepted 48-page CL-IV screen corpus.

- Canvas: `#000000`
- Transparency: prohibited
- Ink family: metallic silver tonal range
- Minimum black coverage: 34%
- Maximum foreground coverage: 66%
- Maximum white-field fraction: 0.15%
- Minimum black edge coverage: 99.5%
- Maximum strong-chroma fraction: 0.3%
- Cast shadows and photographic lighting: prohibited
- Authoritative body copy in generated imagery: prohibited

These values are regression limits, not composition targets.

## Commands

From this directory:

```bash
python -m cl_builder.cli validate volumes/CL-EV-001/volume.yaml

python -m cl_builder.cli compile \
  volumes/CL-EV-001/volume.yaml \
  --output build/CL-EV-001.render-packets.json

python -m cl_builder.cli preflight \
  volumes/CL-EV-001/volume.yaml \
  --output build/CL-EV-001.preflight.json

python -m cl_builder.cli calibrate path/to/cliv-pages \
  --profile profiles/crisis-liturgies-expansion-v1.yaml \
  --source-document path/to/cliv-screen.pdf \
  --output references/CL-IV/CL-IV_CALIBRATION_v0.2.json

python -m cl_builder.cli render-plan \
  volumes/CL-EV-001/volume.yaml \
  --output-dir build/render-plan

python -m cl_builder.cli qc-image \
  volumes/CL-EV-001/volume.yaml \
  path/to/output.png \
  --output build/qc/output.json

python -m cl_builder.cli ingest-result \
  build/render-plan/jobs/CL-PM-I01-P1.json \
  path/to/output.png \
  --accepted-dir build/accepted \
  --receipt build/receipts/CL-PM-I01-P1.json

python -m cl_builder.cli assemble \
  volumes/CL-EV-001/volume.yaml \
  --manuscript path/to/CL-PM_DF_FINAL_PROSE_MANUSCRIPT.txt \
  --assets build/accepted \
  --output build/CL-EV-001.pdf \
  --manifest build/CL-EV-001.assembly.json
```

## Tests

```bash
python -m unittest discover -s tests -v
```

The external Volume IV corpus test runs when `/tmp/cliv_native` is mounted; CI otherwise validates the committed calibration report and all deterministic contracts.

## Render authorization

`CL-EV-001` is normalized and build-valid, but its current state explicitly remains:

```text
NOT_APPROVED_FOR_RENDER
```

The renderer contract must refuse provider execution until the frozen volume specification contains a durable `APPROVED_FOR_RENDER` authorization record.
