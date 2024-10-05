import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import signup, login

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

users = ['admin:admin']

def homeUi():
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_signup.clicked.connect(sign_up)
    MainWindow.show()

def login_w():
    global ui
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_login.clicked.connect(login_check)
    MainWindow.show()

def sign_up():
    username = ui.lineEdit_username.text().strip()
    email = ui.lineEdit_email.text().strip()
    passwword = ui.lineEdit_password.text().strip()
    confirm = ui.lineEdit_confirm.text().strip()
    check = True

    # Thiếu thông tin
    if username == '' or email == '' or passwword == '' or confirm == '':
        check = False
        msg_box('Sign up fail', 'Thiếu thông tin')
    # Password không khớp
    elif passwword != confirm:
        check = False
        msg_box('Sign up fail', 'Mật khẩu không khớp')
    # Kiểm tra trùng username
    else:
        # Kiểm ra ký tự tronng username
        for s in username:
            if s == ':':
                check = False
                msg_box('Sign up fail', 'Username không được chứa ký tự ":"')
                break
        for user in users:
            stored_username, stored_password = user.split(':', 1)
            if username == stored_username:
                check = False
                msg_box('Sign up fail', 'Tên đăng nhập đã tồn tại')

    # Kiểm tra xem có đăng ký thành công không
    if check == True:
        # Add tài khoản vào danh sách user
        new_acc = username + ':' + passwword
        users.append(new_acc)
        msg_box('Sign up successful', 'Đăng ký thành công')
        print(users)
        login_w()

def login_check():
    username = ui.lineEdit_username.text().strip()
    password = ui.lineEdit_pass.text().strip()
    check = False
    for user in users:
            stored_username, stored_password = user.split(':', 1)
            if username == stored_username and password == stored_password:
                check = True
    if check == True:
        msg_box('Login successful', 'Đăng nhập thành công')
        homeUi()
    else:
        msg_box('Login fail', 'Đăng nhập không thành công')


def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

#Run app
homeUi()
sys.exit(app.exec())

# Lưu ý: chuột phải vào folder chứa 2 file này, chọn Open .... terminal
# Câu lệnh convert ui: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert ui: pyuic6 -x login.ui -o login.py
# Câu lệnh convert qrc: pyside6-rcc img.qrc -o img_rc.py