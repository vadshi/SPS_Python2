class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'{self.name} {self.age}'


jack = Person('Jack', 19)
adam = Person('Adam', 43)
becky = Person('Becky', 11)
ada = Person('Ada', 99)
adam2 = Person('Adam', 11)
people = [jack, adam, becky, ada, adam2]
print(jack == adam)
# a = sorted(people)  ## Error
print(people)


# в качестве ключа - имя
def by_name_key(obj):
    return obj.name


a = sorted(people, key=by_name_key)
print(a)  # Out: [Ada 99, Adam 43, Adam 11, Becky 11, Jack 19]

# в качестве ключа - возраст
def by_age_key(person):
    return person.age

b = sorted(people, key=by_age_key)
print(b)  # [Becky 11, Adam 11, Jack 19, Adam 43, Ada 99]

c = sorted(people, key=lambda x: x.age)
print(c) # [Becky 11, Adam 11, Jack 19, Adam 43, Ada 99]
#
print(sorted(people, key=lambda x: (ord(x.name[0]), x.age)))
# Out -> [Adam 11, Adam 43, Ada 99, Becky 11, Jack 19]

print(sorted(people, key=lambda x: (x.name, x.age)))
# Out -> [Ada 99, Adam 11, Adam 43, Becky 11, Jack 19]




