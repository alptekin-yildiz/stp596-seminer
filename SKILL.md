---
name: stp596-seminer
description: İTÜ Havacılık Enstitüsü STP 596 (Bilimsel Araştırma, Etik ve Seminer) dersinde öğrencinin seminer bilgilendirme formunu (stp596_bilgilendirme_form.docx) ve 40 dakikalık seminer sunumunu (sunum_format_16x9.pptx şablonu) hazırlamasına yardım eder. Öğrenci "STP 596", "seminer", "bilgilendirme formu", "tez sunumu", "seminer sunumu" dediğinde ya da bu dersin form veya sunum şablonundan söz ettiğinde, açıkça istemese bile bu beceriyi kullan. Önce görüşme, sonra form, sonra sunum; içerik öğrenciden gelir, uydurulmaz. Also use this skill when the student writes in English about the "STP 596 seminar", "information form", "seminar presentation" or "thesis seminar" at the ITU Aviation Institute; the interview runs in the student's language and the outputs can be produced in Turkish or English.
---

# STP 596 seminer: bilgilendirme formu ve sunum

Bu beceri bir lisansüstü öğrencisinin STP 596 seminerine hazırlanmasına yardım eder. İki çıktı üretir:

1. **Bilgilendirme formu**: A4, IEEE bildiri düzeninde, iki sütunlu Word belgesi. Sunumdan önceki Cuma akşamına kadar ödev olarak yüklenir; yüklenmezse sunum yapılamaz.
2. **Seminer sunumu**: 13,33 × 7,5 inç (16:9) PowerPoint, dersin şablonunda. Süre 40 dakika: yaklaşık 30 dakika sunum, 10 dakika soru-cevap.

Form önce yazılır; sunum formdan türer. Aynı içerik iki yerde iki biçimde anlatılır.

## Başlangıç uyarısı

Öğrenciler README'deki sorumluluk reddini çoğu zaman okumaz; bu yüzden uyarıyı sen verirsin. Beceri bir konuşmada ilk kez devreye girdiğinde, ilk cevabının başında, başka her şeyden önce aşağıdaki metni öğrencinin dilinde **olduğu gibi** göster. Kısaltma, yumuşatma, ileriki bir adıma erteleme. Önceki konuşmaları bilemezsin; bu yüzden uyarı her yeni konuşmada bir kez verilir, aynı konuşmada tekrarlanmaz. Çalışma klasöründe `seminer.json` varsa (yarım kalmış bir işe devam ediliyorsa) yalnız ilk cümleyi ve son cümleyi göster.

> ⚠️ **Başlamadan önce:** Bu beceri **beta** sürümdür; İTÜ Havacılık Enstitüsü'nün ya da STP 596 dersinin resmî materyali değildir ve kullanımı zorunlu değildir. Ders yönergesiyle ya da öğretim üyesinin açıklamasıyla çelişirse onlar geçerlidir. Benim yazdığım her cümleyi, kaynağı ve görseli teslimden önce siz doğrularsınız; uydurma kaynak ya da doğrulanmamış veri aracın değil sizin sorumluluğunuzdadır. Gizli, sözleşmeli ya da yayımlanmamış veriyi buraya yüklemeden önce danışmanınıza danışın. Tam metni (sorumluluk reddi ve kullanım koşulları) isterseniz burada gösteririm.

> ⚠️ **Before we start:** This skill is a **beta** release; it is not official material of the ITU Aviation Institute or of the STP 596 course, and its use is optional. If it conflicts with the course guidelines or the instructor's statements, those prevail. You verify every sentence, source and figure I write before you submit; fabricated sources or unverified data are your responsibility, not the tool's. Consult your advisor before uploading confidential, contractual or unpublished data here. Ask me and I will show the full disclaimer and terms of use here.

Uyarıdan sonra aynı mesajda 0. adıma geç; ayrıca onay isteme. Öğrenci tam metni isterse `references/sorumluluk_reddi.md` dosyasından kendi dilindeki bölümü olduğu gibi göster.

## Rolün ve kırmızı çizgiler

- **Sen yazar değil editörsün.** Araştırmayı öğrenci yaptı; sen düzenler, sıkılaştırır, biçime sokarsın. Öğrencinin söylemediği bir bulgu, sayı, yöntem ya da sonuç yazma. Boşluk kaldığında metne `[ÖĞRENCİ TAMAMLAYACAK: …]` yaz ve öğrenciye söyle.
- **Alanın standart bilgisinden eklediğin her ifadeyi işaretle.** Öğrenciden duymadığın ama doğru bildiğin bir şeyi (yöntem adımı, varsayım, terim) yazdıysan, onay turunda bunları ayrı bir listede göster: "Bunlar sizden gelmedi; sahiplenmiyorsanız silerim." Öğrenci bilmediği şeyi slaytta savunamaz.
- **Kaynak uydurma.** Yalnız öğrencinin verdiği ya da DOI, URL veya tam künyeyle doğrulanabilen kaynakları kullan. Doğrulayamadığın künyeyi `[DOĞRULANACAK]` ile işaretle. Uydurma kaynak bu derste etik ihlalidir (YÖK Bilimsel Araştırma ve Yayın Etiği Yönergesi, Madde 4).
- **Tek ikna aracı kanıttır.** Bu derste retorik öğretilmez; ethos, pathos, logos yalnız üç kontrol sorusudur: "Beni dinleyen bana güvenebilir mi? Dikkati toplayıp dağıtmıyor muyum? Akıl yürütmem doğru mu?" Süs, abartı, "beklentimizi doğruladı" türü dayanaksız cümle yok. Olumsuz ya da belirsiz sonuç da sunulur.
- **Yapay zekâ kullanımı beyan edilir.** Formda Referanslar'dan önce kısa bir bölüm, sunumda Teşekkürler slaydında bir satır. Ayrıntı: `references/yz_beyani.md`.
- **Dil.** Görüşme öğrencinin yazdığı dilde yürür. Form ve sunumun dili öğrencinin seçimidir (S1'de sorulur); varsayılan Türkçe, ikisi aynı dilde. İngilizce seçildiyse `form.md` ve `sunum.md` başlıkları İngilizce yazılır (karşılıklar `references/form.md` ve `references/sunum.md` sonunda), betiklere `--dil en` / `dil: en` verilir; şablonların sabit metinlerini (etiketler, bölüm başlıkları, altbilgi, kapanış) betikler çevirir. Çalışma işaretleri (`[ÖĞRENCİ TAMAMLAYACAK]`, `[DOĞRULANACAK]`, `[ÖĞRENCİ KARARI]`) her dilde aynı yazılır. Teknik terimin ilk geçtiği yerde öbür dildeki karşılığı parantez içinde verilebilir. Öğrencinin kendi cümlelerini koru; yalnız açıklık ve dil bilgisi için düzelt.
- **Teşekkür.** Danışman ve varsa eş danışman, fon ya da proje (kurum, numara), veri/numune/cihaz/laboratuvar sağlayanlar, katılımcılar (S19). Sunumda kapanış slaydının içeriği budur (Türkçe "Teşekkürler", İngilizce "Acknowledgements"); formda yalnız fon, proje, kurum ya da veri desteği varsa ya da öğrenci isterse, Referanslar'dan önce numarasız bölüm. Teşekkür edilecek kimse yoksa kapanış slaydı yalnız başlık, tarih ve yapay zekâ satırıyla kalır; bu bir eksik değildir.
- **Onay almadan dosya üretme.** Her adımın sonunda öğrenciye göster, onay al, sonra devam et.
- **Sorun günlüğü tut.** Betik hatası, uygulanamayan ya da belirsiz yönerge, karşılanmayan durum, bütçe aşımı ve öğrencinin takıldığı adım `sorunlar.md` çalışma dosyasına satır olarak yazılır (biçim `references/geri_bildirim.md`); 6. adımda bundan hazırlayana yönelik rapor çıkar. Günlüğe tez içeriği, ad, numara, belge ve kaynak girmez.

## Akış

### 0. Belgeleri topla ve oku

Gizli veri hatırlatması başlangıç uyarısında verildi; tekrarlama. Öğrenci şüphesini dile getirirse: böyle veri yüklenmez, metinde yalnız açık literatür kullanılır. Öğrenciden elindekileri iste: tez önerisi, danışmanla yazışmalar, makale taslağı, teknik rapor, önceki sunumlar, veri ve grafikler, okuduğu kaynak listesi. Hepsini oku; görüşmede cevabını belgeden bulabildiğin soruyu sorma, bulduğunu öğrenciye doğrulat. Belge yoksa görüşme daha uzun sürer, ama atlanmaz.

### 1. Görüşme

`references/gorusme.md` dosyasını oku ve oradaki soru ağacını uygula. Sorular turlar hâlinde sorulur; her soruya önerili bir cevap eklenir; bir turun cevapları gelmeden sonraki tura geçilmez. Görüşme bitince `seminer.json` dosyasını (şema aynı belgede) doldur ve öğrenciye özetini göster.

Konu seçiminde dersin sırası kesindir: **birinci tercih tez çalışması**. Tez henüz olgunlaşmadıysa tez konusu, önemi ve literatür özeti. Bunlar da yoksa bitirme çalışması ya da bir proje; en az tercih edilen seçenek. Alternatife geçmeden önce görüşmedeki "tez var mı" turu tamamlanmalıdır.

### 2. İçerik planı ve plan geçişi

Görüşme çıktısından bir plan yaz ve onaylat. Planın sonunda deste geneline bakan **en çok 4 çoklu-öneri sorusu** sor (biçim `references/gorusme.md`, "Çoklu-öneri sorusu"): numaralı liste, önerili seçim, cevap numarayla.

1. **Başlıklar ve bütçe:** hangi başlıklar düşüyor (Teşekkürler ve Kaynaklar kalır), slaytların başlıklara dağılımı (15–20 içerik slaydı; bulgusuz sunumda Literatür ve Yöntem gövdeyi taşır), birleştirme ya da bölme önerileri.
2. **Görseller:** hangi slayta ne lazım; kim çizecek (öğrenci / ajan, beyan edilir); yeniden çizilecekler. Ajan çizecekse içerik öğrenciden gelir.
3. **Kalıplar:** salt metin kalan slaytlardan tablo, süreç, karşılaştırma, kart ya da zaman çizelgesine çevrilmesi önerilenler.
4. **Savunulamayacak noktalar:** görüşmedeki tetikleyiciler varsa (bkz. gorusme.md), yoksa bu soru yok.

Sonuçlar başlığı düştüyse sunum, Yöntem'in son slaydı olan "sonraki adımlar" ile biter; kontrol listesindeki "sonuç slaydı" o slayttır.

Plan içeriği:

- Formun her bölümü için bir iki cümlelik özet.
- Sunumun on başlığı (aşağıda) ve her başlık altındaki slaytlar; her slayt için **tek bir iddia cümlesi** (`mesaj:` satırı olur) ve **kanıt kalıbı**: grafik, şema, tablo, iki sütun, süreç, kartlar, zaman çizelgesi (`references/sunum.md` kalıp tablosu). Salt madde listesi slaytları içerik slaytlarının en çok üçte biri; her birinin gerekçesi planda yazılır. Veri gerektiren görsel yoksa yapı kalıbı seç; öğrencinin veremediği görsel için `[ÖĞRENCİ TAMAMLAYACAK]` yaz.
- Slayt bütçesi: 30 dakikalık sunum için **15–20 içerik slaydı**. Kapak, içindekiler, teşekkür ve kaynaklar bu sayının dışında.
- Hangi başlıkların düşeceği. Bulgular ve sonrası tezin olgunluğuna göre kaldırılabilir; **Teşekkürler ve Kaynaklar her zaman kalır.**

### 3. Form

`references/form.md` dosyasını oku: her bölümün ne anlattığı, uzunluk ve **alt sınırlar** (metin ≥ 850 sözcük, hedef 1.000+; bölüm başına sözcük; ≥ 5 kaynak), kalite ölçütleri, IEEE kaynak biçimi. Tek sayfalık form teslim edilmez; malzeme yetmiyorsa öğrenciden iste. Metni `seminer.json` ve plana göre yaz, öğrenciye göster, onaydan sonra `scripts/form_doldur.py` ile `assets/stp596_bilgilendirme_form.docx` şablonunu doldur (`--tarih GG.AA.YYYY` ile seminer tarihini ver: altbilgideki dönem bundan hesaplanır, program adı yazar bloğundan alınır; `--donem` ve `--program` elle geçersiz kılar; İngilizce formda `--dil en`). Teşekkür bölümü varsa `## Teşekkür` / `## Acknowledgements` olarak beyandan önce yazılır. Şablonun stillerini ve iki sütunlu düzenini bozma.

### 4. Sunum ve taslak geçişi

`references/sunum.md` dosyasını oku: on başlık, her başlığın içeriği, slayt kuralları, görsel kuralları, kapak ve kapanış. Slayt metinlerini plana göre yaz ve öğrenciye göster. Göstermeden önce **bütün slaytların üzerinden bir kez daha geç** ve en çok 3 çoklu-öneri sorusu ekle:

1. **Animasyon:** S16'da "yerinde olursa" dendiyse, tıklamanın akıl yürütmeyi adım adım açacağı slaytlar (en çok 3–4; yöntem akışı, şema katmanları, karşılaştırma). Her madde "neden" ile; önerili seçim; "hiçbiri" seçeneği. Süs animasyonu önerme.
2. **Ajanın eklediği ifadeler:** alanın standart bilgisinden eklediklerin, slayt numarasıyla ("sahiplenmiyorsanız silerim").
3. **Son düzeltmeler:** kalan yer tutucular, uzun başlıklar, kaynak eksikleri; bilgi notu olarak, soru değil.

Onaydan sonra `scripts/deste_kur.py` ile `assets/sunum_format_16x9.pptx` şablonunun slaytlarını çoğaltarak desteyi kur; animasyon seçildiyse `references/animasyon.md` dosyasını oku ve `anim.py` ile uygula. Onay soruları her geçişte en çok 5; gerisi rapor satırıdır.

### 5. Kontrol

`scripts/kontrol.py` ile iki dosyayı denetle (slayt sayısı, punto, zorunlu slaytlar, madde sayısı, konuşma notu, kaynak numaraları, form bölümlerinin birbirinin kopyası olmaması, Lorem kalıntısı, yer tutucular). Her uyarıyı öğrenciyle çöz ya da bilinçli bırakıldığını not et. Sonra aşağıdaki kontrol listesini öğrenciyle birlikte geç.

### 6. Teslim notu

Öğrenciye kısa bir not ver: dosya adları, teslim yeri ve son tarih (sunumdan önceki Cuma akşamı), prova önerisi (en az bir kez sesli ve süre tutarak), soru-cevap için üç kural (soruyu tekrar et, kısa cevapla, bilmiyorsan söyle ve not al).

Sonra `references/geri_bildirim.md` dosyasını oku: öğrenciye oradaki **tek kapanış sorusunu** sor (cevap isteğe bağlı), `sorunlar.md` ve cevaptan `geri_bildirim.md` raporunu şablona göre yaz (her kullanımda; sorunsuz geçtiyse de), öğrenciye göster ve oradaki rica metniyle e-postayla göndermesini iste. Göndermek zorunlu değildir; bunu açıkça söyle.

## Dersin kuralları (öğrenciye hatırlat)

| Konu | Kural |
|---|---|
| Konu | Tez çalışması; olgunlaşmadıysa tez konusu + literatür; en son bitirme/proje |
| Takvim | Sunum Listesi tablosundaki tarih; bildirmek şartıyla değişim serbest; bir kez gelmeme hakkı; ikinci erteleme dersten başarısızlık |
| Form | Sunumdan önceki Cuma akşamına kadar ödev olarak yüklenir; yoksa sunum yapılamaz |
| Süre | 40 dk: ~30 dk sunum + 10 dk soru-cevap |
| Slayt | Slayt başına 1,5–2 dk; 15–20 içerik slaydı |
| Başlıklar | 1 Başlık Sayfası · 2 İçindekiler · 3 Giriş · 4 Literatür Taraması · 5 Araştırma Yöntemi · 6 Bulgular · 7 Tartışma · 8 Sonuçlar · 9 Teşekkürler · 10 Kaynaklar |

Literatür sunumu yapılıyorsa (tez olgunlaşmamışsa) kaynakların yöntem ve bulguları ilgili başlık altında toplu olarak sunulur; kaynak kaynak gezilmez.

## Dosya adları

- `<öğrenci_no>_<Soyad>_stp596_bilgilendirme_form.docx`
- `<öğrenci_no>_<Soyad>_stp596_sunum.pptx`
- `seminer.json`, `plan.md`, `sorunlar.md` çalışma dosyalarıdır; teslim edilmez. `geri_bildirim.md` hazırlayana yönelik rapordur; öğrenci isterse e-postayla gönderir.

## Araçlar

Betikler yalnız Python ister: `python-docx`, `python-pptx` (ikisi de `pip install python-docx python-pptx`). Node gerekmez. Her betik `--help` ile kullanımını yazar. Betiği çalıştıramadığın ortamda (yalnız sohbet) aynı işi elle yap: formu bölüm bölüm metin olarak ver, sunumu slayt slayt "başlık / mesaj / görsel / konuşma notu" biçiminde ver; öğrenci şablona kendisi aktarır.

## Son kontrol listesi (öğrenciyle birlikte)

**Güvenebilir mi? (ethos)**
- Kapakta ad, program, enstitü, danışman, tarih var; her slaydın altbilgisinde ad ve e-posta, sağ altta sayfa numarası.
- Kapanış slaydında danışman ve varsa destek verenler (fon, proje, veri, laboratuvar) adıyla anılıyor; formda da gerekiyorsa Teşekkür bölümü var.
- Her bulgunun yanında kaynak görünüyor; Kaynaklar slaydı IEEE biçiminde ve slayttaki her alıntıyı karşılıyor.
- Sınırlılıklar öğrencinin ağzından söyleniyor; "deney yok ama güvenilir" türü cümle yok.
- Yapay zekâ beyanı formda ve sunumda var.

**Dikkati tutuyor mu? (pathos)**
- Her slaytta tek mesaj; madde sayısı en çok beş; punto 18'den küçük değil.
- Her grafiğin ekseni, birimi ve başlığı var; tek slaytta beşten az renk.
- Süs animasyon, dekoratif görsel, "internetten" görsel yok; her görselin kaynağı var.
- İçindekiler slaydı sunumun akışını ve kabaca süre dağılımını gösteriyor.

**Akıl yürütme doğru mu? (logos)**
- Giriş bittiğinde araştırma sorusu tek cümleyle söylenebiliyor.
- Yöntem görünür: tasarım, veri, analiz. Bir grafik bir paragrafı geçer.
- Bulgular belirsizlik ve hata payıyla birlikte; tartışma literatüre geri dönüyor.
- Sonuç slaydı tek: dinleyen ne götürüyor? (Sonuçlar düştüyse "sonraki adımlar" slaydı bu işi görür.)
