from enums.ranks import Ranks

"""
    Class represents a playing card. Consists of a rank and suit
"""
class Card:
    def __init__(self, rank, suit):
        """Initializes rank and suit of card based on input"""
        self.rank = rank
        self.suit = suit
    
    def value(self) -> int:
        """Return the numerical value of the card rank."""
        if self in {Ranks.JACK, Ranks.QUEEN, Ranks.KING}:
            return 10
        elif self == Ranks.ACE:
            return 11  
            # Default value for Ace
        else:
            return int(self.value)
    
    def __str__(self) -> str:
        """Returns string representation of the card"""
        return f"{self.rank.value} of {self.suit.value}"