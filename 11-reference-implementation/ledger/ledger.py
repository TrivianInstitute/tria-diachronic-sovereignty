from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable
from uuid import uuid4


OPERATIVE = "OPERATIVE"
PENDING = "PENDING"
REJECTED = "REJECTED"
SUPERSEDED = "SUPERSEDED"


@dataclass(frozen=True)
class LedgerEvent:
    relationship_id: str
    event_type: str
    actor: str
    state_domain: str
    payload: dict[str, Any]
    authorization_basis: str | None = None
    epistemic_status: str | None = None
    dispute_status: str | None = None
    effective_at: str | None = None
    projection_status: str = PENDING
    event_id: str = field(default_factory=lambda: str(uuid4()))
    recorded_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class RelationalLedger:
    """Minimal append-oriented event store.

    Recording an event does not imply that its content is true, agreed, authorized,
    or eligible to alter current operative state. Projection eligibility is explicit.
    This keeps historical provenance separable from current governance state.
    """

    def __init__(self) -> None:
        self._events: list[LedgerEvent] = []

    def append(self, event: LedgerEvent) -> LedgerEvent:
        if any(existing.event_id == event.event_id for existing in self._events):
            raise ValueError(f"duplicate event_id: {event.event_id}")
        if event.projection_status not in {OPERATIVE, PENDING, REJECTED, SUPERSEDED}:
            raise ValueError(f"unsupported projection_status: {event.projection_status}")
        self._events.append(event)
        return event

    def events(self, relationship_id: str | None = None) -> tuple[LedgerEvent, ...]:
        if relationship_id is None:
            return tuple(self._events)
        return tuple(
            event for event in self._events if event.relationship_id == relationship_id
        )

    def project(self, relationship_id: str) -> dict[str, Any]:
        """Project current operative state from explicitly operative events.

        This reference reducer is intentionally conservative: recorded, pending,
        rejected, or superseded events remain in history but do not alter the current
        projection. The reducer does not itself decide whether authorization or
        consent is legitimate; another governance process must mark an event OPERATIVE.

        Domain-specific reducers may replace this minimal last-operative-write model.
        """
        state: dict[str, Any] = {}
        for event in self.events(relationship_id):
            if event.projection_status != OPERATIVE:
                continue
            if event.event_type in {"REVOKE", "EXPIRE", "DELETE_PROJECTION"}:
                state.pop(event.state_domain, None)
            else:
                state[event.state_domain] = event.payload
        return state

    def extend(self, events: Iterable[LedgerEvent]) -> None:
        for event in events:
            self.append(event)
