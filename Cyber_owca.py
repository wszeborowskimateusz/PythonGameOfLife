from Zwierzeta import Zwierzeta
import random


class Cyber_owca (Zwierzeta):

    def __init__(self, s1):
        Zwierzeta.__init__(self)
        self.obrazek = "cyber_owca.jpg"
        self.nazwa = "Cyber owca"
        self.symbol = 'C'
        self.swiat = s1
        self.sila = 11
        self.inicjatywa = 4
        self.polozenie_x = random.randint(0, self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0, self.swiat.getWysokosc() - 1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def akcja(self, zasieg=1):
        tmp = self.swiat.getPierwszyOrganizm()
        barszcz = False
        barszcz_x = 0
        barszcz_y = 0
        barszcz_odleglosc = -1
        while (tmp is not None):
            if (tmp.getSymbol() == 'B'):
                barszcz = True
                barszcz_x_tmp = tmp.getPolozenie_x()
                barszcz_y_tmp = tmp.getPolozenie_y()
                barszcz_odleglosc_tmp = ((barszcz_x-self.polozenie_x)**2 + (barszcz_y - self.polozenie_y)**2)**(1/2)
                if(barszcz_odleglosc == -1 or barszcz_odleglosc_tmp<barszcz_odleglosc ):
                    barszcz_odleglosc = barszcz_odleglosc_tmp
                    barszcz_y = barszcz_y_tmp
                    barszcz_x = barszcz_x_tmp
            tmp = tmp.getNext()
        if barszcz:
            polozenie_y_before = self.polozenie_y
            polozenie_x_before = self.polozenie_x

            self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, ' ')

            if (self.polozenie_x < barszcz_x):
                self.polozenie_x+=1
            elif(self.polozenie_x > barszcz_x):
                self.polozenie_x-=1

            if (self.polozenie_y < barszcz_y):
                self.polozenie_y+=1
            elif(self.polozenie_y > barszcz_y):
                self.polozenie_y-=1

            if (self.swiat.getPlansza(self.polozenie_y, self.polozenie_x) != ' '):
                tmp2 = self.swiat.getPierwszyOrganizm()
                while (tmp2 is not None):
                    if (tmp2.getPolozenie_x() == self.polozenie_x and tmp2.getPolozenie_y() == self.polozenie_y and tmp2 != self):
                        self.kolizja(tmp2, polozenie_y_before, polozenie_x_before)
                        break
                    tmp2 = tmp2.getNext()
            else:
                self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
        else:
            Zwierzeta.akcja(self, zasieg)

    def czyGinieOdBarszczu(self):
        return False