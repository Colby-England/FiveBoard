# Author: Colby England
# Date: 8/10/2020
# Description: A class that represents a 15x15 tic tac toe board. Contains methods to make a move on the board
# and check if the game has been won or is a draw.


class FiveBoard:
    """
    Represents a 15x15 tic tac toe board.
    """

    def __init__(self):
        """
        Initializes the board to be an empty 15 x 15 grid and sets game state to UNFINISHED.
        Empty cells are represented by -.
        """

        self._board = [['-' for column in range(15)] for row in range(15)]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """
        Returns the current state of the game

        :return: _current_state
        """
        return self._current_state

    def find_left_right_diagonal(self, start_row, start_column):
        """
        Given a starting grid cell, expressed by its row and column number, returns a string that is the left
        to right diagonal running through the supplied cell.

        :param int start_row:
        :param int start_column:
        :return: left_right_diagonal
        """

        # This algorithm finds the diagonal moving from the top left of the board to the bottom right of the board
        # that contains the cell defined by start_row, start_column. There are 3 cases to consider the first being
        # if the start_row > start_column, think of this as being below the 1 to 1 diagonal that runs from
        # (0,0) to (14,14). The second case is if the start_column > start_row think of this as being above the 1 to
        # 1 diagonal. The last case is the 1 to 1 diagonal itself.
        difference = abs(start_row - start_column)
        left_right_diagonal = ''
        for x in range(len(self._board) - difference):
            if start_row > start_column:
                left_right_diagonal += self._board[x + difference][x]
            elif start_column > start_row:
                left_right_diagonal += self._board[x][x + difference]
            else:
                left_right_diagonal += self._board[x][x]
        return left_right_diagonal

    def find_right_left_diagonal(self, start_row, start_column):
        """
        Given a starting grid cell, expressed by its row and column number, returns a string that is the right
        to left diagonal running through the supplied cell.

        :param int start_row:
        :param int start_column:
        :return: right_left_diagonal
        """
        sum_row_column = start_row + start_column
        right_left_diagonal = ''
        if sum_row_column <= 14:
            for x in range(sum_row_column + 1):
                right_left_diagonal += self._board[sum_row_column - x][x]
        else:
            for x in range(1, 2 * len(self._board) - sum_row_column):
                right_left_diagonal += self._board[len(self._board) - x][(
                    sum_row_column - len(self._board)) + x]
        return right_left_diagonal

    def find_row(self, start_row):
        """
        Given a row number returns a string of all elements in that row.

        :param int start_row:
        :return: row
        """
        row = ''
        for x in self._board[start_row]:
            row += x
        return row

    def find_column(self, start_column):
        """
        Given a column number, returns a string of all elements in that column.

        :param int start_column:
        :return: str column
        """
        column = ''
        for x in self._board:
            column += x[start_column]
        return column

    def _check_valid_move(self, row, column):
        """
        Given a starting grid cell, expressed by its row and column number, returns true if that cell is empty.

        :param int row:
        :param int column:
        :return:
        """
        if self._board[row][column] == "-":
            return True
        else:
            return False

    def _check_win(self, attached_lines, player):
        """
        Given a list of strings, checks if any of those strings contain a winning condition for tic tac toe.

        :param list attached_lines:
        :param str player:
        :return:
        """
        for line in attached_lines:
            if player * 5 in line:
                return True
        return False

    def _check_draw(self):
        """
        Represents every row, column and diagonal on the board as a string. Then checks all to see if any contain a
        winning condition, or a blank cell. If no blank cells or winning conditions are presents returns True.

        :return bool:
        """

        for row in self._board:
            if row in self._board:
                return False

        board_lines = []
        for x in range(15):
            board_lines += self.find_column(x)
            board_lines += self.find_row(x)
            board_lines += self.find_right_left_diagonal(0, x)
            board_lines += self.find_right_left_diagonal(14, x)
            board_lines += self.find_left_right_diagonal(x, 0)
            board_lines += self.find_left_right_diagonal(0, x)

        for line in board_lines:
            if "xxxxx" in line or "ooooo" in line:
                return False

        return True

    def make_move(self, row, column, player):
        """
        Allows a player to make a move on the board in a cell described by its row and column number. If the move is
        valid and the game has not been won or ended in a draw return True.

        :param int row:
        :param int column:
        :param str player:
        :return bool:
        """

        # Return False is the game is over
        if self._current_state != "UNFINISHED":
            return False

        # Return False is move is invalid
        if not self._check_valid_move(row, column):
            return False
        else:
            self._board[row][column] = player
            attached_lines = [self.find_row(row),
                              self.find_column(column),
                              self.find_left_right_diagonal(row, column),
                              self.find_right_left_diagonal(row, column)]
            if self._check_win(attached_lines, player):
                self._current_state = player.upper() + "_WON"
                return True
            if self._check_draw():
                self._current_state = "DRAW"
                return False
