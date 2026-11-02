"""
Урок 8.2 "Вызов функции", шаг 12

Функция `bonus(salary)` считает премию, 15% от зарплаты. Программа читает зарплату (целое число) и
выводит зарплату вместе с премией. Программа падает, исправьте её.

Пример. Для `1000` программа выводит `1150.0`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def bonus(salary):
        result = salary * 0.15
        return result

    s = int(input())
    bonus(s)
    print(s + result)
"""

def bonus(salary):
    result = salary * 0.15
    return result

s = int(input())
b = bonus(s)
print(s + b)
