import PySimpleGUI as sg

# Criando o layout
def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]
    return sg.Window('Todo List', layout, finalize=True)

# Criar a janela
janela = criar_janela_inicial()

# Criar as regras dessa janela
while True:
    event, valores = janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
