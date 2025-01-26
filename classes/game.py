# Main game class with deck selection
from classes.deck import Deck
from classes.dealer import Dealer
from classes.player import Player
from rules.rulesEngine import BlackjackRules


class BlackjackGame:
    def __init__(self, num_decks=1):
        self.deck = Deck(num_decks)
        self.player = Player("Player")
        self.dealer = Dealer()
        self.winner = None
        self.rules_engine = BlackjackRules()
        self.setup_game()

    def setup_game(self):
        for _ in range(2):  # Deal initial two cards to both player and dealer
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)

    def run(self):
        print(f"Player's hand: {self.player.show_hand()} (Value: {self.player.get_hand_value()})")
        print(f"Dealer's hand: {self.dealer.show_hand(hide_first_card=True)}")

        while self.winner is None:
            action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
            if action == 'hit':
                self.player.draw(self.deck)
                print(f"Player's hand: {self.player.show_hand()} (Value: {self.player.get_hand_value()})")
            elif action == 'stand':
                print("Player stands.")
                break

            if self.rules_engine.evaluate(self):
                return

        # Dealer's turn
        print(f"Dealer's hand revealed: {self.dealer.show_hand()} (Value: {self.dealer.get_hand_value()})")
        self.dealer.play(self.deck)

        # Evaluate final result
        self.rules_engine.evaluate(self)

        # Display result
        print(f"Final Player's hand: {self.player.show_hand()} (Value: {self.player.get_hand_value()})")
        print(f"Final Dealer's hand: {self.dealer.show_hand()} (Value: {self.dealer.get_hand_value()})")
        print("Result:", self.winner)