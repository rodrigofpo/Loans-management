import Modules as mod
import PySimpleGUI as sg


def tela_cadastro():
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
    janela = sg.Window("Cadastro").Layout(layout)
    botao, valores = janela.Read()
    if botao == "Cadastrar":
        janela.Close()
        return valores
    elif botao == 'Cancelar':
        janela.Close()


def tela_atualizacao(informacao_antiga):
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


def tela_informacoes(emprestimo):
    return [
                [sg.Text(emprestimo['nome'], size=(20, 1))],
                [sg.Text(emprestimo['telefone'], size=(20, 1))],
                [sg.Text(emprestimo['celular'], size=(20,1))],
                [sg.Text(emprestimo['email'], size=(20,1))],
                [sg.Text(emprestimo['vivencia'], size=(20,1))],
                [sg.Text(emprestimo['data'], size=(20,1))],
                [sg.Text(emprestimo['item'], size=(20,1))],
        [sg.Button("Excluir",button_color=('white', 'firebrick3'),pad=(60,0))]
            ]


def tela_busca():
    return [[sg.T("Por qual nome você deseja buscar?",justification='center',pad=(70,0))],
            [sg.In(justification='center',pad=(60,0))],
            [sg.Button("Buscar", button_color=('white', 'springgreen4'),pad=(150,0))]]


def tela_excluir():
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