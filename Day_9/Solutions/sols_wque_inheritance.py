"""
Задача №1 "Квадрат"
сделать класс Square - квадрат, который наследуется от прямоугольника
Класс Point(x: int, y: int)
# прямоугольник создаем на основе двух точек (class Point)
Класс Rect(p1, p2)
rect = Rect(p1: Point, p2: Point)
p1 = left_bottom -> (1, 1)  # левая нижняя
p2 = right_top -> (4, 5)    # правая верхняя
methods: area, perimeter (можно через property)
class Square(Rect):
    def __init__(self, p1, size):
        # ...
    # добавить метод вычисления диагонали
    def diag():
        pass
sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diag())
"""

class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


class Rect:
    def __init__(self, p1: Point, p2: Point):
        self._p1 = p1
        self._p2 = p2
        self._width = abs(self._p1.x - self._p2.x)
        self._height = abs(self._p1.y - self._p2.y)

    def perimeter(self):
        return (self._width + self._height) * 2

    def area(self):
        return self._width * self._height


class Square(Rect):
    def __init__(self, p1: Point, size):
        Rect.__init__(self, p1, Point(p1.x + size, p1.y + size))

    def diag(self):
        return (2 * self._width ** 2) ** 0.5


po1 = Point(1, 1)    # левая нижняя
po2 = Point(4, 5)    # правая верхняя

rect = Rect(po1, po2)
print(rect.perimeter())
print(rect.area())
print(40 * '=')
sq = Square(po2, 7)
print(sq.area())
print(sq.perimeter())
print(sq.diag())