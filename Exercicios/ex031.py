from math import trunc
d = float(str(input('Qual a distância da viagem em km/h? ')).strip().replace('km/h', ''))
dt = trunc(d)

if dt < 200:
    preço = dt * 0.5
    print('O preço da passagem é \033[0;31mR${:.2f}\033[m'.format(preço))
else:
    preço2 = dt * 0.45
    print(f'O preço da sua passagem é \033[0;31mR${preço2:.2f}\033[m')
