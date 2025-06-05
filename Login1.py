import PySimpleGUI as sg

# Layout
sg.theme('Reddit') 
layout = [
    [sg.Text('Usúario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Rafael' and valores['senha'] == '123456':
            sg.popup('Bem-Vindo ao Programa!')
        else:
            sg.popup_error('Usuário ou Senha Inválidos')
