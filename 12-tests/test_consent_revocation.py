from ledger.ledger import OPERATIVE, LedgerEvent, RelationalLedger


def test_revocation_removes_consent_from_current_projection_but_preserves_history():
    ledger = RelationalLedger()
    granted = LedgerEvent(
        relationship_id="rel-1",
        event_type="SET",
        actor="human",
        state_domain="consent:memory",
        payload={"status": "GRANTED", "scope": ["session-memory"]},
        authorization_basis="explicit-consent",
        projection_status=OPERATIVE,
    )
    revoked = LedgerEvent(
        relationship_id="rel-1",
        event_type="REVOKE",
        actor="human",
        state_domain="consent:memory",
        payload={"reason": "participant withdrew consent"},
        authorization_basis="participant-revocation",
        projection_status=OPERATIVE,
    )

    ledger.extend((granted, revoked))

    assert "consent:memory" not in ledger.project("rel-1")
    history = ledger.events("rel-1")
    assert history == (granted, revoked)


def test_revocation_does_not_affect_unrelated_state_domain():
    ledger = RelationalLedger()
    ledger.extend(
        (
            LedgerEvent(
                "rel-1",
                "SET",
                "human",
                "consent:memory",
                {"status": "GRANTED"},
                projection_status=OPERATIVE,
            ),
            LedgerEvent(
                "rel-1",
                "SET",
                "human",
                "authority:calendar",
                {"status": "LIMITED"},
                projection_status=OPERATIVE,
            ),
            LedgerEvent(
                "rel-1",
                "REVOKE",
                "human",
                "consent:memory",
                {},
                projection_status=OPERATIVE,
            ),
        )
    )

    projected = ledger.project("rel-1")
    assert "consent:memory" not in projected
    assert projected["authority:calendar"] == {"status": "LIMITED"}


def test_recorded_event_does_not_silently_become_operative_state():
    ledger = RelationalLedger()
    pending = LedgerEvent(
        relationship_id="rel-1",
        event_type="SET",
        actor="agent-a",
        state_domain="authority:calendar",
        payload={"status": "EXECUTE"},
    )
    ledger.append(pending)

    assert ledger.events("rel-1") == (pending,)
    assert ledger.project("rel-1") == {}
