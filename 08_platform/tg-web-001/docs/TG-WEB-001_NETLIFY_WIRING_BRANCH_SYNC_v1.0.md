# TG-WEB-001 — Netlify Wiring Branch Sync v1.0

**Gate date:** 2026-07-11  
**Review type:** Branch sync only — no deploy, no publication-live mark  
**Prior status:** TG-WEB-001 NETLIFY WIRING READY — MANUAL NETLIFY DEPLOY REQUIRED  
**Deployment branch:** `main`

---

## Verdict

# BRANCH SYNC PASS — NETLIFY READY FOR MANUAL DEPLOY

Netlify wiring is now on `main` and pushed. Publication remains **not live**. Deploy still requires Netlify UI / authenticated CLI.

---

## Pre-Sync State

| Field | Value |
|-------|-------|
| Local branch (before) | `master` |
| Wiring commit (local only) | `6bb2463` — Wire Netlify to TG-WEB-001 static site |
| Remote tracking | `origin/main` @ `caa07d1` |
| Local `main` existed? | No — created from `origin/main` |
| CL-IV publication commit on `origin/main` | `cbf914c` — Publish CL-IV reader PDF entry (**present**) |

---

## Sync Method

| Step | Result |
|------|--------|
| `git fetch origin` | PASS |
| `git checkout -B main origin/main` | PASS — local `main` tracks `origin/main` |
| Confirm `cbf914c` ancestor of HEAD | PASS |
| Cherry-pick `6bb2463` | PASS → new commit `bac10cb` (same tree, new SHA) |
| Verify root `netlify.toml` | PASS |
| Verify CL-IV `companion.json` entry | PASS |
| `git push origin main` | PASS (recorded below) |

**Why cherry-pick (not push master):** Explicit deployment branch is `main`. Local `master` is not authorized as the Netlify deploy branch.

---

## Verification on `main`

### Root `netlify.toml`

```toml
[build]
  publish = "08_platform/tg-web-001"
  command = ""
```

### CL-IV companion entry

| Field | Value |
|-------|-------|
| `acc` | `CL-VOL-IV` |
| `status` | `Reader PDF hosted` |
| `actionLabel` | `OPEN READER PDF` |
| `href` | GitHub Releases `tg-web-pdf-assets` screen PDF URL (unchanged) |

### Ancestry preserved

```text
bac10cb Wire Netlify to TG-WEB-001 static site   ← wiring on main
caa07d1 docs(tg-web-001): record CL-IV commit/deploy gate
cbf914c Publish CL-IV reader PDF entry           ← preserved
```

---

## Push Capture

| Field | Value |
|-------|-------|
| Remote | `origin` |
| Branch | `main` |
| Wiring commit on main | `bac10cb` |
| Source local commit | `6bb2463` (master; cherry-picked) |

---

## Constraints Confirmed

| Rule | Result |
|------|--------|
| Do not modify CL-IV frozen snapshot | PASS |
| Do not modify PDFs | PASS |
| Do not regenerate images | PASS |
| Do not change CL-IV public asset URL | PASS |
| Do not mark publication live | PASS |
| Do not deploy from wrong branch | PASS — synced to `main` only |
| Do not point Netlify at local master | PASS |

---

## Status Transition

| From | To |
|------|-----|
| TG-WEB-001 NETLIFY WIRING READY — MANUAL NETLIFY DEPLOY REQUIRED (wiring on local master only) | **BRANCH SYNC PASS — NETLIFY READY FOR MANUAL DEPLOY** |

---

## Next Gate (Manual)

1. In Netlify UI, confirm site build uses repo `main` + root `netlify.toml` publish dir `08_platform/tg-web-001`
2. Trigger deploy
3. Verify Archive Gateway (not Field Atlas) and `GET /data/companion.json` → 200
4. Only then run live publication verification

**Do not mark publication live from this sync gate.**
