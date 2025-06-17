from card import Card
class Hand:

    def __init__(self):
        self.__hand_of_cards: list = []

    def add_card(self, new_card: Card):
        self.__hand_of_cards.append(new_card)

    def switch_ace(self):


    def get_hand(self):
        return self.__hand_of_cards.copy()