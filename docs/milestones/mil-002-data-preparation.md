# MIL-002 Data Preparation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Go in RC-005 (autonomous, not independent) | pending |

---

## Purpose

Decide whether the data layer is correct: the five course CSV files load, are explored, cleaned, converted to datetimes and made comparable by resampling daily Bitcoin prices to monthly data.

## Deliverable

A tested module `src/google_trends_data/data.py` with functions to load, describe, check for missing values, drop them, convert dates and resample, with unit tests and the CSV files in `data/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The five CSV files are in `data/` and load in a test | Yes | No |
| 2 | Shapes are Tesla 124x3, unemployment 181x3 and Bitcoin price 2204 rows before cleaning | Yes | No |
| 3 | Exactly 2 missing values are found in the Bitcoin price data and removed | Yes | No |
| 4 | All date columns are `datetime64` after conversion | Yes | No |
| 5 | The monthly Bitcoin price has 73 rows, like the Bitcoin search data | Yes | No |
| 6 | Tests pass with no pandas deprecation warning | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the project skeleton |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1; success criteria 1, 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — within the Business Case constraints (no fixed deadline).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add course CSV files to data/ | Place the five course CSV files in `data/`. The files come from the course zip; the Product Owner supplies them or approves the download. | No | |
| 2 | Load and explore the DataFrames | Add `load_data()` and `describe_data()` giving shape, column names, min, max and `.describe()` for Tesla, unemployment and Bitcoin, and state each series' periodicity. | No | |
| 3 | Find and remove missing values | Add `count_missing()` and `drop_missing()` using `.isna()` and `.dropna()`; locate the rows with NaN in the Bitcoin price data. | No | |
| 4 | Convert strings to datetime | Add `convert_dates()` using `pd.to_datetime` on the MONTH and DATE columns of all DataFrames and test the dtype. | No | |
| 5 | Resample Bitcoin prices to monthly | Add `resample_monthly()` with the `ME` alias taking the last price of the month, so price and search data are comparable. | No | |

---

[BC-001]: ../business-case.md
