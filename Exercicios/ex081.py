lista = list()
stop = 'continuar'
qnt = 0
neg = 0
print('\033[1;97m=\033[m' * 50)
print('\033[1;31mOBS:\033[97m DIGITE "\033[1;31msair\033[97m" PARA FINALIZAR O PROGRAMA.')
print('\033[1;97m=\033[m' * 50, '\n')
while stop == 'continuar':
    while True:
        qnt += 1
        n = input(f'\033[1;97mDigíte o \033[1;34m{qnt}º\033[1;97m número:\033[m ').lower()
        if len(n) != 0:
            if '-' in n[0]:
                n = n.replace('-', '', 1)
                neg = 1
        if n.isnumeric() == True:
            if neg == 1:
                neg = 0
                n = '-' + n
            n = int(n)
            if qnt == 1 or n > lista[0]:
                lista.insert(0, n)
            else:
                pos = len(lista) - 1
                while pos >= 0:
                    if n <= lista[pos]:
                        lista.insert(pos + 1, n)
                        break
                    pos -= 1
        elif n == 'sair':
            print('\n'+'\033[1;97m=\033[m' * 50,)
            stop = 'sair'
            break
        else:
            print('\n\033[1;31mINFORME UM VALOR CORRETO!\033[m\n')
            qnt -= 1

tamanho = len(lista)
print(f'\033[1;97mQuantidade de números: \033[34m{tamanho}')
print('\033[1;97mA lista em ordem decrescente:\033[34m ', end='')
for c in range(0, len(lista)):
    if c == len(lista) - 1:
        print(f'{lista[c]}.')
    else:
        print(lista[c], end='\033[97m,\033[34m ')
print('\033[1;97mO número "\033[34m5\033[97m" ', end='')
if 5 in lista:
    print('\033[1;32mestá\033[97m na lista!')
else:
    print('\033[1;31mnão está\033[97m na lista.')
print('\033[1;97m=\033[m' * 50)
