# 31. Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.
import re

with open('price.txt', 'r', encoding='utf-8') as a:
    text = a.read()
    # Создание шаблонов
    b1 = re.findall(r"[0-9]+ руб. [0-9]+ коп.", text)
    b2 = re.findall(r"[0-9]+ копеек", text)
    b3 = re.findall(r"[0-9]+ руб. [0-9]+коп.", text)
    b4 = re.findall(r"[0-9]+руб. [0-9]+ коп.", text)
    b5 = re.findall(r"[0-9]+руб. [0-9]+коп.", text)
    # Обьединение шаблонов
    prc = b1 + b2 + b3 + b4 + b5
    # Вывод
    print(prc)
    # Нахождение кол-ва элементов и вывод полученного числа на экран
    end = len(prc)
    print(f"Всего найдено {end} элементов")
