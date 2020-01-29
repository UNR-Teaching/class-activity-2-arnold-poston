import unittest
from tictactoe import Board


class HasWinnerTests(unittest.TestCase):
    def setUp(self):
        self.tictactoe = Board()
        self.staleMateBoard = [['X', 'O', 'X'],
                               ['O', 'X', 'O'],
                               ['O', 'X', 'O']]

        self.winnerRowBoard = [['O', 'X', 'O'],
                                 ['X', 'X', 'X'],
                                 ['O', 'X', 'X']]

        self.winnerColBoard = [['X', 'O', 'X'],
                               ['O', 'O', 'X'],
                               ['X', 'O', 'O']]


    def test_stalemate(self):
        self.tictactoe.board = self.staleMateBoard
        self.assertFalse(self.tictactoe.has_winner())

    def test_RowWinner(self):
        self.tictactoe.board = self.winnerRowBoard
        self.assertTrue(self.tictactoe.has_winner())

    def test_ColWinner(self):
        self.tictactoe.board = self.winnerColBoard
        self.assertTrue(self.tictactoe.has_winner())


if __name__ == '__main__':
    unittest.main()
