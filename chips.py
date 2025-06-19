class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self, amount_won):
        self.total += amount_won

    def lost_bet(self, amount_lost):
        self.total -= amount_lost