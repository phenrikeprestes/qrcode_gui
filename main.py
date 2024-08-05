import PySimpleGUI as sg
import qrcode
from PIL import Image
import io

# Função para gerar o QR Code
def gerar_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Função para criar a janela que exibe o QR Code
def mostrar_qr_code(img):
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    layout = [
        [sg.Image(data=bio.getvalue())],
        [sg.Button('Close')]
    ]
    window = sg.Window('QR Code Generate', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break
    window.close()

# Definindo o layout da interface principal
layout = [
    [sg.Text('QR Code Generator', font=('Helvetica', 16), text_color='black', background_color='gray')],
    [sg.Text('Type the ext or URL:', background_color='gray', text_color='black')],
    [sg.InputText(key='input_data')],
    [sg.Button('QR Code Gen', button_color=('black', 'gray')), sg.Button('Exit', button_color=('black', 'gray'))]
]

# Criando a janela principal
window = sg.Window('Gerador de QR Code', layout, background_color='gray')

# Loop de eventos da janela principal
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'QR Code Gen':
        data = values['input_data']
        if data:
            img = gerar_qr_code(data)
            mostrar_qr_code(img)

# Fechando a janela principal
window.close()
