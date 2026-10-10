# Örnekler

Bu klasördeki dosyalar betiklerin **girdi biçimini** gösterir; içerik bir denemeden alınmış, adlar ve kurumlar anonimleştirilmiştir. Danışman adı kurgusaldır. Örnekleri kopyalayıp teslim etmeyin; form ve sunum kendi görüşmenizden yazılır.

| Dosya | Ne gösterir |
|---|---|
| `tr/form.md` | İki sayfalık Türkçe form girdisi (bütün bölümler, 5 kaynak, yapay zekâ beyanı) |
| `tr/sunum.md` + `tr/gorseller/` | 20 slaytlık Türkçe deste: kalıplar (tablo, süreç, karşılaştırma, kart, zaman), katmanlı görseller, konuşma notları |
| `tr/seminer.json` | Görüşme çıktısı |
| `en/form.md` | İngilizce form girdisi (başlıklar İngilizce; betik dili otomatik anlar) |
| `en/sunum.md` | Kısa İngilizce deste örneği (`dil: en`; yalnız biçim için, 15–20 içerik slaydı kuralını sağlamaz) |

Çalıştırma (depo kökünden):

```bash
python3 scripts/form_doldur.py ornek/tr/form.md --sablon assets/stp596_bilgilendirme_form.docx --cikti /tmp/ornek_form.docx --tarih 02.12.2026
python3 scripts/deste_kur.py ornek/tr/sunum.md --sablon assets/sunum_format_16x9.pptx --cikti /tmp/ornek_sunum.pptx
python3 scripts/kontrol.py /tmp/ornek_form.docx /tmp/ornek_sunum.pptx
```

*English:* these files show the **input format** of the scripts; names and institutions are anonymised and the advisor is fictional. Do not copy them into your own submission. `en/form.md` and `en/sunum.md` are the English examples.
