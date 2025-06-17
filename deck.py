import random

from card import Card


SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]
VALUES = [2,3,4,5,6,7,8,9,10,10,10,11]

class Deck:
    def __init__(self):
        self.__deck_of_cards = []

    def create_deck(self):
        for suit in SUITS:
            for value in VALUES:
                card = Card(suit, value)
                self.__deck_of_cards.append(card)

    def print_deck(self):
        for card in self.__deck_of_cards:
            print(card)

    def shuffle(self):
        random.shuffle(self.__deck_of_cards)

    def deal(self) -> Card:
        card = random.choice(self.__deck_of_cards)
        self.__deck_of_cards.remove(card)
        return card