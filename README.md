# Gavant Sudoku Solver
This repository contains my sudoku solver implemented using a backtracking strategy. The project is in pure python and was developed on Python 3.9.5.

The solver is an object which can read a sudoku board in the given format, solve the board by filling in blank spaces with the digits 1-9 without violating the following constrains:
1. Rows may only contain the numbers 1 to 9 only once
2. Columns may only contain the numbers 1 to 9 only once
3. Subsquares may only contain the numbers 1 to 9 only once

This contraint is satsified using hashsets of usable numbers for each row, column, and subsquare then taking the intersection of these sets when calulating the placeable numbers for a blank space.

## Implementation
The solver is implemented as a class object with functions that make handling reading, writing, and solving boards hassle free.

## Functions
>setBoard - This function takes in a sudoku board as a python list and sets it as the solver's board.

>clearBoard - This function clears the board referenced by the solver.

>read_board - This static function takes in a path to a sudoku puzzle (completed or not) returns it as a python list.

> write_board - This static function takes in a board to be written to a file as well as the path to that file.

>setBoardWithFile - This function takes in a path to a sudoku puzzle, reads it into a python list, then sets it as the solver's board

>writeBoard - This function takes in a path and writes the solver's board to the given path.

>findEmptyPos - Function finds the next empty position in the board and returns its position, if no empty position is found it returns None

>solve - Solves the solver's sudoku board. Can take in a max_time for the function to spend on solving the puzzle.

>_solve - Interal function called by the solve function, recursively checks solutions with a depth-first-search strategy with pruning and backtracking.

## Installation
To get a working copy of this project, you must first clone this repository to your local machine. You will also need to have the latest version of Python installed.

## How to Run
This project has two main scripts, the test.py script and the solverScript.py. The test script is ran on a few test boards from the University of Vaasa research and were used to verify my solver's capibility and integrity.

The other script solverScript.py is used to run on multiple sudoku boards, specifically the ones provided by Gavant.

To run either script: 
1. Change into the src directory
2. Run the python files using the following commands:
> python test.py
> python solverScript.py

The solver script can be ran on custom boards too as mentioned in the overiew document. To run on custom sudoku boards:
1. Make sure boards are in a .txt file and are formated correctly
2. Place the boards in the "gavant-boards" directory (located in the src directory)
3. Run the solverScript.py as mentioned above, solutions will be placed in a solutions directory within the gavant-boards directory.

### Testing Procedures
To test the solver class, I found a few sudoku puzzles online as well as created an example which should fail. I ran the solver using the test.py script and it performaed as expected, solving the ones with solutions, and returning False on the one with no solution.

### Challenges
The main challenge for this project was how to implement the backtracking algorithm efficiently, I decided upon using sets to calulate placeable values for a given empty position. 

Since no row, column, and subsquare can contain duplicate entries, we simply take the intersection of avaliable numbers to find our placeable numbers for a given position.

To further increase the efficiency of the solver, it outright rejects boards that are observably not solvable before going into the recursive solver. Any board where a blank position has no placements or boards that violate the constraits given immediately returns false.

If the board has no solution and makes it into the solver, the solver will eventually return false.

### Sources
Sudoku Research Boards [http://lipas.uwasa.fi/~timan/sudoku/](http://lipas.uwasa.fi/~timan/sudoku/)