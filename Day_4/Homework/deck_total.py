import random

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'}
PLAYERS = []

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
    def __init__(self, cards=None, main=False):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        if not cards:
            self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]
        else:
            self.cards = cards

        self.main = main

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

    def __repr__(self):
        return ", ".join(str(card) for card in self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __len__(self):
        return len(self.cards)

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return ", ".join(str(card) for card in self.cards)

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        num_cards = len(self.cards)
        if x <= 0:
            print("Невозможно вытянуть 0 и менее карт")
        elif x > num_cards:
            print(f"В колоде {num_cards} карт, они будут вытянуты все, невозможно вытянуть больше")
            return [self.cards.pop(0) for _ in range(num_cards)]
        else:
            return [self.cards.pop(0) for _ in range(x)]

    def pop(self, card):
        return self.cards.pop(self.cards.index(card))

    def shuffle(self):
        random.shuffle(self.cards)

    def __add__(self, other_deck):
        assert not self.main, f'Нельзя добавить в главную колоду'
        if isinstance(other_deck, Deck):
            self.cards += other_deck.cards
        elif isinstance(other_deck, list):
            self.cards += other_deck
        return self

class Player:
    def __init__(self, number: int, cards: Deck = Deck([])):
        assert number not in PLAYERS, f'Игрок {number} уже создан'
        self.number = number
        self.cards = cards

    def __str__(self):
        return f'Игрок {self.number}, список карт в руках:\n{self.cards}'

    def __repr__(self):
        return f'Игрок {self.number}, список карт в руках:\n{self.cards}'

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other_player):
        return len(self) == len(other_player)

    def __ne__(self, other_player):
        return self != other_player

    def __gt__(self, other_player):
        return len(self) > len(other_player)

    def __ge__(self, other_player):
        return len(self) >= len(other_player)

    def __lt__(self, other_player):
        return len(self) < len(other_player)

    def __le__(self, other_player):
        return len(self) <= len(other_player)

    def take_from_main_deck(self, main_deck: Deck, num=10):
        self.cards += main_deck.draw(num)

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 1
        self.attack_player = self.player1
        self.defense_player = self.player2

    def __str__(self):
        return f'Игра между {self.player1.number} и {self.player2.number}'

    def __repr__(self):
        return f'Игра между {self.player1.number} и {self.player2.number}'

    def status(self):
        return f'Идет {self.round} раунд\n{self.player1}\n{self.player2}\n'

    def play_round(self):
        print('\n')
        print(f'Раунд {self.round}')
        cards_on_table = []
        starts_to_attack = self.attack_player.number
        print(f'Атакует игрок {self.attack_player.number}')
        print('Карты игроков в начале раунда:')
        print(self.player1)
        print(self.player2)

        if (len(self.attack_player) == 0 and len(self.defense_player) == 0):
            print('Ничья')

        if len(self.attack_player) == 0:
            print(f'Победил игрок {self.attack_player.number}')
        if len(self.defense_player) == 0:
            print(f'Победил игрок {self.defense_player.number}')

        while True:
            #Атака
            if not cards_on_table:
                if len(self.attack_player.cards) == 0:
                    return None
                attack_card = self.attack_player.cards.pop(min(self.attack_player.cards))
            else:
                attack_card = None
                values_to_throw = set([card.value for card in cards_on_table])
                for card in self.attack_player.cards:
                    if card.value in values_to_throw:
                        attack_card = self.attack_player.cards.pop(card)
                        break
                if not attack_card:
                    print(f'Игрок {self.defense_player.number} отбился')
                    self.attack_player, self.defense_player = self.defense_player, self.attack_player
                    break

            cards_on_table.append(attack_card)
            print(f'Игрок {self.attack_player.number} положил карту {attack_card}')

            #Защита
            defense_card = None
            for card in self.defense_player.cards:
                if card.suit == attack_card.suit and card.value > attack_card.value:
                    defense_card = self.defense_player.cards.pop(card)
                    print(f'Игрок {self.defense_player.number} отбил карту {attack_card} картой {defense_card}')
                    cards_on_table.append(defense_card)
                    break
            if not defense_card:
                print(f'Игрок {self.defense_player.number} не смог отбиться и забирает {len(cards_on_table)} карт на столе')
                self.defense_player.cards += cards_on_table
                break

        print(f'Атаковал игрок {starts_to_attack}, в следующем раунде атакует игрок {self.attack_player.number}')
        print('Карты игроков в конце раунда:')
        print(self.player1)
        print(self.player2)

        self.round += 1

    def take_from_main_deck(self, main_deck: Deck, num_in_player_deck=10):
        if main_deck:
            cards_to_take1 = max(0, num_in_player_deck - len(self.attack_player))
            possible_cards_to_take = len(main_deck)
            print(f'В главной колоде осталось {possible_cards_to_take} карт')
            cards_taken1 = min(cards_to_take1, possible_cards_to_take)
            self.attack_player.cards += main_deck.draw(cards_taken1)

            if not main_deck:
                print(f'Взято {cards_taken1} карт, карт в главной колоде больше нет')
            else:
                print(f'Игрок {self.attack_player.number} взял {cards_taken1} карт, в главной колоде осталось {len(main_deck)} карт')
                cards_to_take2 = max(0, num_in_player_deck - len(self.defense_player))
                possible_cards_to_take = len(main_deck)
                cards_taken2 = min(cards_to_take2, possible_cards_to_take)
                self.attack_player.cards += main_deck.draw(cards_taken2)

                if not main_deck:
                    print(f'Взято {cards_taken2} карт, карт в главной колоде больше нет')
                else:
                    print(
                        f'Игрок {self.defense_player.number} взял {cards_taken2} карт, в главной колоде осталось {len(main_deck)} карт')










