import random

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
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        return f"{self.value}{SUITS_UNI[self.suit]}"

    def __str__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __repr__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        return False
        pass

    def equal_value(self, other_card):
        return self.value == other_card.value

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

    pass


class Deck:
    def __init__(self):
        self.idx = None
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return f"deck[{len(self.cards)}]: {','.join(str(card) for card in self.cards)}"

    def draw(self, need_cards):
        # Принцип работы данного метода прописан в 00_task_deck.md
        out_cards = self.cards[:need_cards]
        self.cards = self.cards[need_cards:]
        return out_cards

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return f"deck[{len(self.cards)}]: {','.join(str(cur_card) for cur_card in self.cards)}"

    def __iter__(self):
        self.idx = -1
        return self

    def __next__(self):
        self.idx += 1
        if self.idx < len(self):
            return self.cards[self.idx]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.cards[index]

    def __len__(self):
        return len(self.cards)

'''
создадим имитацию ходов в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 10 карт
3. Второй игрок берет сверху 10 карт.
4. Игрок-1 ходит:
    4.1. игрок-1 выкладывает самую маленькую карту по значению
    4.2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
    4.3. Если игрок-2 не может побить карту, то он проигрывает/забирает себе(см. пункт 7)
    4.4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Если Игрок-2 отбился, то Игрок-1 и Игрок-2 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.    
6. Выведите в консоль максимально наглядную визуализацию данных ходов.
7* Реализовать возможность добрать карты из колоды после того, как один из игроков отбился/взял в руку
'''

deck = Deck()
deck.shuffle()
player1 = deck.draw(10)
player2 = deck.draw(10)
table = []
move = 1

print("=" * 28 + 'Game Start' + "=" * 28)
print(f"Scorpion - {player1}")
print(f"Sub-Zero - {player2}")
print(f'Карт в колоде - {len(deck)}')

while player1 != [] or player1 != []:
    if move % 2 != 0:
        if player1 == [] or player2 == []:
            break
        else:
            scorpion_move = move
            print("=" * 26, "Ход Scorpion", "=" * 26)
            table.append(min(player1))
            move_player1 = min(player1)
            player1.remove(min(player1))
            print('Первый ход - ', table[0])
            for item in sorted(player2):
                if item.equal_suit(move_player1) and item > move_player1:
                    table.append(item)
                    answer_player2 = item
                    print(*table, sep='<--')
                    player2.remove(item)
                    move += 1
                    break
                if max(player2) < move_player1:
                    player2.extend(table)
                    print('Sub-Zero не смог отбиться')
                    break
            for item in player1:
                if item.equal_value(move_player1) or item.equal_value(answer_player2):
                    table.append(item)
                    print('Scorpion подкидывает', item)
                    new_challenger1 = item
                    player1.remove(item)
                    for card in sorted(player2):
                        if card.equal_suit(new_challenger1) and card > new_challenger1:
                            table.append(card)
                            answer_player2 = card
                            print(new_challenger1, '<--', card)
                            player2.remove(card)
                            break
                        if max(player2) < new_challenger1:
                            player2.extend(table)
                            print('Sub-Zero не смог отбиться')
                            move -= 1
                            break
            move_player1 = Card(0, 0)
            answer_player2 = Card(0, 0)
            table.clear()
            if move == scorpion_move:
                player1.extend(deck.draw(1))
            else:
                player1.extend(deck.draw(1))
                player2.extend(deck.draw(1))
            print(f"Конец хода")
            print(f"Scorpion - {player1}")
            print(f"Sub-Zero - {player2}")
            print(f'Карт в колоде - {len(deck)}')
    if move % 2 == 0:
        if player1 == [] or player2 == []:
            break
        else:
            subzero_move = move
            print("=" * 26, "Ход Sub-Zero", "=" * 26)
            table.append(min(player2))
            move_player2 = min(player2)
            player2.remove(min(player2))
            print('Первый ход - ', table[0])
            for item in sorted(player1):
                if item.equal_suit(move_player2) and item > move_player2:
                    table.append(item)
                    answer_player1 = item
                    print(*table, sep='<--')
                    player1.remove(item)
                    move += 1
                    break
                if max(player1) < move_player2:
                    player1.extend(table)
                    print('Scorpion не смог отбиться')
                    break

            for item in player2:
                if item.equal_value(move_player2) or item.equal_value(answer_player1):
                    table.append(item)
                    print('Sub-Zero подкидывает', item)
                    new_challenger2 = item
                    player2.remove(item)
                    for card in sorted(player1):
                        if card.equal_suit(new_challenger2) and card > new_challenger2:
                            table.append(card)
                            answer_player1 = card
                            print(new_challenger2, '<--', card)
                            player1.remove(card)
                            break
                        if max(player1) < new_challenger2:
                            player1.extend(table)
                            print('Scorpion не смог отбиться')
                            move -= 1
                            break
            move_player2 = Card(0, 0)
            answer_player1 = Card(0, 0)
            table.clear()
            if move == subzero_move:
                player2.extend(deck.draw(1))
            else:
                player1.extend(deck.draw(1))
                player2.extend(deck.draw(1))
            print(f"Конец хода")
            print(f"Scorpion - {player1}")
            print(f"Sub-Zero - {player2}")
            print(f'Карт в колоде - {len(deck)}')

if not player1 and player2:
    print("=" * 26, 'Scorpion Wins!', "=" * 26)
if not player2 == [] and player1:
    print("=" * 26, 'Sub-Zero Wins!', "=" * 26)
if not player1 == [] and not player2:
    print("=" * 26, 'Draw!', "=" * 26)