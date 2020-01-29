""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = ["___"] * 3

        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        if column < 0 or column > 2:
            raise Exception("Column out of bounds")

        if row < 0 or row > 2:
            raise Exception("Row out of bounds")

        if self.board[row][column] != '_':
            return False
        else:
            self.board[row][column] = player

        return True
        pass

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        for i in range(0, 2):
            if (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]):
                return True
            if(self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]):
                return True

        if(self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]):
            return True
        if(self.board[2][0] == self.board[1][1]) and (self.board[0][2] == self.board[1][1]):
            return True

        return False
        pass

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        
        pass
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))