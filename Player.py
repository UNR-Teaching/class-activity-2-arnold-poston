from itertools import count


class Player(object):
    _ids = count(1)

    def __init__(self, playerCharacter):
        # The single character to represent the players move on the board
        self.playerCharacter = playerCharacter
        self.playerNumber = next(self._ids)

    def getMove(self):
        user_entered_data = input("Enter in a move in the form (column, row, player)")
        user_entered_data = user_entered_data.replace(' ', '')
        column, row, player = user_entered_data.split(',')

        # Can break if column or row is not int
        column = int(column)
        row = int(row)
        return column, row

    def check_valid_row_column(self, column, row):
        if column < 0 or column > 2:
            return False
        if row < 0 or row > 2:
            return False
        return True
