co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é \033[7;35m{:.2f}\033[m.'.format(h))
