## Мы можем переопределять методы и атрибуты класса-Предка.
class Super(object):
    def __init__(self, age=30):
        self._age = age
        self.__name = 'python'
        self.__id = 1234

    def method1(self):
        print('in Super.method1')

    def _private(self):
        print('_private method')


## Указываем в скобках класс Предок.
class Sub(Super):
    def __init__(self, age):
        super().__init__(age)
        self.__name = 'sub python'

    def other(self):
        print('my "other" method')

    def method1(self):
        # Переопределить метод
        print('starting Sub. method1')
        # Ищем методы начиная с предков
        super().method1()   # Super(self).method1()
        # Запустить стандартное действие
        print('ending Sub.method')

if __name__ == '__main__':
    y = Super()  # Создать экземпляр Super
    y.method1()  # Выполняется Super.method in Super.method
    print(y._Super__name)  #Out: python
    print('=' * 40)
    x = Sub(50)  # Создать экземпляр Sub
    x.method1()  # Выполняется Sub method
    print(x._age)
    print(x._Super__name)  # Добавляется _ и название класса, в котором определен атрибут с двумя __
    # print(x._Sub__id)  # AttributeError: 'Sub' object has no attribute '_Sub_name'
    print(x._Sub__name)
    x._private()
    print(vars(x))
    y.method1()
    print(x.__class__.__bases__)  ## Получаем класс Предок
    print(x.__class__.__mro__)  ## MRO - method resolution order
