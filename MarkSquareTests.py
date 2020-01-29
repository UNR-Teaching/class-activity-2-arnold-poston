import unittest
import tictactoe


class MarkSquareTests(unittest.TestCase):

    def setUp(self) -> None:
        self.emptyTicTacToe = tictactoe.Board()
        self.almostFilledTicTacToe = tictactoe.Board()
        self.almostFilledTicTacToe.board = [['X', 'O', 'X'],
                                            ['X', '_', 'O'],
                                            ['O', 'X', 'O']]

    def test_valid_row_0_column_0(self):
        self.assertTrue(self.emptyTicTacToe.mark_square(0, 0, 'X'))

    def test_invalid_row_0_column_0(self):
        self.assertFalse(self.almostFilledTicTacToe.mark_square(0, 0, 'X'))

    def test_board_change_valid_row_0_column_0(self):
        self.emptyTicTacToe.mark_square(0, 0, 'O')
        self.assertTrue(self.emptyTicTacToe.board[0][0] == 'O')

    def test_board_change_invalid_row_0_column_0(self):
        self.almostFilledTicTacToe.mark_square(0, 0, 'O')
        self.assertFalse(self.almostFilledTicTacToe.board[0][0] == 'O')

if __name__ == '__main__':
    unittest.main()
