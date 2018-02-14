
class Organizm:

    def __init__(self):

        self.delay = False

    def kill(self):
        self.swiat.decrementIloscOrganizmow()
        self.swiat.dodajDoPlanszy(self.polozenie_y, self.polozenie_x, ' ')
        self.swiat.usunOrganizm(self)

    def akcja(self, zasieg=1):
        pass

    def kolizja(self, broniacy, polozenie_y_before, polozenie_x_before):
        pass

    def getSila(self):
        return self.sila

    def setSila(self, s):
        self.sila = s

    def getInicjatywa(self):
        return self.inicjatywa

    def getSzerokoscSwiata(self):
        return self.swiat.getSzerokosc()

    def getWysokoscSwiata(self):
        return self.swiat.getWysokosc()

    def getPolozenie_x(self):
        return self.polozenie_x

    def getPolozenie_y(self):
        return self.polozenie_y

    def setPolozenie_y(self, y):
        self.polozenie_y = y

    def setPolozenie_x(self, x):
        self.polozenie_x = x

    def getSymbol(self):
        return self.symbol

    def getNext(self):
        return self.next

    def setNext(self,organizm):
        self.next = organizm

    def czyOdbijAtak(self,atakujacy):
        return False

    def czyGinieOdBarszczu(self):
        return True

    def czyDobryWech(self, broniacy):
        return False

    def czyUcieka(self):
        return False

    def czyRoslinaTrujaca(self):
        return False

    def czyZabijZjadajacego(self, atakujacy):
        return False

    def getNazwa(self):
        return self.nazwa

    def getDelay(self):
        return self.delay

    def setDelay(self, x):
        self.delay = x

    def getObrazek(self):
        return self.obrazek
