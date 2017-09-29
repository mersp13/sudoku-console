#!/usr/bin/env python
# coding=utf-8

import re, os, sys

def SudokuInit():
    sudoku = {}
    for i in range(9):
        for j in range(9):
            sudoku["(%s, %s)" %(i+1, j+1)] = " "
    return sudoku

def TxtInput(txt=""):
    if sys.hexversion < 0x30000F0:
        txt_input = raw_input(str(txt))
    else:
        txt_input = input(str(txt))
    return txt_input

def SquareDict(row_args, col_args):
    row_modrlt = int(row_args) % 3
    col_modrlt = int(col_args) % 3
    row_modict = {"1": [int(row_args) + 1, int(row_args) + 2],
                    "2": [int(row_args) - 1, int(row_args) + 1],
                    "0": [int(row_args) - 2, int(row_args) - 1]
                    }
    col_modict = {"1": [int(col_args) + 1, int(col_args) + 2],
                    "2": [int(col_args) - 1, int(col_args) + 1],
                    "0": [int(col_args) - 2, int(col_args) - 1]
                    }
    square_dict = {"row": row_modict["%s" %row_modrlt], "col": col_modict["%s" %col_modrlt]}
    return square_dict

def SudokuInput(soduko):
    print("Input format: 'row col num'" +
        "\n\\" + "| enter 'end' to end input" +
        "\n\\" + "| enter 'reset' to reset" +
        "\n\\" + "| enter 'exit' to exit")
    sudoku_input = TxtInput()
    if sudoku_input == "end":
        ask_msg = TxtInput("solve this sudoku? ('y' or 'n')")
        if ask_msg == "y":
            SudokuSolver(sudoku)
        elif ask_msg == "n":
            pass
        else:
            pass
    elif sudoku_input == "reset":
        for k in sudoku.keys():
            sudoku[k] = " "
    elif sudoku_input == "exit":
        sys.exit()
    else:
        sudoku_reg = re.compile("(?P<row>\d)(\D)+(?P<col>\d)(\D)+(?P<num>\d)")
        match_obj = sudoku_reg.match(sudoku_input)
        if match_obj:
            match_dict = match_obj.groupdict()
            if "0" not in match_dict.values():
                sudoku["(%s, %s)" %(match_dict["row"], match_dict["col"])] = match_dict["num"]
                for i in range(1, 10):
                    if (i != int(match_dict["col"])) and (sudoku["(%s, %s)" %(match_dict["row"], i)] == match_dict["num"]):
                        sudoku["(%s, %s)" %(match_dict["row"], i)] = " "
                    if (i != int(match_dict["row"])) and (sudoku["(%s, %s)" %(i, match_dict["col"])] == match_dict["num"]):
                        sudoku["(%s, %s)" %(i, match_dict["col"])] = " "
                square_dict = SquareDict(match_dict["row"], match_dict["col"])
                for i in square_dict["row"]:
                    for j in square_dict["col"]:
                        if sudoku["(%s, %s)" %(i, j)] == match_dict["num"]:
                            sudoku["(%s, %s)" %(i, j)] = " "
                return sudoku

def SudokuChecker(sudoku):   #TODO:sudokuchecker
    pass

def SudokuSolver(sudoku):    #TODO:sudokusolver
    pass

def SudokuPrint(sudoku):
    for i in range(3):
        print("+-------+-------+-------+")
        for j in range(3):
            print("| " + sudoku["(%s, %s)" %(3*i+j+1, 1)] + " "
                    + sudoku["(%s, %s)" %(3*i+j+1, 2)] + " "
                    + sudoku["(%s, %s)" %(3*i+j+1, 3)] + " | "
                    + sudoku["(%s, %s)" %(3*i+j+1, 4)] + " "
                    + sudoku["(%s, %s)" %(3*i+j+1, 5)] + " "
                    + sudoku["(%s, %s)" %(3*i+j+1, 6)] + " | "
                    + sudoku["(%s, %s)" %(3*i+j+1, 7)] + " "
                    + sudoku["(%s, %s)" %(3*i+j+1, 8)] + " "
                    + sudoku["(%s, %s)" %(3*i+j+1, 9)] + " |")
    print("+-------+-------+-------+")


if sys.hexversion < 0x20700F0:
    print("a higher python version is required")
    sys.exit()

sudoku = SudokuInit()
while True:
    SudokuPrint(sudoku)
    print(len(sudoku.values()))
    SudokuInput(sudoku)
    os.system("cls")



