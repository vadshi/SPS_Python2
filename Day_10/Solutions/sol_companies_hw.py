"""
Решить задачу, используя namedtuple

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за каждый квартал года(4 квартала) для каждого предприятия.
(можно считать с файла, можно с помощью sqlite)

Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple


raws = ['name', 'Quarter1', 'Quarter2', 'Quarter3', 'Quarter4']
Company = namedtuple('Company', raws)

company1 = Company('LG1', 100, 200, 300, 400)
company2 = Company('LG2', 100, 300, 500, 600)
company3 = Company('LG3', 400, 200, 300, 200)
company4 = Company('LG4', 500, 100, 100, 300)

companies = company1 + company2 + company3 + company4

list_average = []

for item in companies:
    if isinstance(item, (int, float)):
        list_average.append(item)

# Средняя прибыль
average = sum(list_average) / len(list_average)
print(f'Средняя прибыль - {average}')


for company in (company1, company2, company3, company4):
    if (summa := sum(company[1:5]) / 4) > average:
        print(f'У компании {company.name} средняя прибыль({summa}) больше средней({average})')
    else:
        print(f'У компании {company.name} средняя прибыль({summa}) меньше средней({average})')


