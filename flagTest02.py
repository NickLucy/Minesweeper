# Importação das bibliotecas

import PySimpleGUI as sg
import random
import time
from PIL import Image

#Time Function

def time_int():
    return int(round(time.time() * 100))


# Execute order 66

def Order66():

    # Criação da Primeira Janela

    sg.theme('DarkGreen')
    l1 = [[sg.Text('Campo Minado', font=('Times New Roman', 14, 'bold'), text_color='darkBlue')],
    [sg.Button('Iniciar')]]
    win1 = sg.Window('Campo Minado', l1)

    # Variável de transição

    condition1 = False
    condition2 = False
    stop = False
    winner = False
    restart = False

    # Variáveis do jogo

    holes = 0
    mines = 0
    coo = []

    # Criação da função de radar de bombas

    def radar():
        coo2 = coo
        contador = 0
        coo2[0] -= 1
        coo[1] -= 1
        if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
            if minas[coo2[0]][coo2[1]] == 1:
                contador += 1
        for i in range(2):
            coo2[1] += 1
            if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
                if minas[coo2[0]][coo2[1]] == 1:
                    contador += 1
        for i in range(2):
            coo2[0] += 1
            if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
                if minas[coo2[0]][coo2[1]] == 1:
                    contador += 1
        for i in range(2):
            coo2[1] -= 1
            if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
                if minas[coo2[0]][coo2[1]] == 1:
                    contador += 1
        coo2[0] -= 1
        if coo[0] >= 0 and coo[1] >= 0 and coo[0] < 10 and coo[1] < 10:
            if minas[coo2[0]][coo2[1]] == 1:
                contador += 1
        return contador

    # Execução da primeira janela

    while True:
        events, values = win1.read()

        if events == sg.WIN_CLOSED:
            break
        if events == 'Iniciar':
            condition1 = True
            break

    win1.close()

    # Criação da Segunda Janela

    l2 = []

    for i in range(10):
        l2.append([])

    for i in range(10):
        for y in range(10):
            l2[i] = []

    for i in range(10):
        for y in range(10):
            l2[i].append(sg.Button('?', size=(5, 3), pad = (2 , 2), key = (str(i) + str(y))))
    
    l2.append([sg.Text('', key='clock', font=('Times New Roman', 14), text_color='black')])

    l1_1 = [[sg.Text('Difficulty:', font=('Times New Roman', 14), text_color='black')],
    [sg.Combo(values=['Easy', 'Medium', 'Hard'], default_value='Easy', key='dif')],
    [sg.Button('Iniciar Jogo')]]

    win1_1 = sg.Window('Campo Minado', l1_1)


    # Execução da janela da dificuldade
    ## Se e somente se, a transição for verdadeira

    if condition1:

        while True:
            events, values = win1_1.read()

            if events == sg.WIN_CLOSED:
                break

            if events == 'Iniciar Jogo':
                if values['dif'] == 'Fácil':
                    mines = 15
                elif values['dif'] == 'Médio':
                    mines = 18
                else:
                    mines = 21
                condition2 = True
                break

    if condition2:

        # Randomização da posição das minas

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

        win2 = sg.Window('Campo Minado', l2, finalize = True)

        # Inicialização da função do botão direito

        for i in range(100):
                if i < 10:
                    y = '0' + str(i)
                else:
                    y = str(i)

                win2[y].bind('<Button-3>', '-right')

        #Inicialização do timer

        current_time = 0
        start_time = time_int()
        win1_1.close()

        # Execução da segunda janela
        ## Se e somente se, a transição for verdadeira

        while True:

            events, values = win2.read(timeout=10)

            #Função constante do timer

            current_time = time_int() - start_time
            #win2['clock'].update('{:02d}:{:02d}:{:02d}:{:02d}'.format(((current_time // 100) // 60) // 60,
            #                                            (current_time // 100) // 60 % 60,
            #                                            (current_time // 100) % 60,
            #                                            current_time % 100))
            win2['clock'].update('{:02d}:{:02d}:{:02d}'.format(((current_time // 100) // 60),
                                                        (current_time // 100) // 60,
                                                        (current_time // 100) % 60,
                                                        current_time % 100))

            if  events == sg.WIN_CLOSED:
                break

            # Verificação minar

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

                    #Verificação de fim de jogo

                    if holes == 100 - mines:
                        winner = True
                        break
                
                #Verificação da bandeira
                
                
                if events == y + '-right':
                    #im = Image.open("flag.png")
                    if not win2[y].ButtonText == sg.Image('flag.png', size=(300,300)):
                        
                        win2[y].update(sg.Image('flag.png', size=(10,10)), button_color=('red', 'light green'))
                    else:
                        win2[y].update('?', button_color=('black','white'))


            if stop:
                break

            if winner:
                break

    # Popup do perdedor
    if stop:
        sg.Popup('Você perdeu!')
        win2.close()
        Order66()

    # Criação da janela do vencedor

    l4 = [[sg.Text('Você ganhou! Meus parabéns')], [sg.Button('Reiniciar')]]
    win4 = sg.Window('Campo Minado', l4)

    # Execução da janela do vencedor
    if winner:
        while True:
            events, values = win4.read()
        
            if events == sg.WIN_CLOSED:
                break

            if events == 'Reiniciar':
                restart = True
                break
            
    
    # Restart do game
    
    if restart:
        restart = False
        win2.close()
        win4.close()
        Order66()

# Iniciando o jogo

Order66()