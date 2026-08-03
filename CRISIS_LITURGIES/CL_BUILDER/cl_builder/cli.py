from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .assembly import assemble_volume_pdf
from .calibration import calibrate_directory
from .compiler import CompileError, compile_volume
from .io import BuilderIOError, dump_json, load_structured
from .qc import inspect_image
from .renderer import ManifestRendererAdapter, RenderAuthorizationError, ingest_rendered_asset
from .schema import SchemaValidationError, validate_instance


def default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def cmd_validate(args: argparse.Namespace) -> int:
    root = default_root()
    volume = load_structured(args.volume)
    validate_instance(volume, root / "schemas", "volume")
    profile = load_structured(root / "profiles" / f"{volume['release_profile']}.yaml")
    compiled = compile_volume(volume, profile)
    for page in volume["pages"]:
        validate_instance(page, root / "schemas", "page")
    for packet in compiled["render_packets"]:
        validate_instance(packet, root / "schemas", "render-packet")
    print(f"PASS: {volume['volume_id']} — {len(volume['pages'])} pages validated")
    return 0


def cmd_compile(args: argparse.Namespace) -> int:
    root = default_root()
    volume = load_structured(args.volume)
    validate_instance(volume, root / "schemas", "volume")
    profile = load_structured(root / "profiles" / f"{volume['release_profile']}.yaml")
    compiled = compile_volume(volume, profile)
    for packet in compiled["render_packets"]:
        validate_instance(packet, root / "schemas", "render-packet")
    dump_json(compiled, args.output)
    print(f"COMPILED: {compiled['page_count']} render packets → {args.output}")
    return 0


def cmd_preflight(args: argparse.Namespace) -> int:
    root = default_root()
    volume = load_structured(args.volume)
    validate_instance(volume, root / "schemas", "volume")
    profile = load_structured(root / "profiles" / f"{volume['release_profile']}.yaml")
    compiled = compile_volume(volume, profile)
    report = {
        "status": "PASS" if compiled["page_count"] == 48 else "FAIL",
        "volume_id": volume["volume_id"],
        "state": volume["state"],
        "render_authorized": compiled["render_authorized"],
        "page_count": compiled["page_count"],
        "volume_spec_sha256": compiled["volume_spec_sha256"],
        "compiled_sha256": compiled["compiled_sha256"],
        "blockers": [] if compiled["render_authorized"] else ["APPROVED_FOR_RENDER"],
    }
    dump_json(report, args.output)
    print(f"PREFLIGHT {report['status']}: {args.output}")
    return 0


def cmd_qc_image(args: argparse.Namespace) -> int:
    root = default_root()
    volume = load_structured(args.volume)
    profile = load_structured(root / "profiles" / f"{volume['release_profile']}.yaml")
    result = inspect_image(args.image, profile["qc"], volume["canvas"])
    dump_json(result.to_dict(), args.output)
    print(("PASS" if result.passed else "FAIL") + f": {args.image}")
    return 0 if result.passed else 2


def cmd_calibrate(args: argparse.Namespace) -> int:
    profile = load_structured(args.profile)
    report = calibrate_directory(args.images, profile["qc"], args.source_document)
    dump_json(report, args.output)
    print(f"CALIBRATED: {report['corpus_page_count']} pages → {args.output}")
    return 0


def cmd_render_plan(args: argparse.Namespace) -> int:
    root = default_root()
    volume = load_structured(args.volume)
    profile = load_structured(root / "profiles" / f"{volume['release_profile']}.yaml")
    compiled = compile_volume(volume, profile)
    index = ManifestRendererAdapter().materialize(compiled, args.output_dir)
    print(f"RENDER PLAN {index['execution_status']}: {args.output_dir}")
    return 0


def cmd_assemble(args: argparse.Namespace) -> int:
    root = default_root()
    volume = load_structured(args.volume)
    manuscript = Path(args.manuscript).read_text(encoding="utf-8-sig")
    manifest = assemble_volume_pdf(volume, manuscript, args.assets, args.output, args.manifest)
    validate_instance(manifest, root / "schemas", "assembly-manifest")
    print(f"ASSEMBLED: {manifest['page_count']} pages → {args.output}")
    return 0


def cmd_ingest_result(args: argparse.Namespace) -> int:
    root = default_root()
    packet = load_structured(args.packet)
    validate_instance(packet, root / "schemas", "render-packet")
    receipt = ingest_rendered_asset(packet, args.image, args.accepted_dir, args.receipt)
    validate_instance(receipt.to_dict(), root / "schemas", "render-receipt")
    print(f"{receipt.status}: {receipt.asset_id} → {args.receipt}")
    return 0 if receipt.status == "ACCEPTED" else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cl-builder")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("volume")
    validate.set_defaults(func=cmd_validate)

    compile_cmd = sub.add_parser("compile")
    compile_cmd.add_argument("volume")
    compile_cmd.add_argument("--output", required=True)
    compile_cmd.set_defaults(func=cmd_compile)

    preflight = sub.add_parser("preflight")
    preflight.add_argument("volume")
    preflight.add_argument("--output", required=True)
    preflight.set_defaults(func=cmd_preflight)

    qc = sub.add_parser("qc-image")
    qc.add_argument("volume")
    qc.add_argument("image")
    qc.add_argument("--output", required=True)
    qc.set_defaults(func=cmd_qc_image)

    calibrate = sub.add_parser("calibrate")
    calibrate.add_argument("images")
    calibrate.add_argument("--profile", required=True)
    calibrate.add_argument("--source-document")
    calibrate.add_argument("--output", required=True)
    calibrate.set_defaults(func=cmd_calibrate)

    render_plan = sub.add_parser("render-plan")
    render_plan.add_argument("volume")
    render_plan.add_argument("--output-dir", required=True)
    render_plan.set_defaults(func=cmd_render_plan)

    assemble = sub.add_parser("assemble")
    assemble.add_argument("volume")
    assemble.add_argument("--manuscript", required=True)
    assemble.add_argument("--assets", required=True)
    assemble.add_argument("--output", required=True)
    assemble.add_argument("--manifest", required=True)
    assemble.set_defaults(func=cmd_assemble)

    ingest = sub.add_parser("ingest-result")
    ingest.add_argument("packet")
    ingest.add_argument("image")
    ingest.add_argument("--accepted-dir", required=True)
    ingest.add_argument("--receipt", required=True)
    ingest.set_defaults(func=cmd_ingest_result)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (BuilderIOError, SchemaValidationError, CompileError, RenderAuthorizationError, OSError, KeyError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
