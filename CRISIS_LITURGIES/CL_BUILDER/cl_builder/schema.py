from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


class SchemaValidationError(ValueError):
    def __init__(self, schema_name: str, errors: list[str]):
        super().__init__(f"{schema_name} validation failed: " + "; ".join(errors))
        self.schema_name = schema_name
        self.errors = errors


def _schema_path(schema_dir: Path, name: str) -> Path:
    return schema_dir / f"{name}.schema.json"


def load_schema(schema_dir: str | Path, name: str) -> dict[str, Any]:
    path = _schema_path(Path(schema_dir), name)
    return json.loads(path.read_text(encoding="utf-8"))


def validate_instance(instance: Any, schema_dir: str | Path, name: str) -> None:
    schema = load_schema(schema_dir, name)
    validator = Draft202012Validator(schema)
    failures = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        failures.append(f"{location}: {error.message}")
    if failures:
        raise SchemaValidationError(name, failures)
