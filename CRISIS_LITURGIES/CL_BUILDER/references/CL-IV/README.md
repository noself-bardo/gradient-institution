# CL-IV Regression Calibration

Status: **MEASURED / v0.2**

Source corpus:

- `crisis-liturgies-iv-depressive-infrastructure-v1.0-screen.pdf`
- Google Drive file ID: `1QrUyqxGOLPilQu9bWLoQPheovIBYuWe8`
- SHA-256: `168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe`
- 48 embedded reader pages at 1086 x 1448 pixels

The source PDF is not committed to Git. `CL-IV_CALIBRATION_v0.2.json` records the measured corpus envelope and per-page results.

The calibration does not redefine canon. It converts the accepted CL-IV proof corpus into machine-testable regression thresholds:

- minimum black coverage: 0.34
- maximum white-field fraction: 0.0015
- maximum foreground coverage: 0.66
- minimum edge black coverage: 0.995
- maximum chroma fraction above a 24-level channel delta: 0.003
- maximum mean channel delta: 9.0

These values are acceptance-envelope thresholds, not design targets. New pages should generally retain more negative space than the most visually dense accepted CL-IV page.
