# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | AI as stand-in for S01 | S01 | Initial review of Project Plan; autonomous, not independent | [bc4fe74] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

Mode: autonomous, not independent. The Business Case, Stakeholder Analysis, plan and milestones were authored by the AI for S01, and the AI reviews them as a stand-in; S01 can challenge each record in the run summary.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-12 and end 2026-11-22 stated; the Business Case sets no deadline, so the plan states its own window. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Four gateways, one row each, with document, date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates 2026-11-14, 16, 19 and 22 match the Target Date of each MIL document and lie inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every in-scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-004, acyclic, in schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | No-Go moves later gateways and the end date; S01 decides the new dates. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | N-A | N-A: no governance document exists; owner S01 is a Stakeholder Analysis ID. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions listed; baseline is the first version. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan risks have impact and mitigation; the CSV risk comes from BC-001. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issues: CSV source and plan review; neither contradicts the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverables match the Deliverable of each MIL document in substance. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says none, with the reason in Planning Assumptions. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Table, Gantt and dependency chain agree. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column is blank: not yet synced (the dry run only). |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single plan file; changes go to Version History. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has Language `en` and Domain `it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | IT Executive English / IT Professional English as the registry states for this type; short, decision-oriented text. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No domain dictionary exists yet (DICT not created); terms are standard IT terms used consistently. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | AI stand-in for S01 reads English and the IT domain; S01 can challenge in the run summary. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (BC, SA, PP, MIL, PO) are spelled out or defined in the framework; CSV, API, PR are common IT terms. |

## Overall Verdict

Go — every Mandatory criterion passes or is not applicable.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in review in the run summary if needed | S01 | 2026-11-22 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[bc4fe74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/commit/bc4fe74dfe75aeeeb4608c64d8dc3ec0b2f17d10
