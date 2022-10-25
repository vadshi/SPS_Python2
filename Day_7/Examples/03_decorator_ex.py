class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    # __call__ выступает в качестве wrapper
    def __call__(self, *args):
        print('> перед вызовом __call__', self.func.__name__)
        result = self.func(*args)
        print('> после вызова __call__')
        return result


# @Decorator
def wrapped(arg):   # wrapped = Decorator(wrapped)
    return f'Результат работы: {arg = }, функция wrapped'


# print('НАЧАЛО:')
# print(wrapped('hello'))  # __call__ отработает здесь
# print('КОНЕЦ')

## Без сахара(без конструкции @Decorator, сам механизм)
print(wrapped('hello'))
print("Before", wrapped)
wrapped = Decorator(wrapped)
# print(type(wrapped))
print(wrapped.func)
print("After:", wrapped)  # экземпляр класса Decorator
# print(callable(wrapped))
print(wrapped('hello'))   # __call__ отработает здесь
