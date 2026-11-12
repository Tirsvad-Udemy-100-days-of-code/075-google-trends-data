# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Go in RC-001 (autonomous, not independent) | pending |

---

## Executive Summary

This project delivers the Udemy "100 Days of Code" Day 75 assignment as a
clean, runnable Python project: it combines Google Trends search-interest data
with Tesla and Bitcoin prices and the US unemployment rate, resamples them to a
common monthly periodicity and plots them as styled Matplotlib charts. The
result is a public repository with readable code that keeps the assignment's
names, a Jupyter notebook, a README and a three-language wiki (English, Danish,
Bahasa Malaysia) that explains what each lecture step teaches.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: Business
Case, Stakeholder Analysis, Project Plan and milestones are written and
reviewed before any code. Quality is described with ISO/IEC 25010:2023
characteristics. Code follows the framework's Python conventions and the Clean
Architecture layering (data preparation logic apart from plotting and file
access).

## Problem Statement

A course participant who finishes the lecture has a notebook that only runs in
Google Colab, with data files and code mixed together. Other participants and
visitors cannot easily run, test or learn from it, and the reasoning behind each
step (resampling, locators, grids, rolling averages) is not written down.

## Business Opportunity

Turning the exercise into a tested, documented project makes it a reusable
reference: coursists can compare solutions, and viewers on GitHub can browse a
small, dependency-light data-visualisation example with explanations in three
languages.

## Objectives

1. Reproduce every lecture step (exploration, cleaning, resampling, Tesla,
   Bitcoin, unemployment, rolling average, 2020 data) in tested Python
   functions that keep the assignment's names.
2. Provide a Jupyter notebook that runs locally in a `.venv` and shows the
   charts.
3. Provide a README with run and test instructions and a screenshot for every
   lecture step.
4. Provide a wiki in English, Danish and Bahasa Malaysia that explains what was
   gained in each lecture step, with the same screenshots.
5. Publish the repository with a description and topics and a history made of
   reviewed pull requests, one per milestone.

## Scope

### In Scope

- Loading, exploring and cleaning the five course CSV files.
- Resampling daily Bitcoin prices to monthly data.
- Charts: Tesla, Bitcoin, unemployment, 6-month rolling average, unemployment
  including 2020.
- Python 3.13 or newer, `venv`, `pyproject.toml`, Python `.gitignore`.
- Jupyter notebook, README, unit tests, wiki in `en`, `da` and `ms`.
- Static analysis with opengrep before each push.

### Out of Scope

- Downloading live data from Google Trends or any price API.
- Hosting, a web UI or packaging for PyPI.
- Google Colab specific setup.
- Financial advice: the charts illustrate a lecture only.

## Expected Benefits

### Tangible Benefits

- A repository others can clone, run and test with documented commands.
- A screenshot and an explanation for each lecture step.

### Intangible Benefits

- Deeper understanding of time-series resampling and chart styling.
- A worked example of the framework's plan-first workflow.

## Strategic Alignment

The project supports the participant's learning goal in the 100 Days of Code
bootcamp and the practice of publishing small, reviewed, documented work.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps implemented | 8 of 8 steps have a function and a test | Count of lecture steps with a passing test |
| 2 | Test suite | 100 % of tests pass on Python 3.13 | `python -m pytest` exit code 0 |
| 3 | Runtime dependencies | No more than pandas and matplotlib | Entries in `[project.dependencies]` |
| 4 | Screenshots | One per lecture step in README and in each wiki language | Count of images referenced per page |
| 5 | Wiki languages | 3 languages with the same page set | Files `*.md`, `*-da.md`, `*-ms.md` |
| 6 | Static analysis | 0 opengrep findings of severity error before push | opengrep report |
| 7 | Repository metadata | Description and at least 5 topics set | Gitea repository API |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The course CSV files are not available in the repository | Code cannot be run on real data | Ask the Product Owner to supply or approve downloading them; tests use small fixtures meanwhile |
| Gitea API or wiki token rejected | Description, topics or wiki not published | Check the token scope early; report and stop instead of working around it |
| Matplotlib behaves differently per platform | Screenshots differ from the lecture | Use the `Agg` backend for screenshots and set a minimum version |
| Pandas resample alias `M` is deprecated | Warning or failure on new pandas | Use the current alias `ME` and test it |
| Translations contain errors | Misleading wiki for Danish or Malay readers | English is authoritative; keep pages short; Product Owner reviews |

## Assumptions

- The Product Owner is S01 and S01 reviews every artifact; where a reviewer is
  another stakeholder, the AI stands in and the review says so.
- The course data files are course material the Product Owner may use for this
  personal learning project.
- S02 and S03 are not interviewed; their needs are taken from the Product
  Owner's brief.

## Constraints

- Python 3.13 or newer; `venv` for the environment; `pyproject.toml` for
  configuration.
- Folders `src/`, `tests/` and `docs/`.
- Few runtime dependencies; Jupyter and test tools are development dependencies.
- Tokens come from `.env` for personal use and are never imported by the project
  or committed.
- GUI or end-to-end tests do not run on the host desktop.
- One branch and one pull request per milestone.

## Cost–Benefit Assessment

Qualitative, because this is an unpaid learning project and no revenue exists.

| Costs | Benefits |
| --- | --- |
| Product Owner time to accept the plan and review the pull requests | A tested, documented reference project |
| Effort to write three wiki languages | Readers in English, Danish and Bahasa Malaysia |
| No monetary cost | Practice of the framework workflow |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Learns the material, owns, builds and reviews the project |
| S02 | Wants readable, runnable code with the assignment's names and run instructions |
| S03 | Wants a clear description, topics and README and no unnecessary runtime dependencies |

## Recommendation

Proceed — the scope is small, the value is clear and the risks are mitigated.

---

[SA-001]: ./stakeholder-analysis.md
