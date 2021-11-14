while True:
    try:
        a = int(input("Введите целое число >>> "))
        break
    except ValueError:
        print("Введите целое число больше нуля!")
b = 0
b = a
count = 1
while True:
    try:
        n = int(input("Введите целое число для степени >>> "))
        break
    except ValueError:
        print("Введите целое число больше нуля!")
while count < n:
    count += 1
    a = a * b
print(a)