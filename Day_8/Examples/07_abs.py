# ====================
# Реализация зоопарка
# ====================
# class Lion:
#     def give_food(self):
#         print("Накормим льва мясом!")
#
#
# class Panda:
#     def feed_animal(self):
#         print("Накормим панду вкусным бамбуком!")
#
#
# class Snake:
#     def feed_snake(self):
#         print("Накормим змею мышами!")
#
#
# # Создадим животных:
# leo = Lion()
# po = Panda()
# sam = Snake()
#
# # Накормим всех животных
# leo.give_food()
# po.feed_animal()
# sam.feed_snake()
#
# # Мы хотели бы оптимизировать этот процесс, поэтому одним из вариантов может
# # быть список, в который мы поместим всех животных
# zoo = [leo, po, sam]  # Здесь может быть больше животных
#
# # Пройдемся по зоопарку и накормим животных
# for animal in zoo:
#     ## Вопрос в том, какой метод вызывать?
#     ## animal.give_food() или animal.feed_animal()?
#     animal.feed() # ошибка AttributeError!



# ====================================
# Абстрактные классы(Abstract classes)
# ====================================
# чтобы не осталось ни одного ненакормленного животного,
# мы используем абстрактные классы

# from abc import ABC, abstractmethod
#
# class Animal(ABC):   # наследуемся от ABC(Abstract base class)
#     @abstractmethod  # декоратор для абстрактного метода(abstract method)
#     def feed(self):
#         pass


# ==============================================================
# Если класс наследуется от абстрактного класса, он должен иметь
# реализации всех абстрактных методов
# class Panda(Animal):
#     # Имя метода должно совпадать с именем метода класса Animal
#     def wrong_name(self):
#         print("Накормим панду вкусным бамбуком!")
#
#
# po = Panda()  # TypeError: Can't instantiate abstract class Panda with abstract method feed
# # ==============================================================
# #
# # # теперь реализация правильная
# class Lion(Animal):
#     def feed(self):
#         print("Накормим льва мясом!")
#
#
# class Panda(Animal):
#     def feed(self):
#         print("Накормим панду вкусным бамбуком!")
#
#
# class Snake(Animal):
#     def feed(self):
#         print("Накормим змею мышами!")


# zoo = [Lion(), Panda(), Snake()]
#
# for animal in zoo:
#     animal.feed()  # Теперь здесь не будет ошибки

# # ================================
# # Абстрактные методы с параметрами
# # ================================
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     # переименуем метод в "do" и добавим параметр "action"
#     @abstractmethod
#     def do(self, action):
#         pass
# #
# # #
# class Lion(Animal):
#     # "time" - это дополнительный параметр
#     def do(self, action, time):
#         print(f"{action} льва! В {time}")
#
#     def give_water(self):
#         print('вода для льва')
#
#
# class Panda(Animal):
#     def do(self, action, time):
#         print(f"{action} панду! В {time}")
#
#
# class Snake(Animal):
#     def do(self, action, time):
#         print(f"{action} змею! В {time}")
#
#
# zoo = [Lion(), Panda(), Snake()]
# #
# for animal in zoo:
#     animal.do(action="Кормим", time="10:10")
#
#
# lo = Lion()
# lo.give_water()
#
# # Добавим абстрактные методы с помощью @property
from abc import ABC, abstractmethod


class Animal(ABC):
    @property
    def food_eaten(self):
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        # проверка для аргумента food
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"{food} не входит в рацион этого животного.")

    @property
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod
    def feed(self, time):
        pass


# Создаем классы-потомки, в которых должны быть реализованы:
# 1. атрибут diet
# 2. метод feed()
class Lion(Animal):
    @property
    def diet(self):
        return ["антилопа", "буйвол"]

    def feed(self, time):
        print(f"Кормим льва. Сегодня у него {self._food}! В {time}")


class Snake(Animal):
    @property
    def diet(self):
        return ["лягушка", "кролик"]

    def feed(self, time):
        print(f"Кормим змею. Сегодня у нее {self._food}! В {time}")


class Panda(Animal):
    @property
    def diet(self):
        return ['Бамбук']

    def feed(self, time):
        print(f"Кормим панду. Сегодня у нее {self._food}! В {time}")


leo = Lion()
leo.food_eaten = "антилопа"
leo.feed("10:20")
adam = Snake()
adam.food_eaten = "лягушка"
adam.feed("10:30")

pa = Panda()
# ValueError: Не бамбук не входит в рацион этого животного.
# pa.food_eaten = 'Не бамбук'

# ValueError: морковка не входит в рацион этого животного.
# leo.food_eaten = "морковка"
leo.feed("10:40")
