n = input("Введите число >>> ")
flag = False
for i in n:
    if not i.isdigit():
        continue
    a = int(i) % 2
    if a == 1:
        flag = True
        break
if flag:
    print("В числе есть нечетная цифра")
