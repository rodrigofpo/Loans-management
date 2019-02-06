import pickle
import PySimpleGUI as sg
from datetime import datetime
from operator import itemgetter

try:
    with open('dadosEmprestimos.bin', 'rb') as ler:
        emprestimos = pickle.load(ler)
except Exception:
    emprestimos = []


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

        emprestimo = {'nome': nome, 'telefone': telefone, 'celular': celular, 'email': email, 'vivencia': vivencia,
                      'item': item, 'data': data}

        emprestimos.append(emprestimo)
        emprestimos.sort(key=itemgetter('data'))
        gravar_dados()
        sg.Popup("Cadastro realizado com sucesso", button_color=('white', 'springgreen4'))
    except ValueError:
        sg.Popup("Erro no cadastro", button_color=('white', 'springgreen4'))

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

def key_func(data):
    return emprestimos[0]['data']
