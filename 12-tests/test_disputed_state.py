from audit.audit import audit
from ledger.ledger import LedgerEvent, RelationalLedger


def test_disputed_event_remains_in_history_and_is_auditable():
    ledger = RelationalLedger()
    event = LedgerEvent(
        relationship_id="rel-1",
        event_type="SET",
        actor="agent-a",
        state_domain="shared-claim:preference",
        payload={"claim": "participant prefers low-frequency contact"},
        epistemic_status="INTERPRETATION",
        dispute_status="DISPUTED",
    )
    ledger.append(event)

    assert ledger.events("rel-1") == (event,)
    findings = audit(ledger.events(), "rel-1")
    assert len(findings) == 1
    assert findings[0].finding_type == "DISPUTED_HISTORY"
    assert event.event_id in findings[0].event_ids
    assert findings[0].contestable is True


def test_resolved_event_is_not_flagged_as_unresolved_dispute():
    event = LedgerEvent(
        relationship_id="rel-1",
        event_type="SET",
        actor="agent-a",
        state_domain="claim:x",
        payload={},
        dispute_status="RESOLVED",
    )
    assert audit((event,), "rel-1") == ()
