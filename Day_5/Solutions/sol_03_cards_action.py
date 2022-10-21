"""
Создаем списки карт
"""
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

    def __str__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __repr__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if VALUES.index(self.value) == VALUES.index(other_card.value):
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card):
        return not self > other_card


cards = []
# DONE-1: в список cards добавьте ВСЕ карты всех мастей
for suit in SUITS[::-1]:
    for value in VALUES:
        cards.append(Card(value, suit))

# DONE-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
print(f'cards[{len(cards)}]: {", ".join(str(x) for x in cards)}')
print(cards[0].value, cards[0].suit)

# Создание списка с помощью генератора
cards_like_deck = [Card(value, suit) for suit in SUITS for value in VALUES]
print(*cards_like_deck)
