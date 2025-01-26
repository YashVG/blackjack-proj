from classes.hand import Hand
from enums.ranks import Ranks

"""
    Class represents a player in the terminal playing blackjack
    Has a score that resets after every hand, which also resets according to blackjack rules
"""
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def draw(self, deck):
        card = deck.draw_card()
        self.hand.add_card(card)
        print(f"{self.name} draws: {card}")

    def get_hand_value(self):
        return self.hand.calculate_value()

    def show_hand(self, hide_first_card=False):
        if hide_first_card and self.name == 'Dealer':
            return f"{self.hand.cards[0]}, ?"
        return self.hand.display()