# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).
from tkinter import *

root = Tk()
root.title("Регистрационная страница")
root.geometry("800x600")
root.resizable(height= False, width= False)

M_title = Label(root, text= "Регистрационная страница Клуба любителей фантастики")
M_title.grid()
F_title = Label(root, text= "Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой")
F_title.grid()

root.mainloop()