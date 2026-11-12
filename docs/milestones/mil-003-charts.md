# MIL-003 Charts

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Go in RC-006 (autonomous, not independent) | [bc4fe74] |

---

## Purpose

Decide whether the visualisation layer reproduces every lecture chart: Tesla, Bitcoin, unemployment, the 6-month rolling average and unemployment including 2020, each saved as an image.

## Deliverable

A module `src/google_trends_data/charts.py` with one function per chart that returns a Matplotlib figure, tests that check axis labels, limits and line styles, and a PNG per lecture step under `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each chart function returns a figure with two y-axes and the lecture's title | Yes | No |
| 2 | Tesla uses the `YearLocator`, `MonthLocator` and `DateFormatter` | Yes | No |
| 3 | Bitcoin price uses a dashed line and search uses circle markers | Yes | No |
| 4 | Unemployment chart has a grey dashed grid | Yes | No |
| 5 | Rolling chart uses a window of 6 months | Yes | No |
| 6 | A PNG exists for each lecture step | Yes | No |
| 7 | Tests run with the `Agg` backend and pass | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Charts use the cleaned and resampled data |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1; success criteria 1, 2, 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-19 — within the Business Case constraints (no fixed deadline).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Basic Tesla chart with two axes | Plot Tesla price and search volume with `twinx()`, then add colours (hex red for price, skyblue for search). | No | |
| 2 | Style Tesla chart | Figure size 14x8, dpi 120, fonts 14, rotated x ticks, title, thicker lines, axis limits and `plt.show()`. | No | |
| 3 | Time axis locators for Tesla | Use `matplotlib.dates` `YearLocator`, `MonthLocator` and `DateFormatter` for major and minor ticks. | No | |
| 4 | Bitcoin chart with line style and markers | Reproduce the Bitcoin news search against the resampled price with a dashed price line and circle markers. | No | |
| 5 | Unemployment chart with grid | Plot unemployment benefits searches against the unemployment rate with a grey dashed grid to see seasonality. | No | |
| 6 | Rolling average chart | Plot the 6-month rolling mean of searches and unemployment to show searches lead the rate. | No | |
| 7 | Unemployment chart including 2020 | Read `UE Benefits Search vs UE Rate 2004-20.csv` and plot the pandemic spike. | No | |

---

[BC-001]: ../business-case.md
[bc4fe74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/commit/bc4fe74dfe75aeeeb4608c64d8dc3ec0b2f17d10
