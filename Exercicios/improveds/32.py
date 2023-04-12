from mdl.tudo import *

ano = 0
linha__()
print(f'{azul}{"ESTE ANO É BISSEXTO?":^50}')
linha__()
while True:
    try:
        ano = int(input(f'{branco}> '))
    except:
        continue
    else:
        break
linha_()
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{verde}O ano {ano} é bissexto!')
else:
    print(f'{vermelho}O ano {ano} não é bissexto...')
linha__()
