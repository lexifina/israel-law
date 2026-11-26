# מבנה המאגר · Repository structure

שמות התיקיות והקבצים בעברית, בשפה שבה מחפשים את הדין. מירכאות בשמות נכתבות כגרשיים וגרש (״ ׳), ורווחים, פסיקים ונקודתיים הופכים למקף אחד.

Folder and file names are in Hebrew, the language people search the law in. Quotation marks in names are written as gershayim and geresh (״ ׳); spaces, commas and colons become one hyphen.

| נתיב · Path | תוכן | Contents |
| --- | --- | --- |
| `חקיקה/חוקי-יסוד/<שם>/סעיף-NNN.md` | חוקי היסוד, קובץ לכל סעיף | the Basic Laws, one file per section |
| `חקיקה/חוקים/<שנה>/<שם>/סעיף-NNN.md` | חוקי הכנסת בנוסחם המשולב | Knesset laws, consolidated text |
| `חקיקה/פקודות/<שנה>/<שם>/סעיף-NNN.md` | פקודות (מנדט ונוסח חדש) | ordinances (Mandate and new version) |
| `חקיקה/תקנות/<שנה>/<שם>/…` , `חקיקה/צווים/…` , `חקיקה/כללים/…` , `חקיקה/אחר/…` | חקיקת משנה | secondary legislation |
| `רשומות/ספר-החוקים/<שנה>/<שם החוק>.md` | החוק כפי שפורסם ברשומות (ספר החוקים) | each law as published in the Official Gazette (Sefer HaHukim) |
| `רשומות/חוקי-תקציב/…`, `רשומות/דיני-מדינת-ישראל/…` | חוקי תקציב; נוסח חדש של דיני מדינת ישראל | budget laws; new versions (Dinei Medinat Israel) |
| `רשומות/עיתון-רשמי/<שנה>/…`, `רשומות/עיתון-רשמי-מנדטורי/<שנה>/…` | פקודות כפי שפורסמו בעיתון הרשמי של מועצת המדינה הזמנית ובעיתון הרשמי המנדטורי | ordinances as published in the Provisional Council's and the Mandate's Official Gazettes |
| `פסיקה/בית-המשפט-העליון/<שנה>/<חודש>/<יום>/<הליך>-<מספר>-<שנה>-<סוג>.md` | החלטות ופסקי דין של בית המשפט העליון, לפי יום ההחלטה | Supreme Court decisions and judgments, by decision day |
| `הצעות-חוק/<הכנסת-ה-NN>/<שנה>/<חודש>/<יום>/<שם הצעת החוק>-<פ-מספר-כנסת>.md` | הצעות חוק בכנסת: כל שלב שהכנסת פרסמה לו נוסח (דיון מוקדם, קריאה ראשונה) הוא גרסה של הקובץ; התיקייה לפי היום שבו הונחה ההצעה או פורסמה לראשונה | Knesset bills: each stage the Knesset published a text for (preliminary reading, first reading) is a version of the file; the folder is the day the bill was first laid or published |
| `פרוטוקולים/מליאה/<הכנסת-ה-NN>/<שנה>/<חודש>/<יום>-ישיבה-<מספר>.md` | דברי הכנסת: פרוטוקולי מליאת הכנסת (ושל מועצת המדינה הזמנית, `מועצת-המדינה-הזמנית/`), לפי יום הישיבה | Knesset plenum transcripts (and those of the Provisional State Council), by session day |
| `פרוטוקולים/ועדות/<הכנסת-ה-NN>/<שם הוועדה>/<שנה>/<חודש>/<יום>-ישיבה-<מספר>.md` | פרוטוקולי ועדות הכנסת, לפי יום הישיבה | Knesset committee transcripts, by session day |
| `קטלוג/` | קטלוג חוקי היסוד (ויקינתונים) | catalogue of the Basic Laws (Wikidata) |
| `אמנות/` | פעולות ישראל באמנות רב-צדדיות (או״ם) | Israel's actions in multilateral treaties (UN) |
| `data/`, `tools/`, `visualisations/`, `vulnerabilities/` | נתונים, כלים ותרשימים (שמות משותפים לכל מאגרי Lexifina) | data, tools and charts (names shared by every Lexifina repository) |

## כללים · Rules

- **סעיפים · Sections.** `סעיף 3א1` → `סעיף-003-א-1.md`: המספר בשלוש ספרות, ואחריו אותיות ומספרי משנה. The number in three digits, then its letters and sub-numbers. Text before section 1 (title, preamble) is `000-כותרת.md`; schedules are `תוספת-<n>.md`.
- **שנה · Year.** The Gregorian year in the law's title (`התשל״ז-1977` → `1977`); the folder name is the title without that year. `ללא-שנה` when the title has none.
- **פסיקה · Case law.** `<הליך>` is the procedure as the court writes it (`ע״א`, `בג״ץ`, `רע״פ`); `<מספר>-<שנה>` is the case number (`1234/20` → `1234-20`); `<סוג>` is the document type (`החלטה`, `פסק-דין`). A day with more than 900 documents gets one sub-folder per procedure. Party names never appear in paths, commit subjects or trailers. Protected cases (family, minors, adoption, sexual offences, publication bans, anonymised captions) are not published.
- **No folder holds more than 1,000 entries.**

## תאריכים · Dates

Every commit is dated 12:00 Asia/Jerusalem on the day its text took effect, and carries `In-force:` and `In-force-evidence:` trailers. A consolidated version is dated by the amending law's in-force day (as the law or its publication states it); a law as published, by its publication in Reshumot (Interpretation Law 5741-1981, s. 10: a law takes effect on publication unless it says otherwise); a decision, by its day. Wiki edit dates are never used as in-force dates. Bills and transcripts are legislative history, not law: a bill stage is dated by the day the bill says it was laid on the Knesset table or by the date its bills booklet prints, a transcript by its session day; their `In-force:` trailer carries that record day. Before 1970 git cannot store the day: the commit is dated 1970-01-01 and the real day leads the subject and the trailers.

## היסטוריה · History

The 2026-11-26 layout commit moved the earlier English folders here in one rename-only commit (`data/paths.json` maps old paths to new). `git log --follow <file>` follows a file across the move.
