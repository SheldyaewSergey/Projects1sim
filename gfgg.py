k = int(input("Введите кол во чисел"))
def input_convert_number():
    while True:
        try:
            num = int(input("»>"))
            break
        except ValueError:
            print("Надо ввести число")
    return num
numbers = []
for _ in range(k):
    numbers.append(input_convert_number())
print(sum(numbers)/k)
