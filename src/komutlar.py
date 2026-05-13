class Komut:
    def calistir(self):
        raise NotImplementedError("Bu metod alt sınıfta tanımlanmalı")

    def geri_al(self):
        raise NotImplementedError("Bu metod alt sınıfta tanımlanmalı")


class UrunEkleKomutu(Komut):
    def __init__(self, sepet, urun_adi, fiyat, adet):
        self._sepet = sepet
        self._urun_adi = urun_adi
        self._fiyat = fiyat
        self._adet = adet

    def calistir(self):
        self._sepet.urun_ekle(self._urun_adi, self._fiyat, self._adet)
        print(f"[KOMUT] '{self._urun_adi}' sepete eklendi.")

    def geri_al(self):
        self._sepet.urunler = [
            u for u in self._sepet.urunler
            if u["ad"] != self._urun_adi
        ]
        print(f"[KOMUT] '{self._urun_adi}' sepetten geri alındı.")


class IndirimUygulaKomutu(Komut):
    def __init__(self, sepet, indirim_turu):
        self._sepet = sepet
        self._indirim_turu = indirim_turu
        self._onceki_indirim = None

    def calistir(self):
        self._onceki_indirim = self._sepet.indirim
        self._sepet.indirim_sec(self._indirim_turu)
        print(f"[KOMUT] '{self._indirim_turu}' indirimi uygulandı.")

    def geri_al(self):
        self._sepet.indirim = self._onceki_indirim
        print(f"[KOMUT] İndirim geri alındı.")


class KomutYoneticisi:
    def __init__(self):
        self._gecmis = []

    def calistir(self, komut):
        komut.calistir()
        self._gecmis.append(komut)

    def geri_al(self):
        if self._gecmis:
            komut = self._gecmis.pop()
            komut.geri_al()
        else:
            print("[KOMUT] Geri alınacak işlem yok.")