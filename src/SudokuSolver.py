class SudokuSolver(object):
    def __init__(self, board=None):
        super().__init__()
        self.board = board

    def __str__(self):
        if not self.board:
            return "None"
        
        formated_board = ""

        for i, element in enumerate(self.board):
            if not element:
                formated_board += "X"
            else:
                formated_board += str(element)

            if i % 9 == 0 and i != 0:
                formated_board += "\n"
            else:
                formated_board += " "
        
        return formated_board

    def setBoard(self, board):
        self.board = board
    
    def clearBoard(self):
        self.board = None


    # these set of functions returns the row, column, or subgroup of a current position.
    def _row(pos: int):
        pass

    def _column(pos: int):
        pass

    def _subgroup(pos: int):
        pass

    def solve(self):
        if not self.board:
            return None