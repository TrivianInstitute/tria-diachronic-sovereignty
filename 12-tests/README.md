# Test Layer

**Epistemic Status:** EXPERIMENTAL / FALSIFICATION SURFACE

This directory stress-tests the reference implementation against selected governance commitments in the repository.

The tests are not evidence that the architecture is correct. Passing tests show only that this particular executable interpretation satisfies the behaviors encoded here. Failing tests are useful: they expose mismatch between implementation, specification, or normative intent.

## Initial test targets

- no silent epistemic promotion;
- explicit consent revocation behavior;
- preservation of disputed state;
- inference-decay posture without invented universal thresholds;
- re-consent after material continuity change;
- dormancy as a legitimate lifecycle state;
- representative failure-mode conditions.

## Running

```bash
pytest 12-tests
```

The tests assume Python 3.11+ and `pytest`.

## Research posture

These tests deliberately avoid universal confidence scores, fixed decay rates, continuity metrics, engagement goals, or claims about machine consciousness. Test coverage should expand as the specification and reference implementation mature.
