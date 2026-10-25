"""Genera guida PDF, mini guida cliente e slide con l'identità Lidia Nail Expert (B · Mandorla). Uso: python3 -I build.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from contenuti import *
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, KeepTogether
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

BR = os.path.join(HERE, '..', 'brand'); LOGO = os.path.join(BR, 'logo-finale'); FONTS = os.path.join(BR, 'fonts')
for n, f in [('PF', 'PlayfairDisplay-Medium.ttf'), ('MS', 'Montserrat-Regular.ttf'), ('MSM', 'Montserrat-Medium.ttf'), ('MSB', 'Montserrat-SemiBold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, os.path.join(FONTS, f)))
OUT = os.path.join(HERE, '..', 'output'); os.makedirs(OUT, exist_ok=True)
OLIVA, SALVIA, AVORIO, ORO = colors.HexColor('#34402F'), colors.HexColor('#C9D8C5'), colors.HexColor('#FAF7F0'), colors.HexColor('#C8A04A')

def pdf(path, titolo, sotto, blocchi):
    h1 = ParagraphStyle('h1', fontName='PF', fontSize=30, textColor=OLIVA, leading=34, spaceAfter=6)
    h2 = ParagraphStyle('h2', fontName='PF', fontSize=16, textColor=OLIVA, spaceBefore=16, spaceAfter=7, leading=20)
    sub = ParagraphStyle('sub', fontName='MS', fontSize=11, textColor=colors.HexColor('#6F7A6C'), spaceAfter=14)
    body = ParagraphStyle('b', fontName='MS', fontSize=9.6, leading=14.5, textColor=OLIVA)
    def first(c, d):
        w, h = A4
        c.setFillColor(OLIVA); c.rect(0, h - 4.6 * cm, w, 4.6 * cm, stroke=0, fill=1)
        lw = 8.2 * cm; c.drawImage(os.path.join(LOGO, 'orizzontale-oro.png'), 2 * cm, h - 4.6 * cm + (4.6 * cm - lw * 260 / 700) / 2, width=lw, height=lw * 260 / 700, mask='auto')
        c.setFillColor(ORO); c.rect(0, h - 4.6 * cm - 0.12 * cm, w, 0.12 * cm, stroke=0, fill=1); foot(c, d)
    def foot(c, d):
        c.setFont('MSM', 7.5); c.setFillColor(colors.HexColor('#6F7A6C')); c.drawString(2 * cm, 1.1 * cm, 'LIDIA · NAIL EXPERT'); c.drawRightString(19 * cm, 1.1 * cm, str(d.page))
        c.setStrokeColor(ORO); c.setLineWidth(0.6); c.line(2 * cm, 1.6 * cm, 19 * cm, 1.6 * cm)
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2.2 * cm, title=titolo, author='Lidia Nail Expert')
    st = [Spacer(1, 3.4 * cm), Paragraph(titolo, h1), Paragraph(sotto, sub)]
    for t, pts in blocchi:
        items = [ListItem(Paragraph(p.replace('&', '&amp;'), body), leftIndent=14, bulletColor=ORO) for p in pts]
        st.append(KeepTogether([Paragraph(t, h2), ListFlowable(items, bulletType='bullet', bulletFontSize=7, start='•')]))
    doc.build(st, onFirstPage=first, onLaterPages=foot)

pdf(os.path.join(OUT, 'guida-professionale.pdf'), TITOLO, SOTTOTITOLO, [(t, p) for t, p, _, _ in SEZIONI])
pdf(os.path.join(OUT, 'mini-guida-cliente.pdf'), 'La cura delle tue Gel Tip', 'Piccola guida per la cliente', MINI_GUIDA)

# ---------- Slide ----------
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5); blank = prs.slide_layouts[6]
def rgb(h): return RGBColor.from_string(h)
def rect(s, x, y, w, h, fill):
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)); r.fill.solid(); r.fill.fore_color.rgb = rgb(fill); r.line.fill.background(); return r
def txt(s, t, x, y, w, h, size, font='Montserrat', color='34402F', bold=False, align=None):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; r = p.add_run(); r.text = t; r.font.size = Pt(size); r.font.name = font; r.font.bold = bold; r.font.color.rgb = rgb(color)
    if align: p.alignment = align
    return tf
from pptx.enum.text import PP_ALIGN
s = prs.slides.add_slide(blank); rect(s, 0, 0, 13.333, 7.5, '34402F')
lw = 5.2; s.shapes.add_picture(os.path.join(LOGO, 'verticale-oro.png'), Inches(1.0), Inches(0.9), height=Inches(5.7))
txt(s, TITOLO, 6.4, 2.6, 6.4, 1.8, 40, 'Playfair Display', 'C9D8C5'); rect(s, 6.45, 4.35, 1.6, 0.05, 'C8A04A'); txt(s, SOTTOTITOLO, 6.4, 4.6, 6.4, 0.6, 18, color='C9D8C5')
IMMAGINI = {3: 'struttura-tip', 4: 'tip-tipi', 5: 'misure-mano', 6: 'unghia-naturale', 7: 'scelta-misura', 9: 'applicazione', 10: 'inclinazione', 12: 'rimozione', 14: 'semaforo'}
from PIL import Image as _I
for idx, ((t, pts, nota, on), brevi) in enumerate(zip(SEZIONI, SLIDE_PUNTI)):
    if not on: continue
    s = prs.slides.add_slide(blank); rect(s, 0, 0, 13.333, 7.5, 'FAF7F0'); rect(s, 0, 0, 0.22, 7.5, 'C9D8C5'); rect(s, 0.22, 0, 0.04, 7.5, 'C8A04A')
    txt(s, t, 0.9, 0.55, 11.8, 1.0, 34, 'Playfair Display')
    img = IMMAGINI.get(idx); imgp = os.path.join(OUT, 'immagini', (img or '') + '.png')
    tf = txt(s, '', 0.9, 1.9, 6.1 if img else 11.5, 4.8, 22, 'Montserrat')
    first_p = True
    for p in brevi:
        para = tf.paragraphs[0] if first_p else tf.add_paragraph(); first_p = False
        r = para.add_run(); r.text = '•  ' + p; r.font.size = Pt(20 if img else 24); r.font.name = 'Montserrat'; r.font.color.rgb = rgb('34402F'); para.space_after = Pt(16)
    if img and os.path.exists(imgp):
        w, h = _I.open(imgp).size; wi = 5.5; hi = wi * h / w
        if hi > 5.0: wi, hi = 5.0 * w / h, 5.0
        s.shapes.add_picture(imgp, Inches(12.9 - wi), Inches(1.7), width=Inches(wi))
    s.shapes.add_picture(os.path.join(LOGO, 'emblema-oliva.png'), Inches(0.9), Inches(6.7), height=Inches(0.5))
    txt(s, 'LIDIA · NAIL EXPERT', 1.5, 6.82, 4, 0.4, 10, 'Montserrat', 'C8A04A', True)
    s.notes_slide.notes_text_frame.text = nota + "\n\nDettaglio:\n" + "\n".join("- " + p for p in pts)
prs.save(os.path.join(OUT, 'slide-lezione.pptx'))
print('ok')
