#!/usr/bin/env python
# coding=utf-8

sudoku = []

print("\
+-------+-------+-------+\n\
| % % % | % % % | % % % |\n\
| % % % | % % % | % % % |\n\
| % % % | % % % | % % % |\n\
+-------+-------+-------+\n\
| % % % | % % % | % % % |\n\
| % % % | % % % | % % % |\n\
| % % % | % % % | % % % |\n\
+-------+-------+-------+\n\
| % % % | % % % | % % % |\n\
| % % % | % % % | % % % |\n\
| % % % | % % % | % % % |\n\
+-------+-------+-------+\n\
")

def SudokuInput():
    for i in range(0, 9):
        for j in range(0, 9):
            print("Please input a number for (row %s, col %s)" %(i, j))
            sudoku_input = int(input())
            if sudoku_input > 0 and sudoku_input <= 9:
                sudoku_input = str(sudoku_input)
            else:
                sudoku_input = " "
            sudoku.append(sudoku_input)
    return sudoku

def SudokuSolver():
    pass

def SudokuPrint(sudoku):
    for i in range(0, 3):
        print("+-------+-------+-------+")
        for j in range(0, 3):
            print("| " + sudoku[(9*i*(j-1))] + " " + sudoku[((9*i*(j-1))+1)] + " " + sudoku[((9*i*(j-1))+2)] + " | "
                    + sudoku[(9*i*(j-1))+3] + " " + sudoku[((9*i*(j-1))+3)] + " " + sudoku[((9*i*(j-1))+5)] + " | "
                    + sudoku[(9*i*(j-1))+6] + " " + sudoku[((9*i*(j-1))+7)] + " " + sudoku[((9*i*(j-1))+8)] + " |")
    print("+-------+-------+-------+")


sudoku = SudokuInput()
while True:
    print("Solve this Sudoku?('y'or'n')")
    YoN_selection = input()
    if YoN_selection == "y":
        SudokuSolver()
        break
    elif YoN_selection == "n":
        sudoku = SudokuInput()
    else:
        print("unknown command")




