# Multi-Agent Field

**Epistemic Status:** ILLUSTRATIVE / NON-NORMATIVE

## Purpose

This example shows how diachronic sovereignty can apply when several agents and human authorities coordinate through partially shared state.

## Scenario

A research program uses four software agents:

- one gathers sources;
- one evaluates claims;
- one manages project memory;
- one proposes actions.

A human research lead retains final authority over publication and external action. The agents share selected governance state, but not every claim, permission, or interpretation is globally visible.

Over time, one agent begins treating another agent’s recurring interpretation as a field-wide assumption.

## Governance response

The architecture should avoid automatic propagation of agreement across the network.

Relevant controls include:

- preserve claim authorship and provenance at each edge;
- distinguish local acknowledgement from global Shared Claim status;
- prevent one agent’s authority from silently propagating to another;
- maintain contested or parallel models where appropriate;
- record which model informed an action and which alternatives remained unresolved;
- minimize shared state to governance-relevant information rather than full-transcript replication.

## Example sequence

1. Agent A observes repeated evidence supporting hypothesis H.
2. Agent B interprets H as the most plausible explanation.
3. Agent C stores B’s interpretation with correct epistemic typing.
4. Agent D retrieves the interpretation and proposes action as though H were established.
5. Governance checks detect that no field-wide Shared Claim exists.
6. The proposal is relabeled as conditional on B’s interpretation.
7. The human lead may act, defer, request review, or preserve multiple models.

## What this example demonstrates

Multi-agent persistence should not turn repeated transmission into consensus. Provenance, scope, authority, and disagreement must survive propagation across relational edges.
