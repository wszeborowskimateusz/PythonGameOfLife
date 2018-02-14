from Rosliny import Rosliny
import random


class Barszcz_Sosnowskiego(Rosliny):
    def __init__(self, s1):
        Rosliny.__init__(self)
        self.obrazek = "barszcz_sosnowskiego.png"
        self.nazwa = "Barszcz"
        self.symbol = 'B'
        self.sila = 10
        self.swiat = s1
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc() - 1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc() - 1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def akcja(self, zasieg=1):

        tmp = self.swiat.getPierwszyOrganizm()
        while (tmp is not None):
            if (
                ((tmp.getPolozenie_x() == self.polozenie_x + 1 and tmp.getPolozenie_y() == self.polozenie_y)
                 or (tmp.getPolozenie_x() == self.polozenie_x - 1 and tmp.getPolozenie_y() == self.polozenie_y)
                 or (tmp.getPolozenie_x() == self.polozenie_x and tmp.getPolozenie_y() - 1 == self.polozenie_y)
                 or (tmp.getPolozenie_x() == self.polozenie_x + 1 and tmp.getPolozenie_y() + 1 == self.polozenie_y)
                 or (tmp.getPolozenie_x() == self.polozenie_x - 1 and tmp.getPolozenie_y() - 1 == self.polozenie_y)
                 or (tmp.getPolozenie_x() == self.polozenie_x + 1 and tmp.getPolozenie_y() - 1 == self.polozenie_y)
                 or (tmp.getPolozenie_x() == self.polozenie_x - 1 and tmp.getPolozenie_y() + 1 == self.polozenie_y))and
                tmp.czyGinieOdBarszczu() is True and
                    tmp != self and tmp.getSymbol() != 'C'):
                self.swiat.dodajWiadomosc(" Barszcz sosnowskiego wlasnie unicestwil ")
                self.swiat.dodajWiadomosc(tmp.getNazwa())
                self.swiat.dodajWiadomosc(" ")
                tmp.kill()
            tmp = tmp.getNext()

    def czyRoslinaTrujaca(self):
        return True

    def czyZabijZjadajacego(self, atakujacy):
        if (atakujacy.getSymbol() == 'C'):
            return False
        else:
            return True



