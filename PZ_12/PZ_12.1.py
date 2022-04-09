# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QCheckBox,\
    QPushButton, QPlainTextEdit, QListWidget, QListWidgetItem
import sys

# create application and main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Регистрационная страница Клуба любителей фантастики")
window.setFixedWidth(700)
window.setFixedHeight(500)

# create widgets for main window
label = QLabel(window)
label.setFont(QFont('Times New Roman', 20))
label.setText("Регистрационная страница Клуба любителей фантастики")
label.move(10, 10)

info_lb = QLabel("Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой.", window)
info_lb.move(10, 50)
info_lb.setFont(QFont('Times New Roman', 12))

log_lb = QLabel("Введите регистрационное имя:", window)
log_lb.move(10, 105)
log_lb.setFont(QFont('Times New Roman', 12))

log_tx = QPlainTextEdit(window)
log_tx.move(250, 100)
log_tx.resize(170, 25)

pass_lb = QLabel("Введите пароль:", window)
pass_lb.move(10, 140)
pass_lb.setFont(QFont('Times New Roman', 12))

pass_tx = QPlainTextEdit(window)
pass_tx.move(250, 135)
pass_tx.resize(170, 25)

conf_pass_lb = QLabel("Подтвердите пароль:", window)
conf_pass_lb.move(10, 175)
conf_pass_lb.setFont(QFont('Times New Roman', 12))

conf_pass_tx = QPlainTextEdit(window)
conf_pass_tx.move(250, 170)
conf_pass_tx.resize(170, 25)

# create radio buttons for old
rbtn_lb = QLabel("Ваш возраст:", window)
rbtn_lb.setFont(QFont('Times New Roman', 12))
rbtn_lb.move(10, 213)

rbtn_1 = QRadioButton("До 20", window)
rbtn_1.move(120, 215)
rbtn_2 = QRadioButton("20-30", window)
rbtn_2.move(180, 215)
rbtn_3 = QRadioButton("30-50", window)
rbtn_3.move(240, 215)
rbtn_4 = QRadioButton("Старше 50", window)
rbtn_4.move(300, 215)

# create radio buttons for language info
btn_lb = QLabel("На каких языках читаете:", window)
btn_lb.setFont(QFont('Times New Roman', 12))
btn_lb.move(10, 253)
btn_rus = QCheckBox("Русский", window)
btn_rus.move(200, 255)
btn_eng = QCheckBox("Английский", window)
btn_eng.move(270, 255)
btn_fr = QCheckBox("Французский", window)
btn_fr.move(360, 255)
btn_deu = QCheckBox("Немецкий", window)
btn_deu.move(455, 255)

format_lb = QLabel("Какой формат данных является для Вас предпочтительным", window)
format_lb.move(10, 295)
format_lb.setFont(QFont('Times New Roman', 12))

format_bar = QListWidget(window)
format_bar.move(10, 315)
format_bar.resize(100, 35)
QListWidgetItem("HTML", format_bar)
QListWidgetItem("Plain text", format_bar)

autor_lb = QLabel("Ваши любимые авторы:", window)
autor_lb.move(10, 365)
autor_lb.setFont(QFont('Times New Roman', 12))
autor_tx = QPlainTextEdit(window)
autor_tx.move(10, 385)
autor_tx.resize(300, 65)

# ok and cancel buttons
ok_btn = QPushButton("Ок", window)
ok_btn.move(10, 460)
ok_btn.resize(40, 25)
cancel_btn = QPushButton("Отменить", window)
cancel_btn.move(50, 460)
cancel_btn.resize(80, 25)

#   Run application
window.show()
app.exec()