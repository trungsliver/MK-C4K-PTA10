# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 5, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 220, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 180, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(160, 100, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(160, 140, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(160, 260, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_confirm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_confirm.setGeometry(QtCore.QRect(160, 300, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_confirm.setFont(font)
        self.lineEdit_confirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 180, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(160, 220, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 220, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(360, 220, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 340, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 180, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(500, 100, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 150, 180, 200))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.btn_signup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(250, 380, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(25)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("QPushButton{\n"
"    border: 1px solid rgb(170, 65, 67);\n"
"    border-radius: 20px;\n"
"    background-color: rgb(170, 65, 67);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(170, 65, 67);\n"
"    background-color: white;\n"
"}")
        self.btn_signup.setObjectName("btn_signup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIGN UP"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_4.setText(_translate("MainWindow", "Confirm:"))
        self.label_5.setText(_translate("MainWindow", "Gender:"))
        self.label_6.setText(_translate("MainWindow", "DOB:"))
        self.label_7.setText(_translate("MainWindow", "Username:"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "username"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "email adress"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "password"))
        self.lineEdit_confirm.setPlaceholderText(_translate("MainWindow", "confirm password"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.radioButton_3.setText(_translate("MainWindow", "Others"))
        self.checkBox.setText(_translate("MainWindow", "I agree with terms conditions and privacy policy"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Others"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "write notes here !!!"))
        self.btn_signup.setText(_translate("MainWindow", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())