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
print(f'{vermelho}Antecessor: {branco}{n - 1}\n'
      f'{verde}Sucessor: {branco}{n + 1}')
linha__()
