from math import trunc
menu = '4'
maior = 0
while menu == '4':
    v1str = str(input('\033[1;97mDigite o PRIMEIRO valor: \033[m')).strip()
    v2str = str(input('\033[1;97mDigite o SEGUNDO valor: \033[m')).strip()
    v1 = float(str(v1str).replace('.', '').replace(',', '.'))
    v2 = float(str(v2str).replace('.', '').replace(',', '.'))
    if v1 == trunc(v1):
        v1 = int(v1)
    if v2 == trunc(v2):
        v2 = int(v2)
    soma = v1 + v2
    mult = v1 * v2
    if soma == trunc(soma):
        soma = int(soma)
    else:
        soma = str(soma).replace('.', ',')
    if mult == trunc(mult):
        mult = int(mult)
    else:
        mult = str(mult).replace('.', ',')
    if v1 > v2:
        maior = f'\033[1;97mO maior é número é: \033[1;32m{v1}\033[m'
    elif v1 < v2:
        maior = f'\033[1;97mO maior é número é: \033[1;32m{v2}\033[m'
    elif v1 == v2:
        maior = f'\033[1;97mOs dois números são iguais: \033[1;32m{v2}\033[m'
    menu = str(input('\n\033[1;97mEscolha uma operação ou opção:'
                     '\n\033[1;32m[1]\033[m\033[1;97m SOMAR'
                     '\n\033[1;35m[2]\033[m\033[1;97m MULTIPLICAR'
                     '\n\033[1;36m[3]\033[m\033[1;97m MAIOR VALOR'
                     '\n\n\033[1;33m[4]\033[m\033[1;97m NOVOS VALORES'
                     '\n\033[1;31m[5]\033[m\033[1;97m SAIR DO PROGRAMA'
                     '\n\n> \033[m'))
    while menu != '1' and menu != '2' and menu != '3' and menu != '4' and menu != '5':
        print('')
        print('\033[1;31mEscolha uma opção válida!\033[m')
        menu = str(input('\033[1;97m> \033[m'))
    if menu == '1':
        print(f'\033[1;97mA soma entre {v1str} e {v2str} é: \033[1;32m{soma}\033[m')
    elif menu == '2':
        print(f'\033[1;97mA multiplicação entre {v1str} e {v2str} é: \033[1;32m{mult}\033[m')
    elif menu == '3':
        print(maior)
    elif menu == '5':
        print(f'\033[1;97mFinalizado!\033[m')
    if menu == '4':
        print('')
    if menu == '1' or menu == '2' or menu == '3':
        menu = str(input('\n\033[1;33m[4]\033[m\033[1;97m NOVOS VALORES'
                         '\n\033[1;31m[5]\033[m\033[1;97m SAIR DO PROGRAMA'
                         '\n\n> \033[m'))
        while menu != '1' and menu != '2' and menu != '3' and menu != '4' and menu != '5':
            print('')
            print('\033[1;31mEscolha uma opção válida!\033[m')
            menu = str(input('\033[1;97m> \033[m'))
        if menu == '5':
            print(f'\033[1;97mFinalizado!\033[m')
