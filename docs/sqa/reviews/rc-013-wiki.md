# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | AI as stand-in for S01 | S01 | Review of the project wiki (docs/wiki, en, da, ms); autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-WIKI-001]
- Scope: full review of docs/wiki: 14 pages in English, Danish and Bahasa Malaysia and the sidebar; the pages are checked by a script (page sets, language lines, identical code blocks and images, no dead links) and by reading
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

Mode: autonomous, not independent. The AI authored the work for S01 and reviews it as a stand-in; S01 can challenge the record in the run summary.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, one list of the English pages with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Every English page is in the list; the script found no dead link. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last: English, Dansk, Bahasa Melayu linking to Home, Home-da, Home-ms. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | The sidebar is written by hand; a comment says so and says it follows the page list in Home. No generator exists. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English is the PO language and is present; Danish and Bahasa Malaysia are added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | The script found 14 pages in each language. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | `-da` and `-ms` suffixes, English has none. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | The script found code blocks and image links identical in all languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | PENDING: the publish workflow runs after the merge; a follow-up review checks the host. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | N-A: no change to layout rules. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 43 files are directly in docs/wiki. |

## Overall Verdict

Go-with-conditions — criterion 14 is Pending until the merge has published the wiki. The Danish and Bahasa Malaysia text was machine translated by the AI and read only by the AI; no human reader of Bahasa Malaysia has checked it.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Verify the published wiki (sidebar, pages, images) after the merge, and ask a reader of Bahasa Malaysia to check the Malay pages | S01 | 2026-11-22 |

---

[MIL-004]: ../../milestones/mil-004-docs-and-wiki.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
