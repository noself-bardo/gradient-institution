# TG-WEB-001 — QA Checklist

Status: Active Rebuild  
Use before each public deployment or major content pass.

## Identity & Boundary

- [ ] Asset ID TG-WEB-001 visible in header and footer metadata
- [ ] Canonical boundary statement in boundary banner
- [ ] Canonical boundary statement in footer
- [ ] README opens with institutional metadata block
- [ ] No copy claims the site defines or governs The Gradient

## Semantic Structure

- [ ] `header`, `nav`, `main`, `section`, `aside`, `footer` landmarks present
- [ ] Single visible page H1 in header
- [ ] Room sections have unique IDs matching navigation
- [ ] Skip link targets `#main`

## Source Registry

- [ ] Every source has authority layer, status, and role labels
- [ ] Governing sources distinguished from companion sources
- [ ] Crisis Liturgies marked companion, not governing
- [ ] Pending PDFs show honest "reader PDF needed" state
- [ ] No links to internal production trackers
- [ ] All public Notion links open in new tabs

## Engines & Case Studies

- [ ] Engine entries show classification, status, lock boundary
- [ ] Validated engines (ISA, Shape Change, Fuckification) present
- [ ] Case studies show method, validation, and what they prove
- [ ] Stewardship Exercise 001 included as institutional proof

## Visual Language

- [ ] GFVP presented as visual doctrine inheritance
- [ ] Crisis Liturgies not treated as governing authority
- [ ] Visual Language Room cross-links to Notion sources

## Platform Room

- [ ] Software explicitly marked servant layer
- [ ] Non-authority banner present
- [ ] GitHub and Netlify described as implementation only

## Accessibility

- [ ] Page works without JavaScript (static HTML content visible)
- [ ] Form controls have associated labels
- [ ] Color contrast sufficient for body text and badges
- [ ] Focus states visible on interactive elements
- [ ] Mobile layout readable at 320px width

## Link Pass

- [ ] Manually verify each Notion URL opens readable content
- [ ] Verify no 403 or broken links on public buttons
- [ ] PDF buttons either work or show pending state

## Deployment

- [ ] netlify.toml present
- [ ] .nojekyll present
- [ ] Publish directory configured correctly
- [ ] Netlify described as public gateway only in docs

## Institutional Records

- [ ] Notion record exists under 10 Implementation
- [ ] Supabase registry pending status documented if write path unavailable
- [ ] Google Drive folder pending status documented

## Reader Path Smoke Test

- [ ] Newcomer path: orientation → sources → glossary reachable
- [ ] Steward path: orientation → system-map → sources reachable
- [ ] Developer path: platform room reachable with servant layer messaging
