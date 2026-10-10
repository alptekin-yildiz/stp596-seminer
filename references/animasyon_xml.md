# pptxgenjs ile üretilen desteye PowerPoint animasyonu ekleme (ajan için yönerge)

Bu metin, bir .pptx dosyasını kodla üreten bir ajana tıklamalı animasyonları nasıl ekleyeceğini anlatır. Yöntem STP 596 destelerinde (01_etik.pptx, 02_retorik.pptx; 50'ye yakın animasyonlu slayt) denendi ve PowerPoint'te sorunsuz çalışıyor.

## 1. Temel gerçek

pptxgenjs de python-pptx de animasyon yazamaz. PowerPoint animasyonları her slaydın XML'inde (`ppt/slides/slideN.xml`) `<p:timing>` bloğunda durur. Bu yüzden iş iki adımdır:

1. Desteyi normal yoldan üret (pptxgenjs). Animasyon alacak **her şekle benzersiz bir ad ver** (`objectName: "maddeler"` gibi). Bu ad XML'e `<p:cNvPr id="7" name="maddeler"/>` olarak geçer.
2. Üretimden sonra .pptx'i zip olarak aç, ilgili slaytların XML'ine `<p:timing>` bloğunu yaz, yeniden zip'le.

Hazır betik: `scripts/anim.py` (yaklaşık 150 satır, yalnız standart kütüphane). Kopyalayıp kullanabilirsin:

```bash
python3 anim.py deste.pptx anim.json
```

## 2. Tıklama senaryosu dosyası (anim.json)

Anahtar slaydın **dosya sırası** (1'den başlar), değer tıklama adımlarının listesi. Her adım bir liste; adımın ilk öğesi tıklamayla, kalanlar "öncekiyle birlikte" çalışır.

```json
{
  "6": [
    [ {"name": "maddeler"} ],
    [ {"name": "sentez"}, {"name": "sentez_zemin"}, {"name": "sentez_bar"} ]
  ],
  "17": { "auto": true, "steps": [
    [ {"name": "anlati"} ],
    [ {"name": "eski_kutu", "dir": "out"}, {"name": "yeni_kutu", "fx": "wipe"} ]
  ]}
}
```

- `fx`: `fade` (varsayılan), `appear`, `wipe`, `fly`, `rise`. `dir`: `in` (varsayılan) ya da `out` (çıkış).
- `auto: true` → ilk adım slayt açılır açılmaz çalışır.
- Aynı ad birden çok şekle verildiyse hepsi hedeflenir (kutu + çubuk + metin gibi grupları tek adla toplamak için kullanışlı).
- Üretici betik bu JSON'u kendisi yazarsa (slayt kurarken `anims[fileIdx] = [...]` diye biriktirip sonda dosyaya dökerek) slayt sırası kayması olmaz.

## 3. XML iskeleti

Tek tıklamada iki şeklin soluklaşarak girdiği en küçük örnek. `spid` değerleri şeklin `<p:cNvPr id="...">` değeridir; `id` değerleri (cTn) slayt içinde benzersiz olmalı, 1 ve 2 kök düğümlere ayrılır.

```xml
<p:timing>
  <p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>
    <p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>

      <!-- 1. tıklama -->
      <p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>
        <p:par><p:cTn id="4" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>

          <!-- ilk efekt: tıklamayla -->
          <p:par><p:cTn id="5" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="clickEffect">
            <p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>
              <p:set><p:cBhvr><p:cTn id="6" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>
                <p:tgtEl><p:spTgt spid="7"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>
                <p:to><p:strVal val="visible"/></p:to></p:set>
              <p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="8" dur="500"/><p:tgtEl><p:spTgt spid="7"/></p:tgtEl></p:cBhvr></p:animEffect>
            </p:childTnLst></p:cTn></p:par>

          <!-- ikinci efekt: öncekiyle birlikte -->
          <p:par><p:cTn id="9" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="withEffect">
            <p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>
              <p:set><p:cBhvr><p:cTn id="10" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>
                <p:tgtEl><p:spTgt spid="12"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>
                <p:to><p:strVal val="visible"/></p:to></p:set>
              <p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="11" dur="500"/><p:tgtEl><p:spTgt spid="12"/></p:tgtEl></p:cBhvr></p:animEffect>
            </p:childTnLst></p:cTn></p:par>

        </p:childTnLst></p:cTn></p:par>
      </p:childTnLst></p:cTn></p:par>
      <!-- sonraki tıklamalar: aynı kalıp, yeni id'lerle -->

    </p:childTnLst></p:cTn>
    <p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>
    <p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>
  </p:childTnLst></p:cTn></p:par></p:tnLst>
  <p:bldLst><p:bldP spid="7" grpId="0"/><p:bldP spid="12" grpId="0"/></p:bldLst>
</p:timing>
```

Efekt kodları: `presetID` 10 = Soluklaş (fade), 1 = Görün (appear; yalnız `<p:set>` yeter, animEffect yok), 22 = Sil (wipe; `filter="wipe(down)"`, presetSubtype 4), 2 = Uçarak gir (fly; ppt_x / ppt_y üzerinde `<p:anim>`), 42 = Yukarı doğru uç (rise). Çıkış için `presetClass="exit"`, `grpId="1"`, `transition="out"` ve `<p:set>` değeri `hidden`; set düğümü solmanın bitişine (`delay="499"`) konur.

## 4. Kurallar ve tuzaklar

- **Yer:** `<p:timing>` bloğu `</p:clrMapOvr>` etiketinden hemen sonra, `</p:sld>` etiketinden önce gelir. Slaytta eski bir `<p:timing>` varsa önce silinir.
- **spid:** `<p:spTgt spid>` değeri şeklin `<p:cNvPr id>` değeriyle birebir aynı olmalı. Şekli adıyla bul: `<p:cNvPr id="(\d+)" name="(…)"`; `p:sp`, `p:pic`, `p:grpSp`, `p:cxnSp`, `p:graphicFrame` hepsi hedeflenebilir.
- **cTn id'leri** slayt içinde benzersiz ve kök düğümlerle çakışmayan sayılar olmalı; bir sayaçla üret.
- **Tıklama grubu:** Her tıklama bir `<p:par>` (koşul `delay="indefinite"`); içinde bir ara `<p:par>` (`delay="0"`); içinde efektler. Gruptaki ilk efekt `nodeType="clickEffect"`, kalanlar `withEffect`. Otomatik başlayan ilk adım için tıklama koşuluna `<p:cond evt="onBegin" delay="0"><p:tn val="2"/></p:cond>` eklenir ve ilk efekt de `withEffect` olur.
- **Giriş efektinde `<p:set style.visibility=visible` şart.** Bu set düğümü sayesinde PowerPoint şekli animasyon çalışana kadar gizler. Onsuz şekil baştan görünür, animasyon işe yaramaz.
- **`<p:bldLst>`:** Metin içeren her animasyonlu şekil için bir `<p:bldP spid grpId="0"/>` satırı ekle; yoksa PowerPoint bazı metinleri paragraf paragraf oynatmaya kalkabilir ya da dosyayı onarmak isteyebilir.
- **Zip'lerken** `[Content_Types].xml` ilk giriş olsun; `ZIP_DEFLATED` kullan; eski dosyayı silmeden üstüne yazma (silinmiş parçalar arşivde kalır).
- **Üretici betiğe dokunmadan** animasyon ekleyeceksen önce şekillerin adlarını kontrol et: pptxgenjs `objectName` verilmemiş şekillere "Text 0", "Shape 1" gibi adlar üretir ve aynı ad slaytta tekrar edebilir; ad bazlı hedefleme için adlar benzersiz olmalı.
- **Doğrulama:** Enjeksiyondan sonra dosyayı bir XML ayrıştırıcıyla aç (her slayt), sonra PowerPoint'te açıp Animasyon Bölmesi'ne bak. pptx becerisindeki `validate.py` de `<p:timing>` hatalarını yakalar.

## 5. Görsel kontrol (animasyon render edilemez)

LibreOffice ya da PDF dönüşümü animasyonu göstermez; slaydın son hâlini çizer, ki bu da tıklamayla gelecek her şeyi açıkta bırakır. Çözüm `storyboard.py` (bu skill'e dahil değil; STP 596 ders üretim klasöründe): anim.json'u okur, her tıklama durumu için henüz görünmemiş şekilleri XML'den çıkarıp slaydı ayrı ayrı çizer, bir ızgara görüntü üretir ("Slayt açılışı", "1. tıklama", …). Senaryoyu kullanıcıya göstermenin en güvenilir yolu budur.

```bash
python3 storyboard.py deste.pptx anim.json 8 tiklama_8.jpg
```

## 6. İş akışı özeti

1. Üretici betikte animasyon alacak her şekle `objectName` ver; slayt kurarken `anims[fileIdx]` listesini doldur; sonda `anim.json`'a yaz.
2. `node build.js deste.pptx` → `python3 anim.py deste.pptx anim.json` → `validate.py`.
3. `storyboard.py` ile tıklama föyünü çiz, kullanıcıya göster.
4. Kullanıcı PowerPoint'te animasyon eklerse, düzenlenmiş kopyadaki `<p:timing>` bloğundan tıklama gruplarını (clickEffect / withEffect sırası, spid → ad) okuyup anim.json'a geri taşı; böylece bir sonraki üretimde kaybolmaz.
