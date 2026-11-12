# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [bc4fe74] |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added ADR-0001, RC-008 and RC-009 (MIL-001) | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-003] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [ADR-0001] | [RC-004], [RC-009] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001] | - | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001] | - | [RC-006] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001] | - | [RC-007] |
| [ADR-0001] | ADR | - | - | [BC-001] | [MIL-001] | [RC-008] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | - | - | - | Gap |
| CN-002 | - | - | - | Gap |
| CN-003 | - | - | - | Gap |
| CN-004 | - | - | - | Gap |
| CN-005 | - | - | - | Gap |
| CN-006 | - | - | - | Gap |
| CN-007 | - | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

No views, ADRs or test plans exist yet, so concerns are `Gap` until MIL-002 to MIL-004 deliver code and tests. In Downstream, `-` means nothing is built on the document yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-data-preparation.md
[MIL-003]: ../milestones/mil-003-charts.md
[MIL-004]: ../milestones/mil-004-docs-and-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-foundation.md
[RC-005]: ./reviews/rc-005-mil-002-data-preparation.md
[RC-006]: ./reviews/rc-006-mil-003-charts.md
[RC-007]: ./reviews/rc-007-mil-004-docs-and-wiki.md
[RC-008]: ./reviews/rc-008-adr-0001-pandas-in-infrastructure.md
[RC-009]: ./reviews/rc-009-mil-001-code.md
[ADR-0001]: ../adr/adr-0001-pandas-in-infrastructure.md
[bc4fe74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/commit/bc4fe74dfe75aeeeb4608c64d8dc3ec0b2f17d10
