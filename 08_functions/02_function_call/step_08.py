"""
Урок 8.2 "Вызов функции", шаг 8

Функция `rect_area(width, height)` возвращает площадь прямоугольника. Программа читает ширину и
высоту (целые числа, каждое на своей строке) и выводит площадь. Программа падает, исправьте её.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def rect_area(width, height):
        return width * height

    w = int(input())
    h = int(input())
    print(rect_area(w))
"""

def rect_area(width, height):
    return width * height

w = int(input())
h = int(input())
print(rect_area(w, h))
