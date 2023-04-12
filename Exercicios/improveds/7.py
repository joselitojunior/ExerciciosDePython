from mdl.tudo import *

linha__()
while True:
    try:
        n1 = float(input(f'{branco}Digite a 1ª nota: '))
    except:
        continue
    else:
        break
while True:
    try:
        n2 = float(input(f'{branco}Digite a 2ª nota: '))
    except:
        continue
    else:
        break
linha_()
print(f'{branco}A {verde}média{branco} do aluno é: {verde}{to_int((n1 + n2) / 2)}')
linha__()
