# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Go in RC-002 (autonomous, not independent) | [bc4fe74] |

---

## Purpose

Identify who is affected by the Day 75 Google Trends project and what each needs,
using a power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer, reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Learn the lecture content and publish a tidy, correct project |
| S02 | Udemy coursists | Fellow course participants | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and run instructions |
| S03 | GitHub viewers | Repository visitors | Public | LOW | MEDIUM | Keep Informed | Clear description, topics and README, no heavy runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely:** S01 decides scope, writes, reviews and accepts everything.
- **Keep Informed:** S02 and S03 cannot change the project but use its output; a
  good README and wiki serve them.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is reproduced correctly | Functionality |
| CN-002 | S01 | Work is reviewed and tracked by pull request per step | Supportability |
| CN-003 | S02 | Code is readable and keeps the assignment's function names | Usability |
| CN-004 | S02 | Instructions to create a `.venv`, run the notebook and run tests work | Usability |
| CN-005 | S03 | Repository has a description, topics and README | Usability |
| CN-006 | S03 | No unnecessary runtime dependencies | Implementation constraints |
| CN-007 | S02 | Wiki explains each step in English, Danish or Bahasa Malaysia | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat with S01 | At plan and at run end | Plan, then run summary | All |
| CM-002 | Pull request | One per milestone | Reviewed change | All |
| CM-003 | README and wiki | At release | Instructions and explanations | MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Many features (notebook, tests, wiki) against few dependencies | S01, S03 | Jupyter and test tools are development dependencies; runtime stays pandas and matplotlib |
| Assignment's names against modern code style | S02, S01 | Keep the assignment's names for public functions; follow Python conventions inside |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1 and 5 |
| S02 | CN-003, CN-004, CN-007 | [BC-001] objectives 2, 3 and 4 |
| S03 | CN-005, CN-006 | [BC-001] objectives 3 and 5 |

## Sign-Off

Pending review by S01.

---

[BC-001]: ./business-case.md
[bc4fe74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/commit/bc4fe74dfe75aeeeb4608c64d8dc3ec0b2f17d10
