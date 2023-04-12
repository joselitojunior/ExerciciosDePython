d = float(input('Quanto de dinheiro você tem? R$'))

div = d / 3.27

print('Você pode comprar: \033[1;32mUS${:.2f}\033[m!'.format(div))
