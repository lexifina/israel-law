# Israel: law history in git

The law of Israel as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `basic-law-*/` | The text of 13 Basic Laws, in Hebrew, one file per section: The Knesset, Israel Lands, The President of the State, The Government, The State Economy, The Military, Jerusalem the Capital of Israel, The Judiciary, The State Comptroller, Human Dignity and Liberty, Freedom of Occupation, Referendum, and Israel the Nation State of the Jewish People | 1 each | The current text only, dated by the day of the version it was read from (oldest version available) |
| `catalogue/` | Catalogue of the Basic Laws of Israel: title, Hebrew title, date and Wikidata identifier of each (facts only) | 13 | One version per date on which Wikidata records a Basic Law, from 12 February 1958 (Basic Law: The Knesset) to 19 July 2018 |
| `treaties/` | Israel's treaty actions (signature, ratification, accession, acceptance, succession) in 40 multilateral treaties deposited with the UN Secretary-General: treaty name, action, date (facts only) | 56 | One version per day on which the UN Treaty Collection records an action, 21 June 1949 to 22 November 2016 |

**Language.** The Basic Laws are in Hebrew, the language they are enacted in; there is no official English text. Catalogue and treaty entries are in English, with the Hebrew title of each Basic Law.

**Sources.** The text of the Basic Laws is from [Hebrew Wikisource](https://he.wikisource.org/wiki/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%94:%D7%97%D7%95%D7%A7%D7%99_%D7%99%D7%A1%D7%95%D7%93), read on 30 October 2026; each Wikisource page cites the Reshumot (Sefer HaChukim) publications of the law and its amendments. No copyright subsists in statutes in Israel (Copyright Act, 5768-2007, section 6), so the text may be reproduced. The catalogue is from [Wikidata](https://www.wikidata.org/wiki/Q2368137) (CC0), and the treaty actions from the UN Treaty Collection (https://treaties.un.org/; facts only).

## Dates

Each Basic Law is a single version: the full current text as Hebrew Wikisource published it, dated by the day of that Wikisource revision and credited to the publisher as the oldest version available. It is not the text as enacted, and the dates of individual amendments are not recorded yet. Catalogue entries are dated by the publication date Wikidata records for each Basic Law (not checked against Reshumot); treaty actions by the date the Treaty Collection gives.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist. The Basic Law texts are credited to the publisher (Hebrew Wikisource) as the oldest version available; catalogue entries to a catalogue key for their date; treaty actions to the treaty action. The committer is always Lexifina.

## Limits

Not complete and not an official text. The Basic Law text is a third-party copy, not the Reshumot publication, and has not been checked against it; for anything that matters, read the official gazette. Each Basic Law has one version, with no amendment history. Editorial notes, chapter headings, signatures and gazette references are left out. The temporary State Budget Basic Laws and Basic Law: Torah Study are not included. Ordinary statutes, regulations and judgments are not included. Treaty actions cover only the 40 treaties (of those read) in which the Treaty Collection lists Israel. This repository is not legal advice.
