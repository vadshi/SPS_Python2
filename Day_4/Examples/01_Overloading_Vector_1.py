# =============================
#    Перегрузка операторов
# =============================

# Имена методов, начинающиеся и заканчивающиеся двумя символами
# подчеркивания __X__, имеют специальное назначение.
# Такие методы вызываются неявно, когда объект участвует в соответствующей операции.
# Возвращаемое значение метода становится результатом соответствующей операции.


class Vector:
    def __init__(self, pos):  # Какой тип данных может быть у pos? str, list, tuple, dict
        self.x = pos[0]
        self.y = pos[1]

    # Реализация оператора +, неявный метод
    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    # Это явный метод
    def add(self, other):
        # каждый раз будет возращаться новый экземпляр Например как со строками: str.lower()
        return Vector((self.x + other.x, self.y + other.y))

    def as_point(self):
        return self.x, self.y

    # Формируем удобное отображение объекта при выводе функцией print()
    def __str__(self):
        return "V(x:{} y:{})".format(self.x, self.y)


class Slon:
    def __init__(self):
        self.x = 100.0
        self.y = 200.0


slonik = Slon()

# Создаем экземпляры класса (объекты)
# Передаем кортеж(tuple) в качестве аргумента в конструктор класса
v1 = Vector((10, 15))
v2 = Vector((12, 10))

# Явно вызываем явный метод
print(v1.add(v2))
#
# # Наши объекты участвуют в операции сложения (+)
# # Благодаря перегрузке, мы можем использовать более удобную и привычную запись:
v3 = v1 + v2  # v1.__add__(v2)
print('v3 =', v3)  # v3.__str__()

# # На самом деле это работает так:
v4 = v1.__add__(v2)
print(f'{v4 = !s}')
#
# v4 = v1 - v2  # TypeError: unsupported operand type(s) for -: 'Vector'
#
something = v1 + slonik  # v1.__add__(slonik)
print(f'something = {something!r}')
print(f'something = {something!s}')
#
# some_v2 = slonik + v2  # TypeError
# # #
# # Функция print() для получения строки для вывода вызывает методы __str__()
print('v3 + v3 =', v3 + v3)
print('Repr of v3 = ', repr(v3))
print(f'{v3!r}')  ## __repr__()
print(f'{v3!s}')  ## __str__()
#
v5 = v1.add(v2)
v6 = v1.__add__(v2)
v7 = v1 + v2
v8 = v1
#
# # Без перегрузки оператора ==, сравниваются id двух объектов
print(v1 == v8)   ## id(v1) == id(v8)
print(v1 != v2)

