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

    def to_str(self):
        return str(self)

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if VALUES.index(self.value) == VALUES.index(other_card.value):
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card):
        return not self > other_card

    def more(self, other_card):
        return self > other_card

    def less(self, other_card):
        return not self.more(other_card)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

    def __repr__(self):
        return ", ".join(str(card) for card in self.cards)

    def __getitem__(self, index):
        return self.cards[index]

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


deck = Deck()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")

# Это на следующее занятие.
#4. Итерация по колоде:
for card in deck:
    print(card)

# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])


# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
