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
    - Victor Manuel - victor.vsantos08@gmail.com -2018005118
    - Willian Lucas - willamlucas@gmail.com -2018001709


4 -Modulos que compoe o software: descrever a funçao de cada arquivo adicional que compoe o software
    - modules.py: Esse modulo fornece todas funções para salvar e ler (os dados da aplicação em arquivo,
     usando a biblioteca Pickle), cadastrar, listar cadastros, buscar por nome, ano e mes + ano(usando dicionario
     e modulo datetime ).
'''

#aqui começa o software ...
from Telas.telas import *

cadastro = tela_cadastro()

busca = tela_busca()

layout = [[sg.TabGroup([[sg.Tab('Cadastrar', cadastro),
                         sg.Tab('Buscar', busca)]])]
          ]

window = sg.Window('Loans Manangement', default_element_size=(32,1)).Layout(layout)


while True:
    botao, valores = window.Read()
    print(botao,valores)
    if botao == 'Cadastrar':
        mod.cadastrar(valores)

    elif botao == 'Buscar':
        resultado = mod.buscar_nome(valores[0])
        janela_resultado = sg.Window("Loans Manangement").Layout(tela_informacoes(resultado))
        botao_busca,valores_busca = janela_resultado.Read()
        if botao_busca == 'Excluir':
            mod.exlcuir_emprestimo(resultado)
            print(mod.EMPRESTIMOS)

    elif botao is None or botao == 'Cancelar':
        break

