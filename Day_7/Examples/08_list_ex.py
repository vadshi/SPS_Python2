# Не забываем об этом
lst10 = [1, 2, True, 'py', 'hello', 8.1, 'go', 'java', 8]
# #
# # # Не рекомендуется изменять список во время итерирования
# for item in lst10:
#     if type(item) == str:
#         lst10.remove(item)
# print(lst10)
#
# # Лучше так
lst1 = [item for item in lst10 if type(item) != str]
# lst1.sort()
print(f'{lst1 = }')
#
#
# # Особенности работы с mutable types в качестве значений по умолчанию
def bad_func(a, lst=[]):
    lst.append(a)
    return lst


lst2 = bad_func(99, lst1)
print(lst2)
# #
lst3 = bad_func(1)
print(lst3)  # Out: [1]

lst4 = bad_func(100)
print(lst4)  # Out: [1, 100]

lst5 = bad_func(10)
print(lst5)  # Out: [1, 100, 10]


# # Как нужно реализовать (через None):
def good_func(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    return lst


lst2 = good_func(999, lst1)
print(lst2)

lst3 = good_func(1)
print(lst3)  # Out: [1]

lst4 = good_func(100)
print(lst4)  # Out: [100]

lst5 = good_func(10)
print(lst5)  # Out: [10]



