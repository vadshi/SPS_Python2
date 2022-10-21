# ================================
#    Принципы работы итераторов
# ================================

test_list = [1, 2, 3, 4, 'python']
print(test_list)
# # Когда вы пишете
# for el in test_list:
#     print(el)

# Итерация по множеству
a = {5, 23, 12}
# for item in a:
#     print(item)

# Python выполняет:
# 1. Вызывает метод __iter__(): test_list.__iter__()
# Метод __iter__() должен вернуть объект, у которого есть метод __next__()
# 2. Цикл for..in каждую итерацию вызывает метод __next__()
#   __next__() при каждом вызове возвращает следующий элемент итератора
# 3. Когда элементы итератора заканчиваются, метод __next__() возбуждает исключение StopIteration
#   for.. in завершает свою работу, когда перехватывает это исключение

# Проведем обход элементов списка test_list вручную (без цикла)
# print("Итерируем вручную...")
# # Получаем объект-итератор
# # Функция iter() просто вызывает метод __iter__()
# test_list_iter = iter(test_list)
# print(test_list_iter)
# # print(test_list_iter[1]) # TypeError
# # print(len(test_list_iter))
#
# # Для того чтобы получить значение, вызываем функцию next
# print(next(test_list_iter))
# print(test_list_iter.__next__())
# print(next(test_list_iter))
# print(next(test_list_iter))
# print(next(test_list_iter))
#
# # Будет вызвано исключение StopIteration
# print(next(test_list_iter, 'Iterator is empty.'))
#
#
# # Создаем итератор для множества
# set_iter = iter(a)
# print(set_iter)
# print(next(set_iter))
# print(next(set_iter))
# print(next(set_iter))
# print(next(set_iter, 'Finish'))
#
# print('=' * 40)
# for item in iter(test_list):
#     print(item)

# Создали итератор
ex_iter = iter(test_list)

# Перебираем элементы итератора и сравниваем с 2
print(2 in ex_iter)  # True
lst = list(ex_iter)

# Берем оставшиеся элементы, если они есть
print(lst)           # Out: [3, 4, 'python']
print(2 in ex_iter)  # Итератор сейчас пустой


# Закрепление
# Создали итератор
ex_iter = iter(test_list)  # list_iterator -> [1, 2, 3, 4, 'python']
print('java' in ex_iter)
tup1 = tuple(ex_iter)
print(tup1)  # Out: ()

print('*' * 40)
# # # Работа со словарем
d = {'a': 1, 'b': 2}
for element in d:
    print(element)   # Out: a b


it = iter(d)     # Получаем итератор из ключей
print(next(it))  # Out: 'a'
print(next(it))  # Out: 'b'
print(next(it))  # StopIteration

# Тот же самый механизм при распаковке
e, f = d
print(e)  # Out: 'a'
print(f)  # Out: 'b'

