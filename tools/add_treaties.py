import sys, json
sys.path.insert(0, r'~\Documents\lexifina\scripts\world-law')
import p3_untc as p
P = r'~\Documents\lexifina\scripts\israel-law\corpus.json'
c = json.load(open(P, encoding='utf8'))
a, l, s, n = p.treaties_act('Israel')
c['acts'] = [x for x in c['acts'] if x['slug'] != 'treaties'] + [a]
c['laws'].update(l)
c['sources'] = [x for x in c['sources'] if not x['name'].startswith('UN Treaty')] + [dict(s, notes=s['notes'] + f' {n} treaties with an Israeli action.')]
open(P, 'w', encoding='utf8', newline='\n').write(json.dumps(c, ensure_ascii=False, indent=1) + '\n')
print(n, len(l))
