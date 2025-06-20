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

def take_bet(player_chips: Chips) -> int:
    """Ask user to place bet
    Validate user input
    Check if user has a balance greater than amount inserted
    Return bet amount"""
    while True:
        try:
            bet_amount = int(input(f"Please enter your bet amount (Available: {player_chips.total})\n"))
            if 0 < bet_amount <= player_chips.total:
                player_chips.total -= bet_amount
            else:
                print(f"Invalid bet. You have {player_chips.total} chips")
                continue
            return bet_amount
        except ValueError as error:
            logger.error(error)
            print("Invalid input! Please enter a number")

def hit(deck: Deck, hand: Hand):
    """Deal card from the deck
    Add card to hand"""
    card = deck.deal()
    hand.add_card(card)

def hit_or_stay() -> str:
    """Ask user if they would like to hit or stay
    Validate input
    Return string representation of user choice"""
    while True:
        player_choice = input("Would you like to hit or stay\n")
        if player_choice.lower() == "hit":
            return "hit"
        if player_choice.lower() == "stay":
            return "stay"
        print("Please enter valid input")


def check_player_score(player: Hand) -> str:
    """Check player score
    Return bust is score > 21
    otherwise return empty string"""
    if player.get_score() > 21:
        return "bust"
    return ""

def check_dealer_score(dealer: Hand) -> str:
    """Check dealer score
    Return bust if > 21
    hit < 17
    otherwise return stay"""
    if dealer.get_score() > 21:
        return "bust"
    if dealer.get_score() < 17:
        return "hit"
    return "stay"

def check_winner(player:Hand, dealer:Hand, bet_amount: int, player_chips:Chips):
    """Compare user score to dealer score and print outcome"""
    if player.get_score() > dealer.get_score():
        player_chips.win_bet(bet_amount * 2)
        print(f"Player wins! Remaining balance: {player_chips.total}")
    elif dealer.get_score() > player.get_score():
        print(f"Dealer wins! Remaining balance: {player_chips.total}")
    else:
        print("Its a draw")
        print(f"Player score: {player.get_score()}, Dealer score: {dealer.get_score()}")
        player_chips.win_bet(bet_amount)
        print(f"Player balance: {player_chips.total}")

def continue_playing(player_chips: Chips) -> bool:
    """Validate user input for continue playing answer
    Return True if yes, False if not enough balance
    False if no"""
    while True:
        player_choice = input("Would you like to continue playing\n")
        print("\n")
        if player_choice.lower() == "yes":
            if player_chips.total == 0:
                print(f"Sorry! Not enough balance. Remaining chips: {player_chips.total}")
                return False
            return True
        if player_choice.lower() == "no":
            return False

        print("Please enter yes or no")

def print_details(first_round: bool, player_hand:Hand, dealer_hand:Hand):
    print("\n")
    print("-------Player turn-------")
    player_hand.print_hand()
    print(f"Score: {player_hand.get_score()}")
    print("-------Dealer's turn-------")
    if first_round:
        dealer_hand.show_one_card()
    else:
        dealer_hand.print_hand()
        print(f"Score: {dealer_hand.get_score()}")

    print("\n")


def game_logic():
    """Logic on game working"""
    game_is_on = True
    player_chips = Chips()

    while game_is_on:
        ###Object instances###
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        player_turn: bool = True
        bet_amount: int = take_bet(player_chips)
        dealer_turn: bool = True

        hit(deck, player_hand)
        hit(deck, player_hand)
        hit(deck, dealer_hand)
        hit(deck, dealer_hand)


        print_details(True, player_hand, dealer_hand)

        while player_turn:
            if hit_or_stay() == "hit":
                hit(deck, player_hand)
                print_details(False, player_hand, dealer_hand)
                if check_player_score(player_hand) == "bust":
                    player_turn = False
                    print(f"Dealer wins! Remaining balance: {player_chips.total} \n")
                    dealer_turn = False
            else:
                player_turn = False



        while dealer_turn:
            hit(deck, dealer_hand)
            print_details(False, player_hand, dealer_hand)
            dealer_score = check_dealer_score(dealer_hand)
            if dealer_score == "bust":
                dealer_turn = False
                player_chips.win_bet(bet_amount * 2)
                print(f"Player wins! Remaining balance: {player_chips.total} \n")
            elif dealer_score == "stay":
                dealer_turn = False
                check_winner(player_hand, dealer_hand, bet_amount, player_chips)


        game_is_on = continue_playing(player_chips)

game_logic()
