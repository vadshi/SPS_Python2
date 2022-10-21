import random

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
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = SUITS_UNI[suit]  # Масть карты

    def to_str(self):
        return f'{self.value}{self.suit}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.value == other_card.value:
            if self.suit == '♥':
                return True
            elif (self.suit == '♦' and (other_card.suit == '♣' or
                  other_card.suit == '♠' and other_card.suit != '♥')):
                return True
            elif self.suit == '♣' and other_card.suit == '♠':
                return True
            return False
        else:
            if self.value in VALUES[:9] and other_card.value in VALUES[:9]:
                return int(self.value) > int(other_card.value)
            else:
                if self.value == 'A':
                    return True
                elif self.value == 'K' and other_card.value != 'A':
                    return True
                elif self.value == 'Q' and other_card.value != 'A' and other_card.value != 'K':
                    return True
                elif self.value == 'J' and other_card.value != 'A' and other_card.value != 'K' and other_card.value != 'Q':
                    return True
                return False

    def less(self, other_card):
        if self.value == other_card.value:
            if self.suit == '♥':
                return False
            elif self.suit == '♦' and other_card.suit == '♣' or other_card.suit == '♠' and other_card.suit != '♥':
                return False
            elif self.suit == '♣' and other_card.suit == '♠':
                return False
            return True
        else:
            if self.value in VALUES[:9] and other_card.value in VALUES[:9]:
                return int(self.value) < int(other_card.value)
            else:
                if self.value == 'A':
                    return False
                elif self.value == 'K' and other_card.value != 'A':
                    return False
                elif self.value == 'Q' and other_card.value != 'A' and other_card.value != 'K':
                    return False
                elif self.value == 'J' and other_card.value != 'A' and other_card.value != 'K' and other_card.value != 'Q':
                    return False
                return True

