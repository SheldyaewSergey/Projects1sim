# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из целых
# положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt)
# следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы первой трети:
# Минимальный элемент первой трети:


import random

f1 = open("file101.txt", "w", encoding='utf-8')
f2 = open("file102.txt", "w", encoding='utf-8')
f3 = open("file103.txt", "w", encoding='utf-8')
a = []
b = []
i = 0


while i < 12:
    k = random.randint(-100, 100)
    i += 1
    a.append(k)
while i > 0:
    k1 = random.randint(-100, 100)
    i -= 1
    b.append(k1)

d = a + b
s1 = " ".join(map(str, a))
s2 = " ".join(map(str, b))
s3 = " ".join(map(str, d))
f1.write(s1)
f2.write(s2)
f3.write(s3)  # Элементы первого и второго файлов:
f1.close()
f2.close()
u1 = len(a)
u2 = len(b)

u3 = u1 + u2
u3 = str(u3)
f3.write('\n')
f3.write(u3)  # Количество элементов первого и второго файлов:

f3.write('\n')
d = d[0:9]
s3 = " ".join(map(str, d))
f3.write(s3)  # Элементы первой трети:

f3.write('\n')
d.sort()
d = d[0]
d = str(d)
f3.write(d)  # Минимальный элемент первой трети:
f3.close()
