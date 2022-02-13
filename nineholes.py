# COMP 302 A
# Nine Holes
# Hamza Asaad 231450993
# Abdullah Baig 231485698

class NineHoles:
    def __init__(self):
        self.board = [
            ["0", "----", "----", "0", "----", "----", "0"],
            ["|", "       ", "", " | ", "", "       ", "|"],
            ["|", "       ", "", " | ", "", "       ", "|"],
            ["0", "----", "----", "0", "----", "----", "0"],
            ["|", "       ", "", " | ", "", "       ", "|"],
            ["|", "       ", "", " | ", "", "       ", "|"],
            ["0", "----", "----", "0", "----", "----", "0"],
        ]

    def runGame(self):  # Function which runs the entire game
        print("---Welcome to Nine Holes---\n\n"
              "-Player 1 is assigned the piece \"A\"\n-Player 2 is assigned the piece \"B\"\n")
        Arr = [[0, 0, 0], [0, 0, 0],
               [0, 0, 0]]  # This array is where are program accepts input it later maps this
        # onto our displayed string board
        self.displayGameBoard()
        playerOnePiece = 1  # Defines the piece for Player 1 for our Arr
        playerTwoPiece = 2  # Defines the piece for Player 2 for our Arr
        outCome = False

        for dropping in range(6):  # For loop for initial phase of the game where players drop their piece onto board
            if outCome:  # If a winning situation arises during our dropping phase we must break loop
                break
            if dropping % 2 == 0:  # If our loop iterator is even then its Player 1s turn else Player 2
                Arr, dropRow, dropCol = self.dropPieces(Arr, playerOnePiece)
                outCome = self.checkWinningConditions(dropRow, dropCol, Arr, playerOnePiece)
            else:
                Arr, dropRow, dropCol = self.dropPieces(Arr, playerTwoPiece)
                outCome = self.checkWinningConditions(dropRow, dropCol, Arr, playerTwoPiece)
            self.mapGameBoard(Arr)

        count = 0
        while not outCome:  # This while loops iterates player by player through the second phase of the game where
            # players move their pieces around the board until there is a victor
            if count % 2 == 0:
                Arr, newRow, newCol = self.movePieces(Arr, playerOnePiece)
                outCome = self.checkWinningConditions(newRow, newCol, Arr, playerOnePiece)
            else:
                Arr, newRow, newCol = self.movePieces(Arr, playerTwoPiece)
                outCome = self.checkWinningConditions(newRow, newCol, Arr, playerTwoPiece)
            self.mapGameBoard(Arr)
            count += 1

    # FUNCTION takes the input to move pieces in the first phase of the game
    def dropPieces(self, Arr, player):
        while True:  # runs infinitely until the player inputs correctly
            try:
                drop = input(f"Please drop a piece Player {player} eg.(12) <--- row: 1 and column: 2 :")
                dropRow = int(drop[0]) - 1
                dropCol = int(drop[1]) - 1
                if Arr[dropRow][dropCol] == 0:  # Check if position is vacant
                    Arr[dropRow][dropCol] = player
                    return Arr, dropRow, dropCol
                else:
                    print("Postion is not vacant.")
            except:
                print("Incorrect input please enter a row number followed by column number to drop your piece!")

    # FUNCTION takes the input to move pieces in the second phase of the game
    def movePieces(self, Arr, player):
        while True:  # runs infinitely until the player inputs correctly
            try:
                move = input(f"Move your piece Player {player} eg.(11 12 from row/column 11 to row/column 12):")
                # Rows and columns that the piece is at currently
                currentRow = int(move[0]) - 1
                currentCol = int(move[1]) - 1
                # Rows and columns where the player wants the piece to move to
                newRow = int(move[3]) - 1
                newCol = int(move[4]) - 1
                if Arr[currentRow][currentCol] == player:  # Check if the current position is occupied by our player
                    if Arr[newRow][newCol] == 0:  # Check if the new position is available
                        Arr[currentRow][currentCol], Arr[newRow][newCol] = 0, player
                        return Arr, newRow, newCol
                    else:
                        print("Position is not vacant.")
                else:
                    print("Incorrect current position.")
            except:
                print("Incorrect input please enter your current row and column followed by new row and column!.")

    # This function is called after every input to check if the piece that has been inputted has met winning conditions
    # Takes the latest positions row and column current Array and player piece to check
    def checkWinningConditions(self, row, column, Arr, player):
        playerPiece = player  # Piece to check
        countRows = 0  # Row counter for the same piece
        countColumns = 0  # Columns counter for the same piece
        outCome = False

        for check in range(3):
            if Arr[row][check] == playerPiece:
                countRows += 1
            if Arr[check][column] == playerPiece:
                countColumns += 1

        if countRows == 3 or countColumns == 3:  # If the same piece exists horizontally or vertically the player has won
            outCome = True
            print(f"Player {player} won!")

        return outCome

    # This function maps our matrix to the equivalent player pieces A and B and displays the board
    # Takes our programs current Arr as input
    def mapGameBoard(self, Arr):
        for i in range(3):
            for j in range(3):
                arrayPiece = Arr[i][j]
                if arrayPiece == 1:
                    self.board[i * 3][j * 3] = "A"
                elif arrayPiece == 2:
                    self.board[i * 3][j * 3] = "B"
                else:
                    self.board[i * 3][j * 3] = "0"
        self.displayGameBoard()

    def displayGameBoard(self):
        for i in self.board:
            str = ""
            for j in i:
                str += j
            print(str)


# Driver function to create an object of our game and run it
def main():
    game = NineHoles()
    game.runGame()


main()
