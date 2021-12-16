#1. Даны строки S и S0. Найти количество вхождений строки S0 в строку S.


s = "1 1 2 3 5 6 5 4 5"
s0 = "5"

count = 0
for a in s:
    if a == s0:
        count += 1
    else:
        continue
print(count)
