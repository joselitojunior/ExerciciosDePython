pt = int(float(input('Digite o primeiro termo da \033[0;33mPA\033[m: ')))
r = int(float(input('Digite a razão da \033[0;33mPA\033[m: ')))
termos = -1
qnt = 0

while termos != 0:
    print('')
    if qnt == 0:
        decimo = pt + (10 - 1) * r
    if qnt > 0:
        decimo = pt + (termos - 1) * r
    if r > 0:
        while pt <= decimo:
            print(f'\033[1;33m{pt}\033[m')
            pt = pt + r
    if r < 0:
        while pt >= decimo:
            print(f'\033[1;33m{pt}\033[m')
            pt = pt + r
    if r == 0:
        if qnt == 0:
            for r0 in range(1, 11):
                print(f'\033[1;33m{pt}\033[m')
        if qnt > 0:
            for r0 in range(1, termos + 1):
                print(f'\033[1;33m{pt}\033[m')
    qnt += 1
    termos = -1
    while termos < 0:
        termos = int(float(input('\n\033[1;97mDigite a quantidade de termos a mais que você deseja ver:\033[m ')))
        if termos < 0:
            print('\n\033[1;31mDigite um número maior ou igual à \033[1;4m0\033[m\033[1;31m!\033[m')
    if termos == 0:
        print('\n\033[1;32mFinalizado!\033[m')

