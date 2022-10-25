import string as st
from random import choices   # choices(iterable, k=0) - возвращает список из k элементов последовательности с повтором
from random import sample    # sample(iterable, k=0) - возвращает список из k элементов последовательности без повторов


digits = st.digits
lower = st.ascii_lowercase
upper = st.ascii_lowercase
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



# @strong
def password(string_len):
    """ функция генерирует строку случайных символов 
	    указанной длины из набора st.digits"""
    pass
    
    

print(password(5))   # Out: 84743