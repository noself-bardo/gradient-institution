# CL-IV Web Commit and Deploy v1.0

**Collection:** Crisis Liturgies IV — Depressive Infrastructure / Domestic Collapse Cycle  
**Gate date:** 2026-07-11  
**Review type:** Commit + deploy gate — publication-live marking blocked until live verification  
**Prior gate:** Web preview validation PASS  

---

## Verdict

# WEB COMMIT AND DEPLOY PASS WITH NOTES

**Authorized status:** WEB COMMIT COMPLETE — DEPLOY PENDING (NETLIFY SITE NOT WIRED FOR TG-WEB-001)

Git commit and push to `main` succeeded. Production Netlify deployment of `08_platform/tg-web-001` could not be completed in this environment: no Netlify CLI/token, no GitHub Actions deploy workflow, and `https://thegradient.netlify.app` currently serves a different Field Atlas site (not TG-WEB-001). Publication remains **not live**.

---

## Commit Capture

| Field | Value |
|---|---|
| Commit SHA | `cbf914caa5ea3110e1d600bc77a07e921182520f` |
| Short SHA | `cbf914c` |
| Branch (local) | `master` |
| Deployment branch (remote) | `main` |
| Remote | `origin` (`noself-bardo/gradient-institution`) |
| Commit URL | https://github.com/noself-bardo/gradient-institution/commit/cbf914caa5ea3110e1d600bc77a07e921182520f |
| Commit message | Publish CL-IV reader PDF entry |
| Author time (UTC) | 2026-07-11T21:38:59Z |
| Push result | **SUCCESS** (`2b8d0f3..cbf914c` → `main`) |

---

## Files Committed (10)

| Path | Change |
|---|---|
| `08_platform/tg-web-001/data/companion.json` | Modified — CL-VOL-IV public href |
| `08_platform/tg-web-001/docs/CLIV_PUBLIC_ASSET_UPLOAD_v1.0.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_WEB_PUBLICATION_PATCH_v1.0.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_WEB_PUBLICATION_PATCH_DIFF_SUMMARY_v1.0.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_WEB_PREVIEW_VALIDATION_v1.0.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_WEB_PREVIEW_VALIDATION_REGISTER_v1.0.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_PUBLIC_RELEASE_RECORD.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_PRINT_READY_AUTHORIZATION_RECORD.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_PUBLIC_RELEASE_AUTHORIZATION_v1.0.md` | Added |
| `08_platform/tg-web-001/docs/CLIV_PRINT_READY_AUTHORIZATION_REVIEW_v1.0.md` | Added |

**Explicitly excluded from commit:** print PDF, screen PDF, frozen snapshot zip, proof folders, archive snapshots, `CRISIS_LITURGIES/` trees, unrelated README edits.

---

## Pre-Commit Checks (7 / 7)

| # | Check | Result |
|---|---|---|
| 1 | `git status` reviewed | **PASS** |
| 2 | Only intended CL-IV website/publication files staged | **PASS** |
| 3 | `companion.json` validates as JSON | **PASS** |
| 4 | CL-VOL-IV `href` = authorized GitHub Release URL | **PASS** |
| 5 | CL-VOL-IV `actionLabel` = `OPEN READER PDF` | **PASS** |
| 6 | No internal/Drive/Windows/print/snapshot/zip paths in CL-IV public entry | **PASS** |
| 7 | Sibling entries not altered by this patch commit | **PASS** |

**Note after rebase onto `origin/main`:** Remote PR #1 had already wired CL-VOL-I and CL-VOL-II public readers. Post-rebase remote `companion.json` preserves those entries plus CL-VOL-IV. Verified via raw GitHub URL for `cbf914c`.

---

## Deploy Attempt

| Field | Value |
|---|---|
| Deployment provider (intended) | Netlify |
| Intended deploy URL | `https://thegradient.netlify.app` (per `institutional-metadata.json` / README) |
| Deploy timestamp | N/A — deploy not executed |
| Deployment status | **NOT EXECUTED / BLOCKED** |
| GitHub Actions workflows | **None** in repo |
| Netlify CLI | **Not installed** |
| `NETLIFY_AUTH_TOKEN` / `NETLIFY_SITE_ID` | **Absent** |
| Auto-deploy on push | **Not observed** (no commit statuses / check runs) |

### Live probe notes

| Probe | Result |
|---|---|
| `https://thegradient.netlify.app/` | HTTP 200 — title: *THE GRADIENT - Constitutional Knowledge Ecology (Field Atlas)* |
| Contains `companionLedger` / TG-WEB-001 markers | **No** |
| `https://thegradient.netlify.app/data/companion.json` | **404** |
| `https://thegradient.netlify.app/08_platform/tg-web-001/` | **404** |

Institutional records already mark Netlify for TG-WEB-001 as **Pending deployment**. Current production hostname does not serve the Archive Gateway build from this path.

---

## Accepted Notes (Non-Blocking for Commit; Blocking for Live Publication)

1. **Commit + push complete** — CL-IV registry and gate docs are on `main` at `cbf914c`.
2. **Netlify deploy not completed** — requires steward Netlify site linkage (publish directory `08_platform/tg-web-001`) or CLI auth + manual deploy.
3. **Do not mark publication live** — live verification cannot pass until TG-WEB-001 is actually hosted.
4. **PDFs remain on GitHub Releases** — site deploy (when wired) hosts HTML/CSS/JS only.

---

## Status Transition

| From | To | Date |
|---|---|---|
| WEB PREVIEW VALIDATION PASS — PENDING COMMIT AND DEPLOY | **WEB COMMIT COMPLETE — DEPLOY PENDING (NETLIFY SITE NOT WIRED FOR TG-WEB-001)** | 2026-07-11 |

---

## Gate Status

| Gate | State |
|---|---|
| Public asset upload | COMPLETE |
| Website patch | COMPLETE |
| Local preview validation | PASS |
| **Git commit** | **COMPLETE** (`cbf914c`) |
| **Push to `main`** | **COMPLETE** |
| **Netlify deploy** | **PENDING / BLOCKED** |
| Live publication verification | **PENDING** |
| Publication live | **NOT MARKED** |

---

## Next Actions (Steward)

1. Connect Netlify site to `noself-bardo/gradient-institution` with publish directory `08_platform/tg-web-001`, **or** run authenticated Netlify CLI deploy from that folder.
2. Confirm production URL serves `data/companion.json` with CL-VOL-IV `OPEN READER PDF`.
3. Run CL-IV live publication verification gate.
4. Only then mark publication live.

---

## References

- `CLIV_WEB_DEPLOY_REGISTER_v1.0.md`
- `CLIV_WEB_PREVIEW_VALIDATION_v1.0.md`
- `CLIV_PUBLIC_RELEASE_RECORD.md`
- Commit: https://github.com/noself-bardo/gradient-institution/commit/cbf914caa5ea3110e1d600bc77a07e921182520f
