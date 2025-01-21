from enums.ranks import Ranks

"""
    Class represents a player in the terminal playing blackjack
    Has a score that resets after every hand, which also resets according to blackjack rules
"""
class Player:
    def __init__(self):
        """
            Initializer function to set the score and hand to initial blank state
        """
        self.score = 0
        self.hand = [] # this is an array of card elements dealt to the player
    

    def calculate_score(self):
        """
            Calculates the score of hand dealt
        """
        score = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == Ranks.ACE)
        while score > 21 and aces:
            score -= 10  # reduce Ace value from 11 to 1
            aces -= 1
        return score
    
    def add_card(self, card):
        # every time a card is added, calculate the score
        self.hand.append(card)
        self.calculate_score()
    
    def show_hand(self):
        ...
    
    def reset(self):
        self.score = 0
        self.hand = []