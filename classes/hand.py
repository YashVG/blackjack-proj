class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = 0
        ace_count = 0

        for card in self.cards:
            if card.rank == 'A':
                ace_count += 1
                value += 11
            else:
                value += card.value()

        while value > 21 and ace_count > 0:
            value -= 10  # Convert an Ace from 11 to 1
            ace_count -= 1

        return value

    def display(self):
        return ', '.join(str(card) for card in self.cards)

    #adding function to return length of hand for dealing purposes
    def hand_size(self):
        return len(self.cards)
