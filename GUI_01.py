from turtle import delay
import PySimpleGUI as sg

layout1 = [
    [sg.Text("Informe um valor")],
    [sg.InputText(key="numero"), sg.InputText(key="yeet")],
    [sg.Button("Antecessor/Sucessor"),sg.Button("Cancel"),sg.Button("Morbin")],
    [sg.Text("bingus",key="antecessor")],
    [sg.Image('flag.png')],
]
layout2 = [
    [sg.Text("Informe um valor")],
    [sg.InputText(key="numero")],
    [sg.Button("Ant/Suc"),sg.Button("Cancel")],
    [sg.Text("",key="antecessor")],
    [sg.Text("",key="sucessor")],
]

janela = sg.Window("Exercicio 1",layout1,)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancel":
        break

    

    if evento == "Antecessor/Sucessor":
        print("Sus")
        numero = int(valores["numero"])
        ant = numero - 1
        suc = numero + 1
        janela["antecessor"].update(f"Antecessor: {ant}")
        janela["sucessor"].update(f"Sucessor: {suc}")
    if evento == "Morbin":
        print("Morb")
        numero = int(valores["numero"])
        yeet = int(valores["yeet"])
        twi = numero * yeet
        div = numero / yeet
        janela["antecessor"].update(f"Multiply: {twi}")
        janela["sucessor"].update(f"Divide: {div}")

janela.close()