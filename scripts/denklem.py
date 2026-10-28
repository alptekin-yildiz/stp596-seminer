"""LaTeX denklemini Word ve PowerPoint'in düzenlenebilir denklem nesnesine (OMML) çevirir.

form_doldur.py ve deste_kur.py kullanır; tek başına çalıştırılmaz. Çeviriyi pandoc yapar (isteğe bağlı:
https://pandoc.org, macOS'ta 'brew install pandoc'). pandoc yoksa ya da denklem çevrilemezse None döner;
betikler o zaman yer tutucu yazar ve uyarır.
"""
import os, re, shutil, subprocess, tempfile, zipfile
from lxml import etree

M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
_CACHE = {}

def pandoc_var():
    return shutil.which("pandoc") is not None

def latex_to_omml(latex):
    """Tek denklem → m:oMath öğesi (lxml); çevrilemezse None."""
    if latex in _CACHE:
        return _CACHE[latex]
    omml = None
    if pandoc_var():
        with tempfile.TemporaryDirectory() as t:
            md, out = os.path.join(t, "d.md"), os.path.join(t, "d.docx")
            with open(md, "w", encoding="utf-8") as f:
                f.write(f"$${latex}$$\n")
            r = subprocess.run(["pandoc", md, "-o", out], capture_output=True, text=True)
            if r.returncode == 0:
                xml = zipfile.ZipFile(out).read("word/document.xml")
                found = etree.fromstring(xml).find(f".//{{{M}}}oMath")
                omml = found
    _CACHE[latex] = omml
    return omml

# ---- düz metin karşılığı: PowerPoint dışındaki programların gördüğü yedek ve son göz turu için ----

_SUP = dict(zip("0123456789+-−=()abcdefghijklmnoprstuvwxyzABDEGHIJKLMNOPRTUW",
               "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁᵂ"))
_SUB = dict(zip("0123456789+-−=()aehijklmnoprstuvx", "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ"))

def _script(text, table, mark):
    if text and all(c in table for c in text):
        return "".join(table[c] for c in text)
    return f"{mark}({text})"

def _group(text):
    return text if len(text) <= 1 or re.fullmatch(r"[\w.]+", text) else f"({text})"

def linear(el):
    """OMML öğesini okunur tek satırlık metne çevirir: (σa/4)((2/3)θ₀ − λ), ∫₀ᴿ, Σ."""
    tag = etree.QName(el).localname
    kids = lambda name: [c for c in el if etree.QName(c).localname == name]
    part = lambda name: "".join(linear(c) for c in kids(name))
    if tag == "t":
        return el.text or ""
    if tag in ("rPr", "fPr", "naryPr", "dPr", "sSubPr", "sSupPr", "sSubSupPr", "accPr", "radPr", "ctrlPr", "oMathParaPr", "funcPr", "limLowPr", "limUppPr", "barPr"):
        return ""
    if tag == "f":                      # kesir her zaman parantezli: (σa/4)
        return f"({_group(part('num'))}/{_group(part('den'))})"
    if tag == "sSup":
        return part("e") + _script(part("sup"), _SUP, "^")
    if tag == "sSub":
        return part("e") + _script(part("sub"), _SUB, "_")
    if tag == "sSubSup":
        return part("e") + _script(part("sub"), _SUB, "_") + _script(part("sup"), _SUP, "^")
    if tag == "nary":
        pr = el.find(f"{{{M}}}naryPr/{{{M}}}chr")
        sym = pr.get(f"{{{M}}}val") if pr is not None else "∫"
        return sym + _script(part("sub"), _SUB, "_") + _script(part("sup"), _SUP, "^") + " " + part("e")
    if tag == "d":
        pr = el.find(f"{{{M}}}dPr")
        beg = pr.find(f"{{{M}}}begChr") if pr is not None else None
        end = pr.find(f"{{{M}}}endChr") if pr is not None else None
        return (beg.get(f"{{{M}}}val") if beg is not None else "(") + ", ".join(linear(c) for c in kids("e")) + (end.get(f"{{{M}}}val") if end is not None else ")")
    if tag == "rad":
        return "√" + _group(part("e"))
    if tag == "acc":
        pr = el.find(f"{{{M}}}accPr/{{{M}}}chr")
        return part("e") + (pr.get(f"{{{M}}}val") if pr is not None else "̂")
    return "".join(linear(c) for c in el)

def linear_text(omml):
    t = linear(omml)
    t = re.sub(r"(?<=[^\s(^_=<>≤≥≈+−±])\s*([=<>≤≥≈+−])\s*", r" \1 ", t)   # ikili işleç: iki yanında boşluk; işaret değil
    return re.sub(r"\s{2,}", " ", t).strip()

# ---- PowerPoint: her m:r'ye DrawingML run özelliği (Cambria Math, punto) eklenir ----

def for_pptx(omml, size):
    el = etree.fromstring(etree.tostring(omml))
    for r in el.iter(f"{{{M}}}r"):
        sty = r.find(f"{{{M}}}rPr/{{{M}}}sty")
        rpr = etree.Element(f"{{{A}}}rPr", nsmap={"a": A})
        rpr.set("lang", "tr-TR"); rpr.set("sz", str(int(size * 100)))
        rpr.set("i", "0" if sty is not None and sty.get(f"{{{M}}}val") == "p" else "1")
        latin = etree.SubElement(rpr, f"{{{A}}}latin")
        latin.set("typeface", "Cambria Math"); latin.set("panose", "02040503050406030204")
        latin.set("pitchFamily", "18"); latin.set("charset", "0")
        mrpr = r.find(f"{{{M}}}rPr")
        r.insert(1 if mrpr is not None else 0, rpr)
    return el

def eq_height(latex, size):
    """Denklemin slayttaki yüksekliği (inç): kesir, integral, toplam iki satır sayılır."""
    tall = re.search(r"\\(frac|dfrac|int|iint|oint|sum|prod|sqrt|lim|begin)", latex)
    return (2.1 if tall else 1.3) * size / 72 + 0.12
