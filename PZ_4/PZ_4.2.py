n = int(input("Chislo >>> "))
b = 0
while True:
    b %= 10
    n = n - b / 10
    if b == 1 or b == 3 or b == 5 or b == 7 or b ==9:
        print("True")
        break
    else:
        print("False")