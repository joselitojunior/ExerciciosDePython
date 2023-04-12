from mdl.tudo import *
from random import randint

n = 0
linha__()
while True:
    try:
        n = int(input(f'{branco}Digite um número de {verde}0{branco} á{verde} 5{branco}: '))
    except:
        continue
    else:
        if n < 0 or n > 5:
            continue
        else:
            break
linha_()
nc = randint(0, 5)
if nc == n:
    print(f'{verde}VOCÊ VENCEU!')
else:
    print(f'{vermelho}Você perdeu... tente novamente!')
linha__()
