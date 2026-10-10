# Görüşme: öğrenciyle soru ağacı

Amaç, formu ve sunumu yazmaya yetecek bilgiyi öğrenciden **sorarak** almak; uydurmak değil. Yöntem bir tasarım ağacıdır: her karar, ona bağlı kararları açar. Ağaç **turlar** hâlinde işlenir.

## Kurallar

- Bir turda, ön koşulu çözülmüş bütün soruları birden sor. Her soruyu numarala ve **önerili cevabını** yaz; öğrenci "evet" diyerek hızlı ilerleyebilsin.
- Cevabı başka bir açık soruya bağlı olan soru bir sonraki tura kalır.
- **Olguyu öğrenciye sorma, belgede ara.** Tez önerisinde yazan danışman adını, başlığı, yöntemi belgeden al ve doğrulat: "Tez önerinde danışman X görünüyor, doğru mu?"
- **Eski ya da tutarsız belge.** Belge bir yıldan eskiyse ya da kendi içinde çelişiyorsa (başlık başka, gövde başka; "kod yazılmadı" ama grafik var) tutarsızlığı 1. turda ayrı bir soru olarak sor; belgeden çıkardığın olguları "o zaman doğruydu, bugün?" diye doğrulat.
- **Tarih ve süre kuralı ajanın sorumluluğunda.** Seminer tarihinin haftanın gününü ve form son tarihini (önceki Cuma) sen hesapla ve yaz. Süre ders kuralıdır: 40 dakika (~30 sunum + 10 soru-cevap). Öğrenci farklı hatırlıyorsa ("20 dakika sanırım") kuralı söyle ve Sunum Listesi'nden doğrulatmasını iste; planı kurala göre kur.
- **Kaynakları doğrula.** Künyeyi DOI ya da Crossref/arama ile doğrula (web erişimin varsa `https://api.crossref.org/works?query=…`); doğrulananı tam yaz. Araç yoksa öğrencinin emin olduğu alanlar (dergi adı, yıl) yazılır, gerisi `[DOĞRULANACAK]`. Hiçbir künyeyi hafızadan tamamlama.
- **Direnç.** Öğrenci savunulamaz bir ifadede ısrar ederse (ölçülmemiş sayı, "ilk olacak", doğrulanmamış kaynak) sessizce kabul etme, ama yazma da: ifadeyi planda ve çıktıda `[ÖĞRENCİ KARARI: … ; ajan önerisi: …]` notuyla bırak. Karar öğrencinindir, kayıt senin.
- **Ajan çizecekse girdisi öğrenciden.** Şema (iş akışı, deney düzeneği) ajan tarafından çizilecekse adımları ve kutuların içeriğini öğrenci madde madde verir; sen yalnız çizersin ve beyan edersin. Alandan eklediğin kutu varsa işaretle.
- **Çalışma dosyaları onay beklemez.** `seminer.json` ve `plan.md` görüşme bitince hemen yazılır; `sorunlar.md` iş boyunca satır satır büyür (bkz. `geri_bildirim.md`); onay form ve sunum çıktıları içindir. `seminer.json` şemasına ihtiyaç duyduğun alanı ekleyebilirsin; var olan alan adlarını değiştirme.
- Öğrencinin cevabı belirsizse ("sanırım", "galiba") bir kez daha sor; belirsizlik `seminer.json` içine `[DOĞRULANACAK]` olarak girer.
- Her turun sonunda bekle. Cevaplar gelmeden sonraki tura geçme, dosya üretme.
- **Sorular asgari kapsamdır, tavan değil.** Belgelerden ve cevaplardan doğan kendi sorularını ilgili tura ekle (ör. yöntem sorusunda "hangi kütüphane, hangi referans rotoru"). Bütçe: bir turda en çok 8 soru, görüşme toplamı en çok 23.
- **Form için malzeme yeterliliği.** `references/form.md` alt sınırlarını (bölüm başına sözcük, en az 5 kaynak, her kaynağın ne yaptığı ve ne bulduğu) görüşmede sağla: bir bölümün malzemesi yetmeyecekse o turda bir derinleştirme sorusu sor ("okuduğunuz üç çalışma ne buldu?"). Tek sayfalık form kabul edilmez. Turun başında hatırlat: "Hepsi doğruysa tek 'evet' yeter."
- **Zayıf cevapta ısrar et, ama tek listede.** Aşağıdaki tetikleyicilerden biri görülürse ayrı tur açma; ilgili turun sonuna "savunulamayacak noktalar" başlıklı tek bir çoklu-öneri sorusu ekle (en çok 3 madde, her biri için ne yazılabileceği önerisiyle). Her turda en çok bir liste; liste turun 8 soru bütçesine dahildir. Yeni tetikleyici sonraki turda yeni listeye girer. Tetikleyiciler: "sınırlılık yok"; "literatürde yok / ilk kez"; ölçülmemiş sayı ("%30 hızlanır"); "sanırım / galiba / herhalde"; 1.1 ile 2.2'nin aynı cümlelerle anlatılması; doğrulanamayan kaynak; "beklentimizi doğruladı" türü dayanaksız sonuç.
- Görüşme ağacın bütün dalları gezildiğinde biter. Bitince `seminer.json` dosyasını doldur ve öğrenciye bir ekran özeti göster; onaydan sonra plana geç.

## Çoklu-öneri sorusu

Deste ya da form geneline bakan kararlar tek tek sorulmaz; bir konu bir sorudur, cevap numarayla verilir:

```
❓ **S16 · Animasyon**: 17 slaydın tamamına baktım; tıklamanın akıl yürütmeyi adım adım
açacağı yerler şunlar. Numarayla seçin ("1, 3" ya da "hiçbiri" ya da "hepsi").
  1. Slayt 8 · GA döngüsü: dört operatör sırayla gelirse döngü mantığı izlenir.
  2. Slayt 11 · İş akışı: kutular sırayla; "her birey için BEMT" vurgusu.
  3. Slayt 16 · Doğrulama: iki adım ayrı tıklamada, sınır en son.
➡️ Önerim 1 ve 2; 3 gerekli değil, iki adım zaten yan yana okunuyor.
```

Bu biçim görüşmede (S15, S16, S18) ve plan ile taslak geçişlerinde (SKILL.md 2. ve 4. adım) kullanılır.

Tur biçimi:

```
❓ **S1 · <soru başlığı>**: <soru; gerekiyorsa seçenekler>
➡️ <önerili cevap>

---

❓ **S2 · …**
➡️ …
```

## 1. tur: kimlik ve durum

**S1 · Kimlik ve dil.** Ad soyad, öğrenci numarası, program (ör. Savunma Teknolojileri YL, Uçak ve Uzay Mühendisliği YL/DR), kurum ve varsa çalıştığı yer, e-posta ya da ORCID. Form ve sunumun dili: Türkçe mi, İngilizce mi?
➡️ Belgelerde bulduğunu yaz, doğrulat. Dil için varsayılan Türkçe; tez İngilizce yazılıyorsa ya da öğrenci isterse İngilizce. İkisi aynı dilde olur; `seminer.json` içine `dil` yazılır.

**S2 · Danışman.** Tez danışmanı kim? Henüz atanmadıysa kiminle görüşülüyor?
➡️ Belgeden; yoksa "henüz atanmadı" kabul edilir ve formda öyle yazılır.

**S3 · Tez aşaması.** Şu an hangisi doğru?
(a) Tez konusu yok. (b) Konu var, danışmanla konuşuldu, literatür okunuyor. (c) Tez önerisi verildi, yöntem kuruldu. (d) Veri ya da ilk bulgular var. (e) Yazım aşamasında.
➡️ Belgelerden tahmin et ve sor. Cevap (a) ise 2B turuna, diğerleri 2A turuna gider.

**S4 · Seminer tarihi ve süre.** Sunum Listesi tablosundaki tarih ne? Form bu tarihten önceki Cuma akşamına kadar yüklenecek.
➡️ Öğrenci bilir; haftanın gününü ve teslim son tarihini sen hesapla, `seminer.json`'a yaz. Süreyi sorma, kuralı söyle: 40 dk (~30 + 10); farklı hatırlıyorsa Sunum Listesi'nden doğrulatmasını iste.

**S5 · Belgeler.** Elinde başka belge var mı: tez önerisi, makale taslağı, rapor, veri, grafik, okunmuş kaynak listesi, önceki sunum?
➡️ Varsa yüklet ve oku; sonraki turların sorularını buna göre azalt.

## 2A. turu: tez var (S3 cevabı b, c, d, e)

**S6 · Tez sorusu.** Tezin araştırma sorusu ya da hipotezi tek cümleyle ne? "X yöntemiyle Y'nin Z üzerindeki etkisini belirlemek" gibi.
➡️ Belgeden bir cümle öner; öğrenci düzeltsin. Bu cümle hem formun özetine hem Giriş slaydına girer.

**S7 · Neden önemli.** Bu soru neden şimdi, neden burada? Hangi boşluğu dolduruyor; kim kullanır?
➡️ İki üç cümle. Formda 1.2, sunumda Giriş.

**S8 · Savunma ve havacılık ilişkisi.** Tez hangi sektör, teknoloji ya da kullanım senaryosuyla ilişkili; ne gibi fayda sağlar? Program savunma teknolojileri değilse "havacılık ve uzay" olarak sor.
➡️ Belgeden öner. Formun 1.2 bölümü budur; "savunma sanayiine katkı sağlar" gibi genel cümleyle yetinme, somut uygulama iste.

**S9 · Yöntem.** Araştırma tasarımı ne: deneysel, sayısal benzetim, gözlemsel, nitel, nicel, karma? Veri nereden, analiz nasıl?
➡️ Belgeden öner. Yöntem henüz kurulmadıysa "planlanan yöntem" olarak yaz.

**S10 · Bulgular.** Elde bulgu var mı? Hangi grafik, tablo, sayı gösterilebilir? Belirsizlik ya da hata payı biliniyor mu?
➡️ (b) ve (c) için "yok" normaldir; o zaman Bulgular, Tartışma ve Sonuçlar başlıkları sunumdan düşer, literatür ve yöntem planı gövdeyi taşır. (d) ve (e) için her bulgunun görselini iste.

**S11 · Yayınlar ve sınırlılıklar.** Tezden çıkmış yayın, bildiri ya da rapor var mı? Çalışmanın bugünkü sınırlılıkları ne?
➡️ Sınırlılığı öğrenci söylesin; sunumda "sınırlılıkları siz söyleyin, dinleyici bulmadan önce" kuralı geçerli.

**S12 · Seminerin tezdeki yeri.** Seminerde tezin hangi parçası anlatılacak: ön çalışma, problemin tanımlanması, yöntem, ara sonuçlar, sonuçlar?
➡️ Aşamaya göre öner: (b) problemin tanımı ve literatür; (c) problem + yöntem; (d) yöntem + ara sonuç; (e) sonuçlar. Formun 2.2 bölümü budur ve **1.1 ile aynı metin olamaz**.

## 2B. turu: tez yok (S3 cevabı a)

Bu tur bir zorlama turudur. Dersin birinci tercihi tezdir; alternatife geçmeden önce aşağıdakiler sorulur.

**S6′ · Gerçekten yok mu?** Danışman atandı mı, danışmanla konu konuşuldu mu, aklında aday konu var mı, tez önerisi ne zaman verilecek?
➡️ Aday konu varsa S3 cevabı (b) sayılır: 2A turuna dön, "tez konusu + literatür" çerçevesinde devam et. Konu adayı bile yoksa S7′'ye geç.

**S7′ · Alternatif.** Sırasıyla: (1) olası tez alanında bir literatür özeti; (2) bitirme çalışması; (3) bir proje. Hangisi mümkün?
➡️ (1)'i öner. Formun "Tez Çalışması Durumu" bölümü boş kalmaz: tezin neden henüz olmadığı ve ne zaman beklendiği bir paragrafla yazılır.

**S8′ · Seçilen konunun sorusu, önemi, savunma/havacılık ilişkisi, kaynakları.** 2A'daki S6–S9'u seçilen konu için sor.
➡️ Literatür sunumunda kaynak kaynak gezilmez; kaynakların yöntemleri ve bulguları ilgili başlık altında toplu olarak anlatılır.

## 3. tur: sunum kararları

(Düşen başlıklar ve slayt bütçesi burada sorulmaz; plan geçişinde, SKILL.md 2. adım, planla birlikte önerilir. S13 ve S14 numaraları bu yüzden boştur.)

**S15 · Eldeki görseller.** Elinde ne var: grafik, şema, fotoğraf, tablo? Her birini aç, kusurlarını (eksensiz, birimsiz, kesik etiket, kaynaksız) çoklu-öneri biçiminde listele: "1. tasarim_degiskenleri.png: etiketler kesik, log eksen yazmıyor → yeniden çizeyim mi?"
➡️ Hangi slayta hangi görselin gerektiği burada sorulmaz; o plan geçişinde (SKILL.md 2. adım) toplu önerilir. "İnternetten" görsel kullanılmaz; her görselin kaynağı yazılır.

**S16 · Animasyon ilkesi.** Tıklamayla açılan içeriğe genel olarak açık mı: "evet, yerinde olursa" / "hayır, hiç"?
➡️ Varsayılan: "yerinde olursa, en çok 3–4 slayt, süs için değil". Hangi slaytlarda olacağı burada sorulmaz; taslak geçişinde (SKILL.md 4. adım) deste geneline bakılıp çoklu öneri olarak sunulur.

**S17 · Yapay zekâ kullanımı.** Bu çalışmada yapay zekâ ne yaptı, ne yapmadı? (Metin düzenleme, çeviri, kaynak biçimlendirme, slayt kurma, kod, analiz?) Hangi araç?
➡️ Doğru cevap bu görüşmenin kendisidir: "biçimlendirme, dil düzeltme, düzen; içerik ve sorumluluk öğrencide." Beyan metni buradan yazılır (`yz_beyani.md`).

**S18 · Kaynaklar.** Formda ve sunumda anılacak kaynakların künyeleri: DOI ya da tam künye.
➡️ Öğrenciden liste iste; DOI ile doğrulanamayanı `[DOĞRULANACAK]` işaretle.

**S19 · Teşekkür.** Kime teşekkür edilecek: danışman ve varsa eş danışman; fon ya da proje (kurum, numara); veri, numune, cihaz ya da laboratuvar sağlayanlar; katılımcılar. Formda da yer alsın mı?
➡️ Adlar unvanıyla, kurumlar tam adıyla, proje numarası varsa yazılır. Sunumda kapanış slaydına girer; formda yalnız fon, proje, kurum ya da veri desteği varsa ya da öğrenci isterse yazılır. Teşekkür edilecek kimse yoksa "yok" cevabı yeterlidir; kapanış slaydı yalnız başlık, tarih ve yapay zekâ satırıyla kalır.

## Çıktı: seminer.json

```json
{
  "dil": "tr | en",
  "ogrenci": { "ad": "", "no": "", "program": "", "kurum": "", "sehir": "İstanbul, Türkiye", "eposta_veya_orcid": "" },
  "danisman": "",
  "seminer_tarihi": "2026-11-04",
  "form_son_tarih": "2026-10-30",
  "konu_turu": "tez | tez_konusu_literatur | bitirme_proje",
  "tez": {
    "baslik": "",
    "soru": "",
    "asama": "konu_yok | konu | oneri_yontem | bulgu | yazim",
    "onem": "",
    "savunma_havacilik_iliskisi": "",
    "yontem": "",
    "bulgular": "",
    "sinirliliklar": "",
    "yayinlar": []
  },
  "seminer": {
    "baslik": "",
    "kapsam": "",
    "tezle_iliski": "on_calisma | problem_tanimi | yontem | ara_sonuc | sonuc",
    "dusen_basliklar": ["Bulgular", "Tartışma"],
    "slayt_butcesi": { "Giriş": 2, "Literatür Taraması": 4, "Araştırma Yöntemi": 5, "Sonuçlar": 1 },
    "animasyon": false
  },
  "kaynaklar": [
    { "ieee": "A. Yazar, \"Başlık,\" Dergi, c. 1, s. 1–10, 2024, doi: 10.xxxx/yyyy.", "dogrulandi": true }
  ],
  "gorseller": [
    { "slayt": "Araştırma Yöntemi", "aciklama": "deney düzeneği şeması", "dosya": "duzenek.png", "kaynak": "öğrencinin çizimi" }
  ],
  "tesekkur": { "satirlar": ["Danışman Doç. Dr. …", "TÜBİTAK 1001, proje no. …"], "formda": false },
  "yz": { "arac": "", "yapilanlar": ["metin düzenleme", "kaynak biçimlendirme", "slayt düzeni"], "yapilmayanlar": ["içerik üretimi", "veri analizi"] },
  "anahtar_kelimeler": []
}
```

Belirsiz kalan her alan `[DOĞRULANACAK]` ya da `[ÖĞRENCİ TAMAMLAYACAK]` değeri alır; betikler bu işaretleri çıktıya aynen taşır ki gözden kaçmasın.
