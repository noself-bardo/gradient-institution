from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


class BuilderIOError(RuntimeError):
    pass


def load_structured(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    if not source.exists():
        raise BuilderIOError(f"File does not exist: {source}")
    try:
        text = source.read_text(encoding="utf-8")
        if source.suffix.lower() in {".yaml", ".yml"}:
            data = yaml.safe_load(text)
        elif source.suffix.lower() == ".json":
            data = json.loads(text)
        else:
            raise BuilderIOError(f"Unsupported structured file type: {source.suffix}")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        raise BuilderIOError(f"Could not read {source}: {exc}") from exc
    if not isinstance(data, dict):
        raise BuilderIOError(f"Top-level value must be an object: {source}")
    return data


def dump_yaml(data: Any, path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )


def dump_json(data: Any, path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
