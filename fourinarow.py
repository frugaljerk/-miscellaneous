"""Four-in-a-Row, by Fred Chiang h.sapiens@hotmail.com
A tile-dropping game to get four-in-a-row, similar to Connect Four.
Credit: Al Sweigart https://inventwithpython.com/beyond/chapter14.html"""

import sys

# Constants used for displaying the board:
EMPTY_SPACE = "."  # A period is easier to count than a space.
PLAYER_X = "X"
PLAYER_O = "O"

# Note: Update BOARD_TEMPLATE & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for displaying the board:
BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""


def main():
    """Runs a single game of Four-in-a-Row."""
    print(
        """Four-in-a-Row, by Al Sweigart al@inventwithpython.com

    Two players take turns dropping tiles into one of seven columns, trying
    to make Four-in-a-Row horizontally, vertically, or diagonally.
    """
    )
    # Set up a new game:
    board = Board()
    playerTurn = PLAYER_X

    while True:
        # Display the board and get player's move:
        board.displayBoard()
        board.getPlayerMove(playerTurn)

        # Check for a win or tie:
        if board.isWinner(playerTurn):
            board.displayBoard() # Display the board one last time.
            print(f"Player {playerTurn} has won!")
            sys.exit()
        elif board.isFull():
            board.displayBoard()  # Display the board one last time.
            print("There is a tie!")
            sys.exit()

        # Switch turns to other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


class Board:
    def __init__(self):
        """Return a dictionary that represents a Four-in-a-Row Board

        The keys are (columnIndex, rowIndex) tupes of two integers, and the
        values are one of the "X", "O", or "." """
        self._board = {}
        for rowIndex in range(BOARD_HEIGHT):
            for columnIndex in range(BOARD_WIDTH):
                self._board[(columnIndex, rowIndex)] = EMPTY_SPACE

    def displayBoard(self):
        """Display the board and its tiles on the screen."""

        # Prepare a list to pass to the format() string method for the board
        # template. The list holds all of the board's tiles( and empty
        # spaces) going left to right, top to bottom:
        tileChars = []
        for rowIndex in range(BOARD_HEIGHT):
            for columnIndex in range(BOARD_WIDTH):
                tileChars.append(self._board[(columnIndex, rowIndex)])

        # Display the board:
        print(BOARD_TEMPLATE.format(*tileChars))

    def getPlayerMove(self, playerTile):
        """Let a player select a column on the board to drop a tile into.

        Returns a tuple of the (colum, row) that the tile falls into"""

        while True:  # Keep asking player until they enter a valid move.
            print(f"Player {playerTile}, enter 1 to {BOARD_WIDTH} or QUIT:")
            response = input("> ").upper().strip()

            if response == "QUIT":
                print("Thanks for playing!")
                sys.exit()

            if response not in COLUMN_LABELS:
                print(f"Enter a number from 1 to {BOARD_WIDTH}.")
                continue # Ask player again for their move.

            columnIndex = int(response) - 1 # -1 for 0-based column indexes

            # If the column is full, ask for a move again:
            if self._board[(columnIndex, 0)] != EMPTY_SPACE:
                print("That column is full, select another one.")
                continue  # Ask player again for their move.

            # Starting from the bottom, find the first empty space.
            for rowIndex in range(BOARD_HEIGHT -1, -1, -1):
                if self._board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                    self._board[(columnIndex, rowIndex)] = playerTile
                    return

    def isFull(self):
        """Returns True if the 'board' has no empty spaces, otherwise returns False."""
        for rowIndex in range (BOARD_HEIGHT):
            for columnIndex in range(BOARD_WIDTH):
                if self._board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                    return False # Found an empty space, so return False
        return True  # All spaces are full

    def isWinner(self, playerTile):
        """Returns True if 'playerTile' has four tiles in a row on 'board',
        otherwise returns False"""

        # Go through the entire board, checking for four-in-a-row:
        for columnIndex in range(BOARD_WIDTH - 3):
            for rowIndex in range(BOARD_HEIGHT):
                # Check for four-in-a-row going across to the right:
                tile1 = self._board[(columnIndex, rowIndex)]
                tile2 = self._board[(columnIndex + 1, rowIndex)]
                tile3 = self._board[(columnIndex + 2, rowIndex)]
                tile4 = self._board[(columnIndex + 3, rowIndex)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True

        for columnIndex in range(BOARD_WIDTH):
            for rowIndex in range(BOARD_HEIGHT - 3):
                # Check for four-in-a-row going down:
                tile1 = self._board[(columnIndex, rowIndex)]
                tile2 = self._board[(columnIndex, rowIndex + 1)]
                tile3 = self._board[(columnIndex, rowIndex + 2)]
                tile4 = self._board[(columnIndex, rowIndex + 3)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True

        for columnIndex in range(BOARD_WIDTH - 3):
            for rowIndex in range(BOARD_HEIGHT - 3):
                # Check for four-in-a-row going right-down diagonal:
                tile1 = self._board[(columnIndex, rowIndex)]
                tile2 = self._board[(columnIndex + 1, rowIndex + 1)]
                tile3 = self._board[(columnIndex + 2, rowIndex + 2)]
                tile4 = self._board[(columnIndex + 3, rowIndex + 3)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True

                # Check for four-in-a-row going left-down diagonal:
                tile1 = self._board[(columnIndex + 3, rowIndex)]
                tile2 = self._board[(columnIndex + 2, rowIndex + 1)]
                tile3 = self._board[(columnIndex + 1, rowIndex + 2)]
                tile4 = self._board[(columnIndex, rowIndex + 3)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True
        return False


if __name__ == "__main__":
    main()