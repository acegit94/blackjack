import random
from card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Deck:
    def __init__(self):
        self.__deck_of_cards = []
        for suit in suits:
            for rank in values:
                card = Card(suit, values[rank], rank)
                self.__deck_of_cards.append(card)


    def shuffle(self):
        random.shuffle(self.__deck_of_cards)

    def deal(self) -> Card:
        card = random.choice(self.__deck_of_cards)
        self.__deck_of_cards.remove(card)
        return card

    def print_deck(self):
        for card in self.__deck_of_cards:
            print(card)