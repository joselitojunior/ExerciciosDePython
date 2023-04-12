from mdl.tudo import *

linha__()
while True:
    try:
        c1 = float(input(f'{branco}Digite o comprimento do cateto oposto: '))
        c2 = float(input(f'{branco}Digite o comprimento do cateto adjacente: '))
    except:
        continue
    else:
        break
linha_()
print(f'{branco}O comprimento da hipotenusa é: {azul}{((c1 ** 2) + (c2 ** 2)) ** (1 / 2):.2f}')
linha__()
