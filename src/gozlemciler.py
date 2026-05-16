class Gozlemci:
    def guncelle(self, olay, veri):
        raise NotImplementedError("Bu metod alt sınıfta tanımlanmalı")


class StokServisi(Gozlemci):
    def guncelle(self, olay, veri):
        if olay == "urun_eklendi":
            print(f"[STOK] '{veri['ad']}' ürününden {veri['adet']} adet rezerve edildi.")


class BildirimServisi(Gozlemci):
    def guncelle(self, olay, veri):
        if olay == "siparis_tamamlandi":
            print(f"[BİLDİRİM] Siparişiniz tamamlandı! Toplam: {veri['toplam']} TL")


class LogServisi(Gozlemci):
    def guncelle(self, olay, veri):
        print(f"[LOG] Olay: {olay} | Veri: {veri}")


class SepetYayinci:
    def __init__(self):
        self._gozlemciler = []

    def gozlemci_ekle(self, gozlemci):
        self._gozlemciler.append(gozlemci)

    def gozlemci_cikar(self, gozlemci):
        self._gozlemciler.remove(gozlemci)

    def bildir(self, olay, veri):
        for gozlemci in self._gozlemciler:
            gozlemci.guncelle(olay, veri)