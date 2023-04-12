from mdl.tudo import *

lista = list()
linha__()
for c in range(2):
    while True:
        try:
            lista.append(int(input(f'{branco}Digite o {c + 1}º número inteiro: ')))
        except:
            continue
        else:
            break
linha_()
if lista[0] > lista[1]:
    print(f'{branco}O {amarelo}primeiro valor{branco} é {azul}maior{branco}!')
elif lista[0] < lista[1]:
    print(f'{branco}O {amarelo}segundo valor{branco} é {azul}maior{branco}!')
elif lista[0] == lista[1]:
    print(f'{amarelo}Não existe{branco} valor maior, os dois são {azul}iguais.')
linha__()
