"""
Урок 8.2 "Вызов функции", шаг 11

Программа читает строку целых чисел через пробел и выводит их сумму. Программа падает, исправьте её.

Программа с ошибкой, которая лежит в редакторе на Stepik

    sum = 0
    nums = []
    for x in input().split():
        nums.append(int(x))
    print(sum(nums))
"""

nums = []
for x in input().split():
    nums.append(int(x))
print(sum(nums))
