import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 811, 681))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(840, 40, 331, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(30, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 150, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.horizontalSlider = QtWidgets.QSlider(self.tab)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 230, 231, 22))
        self.horizontalSlider.setMinimum(250)
        self.horizontalSlider.setMaximum(500)
        self.horizontalSlider.setSingleStep(2)
        self.horizontalSlider.setProperty("value", 1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 51, 41))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 300, 231, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 370, 221, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 51, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 360, 51, 41))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 211, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 301, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(30, 140, 211, 41))
        self.checkBox.setObjectName("checkBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 230, 301, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 211, 31))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 630, 321, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 670, 321, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 40, 571, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1248, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск по карте"))
        self.label.setText(_translate("MainWindow", "Карта"))
        self.radioButton.setText(_translate("MainWindow", "Карта"))
        self.radioButton_2.setText(_translate("MainWindow", "Спутник"))
        self.radioButton_3.setText(_translate("MainWindow", "Гибрид"))
        self.label_5.setText(_translate("MainWindow", "Масштаб:"))
        self.label_6.setText(_translate("MainWindow", "Долгота:"))
        self.label_7.setText(_translate("MainWindow", "Широта:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Вид"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Адрес объекта"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Поиск"))
        self.label_2.setText(_translate("MainWindow", "Полный адрес:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Полный адрес объекта"))
        self.checkBox.setText(_translate("MainWindow", "Приписать почтовый индекс"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Информация не найдена."))
        self.label_3.setText(_translate("MainWindow", "Дополнительная информация:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Результат"))
        self.pushButton.setText(_translate("MainWindow", "Искать по введенным параметрам"))
        self.pushButton_2.setText(_translate("MainWindow", "Сброс поискового результата"))
        self.label_4.setText(_translate("MainWindow", "Поиск по карте"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.actionClose.setText(_translate("MainWindow", "Выйти"))


def check_response(response):
    if not response or response.status_code != 200:
        print('[ERROR] Response')
        a = input('...waiting...')
        print(response.content)
        quit()
    else:
        print('[OK] Response')
        return response


geocoder_server = 'http://geocode-maps.yandex.ru/1.x/'
static_server = 'http://static-maps.yandex.ru/1.x/'
org_search_server = 'http://search-maps.yandex.ru/v1/'


class CustomMap(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.points = []

        self.radioButton.setChecked(True)
        self.pushButton.clicked.connect(self.get_map)
        self.radioButton.clicked.connect(self.get_map)
        self.radioButton_2.clicked.connect(self.get_map)
        self.radioButton_3.clicked.connect(self.get_map)

    def stat(self):
        print(self.horizontalSlider.value())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.scale_up()
            self.get_map()
        elif event.key() == Qt.Key_PageDown:
            self.scale_down()
            self.get_map()
        elif event.key() == Qt.Key_Up or event.key() == Qt.Key_W:
            self.up()
            self.get_map()
        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
            self.down()
            self.get_map()
        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_D:
            self.right()
            self.get_map()
        elif event.key() == Qt.Key_Left or event.key() == Qt.Key_A:
            self.left()
            self.get_map()

    def get_map(self):
        req = self.lineEdit.text()
        if req:
            geocoder_params = {'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
                               'geocode': req,
                               'format': 'json'}
            response = check_response(requests.get(geocoder_server, params=geocoder_params))

            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            toponym_coodrinates = toponym["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
            lower = list(map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split()))
            upper = list(map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split()))
            size = str(abs(lower[0] - upper[0])), str(abs(lower[1] - upper[1]))
            self.points.append(",".join([toponym_longitude, toponym_lattitude, 'comma']))
            if self.radioButton.isChecked():
                mode = 'map'
            elif self.radioButton_2.isChecked():
                mode = 'sat'
            elif self.radioButton_3.isChecked():
                mode = 'sat,skl'
            else:
                mode = 'map'
            self.horizontalSlider.setValue(int((5 - float(size[0])) / 0.01))
            map_params = {
                "ll": ",".join([toponym_longitude, toponym_lattitude]),
                "spn": ",".join(size),
                "l": mode,
                'pt': "~".join(self.points)
            }

            map_api_server = "http://static-maps.yandex.ru/1.x/"
            response = check_response(requests.get(map_api_server, params=map_params))
        else:
            scale = self.horizontalSlider.value()
            point = ','.join([self.lineEdit_3.text(), self.lineEdit_4.text()])
            if self.radioButton.isChecked():
                mode = 'map'
            elif self.radioButton_2.isChecked():
                mode = 'sat'
            elif self.radioButton_3.isChecked():
                mode = 'sat,skl'
            else:
                mode = 'map'
            print(5 - 0.01 * scale, scale)
            map_params = {'ll': point,
                          'l': mode,
                          'spn': ','.join([str(5 - 0.01 * scale)] * 2),
                          'pt': "~".join(self.points)}
            response = check_response(requests.get(static_server, params=map_params))
        with open('image.png', mode='wb') as f:
            f.write(response.content)
        self.label.setPixmap(QPixmap('image.png'))

    def scale_up(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() + 1)

    def scale_down(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() - 1)

    def up(self):
        num = float(self.lineEdit_4.text())
        num += 5 - 0.01 * self.horizontalSlider.value()
        self.lineEdit_4.setText(str(num))

    def down(self):
        num = float(self.lineEdit_4.text())
        num -= 5 - 0.01 * self.horizontalSlider.value()
        self.lineEdit_4.setText(str(num))

    def left(self):
        num = float(self.lineEdit_3.text())
        num -= 5 - 0.01 * self.horizontalSlider.value()
        self.lineEdit_3.setText(str(num))

    def right(self):
        num = float(self.lineEdit_3.text())
        num += 5 - 0.01 * self.horizontalSlider.value()
        self.lineEdit_3.setText(str(num))

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.plainTextEdit.setPlainText('Информация не найдена.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CustomMap()
    ex.show()
    app.exec()
    try:
        os.remove('image.png')
    except FileNotFoundError:
        pass
# 37.564931 55.725803
