# Provenance Specification

Provenance records where consequential relational state came from and how it changed.

Without provenance, persistent systems can preserve assumptions while losing the conditions that originally justified them.

> **A state without provenance is harder to contest, reinterpret, or safely inherit.**

## Purpose

Provenance should make it possible to determine:

- who or what introduced a state
- when it was introduced
- what source supported it
- what epistemic status it had
- what prior state it replaced or extended
- what authority allowed the transition
- whether the state was later disputed, superseded, expired, or revoked

## Provenance Domains

Provenance may attach to:

- consent
- authority
- epistemic claims
- shared commitments
- disputed claims
- model or system transitions
- continuity attestations
- lifecycle changes
- audit findings

## Candidate Provenance Record

```text
provenance_id
state_reference
source_type
source_reference
origin_actor
created_at
prior_state_reference
transition_reason
authorization_basis
epistemic_status
dispute_status
superseded_by
```

This is a specification precursor, not a finalized implementation schema.

## Source Type

A source type may include:

- explicit participant statement
- system observation
- model inference
- external record
- policy rule
- delegated action
- audit finding
- migration artifact
- human review

Source type must not be confused with truth status.

## Provenance and Epistemic Authority

A claim's origin should influence how it may be used.

For example, an explicit permission granted by a participant and an inferred preference generated from behavior should not receive the same authority simply because both are stored persistently.

Provenance therefore supports epistemic sovereignty by preserving the difference between:

- what was said
- what was observed
- what was inferred
- what was interpreted
- what was jointly accepted

## Transformation Provenance

Where systems or participants materially change, provenance should preserve enough lineage to evaluate whether prior relational authority still applies.

Relevant changes may include:

- model replacement
- major capability increase
- architecture migration
- change in hosting institution
- change in memory system
- change in policy regime
- substantial shift in delegated authority

The architecture should not assume that persistence of an identifier proves continuity of authority.

## Provenance Across Systems

When relational state moves between systems, provenance should travel with the state where technically and legally appropriate.

A receiving system should be able to determine:

- where the state originated
- whether it was contested
- whether it has expired
- what permissions governed its transfer
- whether re-consent is required

## Redaction and Privacy

Provenance must not become an excuse for indefinite retention of sensitive source material.

A system may preserve the governance fact of a transition while minimizing or deleting unnecessary underlying content.

For example, it may retain:

```text
consent_revoked: true
revoked_at: timestamp
source: explicit participant action
```

without retaining the full conversation in which revocation occurred.

## Correction

If provenance is wrong, correction should preserve the correction history rather than silently rewriting the past.

A corrected record should indicate:

- what was wrong
- what replaced it
- when correction occurred
- who authorized correction
- whether dependent states require review

## Design Constraint

> **Persistent state should remain attributable enough to be questioned.**

If a system cannot explain where a consequential relational assumption came from, that assumption should lose authority rather than gain it through persistence.