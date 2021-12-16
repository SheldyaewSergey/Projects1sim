# 2. Дан список A размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент BK равен среднему арифметическому элементов списка
# A с номерами от 1 до K.

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
a = []
for _ in range(n):
    a.append(input_number())
# Создаем список из n введенных чисел
i = 1
b = [1]
while n > 0:
    n -= 1
    b.append(sum(a[0: i])/len(b))
    i += 1
b.remove(1)
print(b)
