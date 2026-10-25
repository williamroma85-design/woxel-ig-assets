"""Kit social Lidia Nail Expert: template 1080x1350 / 1920 e copertine highlight. Modifica TESTI e rilancia: python3 -I social.py"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'social-kit'); os.makedirs(OUT, exist_ok=True)
OLIVA, SALVIA, AVORIO = '#34402F', '#C9D8C5', '#FAF7F0'
GOLD = 'linear-gradient(135deg,#7C5A12 0%,#D9B25A 18%,#FFF1B8 32%,#C9962F 48%,#F3D98A 66%,#A8761B 82%,#6F4E10 100%)'
EMB = lambda mode, h: open(os.path.join(HERE, 'logo-finale', f'emblema-{mode}.svg')).read().replace('width="180" height="240"', f'width="{h*0.75:.0f}" height="{h}"')
HOR = lambda mode, w: open(os.path.join(HERE, 'logo-finale', f'orizzontale-{mode}.svg')).read().replace('width="700" height="260"', f'width="{w}" height="{w*260/700:.0f}"')
F = lambda n: 'file://' + os.path.join(HERE, 'fonts', n)

# ---- TESTI (da modificare) ----
T = dict(
 cop_k='GUIDA GEL TIP', cop_t='3 errori che rovinano la tua gel tip', cop_s='Scorri →',
 con_n='01', con_t='Unghia naturale troppo lunga', con_b='Se sporge dalla tip si formano tasche d\'aria. Portala corta, pari al polpastrello, e stondata.',
 reg_k='LA REGOLA', reg_t='Unghia corta, risultato perfetto.', reg_b='Una base ben preparata vale più di mille ritocchi.',
 ev_k='ERRORE vs CORRETTO', ev_no='Colpo a vuoto, tip troppo dritta', ev_ok='Già inclinata, premi al centro e scendi lenta',
 pd_k='PRIMA / DOPO', pd_a='PRIMA', pd_b='DOPO', pd_c='Gel tip · tempo di lavoro: metà',
 cta_t='Vuoi imparare la tecnica?', cta_b='Scrivimi in DM la parola GELTIP', cta_h='@lidiafrt_nailartist',
 reel_t='Gel tip: la misura giusta in 10 secondi',
 hl=['Gel Tip', 'Prima/Dopo', 'Corsi', 'Info', 'Cura', 'Recensioni'])
css = f'''@font-face{{font-family:PF;src:url({F("PlayfairDisplay-Medium.ttf")});font-weight:500}}@font-face{{font-family:MS;src:url({F("Montserrat-Regular.ttf")});font-weight:400}}@font-face{{font-family:MS;src:url({F("Montserrat-Medium.ttf")});font-weight:500}}@font-face{{font-family:MS;src:url({F("Montserrat-SemiBold.ttf")});font-weight:600}}
body{{margin:0}}.s{{width:1080px;height:1350px;position:relative;overflow:hidden;box-sizing:border-box;padding:96px;font-family:MS;display:block;margin-bottom:20px}}.r{{height:1920px}}
.k{{font:500 26px MS;letter-spacing:.32em}}.h{{font-family:PF;font-weight:500;line-height:1.12}}.g{{background:{GOLD};-webkit-background-clip:text;background-clip:text;color:transparent}}.rule{{height:3px;width:140px;background:{GOLD};margin:34px 0}}
.foot{{position:absolute;left:96px;right:96px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font:500 22px MS;letter-spacing:.16em}}
.col{{display:flex;flex-direction:column;justify-content:center;height:100%}}'''
def slide(i, cls, bg, body, dark):
    c = SALVIA if dark else OLIVA
    return f'<div class="s {cls}" id="{i}" style="background:{bg};color:{c}">{body}</div>'
S = []
S.append(slide('01-carosello-copertina', '', OLIVA, f'<div class="col"><div class="k g">{T["cop_k"]}</div><div class="rule"></div><div class="h g" style="font-size:112px">{T["cop_t"]}</div></div><div class="foot"><span>{T["cop_s"]}</span>{EMB("oro",70)}</div>', True))
S.append(slide('02-carosello-contenuto', '', SALVIA, f'<div class="k" style="color:{OLIVA}">{T["con_n"]} / 07</div><div class="col" style="height:70%"><div class="h" style="font-size:92px;color:{OLIVA}">{T["con_t"]}</div><div class="rule"></div><div style="font-size:40px;line-height:1.5;color:{OLIVA}">{T["con_b"]}</div></div><div class="foot"><span>LIDIA · NAIL EXPERT</span>{EMB("oliva",70)}</div>', False))
S.append(slide('03-regola-citazione', '', AVORIO, f'<div class="col" style="align-items:center;text-align:center"><div class="k" style="color:#A8761B">{T["reg_k"]}</div><div class="rule"></div><div class="h" style="font-size:104px;color:{OLIVA}">{T["reg_t"]}</div><div style="font-size:36px;line-height:1.5;margin-top:40px;color:#4a5646">{T["reg_b"]}</div></div><div class="foot" style="justify-content:center">{EMB("oro",86)}</div>', False))
S.append(slide('04-errore-vs-corretto', '', OLIVA, f'<div class="k g">{T["ev_k"]}</div><div style="display:grid;gap:40px;margin-top:60px"><div style="border:3px solid #C0453F55;border-radius:28px;padding:50px"><div class="k" style="color:#E7928C">✕ ERRATO</div><div class="h" style="font-size:64px;margin-top:20px;color:{SALVIA}">{T["ev_no"]}</div></div><div style="border:3px solid #C9D8C5;border-radius:28px;padding:50px"><div class="k" style="color:{SALVIA}">✓ CORRETTO</div><div class="h g" style="font-size:64px;margin-top:20px">{T["ev_ok"]}</div></div></div><div class="foot"><span>LIDIA · NAIL EXPERT</span>{EMB("oro",70)}</div>', True))
fr = lambda l, bg: f'<div style="background:{bg};border-radius:24px;height:640px;display:flex;align-items:flex-end;justify-content:center;padding:20px;box-sizing:border-box"><div class="k" style="color:{OLIVA};background:#FAF7F0cc;padding:8px 18px;border-radius:30px">{l}</div></div>'
S.append(slide('05-prima-dopo', '', AVORIO, f'<div class="k" style="color:#A8761B">{T["pd_k"]}</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:50px">{fr(T["pd_a"], SALVIA)}{fr(T["pd_b"], "#b6c9b1")}</div><div class="h" style="font-size:56px;margin-top:50px;color:{OLIVA}">{T["pd_c"]}</div><div class="foot">{EMB("oro",70)}<span style="color:{OLIVA}">{T["cta_h"]}</span></div>', False))
S.append(slide('06-cta-chiusura', '', OLIVA, f'<div class="col" style="align-items:center;text-align:center">{HOR("oro",640)}<div class="rule" style="margin:70px 0"></div><div class="h" style="font-size:84px;color:{SALVIA}">{T["cta_t"]}</div><div style="font-size:38px;margin-top:36px;color:{SALVIA}">{T["cta_b"]}</div><div class="k g" style="margin-top:50px">{T["cta_h"]}</div></div>', True))
S.append(slide('07-reel-cover', 'r', SALVIA, f'<div class="col" style="padding:0 0"><div class="k" style="color:{OLIVA}">GEL TIP · TUTORIAL</div><div class="rule"></div><div class="h" style="font-size:126px;color:{OLIVA}">{T["reel_t"]}</div></div><div class="foot" style="bottom:300px">{EMB("oliva",90)}</div>', False))
for i, n in enumerate(T['hl']):
    bg, c, m = (OLIVA, SALVIA, 'oro') if i % 2 == 0 else (SALVIA, OLIVA, 'oliva')
    S.append(slide(f'hl-{i+1}-{n.lower().replace("/","-")}', 'r', bg, f'<div class="col" style="align-items:center;text-align:center;gap:50px">{EMB(m,260)}<div class="h" style="font-size:96px;color:{c}">{n}</div></div>', False))
html = f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(S)}</body></html>'
p = os.path.join(HERE, '_s.html'); open(p, 'w').write(html)
ids = [s.split('id="')[1].split('"')[0] for s in S]
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:1200,height:1400}}}});await pg.goto('file://{p}');await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(500);
for(const id of {ids!r}) await pg.locator('[id="'+id+'"]').screenshot({{path:'{OUT}/'+id+'.png'}});await b.close()}})()"""
open(os.path.join(HERE, '_s.js'), 'w').write(js); subprocess.run(['node', os.path.join(HERE, '_s.js')], check=True); os.remove(p); os.remove(os.path.join(HERE, '_s.js'))
print(sorted(os.listdir(OUT)))
