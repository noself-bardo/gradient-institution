# GFVP Object Schema v0.1

Status: Sandbox / Candidate Production Doctrine
Date: 2026-07-03
Package: Gradient Foundational Visual Package

## Core Rule

One object specification equals one institutional object.

One image renders one completed object specification.

The image prompt is a compiler, not a creative brief.

## Required Fields

### Object ID

Unique identifier.

Example: `GFVP-OBJ-P002-ADMISSION-GATE`

### Object Name

The exact institutional object being depicted.

Example: `Admission Gate`

### Purpose

What the object explains in one or two sentences.

### Constitutional Role

How the object serves The Gradient's constitutional architecture.

### Boundaries

What the object is and is not.

This must include the abstraction level being depicted.

### Inputs / Outputs

Inputs: what enters the object.

Outputs: what leaves the object.

The object must not imply outputs that are outside its authority.

### Required Labels

Exact labels that must appear or be structurally represented.

### Forbidden Concepts

Concepts, words, diagrams, visual metaphors, and institutional claims that must not appear.

### Diagram Family

Allowed diagram family for this object.

Examples:

- gate
- ledger
- matrix
- organ map
- stack
- loop
- state machine
- split-field

### Visual Center

The one visual center of the image.

This prevents the image model from creating multiple competing centers.

### Negative Prompt

Explicit visual and conceptual exclusions.

### Compiler Notes

Instructions for converting the object spec into an image prompt.

Compiler notes must be mechanical, not poetic.

### QC Requirements

Pass/fail criteria specific to this object.

## Forbidden Source Behavior

The object spec must not derive from:

- chat discussion alone
- latest conversational topic
- prompt engineering process
- QC process
- image gate process
- production workflow
- visual vibes

The object spec must derive from named Gradient source material.

## Prompt Compiler Rule

The compiled prompt must begin from the object, not the conversation.

The compiled prompt must explicitly say:

You are rendering the institutional object named in this specification.

You are not rendering the production process, prompt architecture, QC process, image gate, this conversation, or the document family itself.

