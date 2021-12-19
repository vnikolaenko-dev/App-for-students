import sys
import gspread
import cryptocode

from shutil import copyfile

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from StyleSheet import appStyle, formStyle
from gen_qr import gen_qr
from mail import mail


class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)  # Загружаем дизайн
        self.setFixedSize(800, 500)

        self.setWindowTitle("Student It Cube")
        self.setWindowIcon(QIcon("./system/brain.ico"))
        self.setStyleSheet(formStyle)

        pixmap = QPixmap("""./system/brain.png""")
        self.label_4.setPixmap(pixmap)

        self.pushButton.clicked.connect(self.inter)
        self.pushButton_2.clicked.connect(self.reg)

    def inter(self):
        global data
        self.label_3.setText("Подождите...")
        data = worksheet.get()
        data = {item: [d[index] for d in data[1:]] for index, item in enumerate(data[0])}
        lo = self.login.text()
        pa = self.password.text()
        for i in range(len(data['id'])):
            if lo == cryptocode.decrypt(data['Login'][i], "it*cube") and \
                    pa == cryptocode.decrypt(data['Password'][i], "it*cube") and int(data['Status'][i]):
                name = data['Name'][i] + " " + data['Surname'][i]
                self.label_3.setText("Выполняется вход...")
                gen_qr(lo, pa)
                self.cams = Adm() if int(data['Admin'][i]) else Window(name)
                self.cams.show()
                self.close()
                break
        else:
            self.label_3.setText("Неверный логин и пароль")

    def reg(self):
        self.cams = Reg()
        self.cams.show()
        self.close()


class Adm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('admin.ui', self)  # Загружаем дизайн
        self.showMaximized()

        self.setWindowTitle("Admin It Cube")
        self.setWindowIcon(QIcon("./system/brain.ico"))
        self.setStyleSheet(appStyle)

        self.menu.setStyleSheet("""background-color: #000000;
                                        border: 2px solid #1B1B1B;""")
        self.cube.setStyleSheet("""color: #FFFFFF;""")
        self.pushButton.setStyleSheet(formStyle)
        self.pushButton_2.setStyleSheet(formStyle)
        self.pushButton_3.setStyleSheet(formStyle)
        self.pushButton_5.setStyleSheet("""color: #A6A6A6;""")

        pixmap = QPixmap("""./system/itcube.png""")
        self.label_2.setPixmap(pixmap)

        pixmap = QPixmap("""./system/adbrain.png""")
        self.label.setPixmap(pixmap)
        for i in range(len(data['id'])):
            if int(data['Status'][i]) == 0:
                self.listWidget.addItem(str(cryptocode.decrypt(str(data['Login'][i]), "it*cube")) + ' ' +
                                        str(cryptocode.decrypt(str(data['Password'][i]), "it*cube")) + '\n' + ' ' +
                                        str(cryptocode.decrypt(str(data['Name'][i]), "it*cube")) + ' ' +
                                        str(cryptocode.decrypt(str(data['Surname'][i]), "it*cube")) + '\n' + ' ' +
                                        str(cryptocode.decrypt(str(data['Email'][i]), "it*cube")))
            elif int(data['Admin'][i]) == 0:
                self.listWidget_2.addItem(str(cryptocode.decrypt(str(data['Login'][i]), "it*cube")) + ' ' +
                                          str(cryptocode.decrypt(str(data['Password'][i]), "it*cube")) + '\n' + ' ' +
                                          str(cryptocode.decrypt(str(data['Name'][i]), "it*cube")) + ' ' +
                                          str(cryptocode.decrypt(str(data['Surname'][i]), "it*cube")) + '\n' + ' ' +
                                          str(cryptocode.decrypt(str(data['Email'][i]), "it*cube")))

        self.out.clicked.connect(self.clos)

        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.no)
        self.pushButton_3.clicked.connect(self.deli)
        self.pushButton_4.clicked.connect(self.mer)

    def clos(self):
        self.cams = Start()
        self.cams.show()
        self.close()

    def mer(self):
        self.cams = Merop()
        self.cams.show()
        self.close()

    def confirm(self):
        try:
            selected = self.listWidget.selectedItems()
            for item in selected:
                c = item.text().split()
                self.listWidget_2.addItem(item.text())
                self.listWidget.takeItem(self.listWidget.row(item))
                for i in range(len(data['id'])):
                    if cryptocode.decrypt(data['Login'][i], "it*cube") == c[0]:
                        worksheet.update(f'G{i + 2}', 1)
                        break
                mail("Поздравляем, ваша заявка была подтверждена!\nДобро пожаловать в резиденство It Cube'а!",
                     c[-1])
        except Exception as e:
            print(e)

    def no(self):
        try:
            selected = self.listWidget.selectedItems()
            for item in selected:
                c = item.text().split()
                self.listWidget.takeItem(self.listWidget.row(item))
                for i in range(len(data['id'])):
                    if cryptocode.decrypt(data['Login'][i], "it*cube") == c[0]:
                        worksheet.delete_rows(i + 2)
                        break
                mail("Ваша заявка была отклонена", c[-1])
        except Exception as e:
            print(e)

    def deli(self):
        try:
            selected = self.listWidget_2.selectedItems()
            for item in selected:
                c = item.text().split()
                self.listWidget_2.takeItem(self.listWidget_2.row(item))
                for i in range(len(data['id'])):
                    if cryptocode.decrypt(data['Login'][i], "it*cube") == c[0]:
                        worksheet.delete_rows(i + 2)
                        break
                mail("Вы были исключены из резиденства It Cube'а.", c[-1])
        except Exception as e:
            print(e)


class Merop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('evem.ui', self)  # Загружаем дизайн
        self.showMaximized()

        self.setWindowTitle("Admin It Cube")
        self.setWindowIcon(QIcon("./system/brain.ico"))
        self.setStyleSheet(appStyle)

        self.menu.setStyleSheet("""background-color: #000000;
                                        border: 2px solid #1B1B1B;""")
        self.cube.setStyleSheet("""color: #FFFFFF;""")

        self.pushButton_2.setStyleSheet(formStyle)
        self.pushButton_3.setStyleSheet(formStyle)
        self.pushButton_4.setStyleSheet("""color: #A6A6A6;""")

        pixmap = QPixmap("""./system/itcube.png""")
        self.label_2.setPixmap(pixmap)

        pixmap = QPixmap("""./system/evbrain.png""")
        self.label.setPixmap(pixmap)

        self.worksheet = gspread.service_account(filename='key.json').open_by_url(
            "https://docs.google.com/spreadsheets/d/1_4XzUJbV9o3-BZlEKNg5QiIaZ5v7OKY4lHzDOnsUIfo/edit#gid=0"
        ).worksheet("Лист1")
        self.data = self.worksheet.get()[1:]
        for i in sorted(self.data, key=lambda x: (x[1].split('.')[::-1], x[2]), reverse=True):
            self.listWidget.addItem(
                str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n' + str(i[3]))

        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.deli)

        self.out.clicked.connect(self.clos)
        self.pushButton_5.clicked.connect(self.stu)

    def add(self):
        try:
            self.worksheet.update(f'A{len(self.data) + 2}:D{len(self.data) + 2}', [
                [self.lineEdit_3.text(), self.dateEdit.text(), self.timeEdit.text(), self.textEdit.toPlainText()]])
            self.lineEdit_3.clear()
            self.dateEdit.clear()
            self.timeEdit.clear()
            self.textEdit.clear()
            self.listWidget.clear()
            self.data = self.worksheet.get()[1:]
            for i in sorted(self.data, key=lambda x: (x[1].split('.')[::-1], x[2]), reverse=True):
                self.listWidget.addItem(
                    str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n' + str(i[3]))
        except Exception as e:
            print(e)

    def deli(self):
        try:
            selected = self.listWidget.selectedItems()
            for item in selected:
                self.listWidget.takeItem(self.listWidget.row(item))
                for i, d in enumerate(self.data):
                    if item.text().split() == d:
                        self.worksheet.delete_rows(i + 2)
                        break

        except Exception as e:
            print(e)

    def stu(self):
        self.cams = Adm()
        self.cams.show()
        self.close()

    def clos(self):
        self.cams = Start()
        self.cams.show()
        self.close()


class Reg(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('reg.ui', self)  # Загружаем дизайн
        self.setFixedSize(800, 500)

        self.setWindowTitle("Student It Cube")
        self.setWindowIcon(QIcon("./system/brain.ico"))
        self.setStyleSheet(formStyle)

        pixmap = QPixmap("""./system/brainreg.png""")
        self.label_6.setPixmap(pixmap)

        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.start)

    def submit(self):
        global data
        if not self.login.text() and self.password.text() and self.name.text() and self.surname.text():
            self.label_err.setText('Заполните все поля!')
        elif len(self.login.text()) > 12 or len(self.password.text()) > 12:
            self.label_err.setText('Логин и пароль должны быть короче 12 символов!')
        elif self.login.text() in [cryptocode.decrypt(i, "it*cube") for i in data['Login']]:
            self.label_err.setText('Данный логин уже занят!')
        else:
            worksheet.update(
                f'A{len(data["id"]) + 2}:H{len(data["id"]) + 2}',
                [[int(data["id"][-1]) + 1 if data['id'] else 1, cryptocode.encrypt(self.login.text(), "it*cube"),
                  cryptocode.encrypt(self.password.text(), "it*cube"), cryptocode.encrypt(self.name.text(), "it*cube"),
                  cryptocode.encrypt(self.surname.text(), "it*cube"),
                  0, 0, cryptocode.encrypt(self.email.text(), "it*cube")]])
            data = worksheet.get()
            data = {item: [d[index] for d in data[1:]] for index, item in enumerate(data[0])}
            self.start()

    def start(self):
        self.cams = Start()
        self.cams.show()
        self.close()


class Window(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.showMaximized()

        self.setWindowIcon(QIcon("./system/brain.ico"))
        self.setWindowTitle("Student It Cube")
        self.setStyleSheet(appStyle)

        self.menu.setStyleSheet("""background-color: #000000;
                                        border: 2px solid #1B1B1B;""")
        self.cube.setStyleSheet("""color: #FFFFFF;""")

        self.name.setStyleSheet("""color: #FFFFFF;""")
        self.name.setText(str(cryptocode.decrypt(name.split()[0], "it*cube")) + " "
                          + str(cryptocode.decrypt(name.split()[1], "it*cube")))

        pixmap = QPixmap("""./system/itcube.png""")
        self.label_2.setPixmap(pixmap)

        pixmap = QPixmap("""./system/brain90.png""")
        self.label_3.setPixmap(pixmap)

        # self.showFullScreen()
        worksheet = gspread.service_account(filename='key.json').open_by_url(
            "https://docs.google.com/spreadsheets/d/1_4XzUJbV9o3-BZlEKNg5QiIaZ5v7OKY4lHzDOnsUIfo/edit#gid=0"
        ).worksheet("Лист1")
        data = worksheet.get()[1:]
        for i in data:
            self.listWidget.addItem(
                str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n' + str(i[3]))

        self.cow.clicked.connect(lambda: self.coworking(name))
        self.pas.clicked.connect(lambda: self.admittance(name))
        self.out.clicked.connect(self.close)

    def coworking(self, name):
        # Функция открытия другого окна
        self.cams = Cowork(name)
        self.cams.show()
        self.close()

    def admittance(self, name):
        self.cams = Admit(name)
        self.cams.show()


class Cowork(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('coworking.ui', self)  # Загружаем дизайн
        self.showMaximized()

        self.setWindowTitle("Student It Cube")
        self.setStyleSheet(appStyle)

        self.menu.setStyleSheet("""background-color: #000000;
                                        border: 2px solid #1B1B1B;""")
        self.cube.setStyleSheet("""color: #FFFFFF;""")

        self.showFullScreen()

        self.man.clicked.connect(lambda: self.main(name))
        self.pas.clicked.connect(lambda: self.admittance(name))
        self.out.clicked.connect(self.close)

    def main(self, name):
        self.cams = Window(name)
        self.cams.show()
        self.close()

    def admittance(self, name):
        self.cams = Admit(name)
        self.cams.show()
        self.close()


class Admit(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('pas.ui', self)  # Загружаем дизайн

        self.setWindowTitle("QrCode")
        self.setStyleSheet(appStyle)

        self.download.setStyleSheet(formStyle)
        self.image.setPixmap(QPixmap('qr.png'))
        self.download.clicked.connect(self.load)
        self.image.setPixmap(QPixmap('qr.png').scaled(440, 440))

    def load(self):
        path = QFileDialog.getExistingDirectory(self, 'Выберите куда скачать')
        if path:
            copyfile('qr.png', path + '/qr.png')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    worksheet = gspread.service_account(filename='key.json').open_by_url(
        "https://docs.google.com/spreadsheets/d/16JbE2bMyrs61opmm7No8PrdDDbN3-4lvJbekqS1ix9o/edit#gid=0"
    ).worksheet("Лист1")
    data = worksheet.get()
    data = {item: [d[index] for d in data[1:]] for index, item in enumerate(data[0])}
    app = QApplication(sys.argv)
    form = Start()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
