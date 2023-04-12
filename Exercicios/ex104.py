vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def leiaInt(n):
    while n.isnumeric() == False:
        print(f'\n{vermelho}ESCREVA UM NÚMERO INTEIRO!')
        n = str(input(f'{branco}> '))
    n = int(n)
    return n

def linha_():
    print(branco+'-' * 50)


def linha__():
    print(branco+'=' * 50)


linha__()
nmr = leiaInt(str(input(f'{branco}Digite um número inteiro: ')))
print(f'\n{branco}Você digitou o número: {azul}{nmr}{branco}.')
linha__()