class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.color = z

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


#p1 = Point(4, 4)
#p2 = Point(3, 3)
#result = p1.dist_to(p2)

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
# Задание-3: вычислите площади треугольников образованных точками разных цветов

# TODO: your core here...

def area(points):
    a = points[0].dist_to(points[1])
    b = points[1].dist_to(points[2])
    c = points[0].dist_to(points[2]
    p = (a + b + c)/2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s

def res_area(points):
    red_points = []
    green_points = []
    for point in points:
        if point.color == 'green':
            green_points.append(point)
        if point.color == 'red':
            red_points.append(point)
    return area(red_points), area(green_points)

result = res_area(points)


print("Площадь красного треугольника = ", result[0])
print("Площадь зеленого треугольника = ", result[1])
