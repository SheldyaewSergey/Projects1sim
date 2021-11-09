def ff():
    while True:
        try:
            z = int(input("Введите первое число:"))
            x = int(input("Введите второе число:"))
            c = int(input("Введите третье число:"))
            # Ввод переменных
            break
        except ValueError:
            print("Введите целые числа!")
    return z, x, c


# Функция для проверки

z, x, c = ff()

if z == x or c == z or x == c:  # Решение
    print("Треугольник равноберенный")
else:
    print("Треугольник не равнобедренный")
