from mdl.tudo import *

n = 0
linha__()
while True:
    try:
        n = int(input(f'{branco}Digite um número inteiro: '))
    except:
        continue
    else:
        break
linha_()
if n % 2 == 0:
    print(f'{branco}O número {azul}{n}{branco} é {verde}par{branco}!')
else:
    print(f'{branco}O número {azul}{n}{branco} é {vermelho}ímpar{branco}!')
linha__()
