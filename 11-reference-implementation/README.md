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
- `measurement/` — semantic validation of Rosetta 2.0 multiplicative snapshots

## Design constraints

The implementation intentionally avoids universal confidence thresholds, continuity scores, fixed inference-decay functions, engagement targets, and claims about machine consciousness.

The code should be read as one executable interpretation of the specification layer, not as the specification itself.

## Running the test surface

From the repository root:

```bash
python -m pip install -r requirements-dev.txt
pytest -q 12-tests
```

Passing tests show only that this implementation exhibits the encoded behavior. They do not establish scientific validity, legitimate consent, correct authority, or deployment safety.

## License

Covered executable software in this directory is licensed under **AGPL-3.0-only** unless a file states otherwise. See [`../SOFTWARE_LICENSE.md`](../SOFTWARE_LICENSE.md).

The surrounding research architecture and machine-readable specifications are licensed separately as described in [`../LICENSE.md`](../LICENSE.md).
