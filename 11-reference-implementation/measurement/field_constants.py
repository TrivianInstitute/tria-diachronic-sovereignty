"""Semantic validation for Rosetta 2.0 field-constant snapshots."""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class FieldConstantSnapshot:
    reciprocity: float
    embodiment: float
    non_domination: float
    emergence_raw: float
    rcd: float
    qualified_emergence: float


def validate_snapshot(snapshot: FieldConstantSnapshot, *, tolerance: float = 1e-9) -> None:
    """Reject internally inconsistent derived values.

    JSON Schema can validate shape and range, but it cannot enforce the
    multiplicative relation. This semantic validator closes that boundary.
    """

    values = (
        snapshot.reciprocity,
        snapshot.embodiment,
        snapshot.non_domination,
        snapshot.emergence_raw,
        snapshot.rcd,
        snapshot.qualified_emergence,
    )
    if any(not 0.0 <= value <= 1.0 for value in values):
        raise ValueError("field-constant snapshot values must be in [0, 1]")

    expected_rcd = snapshot.reciprocity * snapshot.embodiment * snapshot.non_domination
    if not isclose(snapshot.rcd, expected_rcd, abs_tol=tolerance):
        raise ValueError("rcd does not equal reciprocity * embodiment * non_domination")

    expected_emergence = expected_rcd * snapshot.emergence_raw
    if not isclose(snapshot.qualified_emergence, expected_emergence, abs_tol=tolerance):
        raise ValueError("qualified_emergence does not equal rcd * emergence_raw")
