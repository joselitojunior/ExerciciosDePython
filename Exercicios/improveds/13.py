from mdl.tudo import *

linha__()
while True:
    try:
        s = float(input(f'{branco}Digite o salário: '))
    except:
        continue
    else:
        break
linha_()
print(f'\n{branco}O salário com aumento de 15% é: {verde}R${s + (s * 15/100):.2f}')
linha__()
