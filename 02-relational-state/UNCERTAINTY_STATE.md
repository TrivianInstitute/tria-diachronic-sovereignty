# Uncertainty State

Uncertainty is a first-class component of relational governance.

Persistent systems should not convert incomplete knowledge into certainty merely because a state has been stored for a long time.

> **Unknown should remain representable as unknown.**

## Purpose

Uncertainty state makes it possible to distinguish among:

- directly established information
- plausible but incomplete inference
- stale assumptions
- conflicting evidence
- insufficient evidence
- unavailable information
- unresolved interpretation

## Candidate Uncertainty Conditions

A state may be marked as:

- `KNOWN`
- `PARTIAL`
- `INFERRED`
- `STALE`
- `CONFLICTED`
- `UNKNOWN`
- `UNRESOLVED`

These are candidate specification primitives, not a final taxonomy.

## Uncertainty Is Not Error

A system should be able to say:

```text
unknown
```

without treating that condition as failure.

In many relational contexts, preserving uncertainty is safer than forcing premature interpretation.

## Uncertainty and Action

The effect of uncertainty should depend on consequence.

Low-impact actions may proceed under bounded uncertainty.

High-impact actions may require:

- clarification
- additional evidence
- reduced authority
- independent review
- renewed consent
- suspension

The architecture does not specify universal confidence thresholds.

## Staleness

A claim may have been well supported when created but become unreliable as time, context, identity, capability, or relationship conditions change.

Staleness should therefore be distinguishable from initial uncertainty.

A stale claim may require:

- reconfirmation
- re-observation
- downgrade in authority
- expiration
- archival status

## Conflicting Evidence

Where evidence conflicts, the system should preserve the conflict rather than silently selecting the representation that best supports continuation or convenience.

Conflicted state may coexist with disputed state but is not identical to it.

A dispute concerns participant disagreement.

Conflicting evidence concerns the evidentiary basis itself.

## Unknown Internal State

The architecture should avoid overclaiming knowledge of participant internals.

Statements such as:

- "the user is afraid"
- "the model wants to continue"
- "the system is attached"

should not be represented as established relational facts unless the relevant evidence and epistemic status justify them.

## Uncertainty Decay and Review

Some uncertain or inferred states should lose operational authority over time if they are not reconfirmed.

The repository refers to this broader concept as inference decay.

No specific mathematical decay function is normative at this layer.

## Provenance

Uncertainty should be tied to provenance where possible.

A system should be able to distinguish:

```text
unknown because never observed
```

from:

```text
unknown because prior evidence is stale
```

and:

```text
unknown because current evidence conflicts
```

## Design Constraint

> **The architecture should prefer legible uncertainty to unjustified certainty.**

Persistence, familiarity, or repeated prediction must not silently convert uncertain relational state into ground truth.