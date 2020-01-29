import unittest
import tictactoe


class CheckValidPlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.board = tictactoe.Board()

    def test_O_player(self):
        self.assertTrue(self.board.check_valid_player('O'))

    def test_X_player(self):
        self.assertTrue(self.board.check_valid_player('X'))

    def test_W_player(self):
        self.assertFalse(self.board.check_valid_player('W'))

    def test_integer_player(self):
        self.assertFalse(self.board.check_valid_player(2))


if __name__ == '__main__':
    unittest.main()
