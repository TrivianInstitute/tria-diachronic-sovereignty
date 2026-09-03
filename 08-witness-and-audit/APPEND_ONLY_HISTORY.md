# Append-Only History

**Epistemic status:** SPECIFICATION PRECURSOR

TRIA Diachronic Sovereignty favors append-oriented history for consequential relational events so that corrections do not erase the existence of prior state.

Append-only does not mean immutable belief. It means immutable provenance of change.

## Core rule

When a consequential record is corrected, disputed, superseded, revoked, or reinterpreted, the system should generally preserve the prior record and append a new event describing the change.

This allows later review to distinguish:

- what was believed or represented at the time;
- what later changed;
- why it changed;
- who or what initiated the correction;
- what authority or evidence supported the revision.

## What append-only history is not

It is not:

- a requirement to retain full transcripts;
- a requirement to retain data indefinitely;
- a prohibition on privacy-preserving deletion or redaction where legally or ethically required;
- proof that earlier records were correct;
- a substitute for data minimization.

## Corrections and supersession

A correction should preserve linkage to the prior record through an explicit relation such as:

- corrects;
- supersedes;
- revokes;
- narrows;
- disputes;
- expires;
- re-baselines.

The current operative state may exclude a superseded record while the historical event remains available under appropriate access controls.

## Retention tension

Append-oriented accountability can conflict with privacy, deletion rights, safety requirements, storage limits, or data-minimization principles.

This architecture does not assert a universal resolution.

Implementations should distinguish between:

- preservation of governance-relevant provenance;
- preservation of sensitive payloads;
- cryptographic or referential evidence that an event occurred;
- content that may lawfully or appropriately be deleted.

## Integrity

Future implementations may use technical integrity mechanisms such as hashes, signatures, chained records, or external attestations.

These are implementation options, not normative requirements of this document.

## Design principle

> Correct the relational record without pretending the incorrect state never existed.
