# Возвращает кортежи из индекса элемента и самого элемента
import os
from pprint import pprint

# enum = enumerate('hello')
# print(enum)
# # enum_list = tuple(enum)
# # print(enum_list)
# print(next(enum))
#
# # распаковка достает элементы
# e1, e2, e3, e4, e5 = enumerate('hello')
# print(e1, e2, e3, e4, e5)
#
# # *others - всегда список(остальные элементы, если есть)
# _, _, e3, *others, e5 = enumerate('hello')
# print(e3, others, e5)
#
# # Пример с файлом
# with open('some.txt', 'w') as in_file:
#     for i in range(10):
#         print(f'square {i}: {i ** 2}', file=in_file)
#
# # значения по умолчанию: r - read, t - text
# with open('some.txt', 'rt') as out_file:
#     print(out_file, type(out_file))
#     for line in out_file:
#         print(line, end='')

# запускаем приложение notepad.exe
# os.popen("notepad.exe some.txt")

# Используем next у файлового объекта
# f = open('some.txt')
# # Можно сразу в цикл
# for line in f:
#     print(repr(line))
# Можно каждый элемент с помощью next()
# print(repr(next(f)))
# print(repr(next(f)))
# f.close()
#
# zip тоже итератор
# z_obj = zip('hello', range(10))
# print(z_obj)   # Out: <zip object at 0x00000273B93E4FC0>
# print(next(z_obj))
# d = dict(z_obj)
# print(len(d))   # Out: 3
# print(d)       # Out: 'l': 3

# Проверка
z = zip([2, 1, 8.1, False, True, 0], 'python')
print(dict(z))  # Out: len(z): 4

# Важно помнить, что: 0 == False, 1 == True
print([2, 1, 8.1, False, True, 0].count(1))
print([2, 1, 8.1, False, True, 0].count(0))

# КВ
obj = zip('hellopython', range(7), [8, 0, 2, 9, 2, 1])
t_obj = tuple(obj)
print(len(t_obj))  # Out: 6
print(t_obj)
# KB*
obj = zip('hellopython', [1, 0, 2, 2, 1, 1, 0, 0, 1, 1, 2])
s = set(obj)
print(len(s))  # Out: 8

d1 = dict(s)
obj_copy = zip('hellopython', [1, 0, 2, 2, 1, 1, 0, 0, 1, 1, 2])
d2 = dict(obj_copy)
print(d1 == d2)  # Out: True
pprint(d1)
pprint(d2)
print(d1 is d2)  # Out: False
