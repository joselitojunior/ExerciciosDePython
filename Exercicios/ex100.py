from random import randint
from time import sleep

numeros = list()


def sorteia():
    for c in range(5):
        numeros.append(randint(1, 10))


def somaPar():
    global soma
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n


print('\033[1;97m'+'=' * 50)
sorteia()
print(f'Números sorteados:', end=' \033[1;34m')
for valor in numeros:
    print(f'{valor}', end=' ')
    sleep(0.37)
print()
somaPar()
print(f'\033[1;97mSoma dos PARES: \033[1;32m{soma}')
print('\033[1;97m'+'=' * 50)
