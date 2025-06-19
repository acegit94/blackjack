import logging
from deck import Deck
from hand import Hand
from chips import Chips

###Loger configurations###
logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("game.log"), logging.StreamHandler()]
)

logger = logging.getLogger(__name__)


###Object instances###
human_deck = Deck()
human_hand = Hand()
human_chips = Chips()

computer_deck = Deck()
computer_hand = Hand()




def take_bet():
    while True:
        try:
            bet_amount = int(input(f"Please enter your bet amount (Available: {human_chips.total}) "))
            if bet_amount <= human_chips.total:
                human_chips.total -= bet_amount
            else:
                print(f"Invalid bet. You have {human_chips.total} chips")
                continue
            return bet_amount
        except ValueError as error:
            logger.error(error)
            print("Invalid input! Please enter a number")

def hit(deck: Deck, hand: Hand):
    card = deck.deal()
    hand.add_card(card)

def hit_or_stay() -> str:
    while True:
        player_choice = input("Would you like to hit or stay\n")
        if player_choice.lower() == "hit":
            return "hit"
        elif player_choice.lower() == "stay":
            return "stay"
        else:
            print("Please enter valid input")


def check_player_score() -> bool:
    if human_hand.get_score() > 21:
        return False
    return True

def game_logic():

    player_turn:bool = True
    bet_amount:int = take_bet()

    while player_turn:
        if hit_or_stay() == "hit":
            hit(human_deck, human_hand)

        else:
            player_turn = False
