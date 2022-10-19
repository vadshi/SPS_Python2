import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.randint(0, 1)  # random.choice(['heads','tails']); random.randint(0, 1)
        # return side # Это ошибка, здесь return не нужен

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

# Variant 1
# n = int(input('Введите количество монет: '))
# # Создаем список монеток
# coins = [Coin() for _ in range(n)]
#
# # Подкидываем(вызываем метод flip())
# for coin in coins:
#     coin.flip()
#
# # Подсчет соотношения
# heads = tails = 0
# for coin in coins:
#     if coin.side:
#         heads += 1
#     else:
#         tails += 1
#
# print(f'Орлы: {heads / n:.2%}, Решки: {tails / n:.2%}')

# Variant 2
n = int(input('Введите количество монет: '))
# Создаем список монеток
coins = []
for _ in range(n):
    coins.append(Coin())

# Подкидываем(вызываем метод flip()) и подсчитываем
heads = 0
for coin in coins:
    coin.flip()
    if coin.side:
        heads += 1

print(f'Орлы: {heads / n:.2%}, Решки: {(n - heads) / n:.2%}')
