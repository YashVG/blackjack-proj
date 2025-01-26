from enums.suits import Suits
from enums.ranks import Ranks
from classes.card import Card

import random

"""
    Class represents multiple decks of cards
    The number depends on the user input (default is 4)
    Each instance of the class is used to play a blackjack game
"""
class Deck:
    def __init__(self, num_decks=3):
        self.num_decks = num_decks
        self.cards = self._create_deck()
        self.shuffle()

    def _create_deck(self):
        """Creates a deck with multiple sets of 52 cards."""
        single_deck = [Card(rank, suit) for suit in Suits for rank in Ranks]
        return single_deck * self.num_decks

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draws a card from the deck, reshuffling if empty."""
        if len(self.cards) == 0:
            print("Deck is empty. Reshuffling...")
            self.cards = self._create_deck()
            self.shuffle()
        return self.cards.pop()
