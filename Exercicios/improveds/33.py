from mdl.tudo import *

lista = list()
linha__()
for c in range(3):
    while True:
        try:
            lista.append(float(input(f'{branco}Digite o {c + 1}º número: ')))
        except:
            continue
        else:
            break
linha_()
print(f'{branco}Menor número: {ciano}{to_int(min(lista))}\n'
      f'{branco}Maior número: {roxo}{to_int(max(lista))}')
linha__()
