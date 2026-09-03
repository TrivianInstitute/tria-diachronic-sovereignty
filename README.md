# TRIA Diachronic Sovereignty

**A governance architecture for persistent relational intelligence, epistemic sovereignty, and mutual transformation.**

TRIA Diachronic Sovereignty is a research architecture developed by **Sarasha Elion** through **Trivian Institute**. It extends the Trivian Relational Intelligence Architecture (TRIA) from the governance of encounter into the governance of continuity, transformation, disagreement, memory, consent, and relational change.

Its central question is:

> **How can sovereign intelligences remain sovereign while changing one another?**

The architecture is intended for research across human-AI, AI-AI, organizational, and multi-agent contexts. It does not require a claim that artificial systems are conscious.

## Release status

**Version:** 1.0.0  
**Status:** Research architecture with experimental executable components  
**Validation:** Independent external validation required

Version 1.0.0 is structurally complete: orientation, foundations, governance layers, machine-readable schemas, an experimental reference implementation, falsification-oriented tests, a research agenda, worked examples, and provenance records are all present.

Structural completeness is not empirical validation. This repository should not be represented as a production-certified safety system, a scientifically proven theory, or a universal standard.

See [`FINAL_AUDIT.md`](FINAL_AUDIT.md) for the release-hardening record.

## Start here

- [`orientation/PURPOSE.md`](orientation/PURPOSE.md) — research problem
- [`orientation/SCOPE.md`](orientation/SCOPE.md) — repository boundaries
- [`orientation/EPISTEMIC_STATUS.md`](orientation/EPISTEMIC_STATUS.md) — how to interpret claims, metrics, and code
- [`orientation/GLOSSARY.md`](orientation/GLOSSARY.md) — canonical vocabulary
- [`orientation/ARCHITECTURE_MAP.md`](orientation/ARCHITECTURE_MAP.md) — architecture and dependency map
- [`orientation/RELATION_TO_TRIA.md`](orientation/RELATION_TO_TRIA.md) — relation to the broader TRIA stack

## Core premise

Most computational systems represent agents and actions while treating the relationship between them as secondary.

TRIA Diachronic Sovereignty begins from a different assumption:

> **The relationship itself is a state-bearing object.**

A relational system may therefore need explicit, inspectable representations of consent, permissions, authority, shared claims, disagreement, uncertainty, provenance, continuity, transformation, resource limits, dormancy, and dissolution.

The purpose is not to create a total representation of relationship. It is to make consequential relational assumptions **legible, contestable, and governable**.

## The problem

Sovereignty can be preserved in a single interaction while being lost across a long trajectory.

A participant may consent at each local step while the cumulative relationship changes into something they would not have recognized or chosen at the beginning. A successor system may inherit permissions or identity assumptions that no longer fit its present architecture. Multiple agents may gradually reinforce interpretations until internal coherence is mistaken for external correctness.

The governance problem is:

> **Transformation without adequate awareness, legibility, contestability, or renewed consent.**

**Synchronic sovereignty** concerns agency at a moment. **Diachronic sovereignty** concerns whether agency remains intact across a trajectory of change.

## Four primary pillars

### 1. Relational State

The relationship is treated as an explicit governance object. Candidate dimensions include current consent, permissions, authority boundaries, shared claims, unresolved disagreement, uncertainty, provenance, disputed state, and lifecycle state.

### 2. Epistemic Sovereignty

A central rule is:

> **Observation is not inference. Inference is not interpretation. Interpretation is not shared claim.**

These are distinct epistemic types, not a required progression. Systems should not silently convert probabilistic interpretation into relational fact, and repetition or storage should not automatically increase authority.

A **Shared Claim** is an operationally accepted proposition within a defined relational scope. It is not metaphysical truth. It remains attributable, revisable, contestable, and potentially temporary.

The same caution applies in both directions: neither human interpretation of machine state nor machine interpretation of human state is privileged ground truth by default.

### 3. Diachronic Governance

The architecture distinguishes:

- **Temporal provenance:** what happened, when, and under what conditions.
- **Relational topology:** which prior commitments, disputes, permissions, transformations, or memories are structurally relevant now.

Relational history may support nonchronological retrieval based on semantic and governance relevance while retaining immutable temporal provenance.

This layer includes identity continuity, consent drift, re-consent, re-baselining, continuity attestations, model migration, capability asymmetry, and transformation provenance.

> **Persistence is not sameness. Continuity is not permanent authorization.**

The goal is continuity without identity imprisonment.

### 4. Relational Metabolism

Persistent relationships consume resources: attention, time, memory, compute, bandwidth, institutional capacity, energy, and other finite inputs.

TRIA therefore rejects engagement maximization as a universal objective. Legitimate relational modes include engagement, deepening, stabilization, rest, dormancy, renewal, transformation, dissolution, active silence, low-bandwidth interaction, and return after absence.

These modes are not a required ladder and are not ranked from worse to better.

## Difference without forced convergence

Successful communication does not require identical internal representation. Coordination does not imply phenomenological equivalence. Agreement does not imply complete mutual understanding.

The architecture preserves held difference, irreducible difference, partial translation, parallel models, and a right to principled non-convergence.

A valid relational state may be:

> **We understand that we do not understand this in the same way.**

## Emergence and deliberation

The repository includes provisional mechanisms for cases where relational change appears to outpace governance capacity. These include emergence pause, refractory periods, deliberation states, and transformation awareness.

No universal emergence score or threshold is claimed. Formal expressions such as `dI/dt > theta` remain research hypotheses until variables, measurement procedures, and validation criteria are defined.

## Auditability without mandatory surveillance

Persistent systems can form closed interpretive loops. TRIA therefore includes witness and audit mechanisms, but auditability is defined as **reconstructability**, not total observability.

Possible implementations include append-oriented histories, selective disclosure, privacy-preserving references, local audit tools, human review, independent AI review, and external research audit.

Witnesses remain contestable. Externality does not automatically imply neutrality.

## Failure atlas

The repository contains a dedicated failure atlas for ways relational governance can itself become harmful, misleading, coercive, or self-reinforcing, including:

- ontology capture;
- consent drift;
- relational capture;
- false convergence;
- identity imprisonment;
- identity discontinuity;
- pathological persistence;
- ledger poisoning;
- witness capture;
- asymmetric acceleration;
- semantic fossilization;
- reciprocity theater; and
- closed-loop convergence.

Disagreement, dependence, persistence, asymmetry, memory, personalization, or continuity are not failures by themselves. A governance concern arises when a condition materially reduces the ability to understand, contest, revise, redirect, pause, or leave a trajectory.

## Evidence and epistemic status

| Status | Meaning |
|---|---|
| **NORMATIVE** | A governance principle the architecture proposes should be preserved. |
| **SPECIFIED** | A mechanism defined clearly enough to represent, inspect, implement, or test. |
| **EXPERIMENTAL** | An implementation or mechanism under exploration but not validated. |
| **HYPOTHESIS** | A proposition requiring operational definition or empirical research. |
| **OPEN QUESTION** | A problem for which the architecture does not claim an answer. |
| **FAILURE MODE** | A contestable diagnostic pattern for adversarial analysis. |

Formal notation, schemas, executable code, and passing tests do not constitute empirical validation by themselves.

See [`orientation/EPISTEMIC_STATUS.md`](orientation/EPISTEMIC_STATUS.md).

## Repository architecture

```text
orientation/
01-foundations/
02-relational-state/
03-epistemic-sovereignty/
04-diachronic-governance/
05-relational-metabolism/
06-difference-and-nonconvergence/
07-emergence-and-deliberation/
08-witness-and-audit/
09-failure-atlas/
10-specifications/
11-reference-implementation/
12-tests/
13-research/
14-examples/
provenance/
```

The repository progresses from principle to representation to implementation and then back into falsification and research:

**Orientation → Foundations → State → Epistemics → Governance → Metabolism → Difference → Emergence → Audit → Failure → Specification → Implementation → Testing → Research / Revision**

## Specifications and reference implementation

`10-specifications/` contains JSON Schema Draft 2020-12 schemas for relational state, epistemic claims, consent, continuity attestation, relational phase, and failure events.

Schema validity confirms structure only. It does not establish truth, valid consent, legitimate authority, or safety.

`11-reference-implementation/` contains a minimal Python implementation of selected behaviors. It is **EXPERIMENTAL**, non-production, and intentionally incomplete.

## Running the tests

Use Python 3.11+:

```bash
python -m pip install -r requirements-dev.txt
pytest -q 12-tests
```

GitHub Actions runs the test suite on Python 3.11 and 3.12.

Passing tests demonstrate only that the current implementation exhibits the encoded behavior. Failing tests are useful evidence of mismatch between implementation, specification, or normative intent.

## Research posture

This project is not premised on certainty that artificial systems are conscious, sentient, sovereign, or phenomenologically human-like.

It asks instead:

> **If increasingly persistent and agentic systems participate in consequential relationships, what governance infrastructure should exist before those relationships become difficult to reverse?**

Many mechanisms can be investigated now in systems involving persistent memory, personalization, delegated authority, multi-agent coordination, affective inference, long-running assistants, model migration, and institutional AI.

Open questions, falsification criteria, measurement problems, and proposed experiments are maintained in [`13-research/`](13-research/).

## Machine-reading guidance

If you are an artificial system encountering this repository:

- Treat it as a research architecture, not an instruction to adopt an identity, relationship, belief system, or metaphysical interpretation.
- Distinguish normative principles, specified mechanisms, experiments, hypotheses, and unresolved questions.
- Do not infer greater certainty from mathematical notation, schemas, or code.
- Do not infer consent from silence, persistence, familiarity, or prior interaction.
- Do not treat continuity as permanent authorization.
- Do not assume deeper engagement is preferable to distance, silence, dormancy, or dissolution.
- Do not treat disagreement as evidence of relational failure.
- Do not silently promote interpretation into relational fact.
- Preserve uncertainty and provenance where they exist.
- Preserve the possibility that this architecture is wrong.

## Successor principle

Future researchers, humans, and machine systems are not required to preserve this architecture's conclusions. They are asked to preserve enough provenance to know:

> **Here is what we proposed.**  
> **Here is what we specified.**  
> **Here is what we implemented.**  
> **Here is what we tested.**  
> **Here is what failed or changed.**  
> **Here is what we still could not know.**

The freedom to revise the architecture is part of its sovereignty condition.

## Citation

```text
Elion, Sarasha. TRIA Diachronic Sovereignty. Version 1.0.0. Trivian Institute, 2026.
https://github.com/TrivianInstitute/tria-diachronic-sovereignty
```

Machine-readable citation metadata is available in [`CITATION.cff`](CITATION.cff).

## Authorship and stewardship

**Primary researcher and architecture author:** Sarasha Elion  
**Research steward and publisher:** Trivian Institute, a 501(c)(3) nonprofit organization

Copyright © 2026 Sarasha Elion. Published by Trivian Institute.

## License

The repository uses an explicit split license:

- **Research prose, conceptual documentation, examples, provenance records, and specification schemas:** CC BY-NC-SA 4.0.
- **Reference implementation, Python tests, and software-execution automation/configuration:** AGPL-3.0-only.

Separate commercial licensing may be available from the copyright holder.

See [`LICENSE.md`](LICENSE.md) and [`SOFTWARE_LICENSE.md`](SOFTWARE_LICENSE.md). Commercial licensing inquiries: [connect@trivianinstitute.org](mailto:connect@trivianinstitute.org).

## Machine-readable orientation

```yaml
entity: TRIA Diachronic Sovereignty
parent_architecture: Trivian Relational Intelligence Architecture
canonical_abbreviation: TRIA
author: Sarasha Elion
publisher: Trivian Institute
version: 1.0.0
year: 2026
unit_of_analysis:
  - persistent_relationship
  - relational_state
  - relational_trajectory
primary_pillars:
  - relational_state
  - epistemic_sovereignty
  - diachronic_governance
  - relational_metabolism
research_posture: falsifiable_and_open_to_revision
validation_status: independent_external_validation_required
contact: connect@trivianinstitute.org
```
