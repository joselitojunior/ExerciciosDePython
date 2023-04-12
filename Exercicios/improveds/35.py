from mdl.tudo import *

lista = list()
linha__(55)
for c in range(1, 4):
    while True:
        try:
            lista.append(float(input(f'{branco}Digite o tamanho do {c}º lado do triângulo: ')))
        except:
            continue
        else:
            break
linha_(55)
lista.sort()
if lista[0] + lista[1] > lista[2]:
    print(f'{branco}É {verde}possível{branco} formar um triângulo com esses tamanhos!')
else:
    print(f'{vermelho}Não{branco} é possível formar um triângulo com esses tamanhos.')
linha__(55)
