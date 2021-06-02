# Assume the given format is that described in the overview file as such:
#   an ‘X’ represents an open cell and a number indicates a fixed starting value for a cell.

# reads a sudoku board from the path location and returns it as a python list.
def read_board(path):

    # try opening the file
    try:
        with open(path, 'r') as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print("File does not exist")
        exit()
    
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
                    exit()
    
    return puzzle

# writes a sudoku board in python list format to a file specified by path.
def write_board(board, path):
    
    # create the file to write into
    try:
        with open(path, 'x') as file:
            for i, element in enumerate(board):
                if i % 9 == 0 and i != 0:
                    file.write('\n')
                
                if not element:
                    file.write('X')
                else:
                    file.write(str(element))
    except FileExistsError:
        print('File already exists')
        exit()
  