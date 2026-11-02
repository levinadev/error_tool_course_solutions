"""
Урок 8.2 "Вызов функции", шаг 10

Функция `percent(part, whole)` возвращает, сколько процентов `part` составляет от `whole`. Программа
читает сначала целое, потом часть (целые числа) и выводит процент. Ответ неверный, исправьте
программу.

Пример. Для целого `200` и части `50` программа выводит `25.0`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def percent(part, whole):
        return part / whole * 100

    whole = int(input())
    part = int(input())
    print(percent(whole, part))
"""

def percent(part, whole):
    return part / whole * 100

whole = int(input())
part = int(input())
print(percent(part, whole))
