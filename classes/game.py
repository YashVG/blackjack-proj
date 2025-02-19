import random
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
        self.player.has_stood = False  # New flag
        self.dealer.has_finished = False  # New flag
        self.setup_game()

    def setup_game(self):
        for _ in range(2):  # Deal initial two cards to both player and dealer
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)

        # Print initial hands
        print(f"Player's hand: {self.player.show_hand()} (Value: {self.player.get_hand_value()})")
        print(f"Dealer's hand: {self.dealer.show_hand(hide_first_card=True)}")

        # Only evaluate if a player or dealer has Blackjack
        if self.player.get_hand_value() == 21 or self.dealer.get_hand_value() == 21:
            self.rules_engine.evaluate(self)

    def run(self):
        if self.winner:
            print("Result:", self.winner)
            return

        while self.winner is None:
            action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
            if action == 'hit':
                self.player.draw(self.deck)
                print(f"Player's hand: {self.player.show_hand()} (Value: {self.player.get_hand_value()})")

                # Check if player busts
                if self.rules_engine.evaluate(self):
                    return

            elif action == 'stand':
                print("Player stands.")
                self.player.has_stood = True
                break

        # Dealer's turn (only if the player hasn't already won/lost)
        if self.winner is None:
            print(f"Dealer's hand revealed: {self.dealer.show_hand()} (Value: {self.dealer.get_hand_value()})")
            self.dealer.play(self.deck)
            self.dealer.has_finished = True

            # Final evaluation after dealer plays
            self.rules_engine.evaluate(self)

        # Display result
        print(f"Final Player's hand: {self.player.show_hand()} (Value: {self.player.get_hand_value()})")
        print(f"Final Dealer's hand: {self.dealer.show_hand()} (Value: {self.dealer.get_hand_value()})")
        print("Result:", self.winner)

