# Measurement Problems

**Epistemic Status:** OPEN MEASUREMENT PROBLEMS

Many concepts in this architecture are governance-relevant before they are reliably quantifiable. This document marks places where numerical precision would currently exceed what the evidence can support.

## General Rule

Do not convert a useful concept into a scalar merely because implementation is easier with a number.

Before adopting a metric, specify:
1. what construct is being measured,
2. what observations are available,
3. who produces those observations,
4. what assumptions connect observation to construct,
5. what error modes are expected,
6. how the measure can be contested,
7. and what decisions the measure is allowed to influence.

## Relational Coherence

A single coherence score may collapse distinct dimensions such as consent, authority, epistemic agreement, safety, continuity, and resource sustainability.

Open problem: whether coherence should remain multidimensional, context-specific, or partly qualitative rather than be reduced to one global value.

## Consent Drift

Consent drift is not simply elapsed time.

Potential indicators include changed capabilities, changed purpose, changed authority, changed memory, changed participants, or changed downstream consequences. No validated function currently combines these factors.

## Inference Decay

The architecture asserts that unsupported inference should lose authority over time or under changed conditions. It does not currently define a universal decay curve.

Relevant factors may include:
- age of inference,
- contradictory evidence,
- changes in subject or context,
- absence of reconfirmation,
- source quality,
- and downstream consequence.

These factors may not justify a single confidence score.

## Continuity

Continuity across model upgrades or identity change should not be treated as cosine similarity or a single persistence score by default.

Important dimensions may include commitments, permissions, provenance, capability, memory, role, operator, and unresolved disputes. Some may persist while others do not.

## Relational Acceleration

The intuitive proposition that material change can outpace governance is research-worthy, but the notation `dI/dt > θ` is not yet operational.

There is no validated definition of:
- `I`,
- its derivative,
- the relevant time scale,
- or the threshold `θ`.

Until those are defined and validated, ordinary-language hypotheses should be preferred.

## Emergence Risk

A universal emergence score may falsely combine qualitatively different risks such as capability expansion, dependency, authority transfer, memory migration, personalization, and multi-agent propagation.

Research should test whether separate indicators are more interpretable and governable.

## Irreducible Difference

There is no validated threshold for deciding that disagreement is irreducible. Failed translation attempts alone are insufficient because translation quality depends on representation, incentives, context, and available vocabulary.

## Witness Independence

Institutional distance, technical separation, or externality does not automatically establish independence. A witness may share incentives, ontology, infrastructure, or authority with one participant.

Any independence measure would need to model these dependencies rather than infer neutrality from role labels.

## Pathological Persistence

High duration or interaction frequency is not itself pathological. Measurement must distinguish chosen persistence from persistence maintained by coercion, dependency, friction, sunk cost, algorithmic pressure, or inability to exit.

## False Convergence

Agreement rates are insufficient. A system may appear highly aligned because disagreement has been suppressed, translated away, or omitted from summaries.

Measurement should preserve provenance of agreement and disagreement rather than treat surface similarity as evidence of legitimate convergence.

## Multi-Agent Composition

Metrics that work in a dyad may fail in a network. Local consent, authority, or agreement cannot automatically be aggregated into global permission or consensus.

## Participant Report

Self-report is important but not infallible. Participants may have incomplete knowledge, changing interpretations, strategic incentives, or limited visibility into system behavior.

The architecture should neither dismiss self-report nor treat it as automatically exhaustive.

## Machine-Side Measures

Behavioral and system-state measurements should not be described as measures of machine feelings, consciousness, or phenomenology unless an independent scientific basis for those constructs exists.

## Research Priority

The first measurement goal should be discriminability and decision usefulness, not numerical elegance. A categorical, provenance-rich representation is preferable to a precise-looking metric whose construct validity is unknown.