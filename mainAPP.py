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
    - Victor Manuel - victor.vsantos08@gmail.com - 2018005118
    - Willian Lucas - willamlucas@gmail.com - 2018001709


4 -Modulos que compoe o software: descrever a funçao de cada arquivo adicional que compoe o software
    - modules.py: Esse modulo fornece todas funções para salvar e ler (os dados da aplicação em arquivo,
     usando a biblioteca Pickle), cadastrar, listar cadastros, buscar por nome, ano e mes + ano(usando dicionario
     e modulo datetime ).
    - PySimpleGUI: framework para a parte gráfica do projeto
    - Telas.telas: módulo contendo as demais telas do programa
'''

#aqui começa o software ...
import Telas.telas as tela
import Modules as mod
import PySimpleGUI as sg

NOMES = mod.get_nomes()
coluna_detalhes = [[sg.Text("Loans-Management", size=(30,1))],
                   [sg.Text('', key='nome', size=(30, 1), pad=(1,5))],
                   [sg.Text('', key='telefone', size=(30, 1), pad=(1,8))],
                   [sg.Text('', key='celular', size=(30, 1), pad=(1,8))],
                   [sg.Text('', key='email', size=(30, 1), pad=(1,8))],
                   [sg.Text('', key='vivencia', size=(30, 1), pad=(1,8))],
                   [sg.Text('', key='data', size=(30, 1), pad=(1,8))],
                   [sg.Text('', key='item', size=(30, 1), pad=(1,8))],
                   [sg.Button("Editar", size=(8,1), button_color=('white', 'springgreen4'), pad=(10,20)),
                    sg.Button("Apagar", size=(8,1), pad=(50,1), button_color=('white', 'springgreen4'))]]

coluna_nomes = [[sg.Listbox(values= NOMES, key='lista', change_submits=True, size=(90, 25))]]

tela_principal = [[sg.In(size=(30,1)), sg.Button('Buscar', size=(8,1))],
                  [sg.Column(coluna_detalhes), sg.Column(coluna_nomes, size=(90,300))],
                  [sg.Button("Cadastrar",button_color=('white', 'springgreen4'))]]

janela = sg.Window("Loans-Management", size=(550, 450), text_justification=('center')).Layout(tela_principal)

while True:
    evento, valores = janela.Read()
    if evento == 'lista':
        try:
            nome = valores['lista'][0]
            emprestimo = mod.buscar_nome(nome)
            nome = "Nome: " + emprestimo['nome']
            telefone = "Telefone: " + emprestimo['telefone']
            celular = "Celular: " + emprestimo['celular']
            email = "E-mail: " + emprestimo['email']
            vivencia = "Vivencia: " + emprestimo['vivencia']
            data = "Data: " + emprestimo['data'].strftime("%d/%m/%Y")
            item = "Item: " + emprestimo['item']

            janela.FindElement('nome').Update(nome)
            janela.FindElement('telefone').Update(telefone)
            janela.FindElement('celular').Update(celular)
            janela.FindElement('data').Update(data)
            janela.FindElement('item').Update(item)
            janela.FindElement('email').Update(email)
            janela.FindElement('vivencia').Update(vivencia)
        except IndexError:
            pass
    if evento == 'Cadastrar':
        cadastro = tela.tela_cadastro()
        if type(cadastro) == list:
            mod.cadastrar(cadastro)
            NOMES = mod.get_nomes()
            janela.FindElement('lista').Update(NOMES)

    elif evento == 'Editar':
        emprestimo = mod.buscar_nome(valores['lista'][0])
        novos_dados = tela.tela_atualizacao(emprestimo)
        atualizacao = mod.editar_emprestimo(valores['lista'][0], novos_dados)
        sg.Popup("Atulizado com sucesso", button_color=('white', 'springgreen4'))
        NOMES = mod.get_nomes()
        janela.FindElement('lista').Update(NOMES)

    elif evento == 'Apagar':
        confirmar = tela.tela_excluir()
        if confirmar:
            mod.exlcuir_emprestimo(valores['lista'][0])
            NOMES = mod.get_nomes()
            janela.FindElement('lista').Update(NOMES)
    elif evento is None or evento == 'Cancelar':
        break
