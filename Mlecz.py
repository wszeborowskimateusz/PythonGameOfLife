from Rosliny import Rosliny
import random


class Mlecz (Rosliny):
    def __init__(self, s1):
        Rosliny.__init__(self)
        self.obrazek = "mlecz.png"
        self.nazwa = "Mlecz"
        self.symbol = 'M'
        self.sila = 0
        self.swiat = s1
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc()-1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, 'M')
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def akcja(self,zasieg=1):
        Rosliny.akcja(self)
        Rosliny.akcja(self)
        Rosliny.akcja(self)
