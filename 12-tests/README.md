# Test Layer

**Epistemic Status:** EXPERIMENTAL / FALSIFICATION SURFACE

This directory stress-tests the reference implementation and specification layer against selected governance commitments in the repository.

The tests are not evidence that the architecture is correct. Passing tests show only that this particular executable interpretation satisfies the behaviors encoded here. Failing tests are useful: they expose mismatch between implementation, specification, or normative intent.

## Current test targets

- no silent epistemic promotion;
- explicit consent revocation behavior;
- preservation of disputed state;
- inference-decay posture without invented universal thresholds;
- re-consent after material continuity change;
- dormancy as a legitimate lifecycle state;
- representative failure-mode conditions;
- JSON Schema Draft 2020-12 metavalidation.

## Running locally

Use Python 3.11 or newer:

```bash
python -m pip install -r requirements-dev.txt
pytest -q 12-tests
```

The repository CI runs the same suite on Python 3.11 and 3.12.

## What passing means

Passing tests demonstrate conformance to the behaviors currently encoded in the suite. They do **not** demonstrate factual correctness of recorded claims, legitimate consent, safe authority delegation, scientific validity, or production safety.

## Research posture

These tests deliberately avoid universal confidence scores, fixed decay rates, continuity metrics, engagement goals, or claims about machine consciousness. Test coverage should expand when new behavior becomes sufficiently specified to falsify.
