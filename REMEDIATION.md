# Frozen F029 remediation — reference/document version 1.1.1

Base: 40ee96e0034972e0264e37fa7323f5873cc0d6e0 (document version 1.1.0; no installable package version).

RelationalLedger now owns a deep copy on append and returns separate deep copies from append, events and projection reads. Caller-owned input, returned event payload and derived projection cannot rewrite retained history, including nested dict/list/set values. Duplicate identity checking and append occur under one in-process lock. Payloads reject cyclic containers and unsupported custom objects that could override copying. Public payload objects remain mutable snapshots for compatibility; they are never the retained canonical instance.

This is an in-memory reference reducer, not a transactional distributed database. extend still applies sequential appends and is not all-or-nothing; this limitation is explicit, and no compensation is implied. Event/schema shapes and last-operative-write projection behavior remain the same. Object identity across reads is intentionally no longer stable. No persisted history migration or freshness service is introduced.

Tests: 12-tests/test_frozen_remediation.py plus the unchanged external frozen F029 witness. A governed explicit new event can change later projections without rewriting the original event.
