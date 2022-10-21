from pprint import pprint

# Variant 1
# lst = []
# for i in range(10):
#     lst.append(i ** 2)
#
# print(*lst)
#
# # Variant 2 чуть быстрее, чем Variant 1
# lst = [None] * 10
# for i in range(10):
#     lst[i] = i ** 2
#
# print(*lst)
#
# # Генератор в списке (list comprehensions)
# # Variant 3 быстрее чем Variant 1 и Variant 2
# lst = [i ** 2 for i in range(10)]
# print(f'{lst = }')
#
# # Множество - это только про уникальность
# s = {i ** 2 for i in range(10)}
# print(f'{s = }')
#
# # Генератор в словаре
# d = {str(i).zfill(4): i ** 2 for i in range(10)}
# pprint(d)
#
# # Генератор (генератор выражения), но похоже на кортеж
# a = (i ** 2 for i in range(10))
#
# print(a, type(a))
# # print(len(a)) # TypeError
# # print(a[0]) # TypeError
#
# # С помощью next, мы явно требуем создать элемент
# print(next(a))
# print(next(a))
# print(next(a))
# for square in a:
#     print(f'{square = }')  # Out: 9, 16, ...., 81
# print()
# # # # Чтобы не было ошибки StopIteration
# print(next(a, 'empty'))
# print(a)
# print(sum(i ** 2 for i in range(5)))

# Реализация генератора из 3-х элементов
def gen():
    # Начало работы первого вызова next()
    a = 2
    b = 2
    # Происходит возврат значений и
    # приостановка работы генератора до следующего вызова
    yield a, b  # Конец работы первого вызова next()

    # Начало работы второго вызова next()
    a += 2
    yield a, b  # Конец работы второго вызова next()

    # Начало работы третьего вызова next()
    a *= 3
    b += 4
    yield a, b  # Конец работы третьего вызова next()

# Пример использования
# a = gen()
# print(a, type(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))  # StopIteration

# # Реализация: a = (i ** 2 for i in range(10))
def gen_for():
    for item in range(1_000_000):
        yield item ** 2


res = gen_for()
print([i ** 2 for i in range(1_000_000)].__sizeof__(), 'bytes')
print(res.__sizeof__(), 'bytes')
t = tuple(res)
# next(res) # StopIteration
print(t.__sizeof__(), 'bytes')

# Создаю заново, потому что все элементы ушли в кортеж
res = gen_for()
print(next(res))   # Out: 0
print(res.__next__())  # Out: 1

# Закрытие генератора
res.close()
for element in res:
    print(element, end=' ')
print('done')

# sum заставляет генератор создать эти значения
print(sum(i ** 2 for i in range(10)))

# Генератор в кортеже
print(tuple(i ** 2 for i in range(10)))
