""" Закрепляем работу с методами """

from pprint import pprint

# Создаем класс
# class MyClass:
#     pass
#
#
# A = MyClass()
# B = MyClass()
# C = MyClass()
#
# # Создаем первую функцию
# def hello():
#     print("функция - 'hello'")
#
#
# print(f'hello function {id(hello) = }')
# # Создаем вторую функцию
# def hi():
#     print("Другая функция - 'hi'")
#
#
# # Определяем "метод" для экземпляра А
# A.say = hello
#
# # Определяем "метод" для экземпляра C
# C.say = hi
#
# # Вызов "метода" у экземпляра А
# A.say()
# print(type(A.say))
# #
# # Вызов метода у экземпляра B
# try:
#     B.say()
# except AttributeError:
#     print('Нет такого метода')
# #
# print('Продолжаем')
# # Вызов метода у экземпляра C
# C.say()
#
# # Вызов функции класса
# try:
#     MyClass.say()
# except AttributeError:
#     print('Нет такой функции')

# del A.say
#
# # Вызов метода у экземпляра А
# try:
#     A.say()
# except AttributeError:
#     print('Нет такого метода')

# # Вызов метода у экземпляра C
# C.say()
# hello()

# Работа через ссылки на объект
# print('Before del hello function:', id(hello))
# del hello
# print('hello' in globals())
# A.say()
# hello()  # NameError: name 'hello' is not defined.

# Как можно посмотреть байт-код
# import dis
# print(dis.dis(A.say.__code__))


# print(A.say.__name__)
# hello = A.say
# hello()
# print('After del and recreate:', id(hello))
# print('hello' in globals())
# pprint(globals())
#
# # # модуль сборщика мусора
# import gc

# очисти всю память от удаленных объектов
# gc.collect()
# print(gc.get_stats())
