# TG-WEB-001 — Netlify Wiring Precheck v1.0

**Gate date:** 2026-07-11  
**Review type:** Netlify wiring precheck only — no deploy, no publication-live mark  
**Prior status:** WEB COMMIT COMPLETE — DEPLOY PENDING  
**Target site path:** `08_platform/tg-web-001`  
**Documented hostname:** `https://thegradient.netlify.app`

---

## Verdict

# TG-WEB-001 NETLIFY WIRING READY — MANUAL NETLIFY DEPLOY REQUIRED

Root `netlify.toml` now points Netlify at `08_platform/tg-web-001`. Production deploy still requires Netlify UI site linkage or authenticated CLI. Publication remains **not live**.

---

## Precheck Findings

### 1. Repository root inspection

| Item | Result |
|------|--------|
| Root `netlify.toml` (before this gate) | **ABSENT** |
| Root `package.json` | **ABSENT** (static site; no Node build) |
| GitHub Actions deploy workflows | **ABSENT** (no `.github/workflows`) |
| Nested `08_platform/tg-web-001/netlify.toml` | **PRESENT** — `publish = "."` |
| Netlify CLI installed | **NO** |
| `NETLIFY_AUTH_TOKEN` / `NETLIFY_SITE_ID` | **ABSENT** |

### 2. What production currently serves

| Probe | Result |
|-------|--------|
| `https://thegradient.netlify.app/` | HTTP 200 — title includes **Field Atlas** / Constitutional Knowledge Ecology |
| TG-WEB-001 markers (`companionLedger`, Archive Gateway) | **Not observed** |
| `https://thegradient.netlify.app/data/companion.json` | **404** |
| Conclusion | Hostname is **not** publishing `08_platform/tg-web-001` |

### 3. Intended publish target

| Question | Answer |
|----------|--------|
| Should Netlify serve repo root? | **No** |
| Should Netlify serve Field Atlas (current live)? | **No** — wrong product for Archive Gateway |
| Should Netlify serve `08_platform/tg-web-001`? | **Yes** — TG-WEB-001 Archive Gateway |

### 4. Nested config conflict analysis

| Config | Publish | When it applies |
|--------|---------|-----------------|
| Nested `08_platform/tg-web-001/netlify.toml` | `"."` | Correct **only if** Netlify base directory = `08_platform/tg-web-001`, or CLI deploy from that folder |
| Root `netlify.toml` (this gate) | `"08_platform/tg-web-001"` | Correct for **repo-root–linked** Netlify sites |

**Ruling:** No overwrite of nested config. Root file added as the monorepo publish directive. Nested file retained for folder-scoped CLI deploys. Headers mirrored from nested config to root.

### 5. Safe patch applied

| Change | Status |
|--------|--------|
| Create root `netlify.toml` with `publish = "08_platform/tg-web-001"` | **DONE** |
| Preserve nested `netlify.toml` | **DONE** (unchanged) |
| Modify CL-IV frozen snapshot / PDFs / images | **NOT DONE** (out of scope) |
| Change CL-IV public asset URL | **NOT DONE** |
| Mark publication live | **NOT DONE** |
| Execute Netlify deploy | **NOT DONE** — no authenticated CLI/token |

---

## Constraints Confirmed

| Rule | Result |
|------|--------|
| Do not modify CL-IV frozen snapshot | PASS |
| Do not modify PDFs | PASS |
| Do not regenerate images | PASS |
| Do not change CL-IV public asset URL | PASS |
| Do not mark publication live | PASS |
| Do not deploy without Netlify credentials | PASS |
| Do not overwrite unrelated Netlify config without audit | PASS |

---

## Expected Manual Deploy Steps (Steward)

1. In Netlify UI for `thegradient` (or a new TG-WEB-001 site):
   - Link repository `noself-bardo/gradient-institution`
   - Confirm build settings pick up root `netlify.toml`
   - Publish directory must resolve to `08_platform/tg-web-001`
   - Build command: empty / none
2. Trigger deploy from `main`
3. Verify:
   - Site title / Archive Gateway identity (not Field Atlas)
   - `GET /data/companion.json` → 200
   - CL-VOL-IV `href` still the authorized GitHub Releases URL
4. Only then run live publication verification gate

---

## Status Transition

| From | To |
|------|-----|
| WEB COMMIT COMPLETE — DEPLOY PENDING | **TG-WEB-001 NETLIFY WIRING READY — MANUAL NETLIFY DEPLOY REQUIRED** |

---

## Related

- [TG-WEB-001_NETLIFY_WIRING_PLAN_v1.0.md](TG-WEB-001_NETLIFY_WIRING_PLAN_v1.0.md)
- [CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md](CLIV_WEB_COMMIT_AND_DEPLOY_v1.0.md)
- [CLIV_WEB_DEPLOY_REGISTER_v1.0.md](CLIV_WEB_DEPLOY_REGISTER_v1.0.md)
