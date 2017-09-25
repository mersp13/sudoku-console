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

for i in range(0, 9):
    for j in range(0, 9):
        print("Please input a number for (row %s, col %s)" %(i, j))
        sudoku_input = int(input())
        if sudoku_input > 0 and sudoku_input <= 9:
            sudoku_input = str(sudoku_input)
        else:
            sudoku_input = " "
        sudoku.append(sudoku_input)

def SudokuSolver():
    pass

def switch(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")


print("Solve this Sudoku?('y'or'n')")

for i in range(0, 3):
    print("+-------+-------+-------+")
    for j in range(0, 3):
        print("| " + sudoku[(9*i*(j-1))] + " " + sudoku[((9*i*(j-1))+1)] + " " + sudoku[((9*i*(j-1))+2)] + " | "
                + sudoku[(9*i*(j-1))+3] + " " + sudoku[((9*i*(j-1))+3)] + " " + sudoku[((9*i*(j-1))+5)] + " | "
                + sudoku[(9*i*(j-1))+6] + " " + sudoku[((9*i*(j-1))+7)] + " " + sudoku[((9*i*(j-1))+8)] + " |")
print("+-------+-------+-------+")

YoN_selection = input()


