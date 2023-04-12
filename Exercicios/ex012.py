p = float(input('Preço do produto: R$'))

d = p * (5/100)
pn = p - d

print('O \033[4;32mnovo preço\033[m do produto é R${:.2f}.'.format(pn))
