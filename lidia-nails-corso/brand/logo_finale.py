"""Logo finale B · Mandorla in SVG vettoriale (testo convertito in tracciati). Uso: python3 -I logo_finale.py"""
import os, subprocess
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'logo-finale'); os.makedirs(OUT, exist_ok=True)
OLIVA, SALVIA, AVORIO = '#34402F', '#C9D8C5', '#FAF7F0'
PF = TTFont(os.path.join(HERE, 'fonts', 'PlayfairDisplay-Medium.ttf')); MS = TTFont(os.path.join(HERE, 'fonts', 'Montserrat-Medium.ttf'))

def text_d(font, s, size, x, y, tracking=0, anchor='start'):
    gs, cmap, upm = font.getGlyphSet(), font.getBestCmap(), font['head'].unitsPerEm; sc = size / upm
    names = [cmap[ord(c)] for c in s]; adv = [font['hmtx'][n][0] * sc + tracking for n in names]
    total = sum(adv) - tracking
    cx = x - total / 2 if anchor == 'middle' else x
    d = ''
    for n, a in zip(names, adv):
        pen = SVGPathPen(gs); gs[n].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y))); d += pen.getCommands(); cx += a
    return d, total

ALMOND = 'M0,-100 C26,-100 50,-36 54,24 L54,64 Q54,98 20,98 L-20,98 Q-54,98 -54,64 L-54,24 C-50,-36 -26,-100 0,-100 Z'
ALMOND_IN = 'M0,-85 C22,-85 41,-32 45,22 L45,60 Q45,84 18,84 L-18,84 Q-45,84 -45,60 L-45,22 C-41,-32 -22,-85 0,-85 Z'
GOLD = '<linearGradient id="oro" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7C5A12"/><stop offset=".18" stop-color="#D9B25A"/><stop offset=".32" stop-color="#FFF1B8"/><stop offset=".48" stop-color="#C9962F"/><stop offset=".66" stop-color="#F3D98A"/><stop offset=".82" stop-color="#A8761B"/><stop offset="1" stop-color="#6F4E10"/></linearGradient>'

def emblem(cx, cy, sc):
    d, _ = text_d(PF, 'L', 96, 0, 40, anchor='middle')
    return f'<g transform="translate({cx},{cy}) scale({sc})"><path d="{ALMOND}" fill="none" stroke="PAINT" stroke-width="5"/><path d="{ALMOND_IN}" fill="none" stroke="PAINT" stroke-width="1.5"/><path d="{d}" fill="PAINT"/></g>'

def build(kind, mode):
    paint = 'url(#oro)' if mode == 'oro' else {'oliva': OLIVA, 'salvia': SALVIA, 'avorio': AVORIO}[mode]
    if kind == 'orizzontale':
        W, H = 700, 260; body = emblem(90, 130, 1)
        d1, _ = text_d(PF, 'Lidia', 112, 190, 140); d2, _ = text_d(MS, 'NAIL EXPERT', 27, 198, 212, 13)
        body += f'<path d="{d1}" fill="PAINT"/><rect x="196" y="167.2" width="444" height="1.6" fill="PAINT"/><path d="{d2}" fill="PAINT"/>'
    elif kind == 'verticale':
        W, H = 520, 560; body = emblem(260, 150, 1.25)
        d1, _ = text_d(PF, 'Lidia', 120, 260, 400, anchor='middle'); d2, _ = text_d(MS, 'NAIL EXPERT', 28, 266, 470, 14, 'middle')
        body += f'<path d="{d1}" fill="PAINT"/><rect x="140" y="421.2" width="240" height="1.6" fill="PAINT"/><path d="{d2}" fill="PAINT"/>'
    else:  # emblema
        W, H = 180, 240; body = emblem(90, 120, 1)
    defs = '<defs>' + GOLD.replace('X1', '0').replace('Y1', '0').replace('X2', str(W)).replace('Y2', str(H)) + '</defs>' if mode == 'oro' else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{defs}{body.replace("PAINT", paint)}</svg>', W, H

files = []
for kind in ['orizzontale', 'verticale', 'emblema']:
    for mode in ['oro', 'oliva', 'salvia', 'avorio']:
        s, W, H = build(kind, mode); n = f'{kind}-{mode}'; open(os.path.join(OUT, n + '.svg'), 'w').write(s); files.append((n, W, H))
# Avatar quadrato 1080 (emblema oro su oliva) e versione chiara
av = lambda bg, mode: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080"><rect width="1080" height="1080" fill="{bg}"/><g transform="translate(540,540) scale(3.1) translate(-90,-120)">{build("emblema", mode)[0].split("</defs>")[0].split("<svg")[1].split(">",1)[1] if False else ""}</g></svg>'
html = '<html><body style="margin:0;background:transparent">' + ''.join(f'<div id="{n}" style="display:inline-block;width:{W*4}px;height:{H*4}px">{open(os.path.join(OUT, n + ".svg")).read().replace(f"width=\"{W}\" height=\"{H}\"", f"width=\"{W*4}\" height=\"{H*4}\"")}</div><br>' for n, W, H in files)
# avatar: emblema oro su oliva e su salvia (emblema oliva)
for nm, bg, mode in [('avatar-oliva', OLIVA, 'oro'), ('avatar-salvia', SALVIA, 'oliva')]:
    inner = build('emblema', mode)[0]
    html += f'<div id="{nm}" style="width:1080px;height:1080px;background:{bg};display:flex;align-items:center;justify-content:center">{inner.replace("width=\"180\" height=\"240\"", "width=\"560\" height=\"747\"")}</div><br>'
    files.append((nm, 1080, 1080))
html += '</body></html>'
p = os.path.join(HERE, '_l.html'); open(p, 'w').write(html)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:2000,height:1200}}}});await pg.goto('file://{p}');
for(const id of {[f[0] for f in files]!r}) await pg.locator('#'+id).screenshot({{path:'{OUT}/'+id+'.png',omitBackground:true}});await b.close()}})()"""
open(os.path.join(HERE, '_l.js'), 'w').write(js); subprocess.run(['node', os.path.join(HERE, '_l.js')], check=True); os.remove(p); os.remove(os.path.join(HERE, '_l.js'))
print(len(os.listdir(OUT)), 'file')
