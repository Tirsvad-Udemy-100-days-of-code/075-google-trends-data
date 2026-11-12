# Architecture Decision Record

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Go in RC-008 (autonomous, not independent) | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The framework prefers polars for dataframes and allows pandas only when a required library forces it, confined to an adapter. The Day 75 lecture teaches the pandas API (`read_csv`, `isna`, `dropna`, `to_datetime`, `resample`, `rolling`, `describe`), and S02 compares solutions that use those calls. The framework also asks for the layers `domain`, `application` and `infrastructure`, with no dataframe types in the inner layers.

Options:

1. Use polars everywhere. This follows the framework default but changes every lecture step, so S02 cannot compare their solutions.
2. Use pandas everywhere, as in the lecture. This is simple but puts dataframes in the business rules.
3. Use pandas, confined to the infrastructure layer, and pass plain dataclasses between layers.

## Decision

Use pandas, because the lecture requires it, and confine it to the infrastructure layer; the domain and application layers use plain dataclasses and protocols only. Matplotlib is confined to infrastructure in the same way.

## Consequences

**Positive:**

- The code keeps the lecture's pandas calls, so S02 can compare solutions.
- Domain and application tests need no pandas, files or display.
- Dependencies stay at pandas and matplotlib (success criterion 3 of the Business Case).

**Negative:**

- Data is mapped between dataframes and plain dataclasses, which adds some code.
- The project deviates from the framework default (polars); this ADR is the reason.

## Affected Artifacts

- [BC-001] — objective 1 and the dependency constraint: the runtime dependencies are pandas and matplotlib

---

[BC-001]: ../business-case.md
