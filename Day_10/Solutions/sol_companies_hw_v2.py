import csv
from collections import namedtuple


with open("comprev.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader) + ['total']
    CompanyRec = namedtuple("CompanyRec", header, rename=True)
    reestr = []
    for row in reader:
        comp = CompanyRec(*row, 0)
        reestr.append(comp)

# Атрибуты компаний
print(reestr[0]._fields)

# Выводим данные компаний
print('Before: ')
for comp in reestr:
    print(comp)

total_summa = 0
for i in range(len(reestr)):
    summa = sum(map(float, reestr[i][1:5]))
    total_summa += summa
    reestr[i] = reestr[i]._replace(total=summa)

# Выводим данные компаний после изменения поля total
print('After: ')
for comp in reestr:
    print(comp)

avg = total_summa / len(reestr)
print(f'{avg=}')
print("More:")
for c in reestr:
    if c.total > avg:
        print(f'{c.name}: {c.total} > {avg}')
print("Less:")
for c in reestr:
    if c.total < avg:
        print(f'{c.name}: {c.total} < {avg}')


# Проход по всем полям всех экземпляров V1
all_summa = 0
for c in reestr:
    for field in c._fields:
        if field.startswith('q'):
            all_summa += float(eval(f'c.{field}'))

print(f'{all_summa = }')
print(f'average = {all_summa / 10}')

# Проход по всем полям всех экземпляров V2
all_summa = 0
for c in reestr:
    for field in c._fields:
        if field.startswith('q'):
            idx = c._fields.index(field)
            try:
                all_summa += float(c[idx])
            except Exception as error:
                print(field, error)


print(f'{all_summa = }')
print(f'average = {all_summa / 10}')
