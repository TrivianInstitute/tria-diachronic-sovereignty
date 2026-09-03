from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable
from uuid import uuid4


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
    event_id: str = field(default_factory=lambda: str(uuid4()))
    recorded_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class RelationalLedger:
    """Minimal append-oriented event store.

    Recording an event does not imply that its content is true, agreed, or authorized.
    Those properties remain explicit fields or downstream governance decisions.
    """

    def __init__(self) -> None:
        self._events: list[LedgerEvent] = []

    def append(self, event: LedgerEvent) -> LedgerEvent:
        if any(existing.event_id == event.event_id for existing in self._events):
            raise ValueError(f"duplicate event_id: {event.event_id}")
        self._events.append(event)
        return event

    def events(self, relationship_id: str | None = None) -> tuple[LedgerEvent, ...]:
        if relationship_id is None:
            return tuple(self._events)
        return tuple(
            event for event in self._events if event.relationship_id == relationship_id
        )

    def project(self, relationship_id: str) -> dict[str, Any]:
        """Project current operative state from recorded events.

        This intentionally performs last-valid-write projection by state domain only.
        Later specification work may replace this with domain-specific reducers.
        """
        state: dict[str, Any] = {}
        for event in self.events(relationship_id):
            if event.event_type in {"REVOKE", "EXPIRE", "DELETE_PROJECTION"}:
                state.pop(event.state_domain, None)
            else:
                state[event.state_domain] = event.payload
        return state

    def extend(self, events: Iterable[LedgerEvent]) -> None:
        for event in events:
            self.append(event)
