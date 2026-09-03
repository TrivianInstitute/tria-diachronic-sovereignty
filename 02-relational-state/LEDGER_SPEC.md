# Relational Ledger Specification

The relational ledger records consequential changes to governed relational state across time.

It is not intended to function as an exhaustive interaction log.

> **The ledger records governance-relevant change, not everything that happened.**

## Purpose

The ledger exists to make it possible to reconstruct:

- what changed
- when it changed
- who or what initiated the change
- what prior state existed
- what authority permitted the change
- what evidence or claim supported it
- whether the change was disputed
- whether it later expired, was revoked, or was superseded

## Ledger Entry

A ledger entry should contain enough information to make a consequential state transition independently inspectable.

A candidate entry may include:

```text
entry_id
relationship_id
timestamp
actor
state_domain
prior_state
new_state
transition_type
provenance_reference
authorization_basis
epistemic_status
dispute_status
expiry_or_review_condition
```

This structure is a specification precursor, not a final schema.

## Append-Oriented History

Where technically appropriate, consequential state transitions should preserve historical provenance rather than silently overwrite prior state.

This does not mean all raw data must be retained forever.

A system may support deletion, minimization, redaction, or cryptographic tombstoning while still preserving the fact that a governance-relevant transition occurred.

## No Transcript Requirement

A compliant ledger does not require full conversational history.

For example, instead of storing an entire exchange, a system may record:

```text
Consent for calendar access changed:
LIMITED -> REVOKED
Reason: participant revocation
Effective: immediately
```

The goal is reconstructable governance, not surveillance.

## Event Qualification

A relational event should generally enter the ledger when it changes or materially affects:

- consent
- authority
- shared claims
- dispute status
- uncertainty relevant to action
- identity continuity
- relational lifecycle
- delegated responsibility
- transformation provenance
- audit state

Routine conversational turns should not enter the ledger unless they cause one of these changes.

## Ledger and Epistemic Status

The ledger should preserve the epistemic status of the state being recorded.

For example:

```text
claim: "User prefers no reminders after 9 PM"
status: shared_claim
source: explicit user statement
```

is materially different from:

```text
claim: "User is probably tired after 9 PM"
status: inference
source: behavioral pattern
```

Persistence in the ledger must not silently elevate the second claim into the first.

## Disputed Entries

A ledger entry may remain valid as historical provenance while its interpretation is disputed.

The architecture should support states such as:

```text
record_exists: true
interpretation_disputed: true
```

Dispute should not require deleting history or pretending agreement exists.

## Mutation and Correction

Errors should be correctable without destroying traceability.

A correction should ideally record:

- the incorrect entry
- the correction
- who initiated the correction
- why it changed
- whether downstream state must be re-evaluated

## Retention and Minimization

Ledger retention should follow the principle of minimum necessary governance state.

Systems should define:

- retention duration
- expiration rules
- deletion rights
- redaction mechanisms
- portability requirements
- audit-access conditions

Long-term persistence requires justification.

## Ledger Poisoning Risk

A ledger can become unusable if participants or systems flood it with trivial, manipulative, ambiguous, or strategically misleading changes.

Implementations should therefore investigate:

- event qualification
- rate controls
- provenance strength
- dispute handling
- compression or summarization
- malicious-state detection

These mechanisms remain research and implementation questions.

## Design Constraint

> **The ledger must increase accountability without becoming a mechanism for totalizing memory.**

If the system cannot explain why a piece of relational history needs to be retained, it should not automatically be retained.