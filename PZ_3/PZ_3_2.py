def ff():
# Ввод переменных
    while True:
        try:
            z = int(input("Введите первое число:"))
            x = int(input("Введите второе число:"))
            c = int(input("Введите третье число:"))
            break
        except ValueError:
            print("Введите целые числа!")
    return z, x, c


z, x, c = ff()

if z > x > c or x > z > c:
    a = z + x
elif z > c > x or c > z > x:
    a = z + c
elif x > c > z or c > x > z:
    a = x + c
print(">>>", a)