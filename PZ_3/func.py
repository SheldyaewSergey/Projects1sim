def ff(z, x, c):
    try:
        z = int(z)
        x = int(x)
        c = int(c)
    except ValueError:
        print("Введите целое число!")
        z = input()
        x = input()
        c = input()