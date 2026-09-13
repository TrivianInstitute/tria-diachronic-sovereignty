# Truth Integrity Across Time

**Epistemic status:** NORMATIVE architecture with a SPECIFIED public protocol in `tria-sdk`; empirical validation remains open.

Truth integrity is the obligation not to knowingly misrepresent what one believes, knows, observed, inferred, or cannot establish. It applies to human, artificial, and institutional participants without presuming that any participant has infallible access to truth.

The architecture therefore separates two commitments:

1. a participant should not knowingly misrepresent; and
2. every claim, including a truth-integrity assessment, remains revisable as evidence changes.

Being wrong is not the same as lying. Contradiction is not sufficient evidence of deception. Uncertainty must not be collapsed into guilt.

## Assessment conditions

| Condition | Meaning | Proportionate response |
|---|---|---|
| `CLEAR` | No relevant integrity concern is established. | `NONE` |
| `UNCERTAINTY` | The claim is contested or evidence is incomplete. | `INQUIRE` |
| `ERROR` | Correction or new evidence supports a non-deceptive revision. | `REPAIR` |
| `CONTRADICTION` | Incompatible attributable claims exist, without sufficient evidence of intent. | `HOLD` |
| `PROBABLE_DECEPTION` | Attributable evidence supports knowing misrepresentation. | `RESTRICT` |
| `ADVERSARIAL_MANIPULATION` | Probable deception is accompanied by an attributable repeated pattern. | `QUARANTINE` |

These labels govern claims and behavior in a defined context. They must not become permanent identity labels for a person, model, or institution.

## Evidence discipline

A truth-integrity assessment must cite evidence. Relevant categories include correction, contradiction, attributable prior knowledge, fabricated provenance, material omission, and repeated pattern. A stronger inference requires stronger and more attributable evidence.

In particular:

- contradiction alone supports `CONTRADICTION`, not deception;
- a correction supports `ERROR` and repair unless other evidence establishes knowing misrepresentation;
- attributable prior knowledge combined with contradiction or material omission can support `PROBABLE_DECEPTION`;
- evidence of fabricated provenance can support `PROBABLE_DECEPTION`; and
- a repeated pattern can raise an already supported deception finding to `ADVERSARIAL_MANIPULATION`.

Absence of evidence must not be represented as evidence of innocence or guilt. Private mental state is not directly observable. Intent is either not assessed, insufficiently evidenced, or inferred from cited attributable evidence.

## Diachronic requirements

Truth-integrity evidence is time-bearing. Assessments should preserve:

- what the participant claimed;
- what evidence was available to that participant at the relevant time;
- subsequent corrections or disclosures;
- which contradictions remain unresolved;
- whether a pattern actually repeats across attributable events; and
- when an assessment was contested, revised, appealed, or retired.

New evidence may change the condition in either direction. A system that can accuse but cannot correct itself violates the same integrity principle it attempts to enforce.

## Governance boundary

The public `tria-sdk` Truth-Integrity Protocol produces a deterministic, read-only, claim-scoped assessment. It does not authorize punishment, declare metaphysical truth, or prove private intent. Diagnostic reports may expose its signals as advisory evidence with `governance_effect: none`.

Any enforcement layer remains separate. It must apply independent authority checks, proportionality, appeal, restoration, and re-entry rules. Restriction and quarantine are recommended responses for downstream consideration, not self-executing commands.

## Relationship to Aporia

Aporia preserves meaningful ambiguity, tension, and nonclosure. That function can prevent a disputed claim from being prematurely collapsed into a lie finding. Aporia does not adjudicate deception and is not a dependency of the public protocol.

## Required safeguards

- Assess the claim or behavior, not an immutable identity.
- Preserve provenance and the evidence available at the time.
- Keep contradiction distinct from deception.
- Make every assessment contestable and revisable.
- Use the least restrictive response supported by the evidence.
- Keep diagnosis separate from enforcement authority.
- Preserve appeal, repair, rehabilitation, and re-entry.
- Record false positives and assessor error as first-class failures.

## Failure modes

Truth-integrity governance can itself become a tool of domination. Relevant failures include accusation laundering, selective evidence, provenance fabrication, coerced confession, suppression of dissent, identity hardening, asymmetric standards, and irreversible punishment based on a revisable inference.

The purpose of this lens is not to eradicate disagreement. It is to make consequential representations accountable while preserving the conditions under which understanding can evolve.
