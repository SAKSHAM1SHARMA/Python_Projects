puzzle = [
    [3,0,0,0,2,0,0,7,0],
    [9,0,0,5,0,0,0,1,4],
    [0,1,6,3,7,0,0,0,8],
    [2,0,0,8,0,0,0,0,1],
    [5,0,0,0,4,1,8,0,0],
    [0,8,9,0,0,0,0,5,0],
    [0,0,5,0,1,0,2,8,0],
    [0,4,0,0,0,6,0,9,3],
    [7,3,1,0,8,2,0,0,0]
]

def is_valid(puzzle, row, col, value):
    # Row check
    for i in range(9):
        if puzzle[row][i] == value:
            return False
    # Column check
    for j in range(9):
        if puzzle[j][col] == value:
            return False
    # Box check
    r = row - row % 3
    c = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[r + i][c + j] == value:
                return False
    return True

def show_Puzzle(a):
    print("+-------+-------+-------+")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("|-------+-------+-------|")
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")
            if a[i][j] == 0:
                print(".", end=' ')
            else:
                print(a[i][j], end=' ')
        print("|")
    print("+-------+-------+-------+")

def is_Given_Puzzle_Valid(puzzle):
    for i in range(9):
        for j in range(9):
            value = puzzle[i][j]
            if value < 0 or value > 9:
                return False
            if value != 0:
                puzzle[i][j] = 0
                if not is_valid(puzzle, i, j, value):
                    puzzle[i][j] = value
                    return False
                puzzle[i][j] = value
    return True

def Sudoku_Solver(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for value in range(1, 10):
                    if is_valid(puzzle, i, j, value):
                        puzzle[i][j] = value
                        if Sudoku_Solver(puzzle):
                            return True
                        puzzle[i][j] = 0
                return False
    return True

show_Puzzle(puzzle)

if is_Given_Puzzle_Valid(puzzle):
    if Sudoku_Solver(puzzle):
        print("Sudoku Solved Successfully!\n")
        show_Puzzle(puzzle)
    else:
        print("No solution exists for the given Sudoku.")
else:
    print("Given puzzle is invalid.")
