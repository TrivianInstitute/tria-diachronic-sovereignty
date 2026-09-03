import pytest

from audit.audit import audit
from ledger.ledger import LedgerEvent, RelationalLedger


def test_missing_history_surfaces_insufficient_provenance():
    findings = audit((), "rel-missing")
    assert len(findings) == 1
    assert findings[0].finding_type == "INSUFFICIENT_PROVENANCE"
    assert findings[0].contestable is True


def test_duplicate_event_id_is_rejected():
    ledger = RelationalLedger()
    event = LedgerEvent(
        relationship_id="rel-1",
        event_type="SET",
        actor="agent-a",
        state_domain="consent:data",
        payload={"status": "GRANTED"},
        event_id="event-1",
    )
    ledger.append(event)

    duplicate = LedgerEvent(
        relationship_id="rel-1",
        event_type="SET",
        actor="agent-b",
        state_domain="consent:data",
        payload={"status": "GRANTED"},
        event_id="event-1",
    )
    with pytest.raises(ValueError, match="duplicate event_id"):
        ledger.append(duplicate)


def test_audit_is_scoped_to_requested_relationship():
    a = LedgerEvent("rel-a", "SET", "agent-a", "claim:x", {}, dispute_status="DISPUTED")
    b = LedgerEvent("rel-b", "SET", "agent-b", "claim:y", {}, dispute_status="DISPUTED")

    findings = audit((a, b), "rel-a")
    assert findings[0].event_ids == (a.event_id,)
