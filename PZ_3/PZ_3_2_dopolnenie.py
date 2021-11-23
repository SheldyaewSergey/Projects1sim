#Даны целые числа a,b,c. Необходимо найти 2 наибольших и сложить.
def input_convert_number():
    while True:
        try:
            num = int(input("»>"))
            break
        except ValueError:
            print("Надо ввести число")
    return num
#Функция для проверки

numbers = []
for _ in range(3):
    numbers.append(input_convert_number())
#Создаем список из 3 введенных чисел

numbers.sort()
print(numbers[-1] + numbers[-2])
#Сортируем список и берем два больших числа, потом суммируем их
