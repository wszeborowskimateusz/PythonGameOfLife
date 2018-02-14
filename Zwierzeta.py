from Organizm import Organizm
import random


class Zwierzeta (Organizm):

    def __init__(self):
        Organizm.__init__(self)

    def akcja(self, zasieg=1):
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, ' ')
        polozenie_x_before = self.polozenie_x
        polozenie_y_before = self.polozenie_y
        szerokoscSwiata = self.swiat.getSzerokosc()
        wysokoscSwiata = self.swiat.getWysokosc()
        if ((self.polozenie_y == 0 and self.polozenie_x == 0) or (self.polozenie_y == 0 and self.polozenie_x == szerokoscSwiata - 1)
            or (self.polozenie_y == wysokoscSwiata - 1 and self.polozenie_x == 0 )
            or (self.polozenie_y == wysokoscSwiata - 1 and self.polozenie_x == szerokoscSwiata - 1)
            or (zasieg == 2 and self.polozenie_x == 1 and self.polozenie_y == 1)  or (zasieg == 2 and self.polozenie_x == 1 and self.polozenie_y == wysokoscSwiata-zasieg)
            or (zasieg == 2 and self.polozenie_x == szerokoscSwiata-zasieg and self.polozenie_y == 1)
            or (zasieg == 2 and self.polozenie_x == szerokoscSwiata-zasieg and self.polozenie_y == wysokoscSwiata-zasieg)
            or (zasieg == 2 and ((self.polozenie_x == 2 and self.polozenie_y == 1) or (self.polozenie_x == 1 and self.polozenie_y == 2)
            or (self.polozenie_x == szerokoscSwiata-3 and self.polozenie_y == 2) or (self.polozenie_x == szerokoscSwiata - 2 and self.polozenie_y == wysokoscSwiata - 3)
            or (self.polozenie_x == 1 and self.polozenie_y == wysokoscSwiata - 3) or (self.polozenie_x == 3 and self.polozenie_y == wysokoscSwiata - 2)
            or self.polozenie_x == szerokoscSwiata - 2 and self.polozenie_y == wysokoscSwiata -3)
            or self.polozenie_x == szerokoscSwiata - 3 and self.polozenie_y == wysokoscSwiata -2)):

                random2 = random.randint(0,2)
                if (random2==0):
                    if(self.polozenie_y == 0 or (zasieg == 2 and (self.polozenie_y == 1 or self.polozenie_y == 2))):
                        self.polozenie_y += zasieg
                    else:
                        self.polozenie_y -= zasieg
                elif (random2==1):
                    if (self.polozenie_x == 0 or (zasieg == 2 and (self.polozenie_x == 1 or self.polozenie_x == 2))):
                        self.polozenie_x += zasieg
                    else:
                        self.polozenie_x -= zasieg
                elif(random2==2):
                    if (self.polozenie_x == 0 and self.polozenie_y == 0 or (zasieg == 2 and (self.polozenie_x == 1 and self.polozenie_y == 1
                     or (self.polozenie_x == 2 and self.polozenie_y == 1) or (self.polozenie_x == 1 and self.polozenie_y == 2)))):
                        self.polozenie_x += zasieg
                        self.polozenie_y += zasieg
                    elif (self.polozenie_x == 0 and self.polozenie_y == wysokoscSwiata - 1
                        or (zasieg == 2 and (self.polozenie_x == 1 and self.polozenie_y == wysokoscSwiata - zasieg
                        or  (self.polozenie_x == 1 and self.polozenie_y == wysokoscSwiata - 3) or (
                            self.polozenie_x == 3 and self.polozenie_y == wysokoscSwiata - 2)))):
                            self.polozenie_x += zasieg
                            self.polozenie_y -= zasieg
                    elif(self.polozenie_x == szerokoscSwiata - 1 and self.polozenie_y == 0
                        or (zasieg == 2 and (self.polozenie_x == szerokoscSwiata - zasieg and self.polozenie_y == 1)
                        or (self.polozenie_x == szerokoscSwiata - 3 and self.polozenie_y == 2) or (
                            self.polozenie_x == szerokoscSwiata - 2 and self.polozenie_y == wysokoscSwiata - 3))):
                            self.polozenie_x -= zasieg
                            self.polozenie_y += zasieg

                    else:
                        self.polozenie_x -= zasieg
                        self.polozenie_y -= zasieg

        elif (self.polozenie_x == 0 or (
                    zasieg == 2 and self.polozenie_x == 1) or self.polozenie_x == szerokoscSwiata - zasieg or (
                    zasieg == 2 and self.polozenie_x == szerokoscSwiata - 1) or self.polozenie_y == 0 or (
                    zasieg == 2 and self.polozenie_y == 1) or self.polozenie_y == wysokoscSwiata - zasieg or (
                    zasieg == 2 and self.polozenie_y == wysokoscSwiata - 1)):
                random2 = random.randint(0,4)
                if (self.polozenie_x == 0 or (zasieg == 2 and self.polozenie_x == 1)):
                    if (random2 == 0):
                        self.polozenie_y -= zasieg
                    elif (random2 == 1):
                        self.polozenie_y -= zasieg
                        self.polozenie_x += zasieg
                    elif (random2 == 2):
                        self.polozenie_x += zasieg
                    elif (random2 == 3):
                        self.polozenie_y += zasieg
                        self.polozenie_x += zasieg
                    else:
                        self.polozenie_y += zasieg
                elif (self.polozenie_x == szerokoscSwiata - zasieg or (zasieg == 2 and self.polozenie_x == szerokoscSwiata - 1)):
                    if (random2 == 0):
                        self.polozenie_y -= zasieg
                    elif(random2 == 1):
                        self.polozenie_y -= zasieg
                        self.polozenie_x -= zasieg
                    elif(random2 == 2):
                        self.polozenie_x -= zasieg
                    elif (random2 == 3):
                        self.polozenie_x -= zasieg
                        self.polozenie_y += zasieg
                    else:
                        self.polozenie_y += zasieg
                elif (self.polozenie_y == 0 or (zasieg == 2 and self.polozenie_y == 1)):
                    if (random2 == 0):
                        self.polozenie_x -= zasieg
                    elif (random2 == 1):
                        self.polozenie_x -= zasieg
                        self.polozenie_y += zasieg
                    elif (random2 == 2):
                        self.polozenie_y += zasieg
                    elif (random2 == 3):
                        self.polozenie_x += zasieg
                        self.polozenie_y += zasieg
                    else:
                        self.polozenie_x += zasieg
                else:
                    if (random2 == 0):
                        self.polozenie_x -= zasieg
                    elif (random2 == 1):
                        self.polozenie_x -= zasieg
                        self.polozenie_y -= zasieg
                    elif (random2 == 2):
                        self.polozenie_y -= zasieg
                    elif(random2 == 3):
                        self.polozenie_x += zasieg
                        self.polozenie_y -= zasieg
                    else:
                        self.polozenie_x += zasieg

        else:
            random2 = random.randint(0,7)
            if (random2 == 0):
                self.polozenie_y -= zasieg
            elif(random2 == 1):
                self.polozenie_x += zasieg
                self.polozenie_y -= zasieg
            elif (random2 == 2):
                self.polozenie_x+=zasieg
            elif (random2 == 3):
                self.polozenie_x += zasieg
                self.polozenie_y += zasieg
            elif(random2 == 4):
                self.polozenie_y+=zasieg
            elif (random2 == 5):
                self.polozenie_x -= zasieg
                self.polozenie_y += zasieg
            elif (random2 == 6):
                self.polozenie_x -= zasieg
            else:
                self.polozenie_x -= zasieg
                self.polozenie_y -= zasieg

        if (self.swiat.getPlansza(self.polozenie_y, self.polozenie_x) != ' '):
            tmp2 = self.swiat.getPierwszyOrganizm()
            while (tmp2 is not None):
                if (tmp2.getPolozenie_x() == self.polozenie_x and tmp2.getPolozenie_y() == self.polozenie_y and tmp2 != self):
                    if (self.czyDobryWech(tmp2) == True):
                        wysokosc = self.swiat.getWysokosc()
                        szerokosc = self.swiat.getSzerokosc()
                        if ((polozenie_y_before + 1 < wysokosc and self.swiat.getPlansza(polozenie_y_before + 1, polozenie_x_before) != ' ')
                    and(polozenie_y_before - 1 >= 0 and self.swiat.getPlansza(polozenie_y_before - 1, polozenie_x_before) != ' ')
                    and (polozenie_x_before - 1 >= 0 and self.swiat.getPlansza(polozenie_y_before, polozenie_x_before - 1) != ' ')
                    and (polozenie_x_before + 1 < szerokosc and self.swiat.getPlansza(polozenie_y_before,polozenie_x_before + 1) != ' ')
                    and (polozenie_y_before - 1 >= 0 and polozenie_x_before - 1 >= 0 and self.swiat.getPlansza(polozenie_y_before - 1, polozenie_x_before - 1) != ' ')
                    and (polozenie_y_before + 1 < wysokosc and polozenie_x_before + 1 < szerokosc and self.swiat.getPlansza(polozenie_y_before + 1, polozenie_x_before + 1) != ' ')
                    and (polozenie_y_before - 1 >= 0 and polozenie_x_before + 1 < szerokosc and self.swiat.getPlansza(polozenie_y_before - 1, polozenie_x_before + 1) != ' ')
                    and (polozenie_y_before + 1 < wysokosc and polozenie_x_before - 1 >= 0 and self.swiat.getPlansza(polozenie_y_before + 1, polozenie_x_before - 1) != ' ')):
                            self.setPolozenie_x(polozenie_x_before)
                            self.setPolozenie_y(polozenie_y_before)
                            self.swiat.dodajDoPlanszy(polozenie_y_before, polozenie_x_before, self.symbol)
                            break

                        else:
                            self.setPolozenie_x(polozenie_x_before)
                            self.setPolozenie_y(polozenie_y_before)
                            self.swiat.dodajDoPlanszy(polozenie_y_before, polozenie_x_before, self.symbol)
                else:
                    self.kolizja(tmp2, polozenie_y_before, polozenie_x_before)
                    break
                tmp2 = tmp2.getNext()

        else:
            self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)

    def kolizja(self,broniacy, polozenie_y_before,polozenie_x_before):
            if (self.getSymbol() == broniacy.getSymbol()):
                self.setPolozenie_x(polozenie_x_before)
                self.setPolozenie_y(polozenie_y_before)
                self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
                polozenie_x_dziecko=0
                polozenie_y_dziecko=0

                broniacy_x = broniacy.getPolozenie_x()

                broniacy_y = broniacy.getPolozenie_y()
                szerokosc = self.swiat.getSzerokosc()
                wysokosc = self.swiat.getWysokosc()
                mozliwe_kierunki=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                for i in range (0,16):
                    mozliwe_kierunki[i]=0
                if (broniacy_y + 1 < wysokosc and self.swiat.getPlansza(broniacy_y + 1, broniacy_x) == ' '):
                    mozliwe_kierunki[0] = 1
                if (broniacy_y - 1 >= 0 and self.swiat.getPlansza(broniacy_y - 1, broniacy_x) == ' '):
                    mozliwe_kierunki[1] = 1
                if (broniacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y, broniacy_x - 1) == ' '):
                    mozliwe_kierunki[2] = 1
                if (broniacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y, broniacy_x + 1) == ' '):
                    mozliwe_kierunki[3] = 1
                if (broniacy_y - 1 >= 0 and broniacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y - 1, broniacy_x - 1) == ' '):
                    mozliwe_kierunki[4] = 1
                if (broniacy_y + 1 < wysokosc and broniacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y + 1, broniacy_x + 1) == ' '):
                    mozliwe_kierunki[5] = 1
                if (broniacy_y - 1 >= 0 and broniacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y - 1, broniacy_x + 1) == ' '):
                    mozliwe_kierunki[6] = 1;
                if (broniacy_y + 1 < wysokosc and broniacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y + 1, broniacy_x - 1) == ' '):
                    mozliwe_kierunki[7] = 1;

                atakujacy_x = self.getPolozenie_x()
                atakujacy_y = self.getPolozenie_y()
                if (atakujacy_y + 1 < wysokosc and self.swiat.getPlansza(atakujacy_y + 1, atakujacy_x) == ' '):
                    mozliwe_kierunki[8] = 1
                if (atakujacy_y - 1 >= 0 and self.swiat.getPlansza(atakujacy_y - 1, atakujacy_x) == ' '):
                    mozliwe_kierunki[9] = 1
                if (atakujacy_x - 1 >= 0 and self.swiat.getPlansza(atakujacy_y, atakujacy_x - 1) == ' '):
                    mozliwe_kierunki[10] = 1
                if (atakujacy_x + 1 < szerokosc and self.swiat.getPlansza(atakujacy_y, atakujacy_x + 1) == ' '):
                    mozliwe_kierunki[11] = 1
                if (atakujacy_y - 1 >= 0 and atakujacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y - 1, atakujacy_x - 1) == ' '):
                    mozliwe_kierunki[12] = 1
                if (atakujacy_y + 1 < wysokosc and atakujacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y + 1, atakujacy_x + 1) == ' '):
                    mozliwe_kierunki[13] = 1
                if (atakujacy_y - 1 >= 0 and atakujacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y - 1, atakujacy_x + 1) == ' '):
                    mozliwe_kierunki[14] = 1
                if (atakujacy_y + 1 < wysokosc and atakujacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y + 1, atakujacy_x - 1) == ' '):
                    mozliwe_kierunki[15] = 1

                ile = 0
                for i  in range(0,16):
                    if (mozliwe_kierunki[i] == 1):
                        ile+=1


                if (self.swiat.getIloscOrganizmow() >= self.swiat.getSzerokosc() * self.swiat.getWysokosc() or (ile == 0)):
                    return
                else:
                    random2 = random.randint(0,15)
                    while (mozliwe_kierunki[random2] != 1):
                        random2 = random.randint(0,15)
                if (random2 == 0):
                    polozenie_y_dziecko = broniacy_y + 1
                    polozenie_x_dziecko = broniacy_x
                elif (random2 == 1):
                    polozenie_y_dziecko = broniacy_y - 1
                    polozenie_x_dziecko = broniacy_x
                elif(random2 == 2):
                    polozenie_y_dziecko = broniacy_y
                    polozenie_x_dziecko = broniacy_x - 1
                elif (random2 == 3):
                    polozenie_y_dziecko = broniacy_y
                    polozenie_x_dziecko = broniacy_x + 1
                elif (random2 == 4):
                    polozenie_y_dziecko = broniacy_y - 1
                    polozenie_x_dziecko = broniacy_x - 1
                elif (random2 == 5):
                    polozenie_y_dziecko = (broniacy_y + 1)
                    polozenie_x_dziecko = (broniacy_x + 1)
                elif (random2 == 6):
                    polozenie_y_dziecko = (broniacy_y - 1)
                    polozenie_x_dziecko = (broniacy_x + 1)
                elif (random2 == 7):
                    polozenie_y_dziecko = (broniacy_y + 1)
                    polozenie_x_dziecko = (broniacy_x - 1)
                elif (random2 == 8):
                    polozenie_y_dziecko = atakujacy_y + 1
                    polozenie_x_dziecko = atakujacy_x
                elif (random2 == 9):
                    polozenie_y_dziecko = atakujacy_y - 1
                    polozenie_x_dziecko = atakujacy_x
                elif (random2 == 10):
                   polozenie_y_dziecko = atakujacy_y
                   polozenie_x_dziecko = atakujacy_x - 1
                elif (random2 == 11):
                    polozenie_y_dziecko = atakujacy_y
                    polozenie_x_dziecko = atakujacy_x + 1
                elif (random2 == 12):
                    polozenie_y_dziecko = atakujacy_y - 1
                    polozenie_x_dziecko = atakujacy_x - 1
                elif (random2 == 13):
                    polozenie_y_dziecko = (atakujacy_y + 1)
                    polozenie_x_dziecko = (atakujacy_x + 1)
                elif (random2 == 14):
                    polozenie_y_dziecko = (atakujacy_y - 1)
                    polozenie_x_dziecko = (atakujacy_x + 1)
                else:
                    polozenie_y_dziecko = (atakujacy_y + 1)
                    polozenie_x_dziecko = (atakujacy_x - 1)
                from Wilk import Wilk
                from Zolw import Zolw
                from Owca import Owca
                from Cyber_owca import Cyber_owca
                from Antylopa import Antylopa
                from Lis import Lis
                tmp = None
                symbol = self.symbol
                if(symbol == 'A'):
                    tmp = Antylopa(self.swiat)
                elif(symbol=='C'):
                    tmp = Cyber_owca(self.swiat)
                elif(symbol=='L'):
                    tmp = Lis(self.swiat)
                elif(symbol=='O'):
                    tmp = Owca(self.swiat)
                elif(symbol=='W'):
                    tmp = Wilk(self.swiat)
                elif(symbol == 'Z'):
                    tmp = Zolw(self.swiat)

                self.swiat.dodajDoPlanszy(tmp.getPolozenie_y(),tmp.getPolozenie_x(),' ')
                tmp.setPolozenie_x(polozenie_x_dziecko)
                tmp.setPolozenie_y(polozenie_y_dziecko)
                tmp.setDelay(True)
                self.swiat.dodajDoPlanszy(tmp.getPolozenie_y(),tmp.getPolozenie_x(),tmp.getSymbol())
                self.swiat.dodajWiadomosc(self.getNazwa())
                self.swiat.dodajWiadomosc(" wlasnie sie rozmnozyl ")

            elif (broniacy.czyRoslinaTrujaca() == True):
                if (broniacy.czyZabijZjadajacego(self) == True):
                    self.swiat.dodajWiadomosc(broniacy.getNazwa())
                    self.swiat.dodajWiadomosc(" zabil napastnika ")
                    self.swiat.dodajWiadomosc(self.getNazwa())
                    self.swiat.dodajDoPlanszy(self.polozenie_y,self.polozenie_x, ' ')
                    self.kill()
                    broniacy.kill()
                else:
                    self.swiat.dodajWiadomosc(self.getNazwa())
                    self.swiat.dodajWiadomosc(" zabil ")
                    self.swiat.dodajWiadomosc(broniacy.getNazwa())
                    broniacy.kill()
                    self.swiat.dodajDoPlanszy(self.polozenie_y,self.polozenie_x, self.symbol)
            else:
                if (self.getSila() >= broniacy.getSila()):
                    if (broniacy.czyOdbijAtak(self) == True):
                        self.setPolozenie_x(polozenie_x_before)
                        self.setPolozenie_y(polozenie_y_before)
                        self.swiat.dodajDoPlanszy(polozenie_y_before,polozenie_x_before,self.getSymbol())
                        self.swiat.dodajWiadomosc("Zolw zablokowal atak zwierzecia ")
                        self.swiat.dodajWiadomosc(self.getNazwa())
                    elif (broniacy.czyUcieka() == True):
                        random2 = random.randint(0,1);
                        if (random2 == 1):
                            self.swiat.dodajWiadomosc(self.getNazwa())
                            self.swiat.dodajWiadomosc(" zabil ")
                            self.swiat.dodajWiadomosc(broniacy.getNazwa())
                            broniacy.kill()
                            self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
                        else:
                            broniacy_x = broniacy.getPolozenie_x()
                            broniacy_y = broniacy.getPolozenie_y()
                            szerokosc = self.swiat.getSzerokosc()
                            wysokosc = self.swiat.getWysokosc()
                            mozliwe_kierunki=[8]
                            for i in range(0,8):
                                mozliwe_kierunki[i]=0
                            if (broniacy_y + 1 < wysokosc and self.swiat.getPlansza(broniacy_y + 1, broniacy_x) == ' '):
                                mozliwe_kierunki[0] = 1
                            if (broniacy_y - 1 >= 0 and self.swiat.getPlansza(broniacy_y - 1, broniacy_x) == ' '):
                                mozliwe_kierunki[1] = 1
                            if (broniacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y, broniacy_x - 1) == ' '):
                                mozliwe_kierunki[2] = 1
                            if (broniacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y, broniacy_x + 1) == ' '):
                                mozliwe_kierunki[3] = 1
                            if (broniacy_y - 1 >= 0 and broniacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y - 1, broniacy_x - 1) == ' '):
                                mozliwe_kierunki[4] = 1
                            if (broniacy_y + 1 < wysokosc and broniacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y + 1, broniacy_x + 1) == ' '):
                                mozliwe_kierunki[5] = 1
                            if (broniacy_y - 1 >= 0 and broniacy_x + 1 < szerokosc and self.swiat.getPlansza(broniacy_y - 1, broniacy_x + 1) == ' '):
                                mozliwe_kierunki[6] = 1
                            if (broniacy_y + 1 < wysokosc and broniacy_x - 1 >= 0 and self.swiat.getPlansza(broniacy_y + 1, broniacy_x - 1) == ' '):
                                mozliwe_kierunki[7] = 1

                            ile = 0
                            for i in range(0,8):
                                if (mozliwe_kierunki[i] == 1):
                                    ile+=1
                            if (ile == 0):
                                self.swiat.dodajWiadomosc(self.getNazwa())
                                self.swiat.dodajWiadomosc(" zabil ")
                                self.swiat.dodajWiadomosc(broniacy.getNazwa())
                                broniacy.kill()
                                self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, self.symbol)
                            else:
                                self.swiat.dodajWiadomosc(self.getNazwa())
                                self.swiat.dodajWiadomosc(" probwal zaatakowac Antylope. Ta jednak uciekla ")
                            random3 = random.randint(0,7)
                            while (mozliwe_kierunki[random3] != 1):
                                random3 = random.randint(0,7)
                            if (random3 == 0):
                                broniacy.setPolozenie_y(broniacy_y + 1)
                                self.swiat.dodajDoPlanszy(broniacy_y + 1, broniacy_x,broniacy.getSymbol())
                            elif (random3 == 1):
                                broniacy.setPolozenie_y(broniacy_y - 1)
                                self.swiat.dodajDoPlanszy(broniacy_y - 1,broniacy_x,broniacy.getSymbol())
                            elif (random3 == 2):
                                broniacy.setPolozenie_x(broniacy_x - 1)
                                self.swiat.dodajDoPlanszy(broniacy_y,broniacy_x - 1,broniacy.getSymbol())
                            elif (random3 == 3):
                                broniacy.setPolozenie_x(broniacy_x + 1)
                                self.swiat.dodajDoPlanszy(broniacy_y,broniacy_x + 1,broniacy.getSymbol())
                            elif (random3 == 4):
                                broniacy.setPolozenie_y(broniacy_y - 1)
                                broniacy.setPolozenie_x(broniacy_x - 1)
                                self.swiat.dodajDoPlanszy(broniacy_y - 1,broniacy_x - 1,broniacy.getSymbol())
                            elif (random3 == 5):
                                broniacy.setPolozenie_y(broniacy_y + 1)
                                broniacy.setPolozenie_x(broniacy_x + 1)
                                self.swiat.dodajDoPlanszy(broniacy_y + 1,broniacy_x + 1,broniacy.getSymbol())
                            elif (random3 == 6):
                                broniacy.setPolozenie_y(broniacy_y - 1)
                                broniacy.setPolozenie_x(broniacy_x + 1)
                                self.swiat.dodajDoPlanszy(broniacy_y - 1,broniacy_x + 1,broniacy.getSymbol())
                            else:
                                broniacy.setPolozenie_y(broniacy_y + 1)
                                broniacy.setPolozenie_x(broniacy_x - 1)
                                self.swiat.dodajDoPlanszy(broniacy_y + 1,broniacy_x - 1,broniacy.getSymbol())

                            self.swiat.dodajDoPlanszy(self.polozenie_y,self.polozenie_x,self.symbol)

                    else:
                        if (broniacy.getSymbol() == 'G'):
                            self.sila += 3
                        self.swiat.dodajWiadomosc(self.getNazwa())
                        self.swiat.dodajWiadomosc(" zabil ")
                        self.swiat.dodajWiadomosc(broniacy.getNazwa())
                        broniacy.kill()
                        self.swiat.dodajDoPlanszy(self.polozenie_y,self.polozenie_x,self.symbol)
                else:
                    self.swiat.dodajWiadomosc(broniacy.getNazwa())
                    self.swiat.dodajWiadomosc(" zabil napastnika ")
                    self.swiat.dodajWiadomosc(self.getNazwa())
                    self.kill()
                    self.swiat.dodajDoPlanszy(self.polozenie_y,self.polozenie_x,broniacy.getSymbol());
            self.swiat.dodajWiadomosc("\n")
