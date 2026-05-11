

class Sepet:
    def __init__(self):
        self.urunler = []
        self.indirim_turu = None  

    def urun_ekle(self, urun_adi, fiyat, adet):
        self.urunler.append({"ad": urun_adi, "fiyat": fiyat, "adet": adet})

    def toplam_hesapla(self):
        toplam = 0
        for urun in self.urunler:
            toplam += urun["fiyat"] * urun["adet"]

        if self.indirim_turu == "yuzde10":
            toplam = toplam * 0.90
        elif self.indirim_turu == "kargo_bedava":
            print("Kargo bedava!")
        elif self.indirim_turu == "ikial_ucodeol":
            urun_sayisi = sum(u["adet"] for u in self.urunler)
            if urun_sayisi >= 3:
                en_ucuz = min(self.urunler, key=lambda u: u["fiyat"])
                toplam -= en_ucuz["fiyat"]

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
sepet.indirim_turu = "yuzde10"
sepet.sepeti_yazdir()