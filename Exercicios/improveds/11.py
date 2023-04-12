from mdl.tudo import *

l = 0
a = 0
linha__()
while True:
    try:
        l = float(input(f'{branco}Digite em metros a largura da parede: ').replace('m', ''))
        a = float(input(f'{branco}Digite em metros a altura da parede: ').replace('m', ''))
    except:
        continue
    else:
        break
linha_()
print(f'{azul}Área da parede: {branco}{to_int(l * a)}m²\n'
      f'{verde}Quantidade de litros de tinta: {branco}{to_int((l * a) / 2)} litros')
linha__()
