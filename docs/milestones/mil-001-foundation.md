# MIL-001 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Go in RC-004 (autonomous, not independent) | pending |

---

## Purpose

Decide whether the project skeleton is ready for feature work: a Python 3.13 project with `pyproject.toml`, `.venv` instructions, a Python `.gitignore`, a README from the framework template, repository description and topics, and opengrep scanning in place.

## Deliverable

A pull request that adds `pyproject.toml`, `.gitignore`, the `src/` and `tests/` skeleton with one passing smoke test, a README with `.venv`, install, run and test instructions, and a repository on the git host that has a description and topics.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `requires-python` is `>=3.13` and the venv instructions run without error | Yes | No |
| 2 | `python -m pytest` passes in a fresh `.venv` | Yes | No |
| 3 | The repository has a description and at least 5 topics | Yes | No |
| 4 | `check-readme.sh` passes for the README | Yes | No |
| 5 | opengrep reports no error-severity finding | Yes | No |
| 6 | `.env` is ignored and is not read by project code | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5; success criteria 2, 3, 6, 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-14 — within the Business Case constraints (no fixed deadline).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Configure pyproject.toml and src/tests skeleton | Add `pyproject.toml` (Python >=3.13, pandas and matplotlib as the only runtime dependencies; pytest and jupyter as the `dev` extra), the `src/google_trends_data/` package and a smoke test, so every later task has a place to live. | No | |
| 2 | Add Python .gitignore | Add the standard Python `.gitignore` plus `.venv/`, `.env`, notebook checkpoints and build output so secrets and environments are never committed. | No | |
| 3 | Write README with .venv instructions | Create `README.md` from the framework template with how to create and use a local `.venv`, run `python -m pip install --upgrade pip`, install the project, run the notebook and run the tests. | No | |
| 4 | Set repository description and topics | Use the Gitea API with the token from `.env` (personal use only, never imported by the project) to set a description and topics on the repository. | No | |
| 5 | Add opengrep scan step | Document and run `~/.opengrep/cli/latest/opengrep.exe` locally before each push; record the command in the README and fix any error-severity finding. | No | |

---

[BC-001]: ../business-case.md
