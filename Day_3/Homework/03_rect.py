"""
Прямоугольник по двум сторонам
Создать класс прямоугольник:

а) при создании указывается ширина и длина

r = Rect(5, 10)

б) методы для площади и периметра

print(r.area())       # возвращает площадь
print(r.perimeter())  # периметр

в) масштабирование и поворот

r.scale(10) - ширина и длина увеличиваются в 10 раз
r.scale(0.1) - ширина и длина уменьшаются в 10 раз
r.rotate() - меняется местами ширина и длина

г) переопределить магические методы __repr__ и __str__
"""
import random


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def scale(self, number):
        self.width *= number
        self.height *= number

    def rotate(self):
        self.width, self.height = self.height, self.width

    def __str__(self):
        return f'Ширина прямоугольника составляет {self.width}, длина прямоугольника составляет {self.height}'

    def __repr__(self):
        return f'Ширина: {self.width}, длина: {self.height}'

## Тестовая часть
rect = Rect(5, 10)
print("Площадь: ", rect.area())
print("Периметр: ", rect.perimeter())

if random.randint(0, 1):
    rect.scale(10)
    # Покажи значение rect, используя метод __str__()
    print(f"Увеличение: {rect!s}")
else:
    rect.scale(0.1)
    print(f"Уменьшение: {rect!s}")


rect.rotate()
print("Rotate: ", rect)
print("Площадь: ", rect.area())
print("Периметр: ", rect.perimeter())
print(rect)
print(repr(rect))
