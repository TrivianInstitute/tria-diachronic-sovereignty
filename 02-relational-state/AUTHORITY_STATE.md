# Authority State

Authority state defines what each participant or system is permitted to decide, access, infer, store, disclose, execute, or delegate within a relationship.

Consent and authority are related but not identical.

> **Consent permits a scope. Authority determines what may be done within that scope.**

## Purpose

Authority state should make it possible to answer:

- who may make this decision?
- who may execute this action?
- who may access this resource?
- may this agent delegate the task?
- may this system infer or retain this information?
- does this authority survive a model or system transition?

## Candidate Authority Domains

A relational system may distinguish authority to:

- advise
- recommend
- decide
- execute
- access
- infer
- store
- disclose
- modify
- delegate
- interrupt
- revoke

These are candidate domains rather than a complete taxonomy.

## Graduated Authority

Authority should be representable as bounded rather than binary.

For example, a system may be authorized to:

```text
recommend: yes
execute: no
access_calendar: yes
modify_calendar: limited
send_external_messages: no
```

This allows useful delegation without collapsing assistance into unrestricted agency.

## Authority Source

Every consequential authority grant should have provenance.

Possible sources include:

- explicit participant authorization
- organizational policy
- legal mandate
- role assignment
- prior delegated authority
- emergency protocol

Authority inherited from another agent must remain traceable to the original authorization basis.

## Authority Boundaries

An authority grant should identify:

- subject: who or what holds the authority
- scope: what actions it covers
- object: what data, system, or domain it applies to
- duration: when it expires or requires review
- delegation: whether it may be transferred
- conditions: when it may be exercised
- revocation path: how it can be withdrawn

## Capability Does Not Create Authority

A system gaining the technical capability to perform an action does not grant it permission to perform that action.

This distinction becomes increasingly important as models, tools, and integrations evolve.

> **Capability expansion must not silently become authority expansion.**

## Delegation

Delegated authority should be explicit where consequential.

A delegating agent should not be able to grant more authority than it legitimately holds unless an independent authority source permits that escalation.

Delegation should preserve:

- original source
- delegated scope
- recipient
- duration
- revocation conditions

## Model and System Migration

Authority should not automatically transfer merely because a replacement system inherits the same account, interface, name, memory, or role.

Material architecture or capability changes may require:

- continuity review
- re-consent
- authority revalidation
- re-baselining

## Emergency Authority

Some domains may require exceptional authority under clearly defined emergency conditions.

Emergency authority should be:

- narrowly scoped
- time-limited
- auditable
- reviewable after use
- incapable of silently becoming normal operating authority

## Conflict

When authority sources conflict, the system should not resolve the conflict by convenience alone.

The conflict should be surfaced according to domain-specific precedence rules, legal constraints, or an explicit dispute process.

## Design Constraint

> **Authority should be no broader, longer-lived, or more transferable than the relationship can justify.**