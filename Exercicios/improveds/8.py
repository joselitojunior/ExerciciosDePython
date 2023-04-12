from mdl.tudo import *

linha__()
while True:
    try:
        n = float(input(f'{branco}Digite um valor em metros: ').lower().replace('metros', '').replace('m', ''))
    except:
        continue
    else:
        break
linha_()
print(f'{amarelo}Centímetros: {branco}{to_int(n * 100)}\n'
      f'{azul}Milímetros: {branco}{to_int(n * 1000)}')
linha__()
