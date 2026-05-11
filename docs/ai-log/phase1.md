# Faz 1 — AI Kullanım Günlüğü

## AI'a Sorduğum Soru (Prompt)

"Sepet sınıfımda indirim hesaplama if-elif zinciriyle yapılıyor.
Bunu Strategy Pattern ile nasıl düzeltirim? Python örneği verir misin?"

## AI'ın Cevabı (Özet)

Her indirim türü için ayrı bir sınıf oluşturmamı önerdi. Hepsinin ortak
bir üst sınıftan (IndirimStrategy) türemesini ve uygula() metodunu
override etmesini söyledi. Sepet sınıfının bu stratejiyi dışarıdan almasını
ve sadece uygula() çağırmasını önerdi.

## Ben Ne Uyguladım

AI'ın önerisini anladıktan sonra kendi elimle yazdım. Ek olarak
IndirimFactory sınıfını ekledim çünkü string ile nesne seçimi hatalıydı.
Bu kısmı AI önermedi, kendim fark ettim.

## AI'ın Önerisinden Farklı Yaptığım Şey

AI direkt Strategy Pattern önerdi ama Factory Pattern fikrini ben ekledim.
String ile indirim seçmenin yazım hatasına yol açabileceğini kendim fark
edip fabrika sınıfı yazmaya karar verdim.