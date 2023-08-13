import unittest
from a1 import process_move, Move, TicTacToe


class TestProcessMove(unittest.TestCase):
    def test_valid_move(self):
        # Test a valid move
        move_str = "1 2 3"
        expected_move = (0, 1, 3)
        self.assertEqual(process_move(move_str), expected_move)

    def test_invalid_move_format(self):
        # Test an invalid move format
        move_str = "1 2"
        self.assertIsNone(process_move(move_str))

    def test_invalid_row(self):
        # Test an invalid row
        move_str = "4 2 3"
        self.assertIsNone(process_move(move_str))

    def test_invalid_column(self):
        # Test an invalid column
        move_str = "1 3 3"
        self.assertIsNone(process_move(move_str))

    def test_invalid_move_format_with_letters(self):
        # Test an invalid move format with letters
        move_str = "1 a 3"
        self.assertIsNone(process_move(move_str))

    def test_valid_move_with_1_indexed_values(self):
        # Test a valid move with 1-indexed values
        move_str = "2 3 2"
        expected_move = (1, 2, 2)
        self.assertEqual(process_move(move_str), expected_move)

    def test_valid_move_with_0_indexed_values(self):
        # Test a valid move with 0-indexed values
        move_str = "0 1 1"
        expected_move = (0, 1, 1)
        self.assertEqual(process_move(move_str), expected_move)


class TestTicTacToe(unittest.TestCase):
    def test_gameplay(self):
        # Test a full game
        game = TicTacToe()
        moves = [
            "1 1 3",
            "1 2 2",
            "2 2 3",
            "1 3 1",
            "3 3 2",
            "2 1 1",
            "3 1 3",
            "2 3 2",
            "3 2 1",
        ]
        expected_output = [
            " | | ",
            "-----",
            " | | ",
            "-----",
            " | | ",
            "",
            " | | ",
            "-----",
            " |X| ",
            "-----",
            " | | ",
            "",
            " | |O",
            "-----",
            " |X| ",
            "-----",
            " | | ",
            "",
            " | |O",
            "-----",
            " |X|X",
            "-----",
            " | | ",
            "",
            " | |O",
            "-----",
            " |X|X",
            "-----",
            " | |O",
            "",
            " | |O",
            "-----",
            " |X|X",
            "-----",
            " |X|O",
            "",
            " | |O",
            "-----",
            " |X|X",
            "-----",
            "O|X|O",
            "",
            " | |O",
            "-----",
            "X|X| ",
            "-----",
            "O|X|O",
            "",
            " |O|O",
            "-----",
            "X|X| ",
            "-----",
            "O|X|O",
            "",
            "X|O|O",
            "-----",
            "X|X| ",
            "-----",
            "O|X|O",
        ]
        for i, move in enumerate(moves):
            game.make_move(move)
            self.assertEqual(str(game), "\n".join(expected_output[: i * 6 + 6]))


if __name__ == "__main__":
    unittest.main()
