# GFVP P012-P040 Batch Completion Prompt

Status: Ready for Codex Handoff
Date: 2026-07-04
Purpose: Executable prompt for Codex to finish the remaining GFVP text-production layer.

## Copy-Paste Prompt for Codex

You are working inside the Gradient Foundational Visual Package package.

Your job is to finish the text-production layer for P012-P040 without opening image gates, generating images, approving visuals, changing canon status, or altering the locked roadmap unless explicitly instructed.

## Current State

The package is located at:

`/workspace/gradient_foundational_visual_package_batch_01/`

The locked roadmap is:

`13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.md`

The batch protocol is:

`13_ROADMAPS/GFVP_BATCH_PRODUCTION_PROTOCOL_v0-1.md`

The object schema is:

`11_OBJECT_SPECIFICATIONS/GFVP_OBJECT_SCHEMA_v0-1.md`

The compiler doctrine is:

`12_COMPILER_PROMPTS/GFVP_IMAGE_PROMPT_COMPILER_v0-1.md`

P001-P011 are visually approved.

P012-P015 already have object specifications, object QC, compiled prompts, and compiled prompt QC. They are text-locked from Pack A. Do not overwrite them unless a QC defect is found and recorded in a revision log.

P012 is the next image-gate candidate, but no image gate is open by this handoff.

P016-P040 need text production.

## Core Doctrine

One plate equals one institutional object.

One object specification equals one institutional object.

One generated image renders one completed object specification.

The image prompt is a compiler, not a creative brief.

Nothing here is canon by default.

Useful outputs must route through Admission before entering institutional knowledge.

## Do Not Do

Do not generate images.

Do not open image gates.

Do not approve outputs.

Do not promote anything into canon.

Do not revise P001-P011 approved outputs.

Do not collapse multiple roadmap objects into one plate.

Do not generate from broad conversational prompts.

Do not use the old broad prompt packets as generation authority.

Do not use production workflow, QC, prompt engineering, or this handoff as visual subject matter.

## Required Work

### Phase 01 - Verify Existing Pack A Text

Verify that P012-P015 each have:

- object specification
- object QC
- compiled image prompt
- compiled prompt QC

Do not rewrite these files unless a specific defect is found.

If a defect is found, create a revision log before editing.

### Phase 02 - Complete Pack B Text Production

Create object specs, object QC, compiled prompts, compiled prompt QC, and a pack review sheet for:

- P016 Archive
- P017 Book of Becoming
- P018 Commons
- P019 Reclassification
- P020 Distillation

### Phase 03 - Complete Pack C Text Production

Create object specs, object QC, compiled prompts, compiled prompt QC, and a pack review sheet for:

- P021 Engine
- P022 Practice Framework
- P023 Engine Registry
- P024 Practice Framework Registry

### Phase 04 - Complete Pack D Text Production

Create object specs, object QC, compiled prompts, compiled prompt QC, and a pack review sheet for:

- P025 Capability
- P026 Capability Map
- P027 Preserved Human Capability Matrix
- P028 Capability Gap

### Phase 05 - Complete Pack E Text Production

Create object specs, object QC, compiled prompts, compiled prompt QC, and a pack review sheet for:

- P029 Trust State
- P030 Status State
- P031 Uncertainty / Absence
- P032 Conflict / Contradiction
- P033 Failure Mode
- P034 Steward Review

### Phase 06 - Complete Pack F Text Production

Create object specs, object QC, compiled prompts, compiled prompt QC, and a pack review sheet for:

- P035 Session Closeout
- P036 Reentry Protocol
- P037 Confirmation Receipt
- P038 Product / Platform Boundary
- P039 Automation Boundary
- P040 Constitutional Field Atlas Index

Important: P040 is a synthesis/index plate. It may receive a text packet, but its compiled prompt must explicitly say it should not be generated until component plates P001-P039 are approved or intentionally waived by the user.

## File Naming

Object specs:

`11_OBJECT_SPECIFICATIONS/GFVP-OBJ-P###-OBJECT-NAME_v0-1.md`

Object QC:

`11_OBJECT_SPECIFICATIONS/GFVP-OBJ-P###-OBJECT-NAME_OBJECT_QC_v0-1.md`

Compiled prompts:

`12_COMPILER_PROMPTS/GFVP-COMPILED-P###-OBJECT-NAME_PROMPT_v0-1.md`

Compiled prompt QC:

`12_COMPILER_PROMPTS/GFVP-COMPILED-P###-OBJECT-NAME_QC_v0-1.md`

Pack review sheets:

`13_ROADMAPS/GFVP_PACK_B_REVIEW_SHEET_v0-1.md`

Repeat for Packs C-F.

Text-production receipts:

`13_ROADMAPS/GFVP_PACK_B_TEXT_PRODUCTION_RECEIPT.md`

Repeat for Packs C-F.

## Each Object Specification Must Include

- Object ID
- Object Name
- Spec Version
- Status
- Date
- Source Tier
- Primary Source
- Secondary Sources
- Gradient Lane
- Purpose
- Constitutional Role
- Boundaries
- Inputs / Outputs
- Required Labels
- Forbidden Concepts
- Diagram Family
- Visual Center
- Orientation
- Negative Prompt
- Compiler Notes
- QC Requirements

## Each Object QC Must Include

- QC Result
- Source Authority
- Object Boundary
- Diagram Fit
- Required Labels
- Risk Notes
- Decision

Use pass/fail language.

Do not approve weak objects. If the object is too broad, split it or return it to roadmap review.

## Each Compiled Prompt Must Include

- Use case
- Asset type
- instruction to render the institutional object itself
- explicit exclusion of production process, prompt architecture, QC, image gate, document family, and conversation
- Object Name
- Purpose
- Constitutional Role
- Boundaries
- Inputs
- Outputs
- Non-outputs
- Required Labels
- Diagram Family
- Visual Center
- Orientation
- Visual Grammar
- Required Metadata
- Title Text
- Thesis Text
- Status Text
- Footer Text
- Negative Prompt
- final instruction to render only this object

## Required Visual Grammar

Use the established GFVP field atlas grammar:

- flat front-facing constitutional field atlas plate
- matte black background
- metallic silver and pale institutional gray typography and linework only
- strict modular grid
- high negative space
- thin functional rules
- visible status band reading Sandbox / Candidate
- restrained monumental serif title
- readable institutional serif or sans labels
- technical mono metadata
- no color accents

## Required Metadata Pattern

Use exact metadata values for each plate:

- Catalog Identifier: GFVP-B01-P###
- Plate Type: [roadmap plate family]
- Object Class: [specific object class]
- Version: v0.1
- Date: 2026-07-04
- Status: Sandbox / Candidate
- Checksum: TBD

## Pack Review Sheet Must Include

- Pack result
- pack contents table
- object roles
- risk notes
- recommended review order
- recommended image-gate order
- required user decisions
- boundary stating no image generation is authorized

## Roadmap and Handoff Updates

After creating each pack:

1. Update `13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.md`
2. Update `13_ROADMAPS/GFVP_40_PLATE_ROADMAP_v0-1.csv`
3. Update `00_README/README.md`
4. Update `09_HANDOFFS/GFVP_B01_HANDOFF.md`
5. Refresh `/workspace/gradient_foundational_visual_package_batch_01.zip`

Do not mark any unreviewed text packet as approved.

Use status:

`Text Packet Ready for Review`

unless the user explicitly approves the pack.

## Final Deliverable

Create one final handoff:

`09_HANDOFFS/GFVP_CODEX_COMPLETION_REPORT_P012_P040.md`

It must summarize:

- files created
- packs completed
- plates still needing user review
- plates eligible for image gate
- known risks
- next recommended image-gate sequence

## Recommended Stop Point

Stop after text production is complete and the package zip is refreshed.

Do not start image generation.

