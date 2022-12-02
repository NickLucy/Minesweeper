import PySimpleGUI as sg
from io import BytesIO
import base64
from PIL import Image

flag = b'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'
layout = [[sg.Text('Base64 Button Demo')],
          [sg.Button(image_data=flag,
                     button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='Exit')]]
window = sg.Window('Flowers!', layout, no_titlebar=True)
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()