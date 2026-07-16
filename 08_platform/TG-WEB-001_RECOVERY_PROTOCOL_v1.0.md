# TG-WEB-001 Recovery Protocol v1.0

Status: LOCKED / HUMAN RATIFIED

Ratified: 2026-07-16

Human ratifier: Steven

Asset: TG-WEB-001 — The Gradient Archive Gateway

Authority layer: Implementation / Servant Layer

## Purpose

Restore one authoritative development and publication path for the HTML explainer, eliminate contradictory operational states, and make public reader access testable without allowing the explainer to establish canon.

This protocol is an implementation control record. It does not amend The Gradient Constitution, revise Crisis Liturgies canon, or elevate TG-WEB-001 above its servant-layer authority.

## Canonical Topology

| Function | Authority |
|---|---|
| Canonical local checkout | `C:\Users\steve\Projects\gradient-institution` |
| Authoritative executable repository | `https://github.com/noself-bardo/gradient-institution` |
| Canonical branch relationship | local `master` tracking remote `main` |
| Explainer source | `08_platform/tg-web-001` |
| Existing production site | `https://thegradient.netlify.app` |
| Netlify publish directory | `08_platform/tg-web-001` |
| Public reader asset host | GitHub Release tag `tg-web-pdf-assets` |
| Public companion manifest | `08_platform/tg-web-001/data/companion.json` |

Netlify is a deployment target, not a repository. GitHub Releases are public asset storage, not a repository. Diagnostic clones and preview servers have no institutional authority.

## Ratified Public Shelf

The live companion shelf contains only:

- CL-I — Crisis Liturgies, Volume I
- CL-II — Private Instruments
- CL-IV — Depressive Infrastructure

CL-III remains documented only and outside the live `companion.json` manifest until separately ratified. Its existing release asset may remain stored but unlinked. CL-V remains future only.

Crisis Liturgies Canon v1.1 and the Crisis Liturgy Translation Doctrine remain `Reader PDF needed` with empty public hrefs until reader-facing PDFs are intentionally admitted.

## PDF Publication Rule

- Git tracks code, documentation, JSON, and metadata only.
- PDFs are not committed to Git.
- Git LFS is not used.
- Netlify hosts the site only.
- Public reader PDFs are served from the existing GitHub Release.
- Drive, Notion, release snapshots, trackers, handoff pages, and release-status records are not public reader hrefs.
- Public URL availability is validated during build, release, or deployment QC.
- The browser does not perform cross-origin HEAD probes. A non-empty ratified public href renders as a link; an empty href renders as not published.
- An embedded PDF viewer is a separate future feature and is not required for reliable public PDF access.

## Governance

- Steven ratifies public-shelf membership, irreversible architecture, and publication boundaries.
- The Archivist maintains provenance, resolves authority conflicts, and stops drift.
- The TG-WEB Build Steward implements the ratified state without expanding infrastructure.
- Leon, EOTA-LEON-001, performs adversarial review for drift, euphemism, platform multiplication, and false complexity; Leon does not independently alter canon.

## Prohibitions

- No additional repository for TG-WEB-001.
- No additional Netlify site for TG-WEB-001.
- No new PDF host while the existing GitHub Release remains viable.
- No manual large-PDF upload to Netlify.
- No public Drive, Notion, snapshot, tracker, production-handoff, or release-status fallback links.
- No unratified addition of CL-III or CL-V to the live companion manifest.
- No declaration of publication success before live QC.

## Recovery Acceptance Criteria

1. `data/companion.json` contains CL-I, CL-II, and CL-IV; it contains neither CL-III nor CL-V.
2. CL-I, CL-II, and CL-IV public release URLs return HTTP 200 after redirects.
3. Canon v1.1 and Translation Doctrine have empty hrefs and render as not published.
4. No PDF is tracked anywhere in Git history.
5. The existing Netlify site serves the build from `08_platform/tg-web-001`.
6. The live companion shelf opens the three ratified PDFs.
7. The live site exposes no public reader href to Drive, Notion, snapshots, trackers, production handoffs, or release-status records.
8. Desktop and mobile layouts remain usable.

## Supersession Rule

When an older TG-WEB operational record conflicts with this protocol, this ratified recovery protocol governs current implementation and deployment. Older records remain historical evidence and must not be silently rewritten as if their earlier instructions were still active.
