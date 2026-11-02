"""
Урок 10.5 "Итоговая практика", шаг 5

Функция `is_leap(year)` должна возвращать `True`, если год високосный, и `False` иначе. Год
високосный, если делится на 4, но не делится на 100, или если делится на 400. Программа читает год и
выводит результат функции. Исправьте программу.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def is_leap(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(True)
        else:
            print(False)

    print(is_leap(input()))
"""

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(is_leap(int(input())))
