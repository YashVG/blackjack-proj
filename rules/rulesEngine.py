import random

# Rule class to define game rules
class Rule:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def apply(self, game):
        if self.condition(game):
            print(f"Rule triggered: {self.name}")
            self.action(game)
            return True
        return False

# Blackjack rules management
class BlackjackRules:
    def __init__(self):
        self.rules = [
            Rule("Player Blackjack", lambda g: g.player.get_hand_value() == 21, lambda g: setattr(g, 'winner', "Player wins with Blackjack!")),
            Rule("Dealer Blackjack", lambda g: g.dealer.get_hand_value() == 21, lambda g: setattr(g, 'winner', "Dealer wins with Blackjack!")),
            Rule("Player Busts", lambda g: g.player.get_hand_value() > 21, lambda g: setattr(g, 'winner', "Player busts, Dealer wins.")),
            Rule("Dealer Busts", lambda g: g.dealer.get_hand_value() > 21, lambda g: setattr(g, 'winner', "Dealer busts, Player wins.")),
            Rule("Compare Hands", lambda g: g.player.get_hand_value() <= 21 and g.dealer.get_hand_value() <= 21, 
                 lambda g: setattr(g, 'winner', "Player wins!" if g.player.get_hand_value() > g.dealer.get_hand_value()
                                    else "Dealer wins!" if g.dealer.get_hand_value() > g.player.get_hand_value()
                                    else "It's a tie!"))
        ]

    def evaluate(self, game):
        for rule in self.rules:
            if rule.apply(game):
                return True
        return False



