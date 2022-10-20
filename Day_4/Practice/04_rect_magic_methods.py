"""
Используем класс Rect() с длиной и шириной в качестве атрибутов
Дополнительные задания на magic methods:
1) __repr__() - отобразить в виде текста
2) __str__() - отобразить в виде текста
3) r1 * 5 (__mul__()) - обе стороны станут в 5 раз больше
   добавить проверкy, что тип аргумента метода __mul__ это int или float
   # Variant 1, но python -O отключает все assert'ы
   assert type(arg) in (int, float), 'Bad type'
   # Variant 2
   if type(arg) in (int, float):
       pass
   else:
       raise TypeError
4) r1 < r2, r1 == r2, r1 <= r1 и т.п.
Шесть методов для сравнения:
__lt__() -> '<'
__gt__() -> '>'
__le__() -> '<='
__ge__() -> '>='
__eq__() -> '=='
__ne__() -> '!='
Сравнить по площади.
def __gt__(self, other):
	# ...
	# return True/False
"""

class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def scale(self, number):
        self.width *= number
        self.height *= number

    def rotate(self):
        self.width, self.height = self.height, self.width

    def __str__(self):
        return f'Ширина прямоугольника составляет {self.width}, длина прямоугольника составляет {self.height}'

    def __repr__(self):
        return f'Ширина: {self.width}, длина: {self.height}'

    def __mul__(self, p):
        if type(p) in (int, float):
            pass
        else:
            raise TypeError('Wrong type')

        self.width *= p
        self.height *= p
        return self

    def __lt__(self, other):
        return (self.width * self.height) < (other.width * other.height)

    def __gt__(self, other):
        return (self.width * self.height) > (other.width * other.height)

    def __le__(self, other):
        return (self.width * self.height) <= (other.width * other.height)

    def __ge__(self, other):
        return (self.width * self.height) >= (other.width * other.height)

    def __eq__(self, other):
        return (self.width * self.height) == (other.width * other.height)

    def __ne__(self, other):
        return (self.width * self.height) != (other.width * other.height)

#test
a = Rect(5, 5)
b = Rect(10, 10)
c = Rect(5, 5)

print(a)
print(b)
print(c)
print(a > b)
print(a <= b)
print(a == c)
print(a >= c)
c = a * 2
print(b == c)
