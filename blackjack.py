import logging

logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("game.log"), logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

from deck import Deck
from hand import Hand
from chips import Chips

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


hit(human_deck, human_hand)
hit(human_deck, human_hand)
hit(human_deck, human_hand)
human_hand.print_hand()
print(human_hand.get_score())

