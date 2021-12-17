# Импортируем библиотеки
import sys
import sqlite3
import time

from StyleSheet import appStyle, formStyle

from PyQt5 import uic  # Импортируем uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)  # Загружаем дизайн

        self.setWindowTitle("Student It Cube")
        self.setStyleSheet(formStyle)

        self.pushButton.clicked.connect(self.inter)

    def inter(self):
        # Функция открытия другого окна
        self.cams = Window()
        self.cams.show()
        self.close()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн

        self.setWindowTitle("Student It Cube")
        self.setStyleSheet(appStyle)

        self.menu.setStyleSheet("""background-color: #000000;
                                        border: 2px solid #1B1B1B;""")
        self.cube.setStyleSheet("""color: #FFFFFF;""")

        self.showFullScreen()

        self.cow.clicked.connect(self.coworking)
        self.pas.clicked.connect(self.admittance)
        self.out.clicked.connect(self.close)

    def coworking(self):
        # Функция открытия другого окна
        self.cams = Cowork()
        self.cams.show()
        self.close()

    def admittance(self):
        self.cams = Admit()
        self.cams.show()
        self.close()



class Cowork(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coworking.ui', self)  # Загружаем дизайн

        self.setWindowTitle("Student It Cube")
        self.setStyleSheet(appStyle)

        self.menu.setStyleSheet("""background-color: #000000;
                                        border: 2px solid #1B1B1B;""")
        self.cube.setStyleSheet("""color: #FFFFFF;""")

        self.showFullScreen()

        self.man.clicked.connect(self.main)
        self.pas.clicked.connect(self.admittance)
        self.out.clicked.connect(self.close)

    def main(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def admittance(self):
        self.cams = Admit()
        self.cams.show()
        self.close()


class Admit(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pas.ui', self)  # Загружаем дизайн

        self.setWindowTitle("Student It Cube")
        self.setStyleSheet(appStyle)

        self.menu.setStyleSheet("""background-color: #000000;
                                        border: 2px solid #1B1B1B;""")
        self.cube.setStyleSheet("""color: #FFFFFF;""")

        self.showFullScreen()

        self.man.clicked.connect(self.main)
        self.cow.clicked.connect(self.coworking)
        self.out.clicked.connect(self.close)

    def main(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def coworking(self):
        self.cams = Cowork()
        self.cams.show()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Start()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
