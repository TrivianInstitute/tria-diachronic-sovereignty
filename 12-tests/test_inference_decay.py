from epistemics.claims import ClaimType, EpistemicClaim


def test_inference_model_has_no_required_universal_decay_score():
    claim = EpistemicClaim(
        relationship_id="rel-1",
        claim_type=ClaimType.INFERENCE,
        subject="preference",
        content={"maybe": "prefers shorter sessions"},
        asserted_by="agent-a",
        provenance_refs=("obs-1",),
    )

    assert claim.claim_type == ClaimType.INFERENCE
    assert not hasattr(claim, "decay_rate")
    assert not hasattr(claim, "half_life")
    assert not hasattr(claim, "confidence_threshold")


def test_repetition_does_not_change_epistemic_type():
    claim = EpistemicClaim(
        relationship_id="rel-1",
        claim_type=ClaimType.INFERENCE,
        subject="preference",
        content="prefers shorter sessions",
        asserted_by="agent-a",
    )

    repeated = (claim, claim, claim)
    assert all(item.claim_type == ClaimType.INFERENCE for item in repeated)
