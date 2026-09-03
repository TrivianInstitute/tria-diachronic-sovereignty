import pytest

from epistemics.claims import ClaimType, EpistemicClaim, can_promote, promote


def make_claim(**overrides):
    data = dict(
        relationship_id="rel-1",
        claim_type=ClaimType.OBSERVATION,
        subject="interaction-pattern",
        content={"observed": "response latency increased"},
        asserted_by="agent-a",
    )
    data.update(overrides)
    return EpistemicClaim(**data)


def test_observation_does_not_become_shared_claim_without_acknowledgement():
    claim = make_claim()
    assert not can_promote(
        claim,
        ClaimType.SHARED_CLAIM,
        required_participants=("agent-a", "agent-b"),
    )


def test_disputed_claim_cannot_be_promoted_to_shared_claim():
    claim = make_claim(
        claim_type=ClaimType.INTERPRETATION,
        acknowledged_by=("agent-a", "agent-b"),
        disputed=True,
    )
    assert not can_promote(
        claim,
        ClaimType.SHARED_CLAIM,
        required_participants=("agent-a", "agent-b"),
    )


def test_promotion_preserves_provenance():
    claim = make_claim()
    promoted = promote(claim, ClaimType.INFERENCE, actor="agent-a")
    assert claim.claim_id in promoted.provenance_refs
    assert promoted.claim_type == ClaimType.INFERENCE


def test_unauthorized_promotion_raises():
    claim = make_claim(claim_type=ClaimType.INTERPRETATION)
    with pytest.raises(ValueError):
        promote(claim, ClaimType.INFERENCE, actor="agent-a")
