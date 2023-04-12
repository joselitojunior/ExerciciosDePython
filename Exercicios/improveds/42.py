from mdl.tudo import *

lados = 1
ld = 0
tipo = ''

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
for pos, lado in enumerate(lista):
    if pos == 0:
        ld = lado
    else:
        if lado == ld:
            lados += 1
        ld = lado
if lista[0] + lista[1] > lista[2]:
    if lados == 1:
        tipo = 'ESCALENO'
    elif lados == 2:
        tipo = 'ISÓSCELES'
    elif lados == 3:
        tipo = 'EQUILÁTERO'
    print(f'{branco}É {verde}possível{branco} formar um triângulo com esses tamanhos!')
    print(f'{branco}Tipo: {azul}{tipo}{branco}.')
else:
    print(f'{vermelho}Não{branco} é possível formar um triângulo com esses tamanhos.')
linha__(55)
