from mdl.tudo import *

p = 0
linha__()
while True:
    try:
        p = float(input(f'{branco}Digite o preço do produto: '))
    except:
        continue
    else:
        break
linha_()
print(f'{branco}O preço do produto com 5% de desconto é: {verde}R${p - (p * 5/100):.2f}')
linha__()
