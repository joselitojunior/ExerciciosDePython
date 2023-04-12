from cores import *


def linha_(t=50):
    print(branco + '-' * t)


def linha__(t=50):
    print(branco + '=' * t)


def menu():
    def opcao():
        while True:
            try:
                opc = int(input(f'{amarelo}Sua opção: '))
            except ValueError:
                print(f'\n{vermelho}Digite um número inteiro válido.')
                continue
            else:
                if opc == 1 or opc == 2 or opc == 3:
                    return opc
                else:
                    print(f'\n{vermelho}Digite um número de 1 à 3.')
    linha__()
    print(f'{branco}{"MENU PRINCIPAL":^50}')
    linha_()
    print(f'{amarelo}1- {azul}Ver pessoas cadastradas'
          f'\n{amarelo}2- {azul}Cadastrar pessoa'
          f'\n{amarelo}3- {azul}Sair')
    linha_()
    o = opcao()
    linha__()
    return o
