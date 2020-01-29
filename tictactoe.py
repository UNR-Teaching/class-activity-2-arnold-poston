""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_'] * 3] * 3

        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """

        if not self.check_valid_row_column(column, row):
            return False

        if not self.check_valid_player(player):
            return False


        if self.board[row][column] != '_':
            return False

        print(row, column, player)
        print("@@@@@@@@@@@@@")
        for i in range(3):
            for j in range(3):
                print(self.board[i][j])
        print("@@@@@@@@@@@@@")
        self.board[row][column] = player
        for i in range(3):
            for j in range(3):
                print(self.board[i][j])
        print("@@@@@@@@@@@@@")
        return True
        pass

    def check_valid_row_column(self, column, row):
        if column < 0 or column > 2:
            return False
        if row < 0 or row > 2:
            return False
        return True

    def check_valid_player(self, player):
        if player == 'O' or player == 'X':
            return True
        return False

    def check_full_board(self):
        for row in self.board:
            for character in row:
                if character == '_':
                    return False
        return True

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        for i in range(0, 2):
            if (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]) \
                    and (self.board[i][0] != '_'):
                return self.board[i][0]
            if(self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]) \
                    and (self.board[0][i] != '_'):
                return self.board[0][i]

        if(self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]) \
                and (self.board[1][1] != '_'):
            return self.board[0][0]
        if(self.board[2][0] == self.board[1][1]) and (self.board[0][2] == self.board[1][1]) \
                and (self.board[1][1] != '_'):
            return self.board[2][0]

        return False
        pass


    def print(self):
        for row in self.board:
            for element in row:
                print(element, end='')
            print('')


    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        self.print()
        while not self.has_winner():
          user_entered_data = input("Enter in a move in the form (column, row, player)")
          user_entered_data = user_entered_data.replace(' ', '')
          column, row, player = user_entered_data.split(',')

          # Can break if column or row is not int
          column = int(column)
          row = int(row)

          self.mark_square(column, row, player)
          self.print()
        pass
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))