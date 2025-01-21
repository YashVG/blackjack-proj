import random

# Define card values (Ace can be 1 or 11)
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]
}

# Define the Rule class
class Rule:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def apply(self, game_state):
        if self.condition(game_state):
            print(f"Rule triggered: {self.name}")
            self.action(game_state)
            return True
        return False

# Blackjack utility functions
def calculate_hand_value(hand):
    """Calculate the best possible value of a Blackjack hand."""
    value = 0
    ace_count = 0
    
    for card in hand:
        if card == 'A':
            ace_count += 1
            value += 11  # Consider Ace as 11 first
        else:
            value += CARD_VALUES[card]
    
    # Adjust for Aces if total exceeds 21
    while value > 21 and ace_count > 0:
        value -= 10  # Convert an Ace from 11 to 1
        ace_count -= 1

    return value

# Game conditions
def player_blackjack(game_state):
    return calculate_hand_value(game_state['player_hand']) == 21

def dealer_blackjack(game_state):
    return calculate_hand_value(game_state['dealer_hand']) == 21

def player_busts(game_state):
    return calculate_hand_value(game_state['player_hand']) > 21

def dealer_busts(game_state):
    return calculate_hand_value(game_state['dealer_hand']) > 21

def dealer_must_hit(game_state):
    return calculate_hand_value(game_state['dealer_hand']) < 17

def compare_hands(game_state):
    player_total = calculate_hand_value(game_state['player_hand'])
    dealer_total = calculate_hand_value(game_state['dealer_hand'])
    return player_total <= 21 and dealer_total <= 21

# Actions
def declare_player_blackjack(game_state):
    game_state['winner'] = 'Player wins with Blackjack!'

def declare_dealer_blackjack(game_state):
    game_state['winner'] = 'Dealer wins with Blackjack!'

def declare_player_busted(game_state):
    game_state['winner'] = 'Player busts, Dealer wins.'

def declare_dealer_busted(game_state):
    game_state['winner'] = 'Dealer busts, Player wins.'

def dealer_hits(game_state):
    card = game_state['deck'].pop()
    game_state['dealer_hand'].append(card)
    print(f"Dealer hits and draws: {card}")

def determine_winner(game_state):
    player_total = calculate_hand_value(game_state['player_hand'])
    dealer_total = calculate_hand_value(game_state['dealer_hand'])
    
    if player_total > dealer_total:
        game_state['winner'] = 'Player wins!'
    elif dealer_total > player_total:
        game_state['winner'] = 'Dealer wins!'
    else:
        game_state['winner'] = 'It\'s a tie!'

# Rules Engine
class BlackjackEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def run(self, game_state):
        for rule in self.rules:
            if rule.apply(game_state):
                break  # Stop once a rule is triggered

# Game setup
def deal_initial_cards(deck):
    return [deck.pop(), deck.pop()]

def play_blackjack():
    # Create a deck of cards and shuffle
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    # Initial game state
    game_state = {
        'player_hand': deal_initial_cards(deck),
        'dealer_hand': deal_initial_cards(deck),
        'deck': deck,
        'winner': None
    }

    print(f"Player's hand: {game_state['player_hand']} (Value: {calculate_hand_value(game_state['player_hand'])})")
    print(f"Dealer's hand: {game_state['dealer_hand'][0]}, ?")

    # Instantiate the rules engine
    engine = BlackjackEngine()

    # Add rules to the engine
    engine.add_rule(Rule("Player Blackjack", player_blackjack, declare_player_blackjack))
    engine.add_rule(Rule("Dealer Blackjack", dealer_blackjack, declare_dealer_blackjack))
    engine.add_rule(Rule("Player Busts", player_busts, declare_player_busted))
    engine.add_rule(Rule("Dealer Busts", dealer_busts, declare_dealer_busted))
    engine.add_rule(Rule("Dealer Hits", dealer_must_hit, dealer_hits))
    engine.add_rule(Rule("Compare Hands", compare_hands, determine_winner))

    # Run the rules engine until we get a result
    while game_state['winner'] is None:
        action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        if action == 'hit':
            card = game_state['deck'].pop()
            game_state['player_hand'].append(card)
            print(f"Player draws: {card}")
            print(f"Player's hand: {game_state['player_hand']} (Value: {calculate_hand_value(game_state['player_hand'])})")
        elif action == 'stand':
            print("Player stands.")
            break

        # Check rules after player's action
        engine.run(game_state)

    # Dealer's turn (if no winner yet)
    if game_state['winner'] is None:
        print(f"Dealer's full hand: {game_state['dealer_hand']} (Value: {calculate_hand_value(game_state['dealer_hand'])})")
        while calculate_hand_value(game_state['dealer_hand']) < 17:
            engine.run(game_state)

    # Final decision
    if game_state['winner'] is None:
        engine.run(game_state)

    # Show results
    print(f"Final Player's hand: {game_state['player_hand']} (Value: {calculate_hand_value(game_state['player_hand'])})")
    print(f"Final Dealer's hand: {game_state['dealer_hand']} (Value: {calculate_hand_value(game_state['dealer_hand'])})")
    print("Result:", game_state['winner'])

if __name__ == "__main__":
    play_blackjack()