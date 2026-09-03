# Inference Decay

**Inference decay** is the principle that unverified relational inferences should lose authority when they become stale, unsupported, contextually displaced, or contradicted.

The normative principle is stronger than any particular mathematical implementation.

## Why Decay Is Needed

Persistent systems can preserve old inferences long after the conditions that produced them have changed.

Examples include:

- a preference inferred months earlier;
- a capability estimate formed before a major model upgrade;
- an interpretation created during a temporary crisis;
- an identity assumption based on a short behavioral window.

Without decay, memory can become semantic fossilization.

## Decay Does Not Mean Deletion

A decayed inference may remain in provenance history while losing authority in present decision-making.

The architecture should distinguish:

- historical existence;
- current relevance;
- current confidence;
- current authority.

## Possible Decay Triggers

A mature implementation may consider:

- elapsed time;
- context change;
- contradictory evidence;
- participant correction;
- model or capability change;
- re-baselining;
- absence of reconfirmation;
- domain-specific review requirements.

No universal weighting or half-life is specified here.

## High-Consequence Inferences

Inferences that affect consent, identity, authority, disclosure, access, or consequential action should generally face stronger freshness requirements than low-impact conversational preferences.

## Renewal

An inference may regain authority through:

- new supporting observation;
- participant confirmation;
- explicit re-evaluation;
- contextually valid repetition.

Renewal should create new provenance rather than silently pretending the original inference never aged.

## Research Status

The existence of a decay mechanism is a normative architectural proposal.

The choice of decay function, threshold, domain calibration, and timing remains experimental until empirically validated.