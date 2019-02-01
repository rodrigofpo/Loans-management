import pickle
from datetime import datetime
import PySimpleGUI as sg
try:
    with open('dadosEmprestimos.bin', 'rb') as ler:
        emprestimos = pickle.load(ler)
except Exception:
    emprestimos = []

"""
A função 'cadastrar' vai receber os inputs do arquivo tela, da função 'tela_cadastrar' e adicionar seus valores em um
dicionário, e depois adicionar esse dicionário à lista global de emprestimo
"""
def cadastrar(informacoes):
    try:
        nome = informacoes[0]
        telefone = informacoes[1]
        celular = informacoes[2]
        email = informacoes[3]
        vivencia = informacoes[4]
        data = informacoes[5]
        item = informacoes[6]
        data = datetime.strptime(data, '%d/%m/%Y').date()
        data = datetime.today().date()
        emprestimo = {'nome': nome, 'telefone': telefone, 'celular': celular, 'email': email, 'vivencia': vivencia,
                      'item': item, 'data': data}
        emprestimos.append(emprestimo)
        gravar_dados()
        sg.Popup("Cadastro realizado com sucesso!", button_color=('white', 'springgreen4'))
    except ValueError:#Tratamendo de erro, caso o usuário informe a data em um formato não aceito
        sg.Popup("Falha no cadastro!", button_color=('white', 'springgreen4'))

def gravar_dados():
    with open('dadosEmprestimos.bin', 'wb') as fgravar:
        pickle.dump(emprestimos, fgravar)


def ler_dados():
    try:
        with open('dadosEmprestimos.bin', 'rb') as ler:
            global emprestimos
            emprestimos = pickle.load(ler)
    except Exception:
        pass
