class SudokuSolver(object):

    # initalizes the board of the solver
    def __init__(self, board=None):
        self.board = board

    # prints the board in a readable format
    def __str__(self):

        if not self.board:
            return "No board"
        
        formated_board = ""

        for i, element in enumerate(self.board):
            if not element:
                formated_board += "X"
            else:
                formated_board += str(element)

            if (i+1) % 9 == 0:
                formated_board += "\n"
            else:
                formated_board += "  "
        
        return formated_board

    # sets the board
    def setBoard(self, board):
        if isinstance(board, list):
            if len(board) == 81:
                self.board = board
    
    # clears the board
    def clearBoard(self):
        self.board = None

    # finds an empty position on the board.
    def findEmptyPos(self):
        for pos, element in enumerate(self.board):
            if not element:
                return pos 

    
    # recursive, backtracking solver
    def _solve(self, rowHash, colHash, squareHash):

        # find the next empty position
        next_empty = self.findEmptyPos()

        if next_empty == None:
            # if there isn't another empty spot
            return True

        row = next_empty // 9
        col = next_empty % 9
        square = (row // 3, col // 3)

        for num in rowHash[row].intersection(colHash[col], squareHash[square]):
                
            self.board[next_empty] = num

            rowHash[row].discard(num)
            colHash[col].discard(num)
            squareHash[square].discard(num)
                
            # if the board is solved, done!
            if self._solve(rowHash, colHash, squareHash):
                return True

            self.board[next_empty] = None

            rowHash[row].add(num)
            colHash[col].add(num)
            squareHash[square].add(num)

        return False


    def solve(self):

        if not self.board:
            return None

        # first initalize sets of possible choices for rows, cols, and squares
        # used to keep track of usable values
        rowHash = {i:set([j for j in range(1, 10)]) for i in range(9)}
        colHash = {i:set([j for j in range(1, 10)]) for i in range(9)}
        squareHash = {(i, j): set([k for k in range(1, 10)]) for i in range(3) for j in range(3)}

        for i, element in enumerate(self.board):

            # skip over blank spaces
            if not element:
                continue

            row = i // 9
            col = i % 9
            square = (row // 3, col // 3)

            # remove the element from possible choices
            try:
                rowHash[row].remove(element)
                colHash[col].remove(element)
                squareHash[square].remove(element)
            except KeyError:
                print(row, col, square)
                # element already removed no solution
                return False
        
        # sets initalized now pass to helper function

        return self._solve(rowHash, colHash, squareHash)
    