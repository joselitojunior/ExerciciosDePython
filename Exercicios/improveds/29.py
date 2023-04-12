from mdl.tudo import *

v = 0
linha__()
while True:
    try:
        v = float(input(f'{branco}Digite a velocidade do carro em km/h: ').lower().replace('km/h', ''))
    except:
        continue
    else:
        break
linha_()
if v > 80:
    resto = (v - 80) * 7
    print(f'{branco}O carro ultrapassou o limite e será multado em: {verde}{monetario(resto)}')
else:
    print(f'{verde}O carro não ultrapassou o limite e não será multado!')
linha__()
