import contextlib
import io
import unittest
from unittest.mock import patch

from main import main, read_deck_count


class StartupTests(unittest.TestCase):
    def test_invalid_input_reprompts_before_constructing_a_shoe(self):
        with patch("builtins.input", side_effect=["", "many", "1.5", "0", "-2", "9", "2"]):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(read_deck_count(), 2)
        self.assertEqual(output.getvalue().count("Please enter"), 6)

    def test_supported_boundaries(self):
        for count in [1, 8]:
            with self.subTest(count=count), patch("builtins.input", return_value=str(count)):
                self.assertEqual(read_deck_count(), count)

    def test_closed_input_and_interrupt_exit_without_starting_game(self):
        for error in [EOFError, KeyboardInterrupt]:
            with self.subTest(error=error), patch("builtins.input", side_effect=error):
                with patch("main.BlackjackGame") as game, contextlib.redirect_stdout(io.StringIO()) as output:
                    main()
                game.assert_not_called()
                self.assertIn("Goodbye!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
