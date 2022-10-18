class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5



def geron(pnts):
    """ Вычисляем площадь по формуле Герона."""
    a = pnts[0].dist_to(pnts[1])
    b = pnts[1].dist_to(pnts[2])
    c = pnts[2].dist_to(pnts[0])
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5



# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)

greens = []
reds = []

for point in points:
    if point.color == 'red':
        reds.append(point)
    else:
        greens.append(point)

print("Площадь красного треугольника = ", geron(reds))
print("Площадь зеленого треугольника = ", geron(greens))
