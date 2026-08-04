# Crisis Liturgies Builder

Status: **MVP v0.3 / CL-METHOD-001 REGRESSION INTEGRATED / RENDER GATE CLOSED**

This directory implements the specification-driven Crisis Liturgies production layer authorized by CCR-CL-002, CL-GEN-STD-001, CCR-CL-003, and CL-METHOD-001.

It converts frozen specifications into narrow visual-only render packets, validates outputs, and assembles authoritative typography deterministically. It does not author, reinterpret, or silently repair canon.

## Proven method

CL-METHOD-001 is supported by three frozen four-page references:

- CL-REF-001 — MIRROR Golden Production Reference v1.0
- CL-REF-002 — IVORY Contrast Production Reference v1.0
- CL-REF-003 — REFUSAL Governance Stress Reference v1.1

The renderer owns visual evidence only. Deterministic assembly owns authoritative typography, page geometry, margins, folios, citations, and PDF construction.

## Regression coverage

The test suite verifies:

- three distinct frozen references and twelve total reference pages
- one bounded repair in MIRROR, zero rerenders in IVORY, and two page-bounded repairs in REFUSAL
- frozen proof checksums
- invariant four-page function order
- a separate REFUSAL issue cover that does not enter or alter canonical function order
- a cover-only density exception that leaves ordinary interior limits unchanged
- visual-only renderer ownership
- matte-black canvas and closed transparency
- 100% REFUSAL edge-black coverage with zero chroma and transparency violations
- named-layer, live-text, vector-path SVG editability with zero embedded raster images
- REFUSAL package, manifest, and checksum integrity
- fail-closed authorization for every unrelated issue
- page-bounded repair preserving accepted pages
- IVORY QC metrics against the locked envelope
- prior schema, compiler, authorization, calibration, QC, renderer, ingest, and assembly behavior

Current validation: **22 tests pass; one optional external-corpus test skips when the Volume IV corpus is not mounted.**

## Current authorization state

The full CL-EV-001 volume remains `NOT_APPROVED_FOR_RENDER`.

Issue 02 — REFUSAL completed its bounded authorization, proof, QC, packaging, and founder-approval cycle. That approval authorizes no other issue and does not open the full-volume render gate.

PR 17 is founder-authorized for final regression integration and merge after local and CI verification.
