#Create terminal blackjack game
from classes.stackOfDecks import StackOfDecks


def main():
    choice = input("Do you want to play a game of blackjack? (yes/no) ")
    if choice == "yes":
        print("Let's play!")
        number_of_decks = int(input("Number of decks: "))
        stack = StackOfDecks(number_of_decks)
        
        
    else:
        print("Goodbye!")

def game():
    #TODO: Create class instances for blackjack
    ...

if __name__ == "__main__":
    main()