""" реализация игры "Камень, ножницы, бумага" """
import random


class Thing(object):
    def __str__(self):
        return f'{self.__class__.__name__}'


class Rock(Thing):
    pass


class BrownRock(Rock):
    pass


class Paper(Thing):
    pass


class WhitePaper(Paper):
    pass


class Scissors(Thing):
    pass


def beats(x, y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None  # Нет победителя
        elif isinstance(y, Paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Paper):
        if isinstance(y, Rock):
            return x
        elif isinstance(y, Paper):
            return None  # Нет победителя
        elif isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Scissors):
        if isinstance(y, Rock):
            return y
        elif isinstance(y, Paper):
            return x
        elif isinstance(y, Scissors):
            return None  # Нет победителя
        else:
            raise TypeError("Unknown second thing")
    else:
        raise TypeError("Unknown first thing")


rock, paper, scissors = BrownRock(), WhitePaper(), Scissors()
lst = [rock, paper, scissors]
i = 0
while i < 10:
    first = random.choice(lst)
    second = random.choice(lst)
    print(f'{first} vs {second}. {beats(first, second)} win')
    i += 1

# beats(paper, 3)  # TypeError: Unknown second thing

# Пробегаемся по всем классам предкам
print(isinstance(rock, Thing))
print(isinstance(True, int))


# ## Показать иерархию классов
print(rock.__class__.__mro__)
print(True.__class__.__mro__)

# проверяем, что Thing предок класса Rock
print(issubclass(BrownRock, Thing))     # True
print(issubclass(Rock, object))   # True

# аргументы - только классы, поэтому ошибка
# print(issubclass(rock, Thing))  # Error

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale(self, number):
        if isinstance(number, (int, Thing)):
            print(f'Point({self.x} x {self.y}) on {number} ')


p = Point(3, 10)
p.scale(rock)
