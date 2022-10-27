import sys
from collections import namedtuple


### Namedtuple
## В Python именованные кортежи неплохо рассматривать как эффективную
## с точки зрения потребления оперативной памяти краткую форму для
## определения неизменяющегося класса вручную.
## метод __repr__ уже определен

# columns = ['fname', 'pname', 'lname', 'age']
# # Первый аргумент это имя, а второй аргумент - это список атрибутов класса User
# User = namedtuple('User', columns)
# print(type(User), User)
# user = User('Иван', 'Иванович', 'Иванов', 30)
# print(user)
# print(user.lname)
# user.pname = 'change'  # Error

## Пример со списком в качестве атрибута
# Person = namedtuple("Person", "name children")  # неявно вызывается split()
# petr = Person("Petr Ivanovich", ["Anna", "Mikhail"])
# print(f'Before: {petr = }')
# petr.children.append('Svetlana')
# print(f'After: {petr = }')

# Пример с точкой. Порядок атрибутов имеет значение
# Point = namedtuple('Point', 'x y z')
# p = Point(x=1, y=2, z=4)
# print(p)
# print(p.x)
# print(p[2])  # z
#
# # Запрещаем создание атрибутов у объектов класса
# class NewPoint(namedtuple('Point', ['x', 'y'])):
#     __slots__ = ()  # предотвращает создание словарей экземпляров
#     @property
#     def distance_from_zero(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def __str__(self):
#         return f'Point: x={self.x:6.3f}, y={self.y:6.3f}, dist={self.distance_from_zero:6.3f}'
# #
# #
# for p in NewPoint(3, 4), NewPoint(14, 5/7):
#     print(p)
# # # # #
# point1 = NewPoint(4, 4)
# # point1.name = 'name'  # AttributeError
# print(point1.distance_from_zero)


# Методы namedtuple
# Car = namedtuple('Car', 'color mileage')  # неявно вызывается split()
# # Car = namedtuple('Car' , ['color', 'mileage'])  ## the same
#
# my_car = Car('red', 123000)
# # доступ к значениям через атрибуты
# print(f'{my_car.color = }')
# print(f'{my_car.mileage = }')
#
# # доступ к значениям через индексы
# print(f'{my_car[0] = }')
# print(f'{my_car[1] = }')
# print(tuple(my_car))
# color_value, mileage_value = my_car
# print(f'{color_value = }', f'{mileage_value = }')
# print(*my_car)
# print(f'{my_car = }')
#
# # my_car.color = 'brown' ## Error
# attr = {'mileage': 345, 'color': 'green'}
# car_two = Car(**attr)  # Car(color='green', mileage=345)
# print(f'{car_two = }')
#
# ## расширяем класс авто
# class MyCarWithMethods(Car):
#     def hexcolor(self):
#         if self.color == 'red':
#             return '#Oxff0000'
#         else:
#             return '#Ox000000'
#
#     def maintenance(self):
#         if self.mileage > 10000:
#             return "It's time for maintenance"
#
#
# new_car = MyCarWithMethods('red', 89700)
# print(new_car.hexcolor())
# print(new_car.maintenance())
#
# # # Самый легкий способ создать иерархии именованных кортежей —
# # # использовать свойства _fields базового кортежа:
# print(Car._fields)
# ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
# el_car = ElectricCar('red', 123, 45.0)
# print(f'{el_car = }')
# #
# # Помимо свойства _fields, каждый экземпляр именованного кортежа также
# # предлагает еще несколько вспомогательных методов, которые могут
# # быть полезны. Все их имена начинаются с одинарного символа
# # подчеркивания ('_'), который обычно сигнализирует о том, что метод или
# # свойство являются «приватными» и не являются частью стабильного
# # публичного интерфейса класса или модуля.
# #
# # В случае с именованными кортежами согласованное правило
# # именования с символом подчеркивания несет в себе другой смысл. Эти
# # вспомогательные методы и свойства являются составной частью публичного
# # интерфейса класса namedtuple.
# # Вспомогательные методы получают такие имена, чтобы избежать конфликтов
# # имен с определяемыми пользователями полями кортежей.
#
# asdict_res = el_car._asdict()
# print(f'{asdict_res = }')
#
# # Чтобы вызвать значение через строковый ключ,
# # необязательно преобразовывать namedtuple – подходит стандартная функция getattr():
# print(getattr(el_car, 'charge'))
#
# # Метод _replace() создает копию кортежа(с новым id) и позволяет вам выборочно
# # заменять некоторые его поля:
# print('Before:', my_car)
# my_car = my_car._replace(color='blue')
# print('After:', my_car)
#
# # метод класса _make() может использоваться для создания новых
# # экземпляров класса namedtuple из (итерируемой) последовательности:
# car_one = Car._make(['brown', 111])
# print(car_one)

# # Именованные кортежи часто используются для назначения имён полей кортежам,
# # возвращаемым модулями csv или sqlite3:
import csv
## Пример 1
# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# #
# for emp in map(EmployeeRecord._make, csv.reader(open("employees_one.csv", "r"))):
#     print(emp.name, emp.age, emp.title, emp.department, emp.paygrade)
#
# print(emp)
#
# print('=' * 50)
# # Пример 2
# lst = []
# with open("employees_two.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     Employee = namedtuple("Employee", next(reader), rename=True)
#     for row in reader:
#         employee = Employee(*row)
#         lst.append(employee)
#
# print(lst)
# print(f'{lst[0].name}, '
#       f'{lst[0].job}, '
#       f'{lst[0].email}')


# Пример 3
# import sqlite3
# # #
# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
#
# # Создаем базу данных, если нет
# # # ================================================================================
# connection = sqlite3.connect('companydata.db')
# cursor = connection.cursor()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS employees
# (name TEXT, age INTEGER, title TEXT,
# department TEXT, paygrade INTEGER)
# """)
# ## Подтверждение изменений(сохрани изменения)
# connection.commit()
# employees = [('Ivan', 23, 'manager', 'Management', 10000),
#              ('Petr', 45, 'programmer', 'IT', 20000),
#              ('Sidr', 56, 'director', 'Management', 30000)]
# cursor.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", employees)
# connection.commit()
# # # ================================================================================
# emp_list = []
# cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     emp_list.append(emp)
#
# connection.close()
#
# for emp in emp_list:
#     print(emp)
#     print(emp.name, emp.age, emp.title, emp.department, emp.paygrade)
#
# total = 0
# for emp in emp_list:
#     total += emp.paygrade
# print(f'{total = }')

# Размер, занимаемый в памяти меньше, чем у аналогичного словаря
# Point = namedtuple("Point", "x y z")
# point = Point(1, 2, 3)
#
# namedtuple_size = sys.getsizeof(point)
# dict_size = sys.getsizeof(point._asdict())
# gain = 100 - namedtuple_size / dict_size * 100
#
# print(f"namedtuple: {namedtuple_size} bytes ({gain:.2f}% smaller)")
# print(f"dict:       {dict_size} bytes")

# Скорость доступа к данным быстрее, чем у аналогичного словаря
# from time import perf_counter
#
#
# def average_time(structure, test_func):
#     time_measurements = []
#     for _ in range(1_000_000):
#         start = perf_counter()
#         test_func(structure)
#         end = perf_counter()
#         time_measurements.append(end - start)
#     return sum(time_measurements) / len(time_measurements) * int(1e9)
#
#
# def time_dict(dictionary):
#     "x" in dictionary
#     "missing_key" in dictionary
#     2 in dictionary.values()
#     "missing_value" in dictionary.values()
#     dictionary["y"]
#
#
# def time_namedtuple(named_tuple):
#     "x" in named_tuple._fields
#     "missing_field" in named_tuple._fields
#     2 in named_tuple
#     "missing_value" in named_tuple
#     named_tuple.y
#
#
# Point = namedtuple("Point", "x y z")
# point = Point(x=1, y=2, z=3)
# #
# namedtuple_time = average_time(point, time_namedtuple)
# d = point._asdict()
# dict_time = average_time(d, time_dict)
# gain = dict_time / namedtuple_time
#
# print(f"namedtuple: {namedtuple_time:.2f} ns ({gain:.2f}x faster)")
# print(f"dict:       {dict_time:.2f} ns")
