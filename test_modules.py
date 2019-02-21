from Modules import *


def test_cadastro():
    assert cadastrar(['Rômulo', '32820388', '992705412', 'romulo.sa153@live.com', 'Casa', '10/12/2018', 'Celular']) == 0


def test_listar_emprestimos():
    assert len(listar_emprestimos()) == len(EMPRESTIMOS)


def test_buscar_nome():
    resultado = buscar_nome('Rômulo')
    assert 'Rômulo' in resultado['nome']


def test_gravar_dados():
    assert gravar_dados() == 0


def test_ler_dados():
    assert ler_dados() == 0


def test_exluir_emprestimo():
    assert exlcuir_emprestimo(EMPRESTIMOS[0]) == 0


def test_editar_emprestimo():
    assert editar_emprestimo('Rômulo', ['Rômulo', '32820388', '992705412', 'romulo.sa153@live.com', 'Casa', '10/12/2018', 'Celular']) == 0


def test_get_informacoes(mes = '', ano = '', item = '', nome = ''):
    assert type(get_informacoes()) == list


