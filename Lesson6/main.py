import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import menu

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = menu.Ui_h()
    ui.setupUi(MainWindow)
    ui.lobster.valueChanged.connect(checkTotal)
    ui.salmon.valueChanged.connect(checkTotal)
    ui.salad.valueChanged.connect(checkTotal)
    ui.soup.valueChanged.connect(checkTotal)
    ui.crab.valueChanged.connect(checkTotal)
    ui.tuna.valueChanged.connect(checkTotal)
    MainWindow.show()

def checkTotal():
    price = {
        "lobster": 100,
        "tuna": 150,
        "salmon": 150,
        "salad": 50,
        "soup": 10,
        "crab": 100
    }
    totalMoney = 0
    # Tinh so luong tung loai 
    totalMoney += price["lobster"] * int(ui.lobster.text())
    totalMoney += price["tuna"] * int(ui.tuna.text())
    totalMoney += price["salmon"] * int(ui.salmon.text())
    totalMoney += price["salad"] * int(ui.salad.text())
    totalMoney += price["soup"] * int(ui.soup.text())
    totalMoney += price["crab"] * int(ui.crab.text())
    ui.total_money.setText(str(totalMoney))

#Run app
homeUi()
sys.exit(app.exec())
