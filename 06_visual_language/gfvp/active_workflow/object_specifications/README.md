# GFVP Object Specifications

Status: Active production doctrine / Sandbox
Date: 2026-07-03
Package: Gradient Foundational Visual Package

## Purpose

GFVP Object Specifications define the institutional object before any image prompt is written.

The object specification is the source of truth.

The image prompt is a compiler output.

## Production Rule

Generate images only from completed object specifications.

Never generate images directly from conversational prompts, improvised creative briefs, broad plate summaries, or QC discussion.

## Reason

The staged generation process revealed a failure mode: image models can drift upward into the production conversation, QC process, prompt architecture, or workflow instead of rendering the institutional object.

Object specifications prevent this by separating:

- the Gradient object being depicted
- the visual package that renders it
- the production pipeline that creates it
- the conversation that discusses it

## Required Flow

1. Complete object specification.
2. QC object specification.
3. Compile image prompt from object specification.
4. QC compiler prompt.
5. Open image gate for that object only.
6. Generate image.
7. QC output.
8. Archive, reject, revise, or approve.

