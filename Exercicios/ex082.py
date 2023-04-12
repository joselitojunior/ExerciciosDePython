lista = list()
listap = list()
listai = list()
run = 'continuar'
qnt = 0
neg = 0

print('\033[1;97m=' * 50)
print('\033[31mOBS: \033[97mDIGITE "\033[31msair\033[97m" PARA FINALIZAR O PROGRAMA')
print('\033[1;97m=' * 50, '\n')

while run == 'continuar':
    while True:
        qnt += 1
        n = input(f'\033[1;97mDigíte o \033[34m{qnt}º\033[97m número: ')
        if n[0] == '-':
            neg = 1
            n = n.replace('-', '', 1)
        if n.isnumeric():
            n = int(n)
            if neg == 1:
                neg = 0
                n = n * -1
            lista.append(n)
            break
        elif n == 'sair':
            run = 'sair'
            print('\n'+'\033[1;97m=' * 50)
            break
        else:
            print('\n\033[1;31mINFORME UM VALOR CORRETO!\033[m\n')
            qnt -= 1

print(f'\033[1;97mNúmeros: \033[34m', end='')
t = len(lista)
for c in range(0, t):
    if c == t - 2:
        print(lista[c], end=' \033[97me\033[34m ')
    elif c == t - 1:
        print(f'{lista[c]}\033[97m.')
    else:
        print(lista[c], end='\033[97m,\033[34m ')
    if lista[c] % 2 == 0:
        listap.append(lista[c])
    else:
        listai.append(lista[c])
tp = len(listap)
ti = len(listai)
print(f'\033[1;97mNúmeros pares: \033[34m', end='')
for c in range(0, tp):
    if c == tp - 2:
        print(listap[c], end=' \033[97me\033[34m ')
    elif c == tp - 1:
        print(f'{listap[c]}\033[97m.')
    else:
        print(listap[c], end='\033[97m,\033[34m ')
print(f'\033[1;97mNúmeros ímpares: \033[34m', end='')
for c in range(0, ti):
    if c == ti - 2:
        print(listai[c], end=' \033[97me\033[34m ')
    elif c == ti - 1:
        print(f'{listai[c]}\033[97m.')
    else:
        print(listai[c], end='\033[97m,\033[34m ')
print('\033[1;97m=' * 50)
