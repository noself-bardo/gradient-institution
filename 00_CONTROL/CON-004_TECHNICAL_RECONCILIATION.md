# CON-004 Technical Reconciliation

**Classification:** `TECHNICAL_PROVENANCE_BLOCK / NO_FOUNDER_DECISION_REQUIRED`

## Current copies

| Kind | Paths | Bytes | SHA-256 | Identity |
|---|---|---:|---|---|
| Markdown | `CL_PHASE_00_EVIDENCE/...REGISTER...md`; `03_PHASE_EVIDENCE/...REGISTER...md` | 11,631 | `F6E829AA8672A0765912F486AE3CE07084C0AFEDD2BA528D17E036DB4D83903E` | Byte-identical |
| JSON | `CL_PHASE_00_EVIDENCE/...REGISTER...json`; `03_PHASE_EVIDENCE/...REGISTER...json` | 25,541 | `33E180E3665A432882C8EC2CA8CD6567DBA54D81804ADEA444BBED3045A8EABB` | Byte-identical |

Both formats are UTF-8/ASCII without BOM and CRLF-terminated. There is no line-ending, encoding, whitespace, or JSON-key-order difference between each duplicate pair.

## Recorded provenance

- Duplicate package manifests record Markdown `e4caeaba…a8ff29` / 11,517 bytes and JSON `ef53e1a4…983434` / 24,954 bytes.
- The Phase 02I ratified file-authority register and 03-phase admission sidecars repeat that prior hash lineage.
- The current copies do not match those recorded values.
- Git history shows the `CL_PHASE_00_EVIDENCE` copies added in `f61e6bcd` (2026-07-14); the `03_PHASE_EVIDENCE` copies were materialized in `cc9f1e3a` (2026-07-15) and preserve the current bytes.

## Authority-path observation

The ratification register identifies `03_PHASE_EVIDENCE` as `ADMITTED_PHASE_EVIDENCE / NONOPERATIVE`; a migration map targets `CL_PHASE_00_EVIDENCE`. Both current copies are tracked, and neither source authorizes copying or selecting an operative record.

## Conclusion

The exact earlier hashed version was not recoverable from the inspected reachable Git history. Because each current duplicate pair is internally identical, the observed drift is not caused by the duplicate materialization itself. The evidence is insufficient to determine whether the original modification was semantic, a pre-Git export change, or a manifest/sidecar failure.

The discrepancy affects custody and ratification traceability. It does not authorize treating either current copy as canonical, operative, or production-ready.

## Safe next technical action

Recover the source package or the pre-Git custody record that generated the recorded hashes, then compare it against the current pair under the project-local evidence-custody protocol. Do not overwrite, normalize, copy, promote, rename, or select a register during that task.
