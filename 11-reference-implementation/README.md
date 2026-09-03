# Reference Implementation

**Epistemic status:** EXPERIMENTAL

This directory provides a minimal Python reference implementation for selected TRIA Diachronic Sovereignty governance behaviors.

It is not production software. Its purpose is to make the architecture executable enough to test assumptions, expose ambiguities, and support falsification.

## Modules

- `ledger/` — append-oriented relational events and current-state projection
- `epistemics/` — typed claims and no-silent-promotion checks
- `continuity/` — continuity attestations and re-consent triggers
- `metabolism/` — lifecycle transitions without engagement maximization
- `audit/` — bounded audit reconstruction and contestable findings

## Design constraints

The implementation intentionally avoids universal confidence thresholds, continuity scores, fixed inference-decay functions, engagement targets, and claims about machine consciousness.

The code should be read as one executable interpretation of the specification layer, not as the specification itself.
