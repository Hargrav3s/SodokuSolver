from SudokuSolver import *

import os
from time import perf_counter

# intialize solver and paths
solver = SudokuSolver()
test_boards_path = 'example-boards\\test-boards'

# define a comparison function for lists
def same(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        if len(list1) != len(list2):
            return False
        
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True
    return False

# get into the correct working directory
if os.path.isdir(test_boards_path + '\\boards') and os.path.isdir(test_boards_path + '\\solutions'):
    os.chdir(test_boards_path)

    # for each test board
    print()
    for fd in os.listdir(os.getcwd() + "\\boards"):
        name = fd[:-4]

        board = solver.read_board(os.path.join(os.getcwd() + "\\boards", fd))
        solution = solver.read_board(os.path.join(os.getcwd() + "\\solutions", name + "_s.txt"))

        solver.setBoard(board)

        start_time = perf_counter()
        result, msg = solver.solve()
        end_time = perf_counter()

        print("Solution found for {}: {}".format(name, result))
        print("Message: {}".format(msg))

        if solution:
            if same(solver.board, solution):
                print("Solutions Match!")
        else:
            print("No solution to match with")
        
        print()
    print()
else:
    print("Error: Either", os.getcwd() + "\\boards", "or", os.getcwd() + "\\solutions", "is not a directory")
