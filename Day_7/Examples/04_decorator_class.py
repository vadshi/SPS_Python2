# ==================================================
# Дополнительные библиотеки
# https://www.attrs.org/en/stable/examples.html
# https://docs.python.org/3/library/dataclasses.html
# ==================================================

from functools import wraps
from collections.abc import Callable

# Когда класс используем как декоратор,
# пишем с маленькой буквы(по соглашению)
class info:
    def __init__(self, arg1, arg2):
        print('running __init__')
        self.arg1 = arg1
        self.arg2 = arg2
        print('Decorator args: {}, {}'.format(arg1, arg2))

    def __call__(self, function: Callable):
        print('in __call__')
        # Скрываем, что это на самом деле функция wrapper
        @wraps(function)
        def wrapper(*args, **kwargs):
            print('in wrapper()')
            return function(*args, **kwargs) * self.arg1
        return wrapper


# @info(20, 'Python')   # inst = info(20, 'Python'); mul_two = inst(mul_two)
# def mul_two(num1, num2):
#     return num1 * num2


# print(mul_two(5, 3))  ## вызов функции wrapper
# print(mul_two)


def add(arg):
    return arg / 2
#
# ## Создаем экземпляр класс info
info_ex = info(10, 10)
print("=========== Следующий шаг: ===========")
add = info_ex(add)  # working __call__
print("=========== Следующий шаг: ===========")
print(add(110))     # working wrapper
print("=========== Следующий шаг: ===========")
print(type(add))
print("=========== Следующий шаг: ===========")
print(add)
# print(add(10))     # working wrapper




