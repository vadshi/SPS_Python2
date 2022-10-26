"""
class Money

Напишите класс для работы с денежными суммами.

Реализовать:
*   сложение
*   вычитание
*   умножение на целое число
*   сравнение (больше, меньше, равно, не равно)

==========================================================================================
from functools import total_ordering
Описываемый декоратор, позволяет для классов, в которых определён __eq__(), а также один из
__lt__(), __gt__(), __le__(), __ge__(), сгенерировать остальные методы автоматически.

    @total_ordering
    class Student:

        def __eq__(self, other):
            return self.last_name == other.last_name

        def __lt__(self, other):
            return self.last_name < other.last_name

=========================================================================================

При всех операциях, сумма должна преобразовываться к сумме с минимальным количеством копеек.

Примеры:
# Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

# Выводим сумму, с учетом минимального кол-ва копеек <= 99 коп
print(money1) # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 5коп



Примечание: список всех методов для перегрузки операций: (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).


#### Дополнительные задания **

Добавьте операцию - вычисление процента от суммы. %

Пример:

# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money1 % 21

print(percent_sum)  # 4руб 33коп

__mod__()
Пояснение: % (процент от суммы) - должна являться новая денежная сумма.
После вычисления процента, используем округление (функция round())


### Конвертация валют

Доработайте класс Money, добавив ему метод .convert(), для конвертации суммы в рублях в евро и доллары(*любую валюту).
Актуальные значения можно взять, сделав запрос на: https://www.cbr-xml-daily.ru/daily_json.js

#### Отправка запроса на url-адрес

pip install requests
py -m pip install requests
import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

, где url - адрес сайта, на который отправляете запрос.

В переменную response получите ответ сайта.

Для преобразования ответа из json-формата используйте функцию:

import json
data_dict = json.loads(response.text)

Модуля json

print(data_dict['Valute']['EUR']['Value'])
"""

from functools import total_ordering
import requests
import json


@total_ordering
class Money:
    def __init__(self, rub, kop):
        self.value = rub * 100 + kop

    def __str__(self):
        return f'{self.value // 100} руб {self.value % 100} коп'

    def __repr__(self):
        return f'{self.value // 100} руб {self.value % 100} коп'

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        self.value += other.value
        return self

    def __sub__(self, other):
        self.value -= other.value
        return self

    def __mul__(self, other):
        if type(other) == int:
            self.value *= other
        else:
            raise TypeError

    def __mod__(self, other):
        if type(other) == int or type(other) == float:
            self.value = round(self.value * other / 100)
            return self
        else:
            raise TypeError

    def convert(self, valute):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)

        data_dict = json.loads(response.text)
        valute_rate = data_dict['Valute'][valute]['Value']
        valute_value = round(self.value / valute_rate)

        return f'{valute_value // 100}.{valute_value % 100} {valute}'


# Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

# Выводим сумму, с учетом минимального кол-ва копеек <= 99 коп
print(money1) # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 5коп

# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money1 % 21

print(percent_sum)  # 4руб 33коп

#Конвертация
money4 = Money(2530, 45)
money5 = money4.convert('EUR')
print(money5)
