import pytest

from measurement.field_constants import FieldConstantSnapshot, validate_snapshot


def test_valid_multiplicative_snapshot_is_accepted():
    validate_snapshot(FieldConstantSnapshot(0.8, 0.5, 0.25, 0.9, 0.1, 0.09))


def test_additive_or_fabricated_rcd_is_rejected():
    with pytest.raises(ValueError, match="rcd does not equal"):
        validate_snapshot(FieldConstantSnapshot(1.0, 0.0, 1.0, 1.0, 0.75, 0.75))


def test_emergence_cannot_remain_qualified_after_dependency_collapse():
    with pytest.raises(ValueError, match="qualified_emergence does not equal"):
        validate_snapshot(FieldConstantSnapshot(1.0, 0.0, 1.0, 1.0, 0.0, 1.0))
