class sudokusolver:
    def __init__(self,puzzle):#assigns value to the puzzle varible of the class and initiates the solving process
        self.puzzle = puzzle
        self.flag_solvable = self.solve_sudoku()
        print(self.flag_solvable)
    
    def find_next_empty(self):
        # finds the next row, col on puzzle that's not filled yet --> we represent these with -1
        # returns a row, col tuple (or (None, None) if there is none)
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == -1:
                    return row,col
        return None,None

    def solve_sudoku(self):
        # solve sudoku using backtracking!
        # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
        # return solution

        # step 1: choose somewhere on the puzzle to make a guess
        row,col = self.find_next_empty()
        #print(row,col,end=";")
        # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
        if row is None:
            return True
        # step 2: if there is a place to put a number, then make a guess between 1 and 9
        for guess in range(1,10):
            if is_valid(self.puzzle,guess,row,col):# step 3: check if this is a valid guess
                self.puzzle[row][col] = guess# step 3.1: if this is a valid guess, then place it at that spot on the puzzle
                if self.solve_sudoku():# step 4: then we recursively call our solver!
                    return True# step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
            self.puzzle[row][col] = -1
        return False# step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    if guess in puzzle[row]:
        return False
     # now the column
    puzzle_columns = [puzzle[i][col] for i in range(9)]
    if guess in puzzle_columns:
        return False
    # and then the square
    row_start = (row//3)*3
    col_start = (col//3)*3
    subpuzzle3by3 = [puzzle[r][c] for r in range(row_start,row_start+3) for c in range(col_start,col_start+3)]
    if guess in subpuzzle3by3:
        return False
    
    # if it is not returned in the above conditions its probably true
    return True