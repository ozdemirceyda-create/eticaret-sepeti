from indirimler import IndirimFactory

class Sepet:
    def __init__(self):
        self.urunler = []
        self.indirim = None

    def urun_ekle(self, urun_adi, fiyat, adet):
        self.urunler.append({"ad": urun_adi, "fiyat": fiyat, "adet": adet})

    def indirim_sec(self, indirim_turu):
 
        self.indirim = IndirimFactory.olustur(indirim_turu)

    def toplam_hesapla(self):
        toplam = sum(u["fiyat"] * u["adet"] for u in self.urunler)
        if self.indirim:
            toplam = self.indirim.uygula(toplam, self.urunler)
        return toplam

    def sepeti_yazdir(self):
        print("=== SEPET ===")
        for urun in self.urunler:
            print(f"{urun['ad']} x{urun['adet']} = {urun['fiyat'] * urun['adet']} TL")
        print(f"TOPLAM: {self.toplam_hesapla()} TL")

sepet = Sepet()
sepet.urun_ekle("Laptop", 15000, 1)
sepet.urun_ekle("Mouse", 500, 2)
sepet.urun_ekle("Klavye", 300, 1)
sepet.indirim_sec("yuzde10")
sepet.sepeti_yazdir()