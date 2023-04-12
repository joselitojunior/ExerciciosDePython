from mdl.tudo import *

lista = list()
casas = ['Unidade', 'Dezena', 'Centena', 'Milhar']
n = 0

linha__()
while True:
    try:
        n = int(input(f'{branco}Digite um número entre {verde}0{branco} e {vermelho}9999{branco}: ').strip())
    except:
        continue
    else:
        if n < 0 or n > 9999:
            continue
        else:
            linha_()
            break

for alg in str(n):
    lista.append(alg)
for pos, num in enumerate(reversed(lista)):
    print(f'{branco}{casas[pos]}: {ciano}{num}')

linha__()
