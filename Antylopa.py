from Zwierzeta import Zwierzeta
import random


class Antylopa (Zwierzeta):

    def __init__(self, s1):
        Zwierzeta.__init__(self)
        self.obrazek = "antylopa.png"
        self.nazwa = "Antylopa"
        self.symbol = 'A'
        self.swiat = s1
        self.sila = 4
        self.inicjatywa = 4
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc() - 1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def akcja(self,zasieg=1):
        Zwierzeta.akcja(self, 2)

    def czyUcieka(self):
        return True


