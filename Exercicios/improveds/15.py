from mdl.tudo import *

linha__()
while True:
    try:
        km = float(input(f'{branco}Digite a quantidade de KM rodado: '))
        d = int(input(f'{branco}Digite a quantidade de dias que têm estado com o carro: '))
    except:
        continue
    else:
        break
linha_()
print(f'{branco}Preço a ser pago: {verde}R${(d * 60) + (km * 0.15):.2f}')
linha__()
