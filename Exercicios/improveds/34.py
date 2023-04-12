from mdl.tudo import *

s = 0
linha__(80)
while True:
    try:
        s = float(input(f'{branco}Digite o seu salário: '))
    except:
        continue
    else:
        break
linha_(80)
if s > 1250:
    aumento = 10
    novo_s = s + (s * aumento / 100)
else:
    aumento = 15
    novo_s = s + (s * aumento / 100)
print(f'{branco}O salário de {monetario(s)} sofreu um aumento de {aumento}%, totalizando: {verde}{monetario(novo_s)}')
linha__(80)
