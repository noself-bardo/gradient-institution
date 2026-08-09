# CL-CORPUS-001 — Corpus Intake and Orchestration Architecture v0.1

Status: **ENGINEERING CANDIDATE / NOT CANON / NOT PRODUCTION AUTHORITY**

## Decision proposed for validation

Raw reality is plural; Crisis Liturgies production is singular.

`CL_CORPUS` is a project boundary upstream of CL-CONV-001 and CL Builder. It receives heterogeneous evidence, preserves provenance, enforces admission requirements, and emits a single canonical handoff class. It cannot perform canon interpretation or production.

## Lanes admitted at the intake boundary

- Capture lane: folders, files, transcripts, exports, reports, notes.
- Extraction lane: deterministic text extraction with source boundaries preserved.
- Privacy lane: declared classification, consent, third-party-material flag, handling protocol.
- Custody lane: exact inventory, source hashes, normalized-corpus hash, package receipt.
- Scheduling lane: idempotent validation and orchestration suitable for recurring tasks.

Future adapters may transcribe audio or extract PDFs, but must return extracted text plus provenance into the same contract. They may not bypass admission.

## One exit

Every successful run emits `CL-CORPUS-HANDOFF-1.0.0` to CL-CONV-001. No intake adapter may emit a page specification, render packet, image, proof, or release.

## Authority seam

```text
RAW REALITY
  -> CL_CORPUS (capture, admission, normalization, custody)
  -> CL-CONV-001 (interpretation, source arbitration, architecture)
  -> frozen volume specification + explicit authorization
  -> CL_BUILDER (compile, render routing, QC, assembly, custody)
  -> Founder acceptance
```

The seam is deliberately asymmetric: corpus handoff may advance evidence to review, but it cannot advance production state.

## Cold-simulation acceptance criteria

- Mixed postmortem bundle is inventoried deterministically.
- Every source receives an exact checksum.
- Source ordering and normalized corpus are deterministic.
- Missing consent fails closed.
- Unsupported unextracted media fails closed.
- Handoff schema allows exactly one recipient: CL-CONV-001.
- All canon, builder, render, publication, and release permissions remain false.
- Package manifest and custody receipt verify.
