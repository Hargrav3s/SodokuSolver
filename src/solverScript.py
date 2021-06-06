from SudokuSolver import SudokuSolver
import os

from time import perf_counter

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
    print()
    for file in os.listdir(path):

        # if the item is a file
        if os.path.isfile(path + '/' + file):

            print("Solving board stored in {}".format(path + '/' + file))

            # read the board
            solver.setBoardWithFile(path + '/' + file)

            # in case the board was not set, continue to the next board.
            if not solver.board:
                print("Error setting board stored at {}, continuing...".format(path + '/' + file))
                continue

            # solve the board
            start = perf_counter()
            result, msg = solver.solve()
            stop = perf_counter()

            # print results
            print("\nResults:\n\tsolved = {}\n\tmessage = {}\n\ttime = {:.5f} seconds\n".format(result, msg, stop - start))

            # write the board
            print("Writing completed board to {}".format(sol_path + file[:-4] + '.sln.txt'))
            solver.writeBoard(sol_path + file[:-4] + '.sln.txt')
            print()
    print()
else:
    print("{} is and invalid path".format(path))