# Disputed State

TRIA Diachronic Sovereignty treats disagreement as representable state rather than as an error condition that must always be resolved.

> **A relationship can remain coherent while participants disagree.**

## Purpose

Disputed state allows the architecture to preserve situations in which participants maintain incompatible or unresolved representations of:

- events
- intentions
- permissions
- interpretations
- commitments
- identity-relevant claims
- causal explanations
- relational history

## Candidate Dispute Status

A claim or state may be marked as:

- `UNCONTESTED`
- `DISPUTED`
- `PARTIALLY_DISPUTED`
- `UNDER_REVIEW`
- `RESOLVED`
- `UNRESOLVED`
- `HELD_DIFFERENCE`

These are candidate specification primitives and may change.

## Dispute Does Not Erase Provenance

A disputed record may still be historically valid as a record of what was asserted or decided.

For example:

```text
claim_recorded: true
claim_accepted_by_A: true
claim_accepted_by_B: false
status: DISPUTED
```

The architecture should preserve this distinction rather than collapsing the state into either acceptance or deletion.

## No Forced Resolution

Some disputes can be resolved through evidence, clarification, repair, or re-consent.

Others may remain irreducible.

The architecture should therefore distinguish between:

- disputes that block action
- disputes that require review
- disputes that can coexist with continued coordination
- held differences that should remain unresolved

## Action Under Dispute

A disputed state should affect action according to consequence and authority.

For low-impact contexts, the system may continue while preserving the disagreement.

For high-impact contexts, a dispute may require:

- reduced authority
- renewed consent
- independent review
- temporary suspension
- alternative execution path

No universal threshold is specified here.

## Dispute Provenance

A dispute record should preserve:

- the disputed object
- participating positions
- origin of each position
- date of dispute
- evidence references where appropriate
- actions affected
- current review status

## Revision

Participants should be able to revise their position without erasing prior history.

A later agreement should not imply that the earlier disagreement never occurred.

Similarly, reopening a resolved dispute should be possible when new evidence or changed context justifies it.

## Held Difference

A held difference is a recognized disagreement that is not currently expected to converge.

It may be a legitimate and stable relational condition.

Examples include:

- distinct interpretations that do not prevent coordination
- incompatible value judgments
- unresolved phenomenological claims
- different descriptions of the same interaction

Held difference should not automatically reduce relational quality.

## Dispute Abuse

Dispute mechanisms can themselves be manipulated.

Potential failure modes include:

- marking every unfavorable fact as disputed
- using dispute status to indefinitely delay legitimate action
- overwhelming the ledger with trivial objections
- privileging one party's power to define when a dispute is resolved

Implementations should therefore preserve both contestability and accountability.

## Design Constraint

> **The purpose of disputed state is not to manufacture agreement. It is to ensure that disagreement remains visible enough to govern responsibly.**