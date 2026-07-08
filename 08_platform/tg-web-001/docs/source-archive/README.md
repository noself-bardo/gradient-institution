# Source Archive — Desktop `gradient explainer html`

Status: Reference only — not deployed

## Files Archived

| Archive file | Original | Role |
|---|---|---|
| `plate-reader-cl-dark.html` | `the-gradient-constitutional-explainer-cl.html` | **Active design direction** — dark Crisis Liturgies plate reader, snap-scroll, TG-000–TG-010 |
| `index-light-field-atlas.html` | `index.html` | Earlier warm/light field atlas — 1609-line monolith with module explorer |

TG-WEB-001 active build (`../../index.html`) inherits from **plate-reader-cl-dark.html**, split into `styles.css`, `app.js`, and `data/*.json`.

## Assets Expected Alongside Source HTML

The Desktop folder contained **HTML only**. These files were referenced but not present in that folder:

### Companion PRINT PDFs (canonical — not screen PDFs)

| Filename | PRINT Drive ID | Deploy path |
|---|---|---|
| `CRISIS_LITURGIES_COMPLETE_v1.0_PRINT.pdf` | `1BWkZDG1945DTQ15fTS4414NEJZrURevJ` | `../../assets/pdf/` |
| `CRISIS_LITURGIES_II_PRIVATE_INSTRUMENTS_v1.0_PRINT.pdf` | `1jQOjrhLlz2t_eEl-fM7JiRKN72yPAseZ` | `../../assets/pdf/` |

**Do not use** the embedded Drive IDs from archived HTML (`15ruF4Onqb4KDLG-bTt9T-qUFVeat1g2B`, `10wWqyGGs9pAZrtjqZzQ7MWOAc2mVC3tm`) — those point to **screen PDFs**, not print PDFs.

### Companion thumbnails (same folder in original bundle)

- `01-vol-i-reality-collapse-artifact.png`
- `02-vol-i-liturgical-hymn.png`
- `03-vol-i-doctrine-page.png`
- `04-vol-ii-reproductive-calendar-case.png`
- `05-vol-ii-liturgical-hymn.png`
- `06-vol-ii-doctrine-page.png`

Copy into `../../assets/img/` when found. Do not generate substitutes in-repo.

## Governing Sources

Original HTML linked to Notion. TG-WEB-001 uses local PDF exports in `../../assets/pdf/` — see `../../assets/pdf/README.md`.

## Lineage

```text
Desktop/gradient explainer html
  → docs/source-archive/ (this folder)
  → 08_platform/tg-web-001/ (active TG-WEB-001 implementation)
```
