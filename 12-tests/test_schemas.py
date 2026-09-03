from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

SCHEMA_ROOT = Path(__file__).resolve().parents[1] / "10-specifications"
SCHEMA_FILES = sorted(SCHEMA_ROOT.glob("*.schema.json"))


def test_expected_schema_files_exist() -> None:
    expected = {
        "relational-state.schema.json",
        "epistemic-claim.schema.json",
        "consent.schema.json",
        "continuity-attestation.schema.json",
        "relational-phase.schema.json",
        "failure-event.schema.json",
    }
    assert {path.name for path in SCHEMA_FILES} == expected


def test_all_schemas_are_valid_draft_2020_12_schemas() -> None:
    for path in SCHEMA_FILES:
        schema = json.loads(path.read_text(encoding="utf-8"))
        assert schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema"
        Draft202012Validator.check_schema(schema)


def test_schema_descriptions_do_not_claim_truth_or_validation() -> None:
    """Structural validity must not be presented as epistemic or governance validity."""
    combined = "\n".join(path.read_text(encoding="utf-8") for path in SCHEMA_FILES).lower()
    assert "valid json" not in combined or "does not" in combined
    assert "production validated" not in combined
