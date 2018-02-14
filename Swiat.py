from Antylopa import Antylopa
from Barszcz_Sosnowskiego import Barszcz_Sosnowskiego
from Cyber_owca import Cyber_owca
from Guarana import Guarana
from Lis import Lis
from Mlecz import Mlecz
from Owca import Owca
from Trawa import Trawa
from Wilcze_Jagody import Wilcze_Jagody
from Wilk import Wilk
from Zolw import Zolw
from Czlowiek import Czlowiek
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from Czlowiek_Ruch import Czlowiek_Ruch



class Swiat(QtGui.QWidget):

    def __init__(self, wys, sze):
        QtGui.QWidget.__init__(self)
        self.window = QtGui.QWidget
        wysokosc = wys * 30
        szerokosc = sze * 50
        self.window.resize(self, szerokosc, wysokosc)
        self.window.setWindowTitle(self, "Mateusz Wszeborowski 165562")
        self.qPressed = False
        self.ruch = None
        self.ilosc_organizmow = 0
        self.pierwszyOrganizm = None
        self.wysokosc = wys
        self.szerokosc = sze
        self.wiadomosc = ""
        self.numer_tury = 0
        self.plansza = [[0 for x in range(sze)] for y in range(wys)]
        self.buttons = {}

        layout = QtGui.QGridLayout()
        for i in range(0, wys):
            for j in range(0, sze):
                self.plansza[i][j] = ' '
                self.buttons[(i,j)] = QtGui.QPushButton("")
                layout.addWidget(self.buttons[(i, j)], i, j)
                self.buttons[(i,j)].setObjectName("{0},{1}".format(i, j))
                self.buttons[(i, j)].clicked.connect(self.dodajZwierze)

        self.next_round_button = QtGui.QPushButton("NASTEPNA TURA", self)
        self.next_round_button.move(50, wysokosc - 50)
        self.next_round_button.clicked.connect(lambda: self.wykonaj_ture())
        self.save_button = QtGui.QPushButton("ZAPISZ", self)
        self.save_button.move(70, wysokosc - 50)
        self.save_button.clicked.connect(lambda: self.zapiszSwiat())
        self.load_button = QtGui.QPushButton("WCZYTAJ", self)
        self.load_button.move(90, wysokosc - 50)
        self.load_button.clicked.connect(lambda: self.wczytajSwiat())
        layout.addWidget(self.next_round_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.save_button)

        #Text fild
        self.text = QtGui.QLineEdit()
        self.text.setReadOnly(True)

        layout.addWidget(self.text)

        self.setLayout(layout)
        self.window.show(self)

    def wykonaj_ture(self):
        self.wiadomosc = ""
        self.numer_tury += 1
        tmp = self.pierwszyOrganizm
        while (tmp is not None):
            if (tmp.getDelay()):
                tmp.setDelay(False)
            else:
                tmp.akcja()
            tmp = tmp.getNext()
        self.rysuj_plansze()
        self.text.setText(self.wiadomosc)


    def rysuj_plansze(self):
        for i in range(0,self.wysokosc):
            for j in range(0,self.szerokosc):
                if(self.getPlansza(i,j)=='Y'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('czlowiek.png'))
                elif(self.getPlansza(i,j)=='W'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('wilk.png'))
                elif (self.getPlansza(i, j) == 'O'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('owca.png'))
                elif (self.getPlansza(i, j) == 'L'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('lis.png'))
                elif (self.getPlansza(i, j) == 'Z'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('zolw.png'))
                elif (self.getPlansza(i, j) == 'A'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('antylopa.png'))
                elif (self.getPlansza(i, j) == 'C'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('cyber_owca.jpg'))
                elif (self.getPlansza(i, j) == 'T'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('trawa.png'))
                elif (self.getPlansza(i, j) == 'M'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('mlecz.png'))
                elif (self.getPlansza(i, j) == 'G'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('guarana.jpg'))
                elif (self.getPlansza(i, j) == 'J'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('wilcze_jagody.png'))
                elif (self.getPlansza(i, j) == 'B'):
                    self.buttons[(i, j)].setIcon(QtGui.QIcon('barszcz_sosnowskiego.png'))
                else:
                    self.buttons[(i, j)].setIcon(QtGui.QIcon(None))




    def getWysokosc(self):
        return self.wysokosc

    def getSzerokosc(self):
        return self.szerokosc

    def setWysokosc(self, wys):
        self.wysokosc = wys

    def setSzerokosc(self, sze):
        self.szerokosc = sze

    def getPlansza(self,  wys, sze):
        if(wys >= 0 and wys < self.wysokosc and sze >= 0 and sze < self.szerokosc):
            return self.plansza[wys][sze]
        else:
            return '?'

    def getNumerTury(self):
        return self.numer_tury

    def setNumerTury(self, n):
        self.numer_tury = n

    def getPierwszyOrganizm(self):
        return self.pierwszyOrganizm

    def dodajDoPlanszy(self, wys, sze, zn):
        if (wys < self.wysokosc and sze < self.szerokosc and wys >= 0 and sze >= 0):
            self.plansza[wys][sze] = zn

    def incrementIloscOrganizmow(self):
        self.ilosc_organizmow+=1

    def decrementIloscOrganizmow(self):
        self.ilosc_organizmow-=1

    def getIloscOrganizmow(self):
        return self.ilosc_organizmow

    def dodajOrganizm(self, organizm):

        if (self.pierwszyOrganizm == None):
            organizm.setNext(None)
            self.pierwszyOrganizm = organizm
        else:
            tmp = self.pierwszyOrganizm
            dodanie = False
            while (tmp is not None):
                if (tmp == self.pierwszyOrganizm and tmp.getInicjatywa() < organizm.getInicjatywa()):
                    self.pierwszyOrganizm = organizm
                    organizm.setNext(tmp)
                    dodanie = True
                    break
                elif (tmp.getNext()!=None and tmp.getNext().getInicjatywa() < organizm.getInicjatywa()):
                    organizm.setNext(tmp.getNext())
                    tmp.setNext(organizm)
                    dodanie = True
                    break
                tmp = tmp.getNext()
            if (not dodanie):
                tmp2 = self.pierwszyOrganizm
                while (tmp2 != None):
                    if (tmp2.getNext() == None):
                        tmp2.setNext(organizm)
                        organizm.setNext(None)
                    tmp2 = tmp2.getNext()

    def usunOrganizm(self, organizm):
        if (self.pierwszyOrganizm == organizm):
            self.pierwszyOrganizm = organizm.getNext()
        else:
            tmp = self.pierwszyOrganizm
            while (tmp is not None):
                if (tmp.getNext() == organizm):
                    tmp.setNext(tmp.getNext().getNext())
                    break
                tmp = tmp.getNext()

    def dodajWiadomosc(self, komunikat):
        self.wiadomosc += komunikat

    def zapiszSwiat(self):
        file = open("swiat.txt", "w")
        wysokosc = self.getWysokosc()
        szerokosc = self.getSzerokosc()
        tmp = self.getPierwszyOrganizm()
        numer_tury = self.getNumerTury()
        file.write(str(wysokosc) + " " + str(szerokosc) + " " + str(numer_tury) +" "+ '\n')
        while (tmp is not None):
            file.write(str(tmp.getSymbol()) + " " + str(tmp.getPolozenie_y()) + " " + str(tmp.getPolozenie_x()) + " " + str(tmp.getSila()))
            if (tmp.getSymbol() == 'Y'):
                c = tmp
                file.write(" "+str(c.getMocSpecjalna()) + " "+str(c.getCooldown())+" "+str(c.getLiczbaTurMocy())+" "+str(c.getLiczbaTurCooldown()) )
            tmp = tmp.getNext()
            file.write(" "+'\n')
        file.close()
        pass

    def wczytajSwiat(self):
        s1 = None
        isFile = False
        i = 0
        moc_specjalna = 0
        cooldown = False
        liczba_tur_mocy = 0
        liczba_tur_cooldown = 0
        tmp = None
        with open("swiat.txt",'r') as file:
            isFile = True
            for line in file:
                line_split = line.split(" ")
                if (i == 0):
                    wysokosc, szerokosc, numer_tury , znak_nowej_lini = line_split
                    s1 = Swiat(int(wysokosc), int(szerokosc))
                    s1.setNumerTury(int(numer_tury))
                else:
                    znak = line_split[0]
                    polozenie_y = int(line_split[1])
                    polozenie_x = int(line_split[2])
                    sila = int(line_split[3])

                    if(znak == 'Y'):
                        moc_specjalna = int(line_split[4])
                        cooldown = line_split[5]
                        liczba_tur_mocy = int(line_split[6])
                        liczba_tur_cooldown = int(line_split[7])
                    if (znak == 'A'):
                        tmp = Antylopa(s1)
                    elif (znak == 'C'):
                        tmp = Cyber_owca(s1)
                    elif (znak == 'L'):
                        tmp = Lis(s1)
                    elif (znak == 'O'):
                        tmp = Owca(s1)
                    elif (znak == 'W'):
                        tmp = Wilk(s1)
                    elif (znak == 'Z'):
                        tmp = Zolw(s1)
                    elif (znak == 'T'):
                        tmp = Trawa(s1)
                    elif (znak == 'M'):
                        tmp = Mlecz(s1)
                    elif (znak == 'G'):
                        tmp = Guarana(s1)
                    elif (znak == 'J'):
                        tmp = Wilcze_Jagody(s1)
                    elif (znak == 'B'):
                        tmp = Barszcz_Sosnowskiego(s1)
                    elif(znak == 'Y'):
                        tmp = Czlowiek(s1)
                    if (tmp is not None):
                        if (tmp.getSymbol() == 'Y'):
                            tmp.setCooldown(cooldown)
                            tmp.setLiczbaTurCooldown(liczba_tur_cooldown)
                            tmp.setLiczbaTurMocy(liczba_tur_mocy)
                            tmp.setMocSpecjalna(moc_specjalna)
                        s1.dodajDoPlanszy(tmp.getPolozenie_y(), tmp.getPolozenie_x(), ' ')
                        tmp.setPolozenie_y(polozenie_y)
                        tmp.setPolozenie_x(polozenie_x)
                        tmp.setSila(sila)
                        s1.dodajDoPlanszy(tmp.getPolozenie_y(), tmp.getPolozenie_x(), tmp.getSymbol())

                i+=1
        if(isFile):
            self.close()
            s1.rysuj_plansze()


    def dodajZwierze(self):
        zn = 'W'
        x, y = 10, 10
        button = self.sender()
        name = button.objectName().split(",", 1)
        y, x = name
        y = int(y)
        x = int(x)
        zn, ok = QtGui.QInputDialog.getText(self, "Wysokosc", """Podaj znak odpowiadajacy danemu zwierzeciu""")
        if(self.getPlansza(y, x) == ' '):
            tmp = None
            if (zn == 'A'):
                tmp = Antylopa(self)
            elif (zn == 'C'):
                tmp = Cyber_owca(self)
            elif (zn == 'L'):
                tmp = Lis(self)
            elif (zn == 'O'):
                tmp = Owca(self)
            elif (zn == 'W'):
                tmp = Wilk(self)
            elif (zn == 'Z'):
                tmp = Zolw(self)
            elif (zn == 'T'):
                tmp = Trawa(self)
            elif (zn == 'M'):
                tmp = Mlecz(self)
            elif (zn == 'G'):
                tmp = Guarana(self)
            elif (zn == 'J'):
                tmp = Wilcze_Jagody(self)
            elif (zn == 'B'):
                tmp = Barszcz_Sosnowskiego(self)

            if(tmp is not None):
                self.dodajDoPlanszy(tmp.getPolozenie_y(), tmp.getPolozenie_x(), ' ')
                tmp.setPolozenie_x(x)
                tmp.setPolozenie_y(y)
                tmp.setDelay(True)
                self.dodajDoPlanszy(tmp.getPolozenie_y(), tmp.getPolozenie_x(), tmp.getSymbol())
                self.rysuj_plansze()

    def umiescOrganizmy(self):
        wilk = Wilk(self)
        owca = Owca(self)
        trawa = Trawa(self)
        guarana = Guarana(self)
        mlecz = Mlecz(self)
        jagody = Wilcze_Jagody(self)
        barszcz = Barszcz_Sosnowskiego(self)
        cyber = Cyber_owca(self)
        zolw = Zolw(self)
        lis = Lis(self)
        wilk2 = Wilk(self)
        wilk3 = Wilk(self)
        owca2 = Owca(self)
        owca3 = Owca(self)
        antylopa = Antylopa(self)
        czlowiek = Czlowiek(self)
        self.rysuj_plansze()

    def getRuch(self):
        return self.ruch

    def keyReleaseEvent(self, e):
        try:
            res_key = {
                Qt.Key_Q: 'a',
                Qt.Key_Left: Czlowiek_Ruch.LEWO,
                Qt.Key_Right: Czlowiek_Ruch.PRAWO,
                Qt.Key_Up: Czlowiek_Ruch.GORA,
                Qt.Key_Down: Czlowiek_Ruch.DOL
            }[e.key()]
            if(res_key=='a'):
                if (not self.qPressed):
                    self.qPressed = True
                else:
                    self.qPressed = False
            else:
                self.ruch = res_key
        except KeyError:
            pass

    def UsunOrganizmy(self):
        tmp = self.getPierwszyOrganizm()
        while(tmp is not None):
            self.usunOrganizm(tmp)
            tmp = tmp.getNext()


