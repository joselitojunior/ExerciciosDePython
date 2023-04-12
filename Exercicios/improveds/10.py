from mdl.tudo import *

linha__()
while True:
    try:
        n = float(input(f'{branco}Digite o total de dinheiro: '))
    except:
        continue
    else:
        break
linha_()
print(f'{branco}Você pode comprar {verde}{n // 3.27} {branco}dólares'
      f' e restará(ão) {vermelho}{to_int(n % 3.27):.2f}{branco} reais!')
linha__()
