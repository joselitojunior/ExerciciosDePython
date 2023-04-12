from mdl.tudo import *

n = 0
linha__()
while True:
    try:
        n = float(input(f'{branco}Digite um número real: '))
    except:
        continue
    else:
        break
linha_()
print(f'\n{branco}O número {azul}{to_int(n)}{branco} tem a parte inteira: {azul}{int(n)}')
linha__()
