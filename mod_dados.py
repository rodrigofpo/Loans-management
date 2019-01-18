import pickle
from datetime import datetime

try:
    with open('dadosEmprestimos.bin', 'rb') as ler:
        emprestimos = pickle.load(ler)
except Exception:
    emprestimos = []


def cadastrar():

    print("Insira as informações da pessoa, para quem foi feito o emprestimo.")
    nome = input("Nome completo: ")
    telefone = input("Telefone fixo: ")
    celular = input("Telefone celular: ")
    email = input("E-mail: ")
    vivencia = input("De onde conhece o emprestador: ")
    item = input("Item emprestado: ")
    data = input("Data do emprestimo. \nex: dia/mês/ano\n>")
    data = datetime.strptime(data, '%d/%m/%Y')

    emprestimo = {'nome': nome, 'telefone': telefone, 'celular': celular, 'email': email, 'vivencia': vivencia,
                  'item': item, 'data': data}

    emprestimos.append(emprestimo)
    gravar_dados()


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
