from card import Card
class Hand:

    def __init__(self):
        self.__hand_of_cards: list = []
        self.__score = 0
        self.__aces = 0

    def add_card(self, card: Card):
        self.__score += card.get_value()
        self.__hand_of_cards.append(card)
        if card.get_rank().lower() == "ace":
            if self.__score  > 21:
                self.adjust_aces(card)

    def adjust_aces(self, card):
        card.set_ace_value()
        self.__aces += 1
        self.__score -= 10

    def get_score(self):
        return self.__score

    def print_hand(self):
        for index, card in enumerate(self.__hand_of_cards):
            if index < len(self.__hand_of_cards)-1:
                print(card, end =" , ")
            else:
                print(card)

    def show_one_card(self):
        print(self.__hand_of_cards[0])
