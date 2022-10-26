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



Примечание: список всех методов для перегрузки операций:
(https://pythonworld.ru/osnovy/peregruzka-operatorov.html).


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

Доработайте класс Money, добавив ему метод .convert(),
для конвертации суммы в рублях в евро и доллары(*любую валюту).
Актуальные значения можно взять, сделав запрос на:
https://www.cbr-xml-daily.ru/daily_json.js

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
import json
import requests


url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

CURRENCIES = json.loads(response.text)


@total_ordering
class Money:
    def __init__(self, rub, kop):
        self.value = rub * 100 + kop

    def _rub_kop_split(self):
        return divmod(self.value, 100)

    def __str__(self):
        rub, kop = self._rub_kop_split()
        return f'{rub} руб {kop:0>2d} коп'

    def __repr__(self):
        rub, kop = self._rub_kop_split()
        return f'{rub} руб {kop:0>2d} коп'

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        return Money(0,  self.value + other.value)

    def __sub__(self, other):
        if self.value >= other.value:
            return Money(0, self.value - other.value)
        raise Exception('no debt')

    def __mul__(self, arg: int):
        if type(arg) == int:
            return Money(0, self.value * arg)
        raise TypeError('bad type argument.')

    def __mod__(self, percent: int | float):
        if type(percent) in (int, float):
            return Money(0, round(self.value * percent / 100))
        raise TypeError('bad type argument.')

    def convert(self, currency: str):
        currency_rate = CURRENCIES['Valute'][currency]['Value']
        currency_value = round(self.value / currency_rate)
        print(f'{currency_rate:.2f} RUB == 1 {currency}')
        return f'{self} == {currency_value // 100}.{currency_value % 100} {currency}'


def main():
    # Создаем сумму из 20 рублей и 120 копеек
    money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

    # Выводим сумму, с учетом минимального кол-ва копеек <= 99 коп
    print(money1)  # 21руб 20коп

    # Создаем две денежные суммы
    money1 = Money(20, 60)
    money2 = Money(10, 45)
    print(f'{money1 = }')
    print(f'{money2 = }')

    # Проверяем операции сравнения
    print(money1 == money2)
    print(money1 != money2)
    print(money1 > money2)
    print(money1 >= money2)
    print(money1 < money2)
    print(money1 <= money2)

    # Складываем суммы
    money3 = money1 + money2
    print(f'{money3 = }')  # 31руб 05коп

    # Вычитаем суммы
    money6 = money1 - money2
    print(f'{money6 = }')

    # Умножаем на число
    money4 = money2 * 3
    print(f'{money4 = }')

    # Находим 20% от суммы
    money5 = money1 % 20
    print(f'{money5 = }')   # 4 руб 12 коп

    # Конвертация
    money4 = Money(2530, 45)
    money5 = money4.convert('EUR')
    print(money5)


    # check error
    # money7 = money2 - money1   # Out: Exception: no debt


if __name__ == '__main__':
    main()
