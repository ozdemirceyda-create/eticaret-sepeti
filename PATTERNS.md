# Kullanılan Tasarım Örüntüleri

## FAZ 1 — Creational & Behavioral Örüntüler

### 1. Strategy Pattern

Nerede kullandım: src/indirimler.py — IndirimStrategy sınıfı ve alt sınıfları

Neden kullandım: İndirim hesaplama mantığı Sepet sınıfına gömülüydü. Her yeni indirim için
mevcut kodu değiştirmek gerekiyordu. Strategy Pattern ile her indirim türü kendi sınıfına
taşındı. Sepet sınıfı artık indirim detaylarını bilmek zorunda değil.

Ne kazandım: Yeni bir indirim eklemek için sadece yeni bir sınıf yazmak yeterli.
Mevcut koda dokunmak gerekmiyor. Open/Closed Prensibini sağladım.

Önce: Sepet sınıfı içinde if-elif zinciri
Sonra: Her indirim kendi sınıfında, Sepet sadece uygula() metodunu çağırıyor


### 2. Factory Pattern

Nerede kullandım: src/indirimler.py — IndirimFactory sınıfı

Neden kullandım: İndirim türü string ile seçiliyordu. Yazım hatası yapılınca hata vermeden
yanlış çalışıyordu. Factory Pattern ile string yerine fabrika sınıfı doğru nesneyi üretiyor.
Bilinmeyen bir tür girilince hata fırlatıyor.

Ne kazandım: Nesne yaratma sorumluluğu merkezi bir yere taşındı. Hatalı kullanım artık
sessizce değil, açıkça hata vererek fark ettiriyor.

Önce: sepet.indirim_turu = "yuzde10" şeklinde string atama
Sonra: sepet.indirim_sec("yuzde10") ile IndirimFactory üzerinden nesne alınıyor

## FAZ 2 — Structural Örüntüler

### 3. Decorator Pattern

Nerede kullandım: src/dekoratorler.py — SepetDekorator ve alt sınıfları

Neden kullandım: Sepete hediye paketi veya ekspres kargo eklemek istediğimde
mevcut Sepet sınıfını değiştirmek zorunda kalmak istemedim. Decorator Pattern
ile Sepet nesnesini sarmalayarak üstüne yeni özellik ekledim.

Ne kazandım: Hediye paketi ve ekspres kargo birbirinden bağımsız. İkisini
aynı anda, sadece birini, ya da hiçbirini kullanabiliyorum. Mevcut koda
hiç dokunmadım.

Önce: Sepet sınıfına hediye_paketi ve kargo alanları eklerdim, sınıf şişerdi
Sonra: Her özellik kendi dekoratör sınıfında, Sepet sade kaldı


### 4. Facade Pattern

Nerede kullandım: src/servis.py — SepetServisi sınıfı

Neden kullandım: Sepet, IndirimFactory, Dekoratörler ayrı ayrı sınıflar.
Bunları her seferinde tek tek kullanmak karmaşık. SepetServisi tek bir
arayüz sunuyor, kullanıcı altta ne döndüğünü bilmek zorunda değil.

Ne kazandım: Kullanıcı sadece servis.urun_ekle(), servis.indirim_uygula()
gibi sade metodlar çağırıyor. Sistemin iç karmaşıklığı gizlendi.

Önce: Sepet, Factory, Dekoratör nesnelerini ayrı ayrı yönetmek gerekiyordu
Sonra: Sepet


## FAZ 3 — Behavioral Örüntüler

### 5. Observer Pattern

Nerede kullandım: src/gozlemciler.py — SepetYayinci ve Gozlemci sınıfları

Neden kullandım: Sepete ürün eklendiğinde veya sipariş tamamlandığında
stok, bildirim ve log servislerinin haberdar olması gerekiyordu. Hepsini
tek tek çağırmak yerine Observer Pattern ile yayıncı-abone sistemi kurdum.

Ne kazandım: Yeni bir servis eklemek için sadece yeni bir Gozlemci sınıfı
yazıp kaydetmek yeterli. Mevcut koda hiç dokunmuyorum. OCP sağlandı.

Önce: servis.urun_ekle() içinde stok.guncelle(), bildirim.guncelle() tek tek çağrılırdı
Sonra: yayinci.bildir() hepsini otomatik haberdar ediyor


### 6. Command Pattern

Nerede kullandım: src/komutlar.py — Komut sınıfı ve KomutYoneticisi

Neden kullandım: Sepete ürün ekleme ve indirim uygulama işlemlerini geri
alabilmek istedim. Command Pattern ile her işlem bir nesneye dönüştü,
KomutYoneticisi geçmişi tutarak geri alma özelliği sağladı.

Ne kazandım: Yeni bir işlem eklemek için sadece yeni bir Komut sınıfı
yazmak yeterli. Geri alma özelliği tüm komutlarda otomatik çalışıyor.

Önce: İşlemleri geri almak mümkün değildi
Sonra: son_islemi_geri_al() ile son komut geri alınabiliyor