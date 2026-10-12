# Geri bildirim raporu: sorun günlüğü ve kapanış raporu

Bu beceri beta sürümdür; hazırlayana ulaşan tek düzenli bilgi, ajanın her kullanımda yazdığı rapordur. İki dosya:

- `sorunlar.md`: çalışma dosyası; iş boyunca satır eklenir, onay gerektirmez.
- `geri_bildirim.md`: 6. adımda `sorunlar.md`'den yazılan, hazırlayana yönelik rapor. Öğrenci okur, isterse gönderir. Her kullanımda yazılır; sorunsuz geçen kullanım da bilgidir.

## Rapora girmeyenler (kesin)

Tez ya da seminer içeriği, öğrencinin adı ve numarası, danışman adı, belgeler ve alıntıları, kaynak künyeleri, e-posta adresi, kurum dışı iş yeri adı. Örnek verilecekse içerik soyutlanır: "yöntem slaydında beş adımlı süreç" denir, adımların adı yazılmaz. Öğrenci gönderip göndermemekte serbesttir; göndermemesi hiçbir şeyi etkilemez.

## `sorunlar.md` satır biçimi

Her satır bir olay: `adım · tür · ne oldu · ne yapıldı`. Türler:

- `betik`: komut ve hata metninin ilk satırı; hangi sürümde (python, python-docx/python-pptx), hangi ortamda (Claude Code, claude.ai, ChatGPT, Codex).
- `yonerge`: uygulanamayan, çelişen ya da belirsiz kalan kural; hangi dosya ve bölüm.
- `durum`: yönergenin karşılamadığı durum (tez yok, eş danışman, İngilizce ve Türkçe karışık kaynaklar, görsel yok, öğrenci belgesiz geldi).
- `butce`: soru ya da onay bütçesinin aşılması; kaç soru, hangi turda, neden.
- `ogrenci`: öğrencinin takıldığı adım (kurulum, betik, görsel hazırlama, görüşme uzunluğu); yalnız gözlem, yargı yok.
- `calisti`: sorunsuz tamamlanan önemli adım (ör. "deste_kur 20 slayt, uyarı yok").

## `geri_bildirim.md` şablonu

```markdown
# stp596-seminer geri bildirim

Tarih: GG.AA.YYYY · Beceri sürümü: v0.1.1-beta (SKILL.md'deki ya da README'deki sürüm)
Ortam: [Claude Code / claude.ai / ChatGPT / Codex] · Model: [ad] · Betikler çalıştı mı: [evet / kısmen / hayır]
Dil: [tr / en] · Konu türü: [tez / tez konusu + literatür / bitirme-proje] · Tez aşaması: [a–e]

## Sayılar
Görüşme: [n] tur, [n] soru (bütçe 23) · Plan geçişi: [n] soru · Taslak geçişi: [n] soru
Form: [n] sözcük, [n] kaynak · Sunum: [n] içerik slaydı, [n] salt metin, animasyon: [evet/hayır]
kontrol.py: form [n] uyarı, sunum [n] uyarı; bilinçli bırakılanlar: [kısa]

## Betik hataları
- [komut] → [hata metni ilk satır] → [çözüm ya da çözümsüz]

## Yönerge boşlukları ve çelişkiler
- [dosya · bölüm] → [ne eksikti / ne çelişti] → [ajan ne yaptı]

## Karşılanmayan durumlar
- [durum] → [uygulanan çözüm]

## Öğrencinin zorlandığı yer
[Kapanış sorusunun cevabı; cevap verilmediyse "belirtilmedi".]

## Öneriler
- [en çok üç madde; somut: "S9'a 'hangi kütüphane' alt sorusu eklenmeli"]

Bu raporda tez içeriği, ad, numara, belge ve kaynak yoktur; göndermeden önce kontrol edin.
```

## Kapanış sorusu (6. adımda, tek soru, cevap isteğe bağlı)

```
❓ **Geri bildirim**: Bu süreçte sizi en çok ne zorladı? Numarayla seçin; cevap vermek istemezseniz "geç".
  1. Görüşme uzun ya da sorular tekrar etti
  2. Kurulum ya da betiklerin çalıştırılması
  3. Görsel hazırlama ve yeniden çizim
  4. Form metninin alt sınırları
  5. Hiçbiri; başka: …
➡️ Cevabınız rapora yalnız bu başlık altında girer.
```

## Rica metni (teslim notunun sonuna)

> `geri_bildirim.md` hazır; içinde tez içeriğiniz ve adınız yok, okuyup kontrol edin. Dilerseniz dosyayı **alptekin.yildiz@itu.edu.tr** adresine, konu satırı **"stp596-seminer geri bildirim"** olacak şekilde e-postayla gönderin. GitHub hesabınız varsa Issue olarak da açabilirsiniz. Göndermek zorunlu değildir ve dersle ilgili hiçbir şeyi etkilemez; beceri bu raporlarla düzeltilir.
