import unittest
import tictactoe


class CheckValidRowColumnTests(unittest.TestCase):
    def setUp(self) -> None:
        self.board = tictactoe.Board()

    def test_row_0_column_0(self):
        self.assertTrue(self.board.check_valid_row_column(0, 0))

    def test_row_2_column_2(self):
        self.assertTrue(self.board.check_valid_row_column(2, 2))

    def test_row_3_column_3(self):
        self.assertFalse(self.board.check_valid_row_column(3, 3))

    def test_negative_row(self):
        self.assertFalse(self.board.check_valid_row_column(-1, 0))

    def test_negative_column(self):
        self.assertFalse(self.board.check_valid_row_column(0, -1))


if __name__ == '__main__':
    unittest.main()
