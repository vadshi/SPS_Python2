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
    pass

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

