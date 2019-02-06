'''
Projeto de software - Tecnicas de programacao II

1- Descriçao do projeto :
    - Cria e armazena cadastros de comodatos para um usuario a fim.

2- Data: data em que o projeto foi feito

3- Equipe:
    - Diego Caiena - dio141@outlook.com - 2018001914
    - Fabricio Cordeiro - fabriciojose3263@outlook.com - 2018004578
    - Rodrigo Oliveira - rodrigopantoja17@yahoo.com - 2018004710
    - Rômulo Sá - romulo.sa153@live.com - 2018001674
    - Victor Manuel - victor.vsantos08@gmail.com -2018005118
    - Willian Lucas - willamlucas@gmail.com -2018001709


4 -Modulos que compoe o software: descrever a funçao de cada arquivo adicional que compoe o software
    - Modules.py: Esse modulo fornece todas funções para salvar e ler (os dados da aplicação em arquivo,
     usando a biblioteca Pickle), cadastrar, listar cadastros, buscar por nome, ano e mes + ano(usando dicionario e modulo datetime ),

    - Cadastrar
'''



#aqui começa o software ...
import Modules as mod
import PySimpleGUI as sg

tab1_layout =  [[sg.Text("Cadastrar emprestimo")],
                [sg.Text("Nome", size=(15, 1)), sg.InputText()],
                [sg.Text("Telefone Fixo", size=(15, 1)), sg.InputText()],
                [sg.Text("Celular", size=(15,1)), sg.InputText()],
                [sg.Text("E-mail", size=(15,1)), sg.InputText()],
                [sg.Text("De onde conhece", size=(15,1)), sg.InputText()],
                [sg.Text("Data", size=(15,1)), sg.InputText("ex: dia/mês/ano", do_not_clear=False)],
                [sg.Text("Item", size=(15,1)), sg.InputText()],
                [sg.Button("Cadastrar",button_color=('white', 'springgreen4')),
                 sg.Cancel(button_text="Cancelar",button_color=('white', 'firebrick3'))]
                ]

tab2_layout = []

layout = [[sg.TabGroup([[sg.Tab('Cadastrar', tab1_layout, ),
                         sg.Tab('Cadastros', tab2_layout)]], )]]

window = sg.Window('Loans Manangement', default_element_size=(32,1)).Layout(layout)

while True:
    botao, valores = window.Read()
    print(botao,valores)
    if botao == 'Cadastrar':
        mod.cadastrar(valores)
    elif botao is None:
        break

