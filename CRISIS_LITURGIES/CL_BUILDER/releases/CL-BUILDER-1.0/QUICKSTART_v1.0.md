# Quickstart v1.0

From the release directory:

```bash
python -m venv .venv
.venv/bin/python -m pip install -e source
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/cl-builder validate examples/four-page-volume.json
.venv/bin/cl-builder preflight examples/four-page-volume.json --output /tmp/cl-builder-preflight.json
.venv/bin/cl-builder render-plan examples/four-page-volume.json --output-dir /tmp/cl-builder-render-plan
```

Expected state:

- validation passes;
- preflight passes the structural invariant;
- `render_authorized` is false;
- render planning produces non-executing job packets;
- no image service is called.

For production, replace the example with a frozen, schema-valid volume specification and obtain a durable `APPROVED_FOR_RENDER` record before any external execution. Stop on checksum, authority, schema, or custody conflict.
