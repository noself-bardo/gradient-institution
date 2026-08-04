# Crisis Liturgies Builder

Status: **MVP v0.3 / CL-METHOD-001 REGRESSION INTEGRATED / RENDER GATE CLOSED**

This directory implements the specification-driven Crisis Liturgies production layer authorized by CCR-CL-002, CL-GEN-STD-001, CCR-CL-003, and CL-METHOD-001.

It converts frozen specifications into narrow visual-only render packets, validates outputs, and assembles authoritative typography deterministically. It does not author, reinterpret, or silently repair canon.

## Proven method

CL-METHOD-001 is supported by two frozen four-page references:

- CL-REF-001 — MIRROR Golden Production Reference v1.0
- CL-REF-002 — IVORY Contrast Production Reference v1.0

The renderer owns visual evidence only. Deterministic assembly owns authoritative typography, page geometry, margins, folios, citations, and PDF construction.

## Regression coverage

The test suite verifies:

- two distinct frozen references and eight total reference pages
- one bounded repair in MIRROR and zero rerenders in IVORY
- frozen proof checksums
- invariant four-page function order
- visual-only renderer ownership
- matte-black canvas and closed transparency
- page-bounded repair preserving accepted pages
- IVORY QC metrics against the locked envelope
- prior schema, compiler, authorization, calibration, QC, renderer, ingest, and assembly behavior

Current validation: **16 tests pass; one optional external-corpus test skips when the Volume IV corpus is not mounted.**

## Current authorization state

The full CL-EV-001 volume remains `NOT_APPROVED_FOR_RENDER`.

A bounded authorization packet is prepared for Issue 02 — REFUSAL. It authorizes nothing until explicitly accepted by the founder.

PR 17 remains draft and unmerged.
