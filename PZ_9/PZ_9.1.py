# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль.

peterochka = {'Мясо', 'Молоко', 'Сыр'}
magnit = {'Молоко', 'Соль', 'Сахар'}
perekrestok = {'Молоко', 'Творог', 'Сыр', 'Сахар'}
# 1.
if 'Сыр' not in peterochka:
    print("В Пятерочке нельзя купить сыр")
if 'Сыр' not in magnit:
    print("В Пятерочке нельзя купить сыр")

if 'Сыр' not in perekrestok:
    print("В Пятерочке нельзя купить сыр")


# 2.
m = magnit & perekrestok
if 'Молоко' and 'Сахар' in m:
    print("В Магните и Перекрестке можно купить молоко и сахар")
m = magnit & peterochka
if 'Молоко' and 'Сахар' in m:
    print("В Магните и Пятёрочке можно купить молоко и сахар")
m = peterochka & perekrestok
if 'Молоко' and 'Сахар' in m:
    print("В Пятёрочке и Перекрестке можно купить молоко и сахар")

# 3.
if 'Соль' in peterochka:
    print("В Пятёрочке можно купить соль")
if 'Соль' in perekrestok:
    print("В Прекрестке можно купить соль")
if 'Соль' in magnit:
    print("В Магните можно купить соль")