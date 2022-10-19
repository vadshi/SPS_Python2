"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...
  
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезает бензина (capacity)
* "расход топлива на 100 км" (gas_per_100km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведет сообщение "проехали ... километров",
в результате поездки потратится бензин и увеличится пробег.
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (количество бензина в баке и пробег)
"""

class Car:
    def __init__(self, gas, capacity, gas_per_100km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, volume):
        free_space = self.capacity - self.gas
        if volume > free_space:
            self.gas = self.capacity
            extra_volume = volume - free_space
            print('Бак заполнен полностью. Лишних литров: {}'.format(extra_volume))
        else:
            self.gas += volume

    def ride(self, distance):
        possible_distance = self.gas * 100 / self.gas_per_100km
        if distance > possible_distance:
            self.gas = 0
            self.mileage += possible_distance
            print('Не хватает топлива. Проехали километров: {}'.format(possible_distance))
        else:
            self.gas -= distance * self.gas_per_100km / 100
            self.mileage += distance
            print('Проехали километров: {}'.format(distance))

    def info(self):
        print('Количество бензина в баке, литров: {}'.format(self.gas))
        print('Пробег, километров: {}'.format(self.mileage))


""" Test
car1 = Car(30, 60, 8, 20000)
car1.info()
car1.fill(5)
car1.fill(50)
car1.ride(200)
car1.ride(500)
car1.ride(200)
car1.info()
car1.fill(60)
car1.info()
"""
