KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Negatiivinen kapasiteetti")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Negatiivinen kasvatuskoko")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0
    
    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, luku):
        return luku in self.lukujono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        if self.alkioiden_lkm >= len(self.lukujono):
            self._kasvata_taulukkoa()

        self.lukujono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1
        return True

    def _kasvata_taulukkoa(self):
        """Helper metodi"""
        uusi_koko = len(self.lukujono) + self.kasvatuskoko
        uusi_lukujono = self._luo_lista(uusi_koko)

        for i in range(self.alkioiden_lkm):
            uusi_lukujono[i] = self.lukujono[i]

        self.lukujono = uusi_lukujono

    def poista(self, luku):
        if luku in self.lukujono[:self.alkioiden_lkm]:
            self.lukujono.remove(luku)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        tulosjoukko = IntJoukko()
        for luku in joukko_a.to_int_list() + joukko_b.to_int_list():
            tulosjoukko.lisaa(luku)
        return tulosjoukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        tulosjoukko = IntJoukko()
        for luku in joukko_a.to_int_list():
            if joukko_b.kuuluu(luku):
                tulosjoukko.lisaa(luku)
        return tulosjoukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        tulosjoukko = IntJoukko()
        for luku in joukko_a.to_int_list():
            if not joukko_b.kuuluu(luku):
                tulosjoukko.lisaa(luku)
        return tulosjoukko

    def __str__(self):
        luvut = ", ".join(str(luku) for luku in self.lukujono[:self.alkioiden_lkm])
        return f"{{{luvut}}}"
