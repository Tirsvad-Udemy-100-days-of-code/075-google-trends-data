# MIL-004 Documentation and Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Go in RC-007 (autonomous, not independent) | pending |

---

## Purpose

Decide whether the project is ready to share: the Jupyter notebook runs, the README shows a screenshot per lecture step, and the wiki exists in English, Danish and Bahasa Malaysia and explains what each step teaches.

## Deliverable

`notebooks/google_trends.ipynb`, the finished `README.md`, `docs/wiki/` with `Home`, step pages, sidebar in `en`, `da` and `ms`, and the wiki published to the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The notebook runs top to bottom in the `.venv` with `jupyter nbconvert --execute` | Yes | No |
| 2 | README shows one screenshot for each lecture step | Yes | No |
| 3 | Wiki has the same page set in `en`, `da` and `ms` (`*.md`, `*-da.md`, `*-ms.md`) | Yes | No |
| 4 | Each wiki page has the screenshot and a section on what was gained | Yes | No |
| 5 | `check-readme.sh` and `check-languages.sh` pass | Yes | No |
| 6 | opengrep reports no error-severity finding | Yes | No |
| 7 | Wiki is published and readable on the git host | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Screenshots come from the charts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 2, 3, 4; success criteria 4, 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22 — within the Business Case constraints (no fixed deadline).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create Jupyter notebook | Create `notebooks/google_trends.ipynb` that imports the package and walks the lecture steps, executed with nbconvert in the `.venv`. | No | |
| 2 | Generate screenshots for every lecture step | Script that writes one PNG per step to `docs/images/` using the `Agg` backend; non-chart steps (exploration, cleaning) are rendered output images. No desktop GUI is used. | No | |
| 3 | Finish README with screenshots | Add the step-by-step section with an image per lecture step, run and test instructions and the opengrep command. | No | |
| 4 | Write English wiki | Create `docs/wiki/` pages in English following `framework/process/wiki.md`: Home, one page per lecture step with what was gained, sidebar. | No | |
| 5 | Write Danish wiki | Translate every English page to Danish (`-da`), same page set and screenshots. | No | |
| 6 | Write Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia (`-ms`), same page set and screenshots. | No | |
| 7 | Publish the wiki | Publish `docs/wiki/` to the Gitea wiki using the wiki token from `.env` (personal use only). | No | |

---

[BC-001]: ../business-case.md
