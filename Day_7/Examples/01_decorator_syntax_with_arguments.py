# # Version 1 with error
# def func_info(func):
#     def wrapper(*args, **kwargs):
#         print('Function name:', func.__name__)
#         print('Function docstring:', func.__doc__)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
#
# # Так не отработает
# @func_info('$')
# def mul_two(number):
#     """ func for returning triple result """
#     return number * 3
#
#
# print(mul_two(5))

# Version 2 without error
def func_info(arg1, arg2):
    print(f'Decorator arg1 = {arg1}')
    print(f'Decorator arg2 = {arg2}')

    def real_decorator(function):
        print('From real_decorator.')

        def wrapper(*args, **kwargs):
            print('Function {} args: {} kwargs: {}'
                  .format(function.__name__, args, kwargs))
            return len(arg2) * function(*args, **kwargs) * arg1

        return wrapper

    return real_decorator


# "$"  '€'
# @func_info(3, 'Python')
# def mul_two(number):
#     return number * 10


# print(mul_two(5))

# Вариант без сахара
def mul_no_sugar(number):
    return number * 10

# без сахара (@)
chg_no_sugar = func_info(12, 'hello')(mul_no_sugar)
print(chg_no_sugar(5))
print(type(chg_no_sugar))
print(chg_no_sugar)
