import pprint as pp

# Создаем класс
# class MyClass:
#     def __init__(self, n):
#         self.name = n
#
#
# # Создаем экземпляры класса
# A = MyClass('A')
# B = MyClass('B')
#
# # Создаем функцию с аргументом
# def hello(self):
#     print("Этo экземпляр", self.name, "- hello")
#
# # Создаем функцию с аргументом
# def hi(some_obj):
#     print(some_obj.name + ": hi")
#
# # Ошибка, потому что у строки нет атрибута name
# # hello('value')  # Out: AttributeError
#
# # Здесь ошибки не будет
# hello(A)
#
# # Определяем функцию класса
# MyClass.say = hello
# # print(MyClass.say)
# # pp.pprint(MyClass.__dict__)
#
# # Вызываем метод экземпляра
# A.say()
#
# # Вызываем метод экземпляра
# B.say()
# #
# # Вызываем функцию класса
# MyClass.say(A)  # A.say()
# MyClass.say(B)  # B.say()
# #
# # Меняем ссылку на функцию
# MyClass.say = hi
# #
# # Вызываем метод экземпляра
# A.say()
# print(type(A.say))
# print(A.say)
#
# # Вызываем метод экземпляра
# B.say()
#
# # Вызываем функцию класса
# MyClass.say(A)
# MyClass.say(B)
# print('Before:', vars(A))
# # Теперь мы создаем атрибут у экземпляра
# A.say = hello
# print('After:', vars(A))
# # Обязательно передаем аргумент, потому что
# # работа идет не через класс МуClass
# A.say(A)
# # A.say()  # Error
# B.say()  # MyClass.say(B)
# pp.pprint(MyClass.__dict__)
# pp.pprint(A.__dict__)
# pp.pprint(B.__dict__)
# # # Здесь класс MyClass не используем
# A.say(B)  # Out: B - hello
# # А здесь класс MyClass не используем
# # B.say(A) # Out: Error
# # #
# # Удаляем функцию класса
# del MyClass.say
# print("After del:")
# print(vars(A))
# print(vars(B))
# pp.pprint(vars(MyClass))
#
# # # Вызываем метод экземпляра
# A.say(A)
# # # print(A.__dict__)
# B.say()  # AttributeError
# A.say(B) # Это отработает

# Так можно, но ненужно
# class Person:
#     def __init__(some, name):
#         some.name = name
#         print(id(some))
#
#     def add(self, s):
#         self.name += s
#         self.surname = 'Ivanov'
#         print(id(self))
#
#     def second(abcd):
#         abcd.name += ' work'
#         print(f'{abcd.name = }')
#         print(id(abcd))
#
#
# p = Person('python')
# print(id(p))
# print('Before:', p.name)
# p.add('!!!')  # Person.add(p)  s = '!!!'
# print('After:', p.name, p.surname)
# p.second()   # Person.second(p)

