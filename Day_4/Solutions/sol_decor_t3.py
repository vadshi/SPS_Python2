import string as st
from collections.abc import Callable
from random import choices  # choices(iterable, k=0) - возвращает список из k элементов последовательности с повтором
from random import sample  # sample(iterable, k=0) - возвращает список из k элементов последовательности без повторов
from random import shuffle
from functools import wraps

digits = st.digits
lower = st.ascii_lowercase
upper = st.ascii_uppercase
punc = st.punctuation

"""
Написать класс декоратор, который принимает в качестве аргументов имена наборов
из модуля string(punctuation, ascii_lowercase, ascii_uppercase, digits) и возвращает
случайную строку из символов указанных наборов.
Аргумент string_len функции password > 4
Пример:
До декорирования: 
print(password(5))   # Out: 84743

После декорирования:
@strong('lower', 'punc')

print(password(5))   # Out: au%d#
"""
CHARS = {'digits': digits, 'lower': lower, 'upper': upper, 'punc': punc}


class strong:
    def __init__(self, *args):
        if args:
            lst = list(''.join([CHARS[arg] for arg in args]))
            shuffle(lst)  # это необязательно
            self.dictionary: str = ''.join(lst)
        else:
            self.dictionary: str = digits

    def __call__(self, func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            weak_password = func(*args, **kwargs)
            print(f'{weak_password = }')
            strong_password = choices(self.dictionary, k=len(weak_password))
            strong_password = ''.join(strong_password)
            assert type(weak_password) == type(strong_password)
            return strong_password
        return wrapper


@strong('lower', 'digits')
def password(string_len: int) -> str:
    """ Функция генерирует строку случайных символов
        указанной длины из набора st.digits"""
    return ''.join(choices(digits, k=string_len))


print(password(10))  # Out: 84743
