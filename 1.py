import sys
import textwrap
import re
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel, QLineEdit, QMainWindow, QInputDialog, QFontDialog
from PyQt5.uic.properties import QtGui


class SP(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('text1.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('Библиотека')

        #self.settings.clicked.connect(self.run)

        self.next.clicked.connect(self.initUI)

        self.Fontn.clicked.connect(self.run2)

        data = ('«Я́ндекс» — российская транснациональная компания, зарегистрированная в Нидерландах и владеющая одноимённой системой поиска в Сети, интернет-порталами и службами в нескольких странах.] '

                'Поисковая система «Яндекс» является четвёртой среди поисковых систем мира по количеству обрабатываемых поисковых запросов (свыше 6,3 млрд в месяц на начало 2014 года)[9].')
        a = (re.findall(r'(.{350})', data))

       # index
        #lib = Library()
        #a[lib.libraries[index].page - 1]

        if self.next:
           for i in range(len(a)):
                a = (re.findall(r'(.{350})', data))

                g = textwrap.fill(a[0], width=83)
                self.label.setText(g)
        else:
            r = textwrap.fill(a[0], width=83)

            self.label.setText(r)

        self.show()

    def run(self):
        pass
    def run2(self):
        label = self.label
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SP()
    ex.show()
    sys.exit(app.exec())