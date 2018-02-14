from Zwierzeta import Zwierzeta
from Czlowiek_Ruch import Czlowiek_Ruch
import random


class Czlowiek(Zwierzeta):

    def __init__(self, s1):
        Zwierzeta.__init__(self)
        self.obrazek = "czlowiek.png"
        self.liczba_tur_cooldown = 0
        self.liczba_tur_mocy = 0
        self.cooldown = False
        self.moc_specjalna = 0
        self.nazwa = "Czlowiek"
        self.symbol = 'Y'
        self.sila = 5
        self.inicjatywa = 4
        self.swiat = s1
        self.polozenie_x = random.randint(0,self.swiat.getSzerokosc()-1)
        self.polozenie_y = random.randint(0,self.swiat.getWysokosc()-1)
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, 'Y')
        self.swiat.dodajOrganizm(self)
        self.swiat.incrementIloscOrganizmow()

    def kill(self):
        Zwierzeta.kill(self)
        self.liczba_tur_mocy = 0
        self.moc_specjalna = 0
        self.cooldown = False
        self.liczba_tur_cooldown = 0

    def akcja(self, zasieg=1):
        self.brak_mocy = False
        kierunek = self.swiat.getRuch()
        if (self.moc_specjalna == 1):
            self.liczba_tur_mocy+=1
        if (self.liczba_tur_mocy == 4 or self.liczba_tur_mocy == 5):
            self.moc_specjalna = 2
            self.liczba_tur_mocy+=1
        if (self.liczba_tur_mocy == 6):
            self.swiat.qPressed = False
            self.cooldown = True
            self.liczba_tur_mocy = 0
            self.moc_specjalna = 0
        if (self.cooldown):
            self.liczba_tur_cooldown+=1
        if (self.liczba_tur_cooldown == 6):
            self.cooldown = False

        if (self.moc_specjalna == 1):
            zasieg = 2
        elif (self.moc_specjalna == 2):
            random1 = random.randint(0,1)
            if (random1 == 0):
                zasieg = 2
            else:
                zasieg = 1

        if (self.swiat.qPressed):
            if (not self.cooldown and self.moc_specjalna == 0):
                self.moc_specjalna = 1
                self.liczba_tur_mocy+=1
                self.brak_mocy = True
                zasieg = 2
            elif(not self.brak_mocy):
                self.brak_mocy = True
        polozenie_x_before = self.polozenie_x
        polozenie_y_before = self.polozenie_y
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, ' ')
        kierunek = self.swiat.getRuch()
        if (kierunek == Czlowiek_Ruch.GORA and self.polozenie_y - zasieg >= 0):
            self.polozenie_y -= zasieg
        elif (kierunek == Czlowiek_Ruch.DOL and self.polozenie_y + zasieg < self.swiat.getWysokosc()):
            self.polozenie_y += zasieg
        elif (kierunek == Czlowiek_Ruch.LEWO and self.polozenie_x - zasieg >= 0):
            self.polozenie_x -= zasieg
        elif (kierunek == Czlowiek_Ruch.PRAWO and self.polozenie_x + zasieg < self.swiat.getSzerokosc()):
            self.polozenie_x += zasieg

        if (self.swiat.getPlansza(self.polozenie_y, self.polozenie_x) != ' '):
            tmp2 = self.swiat.getPierwszyOrganizm()
            while (tmp2 is not None):
                if (tmp2.getPolozenie_x() == self.polozenie_x and tmp2.getPolozenie_y() == self.polozenie_y and tmp2 != self):
                    self.kolizja(tmp2, polozenie_y_before, polozenie_x_before)
                    break
                tmp2 = tmp2.getNext()

        else:
            self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, 'Y')



    def getMocSpecjalna(self):
        return self.moc_specjalna

    def getCooldown(self):
        return self.cooldown

    def getLiczbaTurMocy(self):
        return self.liczba_tur_mocy

    def getLiczbaTurCooldown(self):
        return self.liczba_tur_cooldown

    def setMocSpecjalna(self, m):
        self.moc_specjalna = m

    def setCooldown(self, m):
        self.cooldown = m

    def setLiczbaTurMocy(self, m):
        self.liczba_tur_mocy = m

    def setLiczbaTurCooldown(self, m):
        self.liczba_tur_cooldown = m


