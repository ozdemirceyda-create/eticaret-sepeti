# Faz 3 — AI Kullanım Günlüğü (Pair Programming Oturumu)

## Oturum Süresi: ~35 dakika

## 1. Hangi Pattern'i Seçeceğimizi Tartıştık (10 dk)

Soru: "Faz 3 için Observer zaten var, ikinci Behavioral pattern
olarak ne önerirsin? State mi, Command mi?"

AI'ın cevabı: Command Pattern'i önerdi çünkü e-ticaret sepetinde
geri alma özelliği gerçek bir ihtiyaç. State Pattern ise sepet
durumları için uygun ama daha karmaşık olurdu.

Karar: Command Pattern seçildi.

## 2. Command Pattern Tasarımını Tartıştık (15 dk)

Soru: "KomutYoneticisi sınıfı hem çalıştırma hem geri alma işini
yapmalı mı, yoksa ayrı sınıflar mı olsun?"

AI'ın cevabı: Tek sınıfta tutmanın daha sade olduğunu söyledi.
Geçmişi stack olarak tutup pop() ile geri almanın yeterli olduğunu
açıkladı.

## 3. OCP'yi Nerede Gösterdiğimizi Tartıştık (10 dk)

Soru: "Bu kodda Open/Closed Prensibi nerede görünüyor? Hocaya
nasıl anlatırım?"

AI'ın cevabı: İki noktada gösterilebileceğini söyledi:
1. Yeni gözlemci eklemek için SepetYayinci'ya dokunmuyoruz
2. Yeni komut eklemek için KomutYoneticisi'na dokunmuyoruz
Sadece yeni sınıf yazıp kaydediyoruz.

## AI Olmadan Ne Kadar Sürerdi?

Observer ve Command Pattern'i sıfırdan araştırıp uygulamak
tahminen 3-4 saat sürerdi. AI ile 35 dakikada tamamlandı.

## AI Bizi Nerede Yanılttı?

AI başta UrunEkleKomutu'nun geri alma metodunda tüm ürün listesini
silip yeniden oluşturmayı önerdi. Bu hatalıydı çünkü aynı isimde
birden fazla ürün olsa hepsini silerdi. Sadece son eklenen ürünü
kaldıracak şekilde kendim düzelttim.