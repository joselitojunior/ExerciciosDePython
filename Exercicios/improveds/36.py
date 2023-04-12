from mdl.tudo import *

valor = 0
s = 0
anos = 0
linha__(85)
while True:
    try:
        valor = float(input(f'{branco}Digite o valor da {amarelo}casa{branco}: '))
    except:
        continue
    else:
        break
while True:
    try:
        s = float(input(f'{branco}Digite o valor do seu {verde}salário{branco}: '))
    except:
        continue
    else:
        break
while True:
    try:
        anos = int(input(f'{branco}Digite a quantidade de {roxo}anos{branco} para o pagamento: '))
    except:
        continue
    else:
        break
linha_(85)
por_mes = valor / (12 * anos)
if por_mes > s * 30 / 100:
    porc = round((100 * por_mes) / s - 30, 2)
    print(f'{vermelho}EMPRÉSTIMO NEGADO! {branco}A prestação excedeu {vermelho}{porc}%{branco}!')
else:
    print(f'{verde}EMPRÉSTIMO ACEITO!'
          f' {branco}Você vai pagar uma prestação no valor de {verde}{monetario(por_mes)}{branco} por mês!')
linha__(85)
