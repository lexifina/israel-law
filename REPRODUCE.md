# How this repository was made (Israel)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Wikidata: items that are instances of "Basic Laws of Israel" (Q2368137), via the Wikidata Query Service | <https://www.wikidata.org/wiki/Q2368137> | 2026-10-30 | CC0 1.0 |
| UN Treaty Collection (MTDSG status pages) | <https://treaties.un.org/> | 2026-10-29 | Facts only (treaty action, date, depositary); no text copied |
| Hebrew Wikisource (he.wikisource.org), Basic Laws project pages | <https://he.wikisource.org/wiki/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%94:%D7%97%D7%95%D7%A7%D7%99_%D7%99%D7%A1%D7%95%D7%93> | 2026-10-30 | Public domain in Israel: Copyright Act, 5768-2007, s. 6 ("Copyright shall not subsist in statutes, regulations, Knesset Records and judicial decisions") |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `catalogue` | Catalogue of the Basic Laws of Israel (facts only, no law text) | 13 | 1958-02-12 to 2018-07-19 |
| `treaties` | Treaty actions of Israel (UN Treaty Collection) | 56 | 1949-06-21 to 2016-11-22 |
| `basic-law-the-president` | Basic Law: The President of the State (חוק-יסוד: נשיא המדינה), current version, Hebrew | 1 | 2026-09-09 to 2026-09-09 |
| `basic-law-human-dignity-and-liberty` | Basic Law: Human Dignity and Liberty (חוק-יסוד: כבוד האדם וחירותו), current version, Hebrew | 1 | 2025-01-24 to 2025-01-24 |
| `basic-law-the-military` | Basic Law: The Military (חוק-יסוד: הצבא), current version, Hebrew | 1 | 2025-07-27 to 2025-07-27 |
| `basic-law-state-comptroller` | Basic Law: The State Comptroller (חוק-יסוד: מבקר המדינה), current version, Hebrew | 1 | 2026-09-09 to 2026-09-09 |
| `basic-law-israel-lands` | Basic Law: Israel Lands (חוק-יסוד: מקרקעי ישראל), current version, Hebrew | 1 | 2024-05-08 to 2024-05-08 |
| `basic-law-jerusalem` | Basic Law: Jerusalem, the Capital of Israel (חוק-יסוד: ירושלים בירת ישראל), current version, Hebrew | 1 | 2024-10-30 to 2024-10-30 |
| `basic-law-state-economy` | Basic Law: The State Economy (חוק-יסוד: משק המדינה), current version, Hebrew | 1 | 2026-01-08 to 2026-01-08 |
| `basic-law-the-judiciary` | Basic Law: The Judiciary (חוק-יסוד: השפיטה), current version, Hebrew | 1 | 2026-06-14 to 2026-06-14 |
| `basic-law-freedom-of-occupation` | Basic Law: Freedom of Occupation (חוק-יסוד: חופש העיסוק), current version, Hebrew | 1 | 2025-01-24 to 2025-01-24 |
| `basic-law-the-government` | Basic Law: The Government (חוק-יסוד: הממשלה), current version, Hebrew | 1 | 2026-03-30 to 2026-03-30 |
| `basic-law-the-knesset` | Basic Law: The Knesset (חוק-יסוד: הכנסת), current version, Hebrew | 1 | 2026-08-09 to 2026-08-09 |
| `basic-law-referendum` | Basic Law: Referendum (חוק-יסוד: משאל עם), current version, Hebrew | 1 | 2020-07-22 to 2020-07-22 |
| `basic-law-nation-state` | Basic Law: Israel, the Nation State of the Jewish People (חוק-יסוד: ישראל – מדינת הלאום של העם היהודי), current version, Hebrew | 1 | 2020-10-25 to 2020-10-25 |

The build made 93 commits:

| Commits | Kind |
| ---: | --- |
| 15 | first version of an act |
| 78 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 18 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 80 laws in the record.
- 161 tags.

## Dates

Each commit is dated at noon (Asia/Jerusalem) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each Basic Law text is the full current version Hebrew Wikisource publishes, dated by the day of that version (oldest version available); catalogue entries are dated by the publication date Wikidata records. https://he.wikisource.org/wiki/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%94:%D7%97%D7%95%D7%A7%D7%99_%D7%99%D7%A1%D7%95%D7%93

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `8d002ace38669cf2f626bc719ba56083ca2d62417dcbc9618c1e172ddc6f50d1` (797795 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.14.0; git version 2.52.0.windows.1.

## Checks

82 versions of 15 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Each version adds the Basic Laws that Wikidata dates to one day, dated that day and credited to a catalogue law key 'catalogue-<date>'. The dates are Wikidata's publication dates and are not checked against the Knesset or Reshumot (the Official Gazette). Basic Laws that Wikidata does not list as items of this class (for example the original 1968 and 1992 versions of Basic Law: The Government, which later versions replaced) are absent.
- Only facts are copied (titles, dates, Wikidata identifiers). The title of a Basic Law is the name of the law, not a description of it.
- Basic Law text is taken from Hebrew Wikisource, a third-party copy of statutes in which no copyright subsists (Copyright Act, 5768-2007, s. 6); knesset.gov.il was not used.
- Each Basic Law is one version, the current text, dated by the Wikisource revision it was read from and credited to the publisher as the oldest version available. It is not the as-enacted text, and no amendment is credited.
- Section keys: Hebrew letter suffixes are written as Latin letters in alphabet order (1א -> sec-001-a, 1ב -> sec-001-b). Editorial notes, gazette references, chapter headings and signatures are left out; the maqaf is written as a hyphen.
- The temporary State Budget Basic Laws (2009-2016, 2017-2018) and Basic Law: Torah Study are not included.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Sonnet 5.5) wrote the extraction code. No model wrote, edited or summarised any text.
- A model (Claude) wrote the parser that reads Wikisource's wikitext; no model wrote or edited legal text.
