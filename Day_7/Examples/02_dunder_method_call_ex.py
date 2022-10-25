class PersonOne:
    def __init__(self, id_num):
        self.i = id_num


p1 = PersonOne(10)
print('Person Class is callable = ', callable(PersonOne))  # True
print('Person object is callable = ', callable(p1))  # False
print(callable(sum))  # True
# p1()  # TypeError: 'PersonOne' object is not callable

# Реализуем dunder метод __call__ для экземпляров класса PersonTwo
class PersonTwo:
    def __init__(self, id_var, name):
        self.id = id_var
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f'{self.id = }, {self.name = }')
        print('printing args')
        print(args) if args else print("nothing in tuple: args")
        print('printing kwargs')
        if kwargs:
            for key, value in kwargs.items():
                print(f"{key} == {value}")
            print('=' * 40)
        else:
            print('nothing in dictionary: kwargs')

    def __str__(self):
        return f'PersonTwo({self.id},{self.name})'


# ## Создание экземпляра класса PersonTwo
p2 = PersonTwo(10, 'Ivan')

## printing object
print(p2)
print(callable(p2))
print('-' * 40)
if callable(p2):
    # вызываем экземпляр класса как функцию
    p2()    # object of PersonTwo called as a function, no arguments
    print('=' * 40)

    # Передаем позиционные аргументы
    p2(10, 20)    # only args
    print('=' * 40)
    p2.__call__(30, 40)  # the same as p2(30, 40)
    print('=' * 40)

    # # Словари, как позиционные аргументы
    p2(10, 20, {'x': 1, 'y': 2}, {3, 5})  # only pos args of different types
    print('=' * 40)
    #
    # # Передаем и позиционные и именованные
    print('Это другое дело.')
    p2(10, 20, **{'x': 1, 'y': 2})  # unpacking(распаковка)
    p2(10, 20, x=1, y=2)  # the same
    p2(10, 'A', name='Python', id_number=20)  # args and kwargs both
