# Helikopter rotor konsept tasarımı için genetik algoritma: problem tanımı ve yöntem planı

## Yazar
Ad SOYAD
Savunma Teknolojileri Yüksek Lisans Programı
İTÜ Havacılık Enstitüsü
İstanbul, Türkiye
ad.soyad@itu.edu.tr

## Özet
Helikopter ana rotorunun konsept tasarımı, birbirine bağlı çok sayıda değişkenin çoğunlukla deneyime dayalı ve iteratif olarak belirlendiği bir süreçtir; bir değişken değiştiğinde hesaplar baştan yapılır. Tez çalışması, pal elemanı momentum teorisine (BEMT) dayalı bir askı performans modeli ile genetik algoritmayı birleştirerek, verilen görev gereksinimleri için beş konsept tasarım değişkenini (rotor yarıçapı, veter, pal sayısı, uç hızı ve burulma) askı gücü ve rotor kütlesi açısından en iyileyen bir yöntem geliştirmeyi amaçlamaktadır. Tasarım değişkenleri ve aralıkları literatürden belirlenmiş, pal profili NACA 0012 olarak sabit tutulmuştur. Askı performans modeli Python ortamında yazılmış ve çalışır durumdadır; genetik algoritma hazır bir kütüphane ile modele bağlanacak, sonuçlar açık literatürde yer alan Westland Lynx rotoru ile karşılaştırılarak doğrulanacaktır. Çalışma tez önerisi sonrasındaki yöntem kurma aşamasındadır ve henüz sayısal sonuç üretilmemiştir; beklenen çıktı, görev gereksiniminden rotor değişkenlerine sistematik olarak ulaşan ve konsept tasarım döngüsünü kısaltan açık bir iş akışıdır. Seminerde problemin tanımı, tasarım değişkeni uzayı, ilgili literatürün yöntem ve bulgularının toplu özeti, planlanan BEMT–genetik algoritma iş akışı, amaç fonksiyonu ve kısıtlar, doğrulama stratejisi ile çalışmanın bugünkü durumu ve sınırlılıkları sunulacaktır.

## Anahtar Kelimeler
genetik algoritma, rotor konsept tasarımı, pal elemanı momentum teorisi, askı performansı, helikopter, tasarım optimizasyonu

## Tez Çalışması Durumu
Tez başlığı "Genetik Algoritma Optimizasyonu ile Helikopter Rotor Konsept Tasarımı" olup danışmanı Doç. Dr. Ayşe Kaya [kurgusal]'dır. Tez önerisi Mayıs 2026'da verilmiştir. Çalışma, helikopter ana rotorunun konsept tasarımında genetik algoritma [1] ile desteklenen bir boyutlandırma yöntemi geliştirmeyi amaçlamaktadır. Şimdiye kadar literatür taraması yapılmış; beş tasarım değişkeni (yarıçap 5,5–7,0 m, veter 0,25–0,45 m, pal sayısı 2–5, uç hızı 190–220 m/s, burulma −6 ile −14°) ve aralıkları literatürden [2]–[4] belirlenmiş; pal elemanı momentum teorisine dayalı askı performans modeli Python ortamında yazılmış ve askı gücü hesabı çalışır hâle getirilmiştir. İleri uçuş performans modeli henüz yazılmamış, genetik algoritma modele bağlanmamış ve sayısal sonuç üretilmemiştir. Amaç fonksiyonu, askı gücü ve rotor kütlesi birlikte ele alınarak ağırlıklı tek fonksiyon ya da çok hedefli biçimde değerlendirilecek; biçimi danışmanla belirlenecektir. Tezden çıkmış yayın ya da bildiri yoktur.

Önümüzdeki dönemde sırasıyla genetik algoritmanın hazır bir kütüphane (DEAP ya da pymoo) ile modele bağlanması, modelin Westland Lynx rotoru verileriyle doğrulanması ve zaman kalırsa ileri uçuş modelinin eklenmesi planlanmaktadır. Yazar bir savunma sanayii kuruluşunda döner kanat tasarım alanında çalışmaktadır; gizlilik nedeniyle çalışmada şirket verisi kullanılmamakta, yalnızca açık literatürdeki veriler kullanılmaktadır.

## Tezin Savunma Teknolojileri ile İlişkisi
Türkiye'de Gökbey gibi yerli döner kanatlı platform programları yürütülmektedir. Bu programlarda ana rotor, platformun kaldırma kuvvetini üreten ve performansını belirleyen alt sistemdir; konsept aşamasında rotor boyutlandırması bugün büyük ölçüde deneyime ve elle yürütülen iterasyonlara dayanmaktadır. Bir değişkenin değişmesi diğer bütün hesapların yinelenmesini gerektirdiğinden, konsept tasarım döngüsü uzun sürmektedir.

Tezde geliştirilecek araç, görev gereksiniminden (azami ağırlık ve buna bağlı itki ihtiyacı) hareketle rotor konsept değişkenlerini sistematik olarak tarayacak ve belirlenen amaç fonksiyonuna göre aday tasarımlar üretecektir. Beklenen fayda, konsept tasarım döngüsünün kısalması ve tasarım uzayının elle iterasyonla ulaşılamayan bölgelerinin de değerlendirilebilmesidir; bu kazancın büyüklüğü henüz ölçülmediğinden sayısal bir iddia ileri sürülmemektedir. Araç açık literatür verisiyle doğrulanacağından, geliştirilen iş akışı gizlilik kısıtı olmadan paylaşılabilecek ve yerli helikopter programlarının konsept tasarım ekipleri tarafından kendi verileriyle kullanılabilecektir.

## Seminer Konusu
Seminerde önce problem tanımlanacaktır: helikopter ana rotorunun konsept tasarımında hangi değişkenlerin söz konusu olduğu, bu değişkenlerin birbirine nasıl bağlı olduğu ve klasik konsept boyutlandırma yaklaşımının nasıl ilerlediği [2], [3] anlatılacak; Westland Lynx rotorunun klasik yöntemle konsept tasarımını ele alan çalışma [4] doğrulama referansı olarak tanıtılacaktır. Tez için belirlenen beş tasarım değişkeni ve literatürden derlenen aralıkları bir grafikle gösterilecektir.

İkinci bölümde genetik algoritmanın işleyişi (popülasyon, uygunluk değerlendirmesi, seçilim, çaprazlama, mutasyon ve yeni nesil döngüsü) ile mühendislik tasarım problemlerindeki kullanımı derleme çalışmasına [1] ve danışmanın önerdiği rotor konsept tasarımı bildirisine [5] dayanarak toplu olarak özetlenecek; kaynaklar tek tek gezilmeyecek, yöntemleri ve bulguları ilgili başlık altında birlikte verilecektir. Bu bölüm, hızlı bir BEMT modeliyle az değişkenli bir genetik algoritma döngüsünü konsept aşamasında kuran açık çalışmaların sınırlı olduğu gözlemiyle, yani araştırma boşluğuyla kapanacaktır.

Üçüncü ve en uzun bölüm yöntem planıdır: BEMT–genetik algoritma iş akışı, askı performans modelinin varsayımları, tasarım değişkenlerinin kromozom olarak kodlanması, amaç fonksiyonu adayları ve kısıtlar (uç hızı aralığı üzerinden dolaylı uç Mach sınırı, pal yüklemesine üst sınır, görev ağırlığından gelen itki ihtiyacı), genetik algoritma ayarları ve kütüphane seçimi, Lynx rotoruyla doğrulama stratejisi ile çalışmanın bugünkü durumu ve takvimi anlatılacaktır. Sınırlılıklar (ileri uçuş modelinin bulunmaması, BEMT'in yüksek yüklemedeki sınırları, dinamik tutunma kaybı ve pal elastikliğinin modellenmemesi, genetik algoritmanın küresel en iyiyi garanti etmemesi, deneysel verinin olmaması) yazar tarafından açıkça belirtilecektir. Sunum, dinleyenin götüreceği üç noktayı özetleyen tek bir sonuç slaydıyla bitecektir.

Askı performans modelinin temeli momentum teorisidir; askı itkisi (1) ile indüklenmiş hıza bağlanır [2]:

$$T = 2 \rho A v_i^2$$

burada T itki, ρ hava yoğunluğu, A rotor disk alanı, vᵢ indüklenmiş hızdır. Pal elemanı teorisi aynı itkiyi kesit kesit hesaplar; iki yaklaşımın birleşimi modelin askı gücünü verir.

## Seminer – Tez İlişkisi
Seminer, tezin "problemin tanımlanması ve yöntem planı" parçasını kapsamaktadır; tezin ilk döneminde yapılan literatür taraması, tasarım değişkeni uzayının kurulması ve askı performans modelinin yazılması bu kapsamın içindedir. Tezin sayısal sonuçları henüz bulunmadığından seminerde bulgu sunulmayacak; askı modelinin deneme amaçlı çalıştırılmasından elde edilen tek değer doğrulanmadığı için gösterilmeyecektir. İleri uçuş performans modeli henüz yazılmadığından kapsam dışıdır. Seminerin tez açısından beklenen katkısı, amaç fonksiyonunun biçimi ve kısıtların seçimi konusunda dinleyicilerden geri bildirim almak ve yöntemin genetik algoritmaya bağlanmadan önce dışarıdan değerlendirilmesidir.

## Yapay Zekâ Kullanım Beyanı
Bu formun ve seminer sunumunun hazırlanmasında Claude (Anthropic) kullanılmıştır. Araç, yazarla yapılan soru-cevap görüşmesiyle içeriğin yapılandırılması, metinlerin dil ve biçim yönünden düzenlenmesi, kaynak künyelerinin IEEE biçimine getirilmesi ve Crossref üzerinden doğrulanması, form ve sunum şablonlarının doldurulması, yazarın belirlediği değerlerle tasarım değişkenleri grafiğinin yeniden çizilmesi ve yazarın tarifine göre üç şemanın (genetik algoritma döngüsü, BEMT–genetik algoritma iş akışı, pal elemanı kesiti) çizilmesi için kullanılmıştır. Tez kodunun yazımı sırasında hata ayıklama amacıyla zaman zaman ChatGPT'ye (OpenAI) danışılmıştır; kod yazar tarafından yazılmıştır. Tez çalışmasına ait yöntem, veri, analiz ve yorumlar ile kaynakların seçimi yazara aittir; araçlar bu amaçla kullanılmamıştır. Metnin doğruluğundan ve kaynakların uygunluğundan yazar sorumludur.

## Referanslar
[1] S. Katoch, S. S. Chauhan ve V. Kumar, "A review on genetic algorithm: past, present, and future," Multimedia Tools and Applications, c. 80, sayı 5, s. 8091–8126, 2021, doi: 10.1007/s11042-020-10139-6.
[2] J. G. Leishman, Principles of Helicopter Aerodynamics, 2. bas. Cambridge, U.K.: Cambridge Univ. Press, 2006.
[3] W. Johnson, Rotorcraft Aeromechanics. Cambridge, U.K.: Cambridge Univ. Press, 2013, doi: 10.1017/CBO9781139235655.
[4] D. Novak, T. Bucak ve A. Domitrović, "Helicopter main rotor conceptual design: application to a Westland Lynx helicopter," Promet – Traffic & Transportation, c. [DOĞRULANACAK: cilt], sayı [DOĞRULANACAK], s. [DOĞRULANACAK], 2008.
[5] [DOĞRULANACAK: AHS Forum bildirisi, 2011].
