from sepet import Sepet
from dekoratorler import HediyelikPaketDekorator, EkspresKargoDekorator

class SepetServisi:
    def __init__(self):
        self._sepet = Sepet()

    def urun_ekle(self, urun_adi, fiyat, adet):
        self._sepet.urun_ekle(urun_adi, fiyat, adet)

    def indirim_uygula(self, indirim_turu):
        self._sepet.indirim_sec(indirim_turu)

    def hediye_paketi_ekle(self, mesaj=""):
        self._sepet = HediyelikPaketDekorator(self._sepet, mesaj)

    def ekspres_kargo_ekle(self):
        self._sepet = EkspresKargoDekorator(self._sepet)

    def siparis_ozeti(self):
        self._sepet.sepeti_yazdir()

servis = SepetServisi()
servis.urun_ekle("Laptop", 15000, 1)
servis.urun_ekle("Mouse", 500, 2)
servis.urun_ekle("Klavye", 300, 1)
servis.indirim_uygula("yuzde10")
servis.hediye_paketi_ekle("Anneme hediye!")
servis.ekspres_kargo_ekle()
servis.siparis_ozeti()