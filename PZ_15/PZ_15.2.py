# 2. В матрице элементы второго столбца заменить элементами из одномерного
# динамического массива соответствующей размерности.
import random as rd

m = int(input("Кол-во столбцов и строк: "))
n = m
a = [[0] * n for i in range(n)]  # Создание матрицы  все значения которой 0
for i in range(m):
    for j in range(n):
        a[i][j] = rd.randint(1, 100)  # Присваивание значений отличных от 0
print(*a, sep='\n')

b = []  # Создание матрицы  все значения которой 0
count = 0
while count < n:
    b.append(rd.randint(1, 100))
    count += 1
print("################")
print(b)

a[1][0] = b[0]
a[1][1] = b[1]
a[1][2] = b[2]
a[1][3] = b[3]

print("################")
print(*a, sep='\n')
