from enums.suits import Suits
from enums.ranks import Ranks
from card import Card

import random

"""
    Class represents multiple decks of cards
    The number depends on the user input (default is 4)
    Each instance of the class is used to play a blackjack game
"""
class StackOfDecks:
    def __init__(self, number_of_times=4):
        """
            Instantiate array for LoC and use generate_cards function
        """
        self.cards = []
        self.generate_cards(number_of_times)
    
    def generate_cards(self, number_of_times=1):
        """
            Generate LoC based on rank and suit enum given in enums folder
            Default value = 1, unless otherwise stated by user in instantation
        """
        for i in range(1, number_of_times):
            for suit in Suits:
                for rank in Ranks:
                    self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    
    def deal(self):
        """
            Deal cards from 0th index in self.cards
        """
        if self.cards:
            return self.cards.pop()
        else:
            raise ValueError("No more cards left in deck")
            #TODO: Find method of adding another deck
    
    def __str__(self):
        return "\n".join(str(card) for card in self.cards)

