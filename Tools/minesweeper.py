import PySimpleGUI as sg
from random import randint

MAX_ROWS = MAX_COL = 10

board = [[randint(0,1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

layout =  [[sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

window = sg.Window('Minesweeper', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    window[event].update(board[event[0]][event[1]], button_color=('white','black'))

window.close()