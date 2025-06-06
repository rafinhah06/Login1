import random
import PySimpleGUI as sg
import os

class Passgen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
            sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email/Usuário', size=(10, 1)),
            sg.Input(key='usuário', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'),
            sg.Combo(values=list(range(30)), key='total_chars', default_value=30, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        self.window = sg.Window('Pasword Generator', layout)
    
    def Iniciar(self):
        while True:
            evento, valores = self.window.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senhar(nova_senha,valores)
    
    def gerar_senha(self, valores):
        char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&'
        chars =  random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    
    def salvar_senhar(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site:{valores['site']}, usuario: {valores['usuário']}, senha: {nova_senha}\n"
                )
        print('Arquivo Salvo')

gen = Passgen()
gen.Iniciar()