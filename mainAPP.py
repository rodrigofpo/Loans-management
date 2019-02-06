'''
Projeto de software - Tecnicas de programacao II

1- Descriçao do projeto : descrever o que o seu projeto faz


2- Data: data em que o projeto foi feito


3- Equipe: listar o nome - email - matricula dos alunos
- Fulano de tal  - Fulano@gmail.com - 201800123


4 -Modulos que compoe o software: descrever a funçao de cada arquivo
adicional que compoe o software

- arquivos.py : Esse modulo fornece as funções para salvar e ler
os dados da aplicação em arquivo usando a biblioteca picles

'''


#aqui começa o software ...
import pickle
from mod_dados import *
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

tab2_layout = [[sg.T('Empréstimos')],
               [sg.In(key='in')]]

layout = [[sg.TabGroup([[sg.Tab('Cadastrar', tab1_layout, ),
                         sg.Tab('Cadastros', tab2_layout)]], )]]

window = sg.Window('Loans Manangement', default_element_size=(12,1)).Layout(layout)    

while True:
    event, values = window.Read()
    print(event,values)
    if event is None:           # always,  always give a way out!
        break
    if botao == 'Cadastrar':
        cadastrar(valores)


