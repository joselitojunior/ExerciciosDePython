vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
branco = '\033[1;97m'


def fatorial(numero=1, show=False):
    '''

    :param numero: O número a ser calculado.
    :param show: Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    if show and numero != 1:
        print(f'{branco}{numero}! -> {numero} x ', end='')
        for c in range(numero - 1, 0, -1):
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
            numero *= c
        return numero
    elif show == False or numero == 1:
        print(f'{branco}{numero}! = ', end='')
        for c in range(numero - 1, 0, -1):
            numero *= c
        return numero


print(branco+'=' * 50)
n = int(input(f'{branco}Digite um número para ser fatorado: '))
while True:
    sh = str(input(f'\n{branco}Deseja ver o processo de fatoramento?\n{verde}[S]{branco} para "sim"'
                   f'\n{vermelho}[N]{branco} para "não"\n>')).lower().strip()
    if sh == 's':
        sh = True
        break
    elif sh == 'n':
        sh = False
        break
print(branco+'=' * 50)
print()
print(branco+'=' * 50)
resp = fatorial(numero=n, show=sh)
print(resp)
print(branco+'=' * 50)
