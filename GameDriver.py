
from Board import Board


class GameDriver(object):

    def __init__(self):
        self.board = Board()
        pass

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """

        self.board.print()
        while not self.board.has_winner() and not self.board.check_full_board():
            user_entered_data = input("Enter in a move in the form (column, row, player)")
            user_entered_data = user_entered_data.replace(' ', '')
            column, row, player = user_entered_data.split(',')

            # Can break if column or row is not int
            column = int(column)
            row = int(row)

            self.board.mark_square(column, row, player)
            self.board.print()


        return self.board.has_winner()
        pass