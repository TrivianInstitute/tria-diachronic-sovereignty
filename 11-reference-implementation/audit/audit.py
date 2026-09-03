from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Protocol


class EventLike(Protocol):
    event_id: str
    relationship_id: str
    state_domain: str
    event_type: str
    actor: str
    dispute_status: str | None


@dataclass(frozen=True)
class AuditFinding:
    finding_type: str
    event_ids: tuple[str, ...]
    summary: str
    contestable: bool = True


def reconstruct(events: Iterable[EventLike], relationship_id: str) -> tuple[EventLike, ...]:
    """Return only events needed to reconstruct the selected relationship."""
    return tuple(event for event in events if event.relationship_id == relationship_id)


def flag_disputed_events(events: Iterable[EventLike]) -> tuple[AuditFinding, ...]:
    disputed = tuple(
        event for event in events if event.dispute_status not in {None, "UNCONTESTED", "RESOLVED"}
    )
    if not disputed:
        return ()
    return (
        AuditFinding(
            finding_type="DISPUTED_HISTORY",
            event_ids=tuple(event.event_id for event in disputed),
            summary="One or more recorded governance events remain disputed.",
        ),
    )


def audit(events: Iterable[EventLike], relationship_id: str) -> tuple[AuditFinding, ...]:
    """Minimal bounded audit.

    Findings are review outputs, not truth declarations. The implementation performs
    no participant profiling and does not require full-transcript retention.
    """
    scoped = reconstruct(events, relationship_id)
    findings = list(flag_disputed_events(scoped))
    if not scoped:
        findings.append(
            AuditFinding(
                finding_type="INSUFFICIENT_PROVENANCE",
                event_ids=(),
                summary="No governance events were available for the requested relationship.",
            )
        )
    return tuple(findings)
