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

        self.Fontn.clicked.connect(self.run)

        data = ('Текст (от лат. textus — ткань; сплетение, сочетание) — зафиксированная на каком-либо материальном носителе человеческая мысль; в общем плане связная и полная последовательность символов.Существуют две основные трактовки понятия «текст»: имманентная (расширенная, философски нагруженная) и репрезентативная (более частная). /'
                '222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222  '
                '33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333/')

        a = (re.findall(r'(.{100})', data))

        if self.next:
            for i in range(len(a)):
                i = 0
                #a = (re.findall(r'(.{100})', data))
                g = textwrap.fill(a[i + 1], width=83)
                self.label.setText(g)

        r = textwrap.fill(a, width=83)

        self.label.setText(r)

        self.show()

    def run(self):
        gg = data
        font, ok = QFontDialog.getFont()
        if ok:
            data.setFont(font)
            a = (re.findall(r'(.{100})', data))
            r = textwrap.fill(a, width=83)
            self.label.setText(r)


    def run2(self):
        data = textwrap.fill(self.data, width=83)
        i, okBtnPressed = QInputDialog.getInt(self, 'Размер шрифта', 'Выберите размер шрифта', 14, 8, 16)
        if okBtnPressed:
            if i == '16':
                data.setFont(QtGui.QFont("Courier", 16, QtGui.QFont.Bold))
                data.adjustSize()




if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SP()
    ex.show()
    sys.exit(app.exec())
