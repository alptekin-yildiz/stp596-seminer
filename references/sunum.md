# Seminer sunumu: on başlık, slayt kuralları, şablon

Şablon: `assets/sunum_format_16x9.pptx` (13,33 × 7,5 inç). Görünüm: açık altıgen desenli zemin, sol üstte İTÜ logosu, sağ üstte lacivert şeritte başlık (Helvetica 28), gövde Helvetica 18, altta sunanın adı ve e-postası (altbilgi), sağ altta "n / N" sayfa numarası. Betik şablonun yedi örnek slaydını çoğaltarak desteyi kurar; sen slayt metinlerini `sunum.md` dosyasına yazarsın (biçim en altta).

Yazım sırası: plan onayı → `sunum.md` → öğrenciye göster → `python3 scripts/deste_kur.py sunum.md --sablon assets/sunum_format_16x9.pptx --cikti <no>_<Soyad>_stp596_sunum.pptx` → istenirse `anim.py` → `kontrol.py`.

## Süre ve sayı

40 dakika: ~30 dakika sunum, 10 dakika soru-cevap. Slayt başına 1,5–2 dakika → **15–20 içerik slaydı**. Kapak, İçindekiler, Teşekkürler ve Kaynaklar sayılmaz. Toplam dosya 19–24 slayt.

## On başlık ve içerikleri

| # | Başlık | Slayt | İçerik |
|---|---|---|---|
| 1 | Başlık Sayfası | 1 | Sunum başlığı, sunan, program ve enstitü, danışman, tarih |
| 2 | İçindekiler | 1 | Akış tek bakışta; kabaca süre dağılımı (ör. "Yöntem · 8 dk") |
| 3 | Giriş | 1–2 | Konunun tanıtımı; araştırma sorusu ya da hipotez **tek cümle**; amaç; önemi: neden şimdi, neden burada |
| 4 | Literatür Taraması | 2–4 | Önceki çalışmaların özeti; kuramsal çerçeve; araştırma boşluğu; her iddianın yanında kaynak [n] |
| 5 | Araştırma Yöntemi | 3–5 | Tasarım (deneysel, sayısal, gözlemsel, nitel, nicel); veri toplama; analiz; örneklem; bir akış şeması bir paragrafı geçer |
| 6 | Bulgular | 3–5 | Ana sonuçlar grafik, tablo, şekille; istatistik varsa; **belirsizlik ve hata payı** |
| 7 | Tartışma | 1–2 | Yorum; soru/hipotezle uyum; literatürle karşılaştırma; sınırlılıklar ve gelecek çalışma |
| 8 | Sonuçlar | 1 | Dinleyen ne götürüyor: ana bulgular, önemi, gelecek çalışma tek cümle |
| 9 | Teşekkürler | 1 | Danışman, kurum, veri/araç/fon sağlayanlar (S19); yapay zekâ beyanı satırı. İngilizce destede başlık "Acknowledgements". Teşekkür edilecek kimse yoksa slayt başlık, tarih ve yapay zekâ satırıyla kalır |
| 10 | Kaynaklar | 1–2 | IEEE liste; slayttaki her [n] burada karşılanır; görsel kaynakları da |

Bulgular, Tartışma, Sonuçlar tezin olgunluğuna göre kaldırılabilir; o zaman Literatür ve Yöntem planı gövdeyi taşır. Teşekkürler ve Kaynaklar her zaman kalır. Literatür sunumunda kaynaklar tek tek gezilmez; yöntemleri ve bulguları ilgili başlık altında toplu verilir.

Slayt başlığında başlık numarasını taşı: "3 · Giriş", "5 · Yöntem: deney düzeneği". Dinleyici nerede olduğunu bilir. Başlık **en çok 45 karakter**; şerit buna göre ölçülüdür, uzun başlık puntoyu düşürür.

## Slayt kuralları (Retorik dersinin üç sorusu)

**Güven (ethos)**
- Kapak sade ve tam: ad, program, enstitü, danışman, tarih. Her slaydın altbilgisinde ad ve e-posta, sağ altta sayfa numarası (betik yazar; `eposta:` ön bilgide zorunlu).
- Her bulgunun, her görselin yanında kaynak; "internetten" görsel yok.
- Sınırlılıklar öğrencinin ağzından, dinleyici bulmadan önce.
- Yazım hatası güveni ilk saniyede bozar; metni iki kez oku.

**Dikkat (pathos)**
- **Tek slayt, tek mesaj.** Slayt başlığı o mesajı söyleyebiliyorsa iyidir ("Kiriş ağırlığı %31,7 azaldı" > "Sonuçlar").
- En çok 5 madde, maddede en çok 2 satır. Paragraf gerekiyorsa en çok 4 satır.
- Punto 18'den küçük olmaz (Kaynaklar slaydında 14 olabilir). Metin sığmıyorsa slaydı böl, puntoyu küçültme. Punto **bütün destede tektir**: başlıklar bir punto, gövde bir punto; slayttan slayta ve slayt içinde değişmez (aşağıda "Tipografi ve matematik").
- Yalnız metinden oluşan slayt sayısı içerik slaytlarının yarısını geçmesin; her iki slayttan birinde şema, grafik, tablo ya da fotoğraf olsun. Yöntem anlatan her slayt bir şema ister.
- Grafik: eksen adı, birim, başlık, kaynak; tek slaytta en çok 4 renk; okunur yazı (grafik içi yazı da 14'ten küçük olmaz ve bütün görsellerde aynı puntodadır).
- Süs animasyon, dekoratif görsel, ses, geçiş efekti yok. Animasyon yalnız bir akıl yürütmeyi adım adım açmak için (`animasyon.md`).
- Konuşmacı ekrana değil dinleyiciye konuşur; konuşma notu slaytta değil notlar bölümünde.

**Doğruluk (logos)**
- Giriş bittiğinde araştırma sorusu tek cümleyle söylenmiş olmalı.
- "Beklentimizi doğruladı", "sonuçlar güvenilirdir", "literatürde en çok bu kullanılıyor" türü dayanaksız cümle yok; iddianın yanında veri, sayı, kaynak.
- Olumsuz ve belirsiz sonuç da sunulur. Eksen kırpma, seçerek gösterme, ölçek oyunu çarpıtmadır (YÖK Yönergesi Madde 4/1-c).
- Yöntem görünür: dinleyen "nasıl yaptın" sorusunun cevabını slaytta görmeli.

## Slayt kalıpları: iddia ve kanıt

Bilimsel sunumda yerleşik kural (Alley, *The Craft of Scientific Presentations*; Doumont, *Trees, Maps, and Theorems*): **her slayt bir iddia taşır, gövde o iddianın kanıtıdır.** İddia tam cümledir ve `mesaj:` satırına yazılır (başlık şeridi dar olduğundan kısa başlık kalır, iddia altında görünür). Kanıt bir görsel ya da yapı kalıbıdır; madde listesi kanıt değil, konuşma notudur.

Plan adımında her slayt için önce iddiayı, sonra kalıbı seç. Kalıp seçimi:

| İçerik ne? | Kalıp | sunum.md türü |
|---|---|---|
| Ölçüm, eğri, dağılım, karşılaştırmalı sayı | Grafik | `gorsel`, `metin_gorsel` |
| Düzenek, akış, kesit, mimari | Şema | `gorsel`, `metin_gorsel` (katmanlı: tıklamayla) |
| Değişkenler, parametreler, aralıklar, kaynaklar | Tablo | `tablo` |
| İki yaklaşım, önce/sonra, var/yok, girdi/çıktı | İki sütun | `karsilastirma` |
| Adımlar, sıra, yöntem akışı | Süreç | `surec` |
| 2–4 paralel öğe (kısıtlar, bileşenler, çıkarımlar) | Kartlar | `kartlar` |
| Takvim, aşamalar, geçmiş ve plan | Zaman çizelgesi | `zaman` |
| Birkaç çarpıcı sayı | Üç sayı | `sayilar` |
| Tek paragraf iddia (araştırma sorusu gibi) | Metin | `metin` |

**Denklem içeren slayt:** ayrı tür yoktur; `metin` ya da `metin_gorsel` kalıbında denklem kendi satırında `$$ … $$` arasında LaTeX ile yazılır, altına değişkenlerin tanımı gelir. Betik onu düzenlenebilir PowerPoint denklemine çevirir (aşağıda "Tipografi ve matematik"); `x_1`, `x^2`, `sqrt()` türü elle yazım kullanılmaz.

**Literatür ve yöntem slaytlarında taban:** her literatür slaydında en az iki kaynak numarası; her yöntem slaydında bir şema, tablo ya da süreç kalıbı.

**Madde listesi sınırı:** salt metin (`metin`) slaytları içerik slaytlarının **en çok üçte biri**; her birinin planda gerekçesi olur ("araştırma sorusu tek cümle" gibi). Betik ve kontrol betiği sınırı aşınca uyarır. Bir slaytta madde listesi kaçınılmazsa en çok 5 madde, maddede en çok 2 satır.

Dayanak: Mayer'in çoklu ortam ilkeleri (tutarlılık, işaretleme, fazlalık): okunan madde listesi dinlemeyi engeller; görsel + konuşma birlikte daha iyi öğrenilir. Kosslyn, *Clear and to the Point*: bir seferde 4 ± 1 öğe.

## Grafik kuralları (dataviz özeti)

- Her grafikte başlık (ne, nerede, ne zaman), eksen adı ve birim, kaynak satırı; alt yazı "Şekil n." ile başlar.
- Tek seri lacivert; ikinci seri bronz, üçüncü çelik mavisi. Dört renkten fazlası yok; renk yalnız anlam taşıyorsa değişir.
- Yazı grafiğin içinde 14 pt'den küçük görünmesin: grafiği slayt ölçüsünde (ör. 6×4 inç, 130–150 dpi) üret. Eksen adı, sayılar ve lejant bütün grafiklerde aynı puntoda.
- **Slayt başına en çok 3 grafik**, yan yana ve her biri okunur boyutta. Görsel alanı ≈ 11,7 × 4,6 inçtir; 3×3 grafik konursa her biri ≈ 3,9 × 1,5 inçe düşer ve 14 pt yazıya yer kalmaz. Büyük çizilip küçültülen grafiğin yazısı da aynı oranda küçülür (16 pt, üçte birine küçültülünce ≈ 5 pt). Fazlası için: slaytlara böl; mesajı taşıyan bir iki grafiği seç, gerisini forma ya da yedek slayta taşı; ortak eksenli tek grafikte birleştir.
- Etiket, sembol ve sayı hiçbir çizginin, okun ya da başka yazının üstüne binmez; açı etiketi açının içine, yayın yanına konur. Sığmıyorsa şekil büyütülür, punto küçültülmez.
- **Grafik başına en çok 4 seri** (eğri, çubuk grubu). Fazlası için asıl seriyi renkli, öbürlerini soluk gri çiz ya da grafiği böl. Lejant yerine serinin ucuna doğrudan etiket tercih edilir.
- Eksen sıfırdan başlar; başlamıyorsa eksen kırığı ve not. Logaritmik eksen etikette yazılır.
- Belirsizlik gösterilir: hata çubuğu, aralık, örneklem büyüklüğü. Yoksa altyazıda "belirsizlik hesaplanmadı".
- Izgara soluk, çerçeve yok, efekt ve üç boyut yok. Tablo yerine grafik, grafik yerine cümle: hangisi daha az mürekkeple aynı şeyi söylüyorsa o.
- Fotoğraf ve başkasının grafiği için kaynak ve lisans; "internetten" yok.

**Bu sınırlar okunabilirlik önerisidir, ders kuralı değildir.** Ajan kendi yazdığı plan, slayt ve grafikte onlara uyar. Öğrencinin planı ya da kendi görseli sınırı aşıyorsa ek soru açmadan mevcut turda söyler: plan geçişinde "Görseller" sorusunun içinde, sonra son göz turunun bulgu listesinde; nedenini bir cümleyle ve bir öneriyle ("6. slaytta 6 grafik var, okunmaz; mesajı taşıyan ikisini seçip gerisini forma taşımayı öneririm"). Öğrenci yine de isterse bırakılır, `plan.md`'ye "bilinçli bırakıldı" notu düşülür ve `sorunlar.md`'ye `uyari` satırı yazılır (`geri_bildirim.md`).

## Tipografi ve matematik

Öğrenci sunumlarında en sık görülen iki biçim hatası: slayttan slayta, hatta aynı slaytta değişen punto ve denklem yerine klavyeyle yazılmış matematik. İkisi de dinleyiciye özensizlik olarak yansır (ethos).

**Punto ölçeği.** Destede her rolün tek puntosu vardır: slayt başlığı, gövde (madde, paragraf, kart ve karşılaştırma kutuları), süreç kutusu, tablo, alt yazı ve not satırı, Kaynaklar (14), sayfa numarası (12). `deste_kur.py` bu ölçeği kendisi kurar: önce her alana sığan en büyük puntoyu ölçer, sonra aynı roldeki bütün alanları en küçüğüyle yazar; çıktıda "Punto (deste geneli)" satırını ve puntoyu düşüren slaydı bildirir. Uzun bir başlık bütün başlıkları küçültür; dolu bir slayt bütün gövdeyi küçültür. Çözüm o başlığı kısaltmak ya da o slaydı bölmektir, tek slayda ayrı punto vermek değildir.
- Vurgu kalın yazıyla yapılır, punto büyütülerek değil.
- Öğrenci desteyi PowerPoint'te elle düzeltirse aynı ölçeği korur; yeni eklediği metin kutusu da gövde puntosundadır. `kontrol.py` slaytlar arası ve slayt içi farkı bildirir.
- Tek yazı tipi ailesi: şablonunki (Helvetica). Şekillerde de tırnaksız (sans-serif) bir aile, mümkünse aynısı.

**Şekil içi yazı.** Eksen etiketi, lejant, şema kutusu yazısı slaytta 14–18 pt görünür ve **bütün görsellerde aynı** puntodadır.
- Görsel, slayttaki son boyutunda çizilir; sonradan küçültmek içindeki yazıyı da küçültür. Kutu ölçüleri (mesaj satırı varken): `gorsel` ≈ 11,7 × 4,6 inç, `metin_gorsel` ≈ 6,1 × 4,6 inç, `uc_gorsel` ≈ 3,95 × 4,0 inç. matplotlib'de `figsize` bu ölçüler, `font.size` bütün şekillerde aynı değer (16 gibi) olur.
- Ajan çizmiyorsa (öğrencinin ya da kaynağın görseli) puntoyu ajan düzeltemez: farklı ya da küçük punto görürse öğrenciye söyler, şekli son boyutunda yeniden üretmesini ister.

**Matematik yazımı.**
- Klavye yazımı kullanılmaz: `x_1`, `V_inf`, `x^2`, `e^(-t)`, `a*b`, `sqrt(x)`, `int`, `sum`, `<=`, `>=`, `$…$`, `\alpha`. Doğrusu gerçek indis ve üs, gerçek simge: x₁, x², a·b ya da a × b, √x, ∫, Σ, ≤, ≥, α.
- Cümle içindeki tek sembol ya da basit ifade Unicode metinle yazılır (θ = 30°, Re ≈ 2·10⁵, vᵢ); cümle içinde `$…$` kullanılmaz.
- Kendi satırında duran her denklem `$$ … $$` arasında LaTeX ile yazılır: `$$ T = 2 \rho A v_i^2 $$`. `deste_kur.py` onu **düzenlenebilir PowerPoint denklemine** çevirir (Cambria Math, gövde puntosunda, ortalı); öğrenci tıklayıp PowerPoint'in denklem aracıyla değiştirebilir. Metin ve denklemler `sunum.md`'deki sırayla alt alta dizilir; denklemli slaytta `~~~` tıklama grubu kullanılmaz. Denklem yalnız `metin` ve `metin_gorsel` türlerinde yerleşir.
- Çeviriyi pandoc yapar (isteğe bağlı). pandoc yoksa ya da LaTeX çevrilemezse betik denklemin yerine `[ÖĞRENCİ TAMAMLAYACAK: denklem, PowerPoint'te Ekle → Denklem ile: …]` yazar ve uyarır; öğrenciye pandoc'u kurmasını ya da denklemi PowerPoint'te kendisinin yazmasını söyle. Denklemin resmini (ekran görüntüsü) koyma.
- Denklem PowerPoint'te görünür. Keynote, Google Slaytlar ve LibreOffice denklemin yerine düz metinli yedeğini gösterir (ör. `T = 2ρAvᵢ²`); öğrenciye sunumu PowerPoint'ten yapmasını söyle. Son göz turunda görüntüye çevirdiğinde yedeği görürsün: içerik doğruluğuna oradan bak, biçimi öğrenci PowerPoint'te denetler.
- Değişkenler italik, birimler, fonksiyon adları (sin, log, exp) ve diferansiyel d dik yazılır. Sayı ile birim arasında boşluk (10 m/s, 30 °C; açı derecesinde boşluk yok: 30°).
- Aynı büyüklük her yerde aynı sembolle gösterilir (form ve sunum, slayt ve slayt); her sembol ilk geçtiği yerde tanımlanır.
- Ondalık ayraç dile göre: Türkçede virgül (2,88 kg), İngilizcede nokta (2.88 kg); aynı belgede karışmaz.

## Şablon slayt türleri

| Tür | Şablon | Kullanım |
|---|---|---|
| `kapak` | 1 | Betik ön bilgiden kurar |
| `icindekiler` | 2 | Numaralı liste; betik `[icindekiler]` türünde listeyi yazar |
| `metin` | 2 | Yalnız metin; Giriş, Tartışma, Sonuç |
| `gorsel` | 3 | Tek büyük görsel + alt yazı; grafik, şema, fotoğraf |
| `metin_gorsel` | 4 | Solda metin, sağda görsel; Yöntem ve Bulgular için varsayılan |
| `uc_gorsel` | 5 | Üç görsel yan yana; karşılaştırma, süreç |
| `sayilar` | 6 | Üç altıgende üç sayı + etiket; ana bulgu özeti |
| `tablo` | 2 | Başlık satırı lacivert, satırlar dönüşümlü; `a \| b \| c` satırları |
| `karsilastirma` | 2 | `### Sol` ve `### Sağ` blokları; lacivert ve bronz başlık şeritli iki sütun |
| `kartlar` | 2 | 2–4 `###` bloğu; renkli başlık + gövde kartları |
| `surec` | 2 | Numaralı adım kutuları ve oklar; `###` bloklar ya da maddeler (≤6) |
| `zaman` | 2 | `tarih \| olay` satırları (≤6); yatay çizelge |
| `kaynaklar` | 2 | 14 pt IEEE liste |
| `tesekkur` | 7 | Betik ön bilgiden kurar; ek satırlar eklenebilir |

## Konuşma notları

Her içerik slaydına 2–4 cümlelik konuşma notu yaz (`>` satırları): slaytta yazmayan ama söylenecek şey, geçiş cümlesi ("Yöntemi gördük; şimdi bu yöntemin ne verdiğine bakalım"), olası soruya hazır cevap. Notlar prova içindir; slayda okunmaz.

## sunum.md biçimi (betiğin okuduğu dosya)

Dil: varsayılan Türkçe. İngilizce destede ön bilgiye `dil: en` eklenir; betik kapaktaki "Danışman" → "Advisor", kapanıştaki "Teşekkürler" → "Acknowledgements", devam slaydındaki "(devam)" → "(cont.)" çevirisini yapar. Slayt başlıkları, İçindekiler ("Contents"), Kaynaklar ("References") ve kapanış (`[tesekkur] Acknowledgements`) ajan tarafından İngilizce yazılır; kontrol betiği iki dili de tanır.

```markdown
---
dil: tr
baslik: Esnek Cidarlı Yakınsak-Iraksak Lüle Tasarımı
hazirlayan: Ad Soyad
program: Savunma Teknolojileri Yüksek Lisans Programı
kurum: İTÜ Havacılık Enstitüsü
danisman: Prof. Dr. Ad Soyad
tarih: 04.11.2026
eposta: ad.soyad@itu.edu.tr
sayfa_no: evet
yz_satiri: Form ve sunum Claude yardımıyla düzenlendi; içerik ve sorumluluk sunana aittir.
---

## [icindekiler] İçindekiler
- Giriş · 3 dk
- Literatür · 6 dk
- Yöntem · 10 dk
- Bulgular · 8 dk
- Sonuç · 3 dk

## [metin] 3 · Giriş: araştırma sorusu
mesaj: Tam cümlelik iddia; başlığın altında görünür (en çok 140 karakter).
Paragraf metni.
- Madde
- Madde
> Konuşma notu.

## [metin_gorsel] 5 · Yöntem: deney düzeneği
- Madde
~~~
- Tıklamayla gelen ikinci grup (animasyon isteğe bağlı)
![Şekil 2. Deney düzeneği şeması (öğrencinin çizimi)](gorseller/duzenek.png)
> Not.

## [gorsel] 6 · Bulgular: ağırlık–gerilme eğrisi
![Şekil 3. … Kaynak: öğrencinin analizi](gorseller/egri.png)

## [uc_gorsel] 6 · Bulgular: üç yük durumu
![2,5g manevra](gorseller/a.png)
![−1g](gorseller/b.png)
![İniş darbesi](gorseller/c.png)

## [tablo] 5 · Yöntem: değişkenler
mesaj: Beş değişken, aralıkları literatürden.
Gen | Değişken | Aralık | Kaynak
R | Yarıçap | 5,5–7,0 m | [3]
c | Veter | 0,25–0,45 m | [3]
Tablo altı not (isteğe bağlı, '|' içermeyen satır).

## [karsilastirma] 4 · Literatür: boşluk
mesaj: Literatürde var olanla eksik olan yan yana.
### Literatürde var
- madde
### Sınırlı ya da yok
- madde

## [kartlar] 5 · Yöntem: kısıtlar
mesaj: Üç kısıt fizikten ve görevden gelir.
### Kısıt 1
- madde
### Kısıt 2
- madde
### Kısıt 3
- madde

## [surec] 5 · Yöntem: doğrulama
mesaj: Doğrulama iki adımda yapılır.
### Adım 1 · Model
- madde
### Adım 2 · Optimizasyon
- madde

## [zaman] 5 · Yöntem: takvim
mesaj: Bugüne kadar yapılanlar ve plan.
- Mayıs 2026 | Tez önerisi
- Aralık 2026 | Seminer
- Bahar 2027 | İleri uçuş modeli (zaman kalırsa)

## [sayilar] 8 · Sonuçlar
- %31,7 | ağırlık azalması
- 2,88 kg | yeni tasarım kütlesi
- 1,5 | emniyet katsayısı

## [kaynaklar] Kaynaklar
[1] A. Yazar, "…," Dergi, c. 1, s. 1–10, 2024, doi: …
[2] …

## [tesekkur] Teşekkürler
Danışmanım Prof. Dr. Ad Soyad'a yönlendirmeleri için, veri desteği için X Laboratuvarı'na teşekkür ederim.
```

Kapanış slaydının satırları S19 cevabından gelir: danışman, destek/fon (kurum, proje no), veri/araç sağlayanlar; en altta `yz_satiri` betikçe eklenir. Teşekkür edilecek kimse yoksa gövde boş bırakılır.

Katmanlı görsel: `metin_gorsel` ya da `gorsel` slaydında birden çok `![…](…)` verilirse görseller aynı kutuya üst üste konur ve tıklamayla açılır (bir şemanın kutularının sırayla belirmesi gibi). `~~~` grup sayısı ile görsel sayısı eşitse her tıklamada ilgili madde grubu ve katman birlikte gelir; alt yazı son katmanınkidir.

Punto: betik bütün destede tek gövde puntosu kullanır; metin az olduğunda bu punto 24'e kadar büyür, en dolu slayta göre belirlenir (yukarıda "Tipografi ve matematik"). `punto:` satırı tek bir slaydı bu ölçünün dışına çıkarır ve tutarlılığı bozar; betik bunu uyarı olarak bildirir.

`mesaj:` satırı her içerik slaydında bulunmalı (İçindekiler ve Kaynaklar hariç). `###` satırları blok açar; blok içindeki `-` maddeler o bloğa aittir.

Kurallar: her `##` bir slayt; köşeli parantezdeki tür yukarıdaki tablodan; `-` ile başlayan satır madde, diğer satırlar paragraf; `![alt yazı](dosya)` görsel; `$$ LaTeX $$` kendi satırında denklem (`metin`, `metin_gorsel`); `>` konuşma notu; `~~~` gövdeyi tıklama gruplarına böler (en çok 3). Görsel dosyası yoksa betik yerine `[ÖĞRENCİ TAMAMLAYACAK: görsel]` kutusu koyar ve uyarır. `punto: 16` satırı bir slaydın gövde puntosunu değiştirir; kullanma, metin sığmıyorsa slaydı böl.
