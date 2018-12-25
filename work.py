import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLCDNumber, QLineEdit, QMainWindow, QTextEdit, QTextEdit, QFileDialog, \
    QInputDialog, QListWidget
from PyQt5 import uic
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('Library')

        # self.label = QLabel
        # self.label.setText('Библиотека')
        # self.label.move(100, 30)

        uic.loadUi('text1.ui', self)

        self.open.clicked.connect(self.run1)

        # self.delete2 = QPushButton(self)
        # self.delete2.move(400, 200)
        # self.delete2.setText('Удалить из библиотеки')
        # self.delete2.clicked.connect(self.run)
        #
        # self.read = QPushButton(self)
        # self.read.move(350, 750)
        # self.read.setText('Начать читать')
        # self.read.clicked.connect(self.run)

        self.show()

    def init(self):
        self.lib = Library()

    def run1(self):
        book = self.lib.open()
        self.libw.addItems([book.link for book in self.lib.librarys])
        # self.open.clicked.connect(self.run1)
        # self.delete2 = self.label("text.ui").pop(self.event)

    def run2(self):
        self.lib.delete()

    def run3(self):
        self.lib.start()


class Library():
    def __init__(self):
        self.librarys = []

    def open(self):
        fname = QFileDialog.getOpenFileName()[0]
        f = open(fname, 'r')

        with f:
            data = f.read()
            # self.textEdit.setText(data)

        book = Book(fname, data)
        self.librarys.append(book)
        return book

    def delete(self):
        index_of_delete = 0
        self.librarys.pop(index=index_of_delete)
        self.libw.removeItems(index_of_delete)

    def start(self):
        pass


class Book():
    def __init__(self, link, stroka):
        self.link = link
        self.page = 1
        self.stroka = stroka


#     def initUI(self):
#         uic.loadUi('qtlab2.ui', self)
#         self.button2.clicked.connect(self.run)
#         self.group1.buttonClicked.connect(self.run2)
#         self.group2.buttonClicked.connect(self.run2)
#         self.group3.buttonClicked.connect(self.run2)
#         self.data = {
#             self.group1: 'Нет цвета',
#             self.group2: 'Нет цвета',
#             self.group3: 'Нет цвета'
#         }
#
#
#     def run(self):
#         self.label.setText('Цвета: {}, {}, {}'.format(*self.data.values()))
#
#     def run2(self, button2):
#         self.data[self.sender()] = button2.text()
#
#
#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
