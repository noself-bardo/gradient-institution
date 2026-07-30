#!/usr/bin/env python3
"""Fail-closed preflight for the Systems Visualizer baseline branch."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIGRATIONS = ROOT / "migrations"

EXPECTED_HASHES = {
    "20260701165820_000_recovered_pre_ledger_public_schema.sql":
        "6cb87f02bc78c9299d39a74be57e9a242af5e3776d0013b57672aada19c5f548",
    "20260701165821_001_gradient_platform_foundation_systems_visualizer.sql":
        "68e719f5f43a370ea6f00942c696a20f718c05db34b2d7594882c9f0d1be7b8b",
    "20260701165844_002_gradient_platform_foundation_hardening.sql":
        "749c2482586a08f161c2c1462fb68497425c799b95743a79f63bbf1f5381c727",
    "20260701165947_003_gradient_authenticated_read_policies.sql":
        "2fe046413ff6296a5992854a0a45000103e2828ad94985610ccbb258b2032211",
}

RUNTIME_TABLES = {
    "workflow_run",
    "source_object",
    "source_segment",
    "evidence_item",
    "derivative_item",
    "decision_item",
    "activity_event",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


actual_names = sorted(path.name for path in MIGRATIONS.glob("*.sql"))
expected_names = sorted(EXPECTED_HASHES)
if actual_names != expected_names:
    fail(f"migration chain changed: expected {expected_names}, found {actual_names}")

combined_sql = ""
for name, expected_hash in EXPECTED_HASHES.items():
    data = (MIGRATIONS / name).read_bytes()
    actual_hash = hashlib.sha256(data).hexdigest()
    if actual_hash != expected_hash:
        fail(f"hash mismatch for {name}: {actual_hash}")
    combined_sql += data.decode("utf-8")

config = (ROOT / "config.toml").read_text(encoding="utf-8")
if "[storage.buckets.visual-systems-assets]" not in config:
    fail("private bucket declaration is missing")
if "public = false" not in config:
    fail("private bucket is not explicitly private")
for forbidden in ("file_size_limit", "allowed_mime_types", "objects_path"):
    if forbidden in config:
        fail(f"bucket no longer preserves the platform default for {forbidden}")

for table in RUNTIME_TABLES:
    if table in combined_sql:
        fail(f"runtime-table stop gate violated by {table}")

print("PASS: four migrations, private empty bucket, zero runtime tables")
