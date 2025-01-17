from flask import Flask, request, jsonify, render_template,redirect,url_for
from main import generate_Sudoku_Board,fill_matrix
from solution.sudokusolver import sudokusolver as sudokusolver


app = Flask(__name__)
example_board = []

def Generateboard(number):
    global example_board
    example_board = []
    example_board,random_positions = generate_Sudoku_Board(number = number)
    # sometimes the number randomized could be repeated in the same row or column or in a sub 3X3 matrix
    fill_matrix(example_board, random_positions)
    

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods = ['GET','POST'])
def index():
    #print(solutionpy,example_board)
    return render_template('index.html',puzzle = example_board,solution = [])

@app.route('/send_number', methods=['POST'])
def send_number():
    generatedBoard =[]
    number = int(request.form.get('number'))  # Get the number from the form data
    # Process the number as needed
    print(f'Received number: {number}')  # For demonstration
    while True:
        Generateboard(number)
        # inital stage of the generated board
        for row in example_board:
            print(row)
        generatedBoard = [data[:] for data in example_board]
        # board solving solution using backtracing/recursion once called it starts solving the given puzle board
        obj = sudokusolver(example_board)
        if obj.flag_solvable:
            break
    # solved sudoku matrix
 
    solutionpy = obj.puzzle
    print("solved puzzle")
    for i in solutionpy:
        print(i)
    return render_template('index.html',puzzle = generatedBoard,solution = solutionpy)
@app.route("/validateSolutuion",methods = ["POST","GET"])
def validateSolution():
    pass

if __name__ == '__main__':
    app.run(debug=True)
