# Başlangıç Kodunun Sorunları

## Tespit Ettiğim Sorunlar

1. İndirim mantığı Sepet sınıfına gömülü
   - Yeni bir indirim eklemek için Sepet sınıfını değiştirmek gerekiyor. Bu Open/Closed Prensibini ihlal ediyor.

2. Uzayan if-elif zinciri
   - Her yeni indirim türü için bir elif daha ekleniyor. 10 indirim türü olsa kod okunmaz hale gelir.

3. İndirim nesnesi yok
   - İndirimler string ile temsil ediliyor. Yazım hatası yapılırsa hata çıkmaz, sessizce yanlış çalışır.

4. Test edilemez yapı
   - İndirim mantığını ayrı test etmek mümkün değil, her şey Sepet sınıfı içinde iç içe geçmiş durumda.

5. Kargo ücreti eksik
   - kargo_bedava dalı hiçbir şey hesaplamıyor, kargo ücreti zaten sisteme hiç eklenmemiş.

## AI'ın Gördükleri (Claude)

Soru: Bu kodda hangi tasarım sorunlarını görüyorsun? Hangi tasarım örüntüleri bu sorunları çözebilir?

AI'ın Cevabı (Özet):

Sepet sınıfı hem ürün yönetimi hem de indirim hesaplama işini yapıyor. Bu Tek Sorumluluk Prensibini (SRP) ihlal ediyor. Her sınıfın tek bir görevi olmalı.

if-elif zinciri Strategy Pattern ile çözülebilir. Her indirim türü ayrı bir sınıf olur, Sepet hangisini kullanacağını bilmek zorunda kalmaz.

Yeni indirim eklemek mevcut kodu kırabiliyor. Bu Open/Closed Prensibine aykırı. Strategy Pattern bunu da çözer.

İndirim string ile seçiliyor. Bu Factory Pattern ile düzeltilebilir. String yerine doğru indirim nesnesini üretecek bir fabrika sınıfı yazılır.

Kargo mantığı eksik ve belirsiz, ayrı bir sınıfa taşınmalı.

## Karşılaştırma: Ben vs AI

if-elif zinciri büyüyor: İkimiz de gördük.
İndirim Sepet'e gömülü: İkimiz de gördük.
String ile tip temsili hatalı: İkimiz de gördük.
Test edilemez yapı: İkimiz de gördük.
Kargo eksik: İkimiz de gördük.
SRP ihlali (ek detay): Sadece AI gördü.
Factory Pattern önerisi: Sadece AI gördü.

Değerlendirme: Temel sorunları ben de yakaladım. AI ek olarak SRP ihlaline dikkat çekti ve çözüm olarak hem Strategy hem de Factory Pattern önerdi. Bu iki örüntüyü Faz 1 ve Faz 2 de uygulayacağım.