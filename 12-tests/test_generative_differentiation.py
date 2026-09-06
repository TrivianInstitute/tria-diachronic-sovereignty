from metabolism.generative_differentiation import (
    TemporalModeObservation,
    renewal_failure,
)
from metabolism.metabolism import RelationalPhase


def test_mode_count_and_run_length_are_explicit():
    obs = TemporalModeObservation(
        history=(RelationalPhase.ENGAGE, RelationalPhase.DEEPEN, RelationalPhase.DEEPEN),
        accessible_modes=frozenset({RelationalPhase.STABILIZE, RelationalPhase.REST}),
    )
    assert obs.observed_mode_count == 2
    assert obs.current_run_length == 2


def test_persistence_with_real_alternatives_is_not_lock_in():
    obs = TemporalModeObservation(
        history=(RelationalPhase.DEEPEN,) * 8,
        accessible_modes=frozenset({RelationalPhase.STABILIZE, RelationalPhase.REST}),
    )
    assert not obs.optimization_lock_in(max_same_mode_run=3)


def test_persistence_plus_loss_of_alternatives_is_lock_in():
    obs = TemporalModeObservation(
        history=(RelationalPhase.DEEPEN,) * 8,
        accessible_modes=frozenset({RelationalPhase.DEEPEN}),
    )
    assert obs.optimization_lock_in(max_same_mode_run=3)


def test_dormancy_is_not_failure_when_renewal_or_exit_is_accessible():
    obs = TemporalModeObservation(
        history=(RelationalPhase.DORMANT,) * 20,
        accessible_modes=frozenset({RelationalPhase.RENEW, RelationalPhase.DISSOLVE}),
    )
    assert not obs.optimization_lock_in(max_same_mode_run=3)


def test_dormancy_can_be_lock_in_when_no_alternative_is_accessible():
    obs = TemporalModeObservation(
        history=(RelationalPhase.DORMANT,) * 20,
        accessible_modes=frozenset({RelationalPhase.DORMANT}),
    )
    assert obs.optimization_lock_in(max_same_mode_run=3)


def test_renewal_failure_requires_an_attempt():
    assert not renewal_failure(
        attempted=False,
        differentiation_before=0.2,
        differentiation_after=0.1,
    )


def test_renewal_failure_detects_no_restoration():
    assert renewal_failure(
        attempted=True,
        differentiation_before=0.2,
        differentiation_after=0.2,
        minimum_gain=0.05,
    )
    assert not renewal_failure(
        attempted=True,
        differentiation_before=0.2,
        differentiation_after=0.5,
        minimum_gain=0.05,
    )
