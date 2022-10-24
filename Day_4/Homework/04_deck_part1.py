import random

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'}

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

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


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return ", ".join(str(card) for card in self.cards)

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        num_cards = len(self.cards)
        if x <= 0:
            print("Невозможно вытянуть 0 и менее карт")
        elif x > num_cards:
            print(f"В колоде {num_cards} карт, невозможно вытянуть больше")
        else:
            return [self.cards.pop(0) for _ in range(x)]

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(*hand, sep=', ')
