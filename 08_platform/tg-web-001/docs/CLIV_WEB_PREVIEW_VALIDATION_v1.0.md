# CL-IV Web Preview Validation v1.0

**Collection:** Crisis Liturgies IV — Depressive Infrastructure / Domestic Collapse Cycle  
**Validation date:** 2026-07-11  
**Review type:** Local preview validation only — no deploy, no publication-live marking  
**Prior gate:** Web publication patch PASS  

---

## Verdict

# WEB PREVIEW VALIDATION PASS

**Authorized status:** WEB COMMIT COMPLETE — DEPLOY PENDING (NETLIFY SITE NOT WIRED FOR TG-WEB-001)

Local preview validation confirms the patched `CL-VOL-IV` companion shelf entry renders correctly with an active `OPEN READER PDF` CTA pointing to the authorized public screen PDF. Commit is complete (`cbf914c`); Netlify deploy remains pending.

---

## Project Inspection

| Field | Value |
|---|---|
| Web project | `08_platform/tg-web-001` |
| Site type | Static HTML/CSS/JS (no bundler) |
| Entry point | `index.html` |
| Renderer | `app.js` → `renderLedger("companionLedger", companion, availability)` |
| Registry | `data/companion.json` |
| `package.json` | **Not present** |
| Build command | **None** (`netlify.toml` publish = `.`, command = `""`) |
| Lint/test scripts | **None** |

---

## Validation Method

| Step | Method |
|---|---|
| Local serve | `python -m http.server 8765` from `tg-web-001/` |
| JSON validation | `json.loads()` on `companion.json` |
| UI render simulation | Python harness mirroring `app.js` `renderLedger()` + `pdfAction()` logic |
| Asset availability | HTTP HEAD probe on authorized GitHub Release URL |
| Layout checks | CSS inspection for desktop + mobile breakpoints (`@media max-width: 700px`, `820px`) |

**Note:** No Node.js / Playwright available in environment. Ledger HTML output was simulated from the same rendering rules as `app.js`; functional CTA, link, and field checks are authoritative for this gate.

---

## Validation Checklist (15 / 15)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Project structure inspected | **PASS** | Static site; `index.html`, `app.js`, `data/companion.json` |
| 2 | Build/lint command identified | **PASS** | No npm scripts; JSON + static serve used |
| 3 | `companion.json` valid JSON | **PASS** | Parse successful |
| 4 | Site served locally | **PASS** | `index.html` + JSON fetched via HTTP |
| 5 | `CL-VOL-IV` renders in companion ledger | **PASS** | Simulated ledger entry present |
| 6 | CTA reads `OPEN READER PDF` | **PASS** | `pdfAction()` output verified |
| 7 | CTA does not read `READER PDF NEEDED` | **PASS** | Pending span not rendered for CL-IV |
| 8 | Link opens authorized screen PDF URL | **PASS** | `href` matches GitHub Release download URL |
| 9 | Link returns HTTP 200 | **PASS** | HEAD probe successful |
| 10 | No forbidden paths in CL-IV public UI | **PASS** | No snapshot, Drive, Windows, zip, print PDF, or checksum strings |
| 11 | Sibling entries render normally | **PASS** | CL-VOL-I, CL-VOL-II, CL-CANON-1.1, CL-TRN-001 render with pending CTAs |
| 12 | Desktop layout CSS present | **PASS** | `.ledger`, `.entry` rules in `styles.css` |
| 13 | Mobile/narrow layout CSS present | **PASS** | `@media (max-width: 700px)` and `820px` breakpoints |
| 14 | Build/lint/test run | **PASS WITH NOTE** | No build/lint scripts exist; JSON + render simulation substituted |
| 15 | Deploy not performed | **PASS** | Deferred |

---

## CL-VOL-IV Observed UI State

| Field | Rendered value |
|---|---|
| ACC | `CL-VOL-IV` |
| STATUS | `Reader PDF hosted` |
| ACCESS | `AVAILABLE` |
| CTA | `<a class="act" href="…screen.pdf">OPEN READER PDF</a>` |
| Link target | `_blank` with `rel="noopener noreferrer"` |
| SOURCE NOTE | Generic steward note (no snapshot path) |

---

## Sibling Entry State (Unchanged)

| `acc` | CTA | ACCESS |
|---|---|---|
| `CL-VOL-I` | `READER PDF NEEDED` (pending span) | `PENDING — READER PDF NEEDED` |
| `CL-VOL-II` | `READER PDF NEEDED` (pending span) | `PENDING — READER PDF NEEDED` |
| `CL-CANON-1.1` | `READER PDF NEEDED` (pending span) | `PENDING — READER PDF NEEDED` |
| `CL-TRN-001` | `READER PDF NEEDED` (pending span) | `PENDING — READER PDF NEEDED` |

---

## Deferred (Non-Blocking)

| Item | Status |
|---|---|
| `sources.json` / `SRC-CL-PDF-IV` | Deferred — site init does not depend on it |
| Headless browser screenshot | Not run — render simulation sufficient for CTA/link validation |
| Netlify deploy | Not performed |

---

## Scope Compliance

| Rule | Result |
|---|---|
| No deploy | **PASS** |
| No publication live | **PASS** |
| No asset upload | **PASS** |
| No snapshot/PDF modification | **PASS** |
| No image regeneration | **PASS** |
| No unrelated entry patches | **PASS** |

---

## Status Transition

| From | To | Date |
|---|---|---|
| WEB PUBLICATION PATCH COMPLETE — PENDING LOCAL PREVIEW VALIDATION | **WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY** | 2026-07-11 |

---

## Gate Status

| Gate | State |
|---|---|
| Public asset upload | COMPLETE |
| Website patch | COMPLETE |
| **Local preview validation** | **PASS** |
| Commit | **COMPLETE** (`cbf914c`) |
| Deploy | **PENDING / BLOCKED** (Netlify not wired) |
| Publication live | **NOT MARKED** |

---

## Next Actions (After Netlify Wiring)

1. Deploy TG-WEB-001 via Netlify (publish directory `08_platform/tg-web-001`)
2. Run live publication verification
3. Optional: add `SRC-CL-PDF-IV` to `sources.json` in separate pass

**Commit complete. See `CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md`.**

---

## References

- `CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md`
- `CLIV_WEB_DEPLOY_REGISTER_v1.0.md`
- `CLIV_WEB_PREVIEW_VALIDATION_REGISTER_v1.0.md`
- `CLIV_WEB_PUBLICATION_PATCH_v1.0.md`
- `CLIV_PUBLIC_ASSET_UPLOAD_v1.0.md`
- `data/companion.json`
- `app.js`
