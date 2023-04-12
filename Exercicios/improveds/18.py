from mdl.tudo import *
from math import cos, tan, sin, radians

a = 0
linha__()
while True:
    try:
        a = float(input(f'{branco}Digite o ângulo: '))
    except:
        continue
    else:
        break
linha_()
print(f'{azul}Seno: {branco}{sin(radians(a)):.2f}\n'
      f'{amarelo}Cosseno: {branco}{cos(radians(a)):.2f}\n'
      f'{vermelho}Tangente: {branco}{tan(radians(a)):.2f}')
linha__()
