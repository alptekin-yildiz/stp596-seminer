#!/usr/bin/env python3
"""Animasyon enjektörü: anim.json'daki tıklama senaryolarını slayt XML'ine <p:timing> olarak yazar.

anim.json biçimi:
{ "<slayt sırası, 1'den>": [            # slayt
     [ {"name": "...", "fx": "fade", "dir": "in"}, {"name": "...", "fx": "fade", "dir": "in"} ],  # 1. tıklama: ilk öğe tıklamayla, kalanlar "önceki ile"
     ...
  ] }
fx: fade (Soluklaş) · appear (Görün/Kaybol) · wipe (Sil, aşağı) · fly (Uçarak gir, alttan) · rise (Yukarı doğru uç)
dir: in | out
"auto": true  → ilk adım slayt açılır açılmaz çalışır (tıklamasız)
Şekil adları pptxgenjs objectName ile verilir; aynı ad birden çok şekle verilmişse hepsi hedeflenir.
"""
import json, re, sys, zipfile, shutil, os, tempfile

def effect_xml(ids, spid, fx, direction, node_type):
    i = ids
    def nid():
        i[0] += 1
        return i[0]
    cls = "entr" if direction == "in" else "exit"
    vis = "visible" if direction == "in" else "hidden"
    preset = {"fade": 10, "appear": 1, "wipe": 22, "fly": 2, "rise": 42}[fx]
    subtype = {"fade": 0, "appear": 0, "wipe": 4, "fly": 4, "rise": 0}[fx]
    grp = ' grpId="0"' if direction == "in" else ' grpId="1"'
    top = nid()
    parts = [f'<p:par><p:cTn id="{top}" presetID="{preset}" presetClass="{cls}" presetSubtype="{subtype}" fill="hold"{grp} nodeType="{node_type}">'
             f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>']
    setid = nid()
    set_xml = (f'<p:set><p:cBhvr><p:cTn id="{setid}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
               f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
               f'<p:to><p:strVal val="{vis}"/></p:to></p:set>')
    if fx == "appear":
        parts.append(set_xml)
    elif fx == "fade":
        if direction == "in":
            parts.append(set_xml)
            parts.append(f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{nid()}" dur="500"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>')
        else:
            parts.append(f'<p:animEffect transition="out" filter="fade"><p:cBhvr><p:cTn id="{nid()}" dur="500"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>')
            parts.append(set_xml.replace('<p:cond delay="0"/></p:stCondLst></p:cTn>', '<p:cond delay="499"/></p:stCondLst></p:cTn>'))
    elif fx == "wipe":
        parts.append(set_xml)
        parts.append(f'<p:animEffect transition="in" filter="wipe(down)"><p:cBhvr><p:cTn id="{nid()}" dur="500"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>')
    elif fx == "fly":
        parts.append(set_xml)
        parts.append(f'<p:anim calcmode="lin" valueType="num"><p:cBhvr additive="base"><p:cTn id="{nid()}" dur="500" fill="hold"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>ppt_x</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst><p:tav tm="0"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav><p:tav tm="100000"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav></p:tavLst></p:anim>')
        parts.append(f'<p:anim calcmode="lin" valueType="num"><p:cBhvr additive="base"><p:cTn id="{nid()}" dur="500" fill="hold"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>ppt_y</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst><p:tav tm="0"><p:val><p:strVal val="1+#ppt_h/2"/></p:val></p:tav><p:tav tm="100000"><p:val><p:strVal val="#ppt_y"/></p:val></p:tav></p:tavLst></p:anim>')
    elif fx == "rise":
        parts.append(set_xml)
        parts.append(f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{nid()}" dur="1000"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>')
        parts.append(f'<p:anim calcmode="lin" valueType="num"><p:cBhvr><p:cTn id="{nid()}" dur="1000" fill="hold"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>ppt_x</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst><p:tav tm="0"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav><p:tav tm="100000"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav></p:tavLst></p:anim>')
        parts.append(f'<p:anim calcmode="lin" valueType="num"><p:cBhvr><p:cTn id="{nid()}" dur="1000" fill="hold"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>ppt_y</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst><p:tav tm="0"><p:val><p:strVal val="#ppt_y+.1"/></p:val></p:tav><p:tav tm="100000"><p:val><p:strVal val="#ppt_y"/></p:val></p:tav></p:tavLst></p:anim>')
    parts.append('</p:childTnLst></p:cTn></p:par>')
    return ''.join(parts)

def build_timing(steps, name_to_ids, text_ids, auto_first=False):
    ids = [2]  # 1 tmRoot, 2 mainSeq
    out = ['<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
           '<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>']
    animated = []
    for si, step in enumerate(steps):
        ids[0] += 1; click_id = ids[0]
        cond = '<p:cond delay="indefinite"/>'
        if si == 0 and auto_first:
            cond += '<p:cond evt="onBegin" delay="0"><p:tn val="2"/></p:cond>'
        out.append(f'<p:par><p:cTn id="{click_id}" fill="hold"><p:stCondLst>{cond}</p:stCondLst><p:childTnLst>')
        ids[0] += 1; grp_id = ids[0]
        out.append(f'<p:par><p:cTn id="{grp_id}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>')
        first = True
        for eff in step:
            targets = name_to_ids.get(eff["name"])
            if not targets:
                raise SystemExit(f'HATA: "{eff["name"]}" adlı şekil bulunamadı')
            for spid in targets:
                node = "clickEffect" if (first and not (si == 0 and auto_first)) else "withEffect"
                out.append(effect_xml(ids, spid, eff.get("fx", "fade"), eff.get("dir", "in"), node))
                first = False
                animated.append(spid)
        out.append('</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    out.append('</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
               '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
               '</p:childTnLst></p:cTn></p:par></p:tnLst>')
    bld = []
    seen = set()
    for spid in animated:
        if spid in text_ids and spid not in seen:
            seen.add(spid)
            bld.append(f'<p:bldP spid="{spid}" grpId="0"/>')
    if bld:
        out.append('<p:bldLst>' + ''.join(bld) + '</p:bldLst>')
    out.append('</p:timing>')
    return ''.join(out)

def main(pptx, spec_path):
    spec = json.load(open(spec_path))
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(pptx) as z:
        z.extractall(tmp)
    # presentation.xml slayt sırası → dosya adı
    pres = open(os.path.join(tmp, 'ppt/presentation.xml')).read()
    rels = open(os.path.join(tmp, 'ppt/_rels/presentation.xml.rels')).read()
    rid_to_target = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="(slides/[^"]+)"', rels))
    rid_to_target.update({a: b for b, a in re.findall(r'Target="(slides/[^"]+)"[^>]*Id="(rId\d+)"', rels)})
    order = re.findall(r'<p:sldId [^>]*r:id="(rId\d+)"', pres)
    count = 0
    for key, cfg in spec.items():
        idx = int(key)
        target = rid_to_target[order[idx - 1]]
        path = os.path.join(tmp, 'ppt', target)
        xml = open(path, encoding='utf8').read()
        steps = cfg["steps"] if isinstance(cfg, dict) else cfg
        auto = cfg.get("auto", False) if isinstance(cfg, dict) else False
        name_to_ids = {}
        text_ids = set()
        for m in re.finditer(r'<p:(sp|pic|grpSp|graphicFrame|cxnSp)>.*?<p:cNvPr id="(\d+)" name="([^"]*)"', xml, re.S):
            name_to_ids.setdefault(m.group(3), []).append(m.group(2))
        for m in re.finditer(r'<p:sp>(.*?)</p:sp>', xml, re.S):
            body = m.group(1)
            idm = re.search(r'<p:cNvPr id="(\d+)"', body)
            if idm and '<p:txBody>' in body and re.search(r'<a:t>[^<]+</a:t>', body):
                text_ids.add(idm.group(1))
        timing = build_timing(steps, name_to_ids, text_ids, auto)
        xml = re.sub(r'<p:timing>.*?</p:timing>', '', xml, flags=re.S)
        # <p:timing> <p:clrMapOvr>'dan sonra, </p:sld>'den önce
        if '</p:clrMapOvr>' in xml:
            xml = xml.replace('</p:clrMapOvr>', '</p:clrMapOvr>' + timing, 1)
        else:
            xml = xml.replace('</p:sld>', timing + '</p:sld>')
        open(path, 'w', encoding='utf8').write(xml)
        count += 1
    out = pptx
    os.remove(out)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f)
                arc = os.path.relpath(full, tmp)
                if arc == '[Content_Types].xml':
                    z.write(full, arc)
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f)
                arc = os.path.relpath(full, tmp)
                if arc != '[Content_Types].xml':
                    z.write(full, arc)
    shutil.rmtree(tmp)
    print(f'{count} slayta animasyon yazıldı → {out}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
