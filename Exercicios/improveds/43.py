from mdl.tudo import *

peso = 0
altura = 0
linha__()
while True:
    try:
        peso = float(input(f'{branco}Digite seu peso: '))
    except:
        continue
    else:
        break
while True:
    try:
        altura = float(input(f'{branco}Digite sua altura: '))
    except:
        continue
    else:
        break
linha_()
imc = peso / altura ** 2
print(f'{branco}IMC: {azul}{to_int(imc, 1)}\n'
      f'{branco}Situação: ', end='')
if imc < 18.5:
    print(f'{vermelho}ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print(f'{verde}PESO IDEAL')
elif 25 < imc <= 30:
    print(f'{amarelo}SOBREPESO')
elif 30 < imc <= 40:
    print(f'{vermelho}OBESIDADE')
elif imc > 40:
    print(f'{vermelho}OBESIDADE MÓRBIDA')
linha__()
