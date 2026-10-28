#!/usr/bin/env python3
"""STP 596 seminer sunumunu dersin şablonundan kurar.

Kullanım:
  python3 deste_kur.py sunum.md --sablon assets/sunum_format_16x9.pptx --cikti 514xxxxxx_Soyad_stp596_sunum.pptx

sunum.md biçimi references/sunum.md içinde: '---' arasında ön bilgi (baslik, hazirlayan, program, kurum,
danisman, tarih, eposta, sayfa_no, yz_satiri), ardından her '## [tür] Başlık' bir slayt. Türler: icindekiler, metin,
gorsel, metin_gorsel, uc_gorsel, sayilar, tablo, karsilastirma, kartlar, surec, zaman, kaynaklar, tesekkur
(kapak ön bilgiden kurulur). 'mesaj: …' satırı başlığın altına tam cümlelik iddia yazar (Alley: iddia–kanıt).
'### Alt başlık' satırları karsilastirma/kartlar/surec türlerinde blok açar.
Gövdede '-' madde, düz satır paragraf, '![alt yazı](dosya)' görsel, '>' konuşma notu, '~~~' tıklama grubu
ayracı, 'punto: 16' gövde puntosu, 'animasyon: evet' görsel/sayı slaytlarında tıklamayla açılma.
'$$ LaTeX $$' satırı (metin ve metin_gorsel türlerinde) gövde puntosunda, düzenlenebilir PowerPoint denklemi olur;
pandoc yoksa yer tutucu yazılır ve uyarılır (scripts/denklem.py).
'~~~' ya da 'animasyon: evet' kullanıldıysa çıktının yanına anim.json yazılır; scripts/anim.py ile uygulanır.
Punto deste genelinde tektir: betik önce her metin alanına sığan en büyük puntoyu ölçer, sonra aynı roldeki
bütün alanları (başlık, gövde, süreç kutusu, tablo) bu ölçülerin en küçüğüyle yazar; slayttan slayta punto değişmez.
Gerekli paket: python-pptx (pip install python-pptx). Görsel boyutu için Pillow varsa kullanılır.
"""
import argparse, copy, json, os, re, sys
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import denklem

NAVY = RGBColor(0x02, 0x27, 0x56)
GREY = RGBColor(0x6E, 0x6E, 0x6E)
FONT = "Helvetica"
SLIDE_W, SLIDE_H = 13.333, 7.5
TEMPLATE_INDEX = {"kapak": 0, "metin": 1, "gorsel": 2, "metin_gorsel": 3, "uc_gorsel": 4, "sayilar": 5, "tesekkur": 6,
                  "icindekiler": 1, "kaynaklar": 1, "tablo": 1, "karsilastirma": 1, "kartlar": 1, "surec": 1, "zaman": 1}
BRONZE = RGBColor(0x8B, 0x73, 0x4A)
STEEL = RGBColor(0x5B, 0x7A, 0x99)
LIGHT = RGBColor(0xF2, 0xF4, 0xF8)
LINE = RGBColor(0xBF, 0xC5, 0xCE)
BODY_X, BODY_W, BODY_BOTTOM = 0.84, 11.65, 6.72
WARN = []
DECK = {}   # rol -> deste genelindeki punto; boşsa ölçüm turundayız
FITS = {}   # ölçüm turu: rol -> [(alana sığan punto, slayt başlığı)]

def warn(msg):
    WARN.append(msg)

def deck_size(role, fit, label=""):
    """Ölçüm turunda alana sığan puntoyu kaydeder; kurulum turunda rolün deste genelindeki puntosunu verir."""
    if role in DECK:
        return DECK[role]
    FITS.setdefault(role, []).append((fit, label))
    return fit

# ---------------- sunum.md ----------------

def parse_md(path):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip().lower()] = v.strip()
        body = m.group(2)
    slides, cur = [], None
    for line in body.split("\n"):
        h = re.match(r"^##\s+(?:\[(\w+)\]\s*)?(.*)$", line)
        if h:
            cur = {"tur": (h.group(1) or "").lower(), "baslik": h.group(2).strip(), "paralar": [[]], "gorseller": [],
                   "notlar": [], "punto": None, "animasyon": False, "mesaj": "", "bloklar": [], "denklemler": []}
            slides.append(cur)
            continue
        if cur is None or not line.strip() and False:
            continue
        if cur is None:
            continue
        s = line.rstrip()
        if not s.strip():
            continue
        if re.match(r"^###\s+", s.strip()):
            cur["bloklar"].append({"baslik": re.sub(r"^###\s+", "", s.strip()), "items": []}); continue
        mm = re.match(r"^mesaj:\s*(.+)$", s.strip(), re.I)
        if mm:
            cur["mesaj"] = mm.group(1).strip(); continue
        eq = re.match(r"^\$\$(.+?)\$\$\s*$", s.strip())
        if eq:                                  # akıştaki yeri korunur: ("denklem", sıra no)
            cur["denklemler"].append(eq.group(1).strip())
            cur["paralar"][-1].append(("denklem", str(len(cur["denklemler"]) - 1))); continue
        img = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", s.strip())
        if img:
            cur["gorseller"].append({"alt": img.group(1).strip(), "dosya": img.group(2).strip()}); continue
        if s.strip().startswith(">"):
            cur["notlar"].append(s.strip()[1:].strip()); continue
        if s.strip() == "~~~":
            cur["paralar"].append([]); continue
        pm = re.match(r"^punto:\s*(\d+)", s.strip(), re.I)
        if pm:
            cur["punto"] = int(pm.group(1)); continue
        if re.match(r"^animasyon:\s*(evet|yes|true)", s.strip(), re.I):
            cur["animasyon"] = True; continue
        if re.match(r"^[-*•]\s+", s.strip()):
            item = ("madde", re.sub(r"^[-*•]\s+", "", s.strip()))
        elif re.match(r"^\d+[.)]\s+", s.strip()):
            item = ("numara", s.strip())
        else:
            item = ("paragraf", s.strip())
        if cur["bloklar"]:
            cur["bloklar"][-1]["items"].append(item)
        else:
            cur["paralar"][-1].append(item)
    for sl in slides:
        if not sl["tur"]:
            b = sl["baslik"].lower()
            n = len(sl["gorseller"]); has_text = any(sl["paralar"][0]) or len(sl["paralar"]) > 1
            if "kaynak" in b: sl["tur"] = "kaynaklar"
            elif "içindekiler" in b or "icindekiler" in b: sl["tur"] = "icindekiler"
            elif "teşekkür" in b or "tesekkur" in b: sl["tur"] = "tesekkur"
            elif n >= 3: sl["tur"] = "uc_gorsel"
            elif n >= 1 and has_text: sl["tur"] = "metin_gorsel"
            elif n >= 1: sl["tur"] = "gorsel"
            else: sl["tur"] = "metin"
        if sl["tur"] not in TEMPLATE_INDEX or sl["tur"] == "kapak":
            warn(f"Bilinmeyen tür '{sl['tur']}' ({sl['baslik']}); 'metin' kullanıldı."); sl["tur"] = "metin"
        if sl["denklemler"] and sl["tur"] not in ("metin", "metin_gorsel"):
            warn(f"'{sl['baslik']}': denklem yalnız metin ve metin_gorsel slaytlarında yerleştirilir; bu slayttakiler yok sayıldı.")
            sl["denklemler"] = []
        if sl["denklemler"] and len([g for g in sl["paralar"] if g]) > 1:
            warn(f"'{sl['baslik']}': denklemli slaytta '~~~' tıklama grupları desteklenmez; gruplar birleştirildi.")
            sl["paralar"] = [[it for g in sl["paralar"] for it in g]]
        if not sl["denklemler"]:
            sl["paralar"] = [[it for it in g if it[0] != "denklem"] for g in sl["paralar"]]
    return meta, slides

def text_groups(groups):
    """Denklem işaretleri çıkarılmış metin grupları (punto ve sığma hesabı için)."""
    return [[it for it in g if it[0] != "denklem"] for g in groups]

# ---------------- pptx yardımcıları ----------------

def duplicate_slide(prs, src):
    new = prs.slides.add_slide(src.slide_layout)
    for shp in list(new.shapes):
        shp._element.getparent().remove(shp._element)
    for shp in src.shapes:
        new.shapes._spTree.insert_element_before(copy.deepcopy(shp._element), "p:extLst")
    return new

def delete_slide(prs, index):
    sldIdLst = prs.slides._sldIdLst
    sldId = list(sldIdLst)[index]
    prs.part.drop_rel(sldId.rId)
    sldIdLst.remove(sldId)

def find_shape(slide, pred):
    for sh in slide.shapes:
        if pred(sh):
            return sh
    return None

def text_of(sh):
    return sh.text_frame.text if sh.has_text_frame else ""

def remove_shape(sh):
    sh._element.getparent().remove(sh._element)

def set_name(sh, name):
    sh._element.xpath("./*[local-name()='nvSpPr' or local-name()='nvPicPr' or local-name()='nvGrpSpPr' or local-name()='nvCxnSpPr' or local-name()='nvGraphicFramePr']/*[local-name()='cNvPr']")[0].set("name", name)

def style_run(run, size=None, bold=None, color=None, font=FONT, italic=None):
    f = run.font
    f.name = font
    if size is not None: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color is not None: f.color.rgb = color

def set_bullet(para, char="•", indent_in=0.3):
    pPr = para._p.get_or_add_pPr()
    pPr.set("marL", str(int(Inches(indent_in)))); pPr.set("indent", str(-int(Inches(indent_in))))
    for tag in ("a:buNone", "a:buChar", "a:buAutoNum", "a:buFont"):
        for el in pPr.findall(qn(tag)): pPr.remove(el)
    bf = etree.SubElement(pPr, qn("a:buFont")); bf.set("typeface", "Arial")
    bc = etree.SubElement(pPr, qn("a:buChar")); bc.set("char", char)

def fill_text(sh, items, size=18, color=NAVY, align=None, space_after=6, bold_first=False, line_spacing=None):
    """items: [(kind, text)] ; kind: paragraf | madde | numara. Kutunun ilk run biçimini (font) korur, puntoyu verir."""
    tf = sh.text_frame
    tf.word_wrap = True
    # ilk paragrafı kalıp al
    first = tf.paragraphs[0]
    for p in list(tf.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    for r in list(first.runs):
        r._r.getparent().remove(r._r)
    for i, (kind, text) in enumerate(items):
        para = first if i == 0 else tf.add_paragraph()
        if i > 0:
            # kalıp pPr'yi kopyala (hizalama vb.)
            if first._p.pPr is not None:
                para._p.insert(0, copy.deepcopy(first._p.pPr))
        run = para.add_run(); run.text = text
        style_run(run, size=size, color=color, bold=(bold_first and i == 0) or None)
        if kind == "madde":
            set_bullet(para)
        else:
            pPr = para._p.get_or_add_pPr()
            for tag in ("a:buChar", "a:buAutoNum", "a:buFont"):
                for el in pPr.findall(qn(tag)): pPr.remove(el)
            pPr.set("marL", "0"); pPr.set("indent", "0")
        para.space_after = Pt(space_after)
        if line_spacing: para.line_spacing = line_spacing
        if align is not None: para.alignment = align
    return sh

def add_textbox(slide, x, y, w, h, items, size=18, color=NAVY, align=None, anchor=None, name=None, bold_first=False, space_after=6):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    if anchor is not None: tf.vertical_anchor = anchor
    fill_text(tb, items, size=size, color=color, align=align, bold_first=bold_first, space_after=space_after)
    if name: set_name(tb, name)
    return tb

def image_size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None

def check_shrink(pic, label):
    """Görsel çizildiği boyuttan çok küçültüldüyse uyarır: içindeki yazı da aynı oranda küçülür."""
    dx, _ = pic.image.dpi
    if dx == 72:          # çözünürlük bilgisi yok (python-pptx varsayılanı); ölçülemez
        return
    oran = pic.width / 914400 / (pic.image.size[0] / dx)
    if oran < 0.7:
        warn(f"'{label}': görsel çizildiği boyutun %{oran * 100:.0f}'ine küçültüldü; içindeki yazı da küçüldü (16 pt → ≈ {16 * oran:.0f} pt). "
             f"Slayttaki boyutunda ({pic.width / 914400:.1f} × {pic.height / 914400:.1f} inç) yeniden üretin.")

def add_picture_fit(slide, path, x, y, w, h, name=None, label=""):
    """Görseli (x,y,w,h) kutusuna sığdırıp ortalar."""
    size = image_size(path)
    if size:
        iw, ih = size
        scale = min(Inches(w) / iw, Inches(h) / ih)
        pw, ph = int(iw * scale), int(ih * scale)
    else:
        pic = slide.shapes.add_picture(path, Inches(x), Inches(y))
        scale = min(Inches(w) / pic.width, Inches(h) / pic.height)
        pw, ph = int(pic.width * scale), int(pic.height * scale)
        remove_shape(pic)
    px = int(Inches(x) + (Inches(w) - pw) / 2); py = int(Inches(y) + (Inches(h) - ph) / 2)
    pic = slide.shapes.add_picture(path, px, py, pw, ph)
    if name: set_name(pic, name)
    check_shrink(pic, label or os.path.basename(path))
    return pic

def place_image(slide, g, x, y, w, h, idx, caption_size=14, base_dir=".", cap_h=None):
    """Görsel + alt yazı; dosya yoksa yer tutucu kutu."""
    path = g["dosya"] if os.path.isabs(g["dosya"]) else os.path.join(base_dir, g["dosya"])
    if cap_h is None:
        cap_h = 0.55 if g["alt"] else 0
    if os.path.exists(path):
        add_picture_fit(slide, path, x, y, w, h - cap_h, name=f"gorsel{idx}", label=f"{g.get('_slayt', '')[:40]} · {os.path.basename(path)}")
    else:
        warn(f"Görsel bulunamadı: {g['dosya']} (slayt: {g.get('_slayt','?')}); yer tutucu kondu.")
        box = slide.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h - cap_h))  # dikdörtgen
        box.fill.solid(); box.fill.fore_color.rgb = RGBColor(0xEC, 0xEC, 0xEC); box.line.color.rgb = RGBColor(0xBF, 0xBF, 0xBF)
        set_name(box, f"gorsel{idx}")
        fill_text(box, [("paragraf", f"[ÖĞRENCİ TAMAMLAYACAK: görsel · {g['alt'] or g['dosya']}]")], size=16, color=GREY, align=PP_ALIGN.CENTER)
        box.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    if g["alt"]:
        add_textbox(slide, x, y + h - cap_h + 0.02, w, cap_h, [("paragraf", g["alt"])], size=caption_size, color=GREY,
                    align=PP_ALIGN.CENTER, name=f"altyazi{idx}")

def place_layered_images(slide, sl, x, y, w, h, base_dir):
    """Tek görsel: normal yerleşim. Birden çok görsel: aynı kutuya katman katman (gorsel1..n);
    alt yazı son katmanınki. Katmanlar tıklama senaryosuna girer (sl["_katman"] = n)."""
    gs = sl["gorseller"] or [{"alt": "", "dosya": "(yok)"}]
    for g in gs: g["_slayt"] = sl["baslik"]
    if len(gs) == 1:
        place_image(slide, gs[0], x, y, w, h, 1, base_dir=base_dir)
        return
    cap = gs[-1]["alt"]
    for i, g in enumerate(gs, 1):
        g2 = dict(g); g2["alt"] = cap if i == len(gs) else ""
        place_image(slide, g2, x, y, w, h, i, base_dir=base_dir, cap_h=0.55 if cap else 0)
    # alt yazı yüksekliği her katmanda aynı olsun diye ilk katmanlara da boş alt yazı payı bırakıldı
    sl["_katman"] = len(gs)

def body_top(sl):
    """Mesaj satırı varsa gövde 2.05'ten, yoksa 1.45'ten başlar."""
    return 2.1 if sl.get("mesaj") else 1.45

def add_message(slide, sl):
    """Başlığın altına tam cümlelik iddia (Alley: assertion). 20 pt lacivert, solda ince bronz çizgi."""
    if not sl.get("mesaj"):
        return
    bar = slide.shapes.add_shape(1, Inches(BODY_X), Inches(1.32), Inches(0.06), Inches(0.62))
    bar.fill.solid(); bar.fill.fore_color.rgb = BRONZE; bar.line.fill.background(); set_name(bar, "mesaj_cizgi")
    n = len(sl["mesaj"])
    size = 20 if n <= 110 else 18 if n <= 140 else 16
    if n > 160: warn(f"'{sl['baslik']}': mesaj satırı çok uzun ({n} karakter); tek cümle, en çok 140 karakter.")
    add_textbox(slide, BODY_X + 0.18, 1.3, BODY_W - 0.18, 0.7, [("paragraf", sl["mesaj"])], size=size, color=NAVY,
                anchor=MSO_ANCHOR.MIDDLE, name="mesaj")

def shape_text(shp, items, size, color=NAVY, align=None, anchor=MSO_ANCHOR.TOP, bold_first=False, margin=0.1):
    tf = shp.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(margin); tf.margin_top = tf.margin_bottom = Inches(0.06)
    fill_text(shp, items, size=size, color=color, align=align, bold_first=bold_first, space_after=4)

def add_box(slide, x, y, w, h, fill=None, line=LINE, name=None, rounded=False):
    shp = slide.shapes.add_shape(5 if rounded else 1, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None: shp.fill.background()
    else: shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None: shp.line.fill.background()
    else: shp.line.color.rgb = line; shp.line.width = Pt(1)
    shp.shadow.inherit = False
    if name: set_name(shp, name)
    return shp

def add_arrow(slide, x1, y1, x2, y2, name=None):
    c = slide.shapes.add_connector(1, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = NAVY; c.line.width = Pt(1.5)
    ln = c.line._get_or_add_ln()
    te = etree.SubElement(ln, qn("a:tailEnd")); te.set("type", "triangle"); te.set("w", "med"); te.set("len", "med")
    if name: set_name(c, name)
    return c

def blocks_or_items(sl):
    """Bloklar yoksa her madde bir blok (başlıksız) sayılır."""
    if sl["bloklar"]:
        return sl["bloklar"]
    return [{"baslik": "", "items": [it]} for g in sl["paralar"] for it in g if it[1].strip()]

def set_title(slide, title):
    tb = find_shape(slide, lambda s: text_of(s).startswith("Başlık (Helvetica"))
    if tb is None:
        return
    n = len(title)
    size = deck_size("baslik", 28 if n <= 30 else 24 if n <= 37 else 20 if n <= 45 else 18, title)
    if n > 52:
        warn(f"Başlık çok uzun ({n} karakter), en çok 45 olmalı: {title[:40]}…")
    tb.left, tb.width = Inches(6.75), Inches(6.3)
    tb.text_frame.word_wrap = False
    para = tb.text_frame.paragraphs[0]
    rpr_color_el = None
    for r in list(para.runs)[1:]:
        r._r.getparent().remove(r._r)
    run = para.runs[0]; run.text = title
    run.font.size = Pt(size); run.font.name = FONT
    para.alignment = PP_ALIGN.CENTER
    tb.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_name(tb, "baslik")

def set_footer(slide, name):
    fb = find_shape(slide, lambda s: text_of(s).strip().lower() == "sunumu hazırlayan")
    if fb is not None:
        run = fb.text_frame.paragraphs[0].runs[0]
        for r in list(fb.text_frame.paragraphs[0].runs)[1:]:
            r._r.getparent().remove(r._r)
        run.text = name
        fb.left, fb.width = Inches(3.5), Inches(6.33)
        set_name(fb, "altbilgi")

def add_page_number(slide, n, total):
    add_textbox(slide, 11.9, 6.88, 1.1, 0.35, [("paragraf", f"{n} / {total}")], size=12, color=NAVY, align=PP_ALIGN.RIGHT, name="sayfa_no")

def estimate_lines(items, size, width_in):
    cpl = max(10, int(width_in * 72 / (size * 0.5)))   # satır başına karakter tahmini
    return sum(max(1, -(-len(t) // cpl)) for _, t in items) + 0.3 * len(items)

def fill_body_groups(slide, groups, x, y, w, h, size):
    """Gövdeyi tıklama gruplarına böler; grup kutuları alt alta, satır sayısına orantılı yükseklikte."""
    groups = [g for g in groups if g]
    if not groups:
        return
    if len(groups) == 1:
        add_textbox(slide, x, y, w, h, groups[0], size=size, name="govde")
        return
    line_h = size * 1.3 / 72          # inç
    cy = y
    for i, g in enumerate(groups, 1):
        gh = min(h - (cy - y), estimate_lines(g, size, w) * line_h + 0.25)
        add_textbox(slide, x, cy, w, gh, g, size=size, name=f"govde{i}")
        cy += gh
    if cy - y > h + 0.01:
        warn("Tıklama grupları gövde alanını aşıyor; slaydı bölün.")

def auto_size(groups, w, h, base=18, max_size=24):
    """Alana sığan en büyük punto (24, 22, 20, 18); deck_size ile deste genelinde en küçüğü kullanılır."""
    groups = [g for g in groups if g]
    if not groups:
        return base
    for size in [z for z in (28, 24, 22, 20, 18, 16) if base <= z <= max_size]:
        need = sum(estimate_lines(g, size, w) * size * 1.3 / 72 + 0.25 for g in groups)
        if need <= h * 0.92:
            return size
    return base

def check_overflow(items, size, w, h, label):
    lines = estimate_lines(items, size, w)
    cap = h * 72 / (size * 1.35)
    if lines > cap:
        warn(f"'{label}': metin kutuya sığmayabilir (~{lines:.0f} satır, kapasite ~{cap:.0f}). Slaydı bölün; puntoyu küçültmeyin.")

def eq_reserve(sl, size=24):
    """Denklemlerin gövdede kaplayacağı yükseklik (inç)."""
    return sum(denklem.eq_height(x, size) for x in sl["denklemler"])

def add_equation(slide, sl, latex, i, x, y, w, size):
    """Bir denklemi (x, y)'den başlayan, w genişliğinde ortalı kutuya gövde puntosunda yerleştirir; yüksekliği döner.
    PowerPoint denklemi (a14:m) olur; PowerPoint dışındaki programlar için düz metinli yedek eklenir.
    Çevrilemeyen denklemin yerine yer tutucu yazılır."""
    h = denklem.eq_height(latex, size)
    omml = denklem.latex_to_omml(latex)
    if omml is None:
        neden = "pandoc bulunamadı" if not denklem.pandoc_var() else "LaTeX çevrilemedi"
        warn(f"'{sl['baslik']}': denklem PowerPoint denklemine çevrilemedi ({neden}); yer tutucu yazıldı. PowerPoint'te Ekle → Denklem ile yazın.")
        add_textbox(slide, x, y, w, h, [("paragraf", f"[ÖĞRENCİ TAMAMLAYACAK: denklem, PowerPoint'te Ekle → Denklem ile: {latex}]")],
                    size=size, align=PP_ALIGN.CENTER, name=f"denklem{i}")
        return h
    tree = slide.shapes._spTree
    ids = [int(e.get("id")) for e in tree.iter() if e.tag.endswith("}cNvPr") and e.get("id", "").isdigit()]
    nid = max(ids + [1]) + 1
    P_, A_, M_ = qn("p:sp").split("}")[0][1:], qn("a:p").split("}")[0][1:], denklem.M
    MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
    A14 = "http://schemas.microsoft.com/office/drawing/2010/main"
    def sp(body):
        return (f'<p:sp xmlns:p="{P_}" xmlns:a="{A_}"><p:nvSpPr><p:cNvPr id="{nid}" name="denklem{i}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
                f'<p:spPr><a:xfrm><a:off x="{int(Inches(x))}" y="{int(Inches(y))}"/><a:ext cx="{int(Inches(w))}" cy="{int(Inches(h))}"/></a:xfrm>'
                f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>'
                f'<p:txBody><a:bodyPr wrap="square" rtlCol="0" anchor="ctr"/><a:lstStyle/><a:p><a:pPr algn="ctr"/>{body}</a:p></p:txBody></p:sp>')
    lin = denklem.linear_text(omml).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    ac = etree.fromstring(
        f'<mc:AlternateContent xmlns:mc="{MC}"><mc:Choice xmlns:a14="{A14}" Requires="a14">'
        + sp(f'<a14:m><m:oMathPara xmlns:m="{M_}"><m:oMathParaPr><m:jc m:val="centerGroup"/></m:oMathParaPr></m:oMathPara></a14:m>')
        + '</mc:Choice><mc:Fallback>'
        + sp(f'<a:r><a:rPr lang="tr-TR" sz="{int(size * 100)}"><a:solidFill><a:srgbClr val="022756"/></a:solidFill><a:latin typeface="{FONT}"/></a:rPr><a:t>{lin}</a:t></a:r>')
        + '</mc:Fallback></mc:AlternateContent>')
    ac.find(f".//{{{M_}}}oMathPara").append(denklem.for_pptx(omml, size))
    tree.append(ac)
    return h

def body_with_equations(slide, sl, groups, x, y, w, h, size):
    """Gövdeyi yazar; denklemli slaytta metin ve denklemler sunum.md'deki sırayla alt alta dizilir."""
    if not sl["denklemler"]:
        fill_body_groups(slide, groups, x, y, w, h, size); return
    items = [it for g in groups for it in g]
    cy, chunk, n_txt, n_eq = y, [], 0, 0
    def flush():
        nonlocal cy, chunk, n_txt
        if chunk:
            th = estimate_lines(chunk, size, w) * size * 1.3 / 72 + 0.15
            n_txt += 1
            add_textbox(slide, x, cy, w, th, chunk, size=size, name="govde" if n_txt == 1 else f"govde_{n_txt}")
            cy += th; chunk = []
    for kind, val in items:
        if kind == "denklem":
            flush(); n_eq += 1
            cy += add_equation(slide, sl, sl["denklemler"][int(val)], n_eq, x, cy, w, size)
        else:
            chunk.append((kind, val))
    flush()
    if cy - y > h + 0.05:
        warn(f"'{sl['baslik']}': denklemler ve metin gövdeye sığmıyor; slaydı bölün.")

# ---------------- slayt kurucular ----------------

def build_kapak(slide, meta):
    t = find_shape(slide, lambda s: text_of(s).startswith("LOREM IPSUM"))
    d = find_shape(slide, lambda s: "??.??" in text_of(s))
    h = find_shape(slide, lambda s: text_of(s).strip().lower() == "sunumu hazırlayan")
    title = meta.get("baslik", "[ÖĞRENCİ TAMAMLAYACAK: başlık]")
    if t:
        run = t.text_frame.paragraphs[0].runs[0]
        for r in list(t.text_frame.paragraphs[0].runs)[1:]: r._r.getparent().remove(r._r)
        run.text = title; run.font.size = Pt(50 if len(title) <= 28 else 40 if len(title) <= 50 else 32)
        t.left, t.width = Inches(1.0), Inches(11.33); t.top, t.height = Inches(2.9), Inches(1.9)
        t.text_frame.word_wrap = True; t.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        set_name(t, "kapak_baslik")
    if d:
        d.text_frame.paragraphs[0].runs[0].text = meta.get("tarih", "")
        for r in list(d.text_frame.paragraphs[0].runs)[1:]: r._r.getparent().remove(r._r)
        set_name(d, "kapak_tarih")
    if h:
        h.text_frame.paragraphs[0].runs[0].text = meta.get("hazirlayan", "[ÖĞRENCİ TAMAMLAYACAK: ad]")
        for r in list(h.text_frame.paragraphs[0].runs)[1:]: r._r.getparent().remove(r._r)
        h.left, h.width = Inches(2.0), Inches(9.33)
        set_name(h, "kapak_ad")
    adv = "Advisor" if meta.get("dil", "tr").strip().lower() == "en" else "Danışman"
    lines = [v for v in (meta.get("program"), meta.get("kurum"),
                         f"{adv}: {meta['danisman']}" if meta.get("danisman") else None) if v]
    if lines:
        add_textbox(slide, 2.0, 4.95, 9.33, 1.3, [("paragraf", l) for l in lines], size=18, color=NAVY,
                    align=PP_ALIGN.CENTER, name="kapak_kunye", space_after=2)

def build_metin(slide, sl, meta, size=None):
    groups = sl["paralar"]
    x, y, w, h = BODY_X, body_top(sl), BODY_W, BODY_BOTTOM - body_top(sl)
    size = sl["punto"] or size or deck_size("govde", auto_size(text_groups(groups), w, h - eq_reserve(sl)), sl["baslik"])
    if sl["punto"]:
        check_overflow([it for g in groups for it in g], size, w, h, sl["baslik"])
    # şablonun Lorem kutusunu kaldırıp yeniden kur (grup bölme ve konum için)
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    body_with_equations(slide, sl, groups, x, y, w, h, size)

def build_icindekiler(slide, sl, meta):
    items = [(k, t) for g in sl["paralar"] for (k, t) in g]
    numbered = [("paragraf", f"{i}.  {t}") for i, (_, t) in enumerate(items, 1)]
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    add_textbox(slide, 1.6, 1.6, 10.0, 5.0, numbered, size=sl["punto"] or 22, name="govde", space_after=10)

def build_kaynaklar(slide, sl, meta, chunk):
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    add_textbox(slide, 0.84, 1.4, 11.65, 5.35, [("paragraf", t) for t in chunk], size=sl["punto"] or 14, name="govde", space_after=5)

def build_gorsel(slide, sl, meta, base_dir):
    for sh in list(slide.shapes):
        if sh.name.startswith("Dikdörtgen") or text_of(sh).strip().lower() == "görsel alan":
            remove_shape(sh)
    t = body_top(sl); place_layered_images(slide, sl, 0.8, t, 11.7, BODY_BOTTOM - t, base_dir)
    extra = [it for grp in sl["paralar"] for it in grp]
    if extra:
        warn(f"'{sl['baslik']}': gorsel türünde metin yok sayıldı ({len(extra)} satır); metin_gorsel kullanın.")

def build_metin_gorsel(slide, sl, meta, base_dir):
    for sh in list(slide.shapes):
        if sh.name.startswith("Dikdörtgen") or text_of(sh).strip().lower() == "görsel alan" or text_of(sh).startswith("Lorem"):
            remove_shape(sh)
    x, y, w, h = BODY_X, body_top(sl), 5.3, BODY_BOTTOM - body_top(sl)
    size = sl["punto"] or deck_size("govde", auto_size(text_groups(sl["paralar"]), w, h - eq_reserve(sl)), sl["baslik"])
    if sl["punto"]:
        check_overflow([it for g in sl["paralar"] for it in g], size, w, h, sl["baslik"])
    body_with_equations(slide, sl, sl["paralar"], x, y, w, h, size)
    place_layered_images(slide, sl, 6.5, y, 6.1, h, base_dir)

def build_uc_gorsel(slide, sl, meta, base_dir):
    for sh in list(slide.shapes):
        if sh.name.startswith("Dikdörtgen") or text_of(sh).strip().lower() == "görsel alan":
            remove_shape(sh)
    if len(sl["gorseller"]) > 3:
        warn(f"'{sl['baslik']}': {len(sl['gorseller'])} görsel verildi, slaytta yalnız ilk 3'ü yer alır; fazlası okunmaz. Slaydı bölün ya da mesajı taşıyanları seçin.")
    gs = (sl["gorseller"] + [{"alt": "", "dosya": "(yok)"}] * 3)[:3]
    for i, g in enumerate(gs, 1):
        g["_slayt"] = sl["baslik"]
        place_image(slide, g, 0.55 + (i - 1) * 4.12, body_top(sl), 3.95, 6.1 - body_top(sl), i, base_dir=base_dir)
    extra = [it for grp in sl["paralar"] for it in grp]
    if extra:
        add_textbox(slide, 0.84, 6.15, 11.65, 0.7, extra[:1], size=18, align=PP_ALIGN.CENTER, name="govde")

def build_sayilar(slide, sl, meta):
    groups = [sh for sh in slide.shapes if sh.shape_type == 6]
    items = [t for g in sl["paralar"] for (_, t) in g]
    nums = [it for it in items if "|" in it][:3]
    rest = [it for it in items if "|" not in it]
    # iç metin kutularını boşalt
    def clear_text(shp):
        if shp.shape_type == 6:
            for c in shp.shapes: clear_text(c)
        elif shp.has_text_frame and shp.text_frame.text.strip():
            for p in shp.text_frame.paragraphs:
                for r in p.runs: r.text = ""
    for i, grp in enumerate(groups, 1):
        clear_text(grp)
        cx = grp.left / 914400 + grp.width / 914400 / 2; cy = grp.top / 914400 + grp.height / 914400 / 2
        if i <= len(nums):
            num, label = [s.strip() for s in nums[i - 1].split("|", 1)]
        else:
            num, label = "[?]", "[ÖĞRENCİ TAMAMLAYACAK]"
            warn(f"'{sl['baslik']}': {i}. sayı eksik ('sayı | etiket' satırı).")
        tb = add_textbox(slide, cx - 1.35, cy - 0.85, 2.7, 1.7, [("paragraf", num), ("paragraf", label)], size=16,
                         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, name=f"sayi{i}", space_after=2)
        r0 = tb.text_frame.paragraphs[0].runs[0]; r0.font.size = Pt(32 if len(num) <= 6 else 26); r0.font.bold = True
    if rest:
        add_textbox(slide, 0.84, 6.0, 11.65, 0.8, [("paragraf", rest[0])], size=18, align=PP_ALIGN.CENTER, name="govde")

def build_tablo(slide, sl, meta):
    """Satırlar '|' ile ayrılmış hücreler; ilk satır başlık."""
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    rows = [[c.strip() for c in t.split("|")] for g in sl["paralar"] for (_, t) in g if "|" in t]
    notes = [t for g in sl["paralar"] for (_, t) in g if "|" not in t]
    if len(rows) < 2:
        warn(f"'{sl['baslik']}': tablo için en az başlık + 1 satır gerekir ('a | b | c')."); rows = rows or [["[ÖĞRENCİ TAMAMLAYACAK: tablo]"]]
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    y = body_top(sl); avail = BODY_BOTTOM - y - (0.7 if notes else 0)
    size = sl["punto"] or deck_size("tablo", 18 if len(rows) <= 6 else 16 if len(rows) <= 9 else 14, sl["baslik"])
    if len(rows) > 12: warn(f"'{sl['baslik']}': {len(rows)} satır; tabloyu bölün.")
    rh = min(0.6, avail / len(rows))
    gf = slide.shapes.add_table(len(rows), ncol, Inches(BODY_X), Inches(y), Inches(BODY_W), Inches(rh * len(rows)))
    set_name(gf, "tablo")
    tbl = gf.table
    # stil: düz (No Style, No Grid), dolguları biz veririz
    tblPr = tbl._tbl.tblPr
    for a in ("firstRow", "bandRow"): tblPr.set(a, "0")
    sid = tblPr.find(qn("a:tableStyleId"))
    if sid is None: sid = etree.SubElement(tblPr, qn("a:tableStyleId"))
    sid.text = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"
    for ri, r in enumerate(rows):
        tbl.rows[ri].height = Inches(rh)
        for ci, val in enumerate(r):
            cell = tbl.cell(ri, ci)
            cell.fill.solid(); cell.fill.fore_color.rgb = NAVY if ri == 0 else (LIGHT if ri % 2 == 0 else RGBColor(0xFF, 0xFF, 0xFF))
            cell.margin_left = cell.margin_right = Inches(0.1); cell.margin_top = cell.margin_bottom = Inches(0.04)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame; tf.word_wrap = True
            para = tf.paragraphs[0]
            for rr in list(para.runs): rr._r.getparent().remove(rr._r)
            run = para.add_run(); run.text = val
            style_run(run, size=size, bold=(ri == 0) or None, color=RGBColor(0xFF, 0xFF, 0xFF) if ri == 0 else NAVY)
            para.alignment = PP_ALIGN.LEFT if ci == 0 else PP_ALIGN.CENTER
            # alt kenar çizgisi
            tcPr = cell._tc.get_or_add_tcPr()
            lnB = etree.SubElement(tcPr, qn("a:lnB")); lnB.set("w", "9525")
            sf = etree.SubElement(lnB, qn("a:solidFill")); c = etree.SubElement(sf, qn("a:srgbClr")); c.set("val", "BFC5CE")
    if notes:
        add_textbox(slide, BODY_X, y + rh * len(rows) + 0.12, BODY_W, 0.6, [("paragraf", notes[0])], size=16, color=GREY, name="tablo_not")

def build_karsilastirma(slide, sl, meta):
    """İki (en çok üç) blok yan yana: başlık şeridi + maddeler."""
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    bl = sl["bloklar"][:3]
    if len(bl) < 2:
        warn(f"'{sl['baslik']}': karşılaştırma için '### Sol' ve '### Sağ' iki blok gerekir."); bl = (bl + [{"baslik": "[ÖĞRENCİ TAMAMLAYACAK]", "items": []}] * 2)[:2]
    y = body_top(sl); h = BODY_BOTTOM - y; gap = 0.3; w = (BODY_W - gap * (len(bl) - 1)) / len(bl)
    colors = [NAVY, BRONZE, STEEL]
    for i, b in enumerate(bl):
        x = BODY_X + i * (w + gap)
        head = add_box(slide, x, y, w, 0.55, fill=colors[i], line=None, name=f"karsi{i+1}_baslik")
        shape_text(head, [("paragraf", b["baslik"])], 18, color=RGBColor(0xFF, 0xFF, 0xFF), align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, bold_first=True)
        body = add_box(slide, x, y + 0.55, w, h - 0.55, fill=RGBColor(0xFF, 0xFF, 0xFF), line=LINE, name=f"karsi{i+1}")
        items = b["items"] or [("paragraf", "[ÖĞRENCİ TAMAMLAYACAK]")]
        size = sl["punto"] or deck_size("govde", auto_size([items], w - 0.3, h - 0.9, max_size=22), sl["baslik"])
        shape_text(body, items, size, align=PP_ALIGN.LEFT, margin=0.15)
        body.text_frame.margin_top = Inches(0.15)

def build_kartlar(slide, sl, meta):
    """2–4 kart yan yana: renkli başlık + gövde."""
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    bl = sl["bloklar"]
    if not 2 <= len(bl) <= 4:
        warn(f"'{sl['baslik']}': kartlar için 2–4 '###' blok gerekir ({len(bl)} var)."); bl = (bl + [{"baslik": "[ÖĞRENCİ TAMAMLAYACAK]", "items": []}] * 2)[:4]
    y = body_top(sl); gap = 0.25; w = (BODY_W - gap * (len(bl) - 1)) / len(bl)
    need = max(estimate_lines(b["items"] or [("p", "x")], 20, w - 0.3) * 20 * 1.3 / 72 + 1.2 for b in bl)
    h = min(BODY_BOTTOM - y, max(2.8, need))
    colors = [NAVY, BRONZE, STEEL, NAVY]
    for i, b in enumerate(bl):
        x = BODY_X + i * (w + gap)
        head = add_box(slide, x, y, w, 0.5, fill=colors[i], line=None, name=f"kart{i+1}_baslik")
        hs = 16 if (w < 3 and len(b["baslik"]) > 14) else 18
        shape_text(head, [("paragraf", b["baslik"])], hs, color=RGBColor(0xFF, 0xFF, 0xFF), align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, bold_first=True)
        body = add_box(slide, x, y + 0.5, w, h - 0.5, fill=RGBColor(0xFF, 0xFF, 0xFF), line=LINE, name=f"kart{i+1}")
        items = b["items"] or [("paragraf", "[ÖĞRENCİ TAMAMLAYACAK]")]
        size = sl["punto"] or deck_size("govde", auto_size([items], w - 0.3, h - 0.9, max_size=20), sl["baslik"])
        shape_text(body, items, size, align=PP_ALIGN.LEFT, margin=0.15); body.text_frame.margin_top = Inches(0.12)
    rest = [t for g in sl["paralar"] for (_, t) in g]
    if rest:
        add_textbox(slide, BODY_X, y + h + 0.1, BODY_W, 0.6, [("paragraf", rest[0])], size=18, color=NAVY, align=PP_ALIGN.CENTER, name="govde")

def build_surec(slide, sl, meta):
    """Numaralı adımlar bir sırada, aralarında ok. Bloklar varsa kutu başlığı + maddeler; yoksa her madde bir adım."""
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    steps = blocks_or_items(sl)
    if len(steps) > 6:
        warn(f"'{sl['baslik']}': {len(steps)} adım; en çok 6, süreci bölün."); steps = steps[:6]
    if len(steps) < 2:
        warn(f"'{sl['baslik']}': süreç için en az 2 adım gerekir."); steps = (steps + [{"baslik": "", "items": [("paragraf", "[ÖĞRENCİ TAMAMLAYACAK]")]}] * 2)[:2]
    n = len(steps); y = body_top(sl); gap = 0.45; w = (BODY_W - gap * (n - 1)) / n
    h = min(BODY_BOTTOM - y - 0.5, 3.6 if n <= 4 else 4.2)
    y0 = y + 0.45
    for i, st in enumerate(steps):
        x = BODY_X + i * (w + gap)
        box = add_box(slide, x, y0, w, h, fill=RGBColor(0xFF, 0xFF, 0xFF), line=NAVY, name=f"adim{i+1}", rounded=True)
        items = ([("paragraf", st["baslik"])] if st["baslik"] else []) + [("paragraf", t) if k == "madde" and st["baslik"] == "" else (k, t) for k, t in st["items"]]
        size = sl["punto"] or deck_size("adim", auto_size([items], w - 0.3, h - 0.6, base=16, max_size=20), sl["baslik"])
        shape_text(box, items, size, align=PP_ALIGN.CENTER if not st["baslik"] else PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE, bold_first=bool(st["baslik"]), margin=0.14)
        box.text_frame.margin_top = Inches(0.35)
        num = slide.shapes.add_shape(9, Inches(x + w / 2 - 0.26), Inches(y0 - 0.3), Inches(0.52), Inches(0.52))  # oval, kutunun üstünde
        num.fill.solid(); num.fill.fore_color.rgb = BRONZE; num.line.fill.background(); num.shadow.inherit = False; set_name(num, f"adim{i+1}_no")
        shape_text(num, [("paragraf", str(i + 1))], 16, color=RGBColor(0xFF, 0xFF, 0xFF), align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, bold_first=True, margin=0)
        if i < n - 1:
            add_arrow(slide, x + w + 0.04, y0 + h / 2, x + w + gap - 0.04, y0 + h / 2, name=f"ok{i+1}")
    rest = [t for g in sl["paralar"] for (_, t) in g] if sl["bloklar"] else []
    if rest:
        add_textbox(slide, BODY_X, y0 + h + 0.15, BODY_W, 0.6, [("paragraf", rest[0])], size=18, color=NAVY, align=PP_ALIGN.CENTER, name="govde")

def build_zaman(slide, sl, meta):
    """Yatay zaman çizelgesi: 'tarih | olay' maddeleri, en çok 6; etiketler üst/alt dönüşümlü."""
    lor = find_shape(slide, lambda s: text_of(s).startswith("Lorem"))
    if lor: remove_shape(lor)
    ev = [[c.strip() for c in t.split("|", 1)] for g in sl["paralar"] for (_, t) in g if "|" in t]
    rest = [t for g in sl["paralar"] for (_, t) in g if "|" not in t]
    if len(ev) < 2:
        warn(f"'{sl['baslik']}': zaman çizelgesi için en az 2 'tarih | olay' satırı gerekir."); ev = (ev + [["?", "[ÖĞRENCİ TAMAMLAYACAK]"]] * 2)[:2]
    if len(ev) > 6: warn(f"'{sl['baslik']}': {len(ev)} olay; en çok 6."); ev = ev[:6]
    n = len(ev); y = body_top(sl); mid = y + (BODY_BOTTOM - y) / 2 - 0.2
    x0, x1 = BODY_X + 1.1, BODY_X + BODY_W - 1.1
    line = slide.shapes.add_connector(1, Inches(x0 - 0.3), Inches(mid), Inches(x1 + 0.3), Inches(mid))
    line.line.color.rgb = NAVY; line.line.width = Pt(2); set_name(line, "zaman_cizgi")
    step = (x1 - x0) / (n - 1) if n > 1 else 0
    lw = min(3.2, step * 1.9 if n > 1 else 3.2)
    for i, (tarih, olay) in enumerate(ev):
        cx = x0 + i * step
        dot = slide.shapes.add_shape(9, Inches(cx - 0.14), Inches(mid - 0.14), Inches(0.28), Inches(0.28))
        dot.fill.solid(); dot.fill.fore_color.rgb = BRONZE if i % 2 else NAVY; dot.line.fill.background(); dot.shadow.inherit = False; set_name(dot, f"zaman{i+1}_nokta")
        up = (i % 2 == 0)
        ty = mid - 0.45 - 1.5 if up else mid + 0.45
        tb = add_textbox(slide, cx - lw / 2, ty, lw, 1.5, [("paragraf", tarih), ("paragraf", olay)], size=16, color=NAVY,
                         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM if up else MSO_ANCHOR.TOP, name=f"zaman{i+1}", bold_first=True, space_after=2)
        tb.text_frame.paragraphs[0].runs[0].font.size = Pt(18)
    if rest:
        add_textbox(slide, BODY_X, BODY_BOTTOM - 0.6, BODY_W, 0.55, [("paragraf", rest[0])], size=16, color=GREY, align=PP_ALIGN.CENTER, name="zaman_not")

def build_tesekkur(slide, sl, meta):
    t = find_shape(slide, lambda s: text_of(s).startswith("LOREM IPSUM"))
    d = find_shape(slide, lambda s: "??.??" in text_of(s))
    title = meta.get("baslik", "")
    if t:
        run = t.text_frame.paragraphs[0].runs[0]
        for r in list(t.text_frame.paragraphs[0].runs)[1:]: r._r.getparent().remove(r._r)
        run.text = title; run.font.size = Pt(40 if len(title) <= 28 else 32 if len(title) <= 50 else 26)
        t.left, t.width = Inches(1.0), Inches(11.33); t.top, t.height = Inches(2.6), Inches(1.7)
        t.text_frame.word_wrap = True; t.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        set_name(t, "kapanis_baslik")
    if d:
        d.text_frame.paragraphs[0].runs[0].text = meta.get("tarih", "")
        for r in list(d.text_frame.paragraphs[0].runs)[1:]: r._r.getparent().remove(r._r)
        d.top = Inches(6.45); set_name(d, "kapanis_tarih")
    lines = [t for g in sl["paralar"] for (_, t) in g]
    if meta.get("yz_satiri"):
        lines.append(meta["yz_satiri"])
    if lines:
        add_textbox(slide, 1.0, 5.5, 11.33, 1.0, [("paragraf", l) for l in lines], size=16, color=NAVY,
                    align=PP_ALIGN.CENTER, name="tesekkur_satirlar", space_after=2)

# ---------------- ana ----------------

def build_deck(sablon, meta, slides, base_dir, dil, footer):
    """Desteyi kurar; (prs, anim, salt metin slaytları) döner. DECK boşsa yalnız punto ölçümü için çalışır."""
    prs = Presentation(sablon)
    T = list(prs.slides)
    if len(T) < 7:
        sys.exit("Şablonda 7 örnek slayt bekleniyordu.")
    total = len(slides) + 1
    anim = {}; metin_yalniz = []
    # kapak
    kapak = duplicate_slide(prs, T[0]); build_kapak(kapak, meta)
    # içerik
    for n, sl in enumerate(slides, 2):
        s = duplicate_slide(prs, T[TEMPLATE_INDEX[sl["tur"]]])
        tur = sl["tur"]
        if tur != "tesekkur":
            set_title(s, sl["baslik"]); set_footer(s, footer)
            if tur not in ("icindekiler", "kaynaklar"): add_message(s, sl)
        if tur == "metin": build_metin(s, sl, meta)
        elif tur == "tablo": build_tablo(s, sl, meta)
        elif tur == "karsilastirma": build_karsilastirma(s, sl, meta)
        elif tur == "kartlar": build_kartlar(s, sl, meta)
        elif tur == "surec": build_surec(s, sl, meta)
        elif tur == "zaman": build_zaman(s, sl, meta)
        elif tur == "icindekiler": build_icindekiler(s, sl, meta)
        elif tur == "kaynaklar": build_kaynaklar(s, sl, meta, sl["_chunk"])
        elif tur == "gorsel": build_gorsel(s, sl, meta, base_dir)
        elif tur == "metin_gorsel": build_metin_gorsel(s, sl, meta, base_dir)
        elif tur == "uc_gorsel": build_uc_gorsel(s, sl, meta, base_dir)
        elif tur == "sayilar": build_sayilar(s, sl, meta)
        elif tur == "tesekkur": build_tesekkur(s, sl, meta)
        if tur != "tesekkur" and meta.get("sayfa_no", "evet").lower() not in ("hayır", "hayir", "no", "false"):
            add_page_number(s, n, total)
        if sl["notlar"]:
            s.notes_slide.notes_text_frame.text = "\n".join(sl["notlar"])
        # madde sayısı uyarısı
        for g in (sl["paralar"] if tur not in ("zaman", "tablo") else []) + [b["items"] for b in sl["bloklar"]]:
            if sum(1 for k, _ in g if k == "madde") > 5:
                warn(f"'{sl['baslik']}': 5'ten çok madde; slaydı bölün.")
        if tur == "metin" and not sl["gorseller"] and not sl["denklemler"]:
            metin_yalniz.append(sl["baslik"])
        # animasyon
        groups = [g for g in sl["paralar"] if g]
        katman = sl.get("_katman", 1)
        if len(groups) > 1 and tur in ("metin", "metin_gorsel") and not sl["denklemler"]:
            steps = []
            for i in range(2, len(groups) + 1):
                step = [{"name": f"govde{i}"}]
                if katman >= i: step.append({"name": f"gorsel{i}"})
                steps.append(step)
            anim[str(n)] = steps
            if katman > 1 and katman != len(groups):
                warn(f"'{sl['baslik']}': {katman} görsel katmanı, {len(groups)} tıklama grubu; sayılar eşit olmalı.")
        elif katman > 1 and tur in ("gorsel", "metin_gorsel"):
            anim[str(n)] = [[{"name": f"gorsel{i}"}] for i in range(2, katman + 1)]
        if sl["animasyon"] and tur == "uc_gorsel":
            anim[str(n)] = [[{"name": f"gorsel{i}"}, {"name": f"altyazi{i}"}] for i in range(1, 4)]
        if sl["animasyon"] and tur == "sayilar":
            anim[str(n)] = [[{"name": f"sayi{i}"}] for i in range(1, 4)]
        if len(groups) > 3:
            warn(f"'{sl['baslik']}': en çok 3 tıklama grubu desteklenir.")
    # şablon slaytlarını sil
    for _ in range(7):
        delete_slide(prs, 0)
    # Düzenler: başlık şeridini 2 inç genişlet; Teşekkür düzenindeki "Sunumu Hazırlayan" → altbilgi,
    # "Teşekkürler" → İngilizce destede "Acknowledgements"
    for lay in prs.slide_layouts:
        for sh in lay.shapes:
            if sh.name.startswith("Serbest Form") and abs(sh.left / 914400 - 8.17) < 0.2:
                sh.left -= Inches(2.0); sh.width += Inches(2.0)
            if text_of(sh).strip().lower() == "sunumu hazırlayan" and footer:
                sh.text_frame.paragraphs[0].runs[0].text = footer
                for r in list(sh.text_frame.paragraphs[0].runs)[1:]: r._r.getparent().remove(r._r)
            if text_of(sh).strip() == "Teşekkürler" and dil == "en":
                sh.text_frame.paragraphs[0].runs[0].text = "Acknowledgements"
                for r in list(sh.text_frame.paragraphs[0].runs)[1:]: r._r.getparent().remove(r._r)
                cx = sh.left + sh.width // 2                          # kutu dar (2 inç); ortalayıp genişlet
                sh.width = Inches(6.0); sh.left = cx - sh.width // 2
                sh.text_frame.word_wrap = False
                sh.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    return prs, anim, metin_yalniz

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sunum_md")
    ap.add_argument("--sablon", required=True)
    ap.add_argument("--cikti", required=True)
    a = ap.parse_args()
    base_dir = os.path.dirname(os.path.abspath(a.sunum_md))

    meta, slides = parse_md(a.sunum_md)
    for k in ("baslik", "hazirlayan", "tarih"):
        if k not in meta: warn(f"Ön bilgide '{k}' yok.")
    dil = meta.get("dil", "tr").strip().lower()
    if dil not in ("tr", "en"): warn(f"Ön bilgide 'dil: {dil}' tanınmadı; tr kabul edildi."); dil = "tr"
    name = meta.get("hazirlayan", "")
    footer = " · ".join(v for v in (name, meta.get("eposta", "")) if v)   # altbilgi: ad + iletişim
    if not meta.get("eposta"): warn("Ön bilgide 'eposta' yok; altbilgide iletişim bilgisi olmalı.")

    # kaynaklar bölme
    expanded = []
    for sl in slides:
        if sl["tur"] == "kaynaklar":
            refs = [t for g in sl["paralar"] for (_, t) in g]
            chunks = [refs[i:i + 7] for i in range(0, max(1, len(refs)), 7)] or [[]]
            for ci, ch in enumerate(chunks):
                s2 = dict(sl); s2["_chunk"] = ch
                if ci > 0: s2["baslik"] = sl["baslik"] + (" (cont.)" if dil == "en" else " (devam)")
                expanded.append(s2)
        else:
            expanded.append(sl)
    slides = expanded
    has_tesekkur = any(s["tur"] == "tesekkur" for s in slides)
    has_kaynak = any(s["tur"] == "kaynaklar" for s in slides)
    if not has_tesekkur: warn("Teşekkürler slaydı yok; dersin kuralı gereği zorunlu.")
    if not has_kaynak: warn("Kaynaklar slaydı yok; dersin kuralı gereği zorunlu.")
    if not any(s["tur"] == "icindekiler" for s in slides): warn("İçindekiler slaydı yok.")
    icerik = [s for s in slides if s["tur"] not in ("icindekiler", "kaynaklar", "tesekkur")]
    if not (15 <= len(icerik) <= 20):
        warn(f"İçerik slaydı sayısı {len(icerik)}; 30 dakika için 15–20 önerilir.")

    total = len(slides) + 1
    # 1. tur: her metin alanına sığan puntoyu ölç; 2. tur: her rolü destedeki en küçük ölçüyle kur
    n_warn = len(WARN)
    build_deck(a.sablon, meta, slides, base_dir, dil, footer)
    del WARN[n_warn:]
    belirleyen = {}
    for role, fits in FITS.items():
        DECK[role], belirleyen[role] = min(fits)
    if DECK.get("baslik", 28) < 28:
        warn(f"Bütün slayt başlıkları {DECK['baslik']} punto oldu; bunu en uzun başlık belirledi: '{belirleyen['baslik'][:50]}'. Kısaltırsanız bütün başlıklar büyür.")
    for sl in slides:
        if sl["punto"]:
            warn(f"'{sl['baslik']}': 'punto: {sl['punto']}' bu slaydı destenin geri kalanından farklı puntoya çekiyor; tutarlılık için kaldırın ya da slaydı bölün.")
    prs, anim, metin_yalniz = build_deck(a.sablon, meta, slides, base_dir, dil, footer)
    if icerik and len(metin_yalniz) > len(icerik) / 3:
        warn(f"{len(icerik)} içerik slaydının {len(metin_yalniz)} tanesi salt madde listesi (üst sınır üçte bir). Tablo, süreç, karşılaştırma, kart ya da görsel kalıbına çevirin: " + "; ".join(metin_yalniz[:6]))
    prs.save(a.cikti)
    print(f"Yazıldı: {a.cikti}  ({total} slayt; {len(icerik)} içerik slaydı)")
    ad = {"baslik": "başlık", "govde": "gövde", "adim": "süreç kutusu", "tablo": "tablo"}
    print("Punto (deste geneli): " + ", ".join(f"{ad[r]} {DECK[r]}" for r in ad if r in DECK))
    if DECK.get("govde", 24) < 24:
        print(f"  Gövde puntosunu en dolu slayt belirledi: '{belirleyen['govde'][:50]}'; sadeleştirilirse bütün gövde büyüyebilir.")
    if anim:
        ap_path = os.path.join(os.path.dirname(os.path.abspath(a.cikti)), "anim.json")
        json.dump(anim, open(ap_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"Tıklama senaryosu yazıldı: {ap_path}  → python3 scripts/anim.py \"{a.cikti}\" \"{ap_path}\"")
    for w in dict.fromkeys(WARN):     # aynı uyarıyı bir kez yaz
        print("UYARI:", w)

if __name__ == "__main__":
    main()
