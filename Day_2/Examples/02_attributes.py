# Красивый вывод словаря(вертикально)
from pprint import pprint


class People:
    """ first class for learning """
    name = "Teachers"


## Встроенный(системный)
# print(People.__name__)
# People.__name__ = 'Some people'
# print(People.__name__)
#
# Сами создаем в классе
# print(People.name)
# print(id(People))
# p = People()
# print(p.name)
# P1 = People      # еще одна ссылка на класс People
# person1 = P1()  # создаю экземпляр на основе класса People
# print(id(P1))
# print(id(People) == id(P1))
# print(People is P1)
# print(p)  # repr(p)
# print(f'{hex(id(p)).upper(): >45}')
#
# # Объект живет, пока есть ссылка на него
# # ======================================
# del People
# doubt_p = P1()
# print(doubt_p)
# print(P1.__name__)
# # p2 = People()  # Out: NameError: name 'People' is not defined
# del P1
# print(p.name)
# # Получаем словарь объекта
# print(vars(p))
# People = type(p)
# print(id(People))
# p9 = People()
# print(type(p9))
# pprint(vars(People))
# ======================================

## class People, создаю новый экземпляр
# print(type(p))
# new_p = type(p)()  # new_p = People()
# print(type(new_p))
# print(new_p)
# print(id(new_p))
#
# ## Получаю доступ к классу экземпляра
# print(p.__class__)
# print(new_p.__class__)
# print('=' * 40)
# # # #
# # # # # Создаем экземпляр
# p2 = p.__class__()  # p2 = People()
# print(type(p2), p2)
# print('=' * 40)

# Получаю доступ к классу экземпляра
# и затем к имени класса
# print(p.__class__.__name__)  # Out: People
# print(p.name)  # Out: Teachers
# p.__class__.__name__ = "Person"
# print(p.__class__.__name__)
# print(People.__name__)
# #
# print(p.__name__)  # AttributeError
# print(type(People))  # <class 'type'>
# p4 = People()
# print(p4.__class__.__name__)

## Доступ к полям класса
# # Получаем словарь объекта
p = People()
pprint(People.__dict__)
People.count = 20
print(p.count)
print(p.name)
pprint(People.__dict__)
pprint(p.__dict__)  # Out: {}

## Создаем значение для атрибута экземпляра
p.count = 30
pprint(p.__dict__)
pprint(p.__class__.__dict__)  # People.__dict__
print(p.count)
print(vars(p).get('name'))
#
del People.name
pprint(People.__dict__)
# print(p.name)  # AttributeError
print(p.count) # Ошибки не будет

p.name = 'Students'
p.age = 22
pprint(p.__dict__)
# #
# # функция vars покажет словарь атрибутов объекта
print(vars(p))
pprint(vars(People))

# ===== PAUSE =====

# p.__class__.name = 'SName'  # People.name = 'SName'
# # pprint(People.__dict__)
# # print(p.__dict__)
# # #
# # ## Функции getattr, setattr, delattr, hasattr
# # # название класса, имя атрибута,
# print(getattr(People, 'name', ))  # Out: People.name -> SName
# #
# # # Вернет третий аргумент, если атрибута нет
# print(getattr(People, 'name2', 'Такого нет'))
# #
# # # # название класса, имя атрибута, значение атрибута
# setattr(People, 'course', 'Python')  # People.course = 'Python'
# pprint(People.__dict__)
#
# # # # Удаляем атрибут
# delattr(People, 'course')
# pprint(People.__dict__)
#
# # # проверка наличия атрибута у объекта(класс,экземпляр)
# print(hasattr(People, 'age'), hasattr(People, 'name'))
# print(hasattr(p, "name"), hasattr(p, 'age'))
#
#
# # # Проверка понимания
# People.some = 567
# print(hasattr(p, 'some'))  # True
# print(p.some)

## Экземпляры класса. Класс как Callable объект
# экземпляры класса не зависят друг от друга
# class Student:
#     name = 'First'
#
#
# s1 = Student()
# s2 = Student()
# print(s1.name)
# print(s2.name)
# print(id(Student.name))  # id одинаковый
# print(id(s1.name))       # id одинаковый
# print(id(s2.name))       # id одинаковый
# print(s1.__dict__)  # Out: {}
# print(s2.__dict__)  # Out: {}
# s1.name = 'Second'
# s2.name = 'Third'
# s2.age = 22
# print(s1.__class__.__name__)
# print(s1.__dict__)  # Out: {'name':'Second'}
# print(s2.__dict__)  # Out: {'name':'Third', 'age':22}
# pprint(Student.__dict__)
# # print(s1.age)  # AttributeError: 'Student' object has no attribute 'age'
# #
# s3 = Student()
# s4 = Student()
# Student.name = 'Last'
# print(s3.name)  # Out: Last
# print(s1.name)  # Out: Second

# print('*' * 50)

# Методы класса
# class StudentBetter:
#     def __init__(self, name='Ivan'):
#         self.name = name
#         self.surname = 'Ivanov'
#
#     def hello1(self) -> None:
#         self.name += ' addons'
#
#     def hello3(self) -> None:
#         print(self.name, self.surname)
#
#     def hello2():
#         print('Hello, Student')
#
#
# print(f'{id(StudentBetter) = }')
# print(StudentBetter.hello1)
# print(id(StudentBetter.hello1))
# sb = StudentBetter()
# print(f'{id(sb) = }')
# print(sb.hello1)
# print(id(sb.hello1))
# # #
# # # Работаем через класс
# sb.hello1()  # StudentBetter.hello1(sb)
# print(sb.name)
# StudentBetter.hello1(sb)  # sb.hello1()
# print(sb.name)
# # # #
# # # Два одинаковых вызова
# sb.hello3()
# StudentBetter.hello3(sb)  # sb.hello3()
#
# # # Важный момент с hello2()
# StudentBetter.hello2()   # Отработает
# # sb.hello2()               # TypeError
# # StudentBetter.hello2(sb)  # TypeError
#
# print(sb.__dict__)
# print(sb.hello1.__self__)
# print(hex(id(sb)))
# print(sb.hello1.__func__)
# print(type(sb.hello1))
