from SudokuSolver import SudokuSolver
import os

# initalize the path and solver
path = 'gavant-boards'
solver = SudokuSolver()
sol_path = path + '/solutions/'

# create the solutions directory if it doesn't exist already.
try:
    os.mkdir(sol_path)
except FileExistsError:
    pass

# check the path is a directory
if os.path.isdir(path):
    # for each item in the directory
    for file in os.listdir(path):

        # if the item is a file
        if os.path.isfile(path + '/' + file):

            # read the board
            solver.setBoardWithFile(path + '/' + file)

            # solve the board
            result, msg = solver.solve()

            # print results
            print(result, msg)

            # write the board
            solver.writeBoard(sol_path + 'solution_' + file)
else:
    print("not valid path")