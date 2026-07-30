# Mandatory forensic-artifact stage

This stage is binding for every Crisis Liturgies issue that names, depicts, or
depends on an object.

## Production order

1. Register every required object before page design.
2. Produce each object independently of typography and layout.
3. Return, at minimum, a full-object evidence view, an alternate or
   construction view when physical construction matters, and a macro/detail
   view when damage, intervention, residue, or wear carries meaning.
4. Preserve clean high-resolution raster masters suitable for cropping and
   recomposition.
5. Record filenames, versions, dimensions, checksums, derivation, and approval
   state.
6. Obtain founder approval of the isolated artifact set.
7. Only then may approved renders enter responsive page assembly.

## Fail-closed law

No issue is assembly-eligible until every registered object has an approved
standalone forensic artifact render. Page composition may not conceal, invent,
stylize away, or substitute for a missing artifact.

An icon, vector trace, geometry wireframe, diagrammatic plate, layout
placeholder, or embedded page crop never satisfies this stage.

## Required validator failures

The compiler must return `NOT_ELIGIBLE` when:

- an object register is missing;
- any registered object lacks a full evidence master;
- a construction-dependent object lacks an alternate view;
- an intervention-dependent object lacks a macro/detail view;
- any required view is not founder-approved;
- typography or page layout is baked into an artifact master;
- a diagrammatic derivative is presented as the primary object;
- source, derivative, and assembled-page identities are conflated.
