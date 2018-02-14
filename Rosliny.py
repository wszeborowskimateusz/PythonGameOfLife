from Organizm import Organizm
import random
class Rosliny (Organizm):
    def __init__(self):
        Organizm.__init__(self)
        self.inicjatywa = 0

    def kolizja(self,broniacy, polozenie_y_before, polozenie_x_before):
        pass

    def akcja(self, zasieg=1):
        szansa = random.randint(0, 19)
        if(szansa == 0):
            wysokosc = self.swiat.getWysokosc()
            szerokosc = self.swiat.getSzerokosc()
            mozliwe_kierunki = [0,0,0,0,0,0,0,0]
            for i in range (0,8):
                mozliwe_kierunki[i]=0

            if (self.polozenie_y + 1 < wysokosc and self.swiat.getPlansza(self.polozenie_y + 1, self.polozenie_x) == ' '):
                mozliwe_kierunki[0] = 1
            if (self.polozenie_y - 1 >= 0 and self.swiat.getPlansza(self.polozenie_y - 1, self.polozenie_x) == ' '):
                mozliwe_kierunki[1] = 1
            if (self.polozenie_x - 1 >= 0 and self.swiat.getPlansza(self.polozenie_y, self.polozenie_x - 1) == ' '):
                mozliwe_kierunki[2] = 1
            if (self.polozenie_x + 1 < szerokosc and self.swiat.getPlansza(self.polozenie_y, self.polozenie_x + 1) == ' '):
                mozliwe_kierunki[3] = 1
            if (self.polozenie_y - 1 >= 0 and self.polozenie_x - 1 >= 0 and self.swiat.getPlansza(self.polozenie_y - 1, self.polozenie_x - 1) == ' '):
                mozliwe_kierunki[4] = 1
            if (self.polozenie_y + 1 < wysokosc  and self.polozenie_x + 1 < szerokosc and self.swiat.getPlansza(self.polozenie_y + 1, self.polozenie_x + 1) == ' '):
                mozliwe_kierunki[5] = 1
            if (self.polozenie_y - 1 >= 0 and self.polozenie_x + 1 < szerokosc and self.swiat.getPlansza(self.polozenie_y - 1, self.polozenie_x + 1) == ' '):
                mozliwe_kierunki[6] = 1
            if (self.polozenie_y + 1 < wysokosc and self.polozenie_x - 1 >= 0 and self.swiat.getPlansza(self.polozenie_y + 1, self.polozenie_x - 1) == ' '):
                mozliwe_kierunki[7] = 1

            ile = 0
            for i in range(0,8):
                if(mozliwe_kierunki[i] == 1):
                    ile+=1
            if(self.swiat.getIloscOrganizmow() >= self.swiat.getSzerokosc() * self.swiat.getWysokosc() or ile == 0):
                return
            else:
                random1 = random.randint(0,7)
                while(mozliwe_kierunki[random1] != 1):
                    random1 = random.randint(0,7)
                if(random1 == 0):
                    polozenie_x_dziecko = self.polozenie_x
                    polozenie_y_dziecko = self.polozenie_y + 1
                elif(random1 == 1):
                    polozenie_y_dziecko = self.polozenie_y - 1
                    polozenie_x_dziecko = self.polozenie_x
                elif(random1 == 2):
                    polozenie_y_dziecko = self.polozenie_y
                    polozenie_x_dziecko = self.polozenie_x - 1
                elif(random1 == 3):
                     polozenie_y_dziecko = self.polozenie_y
                     polozenie_x_dziecko = self.polozenie_x + 1
                elif(random1 == 4):
                    polozenie_y_dziecko = self.polozenie_y - 1
                    polozenie_x_dziecko = self.polozenie_x - 1
                elif(random1 == 5):
                    polozenie_y_dziecko = self.polozenie_y + 1
                    polozenie_x_dziecko = self.polozenie_x + 1
                elif(random1 == 6):
                     polozenie_y_dziecko = self.polozenie_y - 1
                     polozenie_x_dziecko = self.polozenie_x + 1
                else:
                    polozenie_y_dziecko = self.polozenie_y + 1
                    polozenie_x_dziecko = self.polozenie_x - 1
                from Trawa import Trawa
                from Mlecz import Mlecz
                from Guarana import Guarana
                from Wilcze_Jagody import Wilcze_Jagody
                from Barszcz_Sosnowskiego import Barszcz_Sosnowskiego
                tmp = None
                zn = self.getSymbol()
                if (zn == 'T'):
                    tmp = Trawa(self.swiat)
                elif (zn == 'M'):
                    tmp = Mlecz(self.swiat)
                elif (zn == 'G'):
                    tmp = Guarana(self.swiat)
                elif (zn == 'J'):
                    tmp = Wilcze_Jagody(self.swiat)
                elif (zn == 'B'):
                    tmp = Barszcz_Sosnowskiego(self.swiat)

                self.swiat.dodajDoPlanszy(tmp.getPolozenie_y(), tmp.getPolozenie_x(), ' ')
                tmp.setPolozenie_x(polozenie_x_dziecko)
                tmp.setPolozenie_y(polozenie_y_dziecko)
                tmp.setDelay(True)
                self.swiat.dodajDoPlanszy(tmp.getPolozenie_y(), tmp.getPolozenie_x(), tmp.getSymbol())
                self.swiat.dodajWiadomosc(self.getNazwa())
                self.swiat.dodajWiadomosc(" wlasnie sie rozprzestrzenil \n")

        else:
            return

    def czyGinieOdBarszczu(self):
        return False

