from mdl.tudo import *

linha__()
while True:
    try:
        n1 = float(input(f'{branco}Digite um número: '))
        n2 = float(input(f'{branco}Digite outro número: '))
    except:
        continue
    else:
        break
linha_()
total = to_int(n1 + n2)
print(total)
linha__()
