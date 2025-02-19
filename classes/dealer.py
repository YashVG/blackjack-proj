from classes.player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
        self.has_finished = False

    def play(self, deck):
        """Dealer hits until the hand value reaches 17 or higher."""
        while self.get_hand_value() < 17:
            self.draw(deck)
        print(f"Dealer's final hand: {self.show_hand()} (Value: {self.get_hand_value()})")