preço = float(str(input('\033[1mDigite o preço do produto: R$\033[m')).strip().replace('.', '').replace(',', '.'))
cp1 = str(input('Digite se o pagamento é em \033[1;32m"dinheiro"\033[m, \033[33m"cheque"\033[m,\033[m ou no \033[1;35m'
                '"cartão"\033[m: ')).strip().replace('cartao', 'cartão')

if cp1 == 'cartão':
    cp2 = (input('Digite se é \033[1;32m"à vista"\033[m ou mencione a \033[1;36mquantidade\033[m de vezes \033[4mno'
                 ' cartão\033[m: ')).strip().replace('a vista', 'à vista')
    if cp2 == 'à vista':
        preçon = preço - (preço * (5/100))
    elif cp2.isnumeric() == True:
        cp2 = int(cp2)
        if cp2 == 1 or cp2 == 2:
            preçon = preço
        elif cp2 >= 3:
            preçon = preço + (preço * (20/100))
elif cp1 == 'dinheiro' or cp1 == 'cheque':
    preçon = preço - (preço * (10 / 100))

print(f'\nO valor total que deve ser pago é de: \033[0;32mR${preçon:.2f}\033[m')
