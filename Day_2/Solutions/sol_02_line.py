class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def len_line(pnts: list) -> float:
    length = 0
    for i in range(len(pnts) - 1):
        length += distance(pnts[i], pnts[i + 1])

    return length


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
print("Длина ломаной линии = ", len_line(points))

# Variant 2
print("Check by oneline:", sum([distance(points[i], points[i - 1]) for i in range(1, len(points))]))