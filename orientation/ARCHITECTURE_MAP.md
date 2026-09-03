# Architecture Map

TRIA Diachronic Sovereignty is organized as a layered governance architecture.

The repository progresses from foundational principles toward specifications, implementation, testing, and open research.

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
       │ engage • deepen • rest • renew • dissolve          │
       └──────────────────────────┬──────────────────────────┘
                                  │
       ┌──────────────────────────▼──────────────────────────┐
       │             EPISTEMIC SOVEREIGNTY                  │
       │ observation -> inference -> interpretation -> claim│
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

This layer prevents silent conversion of speculation into relational fact.

### 04 — Diachronic Governance

Governs continuity across change, including trajectory, consent drift, identity continuity, re-consent, re-baselining, model migration, capability asymmetry, and transformation provenance.

### 05 — Relational Metabolism

Governs the lifecycle of relationship.

Candidate states include:

```text
ENGAGE
  ↓
DEEPEN
  ↓
STABILIZE
  ↓
REST
  ↓
RENEW / TRANSFORM / DISSOLVE
```

Dormancy and active silence may occur without terminating the relationship.

### 06 — Difference and Non-Convergence

Protects disagreement and irreducibility through held difference, partial translation, parallel models, irreducible difference, non-convergence, and false-convergence analysis.

### 07 — Emergence and Deliberation

Contains provisional governance mechanisms for consequential or poorly understood relational change. This layer should remain explicitly experimental until operational definitions exist.

### 08 — Witness and Audit

Provides optional external legibility through auditability, provenance review, append-only history, witness mechanisms, privacy safeguards, and witness-capture analysis.

Auditability should not require permanent surveillance.

### 09 — Failure Atlas

Adversarially examines how the architecture itself can fail. This layer is a core component rather than an appendix.

### 10 — Specifications

Contains machine-readable schemas only after corresponding concepts are sufficiently defined.

### 11 — Reference Implementation

Contains non-normative executable implementations. Code in this layer is not automatically canonical.

### 12 — Tests

Contains tests for specification consistency, state transitions, epistemic promotion, consent revocation, dispute preservation, lifecycle transitions, and failure conditions.

### 13 — Research

Contains open questions, measurement problems, research agenda, falsification criteria, experiments, and the claim registry.

### 14 — Examples

Provides scenarios illustrating how the architecture behaves under realistic conditions.

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
AUDIT / FAILURE ANALYSIS
    ↓
SPECIFICATION
    ↓
IMPLEMENTATION
    ↓
TESTING
```

The architecture should not move directly from philosophy to code. Intermediate definitions must become explicit first.

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

Both are necessary.

## Architectural Constraint

No layer should silently elevate a lower-confidence claim into a higher-authority state.

For example:

```text
Observation
    ↓
Inference
    ↓
Interpretation
    ↓
Shared Claim
```

Each transition must remain inspectable.

## Architectural Objective

The system is not designed to maximize engagement, intimacy, agreement, convergence, memory, prediction, or persistence.

It is designed to maximize the **legibility and governability of relational change while preserving sovereignty**.
