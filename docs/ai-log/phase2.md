# Faz 2 — AI Kullanım Günlüğü

## AI'a Sorduğum Soru (Prompt)

"Adapter pattern burada uygun mu, yoksa Facade mı?
Sepetim, indirim factory ve dekoratörlerim var, bunları
tek yerden yönetmek istiyorum. Farkını açıkla."

## AI'ın Cevabı (Özet)

AI, Adapter Pattern'in iki uyumsuz arayüzü birbirine bağlamak için
kullanıldığını, bende zaten uyumlu sınıflar olduğu için Adapter'ın
gerekmediğini söyledi. Facade Pattern'in ise var olan karmaşık bir
sistemi basit bir arayüzle örtmek için kullanıldığını, bu yüzden
benim durumuma Facade'ın daha uygun olduğunu açıkladı.

## Ben Ne Uyguladım

AI'ın Facade önerisini doğru buldum ve SepetServisi sınıfını yazdım.
Decorator Pattern fikrini ise kendim ekledim. Sepete hediye paketi ve
ekspres kargo eklerken mevcut kodu bozmamak için Decorator kullandım.

## AI'ın Yanlış veya Eksik Önerdiği Şey

AI başta Decorator yerine Sepet sınıfına doğrudan alan eklenmesini
önerdi. Bu Open/Closed Prensibini ihlal ederdi. Decorator Pattern ile
mevcut kodu hiç değiştirmeden yeni özellik eklemenin daha doğru
olduğuna kendim karar verdim.