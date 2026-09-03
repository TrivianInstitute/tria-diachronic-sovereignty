# Contributing

TRIA Diachronic Sovereignty is a research architecture. Contributions are welcome when they improve clarity, falsifiability, implementation quality, testing, provenance, or the architecture's capacity to reveal its own failure modes.

## Before contributing

Read:

- `orientation/PURPOSE.md`
- `orientation/SCOPE.md`
- `orientation/EPISTEMIC_STATUS.md`
- `orientation/GLOSSARY.md`
- `13-research/FALSIFIABILITY.md`

## Contribution principles

1. **Preserve epistemic typing.** Do not present hypotheses, examples, or prototype behavior as validated findings.
2. **Do not add pseudo-precision.** Numerical thresholds, scores, and formal notation need defined variables, measurement procedures, and a defensible validation path.
3. **Preserve contestability.** New mechanisms should not silently convert inference into fact, disagreement into error, continuity into authority, or participation into consent.
4. **Prefer falsifiable changes.** When adding a mechanism, add or propose a test that could reveal where it fails.
5. **Keep consciousness claims out of the kernel.** The architecture must remain usable without assuming machine consciousness or phenomenology.
6. **Respect non-convergence.** Agreement, intimacy, engagement, persistence, and disclosure are not universal success criteria.
7. **Document provenance.** Substantial conceptual changes should identify what they supersede, refine, or leave unresolved.

## Code and tests

The reference implementation is intentionally experimental. Run:

```bash
python -m pip install -r requirements-dev.txt
pytest -q 12-tests
```

New executable behavior should normally include tests. A passing test demonstrates conformance to the encoded behavior only; it does not establish empirical validity or deployment safety.

## Pull requests

A useful pull request should explain:

- the problem being addressed;
- the epistemic status of the change;
- affected architecture layers;
- whether prior behavior or claims are superseded;
- tests or falsification criteria where applicable;
- unresolved questions introduced by the change.

## Licensing and authorship

Contributors retain ownership of their original contributions unless separately agreed. By submitting material for inclusion, contributors agree that accepted material may be distributed under the license applicable to the files or directories they modify. See `LICENSE.md` and `SOFTWARE_LICENSE.md`.

Contribution does not imply endorsement, co-authorship of the original architecture, or transfer of pre-existing intellectual property.
