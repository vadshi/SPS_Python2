class Point:
    # Поля(fieds) == атрибуты класса
    x = 7
    y = 4


# Создадим несколько объектов-точек
# Экземпляр(instance)
point1 = Point()
point2 = Point()

# Считываем атрибуты
print(point1.x)  # 7
print(point2.x)  # 7

# Три разных объекта(три разных id)
# print(id(point1), id(point2), id(Point), type(point1))
# print(type(5), type('hello'))

point1.x = 10
print(point1.x)  # 10
print(point2.x)  # 7

Point.x = -15
print(point1.x)  # 10
print(point2.x)  # -15

print(point1.y)  # 4
print(point2.y)  # 4

Point.z = 999
print(point1.z)  # 999
print(point2.z)  # 999

point2.z = -99
print(point1.z)  # 999
print(point2.z)  # -99

# Удаляем у экземпляра
del point2.z
print(point1.z)  # 999
print(point2.z)  # 999

# Удаляем у класса
del Point.z
# print(point1.z)   # Out: AttributeError:
# print(point2.z)   # Out: AttributeError:

# del point1
# print(point1.x)  # Out: NameError

point1.name = 'first instance'
print(point1.name)

del point1.y     # Out: AttributeError: