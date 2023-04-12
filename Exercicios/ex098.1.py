from time import sleep

vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def processo(n):
    nn = n
    while True:
        neg = 0
        n = str(input(f'{nn}: '))
        if '-' in n:
            neg = 1
            n = n.replace('-', '', 1)
        if n.isnumeric():
            n = int(n)
            if neg == 1:
                if nn != 'Passo':
                    n *= -1
            break
    return n


def linha_():
    print('\033[1;97m'+'-' * 50)


def linha__():
    print('\033[1;97m'+'=' * 50)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'{branco}De {inicio} até {fim}, de {passo} em {passo}:  ', end=f'{ciano}')

    if inicio <= fim:
        fim += 1
    else:
        fim -= 1
        passo *= -1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.35)
    print()
    sleep(1)


def escreva(cor, txt):
    print(f'{cor}{txt:^50}')


linha__()
contador(inicio=1, fim=10, passo=1)
linha_()
contador(inicio=10, fim=0, passo=2)
linha__()

escreva(cor=azul, txt='Sua vez de personalizar a sequência:')
print('\033[1;97m')
inicio = (processo('Inicio'))
fim = processo('Fim')
passo = processo('Passo')
linha_()
contador(inicio=inicio, fim=fim, passo=passo)
linha__()
