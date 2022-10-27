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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x},{self.y})'

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Rect:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.a = p2.x - p1.x
        self.b = p2.y - p1.y

    def __str__(self):
        return f'{self.__class__.__name__}({self.a},{self.b})'

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rect):
    def __init__(self, p1, size):
        p2 = Point(p1.x + size, p1.y + size)
        super().__init__(p1, p2)

    def diag(self):
        return self.a * 2 ** 0.5

    def diagonal(self):
        return self.p1.distance(self.p2)


point1 = Point(1, 1)
point2 = Point(4, 5)

rect = Rect(point1, point2)
print(f'{rect = !s}')

sq = Square(point1, 5)
print(f'{sq = !s}')
print('*' * 25)

print(f'{rect.area = }')
print(f'{rect.perimeter = }')
print('*' * 25)

print(f'{sq.area = }')
print(f'{sq.perimeter = }')
print(f'{sq.diag() = }')
print(f'{sq.diagonal() = }')