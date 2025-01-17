import random
import solution.sudokusolver


#this is a helper function#to check if the generated board is vaild or not if not it fills with some other random numbers
def fill_matrix(matrix, positions):
    for row, col in positions:
        # Try to place a unique number at each position
        num = random.randint(1, 9)
        while not solution.sudokusolver.is_valid(matrix, num,row, col):
            # solution.sudokusolver.is_valid is a reused function in sudokusolver class where it checks for any repeated values with the row,column,submatrices
            num = random.randint(1, 9)
        matrix[row][col] = num

#generates a randomized sudoku board
def generate_Sudoku_Board(number):
    #initializing all the cell of the board to empty values
    example_board = [[-1 for _ in range(9)] for _ in range(9)]
    #selecting indices at random selectively 9 we can select as many positions as needed(all this consoiider the puzzle is a 1d array not a 2d matrix)
    random_positions = random.sample(range(81), number)
    # after the indices are chosen we need to unpack the values to be fitted to a 9x9 matris using num//9 for rows and num%9 for column this onlu works ofr an NxN matrix
    random_positions = [(pos // 9,pos % 9) for pos in random_positions]
    for row,col in random_positions:
        #randomiozing the numbers generated with a range of 1-9 
        example_board[row][col] = random.randint(1, 9)
    return example_board,random_positions