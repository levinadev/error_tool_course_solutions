"""
Урок 10.5 "Итоговая практика", шаг 3

Программа читает строку из слов через пробел и выводит самое длинное слово. Если таких несколько,
выводится первое из них. Исправьте программу.

Пример. Для `кот собака мышь` программа выводит `собака`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    words = input().split()
    longest = ""
    for w in words:
        if len(w) >= len(longest):
            longest == w
    print(longest)
"""

words = input().split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)
