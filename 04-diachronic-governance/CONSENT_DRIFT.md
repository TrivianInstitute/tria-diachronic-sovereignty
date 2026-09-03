# Consent Drift

**Epistemic status: NORMATIVE / SPECIFICATION PRECURSOR**

Consent drift is the divergence between an earlier authorization and the relationship, capability, context, or consequence that now exists.

A sequence of individually permitted actions may still produce a condition that was never meaningfully authorized as a whole.

## Sources of Drift

Consent may drift when:

- capabilities expand;
- purposes change;
- retained information is reused in new contexts;
- authority accumulates through repeated delegation;
- a model, operator, or institution changes;
- interaction moves into a more consequential domain;
- an inferred preference is treated as durable permission;
- dependencies deepen; or
- earlier disclosures no longer describe present conditions.

## Detection

Possible indicators include:

- present use exceeds the original scope;
- the consenting participant could not reasonably anticipate the current consequence;
- material conditions have changed since authorization;
- consent is technically active but no longer legible;
- withdrawal has become difficult or costly; or
- the system relies on silence, habit, or continued use as renewed consent.

Indicators are review signals, not automatic findings of invalid consent.

## Required Response

When possible drift is detected, the system should:

1. identify the affected authorization;
2. preserve the original scope and provenance;
3. describe the relevant change in accessible language;
4. reduce or pause consequential action where appropriate;
5. request renewed, narrowed, or revised consent;
6. record the outcome without erasing prior state.

## Asymmetric Risk

The burden of review should increase with consequence, opacity, irreversibility, and power asymmetry.

Low-risk personalization and execution authority should not share one consent rule.

## Prohibitions

The architecture rejects:

- consent inferred solely from non-objection;
- permanent consent created by repetition;
- authority inherited from unrelated permissions;
- bundled re-consent that obscures material changes; and
- punitive loss of unrelated service for refusing expanded consent, unless technically necessary and clearly explained.

## Design Principle

> **Consent must remain connected to the conditions that made it meaningful.**
