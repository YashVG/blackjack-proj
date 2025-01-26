from classes.game import BlackjackGame


if __name__ == "__main__":
    num_decks = int(input("Enter number of decks to use (e.g., 1, 2, 4, 6, 8): "))
    game = BlackjackGame(num_decks)
    game.run()