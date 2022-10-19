def func(a: int, b: int) -> int:
    """ return sum of two arguments """
    if hasattr(func, 'call_counter'):
        func.call_counter += 1
    else:
        func.call_counter = 1
    return a + b


# Примеры использования annotations и doc strings
print(func.__annotations__)
print(func.__doc__)

print(func(4, 8))
print(func(12, 19))
print(f'{func.call_counter = }')
print(func(3, 2))
print(f'{func.call_counter = }')
