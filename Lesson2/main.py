import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import lesson2

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = lesson2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_signup.clicked.connect(sign_up)
    MainWindow.show()

def sign_up():
    print('successful')

#Run app
homeUi()
sys.exit(app.exec())

# Lưu ý: chuột phải vào folder chứa 2 file này, chọn Open .... terminal
# Câu lệnh convert ui: pyuic6 -x lesson6.ui -o lesson6.py
# Câu lệnh convert qrc: pyside6-rcc img.qrc -o img_rc.py