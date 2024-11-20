import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), maito.hinta())

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)

        hintojen_summa = maito.hinta() + porkkana.hinta()

        self.assertEqual(self.kori.hinta(), hintojen_summa)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_on_2_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), maito.hinta() * 2)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        nimi = ostos.tuotteen_nimi()
        maara = ostos.lukumaara()

        self.assertEqual((nimi, maara), (maito.nimi(), 1))
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_ostosta(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)