"""
Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
Пример 1:
********
*Привет*
********
Пример 2:
****
*23*
****
Пример 3:
**************
*[34, 45, 12]*
**************
"""


def asterisks(function):
    def wrapper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        num_asterisks = len(str(func_result)) + 2
        return f"{'*' * num_asterisks}\n*{str(func_result)}*\n{'*' * num_asterisks}"
    return wrapper


@asterisks
def func(arg):
    return arg


@asterisks
def func_two(a, b):
    return a + b


# Тестовая часть
print(func('Привет'))
print(func(23))
print(func([34, 45, 12]))
print(func(arg=100))
print(func_two('hello ', 'python'))
