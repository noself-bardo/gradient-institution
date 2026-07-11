# CL-IV Web Deploy Register v1.0

**Gate date:** 2026-07-11  
**Verdict:** WEB COMMIT AND DEPLOY PASS WITH NOTES  
**Status:** WEB COMMIT COMPLETE — DEPLOY PENDING (NETLIFY SITE NOT WIRED FOR TG-WEB-001)  

---

## Commit Register

| Field | Value |
|---|---|
| SHA | `cbf914caa5ea3110e1d600bc77a07e921182520f` |
| Branch pushed | `main` |
| Local branch | `master` (tracks `origin/main`) |
| Repository | `noself-bardo/gradient-institution` |
| Message | Publish CL-IV reader PDF entry |
| Files in commit | 10 (companion.json + 9 CL-IV docs) |
| Push | SUCCESS |

---

## Deploy Register

| Field | Value |
|---|---|
| Provider | Netlify (intended) |
| Deploy URL | Not established for TG-WEB-001 |
| Documented target | `https://thegradient.netlify.app` |
| Observed live site content | Field Atlas (not TG-WEB-001 companion ledger) |
| Deploy timestamp | N/A |
| Deployment status | NOT EXECUTED |
| Blocker | No Netlify CLI/token; no GitHub Actions deploy; hostname not serving `tg-web-001` |

---

## Remote Integrity Spot-Check

| Check | Result |
|---|---|
| Raw `companion.json` at `cbf914c` reachable | PASS |
| CL-VOL-IV `href` authorized URL | PASS |
| CL-VOL-IV `actionLabel` = `OPEN READER PDF` | PASS |
| CL-VOL-I / CL-VOL-II preserved from prior main | PASS (Reader PDF hosted) |

---

## Exclusions Confirmed

| Asset | Committed? |
|---|---|
| Print PDF | No |
| Screen PDF | No |
| Frozen snapshot zip | No |
| Proof folders | No |
| Archive snapshot folders | No |
| `CRISIS_LITURGIES/` trees | No |

---

## Disposition

```text
WEB COMMIT AND DEPLOY PASS WITH NOTES
COMMIT: COMPLETE (cbf914c on main)
DEPLOY: PENDING — NETLIFY NOT WIRED FOR TG-WEB-001
PUBLICATION LIVE: NOT MARKED
```
