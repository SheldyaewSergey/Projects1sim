# 1. Дан целочисленный список размера N. Увеличить все нечетные числа, содержащиеся в
# списке, на исходное значение последнего нечетного числа. Если нечетные числа в
# списке отсутствуют, то оставить список без изменений.

def input_number():
    while True:
        try:
            num = int(input("»>"))
            break
        except ValueError:
            print("Надо ввести число")
    return num


# Функция для проверки и составления списка


n = int(input("Введите длинну списка »>"))
numbers = []
for _ in range(n):
    numbers.append(input_number())
# Создаем список из n введенных чисел

b = 0
for odd in numbers:
    b += 1
    a = odd % 2
    odd = []
    if a == 1:
        continue
    else:
        odd = odd[b] + odd[-1]
