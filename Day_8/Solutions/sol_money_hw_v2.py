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
import requests
from functools import total_ordering
import json


@total_ordering
class Money:
    def __init__(self, full_value, additional_value):
        self.full_value = full_value
        self.additional_value = additional_value
        if additional_value > 99:
            self.full_value += additional_value // 100
            self.additional_value = additional_value - (additional_value // 100 * 100)

    def __str__(self):
        return f'{self.full_value} - рублей, {self.additional_value} - копеек'

    def __add__(self, other):
        full = self.full_value + other.full_value
        additional = self.additional_value + other.additional_value
        return Money(full, additional)

    def __sub__(self, other):
        full = self.full_value - other.full_value
        additional = self.additional_value - other.additional_value
        return Money(full, additional)

    def __mul__(self, number):
        full_value = self.full_value * number
        additional_value = self.additional_value * number
        return Money(full_value, additional_value)

    def __mod__(self, percent):
        self.full_value += self.additional_value / 100
        temporary_something = self.full_value * (percent/100)
        new_value = int(temporary_something)
        new_additional_value = round((temporary_something - int(temporary_something)) * 100)
        return Money(new_value, new_additional_value)

    def convert(self, currency):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        data_dict = json.loads(response.text)
        temp_curr = data_dict.get('Valute')
        temp_curr1 = temp_curr.get(currency)
        nominal = temp_curr1.get('Nominal')
        temp_curr2 = temp_curr1.get('Value')
        self.full_value += self.additional_value / 100
        converted_value = round((self.full_value / temp_curr2) * nominal, 2)
        return f'Перевод в {nominal} {currency} - {converted_value}'

    def __eq__(self, other):
        if self.additional_value > 99:
            self.full_value += self.additional_value // 100
            self.additional_value = self.additional_value - (self.additional_value // 100 * 100)
        if other.additional_value > 99:
            other.full_value += other.additional_value // 100
            other.additional_value = other.additional_value - (other.additional_value // 100)
        return self.full_value == other.full_value and self.additional_value == other.additional_value

    def __lt__(self, other):
        if self.additional_value > 99:
            self.full_value += self.additional_value // 100
            self.additional_value = self.additional_value - (self.additional_value // 100 * 100)
        if other.additional_value > 99:
            other.full_value += other.additional_value // 100
            other.additional_value = other.additional_value - (other.additional_value // 100)
        self.full_value += self.additional_value / 100
        other.full_value += other.additional_value / 100
        return self.full_value < other.full_value


# Создаем две денежные суммы
money1 = Money(20, 160)
money2 = Money(10, 45)

# Выводим сумму, с учетом минимального кол-ва копеек <= 99 коп
print(money1)

# Складываем суммы
money3 = money1 + money2
print(money3) # 32 - рублей, 5 - копеек

# Добавьте операцию - вычисление процента от суммы.
money4 = money3 % 20
print(money4) # 6 - рублей, 73.05 - копеек

# Конвертация валют
print(money1.convert('USD'))  # Перевод в 1 USD - 0.35
print(money1.convert('EUR'))  # Перевод в 1 EUR - 0.37
print(money1.convert('JPY'))  # Перевод в 100 JPY - 55.39 (японские иены)
