from deck import Deck
from human import Human
from computer import Computer

deck = Deck()
deck.create_deck()

human = Human("Anshul", 5000.00)
human.hit(deck.deal())
human.hit(deck.deal())
human.show_hand()
print()


def validate_bet(bet_amount: str):
    if not bet_amount.isdigit():
        while not bet_amount.isdigit():
            bet_amount = input("Please enter a valid amount \n")
    while not human.bet(float(bet_amount)):
        print(f"Remaining amount {human.get_amount()}")
        bet_amount = input("Please enter different amount \n")

    print(human.get_amount())



def game_logic():
    playing = True
    human_turn = True
    validate_bet(input("Please enter bet amount \n"))


game_logic()

