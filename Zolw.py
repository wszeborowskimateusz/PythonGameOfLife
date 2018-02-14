from Zwierzeta import Zwierzeta
import random


class Zolw (Zwierzeta):

    def __init__(self, s1):
        Zwierzeta.__init__(self)
        self.obrazek = "zolw.png"
        self.nazwa = "Zolw"
        self.symbol = 'Z'
        self.swiat = s1
        self.sila = 2
        self.inicjatywa = 1
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc() - 1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def akcja(self,zasieg=1):
        chanceToMove = random.randint(0, 3)

        if(chanceToMove < 3):
            return
        else:
            Zwierzeta.akcja(self)


    def czyOdbijAtak(self, atakujacy):
        if(atakujacy.getSila() < 5):
            return True
        else:
            return False
