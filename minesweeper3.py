from cProfile import label
from sre_constants import JUMP
from tkinter import CENTER
from turtle import color, goto
import PySimpleGUI as sg
from random import randint as rng
import time 
 
sg.theme('dark purple')
layout2 = [
    [sg.Text('Campo Minado', font=('Franklin Gothic Book', 24), text_color=('white'))],
    [sg.Radio('Easy', 'Group_A', key='D', enable_events=True, font=('Franklin Gothic Book', 16), default=True, text_color=('medium spring green'))],
    [sg.Radio('Medium', 'Group_A', key='E', enable_events=True, font=('Franklin Gothic Book', 16), text_color=('yellow'))],
    [sg.Radio('Hard', 'Group_A', key='F', enable_events=True, font=('Franklin Gothic Book', 16), text_color=('FireBrick2'))],
    [sg.Push(), sg.Button('Iniciar', font=('Franklin Gothic Book', 24), button_color=('white','#7967E0')), sg.Push()]
]

window2 = sg.Window('tlauncher2.0', layout2)

while True:
        event, values = window2.read()
        
        if event == sg.WIN_CLOSED:
            break
        if values['D'] == True:
            nm = 10
        if values['E'] == True:
            nm = 15
        if values['F'] == True:
            nm = 20
        if event == 'Iniciar':
            window2.close()           
                    
       
           
            
            MINES = nm
            MAX_ROWS = MAX_COL = 10
            cbr = 0

            layout = [[], [], [], [], [], [], [], [], [], [], []]

            board = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]
            ]
            b = {'size':(4,2), 'font':('Franklin Gothic Book', 14), 'button_color':('white','#7967E0')}
            def gba():            
                PlacedBombs = 0
                while PlacedBombs < MINES:
                    coluna = rng(0,9)
                    linha = rng(0,9)

                    if board[linha][coluna] == 0:
                        board[linha][coluna] = 1
                        PlacedBombs += 1

                


            def glt():
                global layout    
                for i in range(10):
                    layout[i] = []
                    for j in range(10):
                        layout[i].append(sg.Button(('?'), **b, key=(i,j), pad=(0,0))) 
                layout[i + 1].append(sg.Text(0,key = 'text'))  


            def tiab(linha, coluna):
                if board[linha][coluna] == 1:
                    return True
                return False

            def vb(linha, coluna):    
                cbr = 0
                for i in range(linha - 1, linha + 2):
                    for j in range(coluna - 1, coluna + 2):
                        if i >= 0 and i <= 9 and j >= 0 and j <= 9:
                            if board[i][j] == 1:
                                cbr += 1
                return cbr 
            
            def timer():
                return int(round(time.time()*100))    
                    




            def abrejogo():
                global layout
                
                window = sg.Window("minesweepervnaosseimais", layout = layout)

                timer_has_started = timer()
                timer_de_agora = timer_has_started + timer()
                while True:
                    event, values = window.read()
                    timer_de_agora = timer() - timer_has_started                                                 
                    if event == sg.WIN_CLOSED:
                        break            
                    if board[event[0]][event[1]] == True:                
                        window[(event[0], event[1])].update('X',button_color=('white','red'))
                        sg.Popup("Fim de Jogo")
                        window.close()                    
                        layout = [[], [], [], [], [], [], [], [], [], [], []]
                        glt()                    
                        abrejogo()                    
                    else:                                                
                        tiab(event[0], event[1])
                        nb = vb(event[0], event[1])
                        window[(event[0], event[1])].update(f'{nb}', button_color=('white','black'))
                    window['text'].update(f'{(timer_de_agora // 100)// 60}:{(timer_de_agora // 100)% 60}:{(timer_de_agora % 100)}')
                                            
                                
                            
                            

                window.close()

            board = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]
            ]
            gba()
            layout = [[], [], [], [], [], [], [], [], [], [], []]
            glt()
            abrejogo()