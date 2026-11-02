"""
Урок 8.1 "Функция вернула None", шаг 10

Функция `average(nums)` должна возвращать среднее арифметическое списка чисел. Программа читает
строку целых чисел через пробел и выводит среднее. Программа падает, исправьте функцию.

Пример. Для `2 4 9` программа выводит `5.0`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def average(nums):
        print(sum(nums) / len(nums))

    nums = []
    for x in input().split():
        nums.append(int(x))
    result = average(nums)
    print(result)
"""

def average(nums):
    return sum(nums) / len(nums)

nums = []
for x in input().split():
    nums.append(int(x))
result = average(nums)
print(result)
