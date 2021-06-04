class SudokuSolver(object):

    # initalizes the board of the solver
    def __init__(self, board=None):

        # does a simple check to set the list.
        if isinstance(board, list):
            if len(board) == 81:
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

    # sets the board if the board is in valid format
    def setBoard(self, board):

        # simple check to set the list
        if isinstance(board, list):
            if len(board) == 81:
                self.board = board
    
    # clears the board
    def clearBoard(self):
        self.board = None

    # READ/WRITE BOARD FROM FILE FUNCTIONS
    #
    # Assume the file is in the given format that described in the overview file:
    #   an ‘X’ represents an open cell and a number indicates a fixed starting value for a cell.

    # function reads a sudoku board from the path location and returns it as a python list.
    @staticmethod
    def read_board(path):

        # try opening the file
        try:
            with open(path, 'r') as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            print("File does not exist")
            return None
        
        # intialize the puzzle
        puzzle = []

        # read into the puzzle.
        for line in lines:
            for character in line:
                if character == 'X':
                    puzzle.append(None)
                else:
                    try:
                        puzzle.append(int(character))
                    except ValueError:
                        print("Invalid character in puzzle")
                        return None
        
        return puzzle

    # writes a sudoku board in python list format to a file specified by path.
    @staticmethod
    def write_board(board, path):
        
        # create the file to write into
        try:
            with open(path, 'w') as file:
                for i, element in enumerate(board):
                    if i % 9 == 0 and i != 0:
                        file.write('\n')
                    
                    if not element:
                        file.write('X')
                    else:
                        file.write(str(element))
        except IOError:
            print("Error writing to file.")

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

        # next need to elimnate the already filled in spaces on the board.
        for i, element in enumerate(self.board):

            # skip over blank spaces
            if not element:
                continue

            row = i // 9
            col = i % 9
            square = (row // 3, col // 3)

            # remove the number from possible choices
            try:
                rowHash[row].remove(element)
                colHash[col].remove(element)
                squareHash[square].remove(element)
            except KeyError:
                if element in list(range(1,10)):
                    print("Invalid Board. Board violates row, col, subsquare constraint.")
                else:
                    print("Invalid Board. Board contained invalid elements:", element)
                return False
        
        # finally, simply check their are no positions where no moves can be made,
        # saves time when the board is known not too have a solution with the current board state.

        for i in range(81):
            if not self.board[i]:
                row = i // 9
                col = i % 9
                square = (row // 3, col // 3)
                if len(rowHash[row].intersection(colHash[col], squareHash[square])) == 0:
                    return False
        
        # call recursive backtracking helper function to solve.
        return self._solve(rowHash, colHash, squareHash)
    