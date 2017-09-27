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

def SudokuInput(sudoku):
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
                return sudoku

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



