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