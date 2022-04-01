from PySimpleGUI import PySimpleGUI as sg

#Layout Janelas

def janela_entrada():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuário'), sg.Input(key='Usuário', size=(30,2))],
        [sg.Text('Senha  '), sg.Input(key='Senha',password_char='*', size=(30,2))],
        [sg.Button('Entrar')]
    ]
    return sg.Window('LOGIN AZAKI BRASIL', layout=layout, finalize=True)

def janela_escolha():
    sg.theme('Reddit')
    layout = [
        [sg.Checkbox('CADASTRAR', key='1'), sg.Checkbox('CONSULTAR', key='2', size=(10,2))],
        [sg.Button('Voltar'), sg.Button('OK')]
        ]
    return sg.Window('SELECIONE ', layout=layout, finalize=True)

#JANELAS

janela1,janela2 = janela_entrada(), None


#Loop
while True:


    window,events,values = sg.read_all_windows()

         #Fechar Janela
    if window == janela1 and events == sg.WIN_CLOSED:
        break
    if window == janela2 and events == sg.WIN_CLOSED:
        break

        #Nova Janela
    if window == janela1 and events == 'Entrar':
        if values['Usuário'] == 'AZAKI BRASIL' and values['Senha'] == '123':
            sg.popup('SEJA BEM-VINDO AO ALMOXARIFADO!')
            janela2 = janela_escolha()
            janela1.hide()
        else:
            sg.popup('DADOS INCORRETOS')
    if window  == janela2 and events == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and events == 'OK':
        if values['1'] == True and values['2'] == True:
            sg.popup('Você só pode executar uma ação por vez!')
        elif values['1'] == True:
            sg.popup('Você Escolheu a OPÇÃO Cadastrar')
        elif values['2'] == True:
            sg.popup('Você Escolheu a Consultar')











