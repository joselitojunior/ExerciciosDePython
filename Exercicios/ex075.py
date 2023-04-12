lista = []
pares = []
qntp = 0
print('-' * 70)
for c in range(4):
    n = int(input(f'\033[1;97mDigite o {c + 1}º número: '))
    if n % 2 == 0:
        qntp += 1
        pares = pares + [n]
    lista = lista + [n]
tupla = tuple(lista)
print('\nOs números são:', end=' ')
for c in range(4):
    if c == 3:
        print(f' e \033[1;34m{tupla[c]}\033[1;97m.\033[m')
    elif c == 2:
        print(f'\033[1;34m{tupla[c]}\033[1;97m', end='')
    else:
        print(f'\033[1;34m{tupla[c]}\033[1;97m', end=', ')
if tupla.count(9) == 1:
    print(f'    \033[1;97m- O número \033[4m9\033[m\033[1;97m apareceu \033[1;34m{tupla.count(9)}\033[1;97m vez.')
else:
    print(f'    \033[1;97m- O número \033[4m9\033[m\033[1;97m apareceu \033[1;34m{tupla.count(9)}\033[1;97m vezes.')
if 3 in tupla:
    print(f'    \033[1;97m- O primeiro número \033[4m3\033[m\033[1;97m se encontra'
                            f' na \033[1;34m{tupla.index(3)}ª\033[1;97m posição.')
else:
    print(f'    \033[1;97m- Não foi listado nenhum número 3.\033[m')
if qntp == 1:
    print('    \033[1;97m- O número par foi:\033[m', end=' ')
    for c in range(1):
        print(f'\033[1;34m{pares[c]}\033[1;97m.')
elif qntp == 0:
    print(f'    \033[1;97m- Não foi listado nenhum número par.\033[m')
else:
    print('    \033[1;97m- Os números pares foram:\033[m', end=' ')
    for c in range(qntp):
        if c == qntp - 1:
            print(f' e \033[1;34m{pares[c]}\033[1;97m.')
        elif c == qntp - 2:
            print(f'\033[1;34m{pares[c]}\033[1;97m', end='')
        else:
            print(f'\033[1;34m{pares[c]}\033[1;97m', end=', ')
print('-' * 70)
