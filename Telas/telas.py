import modules as mod
import PySimpleGUI as sg


def tela_cadastro():
    return [
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
