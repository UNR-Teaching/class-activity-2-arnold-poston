import unittest
import tictactoe


class CheckFullBoardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.emptyTicTacToe = tictactoe.Board()
        self.fullTicTacToe = tictactoe.Board()
        self.fullTicTacToe.board = [['X', 'O', 'X'],
                                    ['X', 'X', 'O'],
                                    ['O', 'X', 'O']]

        self.halfEmptyTicTacToe = tictactoe.Board()
        self.halfEmptyTicTacToe.board = [['X', '_', 'O'],
                                    ['_', '_', '_'],
                                    ['O', 'X', '_']]

    def test_empty_board(self):
        self.assertFalse(self.emptyTicTacToe.check_full_board())

    def test_full_board(self):
        self.assertTrue(self.fullTicTacToe)

    def test_half_board(self):
        self.assertFalse(self.halfEmptyTicTacToe.check_full_board())


if __name__ == '__main__':
    unittest.main()
