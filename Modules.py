import pickle
import PySimpleGUI as sg
from datetime import datetime
from operator import itemgetter
from Telas.telas import *

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


def listar_emprestimos():
    for emprestimo in emprestimos:
        tela_informacoes(emprestimo)


def buscar_nome(nome):
    for emprestimo in emprestimos:
        if nome.lower() in emprestimo['nome'].lower():
            return emprestimo


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

#auxiliares
def printar_aux(emprestimo):
    print("Nome:", emprestimo['nome'])
    print("Telefone:", emprestimo['telefone'])
    print("Celular:", emprestimo['celular'])
    print("E-mail:", emprestimo['email'])
    print("De onde conheço:", emprestimo['vivencia'])
    print("Data:", emprestimo['data'].strftime("%d/%m/%Y"))
    print("Item:", emprestimo['item'])


def exlcuir_emprestimo(emprestimo):
    emprestimos.remove(emprestimo)