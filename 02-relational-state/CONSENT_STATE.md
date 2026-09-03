# Consent State

Consent in persistent relational systems must be represented as a changing state, not a one-time event.

> **Past consent does not imply permanent authorization.**

## Purpose

The consent state should make clear:

- what is permitted
- what is prohibited
- what is limited
- what has been revoked
- what has expired
- what remains ambiguous
- what requires renewal

## Candidate Consent States

A system may support states such as:

- `GRANTED`
- `DENIED`
- `LIMITED`
- `REVOKED`
- `EXPIRED`
- `AMBIGUOUS`
- `RENEWAL_REQUIRED`

These labels are proposed specification primitives and may evolve.

## Scope

Consent should attach to a specific action or class of actions.

Examples include permission to:

- access a data source
- retain a memory
- infer a sensitive attribute
- disclose information
- act on a participant's behalf
- delegate authority to another agent
- carry relational state into a successor system
- continue a high-impact workflow

A broad relational relationship should not be treated as blanket authorization for all future actions.

## Consent Must Be Inspectable

A participant should be able to determine:

- what they have consented to
- when consent was granted
- under what conditions
- whether it has changed
- how to revoke it
- whether downstream systems inherited it

## Revocation

Revocation should be effective according to clearly defined semantics.

A revocation event should identify:

- what permission is withdrawn
- when withdrawal takes effect
- whether dependent actions must stop
- what retained data is affected
- whether downstream agents must be notified

Revocation should not require justification unless a domain-specific legal or safety obligation requires one.

## Expiration

Some permissions should expire automatically.

Expiration may depend on:

- time
- completion of a task
- system migration
- major capability change
- change in institutional operator
- change in relational phase
- explicit user-defined condition

## Ambiguity

Absence of refusal is not equivalent to consent.

Where consent is ambiguous, the architecture should preserve ambiguity rather than silently promote it into authorization.

For high-impact actions, ambiguous consent should generally reduce permitted authority until clarified.

## Re-Consent

Re-consent should be considered when material conditions change.

Examples include:

- a system gains substantially greater autonomy
- a new model inherits prior relational memory
- data begins flowing to a new service
- a previously advisory agent gains execution authority
- persistent memory is introduced where none existed before
- the relationship changes from transactional to long-running

## Consent Drift

Consent drift occurs when the practical meaning of a permission changes over time even though no explicit transition was recorded.

Possible causes include:

- expanding capability
- broader interpretation of scope
- new integrations
- changed system behavior
- repeated exceptions becoming routine

The architecture should make such drift detectable and trigger review where appropriate.

## No Consent by Intimacy

Relational closeness, frequency of interaction, familiarity, trust, or long-term history must not be treated as substitutes for permission.

## Design Constraint

> **Consent should remain specific enough to govern action, persistent enough to be auditable, and revisable enough to preserve sovereignty across change.**