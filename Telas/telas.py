import Modules as mod
import PySimpleGUI as sg
from datetime import datetime

"""
Módulo contento as telas adicionais do programa.
"""

def tela_cadastro():
    """
    Tela para cadastro de novo emprestimo.
    :return: uma lista contento as informações inputadas.
    """
    layout = [
                [sg.Text("Cadastrar emprestimo")],
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
    janela = sg.Window("Cadastro", disable_close=True).Layout(layout)
    botao, valores = janela.Read()
    if botao == "Cadastrar":
        janela.Close()
        return valores
    elif botao == 'Cancelar':
        janela.Close()


def tela_atualizacao(informacao_antiga):
    """
    Tela para atualizar informações de um emprestimo já cadastrado.
    :param informacao_antiga: um dicionário contento todas as antigas informações do emprestimo.
    :return: uma lista de valores, contento o conteúdo dos InputText.
    """
    layout = [
        [sg.Text("Atualizar emprestimo")],
        [sg.Text("Nome", size=(15, 1)), sg.InputText(default_text=informacao_antiga['nome'], do_not_clear=True)],
        [sg.Text("Telefone Fixo", size=(15, 1)), sg.InputText(default_text=informacao_antiga['telefone'], do_not_clear=True)],
        [sg.Text("Celular", size=(15, 1)), sg.InputText(default_text=informacao_antiga['celular'], do_not_clear=True)],
        [sg.Text("E-mail", size=(15, 1)), sg.InputText(default_text=informacao_antiga['email'], do_not_clear=True)],
        [sg.Text("De onde conhece", size=(15, 1)), sg.InputText(default_text=informacao_antiga['vivencia'], do_not_clear=True)],
        [sg.Text("Data", size=(15, 1)), sg.InputText(default_text=informacao_antiga['data'].strftime("%d/%m/%Y"), do_not_clear=True)],
        [sg.Text("Item", size=(15, 1)), sg.InputText(default_text=informacao_antiga['item'], do_not_clear=True)],
        [sg.Button("Atualizar", button_color=('white', 'springgreen4')),
         sg.Cancel(button_text="Cancelar", button_color=('white', 'firebrick3'))]
    ]
    janela = sg.Window("Cadastro").Layout(layout)
    botao, valores = janela.Read()
    print(valores)
    if botao == "Atualizar":
        janela.Close()
        return valores
    elif botao == 'Cancelar':
        janela.Close()


def tela_escolha_busca():
    """
    Tela na qual o usuário escolhera qual o método de busca.
    :return: retorna uma string, sendo a escolha do usuário.
    """
    layout_busca = [[sg.T("Deseja buscar por:", size=(30, 1))],
                    [sg.Button("Nome", button_color=('white', 'springgreen4'), size=(8, 1)),
                     sg.Button("Item", button_color=('white', 'springgreen4'), size=(8, 1)),
                     sg.Button("Ano", button_color=('white', 'springgreen4'), size=(8, 1)),
                     sg.Button("Mes + Ano", button_color=('white', 'springgreen4'), size=(15, 1))],
                    [sg.Button("Cancelar", button_color=('white', 'firebrick3'), size=(8, 1), pad=(150, 1))]]
    janela_busca = sg.Window("Buscas", size=(450, 150), text_justification=('center')).Layout(layout_busca)
    botao_busca, valores_busca = janela_busca.Read()
    janela_busca.Close()
    return botao_busca

def tela_busca(botao):
    """
    tela na qual será informado o que o usuário deseja pesquisar.
    :param botao: uma string, que informará qual o método de busca.
    :return: retorna dado informado pelo usuário, que será usado em uma função de busca.
    """
    if botao == 'Nome':
        layout_nome = [[sg.T("Qual nome deseja buscar?", size=(30,1))],
                       [sg.In(size=(30,1)), sg.Button("Buscar")]]
        janela_nome = sg.Window("Busca Nome", size=(370,100)).Layout(layout_nome)
        buscar, nome = janela_nome.Read()
        janela_nome.Close()
        return nome[0]
    if botao == 'Item':
        layout_item = [[sg.T("Qual item deseja buscar?", size=(30,1))],
                       [sg.In(size=(30,1)), sg.Button("Buscar")]]
        janela_item = sg.Window("Busca Item", size=(370,100)).Layout(layout_item)
        buscar, item = janela_item.Read()
        janela_item.Close()
        return item[0]
    if botao == 'Ano':
        layout_mes = [[sg.T("Qual ano deseja buscar?", size=(30,1))],
                       [sg.In(size=(30, 1)), sg.Button("Buscar")]]
        janela_mes = sg.Window("Busca Ano", size=(370, 100)).Layout(layout_mes)
        buscar, mes = janela_mes.Read()
        try:
            mes = datetime.strptime(mes[0], '%Y').date().year
        except TypeError and ValueError:
            janela_mes.Close()
            return sg.Popup("Erro na Busca", button_color=('white', 'springgreen4'))
        janela_mes.Close()
        return mes
    if botao == 'Mes + Ano':
        layout_mes_ano = [[sg.T("Qual mes e ano deseja buscar?", size=(30,1))],
                       [sg.In("Ex: 10/2018", size=(30, 1)), sg.Button("Buscar")]]
        janela_mes_ano = sg.Window("Busca Mes", size=(370, 100)).Layout(layout_mes_ano)
        buscar, mes_ano = janela_mes_ano.Read()
        try:
            mes_ano = datetime.strptime(mes_ano[0], '%m/%Y').date()
        except TypeError and ValueError:
            janela_mes_ano.Close()
            return sg.Popup("Erro na Busca", button_color=('white', 'springgreen4'))
        janela_mes_ano.Close()
        return mes_ano
    if botao == 'Cancelar':
        return 0

def tela_excluir():
    """
    Tela para confirmação da exclusão de um emprestimo.
    :return: um valor booleano, para confirmação ou negação da ação.
    """
    layout = [[sg.Text('Tem certeza que deseja excluir?')],
              [sg.Button("Sim", size=(8,1), button_color=('white', 'springgreen4'), pad=(20,1)),
               sg.Button("Não", size=(8,1), button_color=('white', 'firebrick3'))]]
    janela = sg.Window('Excluir').Layout(layout)
    botao, evento = janela.Read()
    if botao == 'Sim':
        janela.Close()
        return True
    else:
        janela.Close()
        return False
