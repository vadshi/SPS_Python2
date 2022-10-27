from collections import (Counter,
                         OrderedDict,
                         deque,
                         defaultdict,
                         ChainMap)
import itertools
from pprint import pprint

# Обычны словарь(dict)
# d_usual = dict()
# print(type(d_usual))
# for word in ['spam', 'egg', 'egg', 'spam',
#              'counter', 'counter', 'counter']:
#     d_usual.setdefault(word, 0)
#     d_usual[word] += 1
# print(d_usual.get("col", 0))
# print(d_usual)
#
# # класс Counter
# counter = Counter()
# print(type(counter))
# for word in ['spam', 'egg', 'egg', 'spam',
#              'counter', 'counter', 'counter']:
#     counter[word] += 1    # Нет ошибки(в обычном dict будет)
# print(counter)
# print(counter['counter'])
# print(counter['collections'])  # Нет ошибки
# print(counter)
#
# print(Counter('sathustahuathusathusathuu'))
#
# # ## Вернуть 3 самых часто встречающихся элемента
# print(Counter('sathustahuathusathusathuu').most_common(3))
# print(Counter('hello students, language python').most_common(3))
# print(Counter('hello students, language python'))
#
# # ## Вернуть 2 самых редко встречающихся элемента
# print(Counter('hello students, language python').most_common()[:-3:-1])
# print(Counter('hello students, language python').most_common()[-2:])

# counter = Counter(a=4, b=2, c=0, d=-2)
# counter2 = Counter(a=1, b=2, c=3, d=4)

# ## Ключи только с положительными значениями
# print('Сложение:\n', counter + counter2)
# print('Вычитание:\n', counter - counter2)  # Counter({'a': 3})
#
# # ## Ключи с минимальными значениями, строго > 0
# print('Минимальные значения:', counter & counter2)
# #
# # ## Ключи с максимальными значениями, строго > 0
# print('Максимальные значения:', counter | counter2)
#
## Ключи со всеми значениями (положительные, нулевые и отрицательные)
# counter.subtract(counter2)
# print(counter)
# print(f'{+counter = }') # пары с положительными значениями
# print(f'{-counter = }') # пары с неположительными значениями
# print(list(counter))  # list(counter.keys())

# # вернет все элементы
# print(list(counter.elements())) ## Counter({'a': 3}) -> 'a', 'a', 'a'
# res = Counter('sathustahuathusathusathuu')
# print(f'{res = }')
# print(''.join(tuple(res.elements())))
#
# # Исходный код метода ====================================
# import inspect
# print(inspect.getsource(type(res)))
# print(inspect.getsource(res.elements))
# #
# # # # ========================================================
# print(sum(counter.values())) ## общее сумма по значениям.
# print(counter.__class__.__mro__)
#
# ## удалить элементы, встречающиеся менее одного раза.
# counter += Counter()
# print(counter)

# import re
# # # # https://regex101.com/  [а-яА-ЯёЁ]
# # # # ## \w+ - буквы, цифры и _, длина от 1 и более
# words = re.findall(r'[\w\']+', open('zen.txt').read().lower())
# print(type(words))
# zen_dict = Counter(words)
# pprint(zen_dict)
# print(sum(zen_dict.values()))
# 
# 
### defaultdict, OrderedDict
## Аргумент функции - это тип значения по умолчанию
# example = defaultdict(str)
# example['first'] = '1'
# example['second'] = '2'
# example['third']  # Ошибки нет, элемент будет создан со значением ''
# pprint(example, width=20)
# # #
# example['fourth'] = 12
# pprint(example, width=20)

# На основе dict
# print(example.__class__.__mro__)

# В качестве типа по умолчанию могут быть и mutable types
# defdict = defaultdict(list)
# print(defdict)
# for i in range(5):
#     # Создаем пары 'ключ:значение([])'
#     defdict[i].append(i ** 3)
# print(defdict)


## OrderedDict
# d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# # # Сортировка по ключам
# print(OrderedDict(sorted(d.items())))
#
# # Сортировка по значениям
# print(OrderedDict(sorted(d.items(), key=lambda t: t[1])))
#
# # Сортировка по длине ключа
# print(OrderedDict(sorted(d.items(), key=lambda t: len(t[0]))))
#
# # # # Подумайте над ответом
# print(OrderedDict(zip(sorted(d, key=lambda t: t[0]), '0000')))
#
# # Пример использования
# ord_dict = OrderedDict.fromkeys('abcdefg')
# pprint(ord_dict)
# #
# # ## добавляет ключ в конец если last=True, и в начало, если last=False.
# ord_dict.move_to_end('b', last=True)
# print(''.join(ord_dict.keys()))
# # # Помещаем 'e' в начало
# ord_dict.move_to_end('e', last=False)
# print(''.join(ord_dict.keys()))
#
# # ## удаляет последний элемент если last=True, и первый, если last=False.
# res = ord_dict.popitem(last=True)
# print(res)
# print(''.join(ord_dict.keys()))
# pprint(ord_dict)

## ChainMap
# letters = {'a': 1, 'b': 2}
# vowels = {'a': 2, 'b': 0, 'c': 3, 'd': 0, 'e': 1}
# chain = ChainMap(letters, vowels)
# pprint(chain)
# print(chain['e'])
# print(chain['a'])
# print(chain['b'])
# print(chain['c'])
# letters['c'] = 5
# print(chain)
# print(chain['c'])
# addons = {'n': 0, 'm': 1, 'k': 1, 'a': 9}

## Метод new_child возвращает новый объект
# chain = chain.new_child(addons)
# print(chain)
# print(chain['a'])
# print(list(chain.keys()))
# print(list(chain.values()))
# print(list(chain.items()))
# return_value = dict((chain.items()))
# print(return_value)
# 

# Deque FIFO -> First In, First Out
# ex = list("python")
# deque_ex = deque(ex)
# print(deque_ex)
# print(deque_ex.__class__.__mro__)
# #
# deque_ex.append('e')      # добавление в конец
# deque_ex.appendleft('a')  # добавление в начало (левый конец)
# print(deque_ex)
# 
# right_elem = deque_ex.pop()
# left_elem = deque_ex.popleft()
# print(deque_ex)
# print(f'{right_elem =}, {left_elem = }')
# #
# deque_ex.extend([10, 11])
# deque_ex.extendleft([98, 99])
# print(deque_ex)
# #
# print(deque_ex.count('p'))
# print(deque_ex[3])
# print(len(deque_ex))

## Перенос n элементов из конца очереди в начало
# deque_ex.rotate(5)
# print(deque_ex)

# ## Перенос n элементов из начала очереди в конец
# deque_ex.rotate(-5)
# print(deque_ex)
# #
# #
# # ### Параметр maxlen
# def tail(filename, n=10):
#     """ Возвращает n последних строк файла """
#     with open(filename) as f:
#         return deque(f, maxlen=n)
#
#
# print(*tail('zen.txt'), sep='')


## реализация скользящего окна
# def moving_average(iterable, n=3):
#     # moving_average([40, 30, 50, 46, 39, 44]) # Out: 40.0 42.0 45.0 43.0
#     it = iter(iterable)
#     # Взять n - 1 элементов из итератора с помощью islice()
#     d = deque(itertools.islice(it, n - 1))  ## deque([40, 30])
#     d.appendleft(0)   # deque([0, 40, 30])
#     print(f'{d = }')
#     s = sum(d)  # s -> 70
#     # Начинаем итерироваться с элемента 50
#     for elem in it:
#         s += elem - d.popleft()
#         d.append(elem)
#         print(f'{d = }')
#         yield s / n
# 
# 
# lst = [40, 30, 50, 46, 39, 44]
# for mean in moving_average(lst):
#     print(f'{mean = }')
# #
# # Примеры работы с itertools.islice
# iter_obj = iter(lst)
# print(list(itertools.islice(iter_obj, 3, 6)))








