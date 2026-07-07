# GFVP Batch Production Protocol v0.1

Status: Locked Sandbox Production Protocol
Date: 2026-07-04
Package: Gradient Foundational Visual Package

## Purpose

This protocol defines how Codex can batch the GFVP object-specification process without contaminating canon or bypassing human image-gate approval.

## Core Rule

Codex may batch text preparation.

Codex may not batch final authority.

## Batch Unit

The default batch unit is a production pack of 4 to 6 plates.

Pack A begins with P011-P015.

## Automatable Stages

Codex may perform these stages for a whole pack:

1. Create object specifications from the locked roadmap and named source material.
2. Run object QC for each specification.
3. Compile image prompts from completed object specifications.
4. Run compiled prompt QC for each compiled prompt.
5. Create a pack review sheet.
6. Create a pack lock receipt after user approval.
7. Update README, handoff, roadmap status, and Notion receipts.
8. Refresh the package zip.

## Human-Gated Stages

These stages require explicit user approval:

1. Selecting or changing roadmap objects.
2. Locking object specifications.
3. Opening any image gate.
4. Approving generated images.
5. Rejecting outputs as failure modes.
6. Promoting material through Admission.
7. Treating any visual as institutional canon.

## Image Gate Rule

Image generation remains gated.

A batch may prepare multiple compiled prompts, but no image is generated until the user explicitly opens the image gate for a named plate or named set of plates.

After each image generation, that plate's image gate closes.

Generated images remain candidates until output QC and explicit approval.

## Recommended Pack Workflow

### Stage 01 - Pack Selection

User approves the next roadmap pack.

Example:

`Lock Pack A for text production.`

### Stage 02 - Spec Draft Batch

Codex creates one object specification per plate.

Output folder:

`11_OBJECT_SPECIFICATIONS/`

### Stage 03 - Object QC Batch

Codex creates one QC sheet per object specification.

Output folder:

`11_OBJECT_SPECIFICATIONS/`

### Stage 04 - Compiled Prompt Batch

Codex compiles one image prompt per passed object specification.

Output folder:

`12_COMPILER_PROMPTS/`

### Stage 05 - Compiled Prompt QC Batch

Codex creates one compiled prompt QC sheet per prompt.

Output folder:

`12_COMPILER_PROMPTS/`

### Stage 06 - Pack Review Sheet

Codex creates one pack-level review sheet summarizing:

- object status
- source status
- diagram family
- required labels
- forbidden concepts
- generation risks
- recommended image-gate order

Output folder:

`13_ROADMAPS/`

### Stage 07 - User Review

User approves, revises, or rejects each object and compiled prompt.

Approval may happen per object or per pack.

### Stage 08 - Image Gate

User opens the image gate for one named plate or a named set.

Codex generates only the approved plate or set.

### Stage 09 - Output QC

Codex preserves each candidate image, runs output QC, and recommends:

- approve
- revise
- reject
- archive as failure mode

### Stage 10 - Approval Lock

User approval moves the output to:

`08_APPROVED_OUTPUTS/`

Codex creates the approval receipt and updates the roadmap status.

## Batch Pack Order

| Pack | Plates | Theme | Batch Size |
|---|---:|---|---:|
| Pack A | P011-P015 | Governance and authority | 5 |
| Pack B | P016-P020 | Memory ecology | 5 |
| Pack C | P021-P024 | Engines and registries | 4 |
| Pack D | P025-P028 | Capabilities | 4 |
| Pack E | P029-P034 | States, uncertainty, and failure | 6 |
| Pack F | P035-P040 | Stewardship, implementation, and index | 6 |

## Pack A Execution Template

When Pack A is approved for text production, Codex should create:

- `GFVP-OBJ-P011-DECISION_v0-1.md`
- `GFVP-OBJ-P011-DECISION_OBJECT_QC_v0-1.md`
- `GFVP-COMPILED-P011-DECISION_PROMPT_v0-1.md`
- `GFVP-COMPILED-P011-DECISION_QC_v0-1.md`

Repeat the same pattern for:

- P012 Institutional Decision Record
- P013 Validation Gate
- P014 Promotion Gate
- P015 Canon Boundary

Then create:

- `GFVP_PACK_A_REVIEW_SHEET_v0-1.md`
- `GFVP_PACK_A_TEXT_PRODUCTION_RECEIPT.md`

## Safeguards

No broad prompt packet may be used for generation if an object specification does not exist.

No synthesis plate may be generated before its component plates have been approved.

No generated image may be moved to approved outputs without explicit user approval.

No approved output may be called canon by default.

No automation may ratify constitutional change.

