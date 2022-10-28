from operator import attrgetter
# from operator import itemgetter   # для словарей
import random as rnd


class Person(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __str__(self):
        return f'name={self.name}, age={self.age}, salary={self.salary}'
    
    def __repr__(self):
        return f'{self.name} {self.age} {self.salary}'


def by_name_key(person):
    return person.name


jack = Person('Jack', 19, rnd.randint(1000, 100000))
adam = Person('Adam', 43, rnd.randint(1000, 100000))
becky = Person('Becky', 11, rnd.randint(1000, 100000))
people = [jack, adam, becky]


get_name = attrgetter('name')
print(type(get_name))
result = get_name(jack)
print(result) # 'Jack'
print(attrgetter('name', 'age')(adam))
# print(attrgetter('surname')(becky)) # AttributeError

result = sorted(people, key=attrgetter('name'))
print(result)  # [Adam 43 79598, Becky 11 48474, Jack 19 83264]

result = sorted(people, key=attrgetter('age'))
print(result) # [Becky 11 21714, Jack 19 93711, Adam 43 29971]

result = sorted(people, key=attrgetter('salary'), reverse=True)
print(*result, sep='\n')

