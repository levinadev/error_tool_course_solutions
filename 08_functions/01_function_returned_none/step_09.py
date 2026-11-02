"""
Урок 8.1 "Функция вернула None", шаг 9

Функция `count_long(words)` должна возвращать, сколько в списке слов длиннее трёх букв. Программа
читает строку слов через пробел и выводит результат. Ответ неверный, исправьте функцию.

Пример. Для `кот собака мышь ёж` программа выводит `2`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def count_long(words):
        count = 0
        for w in words:
            if len(w) > 3:
                count = count + 1
            return count

    print(count_long(input().split()))
"""

def count_long(words):
    count = 0
    for w in words:
        if len(w) > 3:
            count = count + 1
    return count

print(count_long(input().split()))
