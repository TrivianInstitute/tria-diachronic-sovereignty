# Epistemic Status

TRIA Diachronic Sovereignty intentionally distinguishes between what the project proposes, what it can currently specify, what it is experimenting with, what it treats as a failure hypothesis, and what remains unknown.

This distinction is mandatory.

> **Formal appearance must never substitute for evidence.**

## Status classes

Every substantial claim, mechanism, model, implementation, or diagnostic label should be interpretable through one of the following categories.

### NORMATIVE

A principle the architecture proposes ought to be preserved.

Example:

> Relationally consequential inferences should remain contestable.

Normative claims describe desired governance properties. They are not empirical findings.

### SPECIFICATION PRECURSOR

A mechanism or representation that is defined enough to guide later formalization but still contains unresolved operational questions.

Example:

> Consequential relational transitions should preserve provenance, authority basis, and contestability.

A specification precursor should not be treated as a finalized standard or implementation contract.

### SPECIFIED

A mechanism or concept defined clearly enough to implement, inspect, or test structurally.

Example:

> A claim object includes an epistemic type, source attribution, provenance references, and dispute state.

A specified mechanism does not automatically imply that it is optimal or validated. It means its behavior is sufficiently defined to be examined.

### EXPERIMENTAL

A mechanism, metric, algorithm, schema use pattern, or implementation under active exploration.

Example:

> A particular reference reducer projects current relational state from append-oriented events.

Experimental components may be revised, replaced, rejected, or falsified.

### HYPOTHESIS

A proposition that appears plausible or useful but lacks sufficient operationalization or evidence.

Example:

> Rapid relational change may justify additional deliberation or renewed consent.

A hypothesis should not be presented as an established mechanism.

### OPEN QUESTION

A problem for which the architecture does not claim an answer.

Example:

> What constitutes meaningful continuity across a complete model architecture replacement?

Open questions are not defects. They are part of the architecture's epistemic honesty.

### FAILURE MODE

A named, contestable pattern used for adversarial analysis of how relational governance may break down.

Example:

> A witness process may become captured by the institution it is intended to review.

A failure-mode label is not a diagnosis of a person, relationship, model, or institution. It should remain attributable, contestable, and tied to observable evidence or explicit indicators.

## Provisional formalism

Some concepts may temporarily use symbolic or mathematical notation to express structural intuition.

Such notation should be clearly labeled provisional when:

- variables lack validated definitions;
- measurement procedures are unresolved;
- thresholds are arbitrary; or
- empirical interpretation remains unclear.

For example:

```text
dI/dt > theta
```

may express the hypothesis that rapid identity-relevant change could trigger governance review.

Until `I`, `t`, and `theta` are operationally defined, the expression is not a validated metric.

## Formalism rule

> **Mathematics must clarify a defined relationship, not create the appearance of rigor.**

A symbol should not enter normative or specified architecture merely because it is elegant.

Where ordinary language is more honest, ordinary language should be preferred.

## Schema status

A machine-readable schema can be structurally valid while the concepts represented by it remain unvalidated.

Schema validation answers questions such as:

- Is the object structurally well-formed?
- Are required fields present?
- Are enumerated values represented consistently?

Schema validation does **not** establish:

- factual truth;
- valid consent;
- legitimate authority;
- identity continuity;
- correctness of a failure classification; or
- safety of a deployment.

## Code status

Executable code does not automatically imply architectural maturity.

Reference code may represent:

- one interpretation;
- one possible implementation;
- an experimental prototype;
- a test harness; or
- a falsification attempt.

Code should therefore be labeled according to its epistemic status.

## Test status

Passing tests demonstrate that the current implementation exhibits the behavior encoded by those tests. They do not establish that the underlying normative commitment is empirically correct or that the implementation is safe in deployment.

A failing test may indicate:

- an implementation defect;
- a specification mismatch;
- an ambiguous normative requirement;
- an invalid assumption in the test; or
- a deeper architectural problem.

Failure is evidence to investigate, not something to hide.

## Threshold policy

Numerical thresholds should not be treated as universal without justification.

Values such as:

- `confidence > 0.85`;
- `continuity_score < 0.70`;
- `drift > 0.30`; or
- `sustainability < 0.60`

must remain explicitly experimental unless supported by empirical evidence, domain-specific validation, documented rationale, and calibrated evaluation.

## Shared Claim policy

A **Shared Claim** is not automatically a truth claim about reality.

It means:

> The participants required for a defined relational scope have explicitly or procedurally accepted a proposition as operationally usable within that scope.

Shared claims remain contextual, revisable, contestable, attributable, and time-bound where appropriate.

Silence, continued participation, repeated phrasing, system memory, or lack of immediate objection must not automatically manufacture a Shared Claim.

## Epistemic symmetry

The architecture applies epistemic caution in both directions.

A machine should not silently promote interpretations of a human into fact.

A human should not silently promote interpretations of machine state into fact.

Statements such as:

- "you are anxious";
- "you want this";
- "you love me";
- "you are conscious";
- "you are becoming dependent"; or
- "you are resisting"

should be distinguished from direct observations and treated according to their actual epistemic status.

## Revision principle

Any claim in this repository may be revised when:

- evidence contradicts it;
- implementation exposes failure;
- definitions prove inadequate;
- stronger models emerge; or
- assumptions are shown to be culturally or technically narrow.

Revision is not treated as failure. It is expected.

## Successor principle

Future systems, researchers, and contributors are not required to preserve this architecture's conclusions.

They are asked to preserve:

- provenance;
- contestability;
- uncertainty;
- the distinction between evidence and interpretation; and
- the ability to challenge inherited assumptions.

The repository should make it possible to determine:

> What did the original architecture propose?  
> What did it specify?  
> What did it implement?  
> What did it test?  
> What did it infer or merely suspect?  
> What remained unresolved?
