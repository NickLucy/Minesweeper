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

    sg.theme('dark green 1')
    l1 = [[sg.Text('Campo Minado', font=('Times New Roman', 14, 'bold'), text_color='gold')],
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
            l2[i].append(sg.Button('?', button_color = 'yellow green', size=(6, 3), pad = (2 , 2), key = (str(i) + str(y))))
    
    l2.append([sg.Text('', key='clock', font=('Times New Roman', 14), text_color='black')])

    l1_1 = [[sg.Text('Difficulty:', font=('Times New Roman', 14, 'bold'), text_color='gold')],
    [sg.Combo(values=['Easy', 'Medium', 'Hard'], default_value='Easy', key='dif')],
    [sg.Button('Iniciar Jogo')]]

    win1_1 = sg.Window('minesweeper v???', l1_1)


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

        win2 = sg.Window('minesweeper v???', l2, finalize = True)

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
                    flag = b'iVBORw0KGgoAAAANSUhEUgAAADQAAAA0CAYAAADFeBvrAAAACXBIWXMAABJ0AAASdAHeZh94AAAD+UlEQVRo3u2YT0xcVRSHv3PfzDBNoQ2DrYIVF7JwYUzpwEChgk1bNax008a9fza6MK5MTNRNV65cmChTatsQtFpcmFZtU02ByAhMIZSoNDU2FTUiapA385g/7x4XYEJMKRgT+56Z3/a+t/jed+695zz4n0VutZg581S7QXbmpq+e2//apXIYgCLrLYyfefZQvEo+iUaMFJwds2eTu9Pic7JnauqXIAOZ9d3Z1LbqqKnbHpXY9tj9MTWvi2NufJrc8+751uYDr9zq3SAaslZE1jxUb32KIvGckSOeyuHOlj3fXoC+mMo73dnsT8E3dJPNFgfusMrd1kqtalNUOFp0uH4xlRy82JbsOQ1OYA1t9BVqVNlmlaJIzBV5wkMer0slv/8M6fN9PX4om70RGqC1qVIlDqiq5EUaXcOrxQgvf97ech6rvTU+Z1uy2VLgSm5T1lDqraVBNVKD9jhGBt2YXB/amzw60pG8L1RAa/daDKXOKrvUyg7VhirkJUVmhztaLwx3th6+2tRUFdiS2+hrVatSg1ICxxVzMKdycP7O2vkv7mo5JSX/2N4vJ78ODdDaxIA6VRKi5FV2usiLhWjkhdF9qRELaSmbDzoyGS9wJbcpayj1WHapNdvRrqhw0kTtXKYr9cbovuYHQ2HoZokCCSwJFfJCwsU875noc2NdqTFRercY970HLn3lBtrQegdJNVCvlkas1KJtjiHtsfWH8e62t7LdrS2hMLS+NSUB5GHbkugzHvJ09uHUlCPSu5zT/vaxsT8CbWi9bAXqUe4VlYTQ7AhvVlXLTPZgc0MogdaWUQKlESUG9zg29mSogf7KMuCDojofmj309/iACywhlFQKwIlFu2UgVEC6amMJIQ8qMGstfZGiObF7dHQ+NKdcGXAR3BUbeRH90Cnb3uaRiSFZ4Qz+sa2AByxh8ARFmXFE0+ppf2p8/NfQdAplIIewhMEXlgz6PpBuGx7PsEkbtx1IVy5LXDF4oCJcxmo6VrADLdnsYmi67RKQE8HF4MMiyABSTj80cjkbmnloxYbgGmEZVJQMaK+XK55+dHo6F5oBrwjkxJATQZEFlP6IaLpzdGImFD9JACzgiZAToSBYRIbApuPMD3Zk5rz/cp9G/rUNY8iLqMLPopxSK8cOTEzM3s6+7x/byK/aKAq+IBcFeou/LX7Uc+1aIQiN7KZSWD2pPCOq8KPAcZVy3yNj098FrTPfVGn9bpyyET5WX9Pxyclz+1fuxkCOGhvGScS/oVQ69NiVK3NB7843NQ+Z6uhCTwhgQjfgVYAqQBWgClAFqAJUAaoAVYAqQKFKZH1SLeaXfUpli6oWQw/kOsW3Nc+CwTgSYZhKbk/+BPabnPdmuunAAAAAAElFTkSuQmCC'
                    if not win2[y].ButtonText == flag:
                         win2[y].update(image_data=flag)

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

    l4 = [[sg.Text('You Won!')], [sg.Button('Reiniciar')]]
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