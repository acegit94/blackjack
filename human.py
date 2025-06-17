from hand import Hand
from card import Card

class Human:

    def __init__(self, name: str, amount: float):
        self.__human_hand = Hand()
        self.__name = name
        self.__score: int = 0
        self.__amount: float = amount

    def bet(self, bet_amount: float) -> bool:
        if 0 < bet_amount <= self.__amount:
            self.__amount -= bet_amount
            return True
        return False

    def get_amount(self):
        return self.__amount

    def add_winnings(self, winning: float):
        self.__amount += winning

    def hit(self, card: Card):
        self.__human_hand.add_card(card)
        self.__score += card.getValue()

    def score(self) -> int:
        return self.__score

    def found_ace(self):
        self.__score -= 10

    def show_hand(self):
        for card in self.__human_hand.get_hand():
            print(card, end = ",")

