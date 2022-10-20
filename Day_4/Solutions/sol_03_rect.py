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
    def __init__(self,  width=5, length=10):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def __str__(self):
        return f"Ширина: {self.width}, длина: {self.length}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width},{self.length})"

    def scale(self, n):
        self.length *= n
        self.width *= n

    def rotate(self):
        # Variant 1
        self.width, self.length = self.length, self.width

        # # Variant 2
        # a = self.length
        # self.length = self.width
        # self.width = a


## Тестовая часть
rect = Rect(5, 10)
print(rect)
print(repr(rect))
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

