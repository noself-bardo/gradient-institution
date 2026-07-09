# Reader PDF Assets — Local Preview Cache Only

This folder is an **optional local preview cache**. It is **not** the public deployment source for reader PDFs.

## Policy (TG-WEB-004)

Public reader PDFs are served from a **public object/release asset URL**. Netlify hosts the explainer site only. Large print PDFs are not committed to Git and are not uploaded through Netlify manual deploy.

The UI may link only to reader-facing public PDF URLs and must HEAD-probe them before enabling OPEN PDF.

| Layer | Role |
|---|---|
| **Netlify** | HTML / CSS / JS site only |
| **Public reader asset host** | Preferred: GitHub Releases · Fallback: Supabase Storage public bucket |
| **`assets/pdf/` (this folder)** | Optional local cache for steward preview — not public href source |
| **Drive / release snapshots** | Canonical steward-copy sources — never public hrefs |
| **Git** | Code, data, docs, `.gitkeep`, this README — never `*.pdf` |

## Preferred public URL pattern

```text
https://github.com/<OWNER>/<REPO>/releases/download/tg-web-pdf-assets/<FILENAME>.pdf
```

Until release assets exist, companion `href` values remain empty and the UI shows **READER PDF NEEDED**.

## Intended live companion filenames (host when ready)

| File | Accession | Live shelf |
|---|---|---|
| `CRISIS_LITURGIES_COMPLETE_v1.0_PRINT.pdf` | CL-VOL-I | Yes — once hosted |
| `CRISIS_LITURGIES_II_PRIVATE_INSTRUMENTS_v1.0_PRINT.pdf` | CL-VOL-II | Yes — once hosted |
| `CRISIS_LITURGIES_IV_DEPRESSIVE_INFRASTRUCTURE_v1.0_PRINT.pdf` | CL-VOL-IV | Yes — once hosted |

## Not live

| Volume | Status |
|---|---|
| CL-III Emergency Objects | Documented only — separate admission required |
| CL-V Dual Power Domestics | Future only — do not admit until intentionally ready |

Keep `.gitkeep` and this README tracked. Do not commit PDFs.
