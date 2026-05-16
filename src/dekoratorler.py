class SepetDekorator:
    def __init__(self, sepet):
        self._sepet = sepet

    def urun_ekle(self, urun_adi, fiyat, adet):
        self._sepet.urun_ekle(urun_adi, fiyat, adet)

    def indirim_sec(self, indirim_turu):
        self._sepet.indirim_sec(indirim_turu)

    def toplam_hesapla(self):
        return self._sepet.toplam_hesapla()

    def sepeti_yazdir(self):
        self._sepet.sepeti_yazdir()


class HediyelikPaketDekorator(SepetDekorator):
    def __init__(self, sepet, not_mesaji=""):
        super().__init__(sepet)
        self.not_mesaji = not_mesaji
        self.paket_ucreti = 25

    def toplam_hesapla(self):
        toplam = self._sepet.toplam_hesapla()
        print(f"Hediye paketi eklendi (+{self.paket_ucreti} TL)")
        if self.not_mesaji:
            print(f"Not: {self.not_mesaji}")
        return toplam + self.paket_ucreti

    def sepeti_yazdir(self):
        self._sepet.sepeti_yazdir()
        print(f"Hediye Paketi: +{self.paket_ucreti} TL")
        print(f"GENEL TOPLAM: {self.toplam_hesapla()} TL")


class EkspresKargoDekorator(SepetDekorator):
    def __init__(self, sepet):
        super().__init__(sepet)
        self.ekspres_ucreti = 40

    def toplam_hesapla(self):
        toplam = self._sepet.toplam_hesapla()
        print(f"Ekspres kargo eklendi (+{self.ekspres_ucreti} TL)")
        return toplam + self.ekspres_ucreti

    def sepeti_yazdir(self):
        self._sepet.sepeti_yazdir()
        print(f"Ekspres Kargo: +{self.ekspres_ucreti} TL")
        print(f"GENEL TOPLAM: {self.toplam_hesapla()} TL")