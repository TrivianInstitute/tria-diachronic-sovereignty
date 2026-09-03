# Model Upgrade

**Epistemic Status:** ILLUSTRATIVE / NON-NORMATIVE

## Purpose

This example shows how a persistent relationship can continue across a model upgrade without pretending that the successor is identical to the predecessor.

## Scenario

A participant has used Model V1 for several months. The service migrates the relationship to Model V2, which differs in capabilities, safety behavior, context handling, and memory interpretation.

The provider can migrate selected relational state, but cannot guarantee behavioral identity.

## Governance response

The upgrade should be represented as continuity with change, not seamless sameness.

A continuity attestation should identify:

- predecessor and successor identifiers;
- known persisted state;
- known changed capabilities or policies;
- removed or expired permissions;
- active commitments that remain in scope;
- unresolved uncertainties about behavioral continuity.

Material changes should trigger review of inherited authority and consent.

## Example sequence

1. V1 has permission to retain project-level preferences.
2. V2 introduces a new long-term personalization capability.
3. The existing relationship history is migrated.
4. The migration record distinguishes retained project memory from the new personalization capability.
5. The new capability is not treated as pre-authorized merely because the relationship persisted.
6. The participant is given a meaningful opportunity to re-consent, narrow scope, rebaseline, or decline continuity.

## What this example demonstrates

Continuity should preserve useful provenance without imprisoning either participant inside a fiction of perfect identity persistence. A successor inherits history only to the extent that governance permits; it does not inherit unquestioned authority from resemblance alone.
