from mdl.tudo import *

d = 0
linha__()
while True:
    try:
        d = float(input(f'{branco}Digite a distância da viagem (em KM): ').lower().replace('km', ''))
    except:
        continue
    else:
        break
linha_()
if d > 200:
    valor = d * 0.45
else:
    valor = d * 0.5
print(f'{branco}O valor total pela viagem é: {verde}{monetario(valor)}')
linha__()
