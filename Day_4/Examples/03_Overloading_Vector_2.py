from __future__ import annotations

# =============================
#    Перегрузка операторов
# =============================

from math import sqrt


class Vector:
    """ docstring for Vector """
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        txt = "<" + str(self.x) + ","
        txt += str(self.y) + ","
        txt += str(self.z) + ">"
        return txt

    # Неизменяемый вектор
    def __add__(self, obj: Vector):  # v + obj
        v = Vector()
        v.x = self.x + obj.x
        v.y = self.y + obj.y
        v.z = self.z + obj.z
        return v

    def __radd__(self, obj: Vector):  # + ;   obj + v -> v + obj
        v = Vector(self.x, self.y, self.z)
        return v + obj  # v.__add__(obj)

    def __iadd__(self, obj):  # +=, реализация похожа на list
        self = self + obj  # self.__add__(obj)
        return self

    # Используем хинтинг(hint-подсказка)
    def __mul__(self, p: int | float | Vector):  # v1 * v2; v1 * 5
        """ __mul__ может принимать в качестве аргумента int, float, Vector"""
        if type(p) == Vector:
            res = self.x * p.x + self.y * p.y + self.z * p.z  # Out: type -> float
            return res
        elif type(p) in (int, float):
            self.x *= p
            self.y *= p
            self.z *= p
            # Возвращаем тот же самый объект, но значение атрибутов будут новые
            return self   # v1 = v1 * 3
        else:
            raise TypeError('bad type')

    def __rmul__(self, p):  # 5 * v1, вектор - это правый операнд
        return self * p     # v1 * 5

    def __neg__(self):  ## -v1
        return Vector(-self.x, -self.y, -self.z)

    def __sub__(self, obj):  # -: v1 - v2
        return -obj + self   # return self + (-1) * obj

    def __isub__(self, obj):  # -=
        self = -obj + self
        return self

    def __abs__(self):  # abs()
        return sqrt(self * self)  # извлекаем квадратный корень из float или int

    def __truediv__(self, p: int | float):  # реализуем через * (__mul__)
        return self * (1 / p)

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y and self.z == obj.z

    def __ne__(self, obj):
        return not self == obj

    def __lt__(self, obj):
        # return abs(self) < abs(obj)  # можно и так
        if abs(self) < abs(obj):
            return True
        return False

    def __gt__(self, obj):
        if abs(self) > abs(obj):
            return True
        return False

    def __le__(self, obj):  # <=  less or equal
        if abs(self) <= abs(obj):
            return True
        return False

    def __ge__(self, obj):  # >=  greater or equal
        if abs(self) >= abs(obj):
            return True
        return False

    def __invert__(self):   # ~, просто для демонстрации
        self.x = 10 - self.x
        self.y = 10 - self.y
        self.z = 10 - self.z
        return self


# Vectors
print("Vectors:")
a = Vector(1, 2, -1)
b = Vector(1, -1, 3)
c = ~Vector(9, 8, 11)
print("a =", a)
print("b =", b)
print("c =", c)
#
print("Abs of Vectors:")
print("|a| =", abs(a))
print("|b| =", abs(b))
print("|c| =", abs(c))
#
# print("Vectors comparation:")
# print("a == b ->", a == b)
# print("a != b ->", a != b)
# print("a == c ->", a == c)
# print("a < b ->", a < b)
# print("a > b ->", a > b)
# print("a <= b ->", a <= b)
# print("a >= b ->", a >= b)

# print("Vectors operations:")
# print("Vectors sum:")
# print("a + b =", a + b)
# c += a
# print("c += a ->", c)
#
# print("Vectors sub:")
# print("a - b =", a - b)
# c -= a
# print("c -= a ->", c)

# print("Vector mul:")
# print("a * b =", a * b)
# print(f'Before: {id(a) = }')
# print("a * 3 =", a * 3)
# print(f'After: {id(a) = }')
# print("a =", a)
# print("2 * b =", 2 * b)
# print("b =", b)
# print("-b =", -b)
# print("b =", b)
# print("a / 3 =", a / 3)
# print("a =", a)


class M:
    x = 100
    y = 100
    z = 100


my = M()
# print(a * my)  # ERROR, неверный тип
# print(my * a)  # a__rmul__(my) ERROR, неверный тип
print(a + my)  # Out: <101.0,102.0,99.0>
print(my + a)  # Out: <101.0,102.0,99.0>
print(my.x)
print(my.y)
print(my.z)
