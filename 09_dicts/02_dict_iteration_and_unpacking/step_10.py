"""
Урок 9.2 "Перебор словаря и распаковка", шаг 10

Программа собирает журнал оценок. Сначала вводится число n, потом n строк, в каждой имя ученика и
оценка через пробел. Один ученик может получить несколько оценок. Программа выводит, сколько оценок
получил ученик, имя которого вводится последней строкой. Ответ неверный, исправьте программу.

Пример. Для строк `Аня 5`, `Борис 4`, `Аня 3` и имени `Аня` программа выводит `2`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    n = int(input())
    journal = {}
    for i in range(n):
        name, mark = input().split()
        journal[name] = mark
    who = input()
    print(len(journal.get(who, "")))
"""

n = int(input())
journal = {}
for i in range(n):
    name, mark = input().split()
    if name not in journal:
        journal[name] = []
    journal[name].append(mark)
who = input()
print(len(journal.get(who, [])))
