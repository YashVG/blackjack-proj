from classes.game import BlackjackGame


def read_deck_count():
    while True:
        try:
            count = int(input("Enter number of decks to use (1-8): "))
        except ValueError:
            print("Please enter a whole number from 1 to 8.")
            continue
        if 1 <= count <= 8:
            return count
        print("Please enter a whole number from 1 to 8.")


def main():
    try:
        game = BlackjackGame(read_deck_count())
        game.run()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
