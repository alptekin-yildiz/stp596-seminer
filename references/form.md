# Bilgilendirme formu: bölümler, ölçütler, biçim

Şablon: `assets/stp596_bilgilendirme_form.docx`. A4, IEEE bildiri düzeni: başlık ve yazar bloğu tek sütun, gövde iki sütun. Stiller şablonda hazırdır (paper title 24 pt, Author 11, Abstract 9 kalın, Body Text, Heading 1/2, references 8). Betik bu stilleri korur; metni sen yazarsın.

Dil: varsayılan Türkçe. Öğrenci İngilizce seçtiyse (S1) `form.md` başlıkları İngilizce yazılır (karşılıklar en altta) ve betik `--dil en` ile ya da `## Abstract` başlığını görünce şablonun sabit metinlerini (etiketler, bölüm başlıkları, altbilgi: "ITU Aviation Institute – … Fall/Spring Semester, STP 596 Scientific Research, Ethics and Seminar") İngilizce yazar. IEEE kalıplarında "ve" yerine "and", "c." yerine "vol.", "s." yerine "pp." kullanılır.

Hedef uzunluk: **2–3 sayfa; özet dahil, kaynaklar ve teşekkür hariç metin hedef 1.000+ sözcük, alt sınır 850.** Tek sayfa yetersizdir ve kontrol betiği uyarır. Ajanla çalışan öğrencinin ince form vermesi için mazeret yoktur; malzeme yetmiyorsa görüşmede derinleştirme sorusu sorulur.

## Alt sınırlar (kontrol betiği denetler)

| Bölüm | En az |
|---|---|
| Özet | 150 sözcük (en çok 250) |
| 1.1 Tez Çalışması Durumu | 150 sözcük |
| 1.2 Savunma/Havacılık ile İlişkisi | 120 sözcük |
| 2.1 Seminer Konusu | 200 sözcük (hedef 250+); anılan her kaynak için "ne yaptı, ne buldu" cümlesi |
| 2.2 Seminer – Tez İlişkisi | 60 sözcük (hedef 80+); 1.1 ile farklı |
| Referanslar | 5 kaynak; en az 3'ü hakemli makale ya da bildiri; hepsi metinde anılır |

Yöntem anlatan paragraf dört öğeyi içerir: tasarım, veri ya da model, analiz, doğrulama. Eksik öğe `[ÖĞRENCİ TAMAMLAYACAK: …]` ile işaretlenir; işaret kalırsa form teslim edilmez.

## Yazım sırası

1. Önce `seminer.json` ve içerik planı. Formun her bölümünü aşağıdaki ölçütlere göre yaz, `form.md` dosyasına (biçim en altta) koy.
2. Öğrenciye göster; öğrenci kendi cümlesi olarak sahiplenmediği her cümleyi değiştirsin.
3. Onaydan sonra: `python3 scripts/form_doldur.py form.md --sablon assets/stp596_bilgilendirme_form.docx --cikti <no>_<Soyad>_stp596_bilgilendirme_form.docx --tarih <seminer tarihi GG.AA.YYYY>`
   Altbilgideki `{PROGRAM}` ve `{DÖNEM}` yer tutucularını betik doldurur (dönem tarihten: Ağustos–Ocak Güz, Şubat–Temmuz Bahar).
4. `python3 scripts/kontrol.py <çıktı.docx>` ile denetle.

## Bölümler

### Seminer Başlığı
Seminerde anlatılacak şeyin adı; tezin adı değil (çakışabilir). En çok 12 sözcük, büyük harf kullanılmaz (şablon biçimi uygular). "… Çalışması Sonuçları ve Değerlendirme" türü uzatma yok.

### Yazar bloğu
Beş satır: Ad Soyad · Program adı (ör. Savunma Teknolojileri Yüksek Lisans Programı) · İTÜ Havacılık Enstitüsü · İstanbul, Türkiye · e-posta ya da ORCID. Öğrenci bir kurumda çalışıyorsa program satırı kalır, kurum satırına "İTÜ Havacılık Enstitüsü · <işyeri>" yazılabilir.

### Özet
150–250 sözcük, tek paragraf, "Özet—" etiketiyle başlar (betik ekler). Sıra: bağlam (1 cümle) → problem ya da araştırma sorusu (1) → yöntem (1–2) → şu ana kadarki sonuç ya da beklenen çıktı (1–2) → seminerin kapsamı (1). Kaynak numarası ve kısaltma açılımı özete girmez. "Önemli", "kritik", "kapsamlı" gibi değerlendirme sıfatları yerine ölçülebilir ifade.

### Anahtar Kelimeler
3–6 terim, küçük harf, virgülle; en özgülden en genele. Tez başlığındaki sözcükleri tekrarlamak yerine arama yapan birinin kullanacağı terimler.

### 1 Tez Çalışması

**1.1 Tez Çalışması Durumu** (1–3 paragraf). Tez başlığı ya da çalışma başlığı; danışman; hangi aşamada olduğu (konu, öneri, yöntem, veri, yazım); şimdiye kadar yapılanlar; varsa yayın ve bildiriler; önümüzdeki dönem planı; danışmanın onayladığı bir takvim varsa o. Gerekliyse etik değerlendirme (insan katılımcı, kurum verisi, ihracat kontrolü, gizlilik).
Tez yoksa bu bölüm boş kalmaz: tezin neden henüz olmadığı (danışman ataması, konu arayışı), ne zaman beklendiği ve bu seminer için seçilen alternatifin (literatür özeti / bitirme / proje) ne olduğu yazılır.

**1.2 Tezin Savunma Teknolojileri ile İlişkisi** (1–3 paragraf). Program savunma teknolojileri değilse başlık "Tezin Havacılık ve Uzay Teknolojileri ile İlişkisi" olur. Hangi sektör, platform ya da sistem; hangi kullanım senaryosu; hangi şartlar; hangi diğer teknolojilerle birlikte; ne gibi fayda (performans, maliyet, güvenlik, bağımsızlık). Somut ol: "savunma sanayiine katkı sağlayacaktır" değil, "X platformunun Y alt sisteminde Z'yi şu ölçüde iyileştirmesi beklenir."

### 2 Seminer

**2.1 Seminer Konusu** (3–4 paragraf). Seminerde ne anlatılacak: kapsam, ana sorular, hangi yöntem ve bulguların gösterileceği, hangi kaynakların kullanılacağı (kaynak numarasıyla, [1] gibi). Anılan her kaynak için bir cümle: **ne yaptı, ne buldu** ("[4] Lynx rotorunu klasik yöntemle boyutlandırır; optimizasyon yapmaz"). Ad geçirmek yetmez. Dinleyen, bu bölümü okuyunca sunumun içindekiler sayfasını zihninde kurabilmeli.

**2.2 Seminer – Tez İlişkisi** (1–2 paragraf). Seminer tezin neresidir: ön çalışma mı, problemin tanımı mı, yöntem mi, ara sonuçlar mı, sonuçlar mı? Seminerde anlatılmayacak tez parçaları neler ve neden (henüz yok, kapsam dışı, gizli)?
**Bu bölüm 1.1'in kopyası olamaz.** 1.1 tezi, 2.2 seminerin tezdeki yerini anlatır. Betik iki metin fazla benzerse uyarır.

### Teşekkür (gerekirse)
Numarasız başlık (IEEE "Acknowledgment"), beyandan ve Referanslar'dan önce. Yalnız fon ya da proje (kurum, numara), kurum desteği, veri/numune/cihaz/laboratuvar sağlayanlar varsa ya da öğrenci isterse yazılır; danışmana teşekkür isteğe bağlıdır. Yoksa bölüm atlanır; betik `## Teşekkür` başlığı yoksa hiçbir şey eklemez. İki üç cümle; adlar unvanıyla, kurumlar tam adıyla.

### Yapay Zekâ Kullanım Beyanı
Numarasız başlık, bir paragraf; metin kalıbı `yz_beyani.md` içinde. Referanslar'dan önce gelir.

### Referanslar
IEEE biçimi, metinde geçiş sırasına göre numaralı. En az üç, genelde beş ile on kaynak; her kaynak metinde en az bir kez anılır ([n]). Yalnız öğrencinin okuduğu ve doğrulanabilen kaynaklar. Künye kalıpları:

- Dergi: `A. Yazar, B. Yazar ve C. Yazar, "Makale başlığı," Dergi Adı, c. 12, sayı 3, s. 45–67, Mart 2024, doi: 10.xxxx/yyyyy.`
- Bildiri: `A. Yazar, "Bildiri başlığı," Konferans Adı, Şehir, Ülke, 2023, s. 1–8.`
- Kitap: `A. Yazar, Kitap Adı, 2. bas. Şehir: Yayınevi, 2019, böl. 4.`
- Tez: `A. Yazar, "Tez başlığı," Yüksek lisans tezi, Enstitü, Üniversite, Şehir, 2022.`
- Standart ve rapor: `Kurum, "Rapor başlığı," Rapor no. XX-123, 2021.`
- Web: `Kurum/Yazar, "Sayfa başlığı," Site. Erişim: 9 Ekim 2026. [Çevrimiçi]. URL`

Türkçe bağlaç "ve" kullanılır. DOI varsa yazılır. Doğrulanamayan künyeye `[DOĞRULANACAK]` eklenir; betik bunu çıktıya taşır.

## Denklem ve sembol

Formun metnine denklem gerekiyorsa IEEE düzeni uygulanır: denklem ayrı satırda, Word denklem nesnesiyle yazılır, sağda (1), (2) diye numaralanır ve metinde numarasıyla anılır ("(1)'de görüldüğü gibi"). Denklemden hemen sonra sembollerin tanımı gelir ("burada T itki, ρ hava yoğunluğudur").

- Denklemi `form.md`'de kendi satırında `$$ … $$` arasında LaTeX ile yaz: `$$ C_T = \frac{\sigma a}{4}\left(\frac{2}{3}\theta_0 - \lambda\right) $$`. `form_doldur.py` onu düzenlenebilir Word denklemine çevirir, sütunun ortasına koyar ve sağda (1), (2)… diye sırayla numaralar. Numaraları metinde sen anarsın ("(1)'de"); sırayı denklemlerin formdaki sırası belirler.
- Denklemden sonra küçük harfle süren cümle ("burada …") girintisiz başlar; betik bunu yapar.
- Çeviriyi pandoc yapar (isteğe bağlı). pandoc yoksa ya da LaTeX çevrilemezse betik denklemin yerine `[ÖĞRENCİ TAMAMLAYACAK: denklem (n), Word'de Ekle → Denklem ile: …]` yazar ve uyarır; öğrenciye pandoc'u kurmasını ya da denklemi Word'de kendisinin yazmasını söyle.
- Metin içindeki basit sembol Unicode ile ve gerçek indisle yazılır (vᵢ, Cₗ, θ, ρ, m/s²). Klavye yazımı yok: `x_1`, `x^2`, `a*b`, `sqrt()`, `<=`, `$…$`, `\alpha`. `kontrol.py` bunları bildirir.
- Değişkenler italik, birimler ve fonksiyon adları dik; sayı ile birim arasında boşluk (10 m/s); Türkçe formda ondalık virgül, İngilizce formda nokta.
- Aynı büyüklük formda ve sunumda aynı sembolle gösterilir.

## Sık hatalar (arşivden)

- 2.2'nin 1.1'den kopyalanması.
- Kaynaklarda yayın yeri, cilt, sayfa, yıl eksik; yalnız yazar ve başlık.
- Özetin "bu çalışmada … anlatılacaktır" ile başlayıp hiçbir sonuç söylememesi.
- 1.2'de genel sektör cümleleri; somut platform ve fayda yok.
- Şablondaki Lorem ipsum parçalarının çıktıda kalması (betik yakalar).
- Denklemin klavyeyle yazılması (`v_i`, `x^2`, `int`); Word denklem nesnesi yerine düz metin.

## form.md biçimi (betiğin okuduğu dosya)

Başlıklar aynen bu sırayla ve bu adlarla. 1.2 başlığı program adına göre değiştirilebilir; "Tezin … ile İlişkisi" kalıbı korunur.

```markdown
# Seminer Başlığı

## Yazar
Ad Soyad
Program adı
İTÜ Havacılık Enstitüsü
İstanbul, Türkiye
eposta@itu.edu.tr

## Özet
Tek paragraf.

## Anahtar Kelimeler
terim1, terim2, terim3

## Tez Çalışması Durumu
Paragraf 1.

Paragraf 2.

## Tezin Savunma Teknolojileri ile İlişkisi
Paragraf.

## Seminer Konusu
Paragraf.

## Seminer – Tez İlişkisi
Paragraf.

## Teşekkür
(İsteğe bağlı; yoksa başlık da yazılmaz.)

## Yapay Zekâ Kullanım Beyanı
Paragraf.

## Referanslar
[1] A. Yazar, "…," Dergi, c. 1, s. 1–10, 2024, doi: …
[2] …
```

İngilizce formda başlık karşılıkları (betik ikisini de tanır):

| Türkçe | İngilizce |
|---|---|
| `## Yazar` | `## Author` |
| `## Özet` | `## Abstract` |
| `## Anahtar Kelimeler` | `## Keywords` |
| `## Tez Çalışması Durumu` | `## Thesis Status` |
| `## Tezin … ile İlişkisi` | `## Relation of the Thesis to …` |
| `## Seminer Konusu` | `## Seminar Topic` |
| `## Seminer – Tez İlişkisi` | `## Seminar–Thesis Relation` |
| `## Teşekkür` | `## Acknowledgements` |
| `## Yapay Zekâ Kullanım Beyanı` | `## Declaration of AI Use` |
| `## Referanslar` | `## References` |

Yazar bloğunda kurum satırı İngilizce formda "ITU Aviation Institute", şehir "Istanbul, Türkiye". Ana başlıklar (Thesis Work, Seminar) ve etiketler (Abstract—, Keywords—) betikçe yazılır.
