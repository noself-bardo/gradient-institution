# CL-CORPUS-SIM-001 — Cold Simulation Receipt

Date: 2026-08-04

Status: **PASS / HANDOFF READY / PRODUCTION GATES CLOSED**

## Simulated intake

- Mode: `MIXED_PROJECT_BUNDLE`
- Material: fictional project postmortem, timeline CSV, and decision JSON
- Source count: 3
- Source inventory SHA-256: `5d624f7adfa59fd1840fdc554e49adb2df82306eec167fc52a81f20a7a58f6ed`
- Normalized corpus SHA-256: `f3a5c43b8f7c4c9fd306cd277d4af5c263cbb5e289c5de9180b9e5450b30000d`
- Handoff object SHA-256: `00d088196b0774f4e9c56a21ae8f0ae852223e16a0e2b7b3ad802cc5fb674365`
- Serialized handoff file SHA-256: `a3797609e53b57a0b10c828263d5179d3c262356e6d69b6f066c22e9e5e86fd2`
- Package manifest SHA-256: `02efb94a6a8c34cd16c99c93403bfd0de29626cc38275fa711e15d498b2ad027`

## Result

The run emitted exactly one `CL-CORPUS-HANDOFF-1.0.0` package addressed to `CL-CONV-001`. The resulting state is `AWAITING_CONVERSION_ARCHITECT`.

No canon was inferred. No volume specification was generated. No renderer was called. Builder handoff, rendering, publication, and release all remained unauthorized.

## Tests

Eleven corpus tests passed:

- intake schema validation
- canonical handoff validation
- deterministic repeat run
- exact manifest verification
- committed cold-receipt verification
- handoff self-hash verification
- missing-consent fail-closed behavior
- consent-record requirement
- sensitive-handling requirement
- third-party-handling requirement
- unextracted-binary fail-closed behavior

## Verdict

`CL_CORPUS v0.1 COLD SIMULATION PASS / READY FOR ENGINEERING REVIEW`
