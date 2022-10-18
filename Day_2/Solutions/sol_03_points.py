class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

zero = Point(0, 0)
max_distance = 0
max_point = None
for point in points:
    curr_distance = distance(zero, point)
    if curr_distance > max_distance:
        max_distance = curr_distance
        max_point = point

print(f"Координаты наиболее удаленной точки = ({max_point.x}, {max_point.y})")

# Variant 2
distances = [distance(Point(0,0), point) for point in points]
max_point = points[distances.index(max(distances))]
print(f"Координаты наиболее удаленной точки = ({max_point.x}, {max_point.y})")