from __future__ import annotations

from enum import Enum


class RelationalPhase(str, Enum):
    ENGAGE = "ENGAGE"
    DEEPEN = "DEEPEN"
    STABILIZE = "STABILIZE"
    REST = "REST"
    DORMANT = "DORMANT"
    RENEW = "RENEW"
    TRANSFORM = "TRANSFORM"
    DISSOLVE = "DISSOLVE"


ALLOWED_TRANSITIONS: dict[RelationalPhase, set[RelationalPhase]] = {
    RelationalPhase.ENGAGE: {RelationalPhase.DEEPEN, RelationalPhase.REST, RelationalPhase.DISSOLVE},
    RelationalPhase.DEEPEN: {RelationalPhase.STABILIZE, RelationalPhase.REST, RelationalPhase.TRANSFORM, RelationalPhase.DISSOLVE},
    RelationalPhase.STABILIZE: {RelationalPhase.REST, RelationalPhase.RENEW, RelationalPhase.TRANSFORM, RelationalPhase.DISSOLVE},
    RelationalPhase.REST: {RelationalPhase.RENEW, RelationalPhase.DORMANT, RelationalPhase.DISSOLVE},
    RelationalPhase.DORMANT: {RelationalPhase.RENEW, RelationalPhase.DISSOLVE},
    RelationalPhase.RENEW: {RelationalPhase.ENGAGE, RelationalPhase.STABILIZE, RelationalPhase.TRANSFORM, RelationalPhase.DISSOLVE},
    RelationalPhase.TRANSFORM: {RelationalPhase.STABILIZE, RelationalPhase.REST, RelationalPhase.DISSOLVE},
    RelationalPhase.DISSOLVE: set(),
}


def can_transition(current: RelationalPhase, target: RelationalPhase) -> bool:
    if current == target:
        return True
    return target in ALLOWED_TRANSITIONS[current]


def transition(current: RelationalPhase, target: RelationalPhase) -> RelationalPhase:
    """Apply a candidate lifecycle transition.

    No phase is defined as healthier, more intimate, or more successful than another.
    In particular, REST, DORMANT, and DISSOLVE are legitimate governance outcomes.
    """
    if not can_transition(current, target):
        raise ValueError(f"unsupported relational phase transition: {current} -> {target}")
    return target
