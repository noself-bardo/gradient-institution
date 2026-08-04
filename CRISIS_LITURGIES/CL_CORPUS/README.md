# Crisis Liturgies Corpus Intake and Orchestration

Status: **Engineering milestone v0.1 / cold-simulation candidate**

`CL_CORPUS` is a contained program for receiving heterogeneous raw reality and producing one canonical, custody-complete handoff. It does not author Crisis Liturgies, decide canon, generate images, or open a render gate.

## Architectural rule

Many intake lanes may enter:

- voice-memo transcripts
- therapy or reflective notes
- project postmortems
- reports and manuscripts
- exported conversations
- project folders and mixed evidence bundles

Exactly one package leaves:

`CL-CORPUS-HANDOFF-1.0.0`

That package is addressed to `CL-CONV-001`. Only an approved Conversion Architecture and frozen volume specification may cross from interpretation into `CL_BUILDER`.

## Stage sequence

1. `CAPTURE` inventories source material without rewriting it.
2. `ADMISSION` verifies declared authority, consent, privacy, and scope.
3. `NORMALIZATION` extracts supported text into a deterministic corpus while preserving source boundaries.
4. `CUSTODY` records SHA-256 checksums and package lineage.
5. `HANDOFF` emits the single validated package and leaves all production gates closed.

Unsupported binary sources are preserved in the inventory but block handoff until an authorized extraction or transcript is supplied. Source files are never modified.

## Quick start

```text
python -m cl_corpus.cli run simulations/CL-CORPUS-SIM-001/intake.json --output build/CL-CORPUS-SIM-001
```

The command returns `HANDOFF_READY` only when every source, consent declaration, and checksum passes. It never invokes a renderer.

## Scheduling contract

Scheduled tasks or a Codex lane may safely run `validate` and `run`. The run stops at `AWAITING_CONVERSION_ARCHITECT`; it cannot silently continue into editorial interpretation, rendering, publication, or release.
