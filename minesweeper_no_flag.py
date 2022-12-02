# Library stuff

import PySimpleGUI as sg
import random
import time
from PIL import Image

# Time Stuff

def time_int():
    return int(round(time.time() * 100))


# Execute order 66

def Order66():

    # Window 1

    sg.theme('dark green 1')
    l1 = [[sg.Text('Minesweeper', font=('Franklin Gothic Book', 14, 'bold'), text_color='gold')], [sg.Button('Start', font=('Franklin Gothic Book', 14))]]
    win1 = sg.Window('Minesweeper', l1)

    

    condition1 = False
    condition2 = False
    stop = False
    winner = False
    restart = False

   

    holes = 0
    mines = 0
    coo = []

    # Bomb finder

    def radar():
        coo2 = coo
        counter = 0
        coo2[0] -= 1
        coo[1] -= 1
        if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
            if minas[coo2[0]][coo2[1]] == 1:
                counter += 1
        for i in range(2):
            coo2[1] += 1
            if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
                if minas[coo2[0]][coo2[1]] == 1:
                    counter += 1
        for i in range(2):
            coo2[0] += 1
            if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
                if minas[coo2[0]][coo2[1]] == 1:
                    counter += 1
        for i in range(2):
            coo2[1] -= 1
            if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
                if minas[coo2[0]][coo2[1]] == 1:
                    counter += 1
        coo2[0] -= 1
        if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
            if minas[coo2[0]][coo2[1]] == 1:
                counter += 1
        return counter

    # Window execution

    while True:
        events, values = win1.read()

        if events == sg.WIN_CLOSED:
            break
        if events == 'Start':
            condition1 = True
            break

    win1.close()

    # Window 2

    l2 = []

    for i in range(10):
        l2.append([])

    for i in range(10):
        for y in range(10):
            l2[i] = []

    for i in range(10):
        for y in range(10):
            l2[i].append(sg.Button('?', button_color = 'yellow green', size=(6, 3), pad = (2 , 2), key = (str(i) + str(y))))
    
    l2.append([sg.Text('', key='clock', font=('Franklin Gothic Book', 14), text_color='black')])

    l1_1 = [[sg.Text('Difficulty:', font=('Franklin Gothic Book', 14, 'bold'), text_color='gold')],
    [sg.Combo(values=['Easy', 'Medium', 'Hard'], default_value='Easy', key='dif')],
    [sg.Button('Start Game')]]

    win1_1 = sg.Window('Minesweeper', l1_1)


    # Difficulty things i guess

    if condition1:

        while True:
            events, values = win1_1.read()

            if events == sg.WIN_CLOSED:
                break

            if events == 'Start Game':
                if values['dif'] == 'Easy':
                    mines = 15
                elif values['dif'] == 'Medium':
                    mines = 18
                else:
                    mines = 21
                condition2 = True
                break

    if condition2:

        # Random mines, how dangerous

        minas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        y = 0

        while (y < mines):
            coo = [random.randint(0, 9), random.randint(0, 9)]
            if minas[coo[0]][coo[1]] == 0:
                minas[coo[0]][coo[1]] = 1
                y += 1

        print(minas)

        win2 = sg.Window('Minesweeper', l2, finalize = True)

        # Right mouse button

        for i in range(100):
                if i < 10:
                    y = '0' + str(i)
                else:
                    y = str(i)

                win2[y].bind('<Button-3>', '-right')

        # Timely timers

        current_time = 0
        start_time = time_int()
        win1_1.close()

        # Window 2 execution

        while True:

            events, values = win2.read(timeout=10)

            # Timer stuff

            current_time = time_int() - start_time
            win2['clock'].update('{:02d}:{:02d}:{:02d}'.format(((current_time // 100) // 60),
                                                        (current_time // 100) // 60,
                                                        (current_time // 100) % 60,
                                                        current_time % 100))

            if  events == sg.WIN_CLOSED:
                break

            # Mine verification stuff

            for i in range(100):
                if i < 10:
                    y = '0' + str(i)
                else:
                    y = str(i)
            
                if events == y:
                    coo = [int(y[0]), int(y[1])]
                    if minas[coo[0]][coo[1]] == 1:
                        win2[y].update(str('X'), button_color=('white','red'))
                        stop = True
                        break
                    else:
                        win2[y].update(str(radar()), button_color=('white','rosy brown'), disabled=True, disabled_button_color=('dark blue', 'black'))
                        win2[y].unbind('<Button-3>')
                        holes += 1

                    # Winner winner chicken dinner

                    if holes == 100 - mines:
                        winner = True
                        break
                
                # Red flags. Lots of them
                
                if events == y + '-right':
                    if win2[y].ButtonText != '🚩':
                        win2[y].update('🚩', button_color=('red', 'yellow green'))
                    else:
                       win2[y].update('?', button_color=('white','yellow green'))


            if stop:
                break

            if winner:
                break

    # Big L
    if stop:
        sg.Popup('You Lost!')
        win2.close()
        Order66()

    # Win Window

    l4 = [[sg.Text('You Won!')], [sg.Button('Restart')]]
    win4 = sg.Window('Minesweeper', l4)

    # Win Window execution
    if winner:
        while True:
            events, values = win4.read()
        
            if events == sg.WIN_CLOSED:
                break

            if events == 'Restart':
                restart = True
                break
            
    
    # Restart? Addict.
    
    if restart:
        restart = False
        win2.close()
        win4.close()
        Order66()

# Execute order 66

Order66()