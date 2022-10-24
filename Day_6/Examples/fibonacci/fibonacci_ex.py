import functools

from clockdecorator import clock

# используется memoization
@functools.lru_cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(600))

# Пример рекурсии
# def add(n):
#     # Базовый случай
#     if n == 1:
#         print('Отработал базовый случай.')
#         return 1
#     else:
#         print(n)
#         return n + add(n - 1)
#
#
# print(add(5))