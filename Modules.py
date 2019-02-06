import pickle
from datetime import datetime

try:
    with open('dadosEmprestimos.bin', 'rb') as ler:
        emprestimos = pickle.load(ler)
except Exception:
    emprestimos = []


def cadastrar(informacoes):

    nome = informacoes[0]
    telefone = informacoes[1]
    celular = informacoes[2]
    email = informacoes[3]
    vivencia = informacoes[4]
    data = informacoes[5]
    item = informacoes[6]
    data = datetime.strptime(data, '%d/%m/%Y')

    emprestimo = {'nome': nome, 'telefone': telefone, 'celular': celular, 'email': email, 'vivencia': vivencia,
                  'item': item, 'data': data}

    emprestimos.append(emprestimo)
    gravar_dados()
    print("Cadastro Salvo!")

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
