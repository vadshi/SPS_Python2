# super() – супер класс Python

# Есть какой-то товар в классе Base с базовой ценой в 10 единиц.
# Нам понадобилось сделать распродажу и скинуть цену на 20%.

# Variant 1
class Base:
    def price(self):
        return 10


class Discount(Base):
    def price(self):
        return 8
    
    
# Variant 2
class Discount(Base):
    def price(self):
        return Base.price(self) * 0.8  
    
# Главное не забыть указать self при вызове первым параметром явно,
# чтобы метод был привязан к текущему объекту.

# Это будет работать, но этот код не лишен изъянов,
# потому что необходимо явно указывать имя предка.
# Представьте, если иерархия классов начнет разрастаться?
# Например, нам нужно будет вставить между этими классами еще один класс,
# тогда придется редактировать имя класса-родителя в методах Discount:    
class Base:
    def price(self):
        return 10


class InterFoo(Base):
    def price(self):
        return Base.price(self) * 1.1


class Discount(InterFoo):  # <--
    def price(self):
        return InterFoo.price(self) * 0.8  # <--
    
# Функция super()
# Будучи вызванным без параметров внутри какого-либо класса,
# super() вернет прокси-объект, методы которого будут искаться только в классах,
# стоящих ранее, чем он, в порядке MRO.
# То есть, это будет как будто бы тот же самый объект,
# но он будет игнорировать все определения из текущего класса, обращаясь
# только к родительским:
class Base:
    def price(self):
        return 10


class InterFoo(Base):
    def price(self):
        return super().price() * 1.1


class Discount(InterFoo):
    def price(self):
        return super().price() * 0.8


# Для Discount порядок MRO:
# Discount -> InterFoo -> Base -> object.
# Вызов super().price() внутри класса Discount будет игнорировать
# Discount.price(), а будет искать price() в InterFoo, затем, если не найдет,
# то в Base и object.


# Использование в конструкторе класса
class A:
    def __init__(self):
        self.x = 10

# ошибочный вариант класса B
# class B(A):
#     def __init__(self):
#         self.y = self.x + 5
#
# print(B().y)  # ошибка! AttributeError: 'B' object has no attribute 'x'

# правильно:
class B(A):
    def __init__(self):
        super().__init__()  # <- не забудьте!
        self.y = self.x + 5


print(B().y)  # 15


# Параметры super()

# Функция может принимать 2 параметра. super([type [, object]]).
# Первый аргумент – это тип, к предкам которого мы хотим обратиться.
# А второй аргумент – это объект, к которому надо привязаться.
# Сейчас оба аргумента необязательные.
# В прошлых версиях Python приходилось их указывать явно:
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x):
        super(B, self).__init__(x)
        # теперь это тоже самое: super().__init__(x)
        
        
# Теперь Python достаточно умен, чтобы самостоятельно подставить в аргументы
# текущий класс и self для привязки. Но старая форма тоже осталась для особых
# случаев. Она нужна, если вы используете super() вне класса или хотите явно
# указать с какого класса хотите начать поиск методов.
d = Discount()
print(super(Discount, d).price())  # d.price() из InterFoo

# В этом случае объект, полученный из super(), будет вести себя как
# класс InterFoo (родитель Discount), хотя привязан он к переменной d,
# которая является экземпляром класса Discount.


