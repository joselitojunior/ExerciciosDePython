# PROGRAMA NÃO FUNCIONA PORQUE O PYCHARM TEM UM BUG NO QUAL O "ExceptInterrupt" NÃO FUNCIONA.

vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def leiaint():
    while True:
        try:
            n = int(input(f'{branco}Digite um número inteiro: '))
        except KeyboardInterrupt:
            print(f'\n{branco}Você digitou os números: {azul}0{branco} e {azul}0{branco}.')
        except:
            print(f'\n{vermelho}ESCREVA UM NÚMERO INTEIRO!')
        else:
            return n


def leiafloat():
    while True:
        try:
            n = float(input(f'{branco}Digite um número real: '))
        except KeyboardInterrupt:
            print(f'\n{branco}Você digitou os números: {azul}{inteiro}{branco} e {azul}0{branco}.')
        except:
            print(f'\n{vermelho}ESCREVA UM NÚMERO INTEIRO!')
        else:
            return n


def linha_():
    print(branco+'-' * 50)


def linha__():
    print(branco+'=' * 50)


linha__()
inteiro = leiaint()
real = leiafloat()
print(f'\n{branco}Você digitou os números: {azul}{inteiro}{branco} e {azul}{real}{branco}.')
linha__()
