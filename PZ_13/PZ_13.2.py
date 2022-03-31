# 2. Из заданной строки отобразить только символы нижнего регистра.
# Использовать библиотеку string. Строка 'In PyCharm, you can specify third-party standalone
# applications and run them as External Tools'.
import string

a = 'In PyCharm, you can specify third-party standalone ' \
    'applications and run them as External Tools'
b = string.ascii_lowercase

for i in a:
    if i in b:
        print(i)
    else:
        continue