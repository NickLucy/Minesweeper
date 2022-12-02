from PIL import Image, ImageTk
from urllib import request
import PySimpleGUI as sg


    

# Resize PNG file to size (300, 300)
size = (20, 20)
im = Image.open("flag.png")
im = im.resize(size, resample=Image.Resampling.BICUBIC)

sg.theme('DarkGreen3')

layout = [
    [sg.Image(size=(30, 30), key='-IMAGE-')],
]
window = sg.Window('Window Title', layout, margins=(0, 0), finalize=True)

# Convert im to ImageTk.PhotoImage after window finalized
image = ImageTk.PhotoImage(image=im)

# update image in sg.Image
window['-IMAGE-'].update(data=image)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()