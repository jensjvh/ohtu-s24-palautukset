class Sovelluslogiikka:
    def __init__(self, arvo=0, edellinen_arvo = 0):
        self._arvo = arvo
        self._edellinen_arvo = edellinen_arvo
    
    def aseta_edellinen_arvo(self, arvo):
        self._edellinen_arvo = arvo

    def miinus(self, operandi):
        self.aseta_edellinen_arvo(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.aseta_edellinen_arvo(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
