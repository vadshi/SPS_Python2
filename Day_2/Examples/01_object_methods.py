class Point:
    # Конструктор
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод distance возвращает свой результат
    def distance(self, other_point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    # Метод inverse, который меняем состояние экземпляра
    def inverse(self, value: int = -1) -> None:
        self.x *= value
        self.y *= value


point1 = Point(10, -8)
point2 = Point(12, 5)


dist = point1.distance(point2)  # Point.distance(point1, point2)
print("Расстояние между точками =", dist)
print(Point.distance(point1, point2))
print(point2.distance(point1))
print(f'Before calling <inverse> method: {point1.x = }, {point1.y = }')
point1.inverse()
print(f'After calling <inverse> method: {point1.x = }, {point1.y = }')
