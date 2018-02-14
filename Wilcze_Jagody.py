from Rosliny import Rosliny
import random


class Wilcze_Jagody (Rosliny):
    def __init__(self, s1):
        Rosliny.__init__(self)
        self.obrazek = "wilcze_jagody.png"
        self.nazwa = "Jagody"
        self.symbol = 'J'
        self.sila = 99
        self.swiat = s1
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc()-1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, 'J')
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def czyRoslinaTrujaca(self):
        return True

    def czyZabijZjadajacego(self, atakujacy):
        return True
