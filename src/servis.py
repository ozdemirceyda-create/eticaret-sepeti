from sepet import Sepet
from dekoratorler import HediyelikPaketDekorator, EkspresKargoDekorator
from gozlemciler import SepetYayinci, StokServisi, BildirimServisi, LogServisi
from komutlar import KomutYoneticisi, UrunEkleKomutu, IndirimUygulaKomutu

class SepetServisi:
    def __init__(self):
        self._sepet = Sepet()
        self._yayinci = SepetYayinci()
        self._yoneticisi = KomutYoneticisi()

        self._yayinci.gozlemci_ekle(StokServisi())
        self._yayinci.gozlemci_ekle(BildirimServisi())
        self._yayinci.gozlemci_ekle(LogServisi())

    def urun_ekle(self, urun_adi, fiyat, adet):
        komut = UrunEkleKomutu(self._sepet, urun_adi, fiyat, adet)
        self._yoneticisi.calistir(komut)
        self._yayinci.bildir("urun_eklendi", {"ad": urun_adi, "adet": adet})

    def son_islemi_geri_al(self):
        self._yoneticisi.geri_al()

    def indirim_uygula(self, indirim_turu):
        komut = IndirimUygulaKomutu(self._sepet, indirim_turu)
        self._yoneticisi.calistir(komut)

    def hediye_paketi_ekle(self, mesaj=""):
        self._sepet = HediyelikPaketDekorator(self._sepet, mesaj)

    def ekspres_kargo_ekle(self):
        self._sepet = EkspresKargoDekorator(self._sepet)

    def siparis_tamamla(self):
        toplam = self._sepet.toplam_hesapla()
        self._yayinci.bildir("siparis_tamamlandi", {"toplam": toplam})
        self._sepet.sepeti_yazdir()


servis = SepetServisi()
servis.urun_ekle("Laptop", 15000, 1)
servis.urun_ekle("Mouse", 500, 2)
servis.urun_ekle("Klavye", 300, 1)

print("\n--- Klavye geri alınıyor ---")
servis.son_islemi_geri_al()

servis.indirim_uygula("yuzde10")
servis.hediye_paketi_ekle("Anneme hediye!")
servis.siparis_tamamla()