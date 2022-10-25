class DateTime(object):
    # oбычный конструктор, который принимает 3 числа
    def __init__(self, day=10, month=10, year=2000):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    # Используем этот метод класса, как другой конструктор
    @classmethod
    def from_string(cls, string_date: str):   # cls - это ссылка на сам класс DateTime
        day, month, year = map(int, string_date.split('-'))
        my_date = cls(day, month, year)   # cls(day, month, year) == DateTime(day, month, year)
        return my_date
        
    @staticmethod
    def is_valid_date(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 3999

    # можно, но не нужно
    # @staticmethod
    # def from_string1(date_as_string):
    #     day, month, year = map(int, date_as_string.split('-'))
    #     return DateTime(day, month, year)

is_valid = DateTime.is_valid_date('20-05-1994')
if is_valid:
    date_obj = DateTime.from_string('20-05-1994')
    print(date_obj)
date_obj2 = DateTime()
print(date_obj2)
date_obj3 = DateTime(1, 1, 2021)
print(date_obj3)

date_obj5 = DateTime(50, 24, 21)
print(date_obj5)
print(date_obj5.is_valid_date('50-24-21'))

# можно, но не нужно
date_obj4 = date_obj2.from_string('20-05-1994')
print(date_obj4)