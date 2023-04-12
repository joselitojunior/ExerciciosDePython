print('-' * 50)
qnt = 0
soma = 0
mais1000 = 0
barato = 0
nbarato = []
bqnt = 0

while True:
    qnt += 1
    nome = str(input(f'\033[1;97;45mNome do {qnt}º produto:\033[m ')).lower()
    preco = input('\033[1;97;42mPreço:\033[m \033[1;97mR$').replace(' ', '').replace('.', '').replace(',', '.')
    psp = preco.replace('.', '')
    precon = psp.isnumeric()
    preco = float(preco)
    while not precon:
        print('\n\033[1;31mPor favor, digite o preço corretamente.\033[m')
        preco = input('\033[1;97;42mPreço:\033[m \033[1;97mR$').replace(' ', '').replace('.', '').replace(',', '.')
        psp = preco.replace('.', '')
        precon = psp.isnumeric()
        preco = float(preco)

    soma += preco       # CALCULOS
    if preco > 1000:
        mais1000 += 1
    if qnt == 1:
        bqnt += 1
        barato = preco
        nbarato += [nome]
    else:
        if preco < barato:
            bqnt = 1
            barato = preco
            nbarato = []
            nbarato += [nome]
        elif preco == barato:
            bqnt += 1
            barato = preco
            nbarato += [nome]
    continuar = str(input('\n\033[1;32m[SIM] \033[1;97mpara continuar.'
                          '\n\033[1;31m[NÃO] \033[1;97mpara finalizar as compras.'
                          '\n> \033[m')).lower().replace(' ', '').replace('ã', 'a')
    while continuar != 'sim' and continuar != 'nao':
        print('\n\033[1;31mPor favor, informe uma opção válida!\033[m')
        continuar = str(input('\n\033[1;32m[SIM] \033[1;97mpara continuar.'
                              '\n\033[1;31m[NÃO] \033[1;97mpara finalizar as compras.'
                              '\n\n> \033[m')).lower().replace(' ', '').replace('ã', 'a')
    if continuar == 'nao':
        print('\n\033[1;97;42mCompras finalizadas!\033[m')
        print('-' * 50)
        break
    print('-' * 50)
soma = f'{soma:.2f}'
soma = str(soma).replace('.', ',')
print(f'\033[1;97mTotal: \033[1;34mR${soma}\033[1;97m.\033[m')
if mais1000 == 1:
    print(f'\033[1;34m{mais1000} \033[1;97mproduto custa mais de R$1.000,00\033[m')
else:
    print(f'\033[1;34m{mais1000} \033[1;97mprodutos custam mais de R$1.000,00\033[m')
if bqnt == 1:
    print(f'\033[1;97mO nome do produto mais barato é: \033[1;34m{nbarato[0].capitalize()}\033[1;97m.')
elif bqnt == 2:
    print(f'\033[1;97mO nome dos produtos mais baratos são:\033[1;97m ', end='')
    for nomes in range(0, bqnt):
        if nomes == bqnt - 1:
            print(f' \033[1;97me \033[1;34m{nbarato[nomes]}\033[1;97m.')
        else:
            print(f'\033[1;34m{nbarato[nomes].capitalize()}', end='')
else:
    print(f'\033[1;97mO nome dos produtos mais baratos são:\033[1;97m ', end='')
    for nomes in range(0, bqnt):
        if nomes == bqnt - 1:
            print(f' e \033[1;34m{nbarato[nomes]}\033[1;97m.')
        elif nomes == bqnt - 2:
            print(f'\033[1;34m{nbarato[nomes]}\033[1;97m', end='')
        elif nomes == 0:
            print(f'\033[1;34m{nbarato[nomes].capitalize()}\033[1;97m', end=', ')
        else:
            print(f'\033[1;34m{nbarato[nomes]}\033[1;97m', end=', ')
