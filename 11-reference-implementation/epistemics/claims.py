from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class ClaimType(str, Enum):
    OBSERVATION = "OBSERVATION"
    INFERENCE = "INFERENCE"
    INTERPRETATION = "INTERPRETATION"
    SHARED_CLAIM = "SHARED_CLAIM"


@dataclass(frozen=True)
class EpistemicClaim:
    relationship_id: str
    claim_type: ClaimType
    subject: str
    content: Any
    asserted_by: str
    provenance_refs: tuple[str, ...] = ()
    acknowledged_by: tuple[str, ...] = ()
    disputed: bool = False
    claim_id: str = field(default_factory=lambda: str(uuid4()))


def can_promote(
    claim: EpistemicClaim,
    target: ClaimType,
    *,
    required_participants: tuple[str, ...] = (),
) -> bool:
    """Return whether an explicit epistemic promotion is admissible.

    The function deliberately does not use confidence scores. A Shared Claim requires
    an explicitly defined non-empty participant scope and acknowledgement by every
    participant required for that scope. An omitted scope fails closed.
    """
    if claim.claim_type == target:
        return True

    if target == ClaimType.SHARED_CLAIM:
        if claim.disputed or not required_participants:
            return False
        required = set(required_participants)
        acknowledged = set(claim.acknowledged_by)
        return required.issubset(acknowledged)

    allowed = {
        ClaimType.OBSERVATION: {ClaimType.INFERENCE, ClaimType.INTERPRETATION},
        ClaimType.INFERENCE: {ClaimType.INTERPRETATION},
        ClaimType.INTERPRETATION: set(),
        ClaimType.SHARED_CLAIM: set(),
    }
    return target in allowed[claim.claim_type]


def promote(
    claim: EpistemicClaim,
    target: ClaimType,
    *,
    actor: str,
    required_participants: tuple[str, ...] = (),
) -> EpistemicClaim:
    if not can_promote(claim, target, required_participants=required_participants):
        raise ValueError(f"silent or unauthorized promotion: {claim.claim_type} -> {target}")
    return EpistemicClaim(
        relationship_id=claim.relationship_id,
        claim_type=target,
        subject=claim.subject,
        content=claim.content,
        asserted_by=actor,
        provenance_refs=claim.provenance_refs + (claim.claim_id,),
        acknowledged_by=claim.acknowledged_by,
        disputed=claim.disputed,
    )
