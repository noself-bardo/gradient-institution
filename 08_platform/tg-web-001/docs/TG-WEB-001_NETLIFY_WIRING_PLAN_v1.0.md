# TG-WEB-001 — Netlify Wiring Plan v1.0

**Date:** 2026-07-11  
**Purpose:** Safe Netlify publish-directory wiring for the Gradient Archive Gateway  
**Status:** WIRING READY — MANUAL DEPLOY REQUIRED  
**Do not mark publication live from this plan alone.**

---

## Goal

Serve static TG-WEB-001 (`08_platform/tg-web-001`) as the public Archive Gateway on the approved Netlify hostname, without hosting large PDFs on Netlify and without displacing steward release assets.

---

## Architecture

```text
GitHub: noself-bardo/gradient-institution (main)
        │
        ├─ netlify.toml  →  publish = "08_platform/tg-web-001"
        │
        └─ Netlify site (thegradient / TG-WEB-001)
                │
                ├─ HTML / CSS / JS / data/*.json   ← hosted
                └─ PDF buttons → GitHub Releases tg-web-pdf-assets  ← not Netlify
```

---

## Config Inventory

| Location | Role | Action |
|----------|------|--------|
| `/netlify.toml` (repo root) | Repo-linked site publish directory | **Created** this gate |
| `/08_platform/tg-web-001/netlify.toml` | Folder-scoped CLI / base-dir deploy | **Retain** (`publish = "."`) |
| `package.json` | N/A | None — static site |
| `.github/workflows` | N/A | None today; optional later |

### Root `netlify.toml` (authoritative for repo-root linkage)

```toml
[build]
  publish = "08_platform/tg-web-001"
  command = ""
```

Security headers (frame deny, nosniff, referrer policy) are included at root to match the nested site config.

---

## Why Field Atlas Is Wrong for This Gate

Observed production (`https://thegradient.netlify.app`) currently serves a **Field Atlas** experience. That site:

- Does not expose `/data/companion.json` (404)
- Does not render the TG-WEB-001 companion ledger
- Does not satisfy CL-IV / CL-EV-001 public reader wiring

TG-WEB-001 is the Archive Gateway servant layer. Wiring must publish `08_platform/tg-web-001`, not the Field Atlas tree.

**Steward note:** If Field Atlas must remain on the same hostname, that is a product conflict requiring an explicit human decision (new Netlify site vs hostname reassignment). This plan assumes TG-WEB-001 becomes the intended public gateway at the documented URL.

---

## Deploy Options (Manual)

### Option A — Netlify UI (preferred without CLI)

1. Open Netlify site settings for the target site
2. Site configuration → Build & deploy → Continuous deployment
3. Repository: `noself-bardo/gradient-institution`
4. Branch: `main`
5. Confirm root `netlify.toml` is detected **or** set Publish directory = `08_platform/tg-web-001` and Build command blank
6. Trigger deploy
7. Run verification checklist below

### Option B — Authenticated Netlify CLI

```bash
# Requires netlify login / NETLIFY_AUTH_TOKEN + linked site
cd 08_platform/tg-web-001
netlify deploy --prod --dir .
```

Or from repo root after root `netlify.toml` is linked:

```bash
netlify deploy --prod
```

**Not executed in this gate** — CLI absent; tokens absent.

---

## Post-Deploy Verification Checklist

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | Homepage identity | TG-WEB-001 / Archive Gateway (not Field Atlas title) |
| 2 | Companion data | `GET /data/companion.json` → 200 JSON |
| 3 | CL-VOL-IV entry | Present; `href` = authorized GitHub Releases screen PDF URL |
| 4 | CL-VOL-I / II | Preserved hosted entries |
| 5 | PDF host probe | OPEN READER PDF buttons enable after successful HEAD |
| 6 | No Netlify PDF hosting | Large PDFs still on `tg-web-pdf-assets` only |
| 7 | Publication live mark | **Still blocked** until separate live-publication verification gate |

---

## Explicit Non-Goals

- Do not modify CL-IV frozen snapshot
- Do not modify or re-upload PDFs
- Do not regenerate images
- Do not change CL-IV public asset URL
- Do not mark publication live from wiring alone
- Do not auto-deploy without Netlify credentials

---

## Success Criteria for Next Statuses

| Condition | Next status |
|-----------|-------------|
| Root wiring committed; deploy not yet run | **TG-WEB-001 NETLIFY WIRING READY — MANUAL NETLIFY DEPLOY REQUIRED** |
| Deploy succeeds; live probes pending formal gate | **WEB DEPLOY COMPLETE — PENDING LIVE PUBLICATION VERIFICATION** |
| Live probes pass + human authorization | Publication-live marking (separate gate) |

---

## References

- [TG-WEB-001_NETLIFY_WIRING_PRECHECK_v1.0.md](TG-WEB-001_NETLIFY_WIRING_PRECHECK_v1.0.md)
- [TG-WEB-001_PUBLIC_PDF_STRATEGY.md](TG-WEB-001_PUBLIC_PDF_STRATEGY.md)
- [CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md](CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md)
- Root: `/netlify.toml`
- Nested: `/08_platform/tg-web-001/netlify.toml`
