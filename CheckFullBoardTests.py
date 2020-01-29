import unittest
import tictactoe

class CheckFullBoardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.emptyTicTacToe = tictactoe.Board()
        self.fullTicTacToe = tictactoe.Board()
        self.fullTicTacToe.board = [['X', 'O', 'X'],
                                    ['X', 'X', 'O'],
                                    ['O', 'X', 'O']]

    def test_empty_board(self):
        self.assertFalse(self.emptyTicTacToe.check_full_board())

    def test_full_board(self):
        self.assertTrue(self.fullTicTacToe)


if __name__ == '__main__':
    unittest.main()
