# =================================
#    Создание объектов-итераторов
# =================================

# Методы __iter__ и __next__ в разных классе
# class IterObj:
#     """  Объект-итератор """
#     def __init__(self, start=0):
#         self.number = start
#
#     # Объект считается итератором - если у него есть метод __next__
#     def __next__(self):
#         self.number += 1
#         if self.number <= 5:
#             return self.number
#         else:
#             # сами вызываем исключение StopIteration
#             raise StopIteration
#
#
# class Iter:
#     """ Объект, поддерживающий интерфейс итерации """
#     def __init__(self, start=0):
#         self.start = start - 1
#
#     def __iter__(self):
#         # Метод __iter__ должен возвращать объект итератор
#         return IterObj(self.start)
#
#
# # Создаем экземпляр класса Iter
# obj = Iter(start=2)
# # next(obj)  # TypeError: 'Iter' object is not an iterator
# # print(obj.start)  # получаем значение атрибута
# # print(obj, type(obj))
#
# # Каждый раз мы вызываем __iter__ и получаем новый экземпляр IterObj
# # Первый раз
# for el in obj:  # iter(obj); obj.__iter__()
#     print(el)
#
# print(obj)
# # Второй раз
# print("Еще раз ...")
# for el in obj:  # iter(obj); obj.__iter__()
#     print(el)
#
# # Третий раз
# print('sum(obj) -->', sum(obj))
# # #
# print('=' * 40)
#
# print(list(obj))  # Out: [2, 3, 4, 5]
# print(next(iter(obj)))  # Out: 2


# Методы __iter__ и __next__ в одном классе
class Iter2:
    def __init__(self, start=0):
        self.i = start - 1
        self.start = start - 1  # 1

    def __iter__(self):
        self.i = self.start  # 6 -> 1
        # Метод __iter__ должен возвращать объект-итератор
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


print("Demo Iter2")
obj = Iter2(2)

print("Первый раз")
for el in obj:
    print(el)

print(f'{obj.i = }')
print("Еще раз ...")
for el in obj:  # obj.i уже больше пяти
    print(el)

it = iter(obj)
print(next(it))


