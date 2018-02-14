from Zwierzeta import Zwierzeta
import random


class Owca (Zwierzeta):

    def __init__(self, s1):
        Zwierzeta.__init__(self)
        self.obrazek = "owca.png"
        self.nazwa = "Owca"
        self.symbol = 'O'
        self.swiat = s1
        self.sila = 4
        self.inicjatywa = 4
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc() - 1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()
