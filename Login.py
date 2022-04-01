from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout =[
    [sg.Text('Usuário'), sg.Input(key='Usuário', size=(30,2))],
    [sg.Text('Senha  '), sg.Input(key='Senha',password_char='*', size=(30,2))],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('LOGIN AZAKI BRASIL', layout)
while True:

    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'AZAKI BRASIL' and valores['Senha'] == '12345':
            print('Seja Bem-Vindo!!')
        else:
            print('Erro!! Dados Incorretos.Tente novamente :(')



