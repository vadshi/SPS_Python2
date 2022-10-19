import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.choice(['heads', 'tails'])

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

def find_coin_ratio(n: int) -> tuple[float, float]:
    coins = []
    for i in range(n):
        coin = Coin()
        coin.flip()
        coins.append(coin)

    heads_count = sum([1 for coin in coins if coin.side == 'heads'])

    return heads_count / n, (n - heads_count) / n


n = int(input('Введите количество монет: '))
heads_result, tails_result = find_coin_ratio(n)

print('Процент орлов: {} %'.format(heads_result * 100))
print('Процент решек: {} %'.format(tails_result * 100))