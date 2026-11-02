"""
Урок 10.5 "Итоговая практика", шаг 11

Программа читает пароль и проверяет его. Пароль надёжный, если в нём не меньше 8 символов и есть
хотя бы одна цифра. Программа выводит `Надёжный` или `Слабый`. Исправьте программу.

Программа с ошибкой, которая лежит в редакторе на Stepik

    password = input()
    has_digit = False
    for ch in password:
        if ch in "0123456789":
            has_digit = True
        else:
            has_digit = False
    if len(password) > 8 and has_digit:
        print("Надёжный")
    else:
        print("Слабый")
"""

password = input()
has_digit = False
for ch in password:
    if ch in "0123456789":
        has_digit = True
if len(password) >= 8 and has_digit:
    print("Надёжный")
else:
    print("Слабый")
