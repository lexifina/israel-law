"""Build corpus.json for Israel: a facts-only catalogue of the Basic Laws from Wikidata (CC0). No law text."""
import json, os, re, hashlib
H = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(H, '.cache')
NL = chr(10)
raw = open(os.path.join(C, 'basic.json'), 'rb').read()
SHA = hashlib.sha256(raw).hexdigest()
rows = json.loads(raw.decode('utf8'))['results']['bindings']
items = []
for b in rows:
    q = b['i']['value'].rsplit('/', 1)[1]
    items.append({'q': q, 'en': b['iLabel']['value'], 'he': b.get('iLabelHe', {}).get('value'), 'date': b['p']['value'][:10]})
items.sort(key=lambda x: (x['date'], x['q']))


def slug(en):
    s = re.sub(r'[^a-z0-9]+', '-', en.lower()).strip('-')
    return s


laws = {}
units_by_date = {}
for it in items:
    key = 'catalogue-' + it['date']
    laws.setdefault(key, {'label': 'Catalogue entry ' + it['date'], 'title': 'Basic Laws catalogue: entries for ' + it['date'], 'kind': 'law',
                          'enacted': it['date'], 'published': it['date'], 'url': 'https://www.wikidata.org/wiki/' + it['q'],
                          'temporary_until': None, 'restores': None,
                          'note': 'A catalogue entry: it records the date Wikidata gives for the publication of a Basic Law. It changes no legal words and holds no law text.'})
    k = 'basic-law-' + it['date'][:4] + '-' + slug(it['en'])[:60]
    lines = [f"# {it['en']}", f"Title (English, Wikidata): {it['en']}"]
    if it['he']:
        lines.append(f"Title (Hebrew, Wikidata): {it['he']}")
    lines += [f"Date (Wikidata, publication date): {it['date']}", f"Wikidata: https://www.wikidata.org/wiki/{it['q']}",
              "Kind: Basic Law of Israel (constitutional-status law; Israel has no single codified constitution)",
              "Text: not held in this repository (see README)"]
    units_by_date.setdefault(it['date'], {})[k] = {'label': it['en'], 'kind': 'catalogue-entry', 'text': NL.join(lines) + NL, 'law': key}
dates = sorted(units_by_date)
versions = []
state = {}
for i, d in enumerate(dates):
    new = units_by_date[d]
    credits = {k: [v['law']] for k, v in new.items()}
    for k, v in new.items():
        state[k] = {'label': v['label'], 'kind': v['kind'], 'text': v['text']}
    ver = {'from': d, 'source_url': 'https://www.wikidata.org/wiki/Q2368137', 'sha256': SHA, 'credits': credits}
    if i == 0:
        ver['units'] = {k: dict(v) for k, v in state.items()}
    else:
        ver['changes'] = {k: {'label': v['label'], 'kind': v['kind'], 'text': v['text']} for k, v in new.items()}
    versions.append(ver)
URL = 'https://www.wikidata.org/wiki/Q2368137'
corpus = {
    'country': {'code': 'IL', 'name': 'Israel', 'slug': 'israel', 'lang': 'en', 'tz': 'Asia/Jerusalem', 'future_branch': 'future',
                'publisher': {'name': 'Wikidata (CC0)', 'email': 'wikidata@wikidata.invalid'},
                'default_in_force_rule': {'text': 'Not applicable: this repository is a catalogue of facts. Each entry is dated by the publication date Wikidata records for the Basic Law.', 'source': URL},
                'licence_note': 'Facts from Wikidata, dedicated to the public domain under CC0 1.0 (https://creativecommons.org/publicdomain/zero/1.0/). No Israeli law text is included.'},
    'sources': [{'name': 'Wikidata: items that are instances of "Basic Laws of Israel" (Q2368137), via the Wikidata Query Service', 'url': URL, 'retrieved': '2026-10-30', 'requests': 2,
                 'licence': 'CC0 1.0', 'notes': 'Title (English, Hebrew) and publication date of each Basic Law. Facts only.'}],
    'laws': laws,
    'acts': [{'slug': 'catalogue', 'short': 'Catalogue', 'title': 'Catalogue of the Basic Laws of Israel (facts only, no law text)', 'url': URL,
              'first_law': 'catalogue-' + dates[0], 'earlier_laws': [], 'versions': versions}],
    'applies': [],
    'decisions': [
        'Metadata only, no law text: knesset.gov.il (including its robots.txt) answers every request from this machine with a geographic-block page, and the only archived copy of its Basic Laws page is a bot-challenge stub. Neither was worked around. Israeli law text is therefore not published here.',
        "Each version adds the Basic Laws that Wikidata dates to one day, dated that day and credited to a catalogue law key 'catalogue-<date>'. The dates are Wikidata's publication dates and are not checked against the Knesset or Reshumot (the Official Gazette). Basic Laws that Wikidata does not list as items of this class (for example the original 1968 and 1992 versions of Basic Law: The Government, which later versions replaced) are absent.",
        'Only facts are copied (titles, dates, Wikidata identifiers). The title of a Basic Law is the name of the law, not a description of it.',
    ],
    'ai_use': ['Claude Code (Claude Sonnet 5.5) wrote the extraction code. No model wrote, edited or summarised any text.'],
}
json.dump(corpus, open(os.path.join(H, 'corpus.json'), 'w', encoding='utf8', newline=NL), ensure_ascii=False, indent=1)
print(len(items), 'basic laws,', len(versions), 'versions')
