from RWBoards import *
from SudokuSolver import *

import os
from time import perf_counter

# intialize solver and paths
solver = SudokuSolver()
test_boards_path = 'example-boards\\test-boards'

def same(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

# get into the correct working directory
if os.path.isdir(test_boards_path + '\\boards'):
    os.chdir(test_boards_path)

    # for each test board
    print()
    for fd in os.listdir(os.getcwd() + "\\boards"):
        name = fd[:-4]

        board = read_board(os.path.join(os.getcwd() + "\\boards", fd))
        solution = read_board(os.path.join(os.getcwd() + "\\solutions", name + "_s.txt"))

        solver.setBoard(board)
        solver.solve()
 

        if not same(solver.board, solution):
            print("Solver did not find the solution for", name)
        else:
            print("Solver found the solution for", name)

    print()

else:
    print("Error:", os.getcwd() + "\\boards", "is not a directory")
