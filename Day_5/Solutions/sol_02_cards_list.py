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


hearts_cards = []
# DONE-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in VALUES:
    hearts_cards.append(Card(value, 'Hearts'))

# DONE-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = [Card(value, 'Diamonds') for value in VALUES]
print(diamonds_cards)

# DONE-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(*hearts_cards, sep=', ')
print(hearts_cards)
