num = list()
qnt = 0

print('-' * 50)
while True:
    qnt += 1
    n = int(input(f'\033[1;97mDigite o \033[4m{qnt}\033[m\033[1;97mº número:\033[m '))
    if n not in num:
        num.append(n)
    sair = str(input('\n\033[1;97;43mDeseja continuar?\033[m'
                     '\n\033[1;32m[SIM] \033[1;97mpara continuar'
                     '\n\033[1;31m[NÃO] \033[1;97mpara sair'
                     '\n\n> \033[m')).replace(' ', '').lower().replace('ã', 'a')
    while sair != 'sim' and sair != 'nao':
        print('-' * 50)
        sair = str(input('\033[1;97;41mPor favor, digite uma opção válida!\033[m'
                         '\n\033[1;97m> \033[m')).replace(' ', '').lower().replace('ã', 'a')
    if sair == 'nao':
        print(f'\n\033[1;32m{"Finalizado!":^50}\033[m')
        print('-' * 50)
        break
    elif sair == 'sim':
        print('-' * 50)
num.sort()
print(f'\033[1;97mOs números listados foram: \033[1;35m{num}\033[m')
print('-' * 50)
