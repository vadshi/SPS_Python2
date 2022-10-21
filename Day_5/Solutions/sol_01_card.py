# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}


class Card:
    def __init__(self, value, suit):
        self.value = value   # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit     # Масть карты

    def to_str(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __str__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __repr__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if VALUES.index(self.value) == VALUES.index(other_card.value):
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __gt__(self, other_card):
        if VALUES.index(self.value) == VALUES.index(other_card.value):
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def less(self, other_card):
        if VALUES.index(self.value) == VALUES.index(other_card.value):
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)

    def __lt__(self, other_card):
        return not self > other_card


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("9", "Hearts")
card4 = Card("A", "Clubs")

# Выведем карты на экран в виде: 10♥ и A♦
# print(card1.to_str())
# print(card2.to_str())
# print(card3.to_str())
# print('=' * 40)
print(f'{card1 = !s}')
print(f'{card2 = !s}')
print(f'{card3 = !s}')
print(f'{card4 = !s}')

# Проверка явного метода .equal_suit()
# if card1.equal_suit(card2):
#     print(f"У карт: {card1} и {card2} одинаковые масти")
# else:
#     print(f"У карт: {card1} и {card2} разные масти")
#
# if card3.equal_suit(card1):
#     print(f"У карт: {card3} и {card1} одинаковые масти")
# else:
#     print(f"У карт: {card3} и {card1} разные масти")

# print(f'Test more\n {"=" * 40}')
# print(card1.more(card2))
# print(card1.more(card3))
# print(card2.more(card3))
#
# print(f'Test __gt__\n {"=" * 40}')
# print(f'{card1} > {card2}', card1 > card2)
# print(card1 > card3)
# print(card2 > card3)
# print(card4 > card3)
# print(card4 > card2)
#
# print('Test less\n {"=" * 40}')
# print(card1.less(card2))
# print(card1.less(card3))
# print(card2.less(card3))

# print(f'Test __lt__\n {"=" * 40}')
# print(card1 < card2)
# print(card1 < card3)
# print(card2 < card3)
# print(card4 < card3)
# print(card4 < card2)
