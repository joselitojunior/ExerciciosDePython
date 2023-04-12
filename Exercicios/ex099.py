from time import sleep

vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def linha_():
    print(branco+'-' * 50)


def linha__():
    print(branco+'=' * 50)


def maior(* num):
    qnt = 0
    maior_valor = 0
    for valor in num:
        qnt += 1
        if valor > maior_valor:
            maior_valor = valor
    linha_()
    print(f'{branco}Analisando os valores: {azul}{num}{branco}', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.')
    sleep(0.8)
    print(f'\n{branco}Quantidade de valores: {ciano}{qnt}')
    print(f'{branco}Maior valor: {amarelo}{maior_valor}')
    linha_()


linha__()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
linha__()
