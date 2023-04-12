from mdl.tudo import *

n = 0
linha__()
while True:
    try:
        n = float(input(f'{branco}Digite um número: '))
    except:
        continue
    else:
        break
linha_()
print(f'{verde}Dobro: {branco}{to_int(n * 2)}\n'
      f'{ciano}Triplo: {branco}{to_int(n * 3)}\n'
      f'{vermelho}Raiz quadrada: {branco}{to_int(n ** (1 / 2))}')
linha__()
