# Crisis Liturgies Builder

Status: **MVP v0.1 / BUILD VALIDATED / RENDER GATE CLOSED**

This directory implements the specification-driven Crisis Liturgies production layer authorized by:

- `CCR-CL-002` — Builder Authority and Production Gate Reform
- `CL-GEN-STD-001` — Crisis Liturgies Generation Standard v1.0
- `CCR-CL-003` — Four-Page Functional Code and Visual Palette Reconciliation

It converts a frozen volume specification into narrow render packets. It does not author, reinterpret, or repair canon.

## Current boundary

Implemented:

- JSON Schemas for volumes, pages, render packets, repair records, releases, and build locks
- invariant four-page function validation
- matte-black and metallic-silver render enforcement
- removal of legacy conversational image-gate text from executable packets
- deterministic typography ownership at layout stage
- bounded partial-human-evidence exceptions for expansion volumes
- image QC for dimensions, black coverage, white fields, transparency, foreground density, and edge contamination
- normalized 48-page `CL-EV-001` specification generation
- current-state and event-log separation
- dry-run compilation and preflight reporting

Not implemented in v0.1:

- external image-model adapters
- automatic rerender API calls
- PDF layout and typography compositing
- Volume IV asset-derived numeric calibration
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

## Visual defaults

- Canvas: `#000000`
- Transparency: prohibited
- Ink family: metallic silver tonal range
- Maximum foreground coverage: 25%
- White-field maximum: 2%
- Cast shadows and photographic lighting: prohibited
- Authoritative body copy in generated imagery: prohibited

The numeric QC profile is operational but provisional until calibrated against accepted Volume IV masters.

## Regenerate the Pygmalion specification

Export the two authoritative Google Docs as plain text, place them in `source_exports/`, then run:

```bash
python tools/normalize_pygmalion.py \
  --prompt-export source_exports/CL-EV-001_48_PRODUCTION_PACKETS_VISUAL_PROMPTS.txt \
  --copy-register source_exports/CL-PM_48_PAGE_COPY_REGISTER.txt
```

## Commands

```bash
python -m cl_builder.cli validate volumes/CL-EV-001/volume.yaml

python -m cl_builder.cli compile \
  volumes/CL-EV-001/volume.yaml \
  --output build/CL-EV-001.render-packets.json

python -m cl_builder.cli preflight \
  volumes/CL-EV-001/volume.yaml \
  --output build/CL-EV-001.preflight.json

python -m cl_builder.cli qc-image \
  volumes/CL-EV-001/volume.yaml \
  path/to/output.png \
  --output build/qc/output.json
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Render authorization

`CL-EV-001` is normalized and build-valid, but its current state explicitly remains:

```text
NOT_APPROVED_FOR_RENDER
```

A render adapter must refuse execution until the frozen volume specification includes a durable `APPROVED_FOR_RENDER` authorization record.
