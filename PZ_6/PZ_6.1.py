# 1. Дан целочисленный список размера N. Увеличить все нечетные числа, содержащиеся в
# списке, на исходное значение последнего нечетного числа. Если нечетные числа в
# списке отсутствуют, то оставить список без изменений.

lenn = int(input("Введите длинну списка >>>"))
import random
a = [random.randint(0, 20)for i in range(lenn)]
print(a)
n = 0
for i in range(lenn):
    if a[i] % 2 == 1:
        n = a[i]
print(n)
for i in range(lenn):
    if a[i] % 2 == 1:
        a[i] += n
print(a)