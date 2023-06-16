from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from sympy import *
import numpy
from PyQt5.QtWidgets import QMessageBox, QMenuBar, QMenu, QFileDialog

class Ui_CalcWindow(object):
    def setupCalcUi(self, CalcWindow):
        CalcWindow.setObjectName("MainWindow")
        CalcWindow.resize(350, 450)
        CalcWindow.setMinimumSize(QtCore.QSize(350, 450))
        CalcWindow.setMaximumSize(QtCore.QSize(350, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/integral.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CalcWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CalcWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 270, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 320, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(231, 231, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "    background-color: rgb(212, 226, 255);\n"
                                        "    transition: .3s;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 370, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("text-align: center;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        CalcWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalcWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        CalcWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(CalcWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(CalcWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(CalcWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(CalcWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateCalcUi(CalcWindow)
        QtCore.QMetaObject.connectSlotsByName(CalcWindow)

        self. action.triggered.connect(lambda: self.open_file())
        self. action_2.triggered.connect(lambda: self.save_file())
        self. action_3.triggered.connect(lambda: self.open_menu())
        self. action_4.triggered.connect(lambda: self.open_help())


    def retranslateCalcUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Интеграл"))
        self.label_2.setText(_translate("MainWindow", "Введите функцию: "))
        self.label.setText(_translate("MainWindow", "y="))
        self.label_3.setText(_translate("MainWindow", "Введите границы:"))
        self.label_4.setText(_translate("MainWindow", "a="))
        self.label_5.setText(_translate("MainWindow", "b="))
        self.label_6.setText(_translate("MainWindow", "Количество прямоугольников:"))
        self.pushButton_2.setText(_translate("MainWindow", "Вычислить"))
        self.label_7.setText(_translate("MainWindow", "S="))
        # self.menu.setTitle(_translate("MainWindow", "Файл"))
        # self.action.setText(_translate("MainWindow", "Открыть"))
        # self.action_2.setText(_translate("MainWindow", "Сохранить"))
        # self.menu_2.setTitle(_translate("MainWindow", "Меню"))
        # self.action.setText(_translate("MainWindow", "Справка"))
        # self.action_2.setText(_translate("MainWindow", "Главное меню"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Главное меню"))
        self.action_4.setText(_translate("MainWindow", "Справка"))

        self.pushButton_2.clicked.connect(self.result)

    def open_file(self):
        file_ = QFileDialog.getOpenFileName()[0]

        try:
            with open(file_, 'r') as file:
                try:
                    data = file.read().split(' ')
                    a = float(data[1])
                    b = float(data[2])
                    n = int(data[3])
                    self.lineEdit.setText(data[0])
                    self.lineEdit_2.setText(str(a))
                    self.lineEdit_3.setText(str(b))
                    self.lineEdit_4.setText(str(n))
                except:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка!")
                    error.setText("Входные данные имеют неверный вормат")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Ok)
                    error.exec_()

        except FileNotFoundError:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Не удалось открыть файл")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def save_file(self):
        file_ = QFileDialog.getSaveFileName()[0]
        try:
            # data = self.lineEdit.text() + " " + self.lineEdit_2.text() + " " + self.lineEdit_3.text() + " " + self.lineEdit_4.text()
            data = self.label_7.text()[2:]
            with open(file_, 'w') as file:
                file.write(data)
            error = QMessageBox()
            error.setWindowTitle("Соханение")
            error.setText("Файл успешно сохранен!")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        except FileNotFoundError:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Не удалось сохранить файл")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def open_menu(self):
        CalcWindow.close()
        MenuWindow.show()

    def open_help(self):
        HelpWindow.show()

    def result(self):
        try:
            func = self.lineEdit.text()
            a = float(self.lineEdit_2.text())
            b = float(self.lineEdit_3.text())
            n = int(self.lineEdit_4.text())
            square = 0.0
            step = (b - a) / n
            for x in numpy.arange(a, b, step):
                square = square + step * eval(func)
            self.label_7.setText("S=" + str(round(square, 5)))
        except:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Неверные данные")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.setDetailedText("Введены некорректные данные! Ознакомтесь со справкой (пункт \"меню\" на верхней панеле).")
            error.exec_()


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MainWindow")
        MenuWindow.resize(300, 350)
        MenuWindow.setMinimumSize(QtCore.QSize(300, 350))
        MenuWindow.setMaximumSize(QtCore.QSize(300, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/integral.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuWindow.setWindowIcon(icon)
        MenuWindow.setBaseSize(QtCore.QSize(300, 350))
        MenuWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 226, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
                                       "{\n"
                                       "    background-color: rgb(231, 231, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover\n"
                                       "{\n"
                                       "    background-color: rgb(212, 226, 255);\n"
                                       "    transition: .3s;\n"
                                       "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
                                       "{\n"
                                       "    background-color: rgb(231, 231, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover\n"
                                       "{\n"
                                       "    background-color: rgb(212, 226, 255);\n"
                                       "    transition: .3s;\n"
                                       "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(24, 280, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MenuWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MenuWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateMenuUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

        self. action.triggered.connect(lambda: self.open_help())

    def retranslateMenuUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Интеграл"))
        self.pushButton_2.setText(_translate("MainWindow", "О разработчике"))
        self.pushButton.setText(_translate("MainWindow", "Вычислить площадь"))
        self.label.setText(_translate("MainWindow", "Меню"))
        self.label_2.setText(_translate("MainWindow", "© 2021 Все права защищены."))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Справка"))

        self.pushButton.clicked.connect(self.open_calc)
        self.pushButton_2.clicked.connect(self.open_about)

    def open_calc(self):
        MenuWindow.close()
        CalcWindow.show()

    def open_about(self):
        AboutWindow.show()

    def open_help(self):
        HelpWindow.show()


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("MainWindow")
        HelpWindow.resize(561, 394)
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 561, 391))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/help.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpWindow.setWindowIcon(icon)
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateHelpUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateHelpUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Справка"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">1.Описание</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Приложение предназначено для вычисления определенного интеграла (нахождение площади фигуры, ограниченной какой-либо функцией сверху на указанном промежутке методом прямоугольников). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2.Начало работы</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Для начала работы с программой необходимо кликнуть по кнопке «Вычислить площадь», после чего у вас откроется окно, на котором вы уже можете начать работать. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#333333;\">3.</span><span style=\" font-size:8pt; font-weight:600;\">Описание параметров</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Для вычисления площади вам потребуется ввести функцию согласно правилам языка Python (все возможные операции будут представлены ниже), параметры a и b, отвечающие за границы фигуры по координате абсцисс – Х (икс), a, соответственно, левая граница, b – правая, и параметр n, отвечающий за количество прямоугольников, на которое будет разбита фигура для вычисления площади (чем больше прямоугольников, тем выше точность вычисления). После введения всех параметров нажмите на кнопку «Вычислить» и в низу окна вы увидите результат. Если у вас возникла ошибка, еще раз ознакомьтесь со справкой, кликнув на пункт «Меню» на панели инструментов в левом верхнем углу окна и нажав кликнув на справку, в частности, с правилом записи функции. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">4.</span><span style=\" font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Загрузить данные из файла</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Если у вас имеется файл с входными данными, кликните на пункт «Файл» на панели инструментов, выберите пункт «Открыть», в открывшимся проводнике выберите необходимый файл и нажмите на кнопку «Открыть». После чего можете вычислить результат. Данные в файле должны быть записаны в следующем</span><span style=\" font-size:8pt; color:#000000; background-color:#ffffff;\"> </span><span style=\" font-size:8pt;\">формате:&lt;функция&gt;пробел&lt;левая_граница&gt;пробел&lt;правая_граница&gt;пробел&lt;левая граница&gt;пробел&lt;количество прямоугольников&gt;. Например: sqrt(x) 2 4 50. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">5.</span><span style=\" font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Возможные операции для записи функции: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">a. </span><span style=\" font-size:8pt; color:#000000; background-color:#ffffff;\">x**&lt;степень&gt;, пример x**3 (икс в кубе).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">b. </span><span style=\" font-size:8pt; color:#000000; background-color:#ffffff;\">sqrt(x): корень из икса).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">c. sin(x) (синус &quot;x&quot;). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#333333;\">d. cos(x) (косинус &quot;x&quot;).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#333333;\">e. tan(x) (тангенс &quot;x&quot;).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#333333;\">f. asin(x) (арксинус &quot;x&quot;).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#333333;\">g. acos(x) (арккосинус &quot;x&quot;).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">h. atan(x) (арктангенс &quot;x&quot;). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">i. </span><span style=\" font-size:8pt; color:#000000; background-color:#ffffff;\">log(&lt;основание&gt;,x) (логарифм x по указанному основанию).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">j. </span><span style=\" font-size:8pt; color:#000000; background-color:#ffffff;\">exp(x) (экспонента).</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">6.</span><span style=\" font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Сохранение результата в файл</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#000000; background-color:#ffffff;\">Введя данные и вычислив результат, вы можете его сохранить в файл, для этого кликните на пункт «Файл» на панели инструментов, выберите пункт «Сохранить», выберите место для сохранения в открывшимся проводнике и нажмите на кнопку «Сохранить».</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">7.</span><span style=\" font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Возврат в меню</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#000000; background-color:#ffffff;\">Что бы вернуть в главное меню, нажмите на пункт «Меню» на панели инструментов и выберите «Главное меню».</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">8.</span><span style=\" font-size:8pt; font-weight:600;\">О разработчике</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">В клавном меню, кликнув по кнопеи &quot;О разрабочике&quot; находится вся информация о разработчике. По вопросам сотрудничества звоните или пишите по указаной контактной информации. Также, если вы заметите какие-либо ошибки, то обязательно свяжитесь с нами по почте.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span><span style=\" font-size:8pt;\"> </span></p></body></html>"))


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("MainWindow")
        AboutWindow.resize(300, 350)
        AboutWindow.setMinimumSize(QtCore.QSize(300, 350))
        AboutWindow.setMaximumSize(QtCore.QSize(300, 350))
        self.centralwidget = QtWidgets.QWidget(AboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 301, 351))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateAboutUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateAboutUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "О разрабочике"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#333333; background-color:#ffffff;\">О разработчике</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Иванов Иван Иванович</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">По вопросам сотрудничества писать на почту</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:ivanov.i.i@mail.ru\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">ivanov.i.i@mail.ru</span></a><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Или звонить по телефону в рабочее время (пн-пт с 09:00 до 16:00 по Пермскому времени)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">+7 908 269-25-19</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))


if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)

    CalcWindow = QtWidgets.QMainWindow()
    menu_ui = Ui_CalcWindow()
    menu_ui.setupCalcUi(CalcWindow)

    HelpWindow = QtWidgets.QMainWindow()
    help_ui = Ui_HelpWindow()
    help_ui.setupUi(HelpWindow)

    AboutWindow = QtWidgets.QMainWindow()
    about_ui = Ui_AboutWindow()
    about_ui.setupUi(AboutWindow)

    MenuWindow.show()
    sys.exit(app.exec_())
