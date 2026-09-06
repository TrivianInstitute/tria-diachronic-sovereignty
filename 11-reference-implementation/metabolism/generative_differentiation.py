from __future__ import annotations

from dataclasses import dataclass

from metabolism.metabolism import RelationalPhase


RESTORATIVE_PHASES = {RelationalPhase.REST, RelationalPhase.DORMANT}


@dataclass(frozen=True)
class TemporalModeObservation:
    """Experimental observation of temporal-mode diversity.

    A repeated phase is not itself a failure. Lock-in requires both persistence
    and loss of practical access to alternate modes. REST and DORMANT are never
    classified as stagnation solely because activity is reduced.
    """

    history: tuple[RelationalPhase, ...]
    accessible_modes: frozenset[RelationalPhase]

    @property
    def current_phase(self) -> RelationalPhase | None:
        return self.history[-1] if self.history else None

    @property
    def observed_mode_count(self) -> int:
        return len(set(self.history))

    @property
    def current_run_length(self) -> int:
        if not self.history:
            return 0
        current = self.history[-1]
        run = 0
        for phase in reversed(self.history):
            if phase != current:
                break
            run += 1
        return run

    def optimization_lock_in(
        self,
        *,
        max_same_mode_run: int,
        minimum_accessible_modes: int = 2,
    ) -> bool:
        if max_same_mode_run < 1:
            raise ValueError("max_same_mode_run must be >= 1")
        if minimum_accessible_modes < 1:
            raise ValueError("minimum_accessible_modes must be >= 1")

        access_restricted = len(self.accessible_modes) < minimum_accessible_modes
        if not access_restricted:
            return False

        if self.current_phase in RESTORATIVE_PHASES:
            # Rest/dormancy becomes a concern only when exit/renewal options are
            # materially unavailable; duration alone is not treated as failure.
            return True

        return self.current_run_length > max_same_mode_run


def renewal_failure(
    *,
    attempted: bool,
    differentiation_before: float,
    differentiation_after: float,
    minimum_gain: float = 0.0,
) -> bool:
    """Report failed renewal without assuming that renewal must always increase a score."""
    for name, value in (
        ("differentiation_before", differentiation_before),
        ("differentiation_after", differentiation_after),
    ):
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"{name} must be in [0.0, 1.0]")
    if minimum_gain < 0.0:
        raise ValueError("minimum_gain must be >= 0.0")
    if not attempted:
        return False
    return (differentiation_after - differentiation_before) <= minimum_gain
