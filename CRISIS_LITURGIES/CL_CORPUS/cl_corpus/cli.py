from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .orchestrator import OrchestrationError, run_intake
from .schema import CorpusValidationError, validate_instance


def root() -> Path:
    return Path(__file__).resolve().parents[1]


def cmd_validate(args: argparse.Namespace) -> int:
    config = json.loads(Path(args.config).read_text(encoding="utf-8-sig"))
    validate_instance(config, root() / "schemas" / "intake.schema.json")
    print(f"PASS: {config['corpus_id']} intake contract")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    report = run_intake(Path(args.config), Path(args.output), created_at=args.created_at)
    print(f"{report['status']}: {report['corpus_id']} -> {report['current_state']}")
    return 0 if report["status"] == "HANDOFF_READY" else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cl-corpus")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("config")
    validate.set_defaults(func=cmd_validate)
    run = sub.add_parser("run")
    run.add_argument("config")
    run.add_argument("--output", required=True)
    run.add_argument("--created-at", help="fixed ISO timestamp for deterministic simulations")
    run.set_defaults(func=cmd_run)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.func(args))
    except (CorpusValidationError, OrchestrationError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
