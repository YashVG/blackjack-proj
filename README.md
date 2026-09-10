# Blackjack

A terminal blackjack game in Python. A shuffled multi-deck shoe deals to one
player and a dealer; a separate rules engine resolves blackjack, busts, and the
final hand comparison.

## Play

Requires Python 3.9+; there are no third-party dependencies.

```sh
git clone https://github.com/YashVG/blackjack-proj.git
cd blackjack-proj
python3 main.py
```

Choose 1–8 decks, then enter `hit` or `stand`. The dealer completes its turn and
the terminal prints the result. Invalid deck input is re-prompted; Ctrl-C exits.

## Code and checks

- `classes/`: cards, deck, hands, participants, and the game loop.
- `rules/rulesEngine.py`: outcome rules.
- `enums/`: card ranks and suits.

```sh
python3 -m unittest discover -s tests
```

This is a single-round object-oriented learning project. Betting, cash balances,
splitting, doubling down, and a graphical interface are not implemented. The
tests cover startup input handling, not every blackjack rule.
