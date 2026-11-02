"""
Урок 7.2 "Номера элементов", шаг 7

Программа читает строку из целых чисел через пробел и выводит, сколько раз следующее число больше
предыдущего. Программа падает, исправьте её.

Пример. Для `12 15 11 18` программа выводит `2`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    nums = input().split()
    count = 0
    for i in range(len(nums)):
        if int(nums[i + 1]) > int(nums[i]):
            count = count + 1
    print(count)
"""

nums = input().split()
count = 0
for i in range(len(nums) - 1):
    if int(nums[i + 1]) > int(nums[i]):
        count = count + 1
print(count)
