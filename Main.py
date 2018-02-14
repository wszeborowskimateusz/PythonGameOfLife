from Swiat import Swiat
from PySide import QtGui, QtCore


def main(wys, sze):

    s = Swiat(wys, sze)
    s.umiescOrganizmy()


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.wys = 20
        self.sze = 20
        self.wys, ok = QtGui.QInputDialog.getInteger(self,"Wysokosc", """Podaj wysokosc""")
        self.sze, ok2 = QtGui.QInputDialog.getInteger(self, "Szerokosc", """Podaj szerokosc""")
        if(self.wys == 0):
            self.wys = 20
        if(self.sze == 0):
            self.sze = 20
        main(self.wys, self.sze)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = Window()
    sys.exit(app.exec_())