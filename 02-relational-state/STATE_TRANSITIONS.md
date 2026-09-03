# Relational State Transitions

Relational state changes over time. Those changes should be governed rather than treated as incidental updates to memory.

> **A consequential state change should be attributable, authorized, inspectable, and reversible where appropriate.**

## Purpose

State-transition rules define how relational state may move from one condition to another.

Examples include:

```text
CONSENT: GRANTED -> REVOKED
AUTHORITY: ADVISE -> EXECUTE
CLAIM: INFERENCE -> SHARED_CLAIM
DISPUTE: UNCONTESTED -> DISPUTED
LIFECYCLE: ACTIVE -> DORMANT
```

The transition itself is governance-relevant.

## Transition Requirements

A consequential transition should generally specify:

- prior state
- proposed new state
- initiating actor or process
- authorization basis
- provenance
- effective time
- affected scope
- dispute status
- review or expiry condition where relevant

## No Silent Promotion

Certain transitions must never occur merely because time passes, an inference is repeated, or a system becomes more confident.

Examples include:

```text
INFERENCE -> SHARED_CLAIM
AMBIGUOUS_CONSENT -> GRANTED
CAPABILITY -> AUTHORITY
HISTORICAL_PERMISSION -> PERMANENT_PERMISSION
```

These transitions require explicit or procedurally defined authorization.

## Transition Classes

Useful transition classes may include:

### Participant-Initiated

Examples:

- consent revocation
- permission grant
- dispute declaration
- request for deletion
- re-baselining request

### System-Initiated

Examples:

- stale-state downgrade
- expiry
- capability-change review
- uncertainty escalation

System-initiated transitions must remain bounded by prior authority.

### Policy-Initiated

Examples:

- legal retention expiry
- organizational role change
- security revocation

### Jointly Established

Examples:

- shared claim
- new relational baseline
- mutually accepted repair state

## Reversibility

Not every transition is reversible, but the architecture should identify reversibility explicitly.

For example:

- a permission may be revocable
- a disclosure cannot always be undone
- a deleted record may not be recoverable
- a completed external action may require remediation rather than reversal

Systems should not imply reversibility where none exists.

## Transition Preconditions

Some transitions require preconditions.

For example, moving from advisory authority to execution authority may require:

- explicit consent
- scope definition
- expiration or review condition
- confirmation of affected resources

A transition should fail safely when required preconditions are missing.

## Transition Under Dispute

If a transition depends on disputed state, the system should determine whether the action can:

- proceed
- proceed with reduced authority
- require review
- pause
- be denied

This should depend on consequence, domain, and existing authority rather than a universal numeric threshold.

## Transition After Material Change

Changes in model, capability, institution, policy, or infrastructure may invalidate prior assumptions about state.

A material change may trigger:

- continuity review
- authority revalidation
- re-consent
- uncertainty downgrade
- relational re-baselining

## Transition Logging

Governance-relevant transitions should produce a ledger entry with sufficient provenance for reconstruction.

A transition record should not require retention of unrelated conversation content.

## Invalid Transitions

A system should reject or flag transitions that:

- exceed the initiating actor's authority
- depend on expired consent
- silently elevate epistemic status
- erase unresolved dispute without justification
- inherit authority across a discontinuity without review
- expand scope beyond the original authorization

## Design Constraint

> **The architecture should govern not only what state exists, but how that state came to exist.**

A relational system is safer when its consequential transitions can be reconstructed, challenged, and revised instead of appearing as unexplained present-state facts.