# Animasyon: ne zaman, nasıl

## Ne zaman

Animasyon yalnız **akıl yürütmeyi adım adım açmak** için: yöntem akışının kutuları sırayla, bir grafiğe eklenen eğri, karşılaştırmada önce A sonra B, bir soru ve ardından cevabı. Üç dört slaytı geçmesin. Şunlar için kullanılmaz: maddelerin tek tek uçması, geçiş efektleri, ses, süs. Kalabalık slaydı animasyonla "kurtarma": slaydı böl.

Kullanıcı deste üretildikten sonra PowerPoint'te kendi animasyonunu ekleyebilir; bu da geçerli bir yol. Aşağısı betikle eklemek içindir.

## Nasıl

pptxgenjs ve python-pptx animasyon yazamaz; animasyon slayt XML'indeki `<p:timing>` bloğudur. `scripts/anim.py` bu bloğu bir tıklama senaryosundan üretir ve dosyaya enjekte eder.

1. `sunum.md` içinde gövdeyi `~~~` ile böl; betik grupları `govde1`, `govde2`, `govde3` adlı kutulara koyar. `uc_gorsel` slaydında görseller `gorsel1..3`, alt yazılar `altyazi1..3`, `sayilar` slaydında `sayi1..3` adını alır.
2. `deste_kur.py`, `~~~` kullanılan slaytlar için otomatik bir `anim.json` yazar (her grup bir tıklama). Elle düzenlemek istersen biçim:

```json
{
  "7": [ [ {"name": "govde2"} ], [ {"name": "govde3"} ] ],
  "9": [ [ {"name": "gorsel1"}, {"name": "altyazi1"} ],
         [ {"name": "gorsel2"}, {"name": "altyazi2"} ],
         [ {"name": "gorsel3"}, {"name": "altyazi3"} ] ]
}
```

Anahtar slaydın dosya sırası (1'den), değer tıklama adımları. Adımın ilk öğesi tıklamayla, kalanları onunla birlikte gelir. Seçenekler: `"fx": "fade" | "appear" | "wipe"`, `"dir": "in" | "out"`. Varsayılan solarak giriş, 0,5 s.

3. Çalıştır: `python3 scripts/anim.py <deste.pptx> anim.json` (dosyayı yerinde günceller; önce kopyasını al).
4. PowerPoint'te aç, Animasyon Bölmesi'ne bak; slayt gösterisinde tıklayarak dene.

## Tuzaklar

- Aynı ad slaytta iki şekle verilmişse ikisi birden hedeflenir; adlar betikte benzersizdir.
- PDF ya da görüntü dönüşümü animasyonu göstermez; son hâli çizer. Tıklama sırasını görmek için PowerPoint gerekir.
- Giriş efekti alan şekil, animasyon çalışana kadar gizlidir; slaytta sabit duran metin tıklamayla gelecek cevabı önceden söylememeli.
- `anim.py` eski `<p:timing>` bloğunu siler; PowerPoint'te elle eklenmiş animasyon varsa betiği o dosyada çalıştırma.

## Betiksiz yol

`anim.py` çalıştırılamıyorsa ya da animasyon başka bir araçla yazılacaksa `references/animasyon_xml.md` dosyasını oku: `<p:timing>` bloğunun tam iskeleti, efekt kodları, spid eşleme ve tuzaklar orada.
