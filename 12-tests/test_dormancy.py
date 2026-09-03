import pytest

from metabolism.metabolism import RelationalPhase, can_transition, transition


def test_rest_can_transition_to_dormancy():
    assert can_transition(RelationalPhase.REST, RelationalPhase.DORMANT) is True
    assert transition(RelationalPhase.REST, RelationalPhase.DORMANT) == RelationalPhase.DORMANT


def test_dormancy_can_return_through_renewal():
    assert can_transition(RelationalPhase.DORMANT, RelationalPhase.RENEW) is True


def test_dormancy_does_not_imply_forced_deepening():
    assert can_transition(RelationalPhase.DORMANT, RelationalPhase.DEEPEN) is False
    with pytest.raises(ValueError):
        transition(RelationalPhase.DORMANT, RelationalPhase.DEEPEN)


def test_dissolution_is_legitimate_from_dormancy():
    assert transition(RelationalPhase.DORMANT, RelationalPhase.DISSOLVE) == RelationalPhase.DISSOLVE
