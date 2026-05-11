class IndirimStrategy:
    def uygula(self, toplam, urunler):
        raise NotImplementedError("Bu metod alt sınıfta tanımlanmalı")


class YuzdeOnIndirim(IndirimStrategy):
    def uygula(self, toplam, urunler):
        return toplam * 0.90


class KargoBedavaIndirim(IndirimStrategy):
    def uygula(self, toplam, urunler):
        kargo_ucreti = 50
        print("Kargo bedava! 50 TL kargo ücreti düşüldü.")
        return toplam - kargo_ucreti


class IkiAlUcOdeIndirim(IndirimStrategy):
    def uygula(self, toplam, urunler):
        urun_sayisi = sum(u["adet"] for u in urunler)
        if urun_sayisi >= 3:
            en_ucuz = min(urunler, key=lambda u: u["fiyat"])
            print(f"2 al 3 öde: {en_ucuz['ad']} bedava!")
            return toplam - en_ucuz["fiyat"]
        return toplam

class IndirimFactory:
    @staticmethod
    def olustur(indirim_turu):
        if indirim_turu == "yuzde10":
            return YuzdeOnIndirim()
        elif indirim_turu == "kargo_bedava":
            return KargoBedavaIndirim()
        elif indirim_turu == "ikial_ucodeol":
            return IkiAlUcOdeIndirim()
        else:
            raise ValueError(f"Bilinmeyen indirim türü: {indirim_turu}")