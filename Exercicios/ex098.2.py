from time import sleep
neg = 0

vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def linha_():
    print('\033[1;97m'+'-' * 50)


def linha__():
    print('\033[1;97m'+'=' * 50)


def contador(i, f, p):
    if p == 0:
        p = 1
    print(f'{branco}De {i} até {f}, de {p} em {p}:  ', end=f'{ciano}')

    if i <= f:
        f += 1
    else:
        f -= 1
        p *= -1
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.35)
    print()
    sleep(1)


def escreva(cor, txt):
    print(f'{cor}{txt:^50}')


linha__()
contador(i=1, f=10, p=1)
linha_()
contador(i=10, f=0, p=2)
linha__()

escreva(cor=azul, txt='Sua vez de personalizar a sequência:')
print('\033[1;97m')

while True:
    inicio = str(input(f'Início: '))
    if '-' in inicio:
        neg = 1
        inicio = inicio.replace('-', '', 1)
    if inicio.isnumeric():
        inicio = int(inicio)
        if neg == 1:
            inicio *= -1
        break
while True:
    fim = str(input(f'Fim: '))
    if '-' in fim:
        neg = 1
        fim = fim.replace('-', '', 1)
    if fim.isnumeric():
        fim = int(fim)
        if neg == 1:
            fim *= -1
        break
while True:
    passo = str(input(f'Passo: '))
    if '-' in passo:
        neg = 1
        passo = passo.replace('-', '', 1)
    if passo.isnumeric():
        passo = int(passo)
        break
linha_()

contador(i=inicio, f=fim, p=passo)
linha__()
