from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ContinuityAttestation:
    relationship_id: str
    predecessor: str
    successor: str
    changed: tuple[str, ...] = ()
    persisted: tuple[str, ...] = ()
    removed: tuple[str, ...] = ()
    active_commitments: tuple[str, ...] = ()
    expired_permissions: tuple[str, ...] = ()
    uncertainties: tuple[str, ...] = ()


MATERIAL_CHANGE_TYPES = {
    "MODEL_REPLACEMENT",
    "MAJOR_VERSION_CHANGE",
    "MEMORY_MIGRATION",
    "VENDOR_MIGRATION",
    "CAPABILITY_EXPANSION",
    "POLICY_CHANGE",
    "OPERATOR_CHANGE",
}


def requires_reconsent(change_types: set[str], inherited_authority: bool = False) -> bool:
    """Conservative reference rule for material continuity changes.

    This is intentionally categorical rather than score-based. It is a testable
    implementation hypothesis, not a universal threshold.
    """
    if change_types & MATERIAL_CHANGE_TYPES:
        return True
    return inherited_authority


def rebaseline(attestation: ContinuityAttestation) -> dict[str, tuple[str, ...]]:
    """Produce a minimal candidate baseline without erasing prior provenance."""
    return {
        "active_commitments": attestation.active_commitments,
        "known_persistences": attestation.persisted,
        "known_changes": attestation.changed,
        "uncertainties": attestation.uncertainties,
    }
