"""Genera gli schemi per le slide (SVG -> PNG con Chromium). Uso: python3 -I immagini.py"""
import os, subprocess, textwrap
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'output', 'immagini'); os.makedirs(OUT, exist_ok=True)
ROSA, NERO, CIP, VER, ROS, GIA, GRI = '#B76E79', '#2B2B2B', '#F6ECE9', '#4E9F6B', '#C0453F', '#E0A82E', '#8A8A8A'
W, H = 800, 600

def svg(body, h=H):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" font-family="DejaVu Sans, Arial, sans-serif"><rect width="{W}" height="{h}" rx="28" fill="{CIP}"/>{body}</svg>'
def t(x, y, s, size=22, fill=NERO, bold=False, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{"700" if bold else "400"}">{s}</text>'
def lines(x, y, ls, size=20, fill=NERO, gap=26, bold=False):
    return ''.join(t(x, y + i * gap, l, size, fill, bold) for i, l in enumerate(ls))
def badge(x, y, ok):
    c = VER if ok else ROS
    mark = 'M-9,0 L-3,7 L10,-8' if ok else 'M-8,-8 L8,8 M8,-8 L-8,8'
    return f'<circle cx="{x}" cy="{y}" r="17" fill="{c}"/><path d="{mark}" transform="translate({x},{y})" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>'
def title(s): return t(W/2, 48, s, 28, ROSA, True)
figs = {}

# 1. Struttura tip: profilo laterale + giro cuticola
b = title('Struttura di una tip professionale')
b += t(200, 100, 'Profilo laterale', 20, GRI, True) + t(600, 100, 'Profilo laterale', 20, GRI, True)
b += '<path d="M60,225 C130,150 240,150 350,205 L350,232 C240,185 130,190 60,232 Z" fill="#fff" stroke="%s" stroke-width="4"/>' % VER
b += '<path d="M450,225 C490,90 600,90 690,170 L740,285 L450,238 Z" fill="#fff" stroke="%s" stroke-width="4"/>' % ROS
b += t(60, 262, 'cuticola', 15, GRI, anchor='start') + t(350, 262, 'bordo libero', 15, GRI, anchor='end')
b += t(450, 275, 'cuticola', 15, GRI, anchor='start')
b += badge(200, 310, True) + lines(200, 352, ['Sottile alla cuticola,', 'più spessa al bordo libero'], 17, VER)
b += badge(600, 310, False) + lines(600, 352, ['Apice alto, discesa dritta:', '"becco di pappagallo"'], 17, ROS)
b += t(200, 425, 'Giro cuticola', 20, GRI, True) + t(600, 425, 'Giro cuticola', 20, GRI, True)
b += '<path d="M105,520 C105,445 295,445 295,520" fill="none" stroke="%s" stroke-width="5"/>' % VER
b += '<path d="M505,520 L505,462 L695,462 L695,520" fill="none" stroke="%s" stroke-width="5"/>' % ROS
b += badge(200, 556, True) + t(240, 563, 'tondo, a mezzaluna', 18, VER, anchor='start')
b += badge(600, 556, False) + t(640, 563, 'squadrato', 18, ROS, anchor='start')
figs['struttura-tip'] = svg(b, 600)

# 2. Tip trasparente / colorata / semi-opaca
b = title('Quale tip scegliere')
cards = [('Trasparente', VER, '#EAF5EE', 'Vedi il gel camminare', 'Blocco in 7-8 secondi', True), ('Colorata', GIA, '#FBF1D9', 'Non vedi il gel', 'Luce più lenta (≈15 s)', False), ('Semi-opaca', ROS, '#F8E3E1', 'Liscia dentro, già sottile', 'Da scartare', False)]
for i, (n, c, f, l1, l2, ok) in enumerate(cards):
    x = 40 + i * 250
    b += f'<rect x="{x}" y="100" width="220" height="440" rx="20" fill="#fff" stroke="{c}" stroke-width="4"/>'
    fill = {0: 'rgba(255,255,255,0.0)', 1: '#E8A9B3', 2: 'url(#half)'}[i]
    b += f'<path d="M{x+60},400 C{x+60},220 {x+90},170 {x+110},170 C{x+130},170 {x+160},220 {x+160},400 Z" fill="{f}" stroke="{c}" stroke-width="4"/>'
    if i == 1: b += f'<path d="M{x+60},400 C{x+60},220 {x+90},170 {x+110},170 C{x+130},170 {x+160},220 {x+160},400 Z" fill="#E8A9B3" opacity=".7"/>'
    if i == 2: b += f'<path d="M{x+60},400 C{x+60},300 {x+160},300 {x+160},400 Z" fill="#fff" opacity=".85"/><path d="M{x+60},300 L{x+160},300" stroke="{c}" stroke-dasharray="6 6"/>'
    b += t(x + 110, 140, n, 24, c, True) + badge(x + 110, 440, ok)
    b += t(x + 110, 485, l1, 16, NERO) + t(x + 110, 510, l2, 16, NERO)
figs['tip-tipi'] = svg(b, 600)

# 3. Mappa misure sulla mano
b = title('Misure: dove vanno sulla mano')
fingers = [(110, 330, 'pollice', '0 – 1', ROSA), (260, 200, 'indice', '2 – 6,5', '#D9A1A9'), (400, 160, 'medio', '2 – 6,5', '#D9A1A9'), (540, 200, 'anulare', '2 – 6,5', '#D9A1A9'), (670, 260, 'mignolo', '7 – 9', '#E9C3C8')]
for x, top, n, r, c in fingers:
    b += f'<rect x="{x-45}" y="{top+60}" width="90" height="{440-top}" rx="45" fill="{c}"/><ellipse cx="{x}" cy="{top+110}" rx="30" ry="40" fill="#fff" opacity=".85"/>'
    b += t(x, 560, n, 17, NERO, True) + t(x, top + 120, r, 20, NERO, True)
b += t(W/2, 100, '14 misure in totale (0 – 9, con le mezze misure)', 19, GRI)
figs['misure-mano'] = svg(b, 600)

# 4. Unghia naturale corta vs lunga
b = title('Unghia naturale sotto la tip')
for x0, ok, nat_end, lab in [(40, True, 230, ['Corta, pari al polpastrello', 'e stondata']), (420, False, 345, ['Troppo lunga:', 'sporge, tasca d\'aria'])]:
    b += f'<path d="M{x0+10},300 C{x0+60},170 {x0+200},170 {x0+340},250 L{x0+340},275 C{x0+200},215 {x0+60},215 {x0+10},320 Z" fill="#fff" stroke="{GRI}" stroke-width="4"/>'
    c = VER if ok else ROS
    b += f'<path d="M{x0+10},320 C{x0+90},262 {x0+nat_end-40},262 {x0+nat_end},268" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round"/>'
    if not ok: b += f'<circle cx="{x0+300}" cy="230" r="26" fill="none" stroke="{ROS}" stroke-width="4" stroke-dasharray="7 6"/>'
    b += t(x0+170, 140, 'Corta' if ok else 'Lunga', 24, c, True) + badge(x0+170, 400, ok) + lines(x0+170, 450, lab, 19, c)
b += t(W/2, 560, 'Linea colorata = unghia naturale · Contorno grigio = gel tip', 16, GRI)
figs['unghia-naturale'] = svg(b, 600)

# 5. Scelta misura
b = title('Scegliere la misura')
for i, (n, c, wtip, tag, ok) in enumerate([('Troppo piccola', ROS, 120, 'spazi ai lati', False), ('Giusta', VER, 160, 'combacia coi laterali', True), ('Troppo grande', ROS, 205, 'invade la pelle', False)]):
    cx = 135 + i * 265
    b += f'<rect x="{cx-80}" y="140" width="160" height="250" rx="70" fill="#F2D3C9"/>'
    b += f'<rect x="{cx-80+2}" y="170" width="156" height="215" rx="60" fill="#fff" stroke="{GRI}" stroke-width="2"/>'
    b += f'<path d="M{cx-wtip/2},385 L{cx-wtip/2},230 C{cx-wtip/2},150 {cx+wtip/2},150 {cx+wtip/2},230 L{cx+wtip/2},385 Z" fill="none" stroke="{c}" stroke-width="5"/>'
    b += t(cx, 125, n, 21, c, True) + badge(cx, 440, ok) + t(cx, 492, tag, 16, c)
b += t(W/2, 560, 'Grigio chiaro = pelle · Bianco = letto ungueale · Contorno = tip', 15, GRI)
figs['scelta-misura'] = svg(b, 600)

# 6/7. Passi (generico)
def passi(tit, steps, cols=3, color=ROSA):
    rows = (len(steps) + cols - 1) // cols; h = 120 + rows * 210
    b = title(tit)
    for i, s in enumerate(steps):
        r, c = divmod(i, cols); x = 40 + c * (720 / cols) + (720 / cols) / 2; y = 100 + r * 210
        w = 720 / cols - 20
        b += f'<rect x="{x - w/2}" y="{y}" width="{w}" height="185" rx="18" fill="#fff" stroke="{color}" stroke-width="3"/><circle cx="{x}" cy="{y+16}" r="22" fill="{color}"/>' + t(x, y + 24, str(i + 1), 22, '#fff', True)
        b += lines(x, y + 80, s[0], 20, NERO, 25, True) + lines(x, y + 80 + 25 * len(s[0]) + 10, s[1], 15, GRI, 20)
    return svg(b, h)
figs['applicazione'] = passi('Applicazione in 6 passi', [(['Prepara'], ['dry manicure,', 'unghia corta e tonda']), (['Opacizza'], ['interno della tip', '15.000–18.000 giri']), (['Deidratante', '+ primer'], ['acid-free, anche', 'dentro la tip']), (['Gel sulla tip'], ['passata sottile', '+ goccia scaricata']), (['Appoggia'], ['inclina, premi al centro,', 'scendi lenta']), (['Blocca'], ['lampo 7-8 secondi', 'poi 60 s in lampada'])])
figs['rimozione'] = passi('Rimozione in 5 passi', [(['Taglia'], ['accorcia la tip']), (['Fresa'], ['togli lucido e colore']), (['Ammollo'], ['remover, circa 5 min']), (['Pusher'], ['spingi via il gel']), (['Rifinisci'], ['fresa leggera,', 'poi nuova tip'])], cols=3)

# 8. Inclinazione
b = title('Inclinazione di appoggio')
def finger(x0, col):
    return f'<path d="M{x0},420 L{x0},340 Q{x0+10},300 {x0+60},300 L{x0+260},300 L{x0+260},420 Z" fill="#F2D3C9"/><rect x="{x0+70}" y="288" width="190" height="14" rx="7" fill="#fff" stroke="{GRI}" stroke-width="2"/>'
for i, (n, ok, ang, tag) in enumerate([('Corretta', True, 25, 'già inclinata, poi premi e scendi'), ('Errata', False, 70, 'colpo a vuoto, troppo dritta')]):
    x0 = 50 + i * 390
    b += finger(x0, ok) + t(x0 + 140, 110, n, 24, VER if ok else ROS, True)
    c = VER if ok else ROS
    import math
    px, py = x0 + 80, 288; L = 170; ex, ey = px + L * math.cos(math.radians(ang)), py - L * math.sin(math.radians(ang))
    b += f'<line x1="{px}" y1="{py}" x2="{ex}" y2="{ey}" stroke="{c}" stroke-width="12" stroke-linecap="round"/><path d="M{px+60},288 A60,60 0 0 0 {px+60*math.cos(math.radians(ang))},{288-60*math.sin(math.radians(ang))}" fill="none" stroke="{c}" stroke-width="3"/>'
    b += badge(x0 + 140, 480, ok) + t(x0 + 140, 535, tag, 16, c)
figs['inclinazione'] = svg(b, 600)

# 9. Semaforo anomalie
b = title('Anomalie: il semaforo')
rows = [(VER, 'SI LAVORA', ['Macchie bianche su 1-3 unghie', 'Piccola linea rossa da urto', 'Mano leggera, niente limare a fondo']), (GIA, 'CAUTELA', ['Distacco lieve (circa 1/3 unghia)', 'Macchia giallina (pseudomonas)', 'Prodotto mai sulla pelle · controllo a 2 settimane']), (ROS, 'STOP · MEDICO', ['Fungo, paronichia, allergia', 'Anomalia su molte dita', 'Distacco di metà unghia o più'])]
for i, (c, n, ls) in enumerate(rows):
    y = 90 + i * 165
    b += f'<rect x="40" y="{y}" width="720" height="145" rx="18" fill="#fff" stroke="{c}" stroke-width="4"/><circle cx="105" cy="{y+72}" r="40" fill="{c}"/>'
    b += t(190, y + 40, n, 24, c, True, 'start') + ''.join(t(190, y + 75 + j * 26, '• ' + l, 18, NERO, False, 'start') for j, l in enumerate(ls[:3])).replace(f'y="{y+75}"', f'y="{y+70}"')
b += t(W/2, 590, 'Noi curiamo l\'estetica, non la salute.', 17, GRI)
figs['semaforo'] = svg(b, 610)

html = '<html><body style="margin:0;background:#fff">' + ''.join(f'<div id="{k}" style="display:inline-block">{v}</div><br>' for k, v in figs.items()) + '</body></html>'
open(os.path.join(HERE, '_imm.html'), 'w').write(html)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{deviceScaleFactor:2}});await p.goto('file://{os.path.join(HERE,'_imm.html')}');
for (const k of {list(figs)!r}) await p.locator('#'+k).screenshot({{path:'{OUT}/'+k+'.png',omitBackground:true}});await b.close()}})()"""
open(os.path.join(HERE, '_imm.js'), 'w').write(js)
subprocess.run(['node', os.path.join(HERE, '_imm.js')], check=True)
os.remove(os.path.join(HERE, '_imm.html')); os.remove(os.path.join(HERE, '_imm.js'))
print(sorted(os.listdir(OUT)))
