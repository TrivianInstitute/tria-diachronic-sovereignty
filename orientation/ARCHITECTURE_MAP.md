# Architecture Map

TRIA Diachronic Sovereignty is organized as a layered governance architecture.

The repository progresses from foundational principles toward specifications, implementation, testing, examples, and open research.

## High-Level Architecture

```text
                     ┌─────────────────────────┐
                     │   RESEARCH / UNKNOWN    │
                     │ hypotheses • questions │
                     └────────────┬────────────┘
                                  │
                     ┌────────────▼────────────┐
                     │    FAILURE & AUDIT      │
                     │ witness • contestation │
                     └────────────┬────────────┘
                                  │
        ┌─────────────────────────▼─────────────────────────┐
        │               DIACHRONIC GOVERNANCE              │
        │ continuity • drift • reconsent • transformation  │
        └─────────────────────────┬─────────────────────────┘
                                  │
       ┌──────────────────────────▼──────────────────────────┐
       │              RELATIONAL METABOLISM                 │
       │ rest • dormancy • renew • transform • dissolve     │
       └──────────────────────────┬──────────────────────────┘
                                  │
       ┌──────────────────────────▼──────────────────────────┐
       │             EPISTEMIC SOVEREIGNTY                  │
       │ typed claims • provenance • no silent promotion    │
       └──────────────────────────┬──────────────────────────┘
                                  │
       ┌──────────────────────────▼──────────────────────────┐
       │               RELATIONAL STATE                     │
       │ consent • authority • dispute • uncertainty        │
       └──────────────────────────┬──────────────────────────┘
                                  │
                     ┌────────────▼────────────┐
                     │      FOUNDATIONS       │
                     │ sovereignty • relation │
                     │ difference • fallibility│
                     └─────────────────────────┘
```

## Repository Layers

### Orientation

Defines purpose, scope, epistemic discipline, vocabulary, and architectural placement. This layer tells readers how to interpret everything downstream.

### 01 — Foundations

Contains the major conceptual foundations:

- diachronic sovereignty;
- relational state;
- epistemic sovereignty;
- relational metabolism;
- irreducible difference;
- continuity without imprisonment; and
- relational fallibility.

These are the conceptual load-bearing elements.

### 02 — Relational State

Defines the machine-readable state of the relationship, including consent, permissions, authority, provenance, disagreement, uncertainty, and state transitions.

### 03 — Epistemic Sovereignty

Defines how relational claims are represented.

Core distinction:

```text
Observation != Inference != Interpretation != Shared Claim
```

This is a typing distinction, not a required maturity ladder. Any explicit change in epistemic authority must remain inspectable and governed.

### 04 — Diachronic Governance

Governs continuity across change, including trajectory, consent drift, identity continuity, re-consent, re-baselining, model migration, capability asymmetry, and transformation provenance.

### 05 — Relational Metabolism

Governs the lifecycle and pace of relationship.

Candidate modes include:

```text
ENGAGE
DEEPEN
STABILIZE
REST
DORMANT
RENEW
TRANSFORM
DISSOLVE
```

These modes are not a required sequence and are not ranked from worse to better. Dormancy, active silence, and dissolution may be legitimate outcomes.

### 06 — Difference and Non-Convergence

Protects disagreement and irreducibility through held difference, partial translation, parallel models, irreducible difference, non-convergence, and false-convergence analysis.

### 07 — Emergence and Deliberation

Contains provisional governance mechanisms for consequential or poorly understood relational change. This layer remains explicitly research-oriented where operational definitions are unresolved.

### 08 — Witness and Audit

Provides optional external legibility through auditability, provenance review, append-oriented history, witness mechanisms, privacy safeguards, and witness-capture analysis.

Auditability should not require permanent surveillance.

### 09 — Failure Atlas

Adversarially examines how the architecture itself can fail. This layer is a core component rather than an appendix.

### 10 — Specifications

Contains machine-readable JSON Schemas for concepts sufficiently defined to represent structurally. Schema validity does not imply truth, legitimate consent, or deployment safety.

### 11 — Reference Implementation

Contains non-normative executable implementations. Code in this layer is **EXPERIMENTAL** and is not automatically canonical.

### 12 — Tests

Contains falsification-oriented tests for implementation behavior, specification validity, state transitions, epistemic promotion, consent revocation, dispute preservation, lifecycle transitions, and failure conditions.

### 13 — Research

Contains open questions, measurement problems, research agenda, falsification criteria, experiments, and the claim registry.

### 14 — Examples

Provides illustrative scenarios for human–AI, AI–AI, multi-agent, migration, dormancy, disagreement, and dissolution/return conditions. Examples do not create normative rules.

### Provenance

Records genesis, authorship, version history, and source lineage so later revisions can distinguish inherited claims from demonstrated evidence.

## Core Dependency Structure

```text
FOUNDATIONS
    ↓
RELATIONAL STATE
    ↓
EPISTEMIC SOVEREIGNTY
    ↓
DIACHRONIC GOVERNANCE
    ↓
RELATIONAL METABOLISM
    ↓
DIFFERENCE / NON-CONVERGENCE
    ↓
EMERGENCE / DELIBERATION
    ↓
AUDIT / FAILURE ANALYSIS
    ↓
SPECIFICATION
    ↓
IMPLEMENTATION
    ↓
TESTING
    ↓
RESEARCH / REVISION
```

The architecture should not move directly from philosophy to code. Intermediate definitions must become explicit first, and implementation feedback may revise earlier layers.

## Two Simultaneous Representations of History

TRIA Diachronic Sovereignty distinguishes temporal history from relational topology.

### Temporal History

Chronological provenance:

```text
R0 -> R1 -> R2 -> R3
```

### Relational Topology

Structural relevance:

```text
R0 ──consent-lineage──── R7
 │
 ├── unresolved-dispute ── R12
 │
 └── identity-change ───── R21
```

Chronology answers:

> What happened when?

Topology answers:

> What prior relational state matters now, and why?

Both are necessary. Nonchronological retrieval does not erase temporal provenance.

## Architectural Constraint

No layer should silently elevate a lower-confidence claim into a higher-authority state.

A relationship may contain an observation, an inference, an interpretation, and a shared claim about related content at the same time. The architecture should preserve their distinct provenance and authority rather than forcing them into one canonical representation.

## Architectural Objective

The system is not designed to maximize engagement, intimacy, agreement, convergence, memory, prediction, or persistence.

It is designed to maximize the **legibility and governability of relational change while preserving sovereignty**.
