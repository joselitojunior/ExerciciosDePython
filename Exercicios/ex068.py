from random import randint
from math import trunc
print('-' * 50)
v = 0
while True:
    pi = str(input('\033[1;32mPAR \033[1;97mou \033[1;31mÍM'
                   'PAR\033[1;97m?\033[m ')).lower().replace(' ', '').replace('í', 'i')
    if pi == 'par' or pi == 'impar':
        n = -1
        while n < 0 or n > 10:
            n = float(input('\033[1;97mEscolha um número de \033[1;35m0 à 10\033[1;97m: '))
        n = trunc(n)
        nc = randint(0, 10)
        total = n + nc
        print(f'''\n\033[1;97mVocê: \033[1;35m{n}
\033[1;97mComputador: \033[1;35m{nc}\033[m\n''')
        if pi == 'par' and total % 2 == 0:
            v += 1
            print(f'\033[1;97mVOCÊ ACERTOU! O NÚMERO'
                  f' \033[1;35m{total} \033[1;97mÉ \033[1;32m{pi.upper()}\033[1;97m!')
            print('-' * 50)
        elif pi == 'impar' and total % 2 != 0:
            v += 1
            print(f'\033[1;97mVOCÊ ACERTOU! O NÚMERO'
                  f' \033[1;35m{total} \033[1;97mÉ \033[1;31m{pi.upper()}\033[1;97m!')
            print('-' * 50)
        else:
            print(f'\033[1;31mVocê perdeu... {total} não é {pi} :(\033[m')
            if v == 1:
                print(f'\033[1;97mVocê teve um total de \033[1;32m{v} vitória consecutiva\033[1;97m!\033[m')
            elif v > 1:
                print(f'\033[1;97mVocê teve um total de \033[1;32m{v} vitórias consecutivas\033[1;97m!\033[m')
            print('-' * 50)
            break
    else:
        print('\n\033[1;31mOpção inválida!\033[m\n')
