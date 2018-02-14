from Rosliny import Rosliny
import random


class Guarana (Rosliny):
    def __init__(self, s1):
        Rosliny.__init__(self)
        self.obrazek = "guarana.jpg"
        self.nazwa = "Guarana"
        self.symbol = 'G'
        self.sila = 0
        self.swiat = s1
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc()-1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, 'G')
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()
