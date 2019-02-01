from mod_dados import *
import PySimpleGUI as sg

"""A função 'tela_cadastro' vai receber as informações do usuário"""
def tela_cadastro():
    layout = [
                [sg.Text("Cadastrar emprestimo")],
                [sg.Text("Nome", size=(15, 1)), sg.InputText()],
                [sg.Text("Telefone Fixo", size=(15, 1)), sg.InputText()],
                [sg.Text("Celular", size=(15, 1)), sg.InputText()],
                [sg.Text("E-mail", size=(15, 1)), sg.InputText()],
                [sg.Text("De onde conhece", size=(15, 1)), sg.InputText()],
                [sg.Text("Data", size=(15, 1)), sg.InputText("ex: dia/mês/ano", do_not_clear=False)],
                [sg.Text("Item", size=(15, 1)), sg.InputText()],
                [sg.Button("Cadastrar", button_color=('white', 'springgreen4')),
                 sg.Button("Cancelar", button_color=('white', 'firebrick3'))]
                ]

    janela = sg.Window("Teste").Layout(layout)
    botao, valores = janela.Read()

    if botao == 'Cadastrar':
        cadastrar(valores)#aqui os dados são repassadas para a função 'cadastrar' e adicionadas à lista global de emprestimos

    elif botao == 'Cancelar':
        janela.Close()
