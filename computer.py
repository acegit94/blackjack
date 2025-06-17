from hand import Hand
from card import Card


class Computer:

    def __init__(self):
        self.__computer_hand: Hand = Hand()
        self.__score: int = 0

    def hit(self, card: Card):
        self.__computer_hand.add_card(card)
        self.__score += card.getValue()

    def score(self) -> int:
        return self.__score

    def show_hand(self):
        for card in self.__computer_hand.get_hand():
            print(card)