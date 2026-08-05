# Render Authorization Protocol v1.0

Before execution, verify:

- the specification is frozen and schema-valid;
- its checksum matches the authorization record;
- the record states `APPROVED_FOR_RENDER`;
- page and issue scope match the requested jobs;
- prohibited pages remain excluded;
- the renderer receives visual-only prompts.

When any check fails, materialize only non-executing job packets with status `BLOCKED`. Do not call a model, broaden scope, or infer approval from previous issues.
