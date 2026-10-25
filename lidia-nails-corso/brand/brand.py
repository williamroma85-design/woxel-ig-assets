"""Brand identity Lidia Nail Expert – 3 proposte. Uso: python3 -I brand.py  (richiede Chromium/playwright e rete per Google Fonts)"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'proposte'); os.makedirs(OUT, exist_ok=True)
SALVIA, OLIVA, AVORIO, ORO_FLAT = '#C9D8C5', '#34402F', '#FAF7F0', '#C8A04A'
GOLD_DEFS = '''<defs><linearGradient id="g{u}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7C5A12"/><stop offset=".18" stop-color="#D9B25A"/><stop offset=".32" stop-color="#FFF1B8"/><stop offset=".48" stop-color="#C9962F"/><stop offset=".66" stop-color="#F3D98A"/><stop offset=".82" stop-color="#A8761B"/><stop offset="1" stop-color="#6F4E10"/></linearGradient></defs>'''
GOLD_CSS = 'linear-gradient(135deg,#7C5A12 0%,#D9B25A 18%,#FFF1B8 32%,#C9962F 48%,#F3D98A 66%,#A8761B 82%,#6F4E10 100%)'
_u = [0]
def col(mode):
    _u[0] += 1; u = _u[0]
    if mode == 'gold': return f'url(#g{u})', GOLD_DEFS.format(u=u)
    return {'olive': OLIVA, 'sage': SALVIA, 'ivory': AVORIO}[mode], ''

# ---------- Loghi (SVG) ----------
def logo_A(mode, w=520):  # Maison
    c, d = col(mode)
    return f'''<svg viewBox="0 0 600 330" width="{w}" xmlns="http://www.w3.org/2000/svg">{d}
<text x="300" y="170" text-anchor="middle" font-family="Cormorant Garamond" font-weight="600" font-size="170" letter-spacing="22" fill="{c}">LIDIA</text>
<line x1="95" y1="214" x2="280" y2="214" stroke="{c}" stroke-width="2"/><line x1="320" y1="214" x2="505" y2="214" stroke="{c}" stroke-width="2"/>
<path d="M300,203 L311,214 L300,225 L289,214 Z" fill="{c}"/>
<text x="300" y="275" text-anchor="middle" font-family="Montserrat" font-weight="500" font-size="30" letter-spacing="15" fill="{c}">NAIL EXPERT</text></svg>'''
def mono_A(mode, s=220):
    c, d = col(mode)
    return f'''<svg viewBox="0 0 240 240" width="{s}" xmlns="http://www.w3.org/2000/svg">{d}<circle cx="120" cy="120" r="108" fill="none" stroke="{c}" stroke-width="3"/><circle cx="120" cy="120" r="97" fill="none" stroke="{c}" stroke-width="1.2"/>
<text x="120" y="158" text-anchor="middle" font-family="Cormorant Garamond" font-weight="600" font-size="118" fill="{c}">L</text><text x="120" y="188" text-anchor="middle" font-family="Montserrat" font-weight="500" font-size="9" letter-spacing="2.6" fill="{c}">NAIL EXPERT</text></svg>'''

ALMOND = 'M0,-100 C26,-100 50,-36 54,24 L54,64 Q54,98 20,98 L-20,98 Q-54,98 -54,64 L-54,24 C-50,-36 -26,-100 0,-100 Z'
ALMOND_IN = 'M0,-85 C22,-85 41,-32 45,22 L45,60 Q45,84 18,84 L-18,84 Q-45,84 -45,60 L-45,22 C-41,-32 -22,-85 0,-85 Z'
def emblem_B(c, tx=0, ty=0, sc=1):
    return f'''<g transform="translate({tx},{ty}) scale({sc})"><path d="{ALMOND}" fill="none" stroke="{c}" stroke-width="5"/><path d="{ALMOND_IN}" fill="none" stroke="{c}" stroke-width="1.5"/><text x="0" y="40" text-anchor="middle" font-family="Playfair Display" font-weight="500" font-size="96" fill="{c}">L</text></g>'''
def logo_B(mode, w=640):  # Almond – lockup orizzontale
    c, d = col(mode)
    return f'''<svg viewBox="0 0 700 260" width="{w}" xmlns="http://www.w3.org/2000/svg">{d}{emblem_B(c, 90, 130)}
<text x="190" y="140" font-family="Playfair Display" font-weight="500" font-size="112" fill="{c}">Lidia</text>
<line x1="196" y1="168" x2="640" y2="168" stroke="{c}" stroke-width="1.5"/>
<text x="198" y="212" font-family="Montserrat" font-weight="500" font-size="27" letter-spacing="13" fill="{c}">NAIL EXPERT</text></svg>'''
def mono_B(mode, s=220):
    c, d = col(mode)
    return f'<svg viewBox="-90 -125 180 250" width="{s*0.72}" xmlns="http://www.w3.org/2000/svg">{d}{emblem_B(c)}</svg>'

def logo_C(mode, w=560):  # Signature
    c, d = col(mode)
    return f'''<svg viewBox="0 0 620 370" width="{w}" xmlns="http://www.w3.org/2000/svg">{d}
<text x="310" y="195" text-anchor="middle" font-family="Great Vibes" font-size="250" fill="{c}">Lidia</text>
<line x1="70" y1="336" x2="168" y2="336" stroke="{c}" stroke-width="1.5"/><line x1="452" y1="336" x2="550" y2="336" stroke="{c}" stroke-width="1.5"/>
<text x="310" y="345" text-anchor="middle" font-family="Montserrat" font-weight="500" font-size="25" letter-spacing="12" fill="{c}">NAIL EXPERT</text></svg>'''
def mono_C(mode, s=220):
    c, d = col(mode)
    return f'''<svg viewBox="0 0 240 240" width="{s}" xmlns="http://www.w3.org/2000/svg">{d}<circle cx="120" cy="120" r="108" fill="none" stroke="{c}" stroke-width="2.5"/>
<text x="120" y="150" text-anchor="middle" font-family="Great Vibes" font-size="130" fill="{c}">Li</text><path d="M80,178 L160,178" stroke="{c}" stroke-width="1.5"/><circle cx="120" cy="178" r="3.5" fill="{c}"/></svg>'''

DIR = {
 'A': dict(nome='A · Maison', logo=logo_A, mono=mono_A, h='Cormorant Garamond', b='Montserrat', claim='Eleganza classica da maison di alta bellezza.',
           desc='Serif ad alto contrasto, spaziatura ampia, filetto con rombo dorato. Autorevole, editoriale, da maestra. Ideale per formazione e posizionamento premium.', hs='LIDIA', hstyle='font-weight:600;letter-spacing:.12em'),
 'B': dict(nome='B · Mandorla', logo=logo_B, mono=mono_B, h='Playfair Display', b='Montserrat', claim='La forma dell\'unghia a mandorla diventa il simbolo.',
           desc='Emblema a mandorla con L, riconoscibile anche piccolissimo (avatar, highlight, filigrana). Moderno e distintivo: dice "nail" senza clichè. Il più versatile.', hs='Lidia', hstyle='font-weight:500'),
 'C': dict(nome='C · Signature', logo=logo_C, mono=mono_C, h='Great Vibes', b='Montserrat', claim='La firma di Lidia: personal brand caldo e umano.',
           desc='Lettering a mano come firma sul lavoro finito. Femminile, vicino alla cliente, perfetto per un personal brand. Da usare con monogramma "Li" nelle dimensioni piccole.', hs='Lidia', hstyle=''),
}

def board(k):
    d = DIR[k]; L, M = d['logo'], d['mono']
    swatches = f'''<div class="sw" style="background:{SALVIA}"><b>Salvia</b>#C9D8C5<br>colore primario</div><div class="sw" style="background:{OLIVA};color:#fff"><b>Oliva profondo</b>#34402F<br>testi e fondi scuri</div><div class="sw" style="background:{AVORIO}"><b>Avorio</b>#FAF7F0<br>respiro, fondi chiari</div><div class="sw" style="background:{GOLD_CSS}"><b>Oro lucido</b>gradiente metallico<br>fallback piatto #C8A04A</div>'''
    return f'''<div class="board" id="board{k}">
<div class="hd"><span>{d['nome']}</span><em>{d['claim']}</em></div>
<div class="g1"><div class="p olive big">{L('gold', 560)}</div><div class="col"><div class="p sage">{L('olive', 400)}</div><div class="p ivory">{L('gold', 400)}</div></div></div>
<div class="g2"><div class="p small sage">{M('olive', 190)}</div><div class="p small olive">{M('gold', 190)}</div><div class="p small ivory">{M('gold', 190)}</div>
<div class="txt"><h4>Perché funziona</h4><p>{d['desc']}</p><h4>Font</h4><p><span style="font-family:'{d['h']}';font-size:32px">{d['hs']}</span> &nbsp;<span style="font-family:Montserrat;letter-spacing:.2em;font-size:14px">NAIL EXPERT</span></p><p class="mut">Titoli: {d['h']} · Testi: Montserrat</p></div></div>
<div class="g3">{swatches}</div>
<div class="g4">
 <div class="mock post" style="background:{SALVIA}"><div style="font-family:'{d['h']}';font-size:34px;color:{OLIVA};line-height:1.15;margin-top:70px">Unghia corta,<br>risultato perfetto.</div><div class="gl" style="background:{GOLD_CSS}"></div><div class="sm">GEL TIP · GUIDA</div><div class="lg">{M('olive', 70)}</div></div>
 <div class="mock post" style="background:{OLIVA}"><div class="sm" style="color:{SALVIA}">CAROSELLO · 1/7</div><div style="font-family:'{d['h']}';font-size:34px;line-height:1.15;margin-top:50px;background:{GOLD_CSS};-webkit-background-clip:text;color:transparent">3 errori che rovinano la tua gel tip</div><div class="lg">{M('gold', 70)}</div></div>
 <div class="mock hl">{''.join(f'<div><div class="circ" style="background:{b}">{M("olive" if b!=OLIVA else "gold", 46)}</div><span>{n}</span></div>' for b, n in [(SALVIA,'Gel Tip'),(OLIVA,'Prima/Dopo'),(AVORIO,'Corsi'),(SALVIA,'Info')])}</div>
 <div class="mock card"><div class="cf" style="background:{OLIVA}">{L('gold', 190)}</div><div class="cb" style="background:{AVORIO}"><b style="font-family:'{d['h']}'">Lidia</b><br><small>Nail Expert · Gel Tip Specialist<br>@lidiafrt_nailartist</small></div></div>
</div></div>'''

CSS = f'''
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Montserrat:wght@400;500;600&family=Playfair+Display:wght@400;500&family=Great+Vibes&display=swap');
body{{margin:0;background:#fff;font-family:Montserrat,sans-serif;color:{OLIVA}}}
.board{{width:1600px;padding:40px;box-sizing:border-box;background:#fff}}
.hd{{display:flex;align-items:baseline;gap:24px;margin-bottom:22px}}.hd span{{font:600 36px Montserrat;color:{OLIVA}}}.hd em{{font:italic 20px Montserrat;color:#6b766a}}
.g1{{display:grid;grid-template-columns:900px 1fr;gap:20px}}.col{{display:grid;gap:20px}}
.p{{border-radius:22px;display:flex;align-items:center;justify-content:center;padding:30px;box-sizing:border-box}}
.big{{height:470px}}.col .p{{height:225px}}.olive{{background:{OLIVA}}}.sage{{background:{SALVIA}}}.ivory{{background:{AVORIO};border:1px solid #e5e0d3}}
.g2{{display:grid;grid-template-columns:230px 230px 230px 1fr;gap:20px;margin-top:20px}}.small{{height:230px;padding:10px}}
.txt{{padding:0 10px}}.txt h4{{margin:0 0 4px;font:600 13px Montserrat;letter-spacing:.2em;text-transform:uppercase;color:#8a6b1f}}.txt p{{margin:0 0 14px;font-size:15px;line-height:1.5}}.mut{{color:#6b766a}}
.g3{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:20px}}.sw{{height:110px;border-radius:16px;padding:16px;box-sizing:border-box;font-size:13px;line-height:1.5}}.sw b{{display:block;font-size:16px}}
.g4{{display:grid;grid-template-columns:330px 330px 1fr 380px;gap:20px;margin-top:20px}}
.mock{{border-radius:18px;overflow:hidden;position:relative;height:330px;box-sizing:border-box}}.post{{padding:30px}}.post .sm{{position:absolute;left:30px;top:28px;font:500 12px Montserrat;letter-spacing:.2em;color:{OLIVA}}}
.gl{{height:3px;width:80px;margin-top:20px}}.lg{{position:absolute;right:20px;bottom:16px}}
.hl{{background:{AVORIO};border:1px solid #e5e0d3;display:flex;gap:12px;align-items:center;justify-content:center}}.hl div{{text-align:center}}.circ{{width:78px;height:78px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:3px solid #fff;box-shadow:0 0 0 2px #d9b25a}}.hl span{{font-size:12px;display:block;margin-top:8px}}
.card{{display:grid;grid-template-rows:1fr 1fr}}.cf{{display:flex;align-items:center;justify-content:center}}.cb{{padding:24px;font-size:20px;line-height:1.5}}.cb small{{font-size:13px;color:#6b766a}}
'''
html = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>' + ''.join(board(k) for k in DIR) + '<div id="logos">' + ''.join(f'<div id="{k}-{m}-{v}" style="display:inline-block;padding:40px;background:{bg}">{DIR[k]["logo"](m, 900)}</div>' for k in DIR for m, v, bg in [('gold', 'oro-su-oliva', OLIVA), ('olive', 'oliva-su-salvia', SALVIA), ('gold', 'oro-su-avorio', AVORIO)]) + '</div></body></html>'
p = os.path.join(HERE, '_b.html'); open(p, 'w').write(html)
ids = [f'board{k}' for k in DIR] + [f'{k}-{m}-{v}' for k in DIR for m, v in [('gold', 'oro-su-oliva'), ('olive', 'oliva-su-salvia'), ('gold', 'oro-su-avorio')]]
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{deviceScaleFactor:1.5,viewport:{{width:1680,height:1200}}}});await pg.goto('file://{p}',{{waitUntil:'networkidle'}});await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(1500);
for(const id of {ids!r}) await pg.locator('#'+id).screenshot({{path:'{OUT}/'+id+'.png'}});await b.close()}})()"""
open(os.path.join(HERE, '_b.js'), 'w').write(js); subprocess.run(['node', os.path.join(HERE, '_b.js')], check=True)
os.remove(p); os.remove(os.path.join(HERE, '_b.js')); print(sorted(os.listdir(OUT)))
