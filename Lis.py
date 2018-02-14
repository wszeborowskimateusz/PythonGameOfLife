from Zwierzeta import Zwierzeta
import random


class Lis (Zwierzeta):

    def __init__(self, s1):
        Zwierzeta.__init__(self)
        self.obrazek = "lis.png"
        self.nazwa = "Lis"
        self.symbol = 'L'
        self.swiat = s1
        self.sila = 3
        self.inicjatywa = 7
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc() - 1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def czyDobryWech(self, broniacy):
        if(broniacy.getSila() > self.getSila()):
            return True
        else:
            return False
