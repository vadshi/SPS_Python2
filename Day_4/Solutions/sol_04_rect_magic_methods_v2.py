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
    def __init__(self, width=5, length=10):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Ширина: {self.width}, длина: {self.length}"

    def __repr__(self):
        return f"Rect({self.width},{self.length})"

    def __mul__(self, x):
        if type(x) in (int, float):
            self.length *= x
            self.width *= x
        else:
            raise TypeError('Bad type of "x" argument.')

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()


# Тестовая часть
r1 = Rect(5, 10)
r2 = Rect(8, 16)
print('Before:', r1)
# Сейчас у нас реализация меняет состояние экземпляра, но ничего не возвращает
r1 * 5
print('After:', r1)
print(r1.area())
print(r2.area())

# Проверка dunder методов
print(r1 > r2)
print(r1 >= r2)
print(r1 < r2)
print(r1 <= r2)
print(r1 == r2)
print(r1 != r2)


r1 *= 100  # r1 = r1 * 100
print(r1)  # None

# Проверка метода __mul__() на соответствие типов
# print(r1 * 'hello')
