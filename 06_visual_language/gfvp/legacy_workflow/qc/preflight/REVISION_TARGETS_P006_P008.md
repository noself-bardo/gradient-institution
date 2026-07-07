# Revision Targets - P006 and P008

Status: Revision Required Before Prompt Lock
Date: 2026-07-03
Batch: GFVP_B01
Image Gate: Closed

## Summary

Only two prompt packets need revision before prompt lock consideration:

- P006 - Preserved Human Capabilities
- P008 - Product and Platform Servant Layer

No hard fails were found. These are pre-image-gate prompt refinements to prevent the image model from flattening institutional status or over-centering software.

## P006 - Preserved Human Capabilities

Prompt packet:

`03_PROMPT_PACKETS/P006_capability_preserved-human-capabilities_prompt.md`

QC sheet:

`04_PREFLIGHT_QC/P006_capability_preserved-human-capabilities_qc.md`

### Current Issue

The prompt passes, but the diagram type says "capability lattice / matrix." A lattice may visually imply that all systems are equally mature or equally active.

Systems Visualizer is especially sensitive because it is still pending / blocked until a canonical source packet exists.

### Exact Revision Needed

Revise the prompt so the central structure is a **status-aware matrix**, not a lattice.

Add a visible **Pending / Blocked** badge for Systems Visualizer.

Make status differences visible across all entries.

### Text to Add or Strengthen

Use this in the master prompt:

> The central structure should be a status-aware capability matrix, not a freeform lattice. Each row must clearly separate Capability, Preserving System, Class, and Status. Systems Visualizer must be visibly marked Pending / Blocked - canonical source packet required.

Use this in the condensed prompt:

> Status-aware matrix, not lattice. Systems Visualizer visibly marked Pending / Blocked.

### Do Not Change

Keep:

- title
- thesis
- matte black / metallic silver field atlas grammar
- Capability Map v0.3 as primary source
- Sandbox / Candidate status

## P008 - Product and Platform Servant Layer

Prompt packet:

`03_PROMPT_PACKETS/P008_implementation_servant-layer_prompt.md`

QC sheet:

`04_PREFLIGHT_QC/P008_implementation_servant-layer_qc.md`

### Current Issue

The prompt passes, but the software terms may visually dominate: Supabase, Dashboard, APIs, Agents, Automation.

That risks making implementation look like the origin of The Gradient.

### Exact Revision Needed

Make the top three institutional layers visually dominant:

1. Constitution
2. Stewardship
3. Capability Map / Engine Registry

Move software terms into a smaller subordinate implementation band.

Add a visible boundary statement:

> Automation cannot ratify.

### Text to Add or Strengthen

Use this in the master prompt:

> The top three layers must be visually dominant: Constitution, Stewardship, and Capability Map / Engine Registry. Product and Platform Requirements should sit below them. Supabase, Dashboard, APIs, Agents, and Automation must appear only as a smaller subordinate implementation band. Add a visible boundary label: Automation cannot ratify canon, admission, image gate, or constitutional change.

Use this in the condensed prompt:

> Dominant top layers: Constitution, Stewardship, Capability / Registry. Software appears only as subordinate implementation band. Visible boundary: Automation cannot ratify.

### Do Not Change

Keep:

- title
- thesis
- servant-layer stack diagram type
- matte black / metallic silver field atlas grammar
- Sandbox / Candidate status
- anti-dashboard avoid list

## After Revision

Run second-pass QC only on:

- P006
- P008

If both pass above 90%, move all 8 prompt packets to prompt lock consideration.

