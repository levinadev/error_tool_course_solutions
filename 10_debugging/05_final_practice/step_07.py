"""
Урок 10.5 "Итоговая практика", шаг 7

Программа читает число n, потом n строк с названиями товаров. Она выводит каждый товар один раз в
порядке первого появления и рядом, сколько раз он встретился. Исправьте программу.

Пример. Для n `3` и товаров `хлеб`, `сыр`, `хлеб` программа выводит `хлеб 2` и `сыр 1` в столбик.

Программа с ошибкой, которая лежит в редакторе на Stepik

    n = input()
    count = {}
    for i in range(n):
        item = input()
        count[item] += 1
    for item in count:
        print(item, count[item])
"""

n = int(input())
count = {}
for i in range(n):
    item = input()
    count[item] = count.get(item, 0) + 1
for item in count:
    print(item, count[item])
