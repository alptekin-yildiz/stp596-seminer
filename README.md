# stp596-seminer

![Beta](https://img.shields.io/badge/s%C3%BCr%C3%BCm-v0.1.0--beta-orange) ![Lisans: MIT](https://img.shields.io/badge/lisans-MIT-blue)

İTÜ Havacılık Enstitüsü **STP 596 Bilimsel Araştırma, Etik ve Seminer** dersinde seminer **bilgilendirme formunu** ve **40 dakikalık seminer sunumunu** bir yapay zekâ ajanıyla hazırlamak için bir **ajan becerisi** (agent skill). Ajan önce sizinle görüşür, sonra formu ve sunumu dersin şablonlarıyla kurar. İçerik sizin; ajan düzenler, biçime sokar, kuralları denetler.

> **About (English).** A personal, beta-stage agent skill for preparing the seminar information form and the 40-minute seminar presentation of the STP 596 course at the ITU Aviation Institute. It is not official course material and its use is optional; the interview runs in your language and the outputs can be produced in Turkish or English. Every output of an AI tool must be verified by the student, who remains solely responsible for content, sources and course requirements. Code and documentation are under the MIT License without warranty; the templates and the ITU logo in `assets/` are excluded from the licence and may be used only within the course. See [Disclaimer](#sorumluluk-reddi-ve-kullanım-koşulları).

> ⚠️ **Lütfen önce okuyun.** Bu beceri **beta** sürümdür, dersin resmî materyali değildir ve kullanımı **zorunlu değildir**. Ajanın yazdığı her cümleyi, her kaynağı ve her görseli teslimden önce siz doğrularsınız; sorumluluk sizindir. Ayrıntı: [Sorumluluk reddi ve kullanım koşulları](#sorumluluk-reddi-ve-kullanım-koşulları).

## Ne üretir

| Çıktı | Biçim | Kural |
|---|---|---|
| Bilgilendirme formu | A4, IEEE bildiri düzeni, iki sütun, Word (`stp596_bilgilendirme_form.docx` şablonu) | Sunumdan önceki Cuma akşamına kadar ödev olarak yüklenir; 2–3 sayfa |
| Seminer sunumu | 16:9 PowerPoint (`sunum_format_16x9.pptx` şablonu) | 40 dk (~30 + 10 soru); 15–20 içerik slaydı; on başlık; Teşekkürler ve Kaynaklar zorunlu |

İkisinde de yapay zekâ kullanımı beyan edilir; ajan beyanı sizin cevaplarınızdan yazar.

## Kurulum

Gereken: Python 3.9+ ve `pip install python-docx python-pptx` (ajan betikleri çalıştırır; yalnız sohbet ortamında betik olmadan da çalışır, bkz. aşağıda).

**Claude Code (terminal, masaüstü uygulaması ya da VS Code eklentisi)**
1. Sağ üstte **Code → Download ZIP** ile indirin, klasörü `~/.claude/skills/stp596-seminer/` olarak çıkarın (proje içinde `.claude/skills/stp596-seminer/` de olur). Alternatif: `git clone https://github.com/alptekin-yildiz/stp596-seminer ~/.claude/skills/stp596-seminer`
2. Yeni oturumda "STP 596 seminer sunumumu hazırlayalım" yazın ya da `/stp596-seminer` komutunu kullanın.

**claude.ai (web)**
- Planınız özel beceri yüklemeyi destekliyorsa: **Settings → Capabilities → Skills** altından sürüm sayfasındaki ([Releases](https://github.com/alptekin-yildiz/stp596-seminer/releases)) `stp596-seminer.zip` dosyasını yükleyin; sohbette "STP 596 seminer" demeniz yeter.
- Desteklemiyorsa: bir **Project** açın, `SKILL.md` içeriğini proje yönergesi olarak yapıştırın, `references/`, `assets/` ve `scripts/` dosyalarını projeye yükleyin.

**Codex CLI ve SKILL.md okuyan diğer ajanlar**
Aynı klasörü ajanın beceri dizinine koyun (Codex: `~/.codex/skills/`). Biçim Agent Skills standardıdır.

**ChatGPT (Projects)**
Yeni bir Proje açın; `SKILL.md` içeriğini proje yönergesi yapın; `references/`, `assets/`, `scripts/` dosyalarını yükleyin. Betikler ChatGPT'nin Python ortamında çalışır; çalışmazsa ajan formu bölüm bölüm, sunumu slayt slayt metin olarak verir ve siz şablona aktarırsınız.

## Nasıl çalışır

1. **Belgeler:** tez önerinizi, raporlarınızı, grafiklerinizi, kaynak listenizi ajana verirsiniz; ajan okur, bildiğini sormaz. Gizli ya da sözleşmeli veriyi yüklemeden önce danışmanınıza danışın.
2. **Görüşme:** 3 tur, en çok 23 soru; her soruda ajanın önerili cevabı vardır, "evet" deyip geçebilirsiniz. Zayıf cevaplarda ("sınırlılık yok", ölçülmemiş sayı, doğrulanmamış kaynak) ajan ısrar eder. Konu tezinizdir; tez yoksa önce bu sorgulanır.
3. **Plan:** form bölümleri ve slayt slayt iddia–kanıt planı; en çok 4 çoklu-öneri sorusu (başlıklar, görseller, kalıplar, savunulamayacak noktalar).
4. **Form:** metni gösterir, onayınızla `.docx` üretir. Alt sınırlar var: metin ≥ 850 sözcük, ≥ 5 kaynak.
5. **Sunum:** slayt metinleri, kalıplar (tablo, süreç, karşılaştırma, kart, zaman çizelgesi), isteğe bağlı tıklama animasyonu; onayınızla `.pptx` üretir.
6. **Kontrol ve teslim notu:** `kontrol.py` dersin kurallarını makineyle denetler; ajan kalan maddeleri sizinle geçer.

Ajan kaynak uydurmaz, bulgu eklemez; kendi eklediği standart alan bilgisini işaretler ve sahiplenmediğinizi siler. Boşluklar `[ÖĞRENCİ TAMAMLAYACAK]` ile kalır; bunlar silinmeden teslim edilmez.

## Dil

Görüşme sizin yazdığınız dilde yürür. Form ve sunum **Türkçe** (varsayılan) ya da **İngilizce** olabilir; ajan ilk turda sorar. İngilizce çıktıda şablonların sabit metinleri (başlıklar, etiketler, altbilgi, "Acknowledgements") betiklerce çevrilir.

## Elle kullanım (ajan olmadan)

```bash
python3 scripts/form_doldur.py form.md --sablon assets/stp596_bilgilendirme_form.docx \
        --cikti 514xxxxxx_Soyad_stp596_bilgilendirme_form.docx --tarih 02.12.2026      # İngilizce: --dil en
python3 scripts/deste_kur.py sunum.md --sablon assets/sunum_format_16x9.pptx \
        --cikti 514xxxxxx_Soyad_stp596_sunum.pptx                                       # İngilizce: ön bilgide dil: en
python3 scripts/anim.py 514xxxxxx_Soyad_stp596_sunum.pptx anim.json                     # isteğe bağlı tıklama animasyonu
python3 scripts/kontrol.py 514xxxxxx_Soyad_stp596_bilgilendirme_form.docx 514xxxxxx_Soyad_stp596_sunum.pptx
```

`form.md` ve `sunum.md` biçimleri `references/form.md` ve `references/sunum.md` sonunda; çalışan örnekler `ornek/` altında.

## Dersin kuralları (kısa)

| Konu | Kural |
|---|---|
| Konu | Tez çalışması; olgunlaşmadıysa tez konusu + literatür; en son bitirme/proje |
| Form | Sunumdan önceki Cuma akşamına kadar yüklenir; yoksa sunum yapılamaz |
| Süre | 40 dk: ~30 dk sunum + 10 dk soru-cevap; slayt başına 1,5–2 dk |
| Başlıklar | Başlık Sayfası · İçindekiler · Giriş · Literatür Taraması · Araştırma Yöntemi · Bulgular · Tartışma · Sonuçlar · Teşekkürler · Kaynaklar |
| Beyan | Yapay zekâ kullanımı formda ve sunumda yazılır |

Bu tablo ders yönergesinin özetidir; çelişki hâlinde ders yönergesi ve öğretim üyesinin açıklaması geçerlidir.

## Depo yapısı

```
stp596-seminer/
├── SKILL.md              ajanın okuduğu ana yönerge (Agent Skills biçimi)
├── references/           görüşme ağacı, form ve sunum kuralları, animasyon, yapay zekâ beyanı, geri bildirim raporu
├── assets/               stp596_bilgilendirme_form.docx, sunum_format_16x9.pptx
├── scripts/              form_doldur.py, deste_kur.py, anim.py, kontrol.py (yalnız Python)
└── ornek/                anonim girdi örnekleri (Türkçe ve İngilizce)
```

## Geri bildirim ve katkı

Ajan her kullanımın sonunda hazırlayana yönelik bir `geri_bildirim.md` raporu yazar: ortam, sayılar, betik hataları, yönerge boşlukları, sizi zorlayan adım. Raporda tez içeriğiniz, adınız ve belgeleriniz yoktur; okuyup kontrol edin. Dilerseniz **alptekin.yildiz@itu.edu.tr** adresine, konu satırı **"stp596-seminer geri bildirim"** olacak şekilde gönderin. Göndermek zorunlu değildir ve dersle ilgili hiçbir şeyi etkilemez; beceri bu raporlarla düzeltilir.

Hata ve öneriler için ayrıca [Issues](https://github.com/alptekin-yildiz/stp596-seminer/issues). Küçük düzeltmeler doğrudan pull request olabilir; büyük değişiklik için önce bir Issue açın.

## Sorumluluk reddi ve kullanım koşulları

Bu depo kişisel bir çalışmadır; İTÜ Havacılık Enstitüsü'nün ya da STP 596 dersinin resmî materyali değildir ve kurumu bağlamaz. Beceri **beta** sürümdedir; hatalı ya da eksik davranabilir, önceden bildirilmeden değişebilir.

Kullanımı **zorunlu değildir**; dersin form ve sunum şablonlarını hazırlamayı kolaylaştırmaya yönelik bir öneridir. Dersin bütün yükümlülükleri (içerik, teslim tarihi, biçim, süre, akademik dürüstlük) öğrenciye aittir. Bu depodaki yönerge ile ders yönergesi ya da öğretim üyesinin açıklaması çelişirse ders yönergesi geçerlidir.

Yapay zekâ araçlarının ürettiği her metin, kaynak ve görsel teslimden önce öğrenci tarafından doğrulanmalıdır. Uydurma kaynak, doğrulanmamış veri ya da başkasına ait metin, aracın değil öğrencinin sorumluluğundadır (YÖK Bilimsel Araştırma ve Yayın Etiği Yönergesi). Beceri bir not, kabul ya da başarı vaat etmez.

Üçüncü taraf yapay zekâ hizmetleri kendi kullanım koşulları, gizlilik politikaları ve ücretleriyle çalışır; hangi hizmetin kullanılacağı ve hangi verinin yükleneceği öğrencinin kararıdır. Gizli, sözleşmeli ya da yayımlanmamış tez verisini bu hizmetlere yüklemeden önce danışmanınıza danışın.

Yazılım ve belgeler MIT lisansıyla, "olduğu gibi" ve açık ya da örtük hiçbir garanti olmaksızın sunulur; kullanımından doğan hiçbir zarardan hazırlayan sorumlu tutulamaz (bkz. [LICENSE](LICENSE)). `assets/` altındaki şablonlar ve İTÜ logosu MIT kapsamı dışındadır; yalnız STP 596 dersi kapsamında kullanılır, başka amaçla kullanılamaz ve dağıtılamaz.

## Lisans, hazırlayan, yapay zekâ beyanı

- Lisans: [MIT](LICENSE); şablonlar ve logo için istisna LICENSE dosyasının sonundadır.
- Hazırlayan: Doç. Dr. Alptekin Yıldız, İTÜ Havacılık Enstitüsü.
- Bu beceri hazırlanırken Claude Code (Anthropic) yardımcı araç olarak kullanılmıştır. Yönergeler ve betikler hazırlayan tarafından yazılmış, gözden geçirilmiş ve denenmiştir; sorumluluk hazırlayana aittir.
