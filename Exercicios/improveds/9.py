from mdl.tudo import *

linha__()
while True:
    try:
        n = int(input(f'{branco}Digite um número inteiro: '))
    except:
        continue
    else:
        break
linha_()
for c in range(0, 11):
    print(f'{branco}{n} x {c} = {roxo}{n * c}')
linha__()
