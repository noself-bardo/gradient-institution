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
- Serialized handoff file SHA-256: `bac85c94fc6c905bed844975d95d5be2e4e060446544734c266c8a455df71fd9`
- Package manifest SHA-256: `f754a91be0f84196262e8c47a42eb2e17ed03773f98ba05705bf82857ae8628d`

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
