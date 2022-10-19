# =============================
#    Перегрузка операторов
# =============================

# Имена методов, начинающиеся и заканчивающиеся двумя символами
# подчеркивания __X__, имеют специальное назначение.
# dunder(magic) methods.
# Такие методы вызываются неявно, когда объект участвует в соответствующей операции.
# Возвращаемое значение метода становится результатом соответствующей операции.
from pprint import pprint


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # это явный метод
    def to_str(self):
        return f'Point({self.x},{self.y})'

    # Перегрузка(переопределение) магического(dunder) метода
    def __repr__(self):  # repr()
        return f'Point({self.x},{self.y})'

    def __str__(self):  # str()
        return (f'Точка с координатами:'
                f'({self.x},{self.y})')




## Примеры для str, repr
# s1 = "100"
# i1 = 100
# print(s1)
# print(i1)
# print(repr('\not'))
# print(r'\not')   # raw string
# print(repr(s1))  # показать как есть
# print(str(i1))   # i1.__str__()
# print(repr(i1))  # i1.__repr__()

# # Такой же механизм работает для функции len()
# print(len(s1))
# print(s1.__len__())
# print('\not'.__len__())
# print(i1.__len__())  # AttributeError: 'int' object has no attribute '__len__'


# p1 = Point(3, 3)
# p2 = Point(4, 4)
#
# # # Явно вызываем метод to_str()
# print('Вызов явного метода')
# print(p1.to_str())
# print(p2.to_str())
# print('Вызов неявных методов')
# print(p1)
# print(p2)

# Неявно вызываем магические методы __repr__ и __str__
# print сначала ищет __str__(),
# если не находит то использует __repr__()
# print(str(p1))  # str(p1) -> p1.__str__()
# print(repr(p2))  # repr(p1) -> p2.__repr__()
#
# print('=' * 40)
#
# # Четыре вызова с одинаковым функционалом
# print(p2)
# print(str(p2))
# print(p2.__str__())  # print(str(p2))
# print(Point.__str__(p2))
#
# # Вызвать именно repr()
# print(p1.__repr__())  # print(repr(p1))
# print(repr(p1))


# Интроспекция экземпляра p1 (dunder методы)
# pprint(dir(p1))
# print(p1.__sizeof__())
# help(p1.__sizeof__)

# import sys
# # print(sys.getsizeof(p1))
# # # help(sys.getsizeof)
# print(sys.getrefcount(p1))
# print(sys.getrefcount(5))
#
# Создадим функция для интроспекции
# def func(a=5, b=8):
#     return a + b


# Интроспекция экземпляра func (dunder методы)
# pprint(dir(func))
# pprint(func.__defaults__)

# # # Для созданных можем
# func.name_of_function = 'first function'  # Out: work
# print(func.name_of_function)
#
# # А для встроенных нет
# sum.name_of_function = 'sum function'  # Out: error
#
# # На подумать: Как с помощью атрибутов функции посчитать
# # количество вызовов этой функции
