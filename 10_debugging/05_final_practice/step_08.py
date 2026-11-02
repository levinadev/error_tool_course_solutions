"""
Урок 10.5 "Итоговая практика", шаг 8

Программа читает строку целых чисел через пробел и выводит разницу между наибольшим и наименьшим
числом. Исправьте программу.

Пример. Для `5 -3 10 2` программа выводит `13`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    nums = input().split()
    big = 0
    small = 0
    for x in nums:
        if x > big:
            big = x
        if x < small:
            small = x
    print(big - small)
"""

nums = input().split()
big = int(nums[0])
small = int(nums[0])
for x in nums:
    n = int(x)
    if n > big:
        big = n
    if n < small:
        small = n
print(big - small)
