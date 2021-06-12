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

    # sets the board
    def setBoard(self, board):

        # simple check to set the list
        if isinstance(board, list):
            if len(board) == 81:
                self.board = board
    
    # clears the board
    def clearBoard(self):
        self.board = None

    # # # Read Board From File # # #
    #   DESC
    #       reads a board from a given path and sets it to the solvers board
    #
    #   INPUTS
    #       path    - path to the board file.
    #
    def setBoardWithFile(self, path):
        board = self.read_board(path)
        self.setBoard(board)


    # # # Write Board function # # #
    #   DESC
    #       writes the board in the solver to the given path.
    #
    #   INPUTS
    #       path    - path to the output file.
    #
    def writeBoard(self, path):
        if self.board:
            self.write_board(self.board, path)


    # # # Read Board function # # #
    #   DESC
    #       reads a board from a given path.
    #
    #   INPUTS
    #       path    - path to the board file.
    #
    #   OUTPUTS
    #       board   - sudoku board as a python list.
    @staticmethod
    def read_board(path):

        # try opening the file
        try:
            with open(path, 'r') as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            print("File {} does not exist".format(path))
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

    # # # Write Board function # # #
    #   DESC
    #       writes a board to a file given at a path.
    #
    #   INPUTS
    #       board   - given sudoku board in list format.
    #       path    - path to the output file.
    #
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

    # finds an empty position on the board with the smallest number of avaliable numbers.
    # returns None if no empty position on board.
    def findEmptyPos(self, rowHash, colHash, squareHash):
        min_pos = None
        min_avaliable = 10
        for pos, element in enumerate(self.board):
            if not element:
                row = pos // 9
                col = pos % 9
                square = (row // 3, col // 3)

                avaliable = len(rowHash[row].intersection(colHash[col], squareHash[square]))

                if avaliable < min_avaliable:
                    min_avaliable = avaliable
                    min_pos = pos
        
        return min_pos
                

    
    # # # The main backtracking, recursive solver for the sudoku boards # # #
    #   DESC
    #       Main backtracking strategy to solve sudoku boards. Uses the intersection of sets to calulcate
    #       placeable numbers given the contraints of the game.
    #
    #   INPUTS
    #       rowHash     - hashset of avaliable numbers for a given row
    #       colHash     - hashset of avaliable numbers for a given column
    #       squareHash  - hashset of avaliable numbers for a given subsquare
    #       start_time  - time the solver started
    #       max_time    - maximum time solver should spend on solving
    #
    #   OUTPUTS
    #   (the following is outputed as a 2-tuple)
    #       result      - boolean of whether the board was solved or not
    #       message     - string message that tells why the function exited

    def _solve(self, rowHash, colHash, squareHash, start_time, max_time):

        if max_time:
            from time import time
            if time() - start_time > max_time:
                return False, "Max time reached"

        # find the next empty position
        next_empty = self.findEmptyPos(rowHash, colHash, squareHash)

        # if there isn't another empty spot, the board is solved
        if next_empty == None:
            return True, "Solved!"

        # calculate the row, col, and subsquare of the empty position.
        row = next_empty // 9
        col = next_empty % 9
        square = (row // 3, col // 3)

        for num in rowHash[row].intersection(colHash[col], squareHash[square]):
            
            # going to test num in the empty position
            self.board[next_empty] = num

            # remove from avaliable numbers in its respective row, col, and subsquare.
            rowHash[row].discard(num)
            colHash[col].discard(num)
            squareHash[square].discard(num)
            
            result, msg = self._solve(rowHash, colHash, squareHash, start_time, max_time)
            
            # if solved, we stop!
            if result:
                return True, "Solved!"
            
            # if the maximum time has been reached, return out of the stack
            elif msg == "Max time reached":
                return False, msg

            # otherwise we backtrack

            self.board[next_empty] = None

            rowHash[row].add(num)
            colHash[col].add(num)
            squareHash[square].add(num)
        
        # reaching out here, we recieved no solution
        return False, "No solution"

    # # # Solve Helper Function # # #
    #   DESC
    #       Initalizes the hashsets for the backtracking solve function.
    #       Checks if the board is invalid before solving.
    #
    #   INPUTS
    #       max_time    - maximum time the function should spend solving
    #
    #   OUTPUTS
    #   (the following is outputed as a 2-tuple)
    #       result      - boolean of whether the board was solved or not
    #       message     - string message that tells why the function exited
    #
    def solve(self, max_time=None):

        if not self.board:
            return False, "No board"

        # first initalize sets of possible choices for rows, cols, and subsquares
        # used to keep track of usable values for a position.
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
                if element in set(range(1,10)):
                    return False, "Invalid Board. Board violates row, col, subsquare constraint."
                else:
                    return False, "Invalid Board. Board contained invalid elements: {}".format(element)
        
        
        # call recursive backtracking helper function to solve.
        from time import time
        return self._solve(rowHash, colHash, squareHash, time(), max_time)